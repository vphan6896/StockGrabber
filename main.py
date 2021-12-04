import requests
import json
import time
import os
import datetime
import tickerAdd

def main():
    startTime = time.process_time()
    symbolsfile = open("Farn.txt", "r")
    secretfile = open("secret", "r")
    secret = secretfile.readline()
    secretfile.close()

    #Use this for naming directory
    now = datetime.datetime.now()
    timeString = now.strftime('%m-%d-%Y')
    print("Current time is: " + timeString)
    os.mkdir("./" + timeString)
    dumpdir = os.path.join("./", timeString)

    # readlines() also reads the newline character in the textfile
    # This method doesn't need to strip the newline characters
    symbols = symbolsfile.read().splitlines()
    symbolsfile.close()
    print("Length of symbols is", len(symbols))

    #Convert list to string separated by commas
    symbolsCat = ','.join(symbols)

    for symbol in symbols:
        #https://financialmodelingprep.com/api/v3/historical-chart/1min/AAPL?apikey=
        #response = requests.get("https://financialmodelingprep.com/api/v3/profile/"+ symbolsCat + "?apikey=" + secret)
        response = requests.get("https://financialmodelingprep.com/api/v3/historical-chart/1min/" + symbol + "?apikey=" + secret)
        with open (dumpdir + "\\" + symbol + ".json", 'w') as outputfile:
            json.dump(response.json(), outputfile, indent=4, sort_keys=True)
        #print(response.json())

    tickerAdd.tickerAdd(dumpdir)


    print("--- %.2f seconds ---" % (time.process_time() - startTime))
    input("Press Enter to continue...")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()