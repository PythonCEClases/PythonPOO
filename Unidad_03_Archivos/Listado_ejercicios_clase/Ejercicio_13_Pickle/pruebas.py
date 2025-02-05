from clases import Menu, ProgrammingLanguage, Repository

opciones = ["Add language", "Remove language", "Show languages", "Count", "Exit"]
menu = Menu("Programming languages", opciones)

repo = Repository()

while True:

    menu_option = menu.show_menu()

    match menu_option:
        case "1":
            print("**Add language**")
            name = input("Name: ")
            extension = input("Extension: ")
            description = input("Description: ")
            language = ProgrammingLanguage(name, extension, description)
            if repo.add_language(language):
                print("Language added!!!")
            else:
                print("Language exists!!!")

        case "2":
            print("**Remove language**")
            name = input("Language Name: ")
            result = repo.remove_language(name)
            if result:
                print("Language removed!!!")
            else:
                print("Language not found!!!")

        case "3":
            print("**Show languages**")
            for lang in repo.show_languages():
                print(lang)

        case "4":
            print("**Count**")
            print(f"Langueges number: {repo.count_languages()}")

        case "5":
            print("**Exit**")
            break
        case _:
            print("Invalid option!!!")
