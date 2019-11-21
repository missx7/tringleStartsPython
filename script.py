// only recursive function
def pettren(i, n):
    if i == n:
        return 
    else:
        print(" ".join(['*' for x in range(i,n)]))
        return pettren( i + 1, n )


pettren(0,8)

