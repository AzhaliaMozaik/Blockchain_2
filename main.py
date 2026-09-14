from blockchain import Blockchain

blockchain = Blockchain()

# Aktor 1: Donatur
blockchain.add_block({
    "campaign_id": "AMAL-001",
    "campaign": "Bantuan Korban Bencana",
    "actor": "Donatur",
    "donor": "Levi",
    "amount": 500000,
    "purpose": "Donasi bantuan korban bencana",
    "location": "Cirebon"
})

# Aktor 2: Pengelola Amal
blockchain.add_block({
    "campaign_id": "AMAL-001",
    "campaign": "Bantuan Korban Bencana",
    "actor": "Pengelola Amal",
    "amount": 500000,
    "purpose": "Pengelolaan dana donasi",
    "location": "Cirebon"
})

# Aktor 3: Penerima Manfaat
blockchain.add_block({
    "campaign_id": "AMAL-001",
    "campaign": "Bantuan Korban Bencana",
    "actor": "Penerima Manfaat",
    "recipient": "Korban Bencana",
    "amount": 500000,
    "purpose": "Menerima bantuan kebutuhan pokok",
    "location": "Cirebon"
})

# Aktor 4: Auditor/Pengawas
blockchain.add_block({
    "campaign_id": "AMAL-001",
    "campaign": "Bantuan Korban Bencana",
    "actor": "Auditor/Pengawas",
    "status": "Terverifikasi",
    "purpose": "Memeriksa transparansi transaksi",
    "location": "Cirebon"
})

# Menampilkan blockchain
for block in blockchain.chain:

    print("=" * 60)
    print("INDEX :", block.index)
    print("DATA  :", block.data)
    print("PREV  :", block.previous_hash)
    print("HASH  :", block.hash)

print("\nBlockchain valid:", blockchain.is_valid())