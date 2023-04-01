from sympy import*
def maxima_minima(f,x) :
    diff1=diff(f,x)
    diff2=diff(f,x,2)
    print(f"first diff : {diff1}\nsecond diff:{diff2}")
    extrema=solve(diff1,x)
    return extrema
x = symbols("x")
f = ln(x)
print(maxima_minima(f, x))
