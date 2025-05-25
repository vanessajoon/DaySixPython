#A CAR GAME
print('A car game, Press help to start')
message = input('Enter help to start the game').lower()
started = False
if message == 'help':
    print('''Start - To start the car
    Stop - To stop the car
    Quit - To quit''')

    while True:
      command = input('Enter the follow instructions ').lower()
      if command == 'start':
         if started:
             print('Car is already started')
         else:
             started = True
             print('Car started..Ready to go')
      elif command == 'stop':
         if not started:
             print('Car is already stopped')
         else:
             started = False
             print('Car stopped.')
      elif command == 'quit':
         print('Existing the game bye!')
         break
      else:
         print('I dont understand what you are saying')
else:
    print('invalid option. please type "help" to start')

