def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    eligible_loan_amount=0
    #Start writing your code here
    if(account_number>999 and account_number<2000):
        if(account_balance>=100000):
            if(salary>25000 and loan_type=="Car"):
                eligible_loan_amount=500000
                bank_emi_expected=36
                if(customer_emi_expected<=bank_emi_expected and loan_amount_expected<=eligible_loan_amount):
                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
                else:
                    print("The customer is not eligible for the loan")
            elif(salary>50000 and (loan_type=="Car" or loan_type=="House")):
                eligible_loan_amount=6000000
                bank_emi_expected=60
                if(customer_emi_expected<=bank_emi_expected and loan_amount_expected<=eligible_loan_amount):
                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
                else:
                    print("The customer is not eligible for the loan")
            elif(salary>75000 and (loan_type=="Car" or loan_type=="House" or loan_type=="Business")):
                eligible_loan_amount=7500000
                bank_emi_expected=84
                if(customer_emi_expected<=bank_emi_expected and loan_amount_expected<=eligible_loan_amount):
                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
                else:
                    print("The customer is not eligible for the loan")
            else:
                print("Invalid loan type or salary")
        else:
            print("Insufficient account balance")
    else:
        print("Invalid account number")

calculate_loan(1005,90000,100000,"Business",7500000,80)