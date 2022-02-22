def menu():
    print('[1] Start timer \n'
          '[2] Stop timer \n'
          '[3] Pause timer \n'
          '[4] Start Pomodoro timer \n'
          '[0] Exit')


menu()
option = int((input('Select an option: ')))

while option != 0:
    if option == 1:
        pass
    elif option == 2:
        pass
    elif option == 3:
        pass
    else:
        print('Choose a correct option')
    print()
    menu()
    option = int((input('Select an option: ')))

print('Goodbye!')
