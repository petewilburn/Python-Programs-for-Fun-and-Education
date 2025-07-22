# A python program for handling options chains through the IBKR WebAPI
# The implementation here will focus on building out the contract libraries pre-emptively before moving into the daily trading.
# The expectation for this script would be to run it once in the morning at the start of the month rather than intra-day.
# While Python is used in this scenario, the steps can be translated to most other languages given the RESTful request structure of the IBKR WebAPI.
# For the Python libraries used in this script, external libraries documented in the ibkr Endpoints section will be used,
# focusing primarily on "requests", "urllib3", and "csv" from the Python standard library.
# Because we will be working in the client portal gateway, I will also be passing verify=False to the requests to avoid SSL verification issues.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Minimum Python version 3.9

# Reference: https://interactivebrokers.github.io/tws-api/rest_api.html
# Reference: https://www.interactivebrokers.com/campus/ibkr-quant-news/handling-options-chains/

# -----------------------------------------------------------------------------------------------------------------
# File: P5001_ibkr_Options_Chains_Handling.py
# Description: A Python program to handle options chains through the IBKR WebAPI.
# -----------------------------------------------------------------------------------------------------------------

"""
One of the most ubiquitous questions received for the Interactive Brokers API team is the process 
for users to receive options chain data through the WebAPI. And while we have received some positive 
feedback over our existing Options Chains Documentation, we felt there was room for additional guidance 
on how a user could implement this system. Throughout this article, I'll present one method for 
retrieving an option chain programmatically.

As users may be aware already, the Client Portal API requires that users query the 
/iserver/secdef/search, /iserver/secdef/strikes, and /iserver/secdef/info sequentially, with no means 
around this process. However, the implementation here will focus on building out our contract libraries 
pre-emptively before moving into the daily trading. As a result, the expectation for this script would 
be to run it once in the morning at the start of a month rather than intra-day.

While I am using Python in this scenario, these steps can be translated to most other programming 
languages given the RESTful request structure. For the Python libraries used in this script, I'll be 
referencing the external libraries documented in our Endpoints section, focusing primarily on "requests", 
"urllib3", and "csv" from the python standard library. Because I'm working in the client portal gateway, 
I will also be passing verify=False in my requests, though this may be skipped.
"""

import requests
import urllib3
import csv

# Ignore insecure error messages
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def secdefSearch(symbol, listingExchange):
    """
    After establishing imports, I'll define our secdefSearch method to create our initial search request and handle the returned data.
    We can set the arguments for symbol and listingExchange, so we can filter the exact contract we're looking for without having to
    sort the data using the primary listing exchange and symbol.

    Moving into our method, I'll define our "url" variable as f"https://localhost:5001/v1/api/iserver/secdef/search?symbol={symbol}".
    With a URL set, we can make our request, search_request, set to 'requests.get(url=url, verify=False)'.
    If you print search_request.json(), directly, you'll find an array of several contracts.
    """
    url = f"https://localhost:5001/v1/api/iserver/secdef/search?symbol={symbol}"
    search_request = requests.get(url=url, verify=False)

    # We don't necessarily care about all of these contracts, so now we can look to filter it using our listingExchange argument from before. 
    # To do this, I'll loop through each contract in our json, then if any of the contract "description" values match our listingExchange,
    # we'll have found the appropriate contract. Here, I can set our underConid variable to the contract "conid" field, which is the unique
    # identifier for the contract.
    for contract in search_request.json():
        if contract["description"] == listingExchange:
            underConid = contract["conid"]

            # While we are still in the contract we're looking for, we can pull out the expiration month's we're looking for. I'll do this by iterating
            # through the secType items in the contract "sections" section. Here, if I find a secType "secType" that is an "OPT", we'll have our
            # options contract months. I will set our "months" variable to the secType "months" section, and split the value on the semicolons.
            # Now we can return our underConid and months as a tuple.
            for secType in contract["sections"]:
                if secType["secType"] == "OPT":
                    months = secType["months"].split(";")
    return underConid, months


