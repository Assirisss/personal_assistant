
class FINANCE:
    def __init__(self, amount, category, description):
        self.id = None
        self.amount = amount
        self.category = category
        self.date = None
        self.description = description


class FINANCE_FUNC:
    def __init__(self):
        pass

    def add(self, finance:Finance):
        path = '/'.join(os.getcwd().split('/')[:-1])
        with open(os.path.join(path, 'data/finance.json'), 'r') as file:
            data = json.load(file)
            finance.id = data[0]['count'] + 1
            data[0]['count'] = data[0]['count'] + 1
            finance.date = datetime.now().strftime('%d-%m-%Y')
            data.append({
                'id': finance.id,
                'amount': finance.amount,
                'category': finance.category,
                'date': finance.date,
                'description': finance.description
            })
        with open(os.path.join(path, 'data/finance.json'), 'w') as file:
            json.dump(data, file, indent=4)

    def show_all_fin_not(self, filter_type=None, date='01-01-2020', cat=None):
        path = '/'.join(os.getcwd().split('/')[:-1])
        with open(os.path.join(path, 'data/finance.json'), 'r') as file:
            data = json.load(file)[1:]
            mas = []
            if filter_type == 'category':
                for task in data:
                    if task['category'] == cat:
                        mas.append(task)
                return mas
            elif filter_type == 'date':
                for task in data:
                    if task['date'] == date:
                        mas.append(task)
                return mas
            else:
                return data

    def generate_period(self, start, end):
        path = '/'.join(os.getcwd().split('/')[:-1])
        with open(os.path.join(path, 'data/finance.json'), 'r') as file:
            data = json.load(file)[1:]
            mas = []
            for task in data:
                if datetime.strptime(start, '%d-%m-%Y') <= datetime.strptime(task['date'], '%d-%m-%Y') <= datetime.strptime(end, '%d-%m-%Y'):
                    mas.append(task)
            return mas

    def import_export(self, path_csv_file, mode):
        if mode == 'import':
            with open(path_csv_file, 'r') as file_new:
                file_new = csv.DictReader(file_new)
                path = '/'.join(os.getcwd().split('/')[:-1])
                with open(os.path.join(path, 'data/finance.json'), 'r') as file:
                    data = json.load(file)
                    for row in file_new:
                        finance = FINANCE(row['amount'], row['category'], row['description'])
                        finance.id = data[0]['count'] + 1
                        data[0]['count'] = data[0]['count'] + 1
                        finance.date = datetime.now().strftime('%d-%m-%Y')
                        data.append({
                            'id': finance.id,
                            'amount': finance.amount,
                            'category': finance.category,
                            'date': finance.date,
                            'description': finance.description
                        })
            with open(os.path.join(path, 'data/finance.json'), 'w') as file:
                json.dump(data, file, indent=4)
        elif mode == 'export':
            path = '/'.join(os.getcwd().split('/')[:-1])
            with open(os.path.join(path, 'data/finance.json'), 'r') as file:
                data = json.load(file)
            with open(os.path.join(path, 'data/export_finance.json'), 'w') as file:
                file.write('')
                writer = csv.DictWriter(file, fieldnames= ['id', 'amount', 'category', 'date', 'description'])
                writer.writeheader()
                for task in data:
                    writer.writerow(task)
        else:
            return "Invalid mode"

    def all_balance(self):
        path = '/'.join(os.getcwd().split('/')[:-1])
        with open(os.path.join(path, 'data/finance.json'), 'r') as file:
            data = json.load(file)[1:]
            mas = []
            for task in data:
                mas.append(task['amount'])
            return sum(mas)


    def return_income_expense_by_ctg(self, category):
        path = '/'.join(os.getcwd().split('/')[:-1])
        with open(os.path.join(path, 'data/finance.json'), 'r') as file:
            data = json.load(file)[1:]
            mas = []
            for cat in [i['category'] for i in data]:
                income = []
                expenses = []
                for task in data:
                    if task['category'] == category:
                        if task['amount'] > 0:
                            income.append(task['amount'])
                        else:
                            expenses.append(task['amount'])
                mas.append(['cat', income, expenses])
        return mas




