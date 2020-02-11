import os
import json
from web3 import Web3, HTTPProvider
from pprint import pprint
from web3.middleware import geth_poa_middleware

contract_address = os.getenv('CONTRACT_ADDRESS')
private_key = os.getenv('PRIVATE_KEY') #Also the mnemonic
infura_key = os.getenv('INFURA_KEY')

w3 = Web3(HTTPProvider('http://127.0.0.1:9545'))

w3.middleware_onion.inject(geth_poa_middleware, layer=0)

pprint(f'First Account being used is: {w3.eth.accounts[0]}')

with open('build/contracts/S3FileStorage.json') as f:
    info = json.load(f)
abi = info['abi']

# This is the address of the contract
contract = w3.eth.contract(address=contract_address, abi=abi)

pprint(contract.all_functions())

estimated_gas = contract.functions.addFileReference('tripid1', 'someurl', 'somehash').estimateGas()
pprint(f"Estimating Gas price for addFileReference: {estimated_gas}")

transaction = contract.functions.addFileReference('tripid1', 'someurl', 'somehash').buildTransaction()
transaction.update({ 'gas' : int(estimated_gas * 1.3) })
transaction.update({ 'nonce' : w3.eth.getTransactionCount(w3.eth.accounts[0]) })

# Account private key
signed_tx = w3.eth.account.signTransaction(transaction, private_key)

txn_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
txn_receipt = w3.eth.waitForTransactionReceipt(txn_hash)

pprint(txn_receipt)