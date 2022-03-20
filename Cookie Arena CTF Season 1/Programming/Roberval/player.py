import socket
import math

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
    data = str(data).strip()
    createdSocket.send((data + '\n').encode())


# Ham nay giai bai toan
# |||||||||||||||||||||||||||||||||||||||||||||||||
# |||Người chơi điền code giải và return kết quả|||
# |||||||||||||||||||||||||||||||||||||||||||||||||
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
def solver(received):
    # solver lets goo
    # Kiểu dữ liệu trả về là INT
    # nên dùng try-except để tránh xảy ra những tai nạn
    return "NOPE"
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# |||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||


def main():
    # Tạo một socket và kết nối đến server
    ip = "0.0.0.0"  # Đổi thành server IP
    port = 8333     # Đổi port
    # khởi tạo socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Nhận và in ra cho đến khi gặp line "Calculate..."
    # để dừng lại và tính toán kết quả
    # Sau đó lặp lại và nhận bài toán tiếp theo"
    while True:
        received = receive_until("Số lần cân ít nhất là: ", s)
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
