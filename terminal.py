


while True:
    question = input(
        'Enter an action:\n'
        '1. Go to databases = "db"\n'
        '2. Go to gui = "gui"\n'
    )

    match question:
        case 'db':
            database()
        case 'gui':
            run_gui()
