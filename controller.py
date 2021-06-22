import os
import sqlite3


def help_menu():
    print('''------COMMANDS------\ns - search\na - add phone number\nd - delete phone number\nall - show all
help - to show this commands again\nctrl + D - to quit\n--------------------''')


class Controller:
    """Controller for database"""

    def __init__(self):

        if os.path.exists('.' + os.sep + 'persons.db'):
            self.connection = sqlite3.connect('persons.db')
        else:
            self.connection = sqlite3.connect('persons.db')
            cur = self.connection.cursor()
            cur.execute('''CREATE TABLE persons (id INTEGER	constraint persons_pk primary key autoincrement,
             name text, phone text)''')

        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def save(self, person):
        """Put person object to save to database"""

        self.cursor.execute(f"INSERT INTO persons (name, phone) VALUES ('{person.name}', '{person.number}')")
        # Save (commit) the changes
        self.connection.commit()

    def delete(self, person_id):
        """remove person object from database"""

        self.cursor.execute(f"DELETE FROM persons WHERE id={person_id}")
        self.connection.commit()

    def search(self, search):
        self._person_formatter(f"SELECT * from persons where phone LIKE '%{search}%' OR name LIKE '%{search}%'")

    def show_all(self):
        """Show all persons"""
        self._person_formatter()

    def _person_formatter(self, query_string="select * from persons"):
        """Formats output to one format"""

        cur = self.cursor

        print('{0:<5}'.format('ID'), end=' ')
        print('{0:20}'.format('Name'), end=' ')
        print('{0:20}'.format('Number'))
        for row in cur.execute(query_string):
            print('{0:<5}'.format(row[0]), end=' ')
            print('{0:20}'.format(row[1]), end=' ')
            print('{0:20}'.format(row[2]), end=' ')
            print()
