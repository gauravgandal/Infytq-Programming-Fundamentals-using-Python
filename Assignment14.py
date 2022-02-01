def find_common_characters(msg1,msg2):
    list=[]
    for x in msg1:
        if x==" ":
            continue
        else:
            for y in msg2:
                if x == " ":
                    continue
                elif x == y:
                    if x in list:
                        break
                    else:
                        list.append(x)
                        break
    output="".join(list)
    if len(output)==0:
        return -1
    else:
        return output
#Provide different values for msg1,msg2 and test your program
msg1="moto"
msg2="moto"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)