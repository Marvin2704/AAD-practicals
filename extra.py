def sum_using_equation(n):
    a=n
    sum = int(a*((a+1)/2))
    count = 1
    print("Sum = ",sum)
    print("No. of iterations = ",count)
    return sum
def sum_using_loop(n):
    a = n
    sum = 0
    count = 0
    for i in range(a+1):
        count+=1
        if i <= a :
            sum = sum+i
            # print("Sum = " ,sum)
    print("Sum = " ,sum)
    print("No. of iterations = " ,count)
    return sum
def sum_using_recurssion(n):
    sum = 0
    count = 0 
    if n == 1:
        sum = 1
        print ("Sum = ",sum)
        print("No. of iterations = " ,count)
    else:
        count +=1
        sum = n + sum_using_recurssion(n-1)
        print("Sum = ",sum)
        print("No. of iteration = ",count)




n = int(input("Enter the number:"))
# sum_using_loop(n)
# sum_using_equation(n)
sum_using_recurssion(n)

