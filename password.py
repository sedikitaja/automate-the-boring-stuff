password = 'swordfish'
usrpw = ''
count = 0

while usrpw != password and count <= 2:
    count = count+1
    print('Enter your password.')
    usrpw = input()
    print(str(count))
    if usrpw == '':
        count = count-1
        print ('You did not enter a password')
        print('You have ' + str(int(3) - int(count)) +' attempts remaining.')
        if count == 2:
            print('This is your final attempt')
    elif usrpw != password:
        print('Wrong password you numpty :)')
        print('You have ' + str(int(3) - int(count)) +' attempts remaining.')
    elif count == 2:
        print('Last attempt')

if usrpw == password:
    print('Thanks!')
    print('Access granted.')
else:
    print('Access Denied.')
