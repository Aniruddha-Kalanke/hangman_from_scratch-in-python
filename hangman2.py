import random
letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','w','u','v','x','y','z']
number=random.randint(1,10)
word=""
for char in range(1,number+1):
    word+=random.choice(letter)
total_word=len(word)
print(f"The total length of the word in the sentence are exactly {total_word}")
user_guess=0
lives=7
guess=[]
print(word)
while lives!=0:
    user_input=input("guess the letter inside the text you have gotten 7 starting chances: ")
    if user_input in word:
        guess.append(user_input)
    else:
        lives-=1
print(guess)
userguestimate="".join(guess)

if userguestimate==word:
    print("you have successfully won hangman")
else:
    print("i am sorry to announce you have lost the game actually")
print(word)

