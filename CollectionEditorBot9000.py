import util
import sys
import json
import credentials as cred
from credentials import sp
import os


class CollectionEditorBot9000:
    def __init__(self, json_filename='collections.json'):
        self.filename = json_filename
        self.options = [0, 1, 2, 3, 4, 5]
        self.user_functions = [self.create_new_collection, self.delete_collection, self.edit_collection,
                               self.delete_all_collections, self.commit_war_crime, self.exit_program]
        self.menu = 'SPOTIFY COLLECTION EDITOR BOT 9000\n' \
                    '0 - create new collection\n' \
                    '1 - delete a collection\n' \
                    '2 - edit existing collection\n' \
                    '3 - delete all collections\n' \
                    '4 - commit a war crime\n' \
                    '5 - exit\n' \
                    'Which action would you like to take? \n'
        self.error = 'Invalid option selected. \n'
        self.war_crime = 'The Geneva Convention has been sufficiently violated in the former Republic of Yugoslavia. '
        self.collections = self.read_json()

    def main_menu(self):
        user_input = int(input(self.menu))
        while user_input not in self.options:
            print(self.error)
            user_input = int(input(self.menu))
        self.process = user_input
        return user_input

    def create_new_collection(self):
        name = input('Please enter the name of the new collection. \n')
        self.collections['collections'][name] = []
        print(f'Collection \'{name}\' has been created. ')

    def delete_collection(self):
        name = input('Please enter the name of the collection you would like to delete. \n')
        confirm = input(f'Are you sure you would like to delete {name}? This action cannot be undone. \n')
        if confirm and self.collections[name]:
            del self.collections[name]
        pass

    def edit_collection(self):
        name = input('Please enter the name of the collection you would like to edit. \n')
        collection = self.collections['collections'][name]
        functions = ['add', 'remove']
        add_instructions = f'To add a new item to the collection \'{name}\' \n' \
                           f'type \'add\' followed by the name of the item.' \
                           f'For example, to add the album Make It Big by Wham! to the collection, \n' \
                           f'type: \n' \
                           f'add Make It Big \n' \
                           f'And you will be prompted for the type of the item. \n'

        remove_instructions = f'To remove an item from the collection \'{name}\' \n' \
                              f'type \'remove\' followed by the ID of the item listed above.' \
                              f'For example, to remove the album Make It Big by Wham! with ID 2 from the collection, \n' \
                              f'type: \n' \
                              f'remove 2 \n' \
                              f'And the item will be removed from the list. \n'

        error = 'Invalid input. '
        error404 = 'Item not found. Please try entering the URI. '
        print(add_instructions)
        print(remove_instructions)
        command = input()
        command = command.split(' ', 1)
        function = command[0]
        while function not in functions:
            print(error)
            print(function)
            command = input()
            command.split(' ', 1)
            function = command[0]
        item = command[1]

        if function == functions[0]:
            item_type = input('Enter the new item\'s type. (album, artist, playlist, etc.)\n')
            results = sp.search(q=f'{item_type}: ' + item, type=f'{item_type}')
            print(results)
            items = results[f'{item_type}s']['items']
            if len(items) == 0:
                uri = input('Item not found. Please input URI. \n')
            else:
                uri = items[0]['uri']
            item_dict = {'name': item, 'uri': uri, 'type': item_type}
            collection.append(item_dict)
            print(f'{item} has been added to collection {name}. ')
        elif function == functions[1]:
            for i in range(0, len(collection)):
                c_item = collection[i]
                if c_item['name'] == item:
                    del collection[i]
                    break
        return collection

    def delete_all_collections(self):
        self.collections = {}

    def commit_war_crime(self):
        print(self.war_crime)

    def exit_program(self):
        print(self.collections)
        with open(self.filename, 'w+') as write_file:
            json.dump(self.collections, write_file)
        print('peace out, bitch. ')

    def run_process(self, user_input):
        process = self.user_functions[user_input]
        process()

    def read_json(self):
        try:
            with open(self.filename, 'r') as read_file:
                collections = json.load(read_file)
        except json.decoder.JSONDecodeError:
            with open(self.filename, 'w+') as write_file:
                collections = {'collections': {}, 'user': 'politewasp'}
                json.dump(collections, write_file)
        except FileNotFoundError:
            with open(self.filename, 'w+') as write_file:
                collections = {'collections': {}, 'user': 'politewasp'}
                json.dump(collections, write_file)
        self.collections = collections
        return collections
