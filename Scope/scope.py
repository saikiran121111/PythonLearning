#Global Scope
#Local Scope


name = 'Ruku'

def user(): #By the way this is also defined in global scope so it can be called in any function
    color = 'blue'  # defined in local scope
    def anotherUser():
        print(color)
    anotherUser() # This function cna only be called inside user as its defined in user func
    print(name) # name is defined in global scope


user()
#print(color) -> can't print the variables declared in local scope on global

count = 1
def counter():
    #count = 2 consider as new variable
    global count # Takes the global count value
    count += 1 # increaments it
    print(count)

counter()
#Something called nonlocal is used if we need one variable in nested function
#without this
def colour():
    color = 'red'
    def anotherColour():
        nonlocal color # if we add this then it will take the variable defined in color func
        color = 'blue' #This basically means we creating new variable