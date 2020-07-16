word = list(input())
snake = ''
for n in word:
	if n.islower():
		snake += n
	else:
		snake += '_' + n.lower()

print(str(snake))
