#Upgraded Timer
import time
import sys
import string
print('How much time would you like to put on the timer? (Enter a number)')
timertime=input()
while True:
    if timertime==str('quit') or timertime==str('Quit') or timertime==str('QUIT'):
        print('Bye!')
        sys.exit()
    try:
        time.sleep(int(timertime))
        print('Done!')
        time.sleep(1)
        print('How much time would you like to put on the timer? (Enter a number)')
        print('To quit, type quit.')
        timertime=input()
    except ValueError:
        print('Please enter a number, or quit by typing \'Quit\' or \'quit\'.')
        timertime=input()
    


   
