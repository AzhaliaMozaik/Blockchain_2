from blockchain import Blockchain

# 1. Buat objek blockchain
blockchain = Blockchain()

# 2. Tambahkan transaksi (contoh asli modul)
blockchain.add_block({
    "batch_id": "BATCH-001",
    "product": "Coffee Arabica",
    "actor": "Petani",
    "location": "Kuningan",
})

blockchain.add_block({
    "batch_id": "BATCH-001",
    "product": "Coffee Arabica",
    "actor": "Distributor",
    "location": "Cirebon",
})

# 3. Tampilkan hasil di terminal
for block in blockchain.chain:
    print("=" * 50)
    print("INDEX    :", block.index)
    print("DATA     :", block.data)
    print("PREV     :", block.previous_hash)
    print("HASH     :", block.hash)

print("\nBlockchain valid:", blockchain.is_valid())