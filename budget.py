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
        print "                                13  - Print Month's Budget"
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

    def save_to_file(self):
        path = raw_input("Please enter the full path to the data file:  ")
        with open(path, 'w+') as f:
            f.write('[balance]\n')
            f.write(str(self.balance) + '\n')
            f.write('[expenses]\n')
            for i in self.expenses:
                f.write("{}|{}\n".format(self.expenses[i]['day'], self.expenses[i]['amount']))
            f.write('[incomes]\n')
            for j in self.income:
                f.write("{}|{}\n".format(self.income[j]['day'], self.income[j]['amount']))

    def load_from_file(self):
        path = raw_input("Please enter the full path to the data file:  ")
        adding_balance = False
        adding_expenses = False
        adding_incomes = False
        ex_cnt = 0
        in_cnt = 0
        balance = 0
        with open(path) as f:
            for line in f:
                if '[balance]' in line:
                    adding_balance = True
                elif '[expenses]' in line:
                    adding_balance = False
                    adding_expenses = True
                elif '[incomes]' in line:
                    adding_expenses = False
                    adding_incomes = True
                elif adding_balance:
                    self.balance = Decimal(line)
                elif adding_expenses:
                    toks = line.split('|')
                    self.expenses[ex_cnt] = {'day': int(toks[0]), 'amount': Decimal(toks[1])}
                    ex_cnt += 1
                elif adding_incomes:
                    toks = line.split('|')
                    self.income[in_cnt] = {'day': int(toks[0]), 'amount': Decimal(toks[1])}
                    in_cnt += 1

        # update counters
        self.income_counter = len(self.income)
        self.expenses_counter = len(self.expenses)

    def check_for_income_by_day(self, day):
        all_income = Decimal(0.00)
        for i in self.income:
            if day == self.income[i]['day']:
                all_income += self.income[i]['amount']

        return all_income

    def check_for_expenses_by_day(self, day):
        all_expenses = Decimal(0.00)
        for i in self.expenses:
            if day == self.expenses[i]['day']:
                all_expenses += self.expenses[i]['amount']

        return all_expenses

    def print_daily_budget(self):
        running_balance = self.balance
        # Calendar(6) to start week with Sunday
        print " day           balance      income  expenses"
        for d in calendar.Calendar(6).itermonthdays(self.year, self.month):
            if d == 0:
                continue
            inc = self.check_for_income_by_day(d)
            exp = self.check_for_expenses_by_day(d)
            running_balance = running_balance + inc
            running_balance = running_balance - exp
            print "{}/{:<4}        {:>6}{:>8}{:>8} ".format(self.month, d, running_balance, inc, exp)


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
            funcs.save_to_file()
        elif choice == 9:
            funcs.load_from_file()
        elif choice == 10:
            funcs.print_functions()
        elif choice == 11:
            funcs.print_calendar()
        elif choice == 12:
            end_program = True
        elif choice == 13:
            funcs.print_daily_budget()
        else:
            print "No."

    print "Goodbye!"

main()
