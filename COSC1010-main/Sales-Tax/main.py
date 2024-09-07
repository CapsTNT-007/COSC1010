#
# Name Tayson
# Date 9/7/2024
# Sales Tax Programming Project
# COSC 2409 DNT
#

# Variable declarations
purchase = 0
state_tax = 0
country_tax = 0
tax = 0
total = 0
# Constants for the state and county tax rates
state = 0.05
country = 0.025
# Get the amount of the purchase.
purchase = int(input('How much what the purchase amount?'))
# Calculate the state sales tax.
state_tax = int(purchase)*(state)
# Calculate the county sales tax.
country_tax = int(purchase)*(country)
# Calculate the total tax.
tax = state_tax + country_tax
# Calculate the total of the sale.
total = tax + purchase
# Print information about the sale.
print("Amount purchased:")
print(purchase)
print("state tax:")
print(state_tax)
print("country tax:")
print(country_tax)
print("total tax:")
print(tax)
print("total:")
print(total)