import urllib.request

import json

API_KEY = 'WF60VJGBU281Q68U'

 



def getStockData(symbol):
	URL = 'https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols=' + symbol + '&apikey=' + API_KEY
	try:
		connection = urllib.request.urlopen(URL)
		responseString = connection.read().decode()
		s = json.loads(responseString)
		return s['Stock Quotes'][0]['2. price']
	except:
		return "not found"
 
def main():
  	outFile = open('japi.out', 'w')
  	while 1:
  		userInput = input("Enter chosen stock or 'quit' to exit: ").upper()
  		if userInput != "QUIT":
  			currPrice = 'The current price of {} is: {}\n'.format(userInput, getStockData(userInput))
  			print(currPrice)
  			outFile.write(currPrice)
  		else:
  			break
main() 
		
	
