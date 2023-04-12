exchange_rate = 5.61

brl = float(input("Enter the amount in Brazilian Reais: "))

usd = brl / exchange_rate

print(f"{brl:.2f} BRL is equivalent to {usd:.2f} USD at an exchange rate of {exchange_rate:.2f}.")
