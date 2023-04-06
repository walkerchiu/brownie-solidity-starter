// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// SimpleWallet contract is a basic smart contract that allows users to deposit ether.
contract SimpleWallet {
    address public owner; // Address of the contract owner
    uint256 public weiBalance; // Balance in wei stored in the contract

    // Constructor: Initializes the contract with the deployer's address as the owner and zero balance.
    constructor() {
        owner = msg.sender; // Set the contract owner to the deployer's address
        weiBalance = 0; // Initialize the balance to zero
    }

    // deposit function allows users to deposit ether into the contract.
    // It requires the sender to send some ether (greater than zero) along with the transaction.
    function deposit() public payable {
        require(msg.value > 0, "You must send some ether"); // Ensure a positive ether value is sent
        weiBalance += msg.value; // Increase the contract's balance with the sent ether
    }

    // getBalance function returns the current balance stored in the contract (in wei).
    function getBalance() public view returns (uint256) {
        return weiBalance; // Return the current balance
    }
}
