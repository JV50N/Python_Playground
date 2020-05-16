import math
# Simple tip calculator, I'll improve on it once I learn more about python! Enjoy :)
total = input('Please enter amount: ') # Grab user input
total = int(total) # convert the user input string into an int
tax = input('Please enter state tax amount: ')
tip = 0.20

print('-----------------------------')

# Calculations
tax = (total * float(tax) / 100) # Calculate sales tax for item total
total = total + tax # Calculate item_total with sales tax
tip = (float(tip) * total)
total = (float(tip) + total) # Calculate the generous 20% tip into the total

# Round all floats to 2 decimal places
tax = round(tax, 2)
total = round(total, 2)
tip = round(tip, 2)

# Print to CLI
print(f'Your item total before sales tax is ${total}')
print(f'Sales tax for this order is: ${tax}')
print(f'Your total before an expected 20% tip is... ${total}')
print(f'Your tip for this transaction is: ${tip}')