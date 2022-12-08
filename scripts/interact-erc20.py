from brownie import ERC20Basic, accounts, config, network


def main():
    account = accounts.add(config["wallets"]["from_key"])
    erc20Basic = ERC20Basic[-1]
    tx = erc20Basic.transfer(
        "0xa2597e50D6B8b378a262c7f9A5e4A761991e8aBc", 1000, {"from": account})
    tx.wait(1)
    print("The account balance is", erc20Basic.balanceOf(
        "0xa2597e50D6B8b378a262c7f9A5e4A761991e8aBc"))
