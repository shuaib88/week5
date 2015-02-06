#CoinDispenser

class CoinDispenser:

    coins = [25, 10, 5, 1]

    def make_change(self, startingValue):
    	if startingValue < 5:
    		self.coins = [0, 0, 0, startingValue]
    	
    	elif startingValue > 4 and startingValue < 10:
    		self.coins = [0, 0, startingValue//5, startingValue%5]

    	elif startingValue > 9 and startingValue < 25:
    		self.coins = [0, startingValue//10, (startingValue%10)//5, (startingValue%10)%5]
    	
    	elif startingValue > 24:
    		self.coins = [startingValue//25, (startingValue%25)//10, ((startingValue%25)%10)//5, ((startingValue%25)%10)%5]

    	return(self.coins)
