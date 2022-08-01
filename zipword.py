import zipfile
import time

location = input("file Location:\t")
zipf = zipfile.ZipFile(location)

result = 0
tried = 0
c = 0

if not zipf:
    print(
        f"Zip file {location} is not password protected, you can open it successfully")

else:
    wordListFile = open("wordList.txt",'r')
    words=[]

    body = wordListFile.read().lower()
    words = body.split('\n')
    
    starttime = time.time()

    for i in range(len(words)):
        word = words[i]
        password=word.encode('utf8').strip()
        c=c+1
        print(f'Guesses: {word}')
        try:
            with zipfile.ZipFile(location,'r') as zf:
                zf.extractall(pwd=password)
                print("Success! The password is: "+ word)
                endtime = time.time()            
                result = 1                       
            break
        except:
             pass

    if result == 0:
        print("Sorry, password not found. A total of "+str(c) +
              "+ possible combinations . Password is not of 4 characters.")
    else:
        duration = endtime - starttime
        print('Congratulations!!! Password found after trying ' +
              str(c)+' combinations in '+str(duration)+' seconds')
