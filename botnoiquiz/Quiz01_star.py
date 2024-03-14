def starS(n):
# Forward to n pattern 
    for i in range(n+1):
        print("*"*i)
    
# Backward from n-1 pattern
    for i in reversed(range(n)):
        print("*"*i)
    

n = int(input('n = '))
starS(n)




