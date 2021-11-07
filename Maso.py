import random
print("--------------------------------------------------------------------------------")
first_names=['Cường Lee',
'Đăng Hải',
'Giang Hoàng Vũ Trường',
'Le Duy Khiem',
'Lê Nguyên Võ',
'Nguyễn Mai Tiên',
'Nguyễn Thanh Trung',
'Phung Thi Thuy Trang',
'Tĩnh Bùi Quốc',
'Tran Nguyen Huy Truong',
'việt đỗ',
'Vy Huỳnh']
last_names = ['Sói nguyền', 'Sói thường 1', 'Sói thường 2', 'Bán sói', 'Phù thủy', 'Bảo vệ', 'Tiên tri', 'Dân', 'Già làng', 'Thợ săm', 'Thần tình yêu', 'Bảo vệ']
for num in range(100):
    first = random.choice(first_names)
    last = random.choice(last_names)
    print(f'{first} - {last}\n')
