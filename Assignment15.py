sen=input("Enter a Sentennce: ").lower().split(" ")
newSen=""
vow=["a","e","i","o","u"]
for i in range(len(sen)):
    if i%2!=0:
        newSen=newSen+(sen[i][::-1])+" "
    else:
        tempvows=[]
        tempcons=[]
        for n in sen[i]:
            if n in vow:
                tempvows.append(n)
            else:
                tempcons.append(n)
        newSen=newSen+"".join(tempvows)
        newSen=newSen+"".join(tempcons)
        newSen=newSen+" "
print(newSen)