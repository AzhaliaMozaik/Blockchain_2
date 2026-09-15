from blockchain import Blockchain
from pow import proof_of_work 
from pos import proof_of_stake


blockchain = Blockchain()

difficulty = 5

proof_of_work(blockchain.chain[-1], difficulty)
# ==========================================
# AKTOR 1: DONATUR
# ==========================================

blockchain.add_block({
    "campaign_id": "AMAL-001",
    "campaign": "Bantuan Korban Bencana",
    "actor": "Donatur",
    "donor": "Levi",
    "amount": 500000,
    "purpose": "Donasi bantuan korban bencana",
    "location": "Cirebon"
})




# ==========================================
# AKTOR 2: PENGELOLA AMAL
# ==========================================

blockchain.add_block({
    "campaign_id": "AMAL-001",
    "campaign": "Bantuan Korban Bencana",
    "actor": "Pengelola Amal",
    "amount": 500000,
    "purpose": "Pengelolaan dana donasi",
    "location": "Cirebon"
})




# ==========================================
# AKTOR 3: PENERIMA MANFAAT
# ==========================================

blockchain.add_block({
    "campaign_id": "AMAL-001",
    "campaign": "Bantuan Korban Bencana",
    "actor": "Penerima Manfaat",
    "recipient": "Korban Bencana",
    "amount": 500000,
    "purpose": "Menerima bantuan kebutuhan pokok",
    "location": "Cirebon"
})




# ==========================================
# AKTOR 4: AUDITOR / PENGAWAS
# ==========================================

blockchain.add_block({
    "campaign_id": "AMAL-001",
    "campaign": "Bantuan Korban Bencana",
    "actor": "Auditor/Pengawas",
    "status": "Terverifikasi",
    "purpose": "Memeriksa transparansi transaksi",
    "location": "Cirebon"
})



# ==========================================
# MENAMPILKAN BLOCKCHAIN
# ==========================================

print("\n" + "=" * 60)
print("BLOCKCHAIN DONASI")
print("=" * 60)

for block in blockchain.chain:

    print("\n" + "-" * 60)
    print("INDEX :", block.index)
    print("DATA  :", block.data)
    print("PREV  :", block.previous_hash)
    print("NONCE :", block.nonce)
    print("HASH  :", block.hash)


# ==========================================
# PROOF OF STAKE
# ==========================================

print("\n" + "=" * 60)
print("PROOF OF STAKE")
print("=" * 60)

validators = {
    "Donatur": 70,
    "Pengelola Amal": 10,
    "Penerima Manfaat": 10,
    "Auditor/Pengawas":10
}

print("\nValidator:")

for validator, stake in validators.items():
    print(f"{validator}: {stake}")

selected = proof_of_stake(validators)

print("\nValidator terpilih:", selected)


# ==========================================
# VALIDASI BLOCKCHAIN
# ==========================================

print("\nBlockchain valid:", blockchain.is_valid())