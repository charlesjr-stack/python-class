#CHARLES PROVISION STORE CHECKOUT SYSTEM
print(" WELCOME TO CHARLES PROVISION STORE ")
print("Available items: Pen, Notebook, Pencil, Eraser")

#customer information COLLECTION
customer_name = input("Enter customer name: ")
selected_item = input("Enter selected item: ")
unit_price = float(input("Enter unit price: "))
quantity = int(input("Enter quantity purchased: "))
student_answer = input("Are you a student? (yes/no): ")
amount_paid = float(input("Enter amount paid: "))

#bill calculation
subtotal = unit_price * quantity
discount = subtotal * 0.10
discounted_amount = subtotal - discount
service_charge = discounted_amount * 0.05
final_total = discounted_amount + service_charge
payment_difference = amount_paid - final_total

#operator skill
points = 0
points = points + quantity
valid_item = selected_item in ("Pen", "Notebook", "Pencil", "Eraser")
payment_sufficient = amount_paid >= final_total
student_eligibility = subtotal >= 1000 and student_answer == "yes"

#Reciept Printing

print("\n====================================")
print("     CHARLES PROVISION STORE RECEIPT")
print("====================================")

print("Customer Name:", customer_name)
print("Item Purchased:", selected_item)
print(f"Unit Price:          {unit_price:.2f}")
print("Quantity:", quantity)
print(f"Subtotal:            {subtotal:.2f}")
print(f"10% Discount:       {discount:.2f}")
print(f"Discounted Amount:   {discounted_amount:.2f}")
print(f"Service Charge (5%):  {service_charge:.2f}")
print(f"Final Total:          {final_total:.2f}")
print(f"Amount Paid:          {amount_paid:.2f}")
print(f"Payment Difference:   {payment_difference:.2f}")

print("------------------------------------")
print("Payment Sufficient:", payment_sufficient)
print("Valid Item:", valid_item)
print("Student Eligibility:", student_eligibility)
print("Points Earned:", points)
print("====================================")
print("Thank you for shopping with us!")
 




