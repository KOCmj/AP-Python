class Income():
    total_investment = 50000

    def __init__(self, income = [], expenses = [], cash_flow = [], COC_roi = {}):
        self.COC_roi = COC_roi
        self.cash_flow = cash_flow
        self.expenses = expenses
        self.income = income

    def cal_expenses(self):
        total_income = int(input(f'What is your total income?: '))
        self.income.append(total_income)
        print(f'Tenant rental income is ${total_income}')
        expense = int(input(f'What is monthly expenses?: '))
        print(f'Tenant monthly expenses is: ${expense}')
        self.expenses.append(expense)
        

    def cal_total(self):
        total_income = sum(self.income)
        total_expenses = sum(self.expenses)
        cash_flow = total_income - total_expenses
        annual_cash =  cash_flow * 12
        print(f'Annual cash flow is: ${annual_cash}')
        print(f'Total investment made on this property is: ${self.total_investment}')
        roi = annual_cash / self.total_investment * 100
        self.COC_roi = {'ROI': f"{roi}%"}
        print(self.COC_roi)

my_investment = Income()

def TotalI():
    while True:
        i = input('Lets play a game; Enter (add/cal/quit): ')
        if i.lower() == 'add':
            my_investment.cal_expenses()
        elif i.lower() == 'cal':
            my_investment.cal_total()
        elif i.lower() == 'quit':
            print('GGs')
            break
        else: 
            print('Try again')

TotalI()




