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

## Putting it on Rinkeby TestNet