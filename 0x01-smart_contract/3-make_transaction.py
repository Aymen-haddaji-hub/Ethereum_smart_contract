#!/usr/bin/env python3
""" make a transaction in the eth blockchain with py script using web3"""

from web3 import Web3

ganache_url = "http://127.0.0.1:8545"
w3 = Web3(Web3.HTTPProvider(ganache_url))

account_1 = '0x75298cb628F10D2A0Ff7CeB3678c610Ac840ac48'
account_9 = '0x3DeD13D453aE8B28c8fb3aF9402c94807aACD40b'
private_key = '0x60392fc482621edd8de6b19f402bf312d20b6267a896f9076a394b83f2dfcec8'

nonce = w3.eth.getTransactionCount(account_1)

tx = {
    'nonce': nonce,
    'to': account_9,
    'value': w3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': w3.toWei('50', 'gwei'),
}

signed_tx = w3.eth.account.signTransaction(tx, private_key)

tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

print(w3.toHex(tx_hash))

b1 = w3.eth.getBalance(account_1)
b9 = w3.eth.getBalance(account_9)

print("Balance account 1:", b1)
print("Balance account 9:", b9)
