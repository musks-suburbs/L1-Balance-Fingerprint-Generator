# app.py
from web3 import Web3
import sys
import time

RPC_URL = "https://mainnet.infura.io/v3/your_api_key"

def get_balance_fingerprint(address):
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    if not w3.is_connected():
        print("❌ Cannot connect to RPC")
        sys.exit(1)

    addr = Web3.to_checksum_address(address)
    balance = w3.eth.get_balance(addr)
    latest = w3.eth.block_number

    fingerprint = Web3.keccak(str(balance).encode()).hex()
    return balance, latest, fingerprint

if __name__ == "__main__":
    print("🔍 Generating balance fingerprint for ZK soundness...")
    time.sleep(0.2)

    if len(sys.argv) < 2:
        print("Usage: python3 app.py <address>")
        sys.exit(1)

    address = sys.argv[1]
    balance, block, fingerprint = get_balance_fingerprint(address)

    print("Address:", address)
    print("Block number:", block)
    print("Balance (wei):", balance)
    print("Fingerprint:", fingerprint)
    print("✅ Fingerprint generated — suitable for ZK circuits, Aztec inputs, or soundness checks.")
