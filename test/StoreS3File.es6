const s3 = artifacts.require("S3FileStorage");

contract("S3FileStorage", async accounts => {
    it('should return empty values', async ()=> {
        const expected = { '0': '', '1': '' };
        const instance = await s3.deployed();
        const res = await instance.getReference('not_exists');

        assert.notStrictEqual(res, expected, "expected empty for non existing key");
    });

    it('should deny addFileReference() call to non owner', async ()=> {
        let expected;
        const instance = await s3.deployed();
        
        // accounts[0] is the deployer in truffle
        try {
            const res = await instance.addFileReference('any', 'any', 'any', {from: accounts[2]});
        } catch(err) {
            expected = err;    
        }

        assert.notEmpty(expected, "only owner should call addFileReference()");
    });

    it('should add correct reference', async ()=> {
        const expected = { '0': 'url', '1': 'hash' };
        const instance = await s3.deployed();
        
        const refResponse = await instance.addFileReference('_id', 'url', 'hash', {from: accounts[0]});
        const getResponse = await instance.getReference('_id');
        
        assert.notEmpty(refResponse.tx);
        assert.notStrictEqual(getResponse, expected, "values for index did not match when retrieving");
    });

})