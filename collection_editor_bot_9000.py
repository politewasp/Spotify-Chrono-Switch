import util
import sys
import json
import credentials as cred
from credentials import sp
import os


def main_menu():
    options = [0, 1, 2, 3, 4, 5]
    menu = 'SPOTIFY COLLECTION EDITOR BOT 9000\n' \
           '0 - create new collection\n' \
           '1 - delete a collection\n' \
           '2 - edit existing collection\n' \
           '3 - delete all collections\n' \
           '4 - commit a war crime\n' \
           '5 - exit\n' \
           'Which action would you like to take? \n'

    error = 'Invalid option selected. \n'

    user_input = int(input(menu))

    while user_input not in options:
        print(error)
        user_input = int(input(menu))
    return user_input


def create_new_collection(collections):
    name = input('Please enter the name of the new collection. \n')
    collections[name] = []
    print(f'Collection \'{name}\' has been created. ')
    edit_collection(collections[name])


def delete_collection():
    pass


def edit_collection(collection):
    functions = ['add', 'remove']
    name = collection['name']
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
    command.split(' ')
    function = command[0]
    while function not in functions:
        print(error)
        command = input()
        command.split(' ')
        function = command[0]
    item = command[1]
    item_type = input('Enter the new item\'s type. (album, artist, playlist, etc.)')
    results = sp.search(q=f'{item_type}:' + item, type=f'{item_type}')
    items = results[f'item_type']['items']
    if len(items) != 1:
        uri = input('Item not found. Please input URI. ')
    else:
        uri = items[0]['uri']
    item_dict = {'name': item, 'uri': uri, 'type': item_type}
    collection.append(item_dict)
    return collection


def delete_all_collections():
    pass


def commit_war_crime():
    print('The Geneva Convention has been sufficiently violated in the former Republic of Yugoslavia. ')


def exit_program(filename, collections):
    with open(filename, 'w+') as write_file:
        json.dump(collections, write_file)
    print('peace out, bitch. ')


def run_process(function):
    function()


def main():
    """User Interface for Collection Editor. Add more user functions in list below. """
    user_functions = [create_new_collection, delete_collection, edit_collection,
                      delete_all_collections, commit_war_crime, exit_program]

    filename = 'collections.json'
    try:
        with open(filename, 'r') as read_file:
            collections = json.load(read_file)
    except FileNotFoundError:
        with open(filename, 'w+') as write_file:
            collections = {'collections': {}, 'user': 'politewasp'}
            json.dump(collections, write_file)

    run = 'Y'
    while run == 'Y':
        user_selection = main_menu()
        if user_selection == 5:  # remove this once application class created
            break
        process = user_functions[user_selection]
        run_process(process)
        print('Action completed. \n')
        run = input('Would you like to continue editing collections? (Y/N) \n')
        print('\n')

    exit_program(filename, collections)


if __name__ == '__main__':
    main()
