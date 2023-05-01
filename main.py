phone_book = {}


def add_new_contact():
    name = input("Proszę poaj nazwę kontaktu do dodania: ")
    if name in phone_book:
        print("Podany kontakt już istnieje!")
    else:
        phone = input("Proszę podaj numer telefonu do dodania: ")
        phone_book[name] = phone
        print("Kontakt został dodany!")


def delete_contact():
    name = input("Proszę podaj nazwę kontaktu do usunięcia: ")
    if name in phone_book:
        del phone_book[name]
        print("Kontakt został usunięty!")
    else:
        print("Podany kontakt nie istnieje!")


def search_contact():
    name = input("Proszę podaj nazwę kontaktu do wyszukania: ")
    if name in phone_book:
        print("Numer telefonu:", phone_book[name])
    else:
        print("Podany kontakt nie istnieje!")


def modify_contact():
    name = input("Proszę podaj nazwę kontaktu do modyfikacji: ")
    if name in phone_book:
        phone = input("Proszę podaj numer telefonu: ")
        phone_book[name] = phone
        print("Kontakt został zmodyfikowany!")
    else:
        print("Podany kontakt nie istnieje!")


def show_book():
    if len(phone_book) == 0:
        print("Brak zapisanych kontaktów!")
    else:
        for key, value in phone_book.items():
            print(key, value)

print(""""
Twoje kontakty:
1 - Dodaj nowy kontakt
2 - Usuń kontakt
3 - Wyszukaj kontakt
4 - Zmodyfikuj kontakt
5 - Wyświetl wszystkie kontakty
6 - Wyjdź z zakładki kontakty""")

while True:

    option = int(input("Proszę wybierz opcję (1-6):"))

    if option == 1:
        add_new_contact()
    elif option == 2:
        delete_contact()
    elif option == 3:
        search_contact()
    elif option == 4:
        modify_contact()
    elif option == 5:
        show_book()
    elif option == 6:
        print("Wychodzę z zakładki kontakty...")
        break
    else:
        print("Opcja poza zakresem!")

