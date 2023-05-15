import pytest

from brownie import accounts, SimpleNFT


# Fixture that deploys the contract before each test function
@pytest.fixture(scope="function")
def simple_nft():
    deployer = accounts[0]
    return SimpleNFT.deploy("MyNFT", "NFT", {"from": deployer})


def test_deploy_simple_nft(simple_nft):
    # Check if contract was deployed successfully
    assert simple_nft is not None


# Test the createNFT function
def test_create_nft(simple_nft):
    # Ensure that the contract owner is the deploying account
    assert simple_nft.owner() == accounts[0]

    # Check that the initial NFT count is 0
    assert simple_nft.balanceOf(accounts[0]) == 0

    # Create an NFT
    simple_nft.createNFT({"from": accounts[0]})

    # Check that the NFT count increased to 1
    assert simple_nft.balanceOf(accounts[0]) == 1


# Test the transferFrom function
def test_transfer_nft(simple_nft):
    # Create an NFT
    simple_nft.createNFT({"from": accounts[0]})
    nft_id = 0

    # Ensure that the NFT owner is the deploying account
    assert simple_nft.ownerOf(nft_id) == accounts[0]

    # Create a second account
    account1 = accounts[1]

    # Transfer the NFT from the first account to the second account
    simple_nft.transferFrom(accounts[0], account1, nft_id, {"from": accounts[0]})

    # Check that the NFT now belongs to the second account
    assert simple_nft.ownerOf(nft_id) == account1
    # Check that the NFT count of the first account decreased to 0
    assert simple_nft.balanceOf(accounts[0]) == 0
    # Check that the NFT count of the second account increased to 1
    assert simple_nft.balanceOf(account1) == 1


# Test the approve and transferFrom functions
def test_approve_transfer(simple_nft):
    # Create an NFT
    simple_nft.createNFT({"from": accounts[0]})
    nft_id = 0

    # Create a second account
    account1 = accounts[1]

    # Approve the second account to transfer the NFT
    simple_nft.approve(account1, nft_id, {"from": accounts[0]})

    # Transfer the NFT using the second account
    simple_nft.transferFrom(accounts[0], account1, nft_id, {"from": account1})

    # Check that the NFT now belongs to the second account
    assert simple_nft.ownerOf(nft_id) == account1
    # Check that the NFT count of the first account decreased to 0
    assert simple_nft.balanceOf(accounts[0]) == 0
    # Check that the NFT count of the second account increased to 1
    assert simple_nft.balanceOf(account1) == 1
