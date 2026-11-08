base_price=15
age=21
seat_type="gold"
show_time="Evening"
if age>17:
    print("User is eligible to book a ticket")
if age>=21:
    print("User is eligible for Evening shows")
else:
    print("User is not eligible for Evening shows")
is_member=False
is_weekend=False
discount=0
if is_member and age>=21:
 discount=3
 print("User qualifies for membership disocunt")
else:
   print("User does not qualify for membership discount")
print('discount:',discount)
extra_charges=0
if show_time=='Evening' or is_weekend :
   extra_charges=2
   print('Extra charges will be applied')
else:
   print("No extra charges will be applied ")
print('Extra charges:',extra_charges)
if age>=21 or age>=18 and (show_time!='Evening' and is_member):
   print('Ticket booking condition satisfied')
   service_charges=0
   if seat_type=='premium':
      service_charges=5
   elif seat_type=='gold':
      service_charges=3
   else:
      service_charges=1
   print('Service charges:',service_charges)
   final_prices=base_price + extra_charges + service_charges - discount
   print('Final price of ticket:',final_prices)
else:
   print('ticket booking failed due to restrictions')