
# #1
# with open('greetings.txt','w') as file:
#     file.write('Hello\n')
#     file.write('Hi\n')
#     file.write('Hey\n')
#
# with open('greetings.txt','r') as readFile:
#     lines = readFile.readlines()
#     for i in lines:
#         print(i.strip())
#

# #2
#
# with open('diary.txt','w') as diaryFile:
#     diaryFile.write('Day 1: Started Python\n')
#
#
# with open('diary.txt','a') as appendDiary:
#     appendDiary.write('Day 2: Learned file operations\n')
#
# with open('diary.txt','r') as readingDiary:
#     diary = readingDiary.readlines()
#     for i in diary:
#         print(i.strip())

# #3
#
# def save_contacts(name,phone):
#
#     with open('contacts.txt','a') as phoneBook:
#         phoneBook.write(f'{name}:{phone}\n')
#
# def load_contacts():
#     try:
#         with open('contacts.txt','r') as readPhone:
#             phonebook = readPhone.readlines()
#             for i in phonebook:
#                 print(i.strip())
#     except FileNotFoundError as e:
#         print(f'File Not Found {e}')
#
#
# save_contacts('ruku','123')
# save_contacts('sai','456')
# save_contacts('kiran','789')
#
# load_contacts()

# #4
#
# def add_task(tskno,task):
#
#     with open('todo.txt','a') as todowrite:
#         todowrite.write(f'{tskno}.{task}\n')
#
# def show_task():
#
#     try:
#         with open('todo.txt','r') as todoread:
#             todocheck = todoread.readlines()
#
#             for i in todocheck:
#                 print(i.strip())
#     except FileNotFoundError as e:
#         print(f'File Not found {e}')
#
# add_task(1,"tak1")
# add_task(2,"task2")
# add_task(3,"task3")
#
# def complete_task(number):
#     try:
#         with open('todo.txt','r') as todocomplete:
#             todocheck = todocomplete.readlines()
#             with open('todo.txt','w') as todowritecomp:
#                 for i in todocheck:
#                     checktask = i.split('.')
#                     if int(checktask[0]) == number:
#                         continue
#                     todowritecomp.write('.'.join(checktask))
#
#     except FileNotFoundError as e:
#         print(f'File Not found {e}')
#
# complete_task(3)
# show_task()
