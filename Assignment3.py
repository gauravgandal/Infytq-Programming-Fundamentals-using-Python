def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0

    #Start writing your code here
    #Populate the variables: five_needed and one_needed
    total=no_of_five*5+no_of_one
    if(total>=rupees_to_make):
        five_needed=rupees_to_make//5
        one_needed=rupees_to_make%5
        if(five_needed<=no_of_five and one_needed<=no_of_one):
            print("No. of Five needed :", five_needed)
            print("No. of One needed  :", one_needed)
        elif(five_needed>no_of_five and one_needed<no_of_one):
            one_needed=rupees_to_make-no_of_five*5
            five_needed=no_of_five
            print("No. of Five needed :", five_needed)
            print("No. of One needed  :", one_needed)
        elif(no_of_five>=five_needed and no_of_one<one_needed):
            print(-1)
    else:
        print(-1)


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print("No. of Five needed :", five_needed)
    #print("No. of One needed  :", one_needed)
    #print(-1)


#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program

make_amount(93,19,2)