import sqlite3

def main():
    while True:
        nameToSearch = input('Introduce the name of the student:')
        start(nameToSearch)


def start(nameSearch):
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    
    rows = cursor.execute(f"SELECT * FROM student WHERE name = '{nameSearch}'")
    
    listTitles = ['id', 'name','lastname']
    
    for row in rows:
        element = row
        for i in range(len(element)):
            print(f"{listTitles[i]}: {element[i]}".title())
            i += 1
    
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()