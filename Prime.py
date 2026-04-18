import math

#Define the function to calculate a prime number
def Prime(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return True

while True:
    user_input = input("Enter you numeral: ")
    
    if user_input=="close":
        print("Shutdown")
        break

    #Ask a user for a integer
    number=int(user_input)


    #Check if the integer is prime
    if Prime(number):
        print(number, "is Prime")
    else:
        print(number, "is not Prime")