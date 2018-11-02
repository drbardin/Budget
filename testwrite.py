from decimal import Decimal
x = {}
x[0] = {'day': 02, 'amount': 1234}
x[1] = {'day': 02, 'amount': 4321}
w = {}
w[0] = {'day': 02, 'amount': 2121}
balance = 2345.54

with open('saved_data.txt', 'w+') as f:
    f.write('[balance]\n')
    f.write(str(balance) + '\n')
    f.write('[expenses]\n')
    for i in x:
        f.write("{}|{}\n".format(x[i]['day'], x[i]['amount']))
    f.write('[incomes]\n')
    for j in w:
        f.write("{}|{}\n".format(w[j]['day'], w[j]['amount']))


adding_balance = False
adding_expenses = False
adding_incomes = False
ex_cnt = 0
in_cnt = 0
balance = 0
with open('saved_data.txt') as f:
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
            balance = Decimal(line)
        elif adding_expenses:
            toks = line.split('|')
            y[ex_cnt] = {'day': int(toks[0]), 'amount': Decimal(toks[1])}
            ex_cnt += 1
        elif adding_incomes:
            toks = line.split('|')
            z[in_cnt] = {'day': int(toks[0]), 'amount': Decimal(toks[1])}
            in_cnt += 1

print balance
print y
print z