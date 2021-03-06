import requests
import json
import time


def main():
    startTime = time.process_time()
    symbolsfile = open("Symbols.txt", "r")
    secretfile = open("secret", "r")
    secret = secretfile.readline()
    secretfile.close()

    # readlines() also reads the newline character in the textfile
    # This method doesn't need to strip the newline characters
    symbols = symbolsfile.read().splitlines()
    symbolsfile.close()
    print("Length of symbols is", len(symbols))

    #Convert list to string separated by commas
    symbolsCat = ','.join(symbols)


    response = requests.get("https://financialmodelingprep.com/api/v3/profile/"+ symbolsCat + "?apikey=" + secret)
    #print(response.json())


    with open ('output.json', 'w') as outputfile:
        json.dump(response.json(), outputfile, indent=4, sort_keys=True)

    print("--- %.2f seconds ---" % (time.process_time() - startTime))
    input("Press Enter to continue...")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

