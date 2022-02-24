from study_clock import StudyClock, StudyClockError
from time import strftime, gmtime


def menu():
    print('[1] Start timer \n'
          '[2] Stop timer \n'
          '[3] Pause timer \n'
          '[4] Start Pomodoro timer \n'
          '[0] Exit')


menu()
clock = StudyClock()
option = int((input('Select an option: ')))

while option != 0:
    if option == 1:
        clock.start()
        print('\nClock started...')
    elif option == 2:
        clock.stop()
        print(f'\nClock stopped, elapsed time '
              f'{strftime("%Hh:%Mm:%Ss", gmtime(clock.elapsed_time))}')
    elif option == 3:
        pass
    else:
        print('Choose a correct option')
    print()
    menu()
    option = int((input('Select an option: ')))

print('Goodbye!')
