import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, proof):
        self.index = index  # Số thứ tự của block trong chuỗi
        self.previous_hash = previous_hash  # Mã hash của block trước đó
        self.timestamp = timestamp  # Thời gian khi block được tạo
        self.transactions = transactions  # Danh sách các giao dịch trong block
        self.proof = proof  # Proof (bằng chứng) liên quan đến block
        self.hash = self.calculate_hash()  # Mã hash của block hiện tại

    def calculate_hash(self):
        # Tính toán hash của block bằng cách kết hợp tất cả thông tin
        data = str(self.index) + str(self.previous_hash) + str(self.timestamp) + str(self.transactions) + str(self.proof)
        return hashlib.sha256(data.encode()).hexdigest()

# Ví dụ sử dụng:
if __name__ == "__main__":
    # Thông tin của block
    index = 1
    previous_hash = "0"  # Mã hash của block trước đó (với block đầu tiên sẽ là "0")
    timestamp = time.time()  # Thời gian hiện tại
    transactions = [{'sender': 'Alice', 'receiver': 'Bob', 'amount': 50}]  # Ví dụ về giao dịch
    proof = 100  # Một giá trị proof (được sử dụng trong Proof-of-Work hoặc tương tự)

    # Tạo một block mới
    block = Block(index, previous_hash, timestamp, transactions, proof)
    print(f"Block Hash: {block.hash}")
