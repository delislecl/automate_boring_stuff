import threading
import time
from multiprocessing import Process

print('Start of program.')



def count1(begin):
    test = 0
    for i in range(1000000):
        for j in range(100):
            test = i+j
    print(time.time()-begin)
    return test

begin = time.time()

threadObj1 = Process(target=count1, args=(begin,))
threadObj2 = Process(target=count1, args=(begin,))
#count1(begin)
#count1(begin)
threadObj1.start()
threadObj2.start()

#With args
#threadObj = threading.Thread(target=print('Cats', 'Dogs', 'Frogs', sep=' & '))
#threadObj.start()