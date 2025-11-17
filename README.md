# README.md
# L1 Balance Fingerprint Generator

## Overview
This repository contains a simple tool that generates a deterministic fingerprint of an Ethereum account balance. This fingerprint can be used inside ZK systems, soundness verifiers, Aztec-style circuits, or any cryptographic workflow requiring reproducible state commitments.

## Installation
Install Python 3.10 or newer.
Install dependencies using pip install web3.
Insert your own RPC endpoint into the RPC_URL variable in app.py.

## Usage
Run the script by providing an Ethereum address:
python3 app.py 0xYourAddress

## What the Script Does
The script connects to an Ethereum RPC node, retrieves the account balance at the latest block, computes a keccak256 fingerprint, and outputs the resulting values. This fingerprint can be used as a stable public input for ZK circuits, rollup logic, or soundness verification mechanisms.

## Expected Output
The script prints:
Address  
Block number  
Balance in wei  
Fingerprint  
A final confirmation message

## Notes
Works with any EVM-compatible RPC by updating the RPC_URL value.  
Suitable for ZK proving systems, Aztec integrations, Zama workflows, and soundness-oriented projects.  
Uses only account balances, ensuring the result remains deterministic across compatible RPC providers.  
