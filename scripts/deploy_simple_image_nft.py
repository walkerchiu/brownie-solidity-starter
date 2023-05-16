from brownie import accounts, network, SimpleImageNFT
from brownie.network import gas_price
from brownie.network.gas.strategies import LinearScalingStrategy


def main():
    try:
        # Define the gas price strategy for deployment
        initial_gas_price = "60 gwei"
        max_gas_price = "70 gwei"
        increment = 10

        # Create the LinearScalingStrategy with the defined parameters
        gas_strategy = LinearScalingStrategy(
            initial_gas_price=initial_gas_price,
            max_gas_price=max_gas_price,
            increment=increment,
        )

        # Set gas price strategy for development network
        if network.show_active() == "development":
            gas_price(gas_strategy)

        # Replace with the deployer account
        deployer_account = accounts[0]

        # Deploy the SimpleImageNFT contract
        nft_contract = SimpleImageNFT.deploy(
            {"from": deployer_account, "gas_price": gas_strategy}
        )

        # Replace with the recipient address
        recipient = accounts[0]

        # Replace with the URI of your metadata
        tokenURI = "https://ipfs.io/ipfs/QmTr3Nmdey72Q1zG4mznLf67bKTu41z9CFQdvpWmx35kzX?filename=image.json"

        # Call the mint function
        # Replace with the sender's address
        txn = nft_contract.mintNFT(recipient, tokenURI, {"from": accounts[0]})

        # Print the transaction details and NFT information
        print(f"Minting transaction hash: {txn.txid}")
        print(f"Minted NFT ID: {txn.return_value}")
        print(f"NFT URI: {nft_contract.tokenURI(txn.return_value)}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
