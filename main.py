from controller import Controller, help_menu
from person import Person


def main():
    controller = Controller()
    print("Welcome to your phone book!")
    help_menu()
    while True:
        try:
            do_what = input('What you want to do? ')
            if do_what == 's':
                while True:
                    search = input('Enter part of the name or number: ')
                    controller.search(search)
                    break
            elif do_what == 'a':
                while True:
                    name = input('Enter name: ')
                    phone = input('Enter number: ')
                    man = Person(name, phone)
                    controller.save(man)
                    break
            elif do_what == 'd':
                while True:
                    controller.show_all()
                    search = input('Enter ID of number to delete: ')
                    controller.delete(search)
                    break
            elif do_what == 'all':
                controller.show_all()
            elif do_what == 'help':
                help_menu()
            else:
                print(f'Unrecognized command - {do_what}')
        except EOFError:
            print('See you later!')
            break


if __name__ == '__main__':
    main()
