menu={
    'pizza':100,
    'tea':20,
    'coffee':80,
    'pasta':50,
    'poha':30,
    'salad':70,
    'samosha':15,
    'Burger':60

}
print('Welcome to om restorant!')
print('1.pizza=rs100\n2.tea=rs20\n3.coffee=rs80\n4.pasta=rs50\n5.Burger=rs60\n6.Salad=70\n7.Poha=30\n8.Samosha=15')

total_order=0


for i in  range(1,7) :
    

    order=input("Do you want order(yes/no): ")
    
    if order=="no":
      print(f"If the total amount is: {total_order}")
      print("stop")
      break
      
    else:
       
       
       select_1=input("Enter the your item: ")

       if select_1  in menu:
         total_order += menu[select_1]
         print(f"your order is place {select_1}")
       else:
        print(f'not aviable {select_1}')
        


        print(f"If the total amount is: {total_order}")

