import math

# Function to check if a number is prime

def check_prime(n):

    if(n== False or n ==True):

        return False
    
    if (n % 2 == 0):

        return False
    

    divider = 3

    while(divider <= math.sqrt(n)):

        if(n % divider == 0):

            return False

        divider += 2

    return True



# Function to compute maximum common divisor through Euclidean Algorithm

def euclidean(num1, num2):

    if(num1 < num2):
        
        temp = num1
        num1 = num2
        num2 = temp

    while(num2 != 0):

        leftover = num1 % num2
        num1 = num2
        num2 = leftover

    return num1

# Main function to generate keys

def generate_keys():

    print("Key Generator:\n")

    print("Enter two numbers 'p' and 'q' and a expoent 'e' coprime to 'p'*'q'\n ")

    p = int(input("Enter a prime number 'p': "))
    q = int(input("Enter a prime number 'q': "))
    e = int(input("Enter an expoent 'e': "))


    if(check_prime(p) == False or check_prime(q) == False):

        print("Error: p and q must be prime numbers\n")
        return
    
    n = p*q
    phi = (p-1)*(q-1)


    if(euclidean(phi, e) != 1):
            
        print("Error: e must be coprime!\n")
        return


    public_key = open("public_key.txt", "w")
    public_key.write("n = " + str(n) + "\n")
    public_key.write("e = " + str(e) + "\n")
    public_key.close()