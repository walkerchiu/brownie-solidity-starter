from brownie import SimpleWallet, accounts, network


def main():
    try:
        # Switch to the target network (e.g., development, mainnet, ropsten, etc.)
        network_name = network.show_active()
        print(f"Deploying to {network_name} network")

        # Get the deploying account (using the default account)
        deployer = accounts[0]

        # Deploy the SimpleWallet contract
        simple_wallet = SimpleWallet.deploy({"from": deployer})

        # Display the contract address after deployment
        print(f"SimpleWallet deployed to: {simple_wallet.address}\n")

        # If you are using the local development network, you can perform some interactive testing
        if network_name == "development":
            # Query the contract balance before any deposits
            balance = simple_wallet.getBalance()
            print(f"Contract balance before deposit: {balance}\n")

            # Deposit some ether into the contract
            deposit_amount = 1e18  # Deposit 1 ether (1e18 Wei)
            simple_wallet.deposit({"from": deployer, "value": deposit_amount})

            # Query the contract balance after the deposit
            balance = simple_wallet.getBalance()
            print(f"Contract balance after deposit: {balance}\n")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
