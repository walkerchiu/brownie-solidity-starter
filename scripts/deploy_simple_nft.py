from brownie import accounts, SimpleNFT


def main():
    try:
        # Deployer's account, using the first account in the Brownie environment
        deployer = accounts[0]

        # Print the deployer's address
        print(f"Deployer address: {deployer.address}\n")

        # Get the ETH balance before contract deployment
        balance_before = deployer.balance()
        print(f"Balance before deployment: {balance_before}\n")

        # Deploy the contract
        simple_nft = SimpleNFT.deploy({"from": deployer})

        # Print the contract address
        print(f"SimpleNFT deployed at: {simple_nft.address}\n")

        # Get the ETH balance after contract deployment
        balance_after = deployer.balance()
        print(f"Balance after deployment: {balance_after}\n")

        # Calculate the ETH cost of contract deployment
        deployment_cost = balance_before - balance_after
        print(f"Deployment cost: {deployment_cost} wei\n")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