def snapshotData(underConid):
    """
    Before jumping into the strikes endpoint, I'd like to calculate the approximate price of the instrument to find what is in-the-money. 
    To do this, I'll create a snapshotData method, taking an argument for our underConid variable. Similar to our last method, I'll create a 
    'url' variable and set it to "f'https://localhost:5001/v1/api/iserver/marketdata/snapshot?conids={underConid}&fields=31'". This is the 
    market data snapshot endpoint that can be used to retrieve the last price {31} for the instrument. I can then create two requests to the 
    same url, using the format of request.get(url=url,verify=False) just like before. We're sending the request twice due to the mandatory 
    preflight request for the endpoint. I will set my second request to the snapshot variable, to pull from it later. To conclude the method, 
    I'll simply return snapshot.json()[0]["31"] to return the Last price received.
    """
    url = f'https://localhost:5001/v1/api/iserver/marketdata/snapshot?conids={underConid}&fields=31'
    requests.get(url=url, verify=False)
    snapshot = requests.get(url=url, verify=False)
    return snapshot.json()[0]["31"]


def secdefStrikes(underConid, month):
    """
    We can move on and define the secdefStrikes method, passing our underConid and month variables. Within our method, I'll create the variable, 
    snapshot, and set it to the float of our snapshotData's response. We'll be using the value for a calculation later, so we can't use it as 
    the String value we retrieved it as. I will also create a list named itmStrikes, which we'll leave empty but refer to later. And as usual, 
    I'll create a url variable set to the /iserver/secdef/strikes endpoint. And while I'll be passing the underConid and month variables 
    accordingly, I will set the secType param to "OPT", as I have no interest in retrieving Futures Options. However, if you trade Futures 
    Options, or a mix of the two, you could always set the value to a variable all the same. Then, we can set a strike_request variable equal 
    to the request.

    With the request out of the way, we can start working with the response. I'll begin with a strikes variable set to the "put" key. In most 
    scenarios, the list of Put strikes will match those of the Calls; however, this is not always the case. Users interested in trading both 
    rights or Calls specifically can adjust their code accordingly. Now we can begin to iterate through each strike in strikes. My condition 
    for contracts in the money will be those within $20 of our contract, and so I will make an 'if' statement to retrieve all strikes within 
    $10 under our snapshot price, and everything $10 over our snapshot price. Developers may alternatively implement a 5% variable rather than 
    a fixed value to approach a similar result. Now we'll start to append our results to the itmStrikes list we had created before, and then 
    return the list once our loop has finished.
    """
    snapshot = float(snapshotData(underConid))
    itmStrikes = []

    url = f'https://localhost:5001/v1/api/iserver/secdef/strikes?conid={underConid}&secType=OPT&month={month}'
    strike_request = requests.get(url=url, verify=False)

    strikes = strike_request.json()["put"]
    for strike in strikes:
        if strike > snapshot - 10 and strike < snapshot + 10:
            itmStrikes.append(strike)
    return itmStrikes


def secdefInfo(conid, month, strike):
    """
    At this point, we can write out the secdefInfo method, taking the three arguments mentioned before, underConid, month, and strike. We'll 
    create another url variable set to the /iserver/secdef/info endpoint which takes all of our arguments as parameters, and the additional 
    secType and right parameter, which we'll preset to "OPT" and "P" respectively. Then we can follow this with setting the info_request 
    variable to our request.get(url=url, verify=False) call once again.

    Before handling the response, I will first create an empty list, contracts. Now, the response to this endpoint will produce several 
    different contracts as there are multiple expiries within the month. Given my scenario trades each weekly contract, I can retrieve each 
    May contract. However, you are welcome to filter by a given MaturityDate, or other field that you feel is relevant. With my scope settled, 
    I can iterate through our info_request.json() response using individual contract variables for each. Within the for-loop, we can assign the 
    contract, symbol, strike, and maturityDate values to a contractDetails dictionary definition. I'll then append this value to our contracts 
    list. Once the loop has finished, I'll then return the full contracts list.
    """
    url = f'https://localhost:5001/v1/api/iserver/secdef/info?conid={conid}&month={month}&strike={strike}&secType=OPT&right=P'
    info_request = requests.get(url=url, verify=False)

    contracts = []
    for contract in info_request.json():
        contractDetails = {
            "conid": contract["conid"], 
            "symbol": contract["symbol"],
            "strike": contract["strike"],
            "maturityDate": contract["maturityDate"]
        }
        contracts.append(contractDetails)
    return contracts


