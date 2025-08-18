'''
Додаток який буде зберігати нотатки
This is my note<that i am taking on my laptop
- Created on 19.12.2025 20:15

[("This is my note, that i am taking on my laptop","19.12.2025 20:15")]

[{text:"This is my note, that i am taking on my laptop", creation_date:"19.12.2025 20:15"}]
1) створити словник нотаток та записати в нього інфрмацію
2) написати функцію  яка буде виводити 1 нотатку
3) написати функцію  яка буде виводити усі нотатки
4) написати цикл який буде отримувати інфо від користувача
та давати якусь відповідь

'''
from datetime import datetime
note_list = [] #[{creation_date:"19.12.2025 20:15", text:"This is my note, that i am taking on my laptop"}]
note_file = 'notes.txt'

commands = """
COMMANDS:
1) 'exit' - to close the App
2) 'add' - to add a new Note
3) 'print_note i' - to print note number "i"
4) 'print_all' - print all notes
5) 'help' - to see all commands
"""


def add_new_note(note_text):
    note_creation_date = datetime.today().strftime('%d.%m.%Y %H:%M')
    note_list.append({'text':note_text, 'creation_date':note_creation_date})
    print('Note added')


def print_note(note_index:int):
    note = note_list[note_index-1]
    print(f"Note: {note['text']} \n - Created on {note['creation_date']}")


def print_all_notes():
    for note in note_list:
        print(f"Note: {note['text']}\n - Created on {note['creation_date']}\n")

def save_notes():
    with open(note_file, 'w',encoding='utf-8') as file:
        for note in note_list:
            file.write(f"{note['text']};{note['creation_date']}\n")

def read_notes():
    note_list = []
    with open(note_file, 'r', encoding='utf-8') as file:
        for line in file: #1;Created on 18.08.2025 10:14
            text, date = line.strip().split(';')
            note_list.append({'text':text, 'creation_date':date})
        return note_list

def init():
    global note_list
    note_list = read_notes()
    print('Welcome in our Helper Bot!')
    print(commands)

def main():
    while True:
        command, *args = input('Please enter a command: ').strip().split()
        if command == 'exit':
            save_notes()
            print('Goodbye')
            break
        elif command == 'help':
            print(commands)
        elif command == 'add':
            text = input('Please enter your text: ')
            add_new_note(text)
        elif command == 'print_all':
            print_all_notes()
        elif command == 'print_note':
            index = int(args[0])
            if index < 1 or index > len(note_list):
                print('Please enter a valid number of Note')
                continue
            print_note(index)


init()
main()





# text = input('Please enter your text: ')
# add_new_note(text)
# print(note_list)
# text = input('Please enter your text: ')
# add_new_note(text)
# print(note_list)
# print_all_notes(note_list)
# print_note(1)
