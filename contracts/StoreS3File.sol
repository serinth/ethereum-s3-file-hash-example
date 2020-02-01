pragma solidity >=0.4.21 <0.7.0;

contract S3FileStorage {
    address public minter;

    struct FileDetail {
        string s3URL;
        string fileHash;
    }

    event AddFile(
        string id,
        string url,
        string fileHash
    );

    mapping(string => FileDetail) public fileHashes;

    constructor() public {
        minter = msg.sender;
    }

    modifier onlyOwner {
        require(
            msg.sender == minter,
            "Only owner/minter can call this function."
        );
        _;
    }

    function addFileReference(string memory id, string memory url, string memory fileHash) public onlyOwner {
        fileHashes[id].s3URL = url;
        fileHashes[id].fileHash = fileHash;

        emit AddFile(id, url, fileHash);
    }

    function getReference(string memory id) public view returns (string memory, string memory) {
        return (fileHashes[id].s3URL, fileHashes[id].fileHash);
    }
}