def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    i=0
    total=0
    leng=len(reqd_gems)
    check =  all(item in gems_list for item in reqd_gems)
    if check is True:
        while(i<leng):
            inty=gems_list.index(reqd_gems[i])
            total=total+ price_list[inty]*reqd_quantity[i]
            bill_amount=total
            i=i+1
        if(bill_amount>30000):
            bill_amount=bill_amount-(bill_amount*5)/100
        else:
            bill_amount=total
    else:
        bill_amount=-1
    return bill_amount

#List of gems available in the store
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[1760,2119,1599,3920,3999]

#List of gems required by the customer
reqd_gems=["Ivory","Emerald","Garnet"]

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[3,10,12]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)