from brownie import accounts, SimpleWallet


def test_initial_balance():
    # Deploy the contract
    deployer = accounts[0]
    simple_deposit = SimpleWallet.deploy({"from": deployer})

    # Verify that the initial balance of the contract should be 0
    assert simple_deposit.weiBalance() == 0


def test_deposit():
    # Deploy the contract
    deployer = accounts[0]
    simple_deposit = SimpleWallet.deploy({"from": deployer})

    # Deposit 1 ether into the contract
    deposit_amount = 1e18  # Deposit 1 ether (1e18 Wei)
    simple_deposit.deposit({"from": deployer, "value": deposit_amount})

    # Verify that the contract's balance should be equal to the deposited amount
    assert simple_deposit.weiBalance() == deposit_amount


def test_multiple_deposits():
    # Deploy the contract
    deployer = accounts[0]
    simple_deposit = SimpleWallet.deploy({"from": deployer})

    # Deposit 1 ether into the contract
    deposit_amount1 = 1e18
    simple_deposit.deposit({"from": deployer, "value": deposit_amount1})

    # Deposit more ether into the contract
    deposit_amount2 = 2e18
    simple_deposit.deposit({"from": deployer, "value": deposit_amount2})

    # Verify that the contract's balance should be equal to the total deposited amount
    total_deposit = deposit_amount1 + deposit_amount2
    assert simple_deposit.weiBalance() == total_deposit
