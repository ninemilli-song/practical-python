# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month = month + 1
    if principal * (1 + rate / 12) > payment:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment
    else:
        principal = 0
        total_paid = total_paid + principal

    if month >= extra_payment_start_month and month <= extra_payment_end_month and principal >= extra_payment:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    print(f'{month} {round(total_paid, 4)} {round(principal, 4)}')

print(f'Total paid {round(total_paid, 4)}')
print(f'Months {month}')
