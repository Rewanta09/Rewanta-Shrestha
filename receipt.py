""" Name: Rewanta Shrestha
student id= s8114226"""


a= input(" Enter the customers name: ")
b=input(" Is the customer a loyality program member? ")
if (b == 'Yes' or b == 'yes'):
    c = int(input(" Enter the number of regular coffee: "))
    d = int(input(" Enter the no of specilaity coffees: "))
    e = int(input(" Enter the no of pastries: "))
    f = int(input(" Enter the no of coffee mugs: "))
    print(" Receipt for ", a)
    print("------------------------------------------------")
    c_p = 3.50
    d_p = 4.50
    e_p = 2.50
    f_p = 8.00
    sales_tax = 0.08
    discount = 0.1
    print(" Regular Coffees: %14.2f"%\
          (c_p * c))
    print(" Specialty Coffees: %12.2f "%\
          (d_p * d))
    print(" Pastries: %21.2f" %\
          (e_p * e))
    print(" Coffee Mugs: %18.2f" %\
          (f_p * f ))
    subtotal = c_p * c + d_p * d + e_p * e + f_p * f
    print(" Subtotal : %20.2f " %\
          (subtotal))
    g = subtotal * discount
    print(" Discount: %20.2f"%\
          -(g))
    print(" Subtotal after Discount: %6.2f"%\
          (subtotal-g ))
    tax = sales_tax * (subtotal-g)
    print(" Tax: %25.2f" %\
          (tax))
    total_cost = tax + (subtotal-g)
    print(" Total Cost: %19.2f "% \
          (total_cost))
    print("---------------------------------------------------")
else:
    h = input("Enter the customer's name(or press enter to exit):")
    
    
    
