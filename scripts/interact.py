from brownie import YourContract, config, accounts, network


def main():
    account = accounts.add(config["wallets"]["from_key"])
    yourContract = YourContract[-1]
    tx = yourContract.setNumber(123456, {'from': account})
    tx.wait(1)
    print("Number is", yourContract.getNumber())
