def add_binary(a, b):
    a=a.replace('0b',"")[::-1]
    b=b.replace('0b',"")[::-1]
    x=0
    y=0
    for i in range(len(a)):
        if a[i]=='1':
            x+=2**i
    for i in range(len(b)):
        if b[i]=='1':
            y+=2**i
    tot=x+y
    res="" 
    while tot>0:
        res+=str(tot%2)
        tot//=2
    return "0b"+res[::-1]
        
        
        
        
            
            