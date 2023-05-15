// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// ERC-721 NFT interface
interface IERC721 {
    event Transfer(
        address indexed _from,
        address indexed _to,
        uint256 indexed _tokenId
    );
    event Approval(
        address indexed _owner,
        address indexed _approved,
        uint256 indexed _tokenId
    );

    // Query the number of NFTs owned by an account
    function balanceOf(address _owner) external view returns (uint256);

    // Query the owner of a specific NFT
    function ownerOf(uint256 _tokenId) external view returns (address);

    // Transfer an NFT from one account to another
    function transferFrom(
        address _from,
        address _to,
        uint256 _tokenId
    ) external;

    // Approve another account to transfer an NFT
    function approve(address _approved, uint256 _tokenId) external;
}

contract SimpleNFT is IERC721 {
    address public owner;
    uint256 private _tokenIdCounter;
    mapping(uint256 => address) private _tokenIdToOwner;
    mapping(uint256 => address) private _tokenIdToApproved;
    mapping(address => uint256) private _ownershipTokenCount;

    string private _name;
    string private _symbol;

    constructor(string memory name_, string memory symbol_) {
        owner = msg.sender;
        _tokenIdCounter = 0;
        _name = name_;
        _symbol = symbol_;
    }

    // Get the name of the NFT
    function name() external view returns (string memory) {
        return _name;
    }

    // Get the symbol of the NFT
    function symbol() external view returns (string memory) {
        return _symbol;
    }

    // Query the number of NFTs owned by an account
    function balanceOf(
        address _owner
    ) external view override returns (uint256) {
        return _ownershipTokenCount[_owner];
    }

    // Query the owner of a specific NFT
    function ownerOf(
        uint256 _tokenId
    ) external view override returns (address) {
        require(_tokenId <= _tokenIdCounter, "Invalid Token ID");
        return _tokenIdToOwner[_tokenId];
    }

    // Transfer an NFT from one account to another
    function transferFrom(
        address _from,
        address _to,
        uint256 _tokenId
    ) external override {
        require(
            msg.sender == _from || msg.sender == _tokenIdToApproved[_tokenId],
            "Not approved"
        );
        require(_from == _tokenIdToOwner[_tokenId], "Not the owner");

        _tokenIdToOwner[_tokenId] = _to;
        _ownershipTokenCount[_from]--;
        _ownershipTokenCount[_to]++;

        emit Transfer(_from, _to, _tokenId);
    }

    // Approve another account to transfer an NFT
    function approve(address _approved, uint256 _tokenId) external override {
        require(msg.sender == _tokenIdToOwner[_tokenId], "Not the owner");
        _tokenIdToApproved[_tokenId] = _approved;

        emit Approval(msg.sender, _approved, _tokenId);
    }

    // Create a new NFT
    function createNFT() external {
        uint256 tokenId = _tokenIdCounter;
        _tokenIdToOwner[tokenId] = msg.sender;
        _ownershipTokenCount[msg.sender]++;
        _tokenIdCounter++;
        emit Transfer(address(0), msg.sender, tokenId);
    }
}
