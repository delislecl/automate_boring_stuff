import threading, time

print('Start of program.')


def takeANap():
    time.sleep(5)
    print('Wake up!')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program.')

#With args
threadObj = threading.Thread(target=print('Cats', 'Dogs', 'Frogs', sep=' & '))
threadObj.start()