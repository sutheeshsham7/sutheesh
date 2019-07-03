vj,se=input().split()
ma=abs(len(vj)-len(se))
for i in range(len(vj)):
    if len(se)==1 and se[i] in vj:
        break
    if vj[i]!=se[i]:
        ma+=1
print(ma)
