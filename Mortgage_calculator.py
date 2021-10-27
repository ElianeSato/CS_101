#! python3
# Final project in "CS 101: Introduction to Programming" class: Mortgage calculator

import os
import pyinputplus as pyip

# calculating monthly_payment: monthly_payment = ((6.5 / 100 / 12) * 200000) / (1 - ((1 + (6.5 / 100 / 12)) ^ (-30 * 12)))
class Mortgage:
    def __init__(self):
        self.principal = pyip.inputFloat("Type loan's principal: ")
        self.interest_rate = pyip.inputFloat("Type yearly interest rate: ")
        self.interest_rate = self.interest_rate / 100 / 12  # yearly percentage rate divided by 12

    def monthly_amount(self):
        self.yearly_term = pyip.inputInt("Type yearly term: ")
        self.yearly_term *= 12 #number of monthly payments
        payment = ((self.interest_rate * self.principal) / ((1 - ((1 + (self.interest_rate)) ** (-self.yearly_term)))))
        return f'Monthly amount payment for ${self.principal:6.2f} in {self.yearly_term} months: ${payment:6.2f}'

    def term(self):
        self.payment = pyip.inputFloat("Type the monthly amount: $")
        term = 0
        balance = self.principal
        while balance > 0:
            balance = balance + (self.interest_rate * balance) - self.payment
            term += 1
        return f"The loan's principal ${self.principal} would take {term} months to be paid."

#print(mortgage.term)
# testing monthly_amount()
#print(mortgage.monthly_amount()) #output: Monthly amount payment: $1264.14

#testing term()
#print(mortgage.term()) # output: 360 months

clean_screen = os.system('clear')

mes = 'Welcome to the Mortgage Calculator!'
print('=' * (len(mes) + 10))
print(mes.center(len(mes) + 10))
print('=' * (len(mes) + 10))

mortgage = Mortgage()
print("Choose '1' for monthly amount, '2' for loan's term(years), or '3' to exit.")
choice = pyip.inputMenu(choices=['monthly amount', "loan's term", "quit"], numbered=True)
print('Your choice:', choice)
if choice == 'monthly amount':
    print('=' * (len(mes) + 10))
    print(mortgage.monthly_amount())
    print('=' * (len(mes) + 10))
elif choice == "loan's term":
    print('=' * (len(mes) + 10))
    print(mortgage.term())
    print('=' * (len(mes) + 10))
else:
    print('=' * (len(mes) + 10))
    print('Thanks for your visit!'.center(len(mes) + 10))
    print('=' * (len(mes) + 10))
    quit()














