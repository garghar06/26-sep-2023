
def rec(n):
    if(n<=1):
        return n
    else:
        return(rec(n-1)+rec(n-2))

terms=4
print("Fibonacci sequence ")
for i in range(terms):
    print(rec(i))