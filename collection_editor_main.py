import CollectionEditorBot9000 as ceb


def main():
    """User Interface for Collection Editor. Add more user functions in list below. """
    filename = 'collections.json'
    bot = ceb.CollectionEditorBot9000(json_filename=filename)

    run = 'Y'
    while run.upper() == 'Y':
        user_selection = bot.main_menu()
        bot.run_process(user_selection)
        print('Action completed. \n')
        run = input('Would you like to continue editing collections? (Y/N) \n')
        print('\n')

    bot.exit_program()


if __name__ == '__main__':
    main()