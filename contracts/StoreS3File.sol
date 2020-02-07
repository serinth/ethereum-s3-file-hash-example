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

    function addFileReference(string memory _id, string memory _url, string memory _fileHash) public onlyOwner {
        fileHashes[_id].s3URL = _url;
        fileHashes[_id].fileHash = _fileHash;

        emit AddFile(_id, _url, _fileHash);
    }

    function getReference(string memory _id) public view returns (string memory, string memory) {
        return (fileHashes[_id].s3URL, fileHashes[_id].fileHash);
    }
}
