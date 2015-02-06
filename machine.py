#CoinDispenser

class CoinDispenser:

    coins = [25, 10, 5, 1]

    def make_change(self, startingValue):
    	self.coins = [startingValue//25, (startingValue%25)//10, 
    	((startingValue%25)%10)//5, ((startingValue%25)%10)%5]
    	
    	return(self.coins)
