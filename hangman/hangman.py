from random import sample
word=list(sample(["gravity","ironman","galaxy","meteor","polaris"],1)[0])

guessed_word=['_' for i in range(len(list(word)))]
print("guessed:", ''.join(guessed_word))
avai_guess=10 # max 10 turns.
success=False
for i in range(avai_guess,0,-1):
	letter=input("guess a letter, you have "+str(i)+" chances   ").lower()
	if letter in word:
		guessed_word=[letter if char==letter else guess  for char,guess in zip(word,guessed_word) ]
		print("right guess..", ''.join(guessed_word))
	else:
		print("wrong guess", ''.join(guessed_word))
	if word==guessed_word:
		success=True
		break
if success:
	print("Success")
else:
	print(" thank you. answer:",''.join(word))

