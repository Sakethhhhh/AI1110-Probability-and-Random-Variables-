import random
t=1000000 #enter sample size
t1=t
sum=0
while(t>0):
    roll1=random.randint(1,6)
    roll2=random.randint(1,6)
    if(roll1==6):
        sum+=1
    if(roll2==6):
        sum+=1
    t-=1
sum=sum/t1;
print(sum)
