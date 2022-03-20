import socket
import cmath

# Hàm này nhận một line từ server
def get_line(createdSocket):
    inputByte = b''
    while True:
        userInputByte = createdSocket.recv(1)
        if userInputByte == b'\n':
            break
        inputByte = inputByte + userInputByte

    # Trả về kết quả dạng string
    return inputByte.decode()


# Hàm sử dụng get_line để nhận tới khi gặp 1 line định trước
def receive_until(string, sock):
    received = ""
    while True:
        line = get_line(sock)
        received += line + "\n"
        if line == string or "Flag" in line:
            break
    return received


# Gửi 1 string tới server
def send_line(createdSocket, data):
    # Bỏ hết ký tự xuống dòng trong data (nếu có) và gửi đến server
    data = data.strip()
    createdSocket.send((data + '\n').encode())


# Ham nay giai bai toan
# |||||||||||||||||||||||||||||||||||||||||||||||||
# |||Người chơi điền code giải và return kết quả|||
# |||||||||||||||||||||||||||||||||||||||||||||||||
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
def solver(received):
    list_line = received.split("\n")
    for line in list_line:
        if "X^2" in line:
            # tương tự bài PRO101 khi tới phần code này các cậu sẽ có line là đề bài 
            # có dạng "{}*X^2 + {}*X + C = 0"
            # Xử lý và return kết quả theo lưu ý bên dưới nha
           
    # nên dùng try-except
    # NẾU KẾT QUẢ LÀ VÔ NGHIỆM -> RETURN "NOPE"
    # NẾU KẾT QUẢ CÓ 1 NGHIỆM DUY NHẤT -> RETURN 1 STRING CÓ 2 KẾT QUẢ NGĂN CÁCH BẰNG DẤU "," (VD: "1, 1"    "123, 123")
    # NẾU KẾT QUẢ CÓ 2 NGHIỆM KHÁC NHAU -> RETURN 1 STRING KẾT QUẢ THEO THỨ TỰ TỪ BÉ ĐẾN LỚN, NGĂN CÁCH NHAU BẰNG DẤU "," (VD: "-1, 1"   "-123, 123")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# |||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||


def main():
    # Tạo một socket và kết nối đến server
    ip = "127.0.0.1"  # Đổi thành server IP
    port = 8011     # Đổi port
    # khởi tạo socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Nhận và in ra cho đến khi gặp line "Calculate..."
    # để dừng lại và tính toán kết quả
    # Sau đó lặp lại và nhận bài toán tiếp theo"
    while True:
        received = receive_until("Calculate the roots of this equation: ", s)
        print(received)
        # Nếu phát hiện Flag, dừng vòng lặp và in kết quả
        if "Flag" in received:
            break
        else:
            ans = solver(received)
            send_line(s, ans)

    # Đóng socket sau khi sử dụng xong
    s.close()


if __name__ == '__main__':
    main()
