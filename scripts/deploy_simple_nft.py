from brownie import accounts, SimpleNFT


def main():
    try:
        # Deployer's account, using the first account in the Brownie environment
        deployer = accounts[0]

        # Print the deployer's address
        print(f"Deployer address: {deployer.address}\n")

        # Get the ETH balance before contract deployment
        balance_before = get_balance(deployer)
        print(f"Balance before deployment: {balance_before}\n")

        # Deploy the contract
        simple_nft = deploy_simple_nft(deployer)

        # Print the contract address
        print(f"SimpleNFT deployed at: {simple_nft.address}\n")

        # Get the ETH balance after contract deployment
        balance_after = get_balance(deployer)
        print(f"Balance after deployment: {balance_after}\n")

        # Calculate the ETH cost of contract deployment
        deployment_cost = balance_before - balance_after
        print(f"Deployment cost: {deployment_cost} wei\n")
    except Exception as e:
        print(f"An error occurred: {e}")


def deploy_simple_nft(deployer):
    """
    Deploy the SimpleNFT contract.

    :param deployer: The account used for deployment.
    :return: The deployed SimpleNFT contract object.
    """
    try:
        # Deploy the contract
        simple_nft = SimpleNFT.deploy({"from": deployer})
        return simple_nft
    except Exception as e:
        print(f"Error deploying contract: {e}")
        return None


def get_balance(account):
    """
    Get the ETH balance of an account.

    :param account: The account to check the balance.
    :return: The ETH balance of the account.
    """
    return account.balance()


if __name__ == "__main__":
    main()
