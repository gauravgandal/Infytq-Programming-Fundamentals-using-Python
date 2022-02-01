#lex_auth_012693816331657216161

def encode(message):
    message_new = message + "0"
    data = []
    counter = 1
    for i in range(0, len(message)):
        if message_new[i]==message_new[i+1]:
            counter += 1
        else:
            data.append(str(counter))
            data.append(message[i])
            counter = 1
    return "".join(data)
    #Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)