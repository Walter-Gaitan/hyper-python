import random

chosen = list(random.choice(['python', 'java', 'kotlin', 'javascript']))
# Write your code here
print('H A N G M A N')
hidden = list('-' * len(chosen))
letters = []
j = 0
start = input('Type "play" to play the game, "exit" to quit:')
while start != 'play':
	if start != 'exit' or start != 'play':
		continue
	elif start == 'exit':cd\\
		break
while j < 8:
	if hidden == chosen:
		print('You guessed the word!')
		print('You survived!')
		break
	print()
	print(''.join(hidden))
	guess = input('Input a letter: ')
	if len(guess) > 1:
		print('You should input a single letter')
	elif guess.isupper() or not guess.isalpha():
		print('It is not an ASCII lowercase letter')
	elif guess in letters:
		print('You already typed this letter')
	elif guess in chosen:
		for i in range(len(chosen)):
			if chosen[i] == guess:
				hidden[i] = guess
				letters.append(guess)
	else:
		print('No such letter in the word')
		j += 1
		letters.append(guess)
else:
	print('You are hanged!')
