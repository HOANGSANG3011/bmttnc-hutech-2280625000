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


class Blockchain:
    def __init__(self):
        self.chain = []  # Chuỗi các block
        self.current_transactions = []  # Danh sách các giao dịch hiện tại
        self.create_block(proof=1, previous_hash='0')  # Tạo block đầu tiên (genesis block)

    def create_block(self, proof, previous_hash):
        block = Block(len(self.chain) + 1, previous_hash, time.time(), self.current_transactions, proof)
        self.current_transactions = []  # Xóa danh sách giao dịch hiện tại sau khi tạo block
        self.chain.append(block)  # Thêm block vào chuỗi
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while not check_proof:
            # Tính toán hash theo công thức Proof-of-Work
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def add_transaction(self, sender, receiver, amount):
        # Thêm giao dịch vào danh sách các giao dịch hiện tại
        self.current_transactions.append({'sender': sender, 'receiver': receiver, 'amount': amount})
        # Trả về số thứ tự của block tiếp theo
        return self.get_previous_block().index + 1

    def is_chain_valid(self, chain):
        previous_block = chain[0]  # Block đầu tiên
        block_index = 1

        # Kiểm tra tính hợp lệ của chuỗi block
        while block_index < len(chain):
            block = chain[block_index]
            # Kiểm tra xem previous_hash có đúng không
            if block.previous_hash != previous_block.hash:
                return False

            # Kiểm tra Proof-of-Work
            previous_proof = previous_block.proof
            proof = block.proof
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False

            previous_block = block
            block_index += 1

        return True