def writeResult(contractDict):
    """
    With the larger script completed, we could simply print our resulting contractDict, or pass it around our trading session if we chose to 
    run this every morning possible. However, as we mentioned at the start of the article, the intention of this is to elaborate on how to use 
    these requests in the long term. We can look to add our dictionary into a CSV file for future use. I would encourage readers to extrapolate 
    on this idea potentially with a larger internal database structure, or those empowered by Excel may choose to connect with xlwings as we 
    discussed in our prior lesson. We'll conclude our idiom with a call to a new writeResult method sending our contractDict variable as our 
    argument.

    Within our writeResult method, we can start with our header values, that we had taken from the /info endpoint: conid, symbol, strike, and 
    maturityDate. Then, I can write out a filePath to our current directory into a file named "./MayContracts.csv".

    Now we can create some general structures using the csv library. We'll start with a contract_csv_file variable, set to open(filePath, 'w', 
    newline=''). This way we can reference a file, defined by our filePath variable that we'll be writing to. Then, we can set a contract_writer 
    variable equal to the csv.DictWriter object class. We'll pass in our contract_csv_file as the "f" variable, and set the fieldnames variable 
    equal to our headers. Then, I'd like to write out our headers using the DictWriter.writeheader method.

    With our structure set, let's iterate through each strikeGroup in our contractDict dictionary. Nesting further down, we can then iterate 
    through each contractDetail inside the contractDict's strikeGroup. This will allow us to write out the contractDetails with the 
    contract_writer. We can conclude the method by closing out the file once we have finished iterating through our dictionary. I will add a 
    simple print to indicate "Job's done.", as none of the other requests handled so far have actually been displayed to the user.
    """
    headers = ["conid", "symbol", "strike", "maturityDate"]
    filePath = "./MayContracts.csv"
    
    contract_csv_file = open(filePath, 'w', newline='')
    contract_writer = csv.DictWriter(f=contract_csv_file, fieldnames=headers)
    contract_writer.writeheader()
    
    for strikeGroup in contractDict:
        for contractDetails in contractDict[strikeGroup]:
            contract_writer.writerow(contractDetails)
    contract_csv_file.close()
    print("Job's done.")


if __name__ == "__main__":
    """
    With our first method settled, we can create our name-main idiom and make our initial call to secdefSearch from there. At the bottom of the 
    file, we can build out the standard 'if __name__ == "__main__":', then set matching variables underConid and months equal to the 
    secdefSearch method. I will pass in "AAPL" as the symbol and "NASDAQ" as the listingExchange, but you're welcome to change these to any 
    other symbol or exchange you wish.

    I will also be creating a new variable in our idiom, month, which I will set to the 0 value of our returned months method. You're welcome 
    to query whichever contracts you'd like; however, I typically prefer to focus on the front month, so using the first indexed item will 
    always bring up the front month.
    """
    # I'm looking for the U.S. Apple Incorporated company listed on NASDAQ
    underConid, months = secdefSearch("AAPL", "NASDAQ")
  
    # I only want the front month. 
    # Users could always grab all months, or pull out a specific value, but sending the 0 value always gives me the first available contract.
    month = months[0]

    """
    Now we can move back to our Name-Main idiom before writing our last methods. After setting our month variable, I will set a new itmStrikes 
    variable equal to a call to our secdefStrikes method with our underConid and month variables. Next, we can create a dictionary, contractDict. 
    Then, we'll iterate through each strike in itmStrikes. Here, we can set the strike as the key of contractDict, and set it equivalent to the 
    response of a new secdefInfo method we're about to write, taking the underConid, month, and strike variables we've retrieved up to this point.
    """
    # We'll be calling our Strikes endpoint to pull in the money strike prices rather than all strikes.
    itmStrikes = secdefStrikes(underConid, month)

    # We can then pass those strikes to the /info endpoint, and retrieve all the contract details we need.
    contractDict = {}
    for strike in itmStrikes:
        contractDict[strike] = secdefInfo(underConid, month, strike)

    """
    Thus the file is settled correctly. Assuming everything was saved correctly, we should now see the MayContracts.csv file stored in the same 
    directory as where our python was executed. Opening the file, we'll find that we now have a column displaying each conid, symbol, strike, 
    and expiration date. Going forward, you could conversely utilize the csv.DictReader() class to pull out these same values as necessary 
    whenever needed, and we can look to use them throughout the month as our trading persists. 
    """
    writeResult(contractDict)

