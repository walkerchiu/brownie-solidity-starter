from brownie import accounts, network, Contract, ERC20Token


def main():
    try:
        # Contract parameters
        CONTRACT_NAME = "MyToken"
        CONTRACT_SYMBOL = "MTK"
        INITIAL_SUPPLY = 1000000

        # Supported networks for deployment
        SUPPORTED_NETWORKS = [
            "development",
            "goerli",
            "kovan",
            "mainnet",
            "rinkeby",
            "ropsten",
            "sepolia",
        ]

        # Gas price setting
        GAS_PRICE = "10 gwei"  # Recommended gasPrice, you can adjust this as needed

        # Check if deployment is on a supported network
        network_name = network.show_active()
        if network_name not in SUPPORTED_NETWORKS:
            raise ValueError(
                f"Unsupported network '{network_name}'. Check your Brownie configuration."
            )

        # Use the desired account for deployment
        deployer = accounts[0]

        # Check if the account has sufficient balance for deployment
        min_balance_required = 0.1 * 10**18  # Minimum 0.1 ETH balance required
        if deployer.balance() < min_balance_required:
            raise ValueError(
                "Insufficient balance in the deployer account. Please fund the account with ETH."
            )

        # Deploy the contract
        print(f"Deploying {CONTRACT_NAME} contract...")
        contract = ERC20Token.deploy(
            CONTRACT_NAME,
            CONTRACT_SYMBOL,
            INITIAL_SUPPLY,
            {"from": deployer, "gas_price": GAS_PRICE},
        )
        print(f"{CONTRACT_NAME} contract deployed at address: {contract.address}")

        # Optional: Save ABI and contract address to a JSON file for future use
        save_abi_and_address(contract.abi, contract.address)
    except Exception as e:
        print(f"An error occurred: {e}")


def save_abi_and_address(abi, address):
    """
    Save the contract's ABI and address to a JSON file.

    :param abi: The contract's ABI.
    :param address: The contract's address.
    """
    import json

    contract_info = {"abi": abi, "address": address}
    with open("storage/contract_info.json", "w") as f:
        json.dump(contract_info, f)


def load_contract_from_json():
    """
    Load the contract's ABI and address from a JSON file and create a contract object.

    :return: Contract object.
    """
    import json

    # Read ABI and address from the JSON file
    with open("storage/contract_info.json", "r") as f:
        contract_info = json.load(f)

    # Create contract object using ABI and address
    contract = Contract.from_abi(
        "MyToken", contract_info["address"], contract_info["abi"]
    )

    return contract


if __name__ == "__main__":
    main()
