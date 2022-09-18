greet=input('').lower().replace("","")
y=greet[0:5]
if(greet=='hello'):
    money=0
elif(y=='hello'):
    money=0
elif(greet[0]=='h'):
    money=20
else :
    money=100
    
print ('$' ,money)