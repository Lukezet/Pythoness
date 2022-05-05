def divisors(num):
    divisors=[]
    for i in range(1,num+1):
        if num%i==0:
            divisors.append(i)
    return divisors

def run():
    while True:
        num=input("enter a number")
        assert num.isnumeric() and int(num)> 0, "You only have permission to enter positive numbers"
        print(divisors(int(num)))
        print("FINISHED")
        break

if __name__=='__main__':
    run()