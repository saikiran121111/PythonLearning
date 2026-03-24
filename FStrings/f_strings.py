coins = 3
user = 'sai'
print(f'I am {user} and I have {coins} coins')

# This will help us to escape using + and concatenate and converting int into string etc...

#There are multiple ways to use fstrings

message = 'I am %s and I have %s coins' % (user, coins)# 1 way
print(message)
message2 = 'I am {} and I have {} coins'.format(user, coins)# 2 way
print(message2)

message3 = 'I am {1} and I have {0} coins'.format(coins, user)# 3 way giving index to show their position
print(message3)

message4 = 'I am {user} and I have {coins} coins'.format(user=user,coins=coins )# 4 assigning values
print(message4)

#pulling values from dictionary #5 way
player = {'user':'kiran','coins':12}
message5 = 'I am {user} and I have {coins} coins'.format(**player)
print(message5)


#f_strings best way

mes = f'I am {user.upper()} and I have {coins * 10} coins' #can use the formats like .lower() calculations etc and they will work
print(mes)

mes2 = f"I am {player['user']} and I have {player['coins'] * 10} coins"
print(mes2)

#You can pass formatting options
value = 10

format = f'The value of 2.25 times {value} is {2.25*value:.2f}'
print(format)

for i in range(1,11):
    print(f'{i} divided by 6.75 is {i/6.75:.2%}')