#
# class FINANCE:
#     def __init__(self, amount, category, description):
#         self.id = None
#         self.amount = amount
#         self.category = category
#         self.date = None
#         self.description = description
#
#
# class FINANCE_FUNC:
#     def __init__(self):
#         pass
#
#     def add(self, finance:Finance):
#         path = '/'.join(os.getcwd().split('/')[:-1])
#         with open(os.path.join(path, 'data/finance.json'), 'r') as file:
#             data = json.load(file)
#             finance.id = data[0]['count'] + 1
#             data[0]['count'] = data[0]['count'] + 1
#             finance.date = datetime.now().strftime('%d-%m-%Y')
#             data.append({
#                 'id': finance.id,
#                 'amount': finance.amount,
#                 'category': finance.category,
#                 'date': finance.date,
#                 'description': finance.description
#             })
#         with open(os.path.join(path, 'data/finance.json'), 'w') as file:
#             json.dump(data, file, indent=4)
#
#     def show_all_tasks(self, filter_type=None, data='01-01-2020', cat=None):
#         path = '/'.join(os.getcwd().split('/')[:-1])
#         with open(os.path.join(path, 'data/finance.json'), 'r') as file:
#             data = json.load(file)[1:]
#             mas = []
#             if filter_type == 'category':
#                 for task in data:
#                     if task['category'] == cat:
#                         mas.append(task)
#                 return mas
#             elif filter_type == 'date':
#                 for task in data:
#                     if task['date'] == data:
#                         mas.append(task)
#                 return mas
#             else:
#                 return data
#
#     def generate_period(self, start, end):
#         path = '/'.join(os.getcwd().split('/')[:-1])
#         with open(os.path.join(path, 'data/finance.json'), 'r') as file:
#             data = json.load(file)[1:]
#             mas = []
#             for task in data:
#                 if start <= task['date'] <= end:
#                     mas.append(task)
#             return mas
#
#     def show_by_id(self, id):
#         path = '/'.join(os.getcwd().split('/')[:-1])
#         with open(os.path.join(path, 'data/finance.json'), 'r') as file:
#             data = json.load(file)
#             for finance in data:
#                 if finance['id'] == id:
#                     return finance
#             return None
#
#     def update(self, id, finance:Finance):
#         path = '/'.join(os.getcwd().split('/')[:-1])
#         with open(os.path.join(path, 'data/finance.json'), 'r') as file:
#             data = json.load(file)
#             for finance in data:
#                 if finance['id'] == id:
#                     finance['amount'] = finance.amount
#                     finance['category'] = finance.category
#                     finance['date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#                     finance['description'] = finance.description
#                     break
#         with open(os.path.join(path, 'data/finance.json'), 'w') as file:
#             json.dump(data, file, indent=4)
#
#     def delete(self, id):
#         path = '/'.join(os.getcwd().split('/')[:-1])
#         with open(os.path.join(path, 'data/finance.json'), 'r')