import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
length = len(choices)

#user choice
userChoice = input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors : \n")
toInt = int(userChoice)
print(choices[toInt])

#computer choice
compChoice = random.randint(0, length-1)
print("Computer chose :\n")
print(choices[compChoice])

#win or not?
lose = compChoice > toInt
draw = toInt == compChoice

if (toInt == 0 and compChoice == 2) :
    print("You won!")
elif draw :
    print("Draw!")
elif lose :
    print("You lose!")
else :
    print("You won!")