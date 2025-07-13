def Check(amount):
    if(amount>5000):
        discount=5
    elif(amount>10000):
        discount=10
    elif(amount>20000):
        discount=20
    else:
        discount=0
    discount=amount*(discount/100)
    final_amount=amount-discount 
    print("final discount is:",final_amount)
Check(9000)
            
