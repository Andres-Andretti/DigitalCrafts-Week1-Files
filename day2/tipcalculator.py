# Activity 2

total_amount = int(input("Enter the total amount: "))
tip_percentage = int(input("Enter the tip percentage amount: "))
# tip_amount = ((int(total_amount)) * (int(tip_percentage) / 100)

def calculate_tip():
    return (int(total_amount) * (tip_percentage / 100))
   
tip = calculate_tip()
print(tip)