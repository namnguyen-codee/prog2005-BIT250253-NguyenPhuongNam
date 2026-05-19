#Bài 1
# Khai báo biến
so_nguyen = 99
so_thuc = 1.99
chuoi = "Xin chào Python"

# In ra màn hình
print("Số nguyên:", so_nguyen)
print("Số thực:", so_thuc)
print("Chuỗi:", chuoi)

#Bài 2
# Khai báo hằng số PI và bán kính
PI = 3.14
r = 7

# Tính chu vi
chu_vi = 2 * PI * r

# In kết quả
print("Chu vi hình tròn là:", chu_vi)

#Bài 3
# Nhập hai số nguyên từ bàn phím
a = 1
b = 4

# Tính toán
tong = a + b
hieu = a - b
tich = a * b
thuong = a / b

# In kết quả
print("Tổng =", tong)
print("Hiệu =", hieu)
print("Tích =", tich)
print("Thương =", thuong)

#Bài 4
# Định nghĩa hàm
def sum_two_numbers(a, b):
    return a + b

# Gọi hàm
ket_qua = sum_two_numbers(5, 7)

# In kết quả
print("Tổng hai số là:", ket_qua)

#Bài 5
# Khai báo biến
name = "Nam"
age = 19
average_score = 9.0

# Hiển thị kiểu dữ liệu
print("Kiểu dữ liệu của name:", type(name))
print("Kiểu dữ liệu của age:", type(age))
print("Kiểu dữ liệu của average_score:", type(average_score))

# Xử lý dữ liệu
age_next_year = age + 1
doubled_score = average_score * 2

# In thông tin
print("Tên:", name)
print("Tuổi hiện tại:", age)
print("Tuổi năm sau:", age_next_year)

print("Điểm trung bình:", average_score)
print("Điểm sau khi nhân đôi:", doubled_score)

# In kiểu dữ liệu của biến mới
print("Kiểu dữ liệu của age_next_year:", type(age_next_year))
print("Kiểu dữ liệu của doubled_score:", type(doubled_score))
