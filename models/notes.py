from datetime import datetime
import json
import os

class Note:
    def __init__(self, title, content):
        self.note_id = None
        self.title = title
        self.content = content
        self.timestamp = None

class Func_Note:



    def create(self, Note:Note):
        path = '/'.join(os.getcwd().split('/')[:-1])
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


        # note = Note(self.note.id, title, content, timestamp)
        # return note

print(Func_Note().create(Note(1, 1)))
