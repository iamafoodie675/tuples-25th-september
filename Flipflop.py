def palind(r):
    end = len(r) -1
    start = 0
    
    while(start<end):
        
        if (r[start] != r[end]):
            return False
        start = start +1
        end = end -1
        
        return True
    
r = (1,2,3,3,2,1)

if (palind(r)):
    print("the tuple is flip flop")
else:
    print("the tuple is not flip flop")
    