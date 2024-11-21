from tkinter.font import names


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
        path = '/'.join(os.getcwd().split('/')[:-1])
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
        path = '/'.join(os.getcwd().split('/')[:-1])
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


    def update(self, id, contact:CONTACT):
        path = '/'.join(os.getcwd().split('/')[:-1])
        with open(os.path.join(path, 'data/contacts.json'), 'r') as file:
            data = json.load(file)[1:]
            for contact in data:
                if contact['id'] == id:
                    contact['name'] = contact.name
                    contact['phone'] = contact.phone
                    contact['email'] = contact.email
                    break
        with open(os.path.join(path, 'data/contacts.json'), 'w') as file:
            json.dump(data, file, indent=4)


    def delete(self, id):
        path = '/'.join(os.getcwd().split('/')[:-1])
        with open(os.path.join(path, 'data/contacts.json'), 'r') as file:
            data = json.load(file)
            for i, contact in enumerate(data):
                if contact['id'] == id:
                    data.pop(i)
                    break
        with open(os.path.join(path, 'data/contacts.json'), 'w') as file:
            json.dump(data, file, indent=4)

    def import_export(self, path_csv_file, mode):
        if mode == 'import':
            with open(path_csv_file, 'r') as file_new:
                file_new = csv.DictReader(file_new)
                path = '/'.join(os.getcwd().split('/')[:-1])
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
                with open(os.path.join(path, 'data/contacts.json'), 'w') as file:
                    json.dump(data, file, indent=4)

        elif mode == 'export':
            path = '/'.join(os.getcwd().split('/')[:-1])
            with open(os.path.join(path, 'data/contacts.json'), 'r') as file:
                data = json.load(file)
            with open(os.path.join(path, 'data/export_contacts.json'), 'w') as file:
                json.dump(data, file, indent=4)
        else:
            return 'Invalid mode'

