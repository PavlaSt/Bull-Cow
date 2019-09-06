# PROJECT 2: Bull Cow

import random
import time

#============================================
def secret_number_generator():
	secret=[]
	i=0
	while i<4:
		num=str(random.randint(0,9))
		if num not in secret:
			secret.append(num)
			i+=1
	secret=''.join(secret)
	return secret
#============================================
def input_taker():
	while True:
		guess=str(input('Please, enter the 4 digit number:'.center(50)))
		if guess.isnumeric() and len(guess)==4:
			return guess
		print('Input has to be exactly 4 digits.'.center(50))
		print()	
#============================================
def comparator(guess,secret):
	tips=1
	while secret!=guess:
		bull,cow=0,0
		for i,dig in enumerate(guess):
			if guess[i]==secret[i]:
				bull+=1
			elif guess[i] in secret:
				cow+=1
		tips+=1
		print(f'{bull} bulls, {cow} cows'.center(50))
		print()
		guess=input_taker()
	return(tips)
#============================================
def evaluator(tips):
	score=['amazing', 'average', 'not so good','pretty bad']
	rating=int(tips/10)
	if rating>3:
		rating=3
	return score[rating]	
#============================================

def main():
	#Introduction
	print('='*55)
	print("Hi there!".center(55))
	print("I've generated a random 4 digit number for you.") 
	print("Let's play a bulls and cows game.")
	print('='*55)
	print()

	#Generate secret number
	secret=secret_number_generator()
	
	#Taking first guess
	guess=input_taker()  

	#Comparing and guessing
	start_time = time.time()
	tips=comparator(guess, secret)
	elapsed_time = int(time.time() - start_time)

	#Rating	and printing result
	print('='*55)
	print()
	print(f"Correct, you've guessed the right number in {tips} guesses! \nIt took you {elapsed_time//60} min and {elapsed_time%60} sec.")
	print(f"That's {evaluator(tips)}.")
#============================================


if __name__ == "__main__":
    main()