#input:
# Só lượng phiếu đăng ký, kiểu chữ Int
# chuỗi thông tin thô của từng phần: Họ tên , tên khóa học, mã học viên, email
#output:
#Thông báo lỗi cụ thể nếu dữ liệu vi phạm quy định
# hiển thị thông tin sạch kềm mã xác nhận tự động

## Giải pháp xử lý:
#Tách chuỗi bằng dấu gạch đứng | và xóa khoảng trắng ở hai đầu bằng phương thức .split() và .strip()

#định dạng lại chữ: viết hoa chữ cái đầu cho Họ tên và Khóa hoc, viết hoa toàn bộ cho mã học viên, viết thường toàn bộ cho email.
#sinh mã xác nhận bằng cách chuyển tên khóa học thành chữ in hoa và thay khoảng trắng bằng dấu gạch ngang



#Thiết kế thuật toán: 
"""
B1:Nhập số lượng phiếu đăng ký
B2: Kiểm tra bẫy dữ liêu 1:
    Nếu số lượng phiếu nhỏ hơn hoặc bằng 0:
        in thông báo: "Số lượng phiếu đăng ký không hợp lệ"
        kết thúc chương trình

B3: chạy vòng lặp duyệt qua từng phiếu đăng ký:
    Nhập chuỗi thông tin của phiếu hiện tại
    Tách chuỗii vừa nhập bằng dấu gạch đứng
    Kiểm tra bẫy dữ liệu 2:
        Nếu sau khi tách không đủ 4 phần tử:
            in thông báo: "Dữ liệu đăng ký ko hợp lệ. Bỏ qua phiếu này
            Bỏ qua phiếu hiện tại, chuyển sang phiếu tiếp theo.

    Thực hiện xóa khoảng trắng và chuẩn hóa kiểu chữ cho từng trường thông tin.
    Kiểm tra bẫy dữ liệu 3:
        Nếu trường hợp Email không có ký tự @:
            in thông báo: "Email không hợp lệ. Bỏ qua phiếu này"
            Bỏ qua phiếu hiện tại, chuyển sang phiếu tiếp theo.

    Kiểm tra bẫy dữ liệu 4:
        Nếu độ dài của Mã học viên nhỏ hơn 5 ký tự:
            in thông báo: "Mã học viên không hợp lệ. Bỏ qua phiếu này."
            Bỏ qua phiếu hiện tại, chuyển sang phiếu tiếp theo.

    Ghép mã học viên và tên khóa học để tự động sinh ra mã xác nhận
    In thông tin phiếu đã chuẩn hóa ra màn hình theo đúng biểu mẫu yêu cầu.

B4: kết thúc chương trình sau khi duyệt hết số lượng phiếu đã nhập.
"""

import email


so_Luong_phieu = int(input("Nhập số lượng phiếu đăng ký cần xử lý: "))

if so_Luong_phieu <= 0:
    print("Số lượng phiếu đăng ký không hợp lệ!")
else:
    print("-" * 50)

    for i in range(so_Luong_phieu):
        chuoi_nhap_vao = input(f"Nhập thông tin phiếu thứ {i+1}: ")

        cac_thanh_phan = []
        for item in chuoi_nhap_vao.split('|'):
            cac_thanh_phan.append(item.strip())

        if len(cac_thanh_phan) != 4:
            print("Dự liệu đăng ký không hợp lệ. Bot qua phiếu này!")
            print("-" * 50)
            continue

        ho_ten_raw = cac_thanh_phan[0]
        ten_khoa_raw = cac_thanh_phan[1]
        ma_hoc_vien_raw = cac_thanh_phan[2]
        email_raw = cac_thanh_phan[3]

        ho_ten = " ".join(ho_ten_raw.split()).title()
        ten_khoa = " ".join(ten_khoa_raw.split()).title()
        ma_hoc_vien = ma_hoc_vien_raw.upper()
        email = email_raw.lower()

        if '@' not in email:
            print("Email không hợp lệ. Bỏ qua phiếu này!")
            print("-" * 50)
            continue

        if len(ma_hoc_vien) < 5:
            print("Mã học viên không hợp lệ. Bỏ qua phiếu này!")
            print("-" * 50)
            continue

        ten_khoa_viet_hoa = ten_khoa.upper().replace(" ", "-")
        ma_xac_nhan = ma_hoc_vien + "_" + ten_khoa_viet_hoa


        print("\n===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====")
        print(f"Học viên: {ho_ten}")
        print(f"Khóa học: {ten_khoa}")
        print(f"Mã học viên: {ma_hoc_vien}")
        print(f"Email: {email}")
        print(f"Mã xác nhận: {ma_xac_nhan}")
        print("-" * 50)