import sys
from PIL import Image

# Hàm giải mã thông điệp từ ảnh
def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)  # Mở ảnh đã mã hóa   
    width, height = img.size  # Lấy kích thước của ảnh
    binary_message = ""  # Chuỗi nhị phân để lưu thông điệp

    # Duyệt qua từng pixel để lấy các bit thông điệp
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))  # Lấy màu pixel tại vị trí (col, row)
            for color_channel in range(3):  # Duyệt qua các kênh màu RGB
                binary_message += format(pixel[color_channel], '08b')[-1]  # Lấy bit cuối của mỗi kênh màu  

    # Chuyển nhị phân thành thông điệp văn bản
    message = ""
    for i in range(0, len(binary_message), 8):  # Chia nhị phân thành các nhóm 8 bit
        char = chr(int(binary_message[i:i+8], 2))  # Chuyển 8 bit thành ký tự
        if char == '\0':  # Kết thúc thông điệp khi gặp ký tự null (thường là \0)
            break
        message += char

    return message

# Hàm main
def main():
    if len(sys.argv) != 2:  # Kiểm tra số lượng tham số đầu vào
        print("Usage: python decrypt.py <encoded_image_path>")
        return

    encoded_image_path = sys.argv[1]  # Lấy đường dẫn ảnh từ tham số
    decoded_message = decode_image(encoded_image_path)  # Giải mã thông điệp từ ảnh
    print("Decoded message:", decoded_message)  # In ra thông điệp đã giải mã

# Kiểm tra xem script có đang được gọi trực tiếp không
if __name__ == "__main__":
    main()
