def Check(amount):
    if(amount>=50000):
        discount=5
    elif(amount>=10000):
        discount=10
    elif(amount>=20000):
        disount=20
    else:
        discount=0
        discount=amount*(discount/100)
        final_amount=amount-discount 
        if discount==5:
            print("5%discount",discount)
        elif discount==10:
            print("10%discount",discount)
        elif discount==20:
            print("20%discount",discount)
        print("final amount is:",final_amount)    
check=(9000)
    