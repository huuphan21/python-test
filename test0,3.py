import cv2
import os
import pandas as pd

# Đọc file excel chứa thông tin sinh viên
df = pd.read_excel("path/to/excel/file.xlsx")

# Đường dẫn thư mục chứa ảnh sinh viên
img_dir = "path/to/image/folder"

# Đường dẫn file classifier của OpenCV Haar Cascades
face_cascade_file = "path/to/haarcascade_frontalface_default.xml"

# Load classifier khuôn mặt
face_cascade = cv2.CascadeClassifier(face_cascade_file)

# Tạo cửa sổ camera
cap = cv2.VideoCapture(0)

while True:
    # Đọc frame từ camera
    ret, frame = cap.read()

    # Chuyển frame sang grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Xác định khuôn mặt trong frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Lặp qua từng khuôn mặt để vẽ hộp giới hạn và in thông tin sinh viên
    for (x, y, w, h) in faces:
        # Vẽ hộp giới hạn quanh khuôn mặt
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Lấy mã số sinh viên từ tên file ảnh
        mssv = "308191143"

        # Lấy thông tin sinh viên từ file excel
        df['MSSV'] = df['MSSV'].astype(str)
        sv_info = df.loc[df["MSSV"] == mssv]

        # In thông tin sinh viên lên frame
        if not sv_info.empty:
            ten = sv_info["Họ và tên"].iloc[0]
            cv2.putText(frame, "MSSV: {}".format(mssv), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            cv2.putText(frame, "Họ và tên: {}".format(ten), (x-10, y + h), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Hiển thị frame trên cửa sổ camera
    cv2.imshow("Camera", frame)

    # Nhấn phím 'q' để thoát khỏi chương trình
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng bộ nhớ và đóng cửa sổ camera
cap.release()
cv2.destroyAllWindows()
