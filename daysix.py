#While LOOPS
#Reverse loop
# i = 10
# while i >=1:
#     print( i)
#     i = i - 1

#loop to 10
# i = 1
# while i <=10:
#     print(i)
#     i = i + 1

#adding of the total numbers
# num = 1
# total = 0
#
# while num <=10:
#     total = total + num
#     num = num +1
# print(f'The total sum is: {total}')


#even number
# num = 0
# while num <= 10:
#     if num % 2 == 0:
#         print(num)
#     num = num + 1


#Guess the number correctly
# num = int(input('''Enter random num to guess what number ends the loop...
#                    Hints: the number is less than 10 '''))
#
# while num != 0:
#     print('Number not guessed correctly')
#     num = int(input('Enter number again'))
#
# print('Number guessed correctly ')


#Multiplication table using while loop
# intake = int(input('Enter a number to print its multiplication table '))
# num = 1
# while  num <=12:
#     multi = intake * num
#     print(f'{intake} * {num} = {multi}')
#     num = num + 1


#Password checker
# correctPassword = 'Vanny123'
# attempts = 0
# maxAttempts = 3
#
# while attempts < maxAttempts:
#     user = input('Enter correct password ')
#
#     if user == correctPassword:
#         print('Password correct')
#         print('Access Granted')
#         break
#     else:
#         attempts +=1
#         print(f'Password Incorrect try again')
#         leftAttempts = maxAttempts - attempts
#         print(f'You have only {leftAttempts} attempts left')
# if attempts == maxAttempts:
#     print('You have exceeded your attempts, You are logged out')

#sum of digits
# print('Enter any number to add. Press zero to cancel')
# total = 0
# count = 0
# num =int(input('Enter a number '))
# while num != 0:
#     total = total + num
#     count += 1
#     num= int(input('Enter another num to add to the previous one '))
# print(f'You entered {count} numbers')
# print(f'The addition of the total numbers are {total} ')

#factorial
# print('To calculate the factorial of a number')
# num = int(input('Enter a number '))
# count = 1
# total = 1
# while count <= num:
#     total = total * count
#     print(f'{count}! so far = {total}')
#     count +=1
# print(f'The factorial of {num} is {total}')

#sum of numbers 1-100
# num = 100
# count = 1
# total = 0
#
# while count <= num:
#     total = total + count
#     count +=1
# print(f'Total numbers from 1-100 is {total}')

#print digits one by one

num = input('Enter 4 numbers')
count = 0
while count < len(num):
    print(num[count])
    count +=1
