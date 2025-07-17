           #"""Currency Convertor"""

# Predefined Exchange Rates:
exchange_rates = {
    "USD": 277.50,  # 1 USD = 277.50 PKR
    "EUR": 301.25,  # 1 EUR = 302.25 PKR
    "SAR": 74.00    # 1 SAR = 74.00 PKR
}

def convert_to_pk(a, c):           #Currency Converter Function
#"""Converts given amount from selected currency to PKR"""
    rate = exchange_rates.get(c.upper())
    if rate:
        return a * rate
    else:
        return 0    #Invalid Currency

#Infinite loop to do multiple task:
while True:
    print("Welcome to Currency Converter!")
    print("Supported Currencies: USD, EUR, SAR")

    #input currency 
    currency = input("Enter currency : ").upper()
    #if-else statement
    if currency in exchange_rates:
        amount = float(input(f"Enter your amount {currency} that you want to convert: "))
        converted = convert_to_pk(amount, currency)
        #Display converted currency
        print(f"{amount}{currency} = {converted:.2f}PKR")
    else:
        print("Unsupported Currency.")

    again = input("Do you want to convert another amount?(yes/no): ").lower()
    if again != 'yes':
        print("Thank you for using the currency converter! ")
        break




   
    
        