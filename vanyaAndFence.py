n,h=[int(i) for i in raw_input().split()]
x=[int(i) for i in raw_input().split()]
sum=0
for i in x:
    if i>h:
        sum+=2
    else:
        sum+=1
print sum
