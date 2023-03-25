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

# Lấy danh sách tất cả các file ảnh trong thư mục
img_files = os.listdir(img_dir)

# Lặp qua từng file ảnh để đọc và xử lý
for img_file in img_files:
    # Lấy mã số sinh viên từ tên file ảnh
    mssv = img_file.split(".")[0]

    # Đọc ảnh và resize về kích thước 1080x2040
    img_path = os.path.join(img_dir, img_file)
    img = cv2.imread(img_path)
    img = cv2.resize(img, (924, 1080))

    # Chuyển ảnh sang grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Xác định khuôn mặt trong ảnh
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Lặp qua từng khuôn mặt để vẽ hộp giới hạn và in thông tin sinh viên
    for (x, y, w, h) in faces:
        # Vẽ hộp giới hạn quanh khuôn mặt
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Lấy thông tin sinh viên từ file excel
        df['MSSV'] = df['MSSV'].astype(str)
        sv_info = df.loc[df["MSSV"] == mssv]

        # In thông tin sinh viên lên ảnh
        if not sv_info.empty:
            ten = sv_info["Họ và tên"].iloc[0]
            cv2.putText(img, "MSSV: {}".format(mssv), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            cv2.putText(img, "Họ và tên: {}".format(ten), (x, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
cv2.imshow("Sinh vien {}".format(mssv), img)
cv2.waitKey(0)
cv2.destroyAllWindows()
