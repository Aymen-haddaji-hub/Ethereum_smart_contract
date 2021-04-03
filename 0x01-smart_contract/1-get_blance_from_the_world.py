#!/usr/bin/env python3
"""
Python program that will interact with Ethereum blockchain \
using infura.io testing network.
    Checking connection status.
    retriving Block number.
    retriving Balance.
"""
from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/4b2db1e7906b4e80b9cd81c7a004bc29"
w3 = Web3(Web3.HTTPProvider(infura_url))

testing_adr = "0x829BD824B016326A401d083B33D092293333A830"

# check connection and print status.
print(Web3.isConnected(w3))

# fetch the block index and print it.
print(w3.eth.blockNumber)

# fetch the Balance value and print it.
balance = w3.eth.getBalance(testing_adr)
print("Ethereum Balance:", w3.fromWei(balance, "ether"))
