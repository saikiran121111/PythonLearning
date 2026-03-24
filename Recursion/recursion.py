#Recursion is something when a function calls itself

def recurr(num):
    if (num >=9):
        return num + 1
    else:
        total = num+1
        print(total)
        return recurr(total)
mynewNum = recurr(0)
print(mynewNum)

# Think of it like a stack of people where each person shouts a question to the next —
# once the last person answers, the answer travels back through every single person
# in reverse order before reaching the first.