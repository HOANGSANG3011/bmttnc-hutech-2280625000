import sys
from PIL import Image

# Hàm mã hóa thông điệp vào trong ảnh
def encode_image(image_path, message):
    img = Image.open(image_path)  # Mở ảnh
    width, height = img.size  # Lấy kích thước của ảnh
    pixel_index = 0

    # Chuyển thông điệp thành chuỗi nhị phân
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '1111111111111110'  # Đánh dấu kết thúc thông điệp
    data_index = 0

    # Duyệt qua từng pixel của ảnh để mã hóa thông điệp
    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))  # Lấy màu pixel tại vị trí (col, row)
            for color_channel in range(3):  # Duyệt qua các kênh màu RGB
                if data_index < len(binary_message):
                    pixel[color_channel] = int(format(pixel[color_channel], '08b')[:-1] + binary_message[data_index], 2)
                    data_index += 1
            img.putpixel((col, row), tuple(pixel))  # Cập nhật pixel với giá trị mới

            # Nếu tất cả thông điệp đã được mã hóa, thoát khỏi vòng lặp
            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break

    # Lưu ảnh đã mã hóa
    encoded_image_path = 'encoded_image.png'
    img.save(encoded_image_path)
    print("Steganography complete. Encoded image saved as", encoded_image_path)

# Hàm main
def main():
    if len(sys.argv) != 3:  # Kiểm tra số lượng tham số đầu vào
        print("Usage: python encrypt.py <image_path> <message>")
        return

    image_path = sys.argv[1]  # Lấy đường dẫn đến ảnh từ tham số
    message = sys.argv[2]  # Lấy thông điệp từ tham số
    encode_image(image_path, message)  # Gọi hàm mã hóa

# Kiểm tra xem script có đang được gọi trực tiếp không
if __name__ == "__main__":
    main()
