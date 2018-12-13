import subprocess

calcProc = subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")

calcProc.wait()

#poll return 0 when program is done
calcProc.poll()

#Run python files
subprocess.Popen(['C:\\Users\\Clement\\Anaconda3\\python.exe', 'hello.py'])


#Opening files with default apps
fileObj = open('hello.txt', 'w')
fileObj.write('Hello world!')
fileObj.close()
subprocess.Popen(['start', 'hello.txt'], shell=True)