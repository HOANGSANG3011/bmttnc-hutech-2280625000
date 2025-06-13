from blockchain import Blockchain

# Tạo đối tượng Blockchain
my_blockchain = Blockchain()

# Thêm giao dịch vào blockchain
my_blockchain.add_transaction('Alice', 'Bob', 10)
my_blockchain.add_transaction('Bob', 'Charlie', 5)
my_blockchain.add_transaction('Charlie', 'Alice', 3)

# Tiến hành khai thác (mining) block mới
previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof  # Lấy proof của block trước
new_proof = my_blockchain.proof_of_work(previous_proof)  # Tính proof của block mới
previous_hash = previous_block.hash  # Lấy hash của block trước

# Thêm giao dịch "Genesis" cho miner
my_blockchain.add_transaction('Genesis', 'Miner', 1)

# Tạo một block mới với proof và previous_hash
new_block = my_blockchain.create_block(new_proof, previous_hash)

# Hiển thị thông tin của toàn bộ blockchain
for block in my_blockchain.chain:
    print(f"Block #{block.index}")
    print("Timestamp:", block.timestamp)
    print("Transactions:", block.transactions)
    print("Proof:", block.proof)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    print("-" * 50)

# Kiểm tra tính hợp lệ của blockchain
print("Is Blockchain Valid:", my_blockchain.is_chain_valid(my_blockchain.chain))
