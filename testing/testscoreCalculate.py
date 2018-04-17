import ScoreCalculate

def main():

	#these are the worst inputs possible 
	x = ["AAPL",'1234','d10@#$','61-3',';','','11111111111111111111111111','here is a stock TWTR']

	for i in range(0,8):
		z = x[i]
		y = ScoreCalculate.scoreCalculate(z)
		print(y)


	print(y)
    

if __name__ == '__main__':
    main() # this calls your main function

