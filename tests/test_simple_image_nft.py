import pytest

from brownie import accounts, SimpleImageNFT
from brownie.network import gas_price
from brownie.network.gas.strategies import LinearScalingStrategy


# Define the gas price strategy for testing
initial_gas_price = "60 gwei"
max_gas_price = "70 gwei"
increment = 10

# Create the LinearScalingStrategy with the defined parameters
gas_strategy = LinearScalingStrategy(
    initial_gas_price=initial_gas_price,
    max_gas_price=max_gas_price,
    increment=increment,
)

# Use pytest fixture to deploy the contract
@pytest.fixture(scope="module")
def nft_contract():
    # Set gas price strategy for development network
    gas_price(gas_strategy)

    # Deploy the SimpleImageNFT contract
    deployer_account = accounts[0]
    contract = SimpleImageNFT.deploy(
        {"from": deployer_account, "gas_price": gas_strategy}
    )

    return contract


# Test contract deployment
def test_deploy(nft_contract):
    assert nft_contract is not None


# Test minting an NFT
def test_mint_nft(nft_contract):
    # Mint an NFT
    recipient = accounts[1]
    tokenURI = "https://ipfs.io/ipfs/QmTr3Nmdey72Q1zG4mznLf67bKTu41z9CFQdvpWmx35kzX?filename=image.json"
    txn = nft_contract.mintNFT(recipient, tokenURI, {"from": recipient})

    # Verify the minting result
    assert nft_contract.balanceOf(recipient) == 1
    assert nft_contract.ownerOf(1) == recipient.address
    assert nft_contract.tokenURI(1) == tokenURI
