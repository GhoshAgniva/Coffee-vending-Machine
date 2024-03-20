Coffee Vending Machine

Introduction

This code simulates a coffee vending machine that allows users to select
from a variety of beverages and dispenses them upon successful payment.
It manages ingredient inventory, simulates coin insertion, and provides
change if necessary.

#Features

#Menu: Offers three beverage options: Tea, Filter Coffee, and Lemon Tea.
Inventory Management: Tracks available quantities of water, milk,
coffee, sugar, lemon flavor, and tea. Payment Processing: Simulates
inserting 5, 10, and 20 rupee coins to make payment. Change Dispense:
Provides change for any overpayment. Reporting: Displays current
ingredient levels and total profit. Special Coupon (Optional): Allows
for a limited number of free drinks using a secret code (commented out
by default). How to Use

Run the Python script. Enter a coupon code (optional). You have 3
attempts to enter a valid code (currently commented out). Select your
desired beverage (Tea, Filter Coffee, Lemon Tea) or \"report\" to check
inventory and profit. For valid beverage selections: The program checks
if sufficient ingredients are available. If yes, it prompts you to
insert coins (5, 10, or 20 rupees). It calculates and verifies if the
inserted amount is enough to cover the beverage cost. Upon successful
payment, it dispenses the drink and provides change if necessary. Type
\"off\" to exit the program. Code Structure

The code is well-organized with clear function definitions:

check_meterials(check_items): Verifies if enough ingredients are
available for a desired drink. coin_process(): Simulates coin insertion
and calculates the total amount entered.
is_payment_successful(money_received, coffee_cost): Checks if the
payment is sufficient and dispenses change if necessary.
make_drink(drink_name, drink_meterials): Reduces ingredient quantities
and prints a message after successfully dispensing the drink.
Customization

You can modify the menu dictionary to add or remove beverages and adjust
their prices and ingredient requirements. Adjust the initial ingredient
quantities in the items dictionary. Uncomment the coupon code logic
(currently disabled) and set a custom password in the couponRetryCounter
section. Further Enhancements

Implement a more visual interface (e.g., using libraries like tkinter or
a web framework). Connect to real hardware for dispensing drinks and
collecting payments. Integrate error handling for invalid user inputs.
Consider adding additional payment options like cashless transactions



![337c3951853579 58fc76482621b](https://github.com/GhoshAgniva/Coffee-vending-Machine/assets/130777118/11eadd3e-ee53-4265-9fa6-52fd862b0165)

