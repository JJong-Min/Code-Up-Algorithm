# 음수이면서 짝수이면, A
# 음수이면서 홀수이면, B
# 양수이면서 짝수이면, C
# 양수이면서 홀수이면, D

a = int(input())
if a<0 and a%2==0:
    print('A')

elif a<0 and a%2!=0:
    print('B')

elif a>0 and a%2==0:
    print('C')

else:
    print('D')
