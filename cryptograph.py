# Function that crpt a message

def encrypt():

    message = input("Enter the message to be encrypted: \n")

    n = int(input("Enter the public key 'n': "))
    print("\n")

    e = int(input("Enter the public key 'e': "))
    print("\n")

    # Transform a string in a list

    message_list = list(message)

    # Transform char values into int

    i = 0 # type: ignore

    while(i < len(message_list)):

        message_list[i] = ord(message_list[i])
        i += 1

        # padronize value in 2 to 28
        i = 0

        while(i < len(message_list)):

            if (message_list[i] > 64 and message_list[i] < 91):
                message_list[i] -= 63

            elif (message_list[i] > 96 and message_list[i] < 123):
                message_list[i] -= 95
        
            elif (message_list[i] == 32):
                message_list[i] = 28
            i += 1

        # Encrypt the message

        i = 0
        tmp = 0
        while(i < len(message_list)):

            tmp = pow(message_list[i], e, n) #fast mod pow
            message_list[i] = tmp % n
            i += 1

        # Save the encrypted message in a file

        encrypted_message = open("encrypted_message.txt", "w")
        for item in message_list:
            encrypted_message.write("%s\n" % item)

        encrypted_message.close()