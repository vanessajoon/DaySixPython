#to reverse a number
# num = int(input('Enter four numbers '))
# while num > 0:
#     digit = num % 10 #To get the last digit
#     print(digit)
#     num = num // 10 # remove the last digit

#Find how many digits are there in a string
# num = input('Enter a strings of num to know to know many digits are there ')
# count = 0
# while count < len(num):
#     count +=1
# print(f'The number has {count} digits')

#Password checker with 3 limits
# password = 'Vanny123'
# maxAttempts = 3
# attempts = 0
# user = input('Enter your password \nYou have only 3 attempts ')
# while attempts < maxAttempts:
#
#     if user == password:
#         print('Password Correct \n Access Granted')
#         break
#     else:
#         attempts +=1
#         print('Password Incorrect ')
#         leftAttempts = maxAttempts - attempts
#         print(f'Try again you have only {leftAttempts} attempt remaining')
#         user = input('Enter your password again ')
# if attempts == maxAttempts:
#     print('LOGGED OUT')
#     print('You have exceeded your 3 attempts')

#sum of numbers
# print('You are to keep entering numbers till the sum is 100')
#
# count = 0
# total  = 0
# while total < 100:
#     num = int(input('Enter a number '))
#     if total + num > 100:
#         print('Number is too big! It will make the sum more than 100. Try a smaller number')
#         continue # to skip it
#     total = total + num
#     count +=1
# print(f'The total sum is {total}')
# print(f'You enter {count} numbers')

#Find the first number divisible by both 3 and 7 between 1 - 100
# count = 0
# while True:
#     num = int(input('Enter a number'))
#
#     if num > 100:
#         print('Number is too big! It will make the sum more than 100. Try a smaller number')
#         continue
#     count += 1
#
#     if num % 3 == 0 and num % 7 == 0:
#         print(f'This number {num} is divisible by both 3 and 7')
#         break
#     else:
#         print('Not divisible by both 3 and 7, Try again.')
# print(f'You enter {count} digit ')






#The secret word chalange
# print('To check if a number is divisible by 3 or 7 or both 3 and 7')
# count = 0
# while True:
#     num = int(input('Enter any number from 1-100 '))
#
#     if num > 100:
#         print('Number is too big! It will make the sum more than 100. Try a smaller number')
#         continue
#     count +=1
#     if num % 3 == 0 and num % 7 == 0:
#         print('FizzBuzz')
#         print('Can be divided by both 3 and 7')
#         break
#     elif num % 7 == 0:
#         print('Buzz')
#         print('Can be divided by 7')
#
#     elif num % 3 == 0 :
#         print('Fizz')
#         print('Can be divided by 3')
#
#     else:
#         print('Number cannot be divided by 3 or 7 or both')
# print(f'You entered {count}digits')

#Number guessing game
# print('This is a number guessing game. \nHint: the number is less than 20, and you have only five tries')
# number = 15
# attempts = 0
# maxAttempts = 5
#
#
# while attempts < maxAttempts:
#     num = int(input('Enter a number to guess the hidden number'))
#     if num == number:
#         print('You Guessed Right, Congratulations!!!')
#         break
#
#     else:
#         attempts +=1
#         print('Wrong!! Try Again')
#         leftAttempts = maxAttempts - attempts
#         print(f'You have only {leftAttempts} left')
#
#     if num > 20:
#         print('Number too high, try something lower')
#     elif num < 10:
#         print('Number to low, try something higher ')
#     continue
# if attempts == maxAttempts:
#     print('You have exceeded your tries\n You cant try again sorry')


#Simple login
username = 'Vannjoon'
password = 'Kimnamjoon'
attempts = 0
maxAttempts = 3

while attempts < maxAttempts:
    user = input('Enter your username to login')
    passkey = input('Enter your password to log in')

    if user == username and passkey == password:
        print('LOG IN SUCCESSFUL')
        break

    attempts +=1
    leftAttempts = maxAttempts - attempts

    if user != username and passkey == password:
        print('Username incorrect! Try again')
        print(f'You have {leftAttempts} tries left')
    elif passkey != password and user == username:
        print('Password incorrect! Try again')
        print(f'You have {leftAttempts} tries left')
    elif user!= username and passkey != password:
        print('Password and user name are incorrect! Try Again')
        print(f'You have {leftAttempts} tries left')
    else:
        print('Try again')


if maxAttempts == attempts:
 print('You have exceeded the amount of tries \nYou are logged out')
 print(f'You used all your {attempts}attempts')