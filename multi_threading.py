from time import sleep
from threading import Thread
class Hello(Thread):
    def run(self):      #You always need to use name of function as run cz it is built-in
        for _ in range(5):

            print('Hello')
            sleep(1)

class Hi(Thread):
    def run(self):
        for _ in range(5):

            print('Hi')
            sleep(1)

t1 = Hello()
t2 = Hi()
t1.start()    #instead of t1.run you have to use t1.start to create a different thread.
sleep(0.2)
t2.start()

t1.join()  #this will make sure main thread to wait for thread t1 to get executed first
t2.join()  #this will make sure main thread to wait for thread t2 to get executed first

print('Bye')