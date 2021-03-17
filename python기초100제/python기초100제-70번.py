# 12, 1, 2 : winter
# 3, 4, 5 : spring
# 6, 7, 8 : summer
# 9, 10, 11 : fall

a = int(input())
if a>=3 and a<=5 :
    print('spring')

elif a>=6 and a<=8:
    print('summer')

elif a>=9 and a<=11:
    print('fall')

else:
    print('winter')
