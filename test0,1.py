import pandas as pd
import os

# Đường dẫn đến thư mục chứa ảnh sinh viên
image_folder = "path/to/image/folder"

# Đường dẫn đến tệp Excel chứa thông tin sinh viên
excel_file = "path/to/excel/file.xlsx"

# Lấy danh sách tất cả các tệp ảnh có định dạng là .jpg trong thư mục
image_files = [f for f in os.listdir(image_folder) if f.endswith(".jpg")]

# Đọc tệp Excel và lưu thông tin vào DataFrame
df = pd.read_excel(excel_file)

# Duyệt qua từng tệp ảnh và lấy MSSV từ tên ảnh để tìm kiếm thông tin sinh viên tương ứng trong Excel
for image_file in image_files:
    # Lấy MSSV từ tên ảnh
    mssv = os.path.splitext(image_file)[0]
    # Tìm kiếm thông tin sinh viên với MSSV được lấy từ tên ảnh
    df['MSSV'] = df['MSSV'].astype(str)
    student_info = df.loc[df['MSSV'] == mssv]
    # Nếu tìm thấy thông tin sinh viên
    if not student_info.empty:
        # Lấy tên của sinh viên
        name = student_info.iloc[0]['Họ và tên']
        # Xuất thông tin của sinh viên ra màn hình
        print(f"MSSV: {mssv}\nName: {name}")
    else:
        # Nếu không tìm thấy thông tin sinh viên, xuất thông báo lỗi ra màn hình
        print(f"Cannot find student with MSSV {mssv}")
