'''



#----------------------------#



'''

import time
from termcolor import colored


class Vehicle:
    def start(self):
        print('Starting engine')

    def stop(self):
        print('Stopping engine')


class TwoWheeler(Vehicle):
    def say(self):
        super().start()
        print("I have two wheels")
        super().stop()


def main_process():
    pulsar=TwoWheeler()
    pulsar.say()
    print(colored('--------------------', 'green'))

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





