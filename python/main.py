#coding=utf-8
"""
author:kidd
"""

# python 3.6

from python.restful import BisionSDK

def main():
    sdk = BisionSDK("37cb78cd-7c35-48cc-83bb-aaa", "aaa")
    print("balance: ", sdk.getBalance())
    print("market config: ", sdk.getMarketConfig())
    print("funds: ", sdk.getFunds())
    print("getDepth: ", sdk.getDepth("btc_usdt"))

if __name__ == '__main__':
    main()
