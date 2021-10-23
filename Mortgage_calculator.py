#! python3
# Final project in "CS 101: Introduction to Programming" class: Mortgage calculator

# calculating monthly_payment: monthly_payment = ((6.5 / 100 / 12) * 200000) / (1 - ((1 + (6.5 / 100 / 12)) ^ (-30 * 12)))
class Mortgage:
    def __init__(self):
        self.principal = float(input("Type loan's principal: "))
        self.interest_rate = float(input("Type yearly interest rate: "))
        self.interest_rate = self.interest_rate / 100 / 12  # yearly percentage rate divided by 12

    def monthly_amount(self):
        self.yearly_term = int(input("Type yearly term: "))
        self.yearly_term *= 12 #number of monthly payments
        payment = ((self.interest_rate * self.principal) / ((1 - ((1 + (self.interest_rate)) ** (-self.yearly_term)))))
        return f'Monthly amount payment: ${payment:6.2f}'

    def term(self):
        self.payment = float(input("Type the monthly amount: "))
        term = 0
        while self.principal > 0:
            self.principal = self.principal + (self.interest_rate * self.principal) - self.payment
            term += 1
        return f'This amount would take {term} months to be paid.'

#print(mortgage.term)
# testing monthly_amount()
#print(mortgage.monthly_amount()) #output: Monthly amount payment: $1264.14

#testing term()
#print(mortgage.term()) # output: 360 months

mes = 'Welcome to the Mortgage Calculator!'
print('=' * len(mes))
print(mes)
print('=' * len(mes))
try:
    mortgage = Mortgage()
    print("Choose 'monthly amount' or 'loan's term'.")
    choice = input('Your choice: ')
    if choice == 'monthly amount':
        print(mortgage.monthly_amount())
    elif choice == "loan's term" or choice == "term":
        print(mortgage.term())
    else:
        print('Option is not available.')
except:
    print('Option is not available.')












