n=input()
x=raw_input()
d=0
a=0
for i in x:
    if i=="D":
        d+=1
    else:
        a+=1
if a>d:
    print "Anton"
elif a<d:
    print "Danik"
else:
    print "Friendship"
