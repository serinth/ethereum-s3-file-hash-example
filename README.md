# Working Locally

```bash
mkdir myproject
cd myproject
npm install -g truffle
truffle init
```

Start the **develop** console:
```bash
truffle develop
```


## Truffle Develop CLI Quick Reference
`accounts`

It will use the default / first account when running a deployment.
```bash
compile
deploy
```
You can get the account from the output of the deploy command.

To add a file reference interactively, get the instance at the deployed address:
```javascript
let c = S3FileStorage.at("0x...") // or S3FileStorage.deployed()
c.addFileReference('<fileid>','https://<url>','<HASH>')
```

To show that it doesn't work i.e. not the owner (assuming accounts[0] is the owner):
```javascript
c.addFileReference('<fileid>','https://<url>','<HASH>', {from: accounts[3]})
```
Should return an error.

# Putting The Smart Contract on Rinkeby TestNet

1. Using a hosted blockchain node, sign up for keys at [Infura](https://infura.io).

2. Install an HD Wallet Provider which will manage private keys for us.
```bash
npm install @truffle/hdwallet-provider
```

3. Create a `.env` file and have the following values filled out:
```
MNEMONIC=""
INFURA_KEY=""
```

4. Go to https://www.rinkeby.io/#faucet and add ETH into one of your wallets. Use the reference link below to generate those keys.

5. Deploy to Rinkeby 
You can also append `--dry-run` to make sure everything is ok. Sometimes wrong accounts are used or there isn't enough ETH in the account.

```bash
truffle deploy --network rinkeby
```

You should see something like this:
```
Migrations dry-run (simulation)
===============================
> Network name:    'rinkeby-fork'
> Network id:      4
> Block gas limit: 0x989680


1_initial_migration.js
======================

   Deploying 'Migrations'
   ----------------------
   > block number:        5897700
   > block timestamp:     1580605566
   > account:             0x1EacB1739bE1A3aA8F115Ad2021D69a775df8698
   > balance:             18.74970165
   > gas used:            149175
   > gas price:           2 gwei
   > value sent:          0 ETH
   > total cost:          0.00029835 ETH

   -------------------------------------
   > Total cost:          0.00029835 ETH


2_deploy_s3filestore.js
=======================

   Deploying 'S3FileStorage'
   -------------------------
   > block number:        5897702
   > block timestamp:     1580605579
   > account:             0x1EacB1739bE1A3aA8F115Ad2021D69a775df8698
   > balance:             18.74802706
   > gas used:            809954
   > gas price:           2 gwei
   > value sent:          0 ETH
   > total cost:          0.001619908 ETH

   -------------------------------------
   > Total cost:         0.001619908 ETH


Summary
=======
> Total deployments:   2
> Final cost:          0.001918258 ETH
```

Once deployed, grab the contract address and put it into the explorer:
https://www.rinkeby.io/#explorer

# Calling the contract in Python

Setup your environment with python 3.7

```bash
pipenv --python 3.7
pipenv install
```

## Calling the addFileReference Function (Transaction -- costs gas)

This is a transaction and requires some gas. Open up `createTransaction.py` to have a look. It's setup to run locally but can be modified in the comments to point to a hosted node on Infura.
Have the following environment variables set:

**CONTRACT_ADDRESS** and **PRIVATE_KEY**

Infura requires that raw transactions are sent and signed.

Modify the source code with the desired values. 

Run:

```bash
pipenv run python createTransaction.py
```

## Calling getReference Function (Call -- no gas required)

Make sure you change the values to match in `readContractData.py`

```bash
pipenv run python readContractData.py
```

It should spit back the values you put on the blockchain earlier.

# References
- https://iancoleman.io/bip39/
- https://www.trufflesuite.com/tutorials/using-infura-custom-provider
