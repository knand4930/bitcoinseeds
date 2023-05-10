from mnemonic import Mnemonic
import os
from eth_account import Account
Account.enable_unaudited_hdwallet_features()
import requests

API_KEY = "DFRBQVTNSMYCPXRDDCN5UTRWKGK89IPX6I"


while True:
    random_bytes = os.urandom(16)
    mnemo = Mnemonic("english")
    seed_words = mnemo.to_mnemonic(random_bytes)
    print(seed_words)
    with open('data.txt', 'a') as file:
        file.write('\n' + str(seed_words))

    # try:
    #     acct = Account.from_mnemonic(seed_words)
    #     print(acct.address)
    #     url = f"https://api.etherscan.io/api?module=account&action=balance&address={acct.address}&tag=latest&apikey={API_KEY}"
    #     response = requests.get(url)
    #     print(response)
    #     if response.status_code == 200:
    #         data = response.json()

    #         if int(data['result']) !=0:
    #             variable = {
    #                 "results": data['result'],
    #                 "address": acct.address,
    #                 "seeds" : seed_words,
    #             }
    #             with open('balance.txt', 'a') as file:
    #                 file.write('\n' + str(variable))
    #         else:
    #             acc = {
    #                 "results": data['result'],
    #                 "address": acct.address,
    #                 "seeds": seed_words,
    #             }

    #             with open('metamasktreal.txt', 'a') as file:
    #                 file.write('\n' + str(acc))

    # except Exception as E:
    #     print(E)
    #     with open('metamaskdummy.txt', 'a') as file:
    #         file.write('\n' + str(E))
        