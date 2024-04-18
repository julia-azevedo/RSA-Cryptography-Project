# Function that finds the t of the linear congruence of two numbers

def find_t(arrayofquoc, quocCounter):

    i = 0
    tmp = 0
    t = 1
    new = 0

    while(i < quocCounter):

        new = (arrayofquoc[i] * t) + tmp
        tmp = t
        t = new
        i += 1

    if (quocCounter % 2 == 0):
        
        return t
    else:
        return t * (-1)
    
# Function to compute the modular inverse through the extended euclidean algorithm

def invmod(numA, numB):

    tmp = 0
    quoc = []
    counter = 0
    initialnumB = numB

    while(numB != 0):
        
        tmp = numB
        quoc.append(numA // numB)
        numB = numA % numB
        numA = tmp

    inverso = find_t(quoc, len(quoc) - 1)

    return inverso

# Main function to decrypt the message

def decrypt():

    print("Enter the value of 'p', 'q' and the expoent 'e'\n")

    p = int(input("Enter the value of 'p': "))
    q = int(input("Enter the value of 'q': "))
    e = int(input("Enter the value of 'e': "))


    totiente = ((p - 1) * (q - 1))

    n = p * q
    
    d = invmod(totiente, e)

    encrypted_msg = open("encrypted.txt", "r")

    buffer = []

    for line in encrypted_msg:
        for letter in line.split():
            buffer.append(letter)

    decrypted_msg = open("decrypted.txt", "w")

    for letter in buffer:

        tmp = pow(int(letter), d, n)
        
        if(tmp != 28):
            tmp += 63
        
        else:
            tmp = 32
        decrypted_msg.write("%c" % tmp)


