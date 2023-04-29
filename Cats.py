print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >=4:
        print('That is a lot of cats. You crazy lady.')
    elif int(numCats) <=0:
        print('You cannot have negative cats, you monster.')
    else:
        print('That is not enough cats, you disappoint Simon the god of Cats.')
except ValueError:
    print('You did not enter a number.')
