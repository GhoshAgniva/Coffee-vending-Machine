# Coffee and Tea Vending Machine

A simple Python program that simulates a coffee and tea vending machine. Users can choose from various beverages, insert coins for payment, and even use a special coupon code for free drinks.

## Features

- Offers **Tea**, **Filter Coffee**, and **Lemon Tea** with distinct recipes.
- Checks if sufficient ingredients are available before preparing the drink.
- Accepts payments through coins (₹5, ₹10, ₹20 denominations).
- Provides change for overpayments.
- Includes a **special coupon code** feature for free drinks.
- Maintains a real-time report of ingredient levels and profits.

## Menu

| Drink         | Ingredients                                 | Cost (₹) |
|---------------|--------------------------------------------|----------|
| **Tea**       | Water: 50ml, Milk: 150ml, Sugar: 15g, Tea: 10g | ₹15      |
| **Filter Coffee** | Water: 50ml, Milk: 150ml, Sugar: 15g, Coffee: 15g | ₹15      |
| **Lemon Tea** | Water: 50ml, Lemon Flavor: 20ml, Sugar: 15g, Tea: 20g | ₹20      |

---

## Installation and Usage

### Prerequisites
- Python 3.x installed on your system.

### Steps to Run the Program
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/vending-machine.git
    cd vending-machine
    ```
2. Run the program:
    ```bash
    python vending_machine.py
    ```

---

## How It Works

1. **Special Coupon Code**:  
   - If the user has a coupon code, they can input it to get a free drink. The code is **1234**.
   - Users have three attempts to enter the correct code.

2. **Choose a Drink**:  
   - Select one of the available drinks: **Tea**, **Filter Coffee**, or **Lemon Tea**.
   - The machine checks if there are enough ingredients to prepare the drink.

3. **Insert Coins**:  
   - Users can insert ₹5, ₹10, or ₹20 coins.
   - The program calculates the total payment.

4. **Drink Preparation**:  
   - If payment is successful, the drink is prepared, and any change is returned to the user.

5. **Reports**:  
   - Type `report` to view the current status of ingredients and total profit.

6. **Shutdown**:  
   - Type `off` to turn off the vending machine.

---

## Example Usage

### Starting the Machine
```plaintext

do you have the special coupon code for free coffee: YES/NO
What you need (TEA / FILTER COFFEE / LEMON TEA): TEA
Please insert a coin: 
Number of 5 rupees coin/coins you have: 2
Number of 10 rupees coin/coins you have: 1
Number of 20 rupees coin/coins you have: 0
Here is your change: 5
Here is your drink: tea


What you need (TEA / FILTER COFFEE / LEMON TEA): REPORT
water=450ml
milk=350ml
coffee=500g
sugar=485g
lemon flavour=500ml
tea=490g
money Rs=15
What you need (TEA / FILTER COFFEE / LEMON TEA): REPORT
water=450ml
milk=350ml
coffee=500g
sugar=485g
lemon flavour=500ml
tea=490g
money Rs=15



vending-machine/
│
├── vending_machine.py      # Main Python program
└── README.md               # Documentation for the project




![337c3951853579 58fc76482621b](https://github.com/GhoshAgniva/Coffee-vending-Machine/assets/130777118/11eadd3e-ee53-4265-9fa6-52fd862b0165)

