num,sim=input().split()
var=0
if len(num)>len(sim):
  num,sim=sim,num
p=0
while p<len(num):
  var+=(ord(sim[p])-ord(num[p]))
  p+=1
for p in range(p,len(sim)):
  var+=ord(sim[p])-ord('a')+1
print(var)
