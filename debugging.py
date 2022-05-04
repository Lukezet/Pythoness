def divisors(num):
    divisors=[]
    while True:
        try: 
            if num<0:
                raise Exception
            for i in range(1,num+1):
        
                if num%i==0:
           
                    divisors.append(i)
            break            
        
        except Exception:
            num=int(input("you have to enter only positive numbers, please enter a number"))
    
    return divisors

def run():
    while True:

        try:
            num=int(input("enter a number"))
                          
            print(divisors(num))
        
            print("Terminó")

            break
        
        except ValueError:
            print("Only can enter numbers")
    

if __name__=='__main__':
    run()