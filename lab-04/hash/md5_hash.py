def left_rotate(x, amount):
    x &= 0xFFFFFFFF
    return ((x << amount) | (x >> (32 - amount))) & 0xFFFFFFFF

def md5(message):
    import struct

    # Initialize variables:
    a0 = 0x67452301
    b0 = 0xEFCDAB89
    c0 = 0x98BADCFE
    d0 = 0x10325476

    # s specifies the per-round shift amounts
    s = [7, 12, 17, 22] * 4 + \
        [5, 9, 14, 20] * 4 + \
        [4, 11, 16, 23] * 4 + \
        [6, 10, 15, 21] * 4

    # Use binary integer part of sines of integers (Radians) as constants:
    K = [int(abs(__import__('math').sin(i + 1)) * 2**32) & 0xFFFFFFFF for i in range(64)]

    # Pre-processing:
    original_len_bits = (8 * len(message)) & 0xffffffffffffffff
    message += b'\x80'
    while len(message) % 64 != 56:
        message += b'\x00'
    message += struct.pack('<Q', original_len_bits)

    # Process the message in successive 512-bit chunks:
    for offset in range(0, len(message), 64):
        a, b, c, d = a0, b0, c0, d0
        chunk = message[offset:offset + 64]
        M = list(struct.unpack('<16I', chunk))

        for i in range(64):
            if 0 <= i <= 15:
                F = (b & c) | (~b & d)
                g = i
            elif 16 <= i <= 31:
                F = (d & b) | (~d & c)
                g = (5 * i + 1) % 16
            elif 32 <= i <= 47:
                F = b ^ c ^ d
                g = (3 * i + 5) % 16
            else:
                F = c ^ (b | ~d)
                g = (7 * i) % 16

            F = (F + a + K[i] + M[g]) & 0xFFFFFFFF
            a = d
            d = c
            c = b
            b = (b + left_rotate(F, s[i])) & 0xFFFFFFFF

        # Add this chunk's hash to result so far:
        a0 = (a0 + a) & 0xFFFFFFFF
        b0 = (b0 + b) & 0xFFFFFFFF
        c0 = (c0 + c) & 0xFFFFFFFF
        d0 = (d0 + d) & 0xFFFFFFFF

    # Output final hash in little-endian hex format
    return '{:08x}{:08x}{:08x}{:08x}'.format(a0, b0, c0, d0)

# --- Usage Example ---
input_string = input("Nhập chuỗi cần băm: ")
md5_hash = md5(input_string.encode('utf-8'))
print("Mã băm MD5 của chuỗi '{}' là: {}".format(input_string, md5_hash))
