#defining the menu by using nested dicsnary

menu={
    "tea":{
    "meterials":{
        "water":50,
        "milk":150,
        "sugar":15,
        "tea":10
    },
     "cost":15
    },
    "filtercoffee":{
        "meterials":{
            "water":50,
            "milk":150,
            "sugar":15,
            "coffee":15
        },
         "cost":15
    },
     "lemontea":{
         "meterials":{
            "water":50,
            "lemon flaviour":20,
            "sugar":15,
            "tea":20
         },
         "cost":20
     }
}


profit=0
items={
    "water":500,
    "milk":500,
    "coffee":500,
    "sugar":500,
    "lemon flaviour":500,
    "tea":500

}
#this function is used for checking the suffficient meterials is avalavle or not for a particular items
def check_meterials(check_items):
    for product in check_items:
        if check_items[product]>items[product]:
            print(f"insufficient items{product} : for now this  is not possible to do ")
            return False
    return True

#After checking the meterials are avalavle or not we have to ask for inserting a coin.The mechine will take 5 10 and 20 rupees coin

def coin_process():
    print("Please insert a coin: ")
    five_coin=int(input("Number of 5 rupees coin/coins you have: "))
    ten_coin=int(input("Number of 10 rupees coin/coins you have: "))
    twenty_coin=int(input("Number of 20 rupees coin/coins you have: "))
    total=five_coin*5+ten_coin*10+twenty_coin*20
    return total

#checking payment is successful or not and if it pay extra then it will give change

def is_payment_successful(money_received,coffee_cost):
    if money_received>=coffee_cost:
        global profit               #as profit is a global varriable
        profit+=coffee_cost
        change=money_received-coffee_cost
        print(f"Here is your change :  {change}")
        return True
    else:
        print(f"not enough money . money refunded{money_received} visit again")
        return False

#this function will give tea

def make_drink(drink_name,drink_meterials):
    for item in drink_meterials:
        items[item]-=drink_meterials[item]
    print(f"here is your drink: {drink_name}")






couponRetryCounter = 3 # camel casing
# CouponRetryCounter -> pascal casing
# coupon_retry_counter

while True:

    coupon=input("do you have the spical cupon code for free coffee: YES/NO")
    if couponRetryCounter > 0 and coupon.lower() == "yes":
            y = input("enter the passsword:")
            if y == "1234":
                couponRetryCounter = 3  # reset counter
                x = input("what you want")
                if x == "tea":
                    print("here is your tea")
            else:
                couponRetryCounter -= 1
                print("Invalid coupon code!!!")



    else:
        if couponRetryCounter == 0:
            print("You have exhausted all your retries! Please retry again later.")
            couponRetryCounter = 3 # reset counter
        choisee=input("What you need (TEA / FILTER COFFEE / LEMON TEA): ")
        choise=choisee.lower().strip()
        if choise.lower().strip()=="off":
            break
        elif  choise.lower().strip() == "report":#fetching the data from the dicsnary through a f string "first the dicsnary name and then the key value"
            print(f"water={items["water"]}ml")
            print(f"milk={items["milk"]}ml")
            print(f"coffee={items["coffee"]}g")
            print(f"sugar={items["sugar"]}gn")
            print(f"lemon flaviour={items["lemon flaviour"]}")
            print(f"tea={items["tea"]}")
            print(f"money Rs={profit}")

        else:
            drink=menu[choise] #the drink varriable gives the drink which the user chhose and its meterials
            print(drink)
            if check_meterials(drink["meterials"]):
                payment=coin_process()
                if is_payment_successful(payment,drink["cost"]):
                    make_drink(choise,drink["meterials"])


