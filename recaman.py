def rec(n):
    lst=list()
    if n==0:
        return 0
    elif n==1:
        return 1

    elif rec(n-1)-n<=0:
        return rec(n-1)+n

    else:
        for i in range(n):
            x=rec(0+i)
            lst.append(x)
        if rec(n-1)-n in lst:
            return rec(n-1)+n
        else:
            return rec(n-1)-n



