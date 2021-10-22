#! python3
# Final project in "CS 101: Introduction to Programming" class: Mortgage calculator

# calculating monthly_payment: monthly_payment = ((6.5 / 100 / 12) * 200000) / (1 - ((1 + (6.5 / 100 / 12)) ^ (-30 * 12)))
def monthly_amount(principal, interest_rate, term):
    term *= 12 #number of monthly payments
    interest_rate = interest_rate / 100 / 12 #yearly percentage rate divided by 12
    payment = ((interest_rate * principal) / ((1 - ((1 + (interest_rate)) ** (-term)))))
    return f'Monthly amount payment: ${payment:6.2f}'

def term(principal, interest_rate, payment):
    interest_rate = interest_rate / 100 / 12  # yearly percentage rate divided by 12
    term = 0
    while principal > 0:
        principal = principal + (interest_rate * principal) - payment
        term += 1
    return f'{term} months'





# testing monthly_amount()
print(monthly_amount(200000, 6.5, 30)) #output: Monthly amount payment: $1264.14

#testing term()
print(term(200000, 6.5, 1264.14)) # output: 360 months









