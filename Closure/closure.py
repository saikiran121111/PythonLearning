# Closure is a function having access to the scope of its parent.
# function after the parent function is returned.

def parentsfunc(player):
    coin = 3
    def childfunc(): # This is a clusure function
        nonlocal coin
        coin -= 1

        if coin > 1 :
            print(player+ ' has '+ str(coin)+' coins left')
        elif coin == 1:
            print(player+ ' has only '+ str(coin)+' coin left')
        else:
            print(player+ ' is out of coins')

    return childfunc # if we use () it will call function and returns the value
# if we don't use () it returns function itself


sai = parentsfunc('sai') # Creates new function
sai()
sai()
sai()