from datetime import datetime
import json
import os
import csv

class NOTE:
    def __init__(self, title, content):
        self.note_id = None
        self.title = title
        self.content = content
        self.timestamp = None


class FUNC_NOTE:
    def __init__(self):
        pass


    def create(self, Note:NOTE):
        path = '/'.join(os.getcwd().split('/'))
        with open(os.path.join(path, 'data/notes.json'), 'r') as file:
            data = json.load(file)
            Note.note_id = data[0]['count'] + 1
            data[0]['count'] = data[0]['count'] + 1
            Note.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            data.append({
                'id': Note.note_id,
                'title': Note.title,
                'content': Note.content,
                'timestamp': Note.timestamp
            })
        with open(os.path.join(path, 'data/notes.json'), 'w') as file:
            json.dump(data, file, indent=4)

    def show_by_id(self, id):
        path = '/'.join(os.getcwd().split('/'))
        with open(os.path.join(path, 'data/notes.json'), 'r') as file:
            data = json.load(file)
            for note in data[1:]:
                if note['id'] == id:
                    return note
            return None


    def show(self):
        path = '/'.join(os.getcwd().split('/'))
        with open(os.path.join(path, 'data/notes.json'), 'r') as file:
            data = json.load(file)
            return data[1:]

    def update(self, id, Note):
        path = '/'.join(os.getcwd().split('/'))
        with open(os.path.join(path, 'data/notes.json'), 'r') as file:
            data = json.load(file)
            for note in data[1:]:
                if note['id'] == id:
                    note['title'] = Note.title
                    note['content'] = Note.content
                    note['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    break
        with open(os.path.join(path, 'data/notes.json'), 'w') as file:
            json.dump(data, file, indent=4)


    def delete(self, id):
        path = '/'.join(os.getcwd().split('/'))
        with open(os.path.join(path, 'data/notes.json'), 'r') as file:
            data = json.load(file)
            for note in data[1:]:
                if note['id'] == id:
                    data.remove(note)
                    break
        with open(os.path.join(path, 'data/notes.json'), 'w') as file:
            json.dump(data, file, indent=4)

    def import_export(self,  mode, path_csv_file=None):
        try:
            if mode == 'import':
                with open(path_csv_file, 'r') as file_new:
                    file_new = csv.DictReader(file_new)
                    path = '/'.join(os.getcwd().split('/'))
                    with open(os.path.join(path, 'data/notes.json'), 'r') as file:
                        data = json.load(file)
                        for row in file_new:
                            note = NOTE(row['title'], row['content'])
                            note.note_id = data[0]['count'] + 1
                            data[0]['count'] = data[0]['count'] + 1
                            note.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            data.append({
                                'id': note.note_id,
                                'title': note.title,
                                'content': note.content,
                                'timestamp': note.timestamp
                            })
                with open(os.path.join(path, 'data/notes.json'), 'w') as file:
                    json.dump(data, file, indent=4)
            elif mode == 'export':
                path = '/'.join(os.getcwd().split('/'))
                with open(os.path.join(path, 'data/notes.json'), 'r') as file:
                    data = json.load(file)
                with open(os.path.join(path, 'data/export_notes.json'), 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames= ['id', 'title', 'content', 'timestamp'])
                    writer.writeheader()
                    for task in data[1:]:
                        writer.writerow(task)
        except Exception as e:
            print(e)

