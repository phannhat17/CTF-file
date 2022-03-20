# PLAYERS ARE WELCOME TO MAKE YOUR OWN SOCKET
# Các cậu có thể tự viết script của riêng mình để giải bài
import socket


# Hàm này nhận một line từ server
def get_line(createdSocket):
    inputByte = b''
    while True:
        # Nhận từng byte cho đến khi gặp kí tự xuống dòng
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


# |||||||||||||||||||||||||||||||||||||||||||||||||
# |||Người chơi điền code giải và return kết quả|||
# |||||||||||||||||||||||||||||||||||||||||||||||||
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
def solver(received):
    # tách string nhận được thành các line bằng cách loại bỏ dấu xuống dòng
    list_line = received.split("\n")
    # kiểm tra từng line để nhận "đề bài"
    for line in list_line:
        # khi test đề bằng netcat, nhận thấy được đề bài là 1 line có dạng "int int int int ..."
        # kiểm tra ký tự đầu tiên của line, nếu là digit thì tiếp tục xử lý
        if len(line) > 0:
            if line[0].isdigit():
                pass
            # khi tới được đây, các cậu đã có được đề bài có kiểu dữ liệu STRING "0 1 2 3 4 5"
            # Từ đây các cậu có thể xử lý đề bài và tính tổng ( ͡° ͜ʖ ͡°)

            # Return kết quả là kiểu dữ liệu INT và nhận flag ( ͡° ͜ʖ ͡°)
    # nên dùng try-except...

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# |||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||


def main():
    # Tạo một socket và kết nối đến server
    ip = "127.0.0.1"  # Đổi thành server IP
    port = 8008     # Đổi port
    # khởi tạo socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Nhận và in ra cho đến khi gặp line "Calculate..."
    # để dừng lại và tính toán kết quả
    # Sau đó lặp lại và nhận bài toán tiếp theo"
    while True:
        received = receive_until("Calculate the equation of this numbers: ", s)
        print(received)
        # Nếu phát hiện "Flag" trong string nhận được, dừng vòng lặp và in kết quả
        if "Flag" in received:
            break
        else:
            # Toàn bộ string nhận được từ socket được đưa vào solver để xử lý
            # lưu ý: send line nhận 2 tham số socket và STRING
            send_line(s, str(solver(received)))

    # Đóng socket sau khi sử dụng xong
    s.close()


if __name__ == '__main__':
    main()
