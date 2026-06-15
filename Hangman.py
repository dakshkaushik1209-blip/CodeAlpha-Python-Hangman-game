import random
words = ["python","java","apple","coding","tiger","glasses","zoo"]
word = random.choice(words)
chosen_letter=[]

attempts = 8
while attempts > 0:
    display=""
    for letter in word:
        if letter in chosen_letter:
            display+=letter+" "
        else:
            display+="_ "
        
    if "_" not in display:  
        print(display)
        print("Congratulation You Won The Game")
        break
    print(display)
    guess=input("enter letter :- ").lower()
    if len(guess) !=1:
        print("Give one letter at a time")
        continue
    chosen_letter.append(guess)
    if guess in word:
        print("Correct")
    else:
        attempts-=1
        print("Wrong")
        print(f"You have {attempts} attempts left")
    if attempts ==0:
        print("You lost the game")
    if guess in chosen_letter:
        print("You already guessed this letter")
