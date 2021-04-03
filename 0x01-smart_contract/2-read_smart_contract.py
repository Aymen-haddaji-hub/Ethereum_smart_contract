#!/usr/bin/env python3
"""
Python program to read smart contract
from ethereum blockchain using web3 package
"""
from web3 import Web3
import json

infura_url = "https://mainnet.infura.io/v3/4b2db1e7906b4e80b9cd81c7a004bc29"
w3 = Web3(Web3.HTTPProvider(infura_url))

with open('file.json', 'r') as f:
    data = json.load(f)

testing_adr = "0xd26114cd6EE289AccF82350c8d8487fedB8A0C07"
contract = w3.eth.contract(address=testing_adr, abi=data)

totalSupply = contract.functions.totalSupply().call()
print(w3.fromWei(totalSupply, 'ether'))
print(contract.functions.name().call())
print(contract.functions.symbol().call())
balance = contract.functions.balanceOf(testing_adr).call()
print(w3.fromWei(balance, 'ether'))
