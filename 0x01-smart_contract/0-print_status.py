#!/usr/bin/env python3
"""
Python program that will interact with Ethereum blockchain \
using ganache-cli testing network.
    Checking connection status.
    retriving Block number.
    retriving Balance.
"""
from web3 import Web3

ganache_url = "http://127.0.0.1:8545"
w3 = Web3(Web3.HTTPProvider(ganache_url))

testing_adr = "0xd239F7f85523be18786e733DFd5A8075236dc75c"

# check connection and print status.
print(Web3.isConnected(w3))

# fetch the block index and print it.
print(w3.eth.blockNumber)

# fetch the Balance value and print it.
balance = w3.eth.getBalance(testing_adr)
print(w3.fromWei(balance, "ether"))
