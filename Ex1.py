from datetime import date
today = date.today()
a = int(input("Nhập năm sinh của bạn = "))
d1 = int(today.strftime("%Y"))
if a > d1:
    print("Bạn nhập đúng năm sinh chưa ?")
else:
    b = d1 - a
    print("Số tuổi của bạn là ", b, "tuổi")
print("Ngày hôm nay là ngày ", today.strftime("%d-%m-%Y"))