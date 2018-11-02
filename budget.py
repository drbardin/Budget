import calendar
import datetime
from decimal import Decimal


class BudgetFunctions:
    def __init__(self):
        self.balance = 0.00
        self.expenses = {}
        self.income = {}
        self.month = 0
        self.year = 0
        self.income_counter = 0
        self.expenses_counter = 0

    def print_functions(self):
        print
        print "Choose a function:"
        print
        print "  1  - Set Checking Balance      7  - Get Balance for Date"
        print "  2  - Get Checking Balance      8  - Save Data to File"
        print "  3  - Add Income                9  - Load Data From File"
        print "  4  - Print Income             10  - Print Available Functions"
        print "  5  - Add Expense              11  - Print This Month's Calendar"
        print "  6  - Print Expenses           12  - Exit"
        print

    def set_balance(self):
        amount = raw_input("Enter starting balance for the month: ")
        self.balance = Decimal(amount)

    def set_dates(self, year, month):
        if not year and not month:
            now = datetime.datetime.now()
            self.year = now.year
            self.month = now.month
        else:
            self.year = int(year)
            self.month = int(month)

    def print_calendar(self):
        print
        print(calendar.month(self.year, self.month))

    def add_income(self):
        day = raw_input("What day does this income arrive (dd)?: ")
        amount = Decimal(raw_input("Amount to add: "))
        self.income[self.income_counter] = {'day': day, 'amount': amount}
        self.income_counter += 1

    def print_income(self):
        if len(self.income) == 0:
            print "\nNo income entered.\n"
        print "  Day    Amount   "
        for k, v in self.income.iteritems():
            print "   {}     ${}".format(v['day'], v['amount'])

    def add_expense(self):
        # resp = raw_input("Enter single expense or multiple? (s or m): ")
        # if resp == 's':
        day = raw_input("What day for this expense (dd)?: ")
        amount = Decimal(raw_input("Expense amount: "))
        self.expenses[self.expenses_counter] = {'day': day, 'amount': amount}
        self.expenses_counter += 1
        # else:
        #     print "Enter multiple expenses as: [day, amount"

    def print_expenses(self):
        print "  Day    Amount   "
        for k, v in self.expenses.iteritems():
            print "   {}     ${}".format(v['day'], v['amount'])


def main():
    funcs = BudgetFunctions()

    end_program = False
    first_pass = True

    while not end_program:
        if first_pass:
            date = raw_input("Enter the month and year to budget for (yyyy-mm) or leave empty to use current month: ")
            if date == '':
                year = None
                month = None
            else:
                tokens = date.split('-')
                year = tokens[0]
                month = tokens[1]
            funcs.set_dates(year, month)
            funcs.print_functions()
            first_pass = False

        choice = int(raw_input("Enter a function, I'll wait here... : "))
        if choice == 1:
            funcs.set_balance()
        elif choice == 2:
            print "$" + str(funcs.balance)
        elif choice == 3:
            funcs.add_income()
        elif choice == 4:
            funcs.print_income()
        elif choice == 5:
            funcs.add_expense()
        elif choice == 6:
            funcs.print_expenses()
        elif choice == 7:
            print "Not implemented yet."
        elif choice == 8:
            print "Not implemented yet."
        elif choice == 9:
            print "Not implemented yet."
        elif choice == 10:
            funcs.print_functions()
        elif choice == 11:
            funcs.print_calendar()
        elif choice == 12:
            end_program = True
        else:
            print "No."

    print "Goodbye!"

main()
