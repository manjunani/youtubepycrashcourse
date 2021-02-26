# importing statements
import sqlite3 as lite


# functionality goes here
class DatabaseManage(object):

    def __init__(self):
        global conn
        try:
            conn = lite.connect('courses.db')
            with conn:
                cur = conn.cursor()
                cur.execute(
                    "CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEAFULT 1)"
                )
        except Exception:
            print("Unable to create DB !")

    # method for insterting data
    def insert_data(self, data):
        try:
            with conn:
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO course(name, description, price, is_private) VALUES(?, ?, ?, ?)", data
                )
                return True
        except Exception:
            return False

    def fetch_data(self):
        try:
            with conn:
                cur = conn.cursor()
                cur.execute(
                    "SELECT * FROM course"
                )
                return cur.fetchall()
        except Exception:
            return False

    def delete_data(self, id):
        try:
            with conn:
                cur = conn.cursor()
                sql = "delete from course where id = ?"
                cur.execute(sql, [id])
                return True
        except Exception:
            return False


# TODO: provide interface to user here
def main():
    print("#"*50)
    print("\n :: COURSE MANAGEMENT :: \n")
    print("#"*50)

    db = DatabaseManage()

    print("#"*50)
    print("\n :: User Manual :: \n")
    print("#"*50)

    print("\n Press 1. Insert new course\n")
    print("Press 2. Show all Courses\n")
    print("Press 3. Delete a Course( Need ID of the course)")
    print("#"*40)
    choice = int(input("\nEnter a choice:"))
    if choice == 1:
        name = input("\n Enter Name: ")
        description = input("\n Enter Derscription: ")
        price = input("\n Enter Price: ")
        private = input("\n Is this course Private(0/1): ")
        if db.insert_data([name, description, price, private]):
            print("Course was inserted successfully")
        else:
            print("Ooops !!!!!!!!!!!!!")
    elif choice == 2:
        print("\n::Courses List ::")
        for index, item in enumerate(db.fetch_data()):

            print("Course Id:" + str(item[0]))
            print("Course Name:" + str(item[1]))
            print("Course Description:" + str(item[2]))
            print("Course Price:" + str(item[3]))
            private = 'Yes' if item[4] else "No"
            print("Is it Private:" + private)
            print("\n")
    elif choice == 3:
        record_id = input("Enter the course id: ")
        if db.delete_data(record_id):
            print("deleted ZSuccessfully")
        else:
            print("Not deleted")
    else:
        print("Try entering 1||2||3")


if __name__ == '__main__':
    main()
