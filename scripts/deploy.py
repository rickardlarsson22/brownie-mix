from brownie import YourContract, config, accounts

def deployContract():
    account = accounts.add(config["wallets"]["from_key"]) or accounts[0]
    YourContract.deploy({'from': account})
    
def main():
    deployContract()
    