const S3FileStorage = artifacts.require("S3FileStorage");

module.exports = function(deployer) {
  deployer.deploy(S3FileStorage);
};
