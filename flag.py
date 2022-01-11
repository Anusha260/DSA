l=[8,7,5,4,3,2,6]
flag=0
searched_e=5
for i in range(0,len(l)):
    if l[i]==searched_e:
        flag=i
        break
if flag>0:
    print(flag)
else:
    print(-1)