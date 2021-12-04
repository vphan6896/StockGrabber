import sys
import os
import json

def tickerAdd(folderName="12-03-2021"):
    fileList = os.listdir(folderName)
    for file in fileList:
        ticker = file.strip(".json")

        # Open file
        with open(folderName + "\\" + file) as stockFile:
            stockData = stockFile.read()

        # Parse file
        stock = json.loads(stockData)

        for stockMinute in stock:
            stockMinute['ticker'] = ticker

        stock_file = open(folderName + "\\" + file, "w")
        stock_file.write(json.dumps(stock))
        stock_file.close()

if __name__ == '__main__':
    tickerAdd(sys.argv[1])