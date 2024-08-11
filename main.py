import Modules.CurClass as Currencies
import os
import time

#main currency.
global dollar 
dollar = Currencies.Currency(1, 25, "USD")

# [all currencies available]
pln = Currencies.Currency(3.96, 0, "PLN")
eur = Currencies.Currency(0.92, 0, "EUR")
#put every currency here.
curall = [dollar, pln, eur]

#region HOW TO ADD CUSTOM CURRENCY?
# under the [all currencies availble] comment, there are currencies additional currencies. you can add your own under both.
# example = Currencies.Currency(A, B, C)
# A - How much of this currency is worth a dollar?
# B - The starting amount of the currency.
# C - The Name.
# after finishing, add the currency to the curall list.
#endregion 

def DollarsToCurrency(amount, curtype):
    dollar.curamount -= amount
    curtype.curamount += curtype.ConvertFromDollar(amount)

def CurrencyToDollar(amount, curtype):
    dollar.curamount += curtype.ConvertToDollar(amount)
    curtype.curamount -= amount

def CurrencyToCurrency(amount, from_currency, to_currency):
    from_currency.curamount -= amount
    to_currency.curamount += to_currency.ConvertFromDollar(from_currency.ConvertToDollar(amount))


# big ass function, handles everything. 
def Menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("------CURRENCIES------")
    for i in range(0, len(curall)):
        print("({}){}: {}".format(i,curall[i].name, curall[i].curamount))
    print("----------------------")
    print("1. Convert Dollars to Currency")
    print("2. Convert Currency to Dollars")
    print("3. Convert Currency to Currency")
    print("4. Deposit USD")
    print("5. Withdraw USD")
    print("6. Close")
    choice = input("Choose your option: ")
    # checking choice
    while choice not in ['1', '2', '3', '4','5','6']:
        choice = input("Invalid option. Choose your option: ")
    if choice == '1':
        amount = float(input("Enter the amount you want to convert: "))
        cur_index = int(input("Enter the currency index you want to convert to: "))
        while cur_index not in range(0, len(curall)):
            cur_index = int(input("Invalid currency index. Enter the currency index you want to convert to: "))
        DollarsToCurrency(amount, curall[cur_index])
        Menu()
    elif choice == '2':
        amount = float(input("Enter the amount you want to convert: "))
        cur_index = int(input("Enter the currency index you want to convert from: "))
        while cur_index not in range(0, len(curall)):
            cur_index = int(input("Invalid currency index. Enter the currency index you want to convert from: "))
        CurrencyToDollar(amount, curall[cur_index])
        Menu()
    elif choice == '3': 
        amount = float(input("Enter the amount you want to convert: "))
        cur_index1 = int(input("Enter the currency index you want to convert from: "))
        while cur_index1 not in range(0, len(curall)):
            cur_index1 = int(input("Invalid currency index. Enter the currency index you want to convert from: "))
        cur_index2 = int(input("Enter the currency index you want to convert to: "))
        while cur_index2 not in range(0, len(curall)):
            cur_index2 = int(input("Invalid currency index. Enter the currency index you want to convert to: "))
        CurrencyToCurrency(amount,curall[cur_index1], curall[cur_index2])
        Menu()
    elif choice == '4':
        amount = float(input("Enter the amount of USD you want to deposit: "))
        dollar.curamount += amount
        print("Deposit successful! Your new balance is: ", dollar.curamount)
        time.sleep(2)
        Menu()
    elif choice == '5':
        amount = float(input("Enter the amount of USD you want to withdraw: "))
        dollar.curamount += amount
        print("Withdraw successful! Your new balance is: ", dollar.curamount)
        time.sleep(2)
        Menu()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Thank you for using my currency converter!")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        exit()

def Intro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("    --Fake ATM--    ")
    time.sleep(1)
    print("a basic program made by Coden.")
    time.sleep(1)
    print("with a tiny bit of mod support!")
    time.sleep(1)
    print("And an option to put yourself in debt!")
    print("    ------------    ")
    time.sleep(3)
    Menu()

Intro()