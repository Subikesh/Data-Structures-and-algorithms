def f(Y, x):
    i = 0; j = 9;
    while True:
        k =  (i + j) //2;
        if Y[k] < x:  i = k 
        else: j = k
        if Y[k] != x and  i < j:
            continue
        else:
            break
    if(Y[k] == x):
        print(x," is in the array ")
    else:
        print(x," is not in the array ")

a = list(2 for i in range(1, 11))
print(" Y is ", a)
# for b in a: 
f(a, 5)