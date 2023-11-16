price=float(input("Enter your input here :"))
if(price>=300):
    discount=price*30/100
    print(discount)
elif price<300 and price>=200:

 discount=price*20/100
 print(discount)
elif price<200 and price>=100:
 discount=price*10/100
 print(discount)
elif price<100 and price>0:
    discount=price*5/100
    print(discount)
else:
  
        print("no discount")
