# Ben Zhao CS550 A block
# Etoa is a world where you can hunt dragons, play blackjack, or even go fishing. It gives the user flexibility with the games that the user wants to play. I hope you enjoy!
# source for borrowed code https://github.com/TigerhawkT3/small_scripts/blob/master/blackjack.py

import sys
import random
import math
import time

#Gameloop

finish = 0 
live = True
while live: 

	print('Welcome to the world of Etoa!')

	time.sleep(2)

	print('You\'ve just entered a world of brand new possibilities. Let\'s see what is in store for you today!' '\n''If you want to fight a dragon, press 1!''\n''If you want to play blackjack, press 2!''\n''If you want to go fishing in the lake, press 3!')


	time.sleep(4)
	#PICK YOUR GAME
	choice = input('So what would you like to do??? :')
	while choice != '1' and choice != '2' and choice!='3':
		print('Sorry. You have not typed in one of the correct choices. Please try again.')
		choice = input('So what would you like to do??? :')
			
		

	#DRAGONHUNT	
	if choice == '1':
		print('Nice choice! Let\'s go to the mountain to hunt for a dragon! Grab your bow and I will see you!')
		time.sleep(2)
		print('...''\n''I see a dragon coming for you!!!! Launch an arrow!''\n''Fighting...''\n' 'You must hit above a 3 to defeat the dragon')
		player = int(random.randint(1,7))
		dragon = int(random.randint(1,3))
		time.sleep(2)
		print('You have hit a', player)
		time.sleep(2)
		print('The dragon has hit a', dragon)

		if player > dragon: 
			print('You have defeated the dragon! You win!')
			finish = 1
			break
		elif player == dragon: 
			print('Tie...')
			finish = 1 
			break
		else:
			print('You have lost...The dragon has burned with you his fiery flame! Sorry')
			finish = 1
			break
			
	#Blackjack Game
	elif choice == '2':
		print('This is one of my favorite activities too! Let\'s go hit the tent for some blackjack!')
		time.sleep(2)
		print('Dealer:\"Welcome to the blackjack tent!\" Come and try your luck to see if you can beat me!')
		#BORROWED CODE FROM TIGERHAWK PYTHON CENTRAL
		deck = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
		random.shuffle(deck)
		

		player1 = [deck.pop() for _ in range(2)]
		dealer = [deck.pop() for _ in range(2)]
		#END OF BORROWED CODE (ABOVE ALLOWS BOTH PLAYERS TO TAKE OUT TWO CARDS EACH AND POP UPDATES THE LIST SO THAT ONCE A VALUE IS GONE, IT DISAPPEARS FROM THE LIST)
		

		
		#DEALER HAS... PLAYER HAS...
		print('You have', player1)
		time.sleep(1)
		print('The dealer has', dealer[1])

		subtotal = sum(player1)
		subtotald = sum(dealer)

		# print(subtotal)
		if subtotal == 21:
			print('Blackjack! You win!')
			finish = 1
			break
		elif subtotald == 21: 
			print('Dealer has blackjack! You lose.')
			finish = 1
			break
		elif subtotal and subtotald == 21: 
			print('Tie.')
			finish = 1
			break

		else: 
			trials = 0
			while trials < 6:
				decision = input('Would you like to Hit [H] or Stay [S]?')
				while decision != 'H' and decision != 'S':
					print('Sorry. You did not pick H or S. Please pick again!')
					decision = input('Would you like to Hit [H] or Stay [S]?') 
					break
				if decision == 'H':
					player1.append(deck.pop(3))
					print(player1)

					if sum(player1) > 21:
						print('Bust. Sorry, you lose.')
						finish = 1 
						break
					else: 
						trials = trials + 1
				elif decision == 'S': 
					if sum(dealer) > 15:
						new1 = dealer.append(deck.pop(1))
						print('Dealer busts. You win!')
						finish = 1 
						break
					if sum(dealer) > 21: 
						print('Dealer busts. You win!')
						finish = 1
						break
				else: 
					if sum(dealer) > sum(player1):
						print('Dealer has', sum(dealer))
						print('He wins')
						finish = 1
						break
					elif sum(dealer) < sum(player1):
						print('Dealer has', sum(dealer))
						print('You win!')
						finish = 1
						break
					else: 
						print('Tie.')
						finish = 1
						break
						#Do you want to play again sequence
	#FISHING GAME
	elif choice == '3': 
		print('Welcome to the lake!')
		time.sleep(1)
		print('....fishing....fishing....fishing...')
		time.sleep(1.5)
		print('You just got a bite. Guess a number from 1 to 5. If your number is correct. You win!')
		from random import *
		fish = randint(1,5)
		print(fish)
		guess = int(input('What is your number?'))

		#if statement for accuracy of guessing number...and deciding if you caught the fish
		if guess == fish: 
			print('You just caught the fish! You won!')
			finish = 1
			break
		else: 
			print('The fish got away.')
			finish = 1
			break
		
	else:
		print('Sorry. You have not typed in one of the correct choices. Please try again.')



	#END MENU
	if finish == 1: 
		live = input('Would you like to play another game? Press 1 if you want to play another game, press any other key if you want to leave: ')
		if live == '1': 
			choice 
		else: 
			print('I am sorry you have to leave. Come play again next time...Bye!')
			break 







