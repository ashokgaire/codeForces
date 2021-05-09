
def power(x,n):

    if n == 0:
        return  1

    temp = power(x,int(n/2))

    if n % 2 == 0:
        return  temp*temp
    else:
        if (n>0):
            return  temp*temp*x
        else:
            return (temp*temp) / x



print(power(3,2))