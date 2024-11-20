import os
import json
from datetime import datetime
import csv
from asyncio import TaskGroup


class TASK:
    def __init__(self, title, description, done, priority, due_date):
        self.task_id = None
        self.title = title
        self.description = description
        self.done = done
        self.priority = priority
        self.due_date = due_date


class TASK_FUNC:
    def __init__(self):
        pass

    def add_new_task(self, task:TASK):
        path = '/'.join(os.getcwd().split('/')[:-1])
        with open(os.path.join(path, 'data/tasks.json'), 'r') as file:
            data = json.load(file)
            task.task_id = data[0]['count'] + 1
            data[0]['count'] = data[0]['count'] + 1
            data.append({
                'id': task.task_id,
                'title': task.title,
                'description': task.description,
                'done': task.done,
                'priority': task.priority,
                'due_date': task.due_date
            })

        with open(os.path.join(path, 'data/tasks.json'), 'w') as file:
            json.dump(data, file, indent=4)


    def show_all_tasks(self, filter_type=None, done=True):
        path = '/'.join(os.getcwd().split('/')[:-1])
        with open(os.path.join(path, 'data/tasks.json'), 'r') as file:
            data = json.load(file)[1:]
            mas = []
            if filter_type == 'priority':
                for typ in ['Высокий', 'Средний', 'Низкий']:
                    for task in data:
                        if task['priority'] == typ:
                            mas.append(task)
                return mas
            elif filter_type == 'done':
                for task in data:
                    if task['done'] == done:
                        mas.append(task)
                return mas
            elif filter_type == 'due_date':
                mas_times = [(datetime.strptime(task['due_date'], '%d-%m-%Y'), i) for i, task in enumerate(data)]
                mas_times.sort(key=lambda x: x[0])
                return [data[i[1]] for i in mas_times]
            return data


    def complete(self, id):
        path = '/'.join(os.getcwd().split('/')[:-1])
        with open(os.path.join(path, 'data/tasks.json'), 'r') as file:
            data = json.load(file)
            for task in data:
                if task['id'] == id:
                    task['done'] = True
                    break
        with open(os.path.join(path, 'data/tasks.json'), 'w') as file:
            json.dump(data, file, indent=4)


    def update(self, id, task_new:TASK):
        path = '/'.join(os.getcwd().split('/')[:-1])
        with open(os.path.join(path, 'data/tasks.json'), 'r') as file:
            data = json.load(file)
            for task in data[1:]:
                if task['id'] == id:
                    task['title'] = task_new.title
                    task['description'] = task_new.description
                    task['done'] = task_new.done
                    task['priority'] = task_new.priority
                    task['due_date'] = task_new.due_date
                    break
        with open(os.path.join(path, 'data/tasks.json'), 'w') as file:
            json.dump(data, file, indent=4)


    def delete(self, id):
        path = '/'.join(os.getcwd().split('/')[:-1])
        with open(os.path.join(path, 'data/tasks.json'), 'r') as file:
            data = json.load(file)
            for task in data:
                if task['id'] == id:
                    data.remove(task)
                    break
        with open(os.path.join(path, 'data/tasks.json'), 'w') as file:
            json.dump(data, file, indent=4)

    def import_export(self, path_csv_file, mode):
        if mode == 'import':
            with open(path_csv_file, 'r') as file_new:
                file_new = csv.DictReader(file_new)
                path = '/'.join(os.getcwd().split('/')[:-1])
                with open(os.path.join(path, 'data/contacts.json'), 'r') as file:
                    data = json.load(file)
                    for row in file_new:
                        task = TASK(row['title'], row['description'], row['done'], row['priority'], row['due_date'])
                        task.task_id = data[0]['count'] + 1
                        data[0]['count'] = data[0]['count'] + 1
                        data.append({
                            'id': task.task_id,
                            'title': task.title,
                            'description': task.description,
                            'done': task.done,
                            'priority': task.priority,
                            'due_date': task.due_date
                        })
            with open(os.path.join(path, 'data/tasks.json'), 'w') as file:
                json.dump(data, file, indent=4)
        elif mode == 'export':
            path = '/'.join(os.getcwd().split('/')[:-1])
            with open(os.path.join(path, 'data/tasks.json'), 'r') as file:
                data = json.load(file)
            with open(os.path.join(path, 'data/export_tasks.json'), 'w') as file:
                file.write('')
                writer = csv.DictWriter(file, fieldnames=['id', 'title', 'description', 'done', 'priority', 'due_date'])
                writer.writeheader()
                for task in data:
                    writer.writerow(task)


# TASK_FUNC().add_new_task(TASK('title', 'description', False, 'Высокий', '8-10-2020'))
# print(TASK_FUNC().show_all_tasks('due_date'))
# TASK_FUNC().update(6, TASK('tisdfsdftle', 'dessdfsdfcription', False, 'Высокий', '8-10-2020'))