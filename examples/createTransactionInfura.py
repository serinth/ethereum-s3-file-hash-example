import os
import json
from web3 import Web3, HTTPProvider
from pprint import pprint
from web3.middleware import geth_poa_middleware

wallet_address = os.getenv('PUBLIC_ADDRESS')
contract_address = os.getenv('CONTRACT_ADDRESS')
private_key = os.getenv('PRIVATE_KEY')
infura_key = os.getenv('INFURA_KEY')

w3 = Web3(Web3.HTTPProvider(f'https://rinkeby.infura.io/v3/{infura_key}'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

with open('build/contracts/S3FileStorage.json') as f:
    info = json.load(f)
abi = info['abi']

contract = w3.eth.contract(address=contract_address, abi=abi)

pprint(contract.all_functions())

estimated_gas = contract.functions.addFileReference('tripid1', 'someurl', 'somehash').estimateGas({'gas': 300000, 'from': wallet_address})
pprint(f"Estimating Gas price for addFileReference: {estimated_gas}")

transaction = contract.functions.addFileReference('tripid1', 'someurl', 'somehash').buildTransaction({
    'from': wallet_address,
    'gas': int(estimated_gas * 1.3),
    'nonce': w3.eth.getTransactionCount(wallet_address)
})

# Account private key
signed_tx = w3.eth.account.signTransaction(transaction, private_key)

txn_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
txn_receipt = w3.eth.waitForTransactionReceipt(txn_hash)

pprint(txn_receipt)