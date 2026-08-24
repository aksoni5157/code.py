# print("hello world")

#Square star pattern
# for i in range(5): 
#     for j in range(5):
#         print("*",end=' ')
#     print()

# Right star pattern.
# for i in range(5): 
#     for j in range(i+1):
#         print('*',end=' ')
#     print()

# Right star in riverse order.
# for i in range(5,0,-1): 
#     for j in range(i):
#         print("*",end=' ')
#     print()

# for i in range(5):

#     for j in range(i):
#         print(" ",end=' ')
#         print("*",end=' ')
#     print ()

# print("hello world")

# file handling

# f=open("student.txt",'r')
# print(f.read())

# f=open("student.txt",'a')
# f.write("hello world")
# f.close()
# f=open("student.txt",'r')
# print(f.read())

# f=open("student.txt",'w')
# f.write("hello world")

import secrets
password=secrets.token_urlsafe(4)
print(password)







