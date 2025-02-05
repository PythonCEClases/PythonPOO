# Definición de clases
import os
import pickle


class Menu:
    def __init__(self, title, options):
        self.title = title
        self.options = options

    def show_menu(self):
        result = self.title + "\n"
        for i in range(len(self.options)):
            result += f"{i+1}. {self.options[i]}\n"
        result += "Choose option: "
        print("\n", result)
        option = input()
        return option


class ProgrammingLanguage:
    def __init__(self, name, extension, description):
        self.name = name
        self.extension = extension
        self.description = description

    def __str__(self):
        return f"{self.name} ({self.extension})"

    def __repr__(self):
        return f"ProgrammingLanguage({self.name}, {self.extension}, {self.description})"

    def __eq__(self, other):
        return self.name == other.name


class Repository:
    
    def __init__(self):
        directorio = os.path.dirname(os.path.abspath(__file__))
        self.ruta_archivo = os.path.join(directorio, "languages.pkl")
        if os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, "rb") as file:
                self.languages = pickle.load(file)
        else:
            self.languages = []

    def search_language(self, language_name):
        for i in range(len(self.languages)):
            if self.languages[i].name.lower() == language_name.lower():
                return i
        return -1

    def add_language(self, language):
        if language not in self.languages:
            self.languages.append(language)
            return True
        return False

    def remove_language(self, language_name):
        index = self.search_language(language_name)
        if index != -1:
            self.languages.pop(index)
            return True
        return False

    def count_languages(self):
        return len(self.languages)

    def show_languages(self):
        return self.languages

    def save(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self.languages, file)

    # Destructor
    # al destruir el objeto repo se guarda la lista de lenguajes en un archivo
    def __del__(self):
        self.save(self.ruta_archivo)