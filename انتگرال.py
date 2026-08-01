F=input("Enter the function expression:")
b=float(input("Enter the upper limit of the integral:"))
a=float(input("Enter the lower limit of the integral:"))
def evaluate_function(expr, x):
    local_vars = {"x": x}
    exec("out = " + expr, {}, local_vars)
    return local_vars["out"]
n = 1000
sum = 0
h = (b-a) / n
for i in range(1,n+1):
    x1 = a + (i-1)*h
    x2 = a + i*h
    fx1 =  evaluate_function(F, x1)
    fx2 =  evaluate_function(F, x2)
    s = ((fx1 + fx2 )*h)/2
    sum+=s
print(sum)


