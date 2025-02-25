import csv
import os

# Set the correct file path
file_path = "C:\Users\domel\OneDrive\Documents\FEU\2nd Year\2nd Sem\IT0011, INTEGRATIVE PROGRAMMING AND TECHNOLOGIES\LAB 4B\2\currency.csv"  # Update this if needed

# Check if file exists before opening
if not os.path.exists(file_path):
    print("Error: currency.csv not found. Make sure the file is in the correct location.")
else:
    # Load exchange rates
    exchange_rates = {}
    with open(file_path, mode="r", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            currency, rate = row
            exchange_rates[currency] = float(rate)

    # Get user input
    usd_amount = float(input("How much dollar do you have? "))
    target_currency = input("What currency you want to have? ").upper()

    # Convert and display result
    if target_currency in exchange_rates:
        converted_amount = usd_amount * exchange_rates[target_currency]
        print(f"\nDollar: {usd_amount} USD")
        print(f"{target_currency}: {converted_amount}")
    else:
        print("Currency not found in the exchange rate data.")
