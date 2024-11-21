from tkinter.font import names
from datetime import datetime
import json
import os
import csv

class CONTACT:
    def __init__(self, name, phone, email):
        self.contact_id = None
        self.name = name
        self.phone = phone
        self.email = email


class CONTACT_FUNC:
    def __init__(self):
        pass

    def add_new_contact(self, contact:CONTACT):
        path = '/'.join(os.getcwd().split('/'))
        with open(os.path.join(path, 'data/contacts.json'), 'r') as file:
            data = json.load(file)
            contact.contact_id = data[0]['count'] + 1
            data[0]['count'] = data[0]['count'] + 1
            data.append({
                'id': contact.contact_id,
                'name': contact.name,
                'phone': contact.phone,
                'email': contact.email
            })

        with open(os.path.join(path, 'data/contacts.json'), 'w') as file:
            json.dump(data, file, indent=4)

    def find_contact(self, type = None, value = None):
        path = '/'.join(os.getcwd().split('/'))
        with open(os.path.join(path, 'data/contacts.json'), 'r') as file:
            data = json.load(file)[1:]
            mas = []
            if type == 'name':
                for contact in data:
                    if contact['name'] == value:
                        mas.append(contact)
                return mas
            elif type == 'phone':
                for contact in data:
                    if contact['phone'] == value:
                        mas.append(contact)
                return mas
            return data


    def update(self, id, Contact:CONTACT):
        path = '/'.join(os.getcwd().split('/'))
        with open(os.path.join(path, 'data/contacts.json'), 'r') as file:
            data = json.load(file)
            for contact in data[1:]:
                if contact['id'] == id:
                    contact['name'] = Contact.name
                    contact['phone'] = Contact.phone
                    contact['email'] = Contact.email
                    break
        with open(os.path.join(path, 'data/contacts.json'), 'w') as file:
            json.dump(data, file, indent=4)


    def delete(self, id):
        path = '/'.join(os.getcwd().split('/'))
        with open(os.path.join(path, 'data/contacts.json'), 'r') as file:
            data = json.load(file)
            for contact in data[1:]:
                if contact['id'] == id:
                    data.remove(contact)
                    break
        with open(os.path.join(path, 'data/contacts.json'), 'w') as file:
            json.dump(data, file, indent=4)

    def import_export(self,  mode, path_csv_file=None):
        try:
            if mode == 'import':
                with open(path_csv_file, 'r') as file_new:
                    file_new = csv.DictReader(file_new)
                    path = '/'.join(os.getcwd().split('/'))
                    with open(os.path.join(path, 'data/contacts.json'), 'r') as file:
                        data = json.load(file)
                        for row in file_new:
                            contact = CONTACT(row['name'], row['phone'], row['email'])
                            contact.contact_id = data[0]['count'] + 1
                            data[0]['count'] = data[0]['count'] + 1
                            data.append({
                                'id': contact.contact_id,
                                'name': contact.name,
                                'phone': contact.phone,
                                'email': contact.email
                            })
            elif mode == 'export':
                path = '/'.join(os.getcwd().split('/'))
                with open(os.path.join(path, 'data/contacts.json'), 'r') as file:
                    data = json.load(file)
                with open(os.path.join(path, 'data/export_contacts.json'), 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=['id', 'name', 'phone', 'email'])
                    writer.writeheader()
                    for task in data[1:]:
                        writer.writerow(task)
                with open(os.path.join(path, 'data/contacts.json'), 'w') as file:
                    json.dump(data, file, indent=4)
        except Exception as e:
            print(e)





