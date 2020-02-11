import os
import json
from web3 import Web3, HTTPProvider
from pprint import pprint
from web3.middleware import geth_poa_middleware

contract_address = os.getenv('CONTRACT_ADDRESS')
#w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/YOUR_INFURA_KEY"))
w3 = Web3(HTTPProvider('http://127.0.0.1:9545'))

w3.middleware_onion.inject(geth_poa_middleware, layer=0)

pprint(f'First Account being used is: {w3.eth.accounts[0]}')

with open('build/contracts/S3FileStorage.json') as f:
    info = json.load(f)
abi = info['abi']

# This is the address of the contract
contract = w3.eth.contract(address=contract_address, abi=abi)

pprint(contract.all_functions())

data = contract.functions.getReference('tripid1').call()

pprint(data)