import pytest

from brownie import accounts, OpenZeppelinERC20Token


@pytest.fixture(scope="module")
def erc20_token():
    # Deploy OpenZeppelinERC20Token contract and return the contract object
    deployer = accounts[0]
    contract_name = "MyToken"
    contract_symbol = "MTK"
    initial_supply = 1000000
    gas_price = "10 gwei"  # Set gasPrice, you can adjust this as needed
    contract = OpenZeppelinERC20Token.deploy(
        contract_name,
        contract_symbol,
        initial_supply,
        {"from": deployer, "gas_price": gas_price},
    )
    yield contract


def test_initial_state(erc20_token):
    # Test the initial state of the contract
    assert erc20_token.name() == "MyToken"
    assert erc20_token.symbol() == "MTK"
    assert erc20_token.decimals() == 18
    assert erc20_token.totalSupply() == 1000000 * 10**18
    assert erc20_token.balanceOf(accounts[0]) == 1000000 * 10**18


def test_transfer(erc20_token):
    # Test the transfer functionality
    sender = accounts[0]
    recipient = accounts[1]
    initial_balance_sender = erc20_token.balanceOf(sender)
    initial_balance_recipient = erc20_token.balanceOf(recipient)

    amount_to_transfer = 1000 * 10**18
    erc20_token.transfer(
        recipient, amount_to_transfer, {"from": sender, "gas_price": "10 gwei"}
    )

    assert erc20_token.balanceOf(sender) == initial_balance_sender - amount_to_transfer
    assert (
        erc20_token.balanceOf(recipient)
        == initial_balance_recipient + amount_to_transfer
    )


def test_approval_and_transfer_from(erc20_token):
    # Test the approval and transferFrom functionality
    sender = accounts[0]
    recipient = accounts[1]
    third_party = accounts[2]

    initial_balance_sender = erc20_token.balanceOf(sender)
    initial_balance_recipient = erc20_token.balanceOf(recipient)

    amount_to_approve = 500 * 10**18
    erc20_token.approve(
        third_party, amount_to_approve, {"from": sender, "gas_price": "10 gwei"}
    )
    assert erc20_token.allowance(sender, third_party) == amount_to_approve

    amount_to_transfer_from = 200 * 10**18
    erc20_token.transferFrom(
        sender,
        recipient,
        amount_to_transfer_from,
        {"from": third_party, "gas_price": "10 gwei"},
    )

    assert (
        erc20_token.balanceOf(sender)
        == initial_balance_sender - amount_to_transfer_from
    )
    assert (
        erc20_token.balanceOf(recipient)
        == initial_balance_recipient + amount_to_transfer_from
    )


def test_insufficient_balance(erc20_token):
    # Test transfer with insufficient balance
    sender = accounts[0]
    recipient = accounts[1]

    initial_balance_sender = erc20_token.balanceOf(sender)
    amount_to_transfer = initial_balance_sender + 1  # Transfer more than the balance

    # Use try-except to catch a specific exception
    with pytest.raises(Exception) as excinfo:
        erc20_token.transfer(
            recipient, amount_to_transfer, {"from": sender, "gas_price": "10 gwei"}
        )

    # Ensure the exception is due to the transfer amount exceeding the balance
    assert "transfer amount exceeds balance" in str(excinfo.value)
