import random
user_choice=input('choose your weapon[rock,paper,scissor]:')
computer_choice=random.choice(['rock','paper','scissor'])
#elif user_choice!==
print('user choice:',user_choice)
print('computerchoice:',computer_choice)

if user_choice=='rock' and computer_choice=='rock':
  print('draw')
elif user_choice=='rock' and computer_choice=='paper':
  print('computer won')
elif user_choice=='rock' and computer_choice=='scissor':
  print('user won')
elif user_choice=='paper' and computer_choice=='rock':
  print('user won')
elif user_choice=='paper' and computer_choice=='paper':
  print('draw')
elif user_choice=='paper' and computer_choice=='scissor':
  print('computer won')
elif user_choice=='scissor' and computer_choice=='rock':
  print('computer won')
elif user_choice=='scissor' and computer_choice=='paper':
  print('user won')
elif user_choice=='scissor' and computer_choice=='scissor':
  print('draw')
'''
num1=2
num2=3
print(num1==2 and num2==3)
print(num1==2 and num2==2)
print(num1==4 and num2==3)
print(num1==4 and num2==4)
#or operator
print(num1==2 or num2==3)
print(num1==2 or num2==2)
print(num1==4 or num2==3)
print(num1==4 or num2==4)
'''



