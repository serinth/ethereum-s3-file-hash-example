import os
import json
import time
from web3 import Web3, HTTPProvider
from threading import Thread
from pprint import pprint
from web3.middleware import geth_poa_middleware

def handle_event(event):
    print(event)
    pprint(event)


def event_thread(event_filter, poll_interval):
    while True:
        for event in event_filter.get_all_entries():
            handle_event(event)
        time.sleep(poll_interval)

def main():
    contract_address = os.getenv('CONTRACT_ADDRESS', None)

    w3 = Web3(HTTPProvider('http://127.0.0.1:9545'))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    with open('build/contracts/S3FileStorage.json') as f:
        info = json.load(f)
        abi = info['abi']

    # This is the address of the contract
    contract = w3.eth.contract(address=contract_address, abi=abi)

    block_filter = contract.events.AddFile.createFilter(fromBlock=0)

    pprint(block_filter.get_all_entries())
    
    worker = Thread(target=event_thread, args=(block_filter, 2), daemon=True)
    worker.start()
    print('Started Listener...')

    worker.join()

if __name__ == '__main__':
    main()