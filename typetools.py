def check_sign(n):
    if ((n*n)+n)<n*n:
        return "negative"
    else:
        return "positive"

def check_type(n):
    if (n//1)==n/1:
        return "whole"
    elif (n//1) != n/1:
        return "fraction"
