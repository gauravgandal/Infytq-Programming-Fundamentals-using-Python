def find_max(num1, num2):
    list2=[]
    max_num=-1
    list1=list(range(num1,num2+1))
    if num1>=num2:
        max_num=-1
    else:
        for i in list1:
            temp = i
            temp1=0
            while temp!=0:
                temp1+=temp%10
                temp=temp//10    
            if temp1%3==0 and i%5 ==0 and len(str(i)) == 2:
                    list2.append(i)
        if(len(list2)!=0):
            list2.sort()
            max_num = list2[-1]
        else:
            max_num=-1
    return max_num      
max_num=find_max(24,29)
print(max_num)