#The provided code stub reads an integer,n , from STDIN. For all non-negative integers i<n , print n^2 

n = int(input('n: '))

if 1<=n<=20:
    for item in range(n):
        print(item*item)


