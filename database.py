import sqlite3 as sql3


class Database():
    def __init__(self):
        self.sql=sql3.Connection("bookshelf.sqlite")
        
        self.cursor=self.sql.cursor()
        #self.cursor.execute("CREATE TABLE IF NOT EXISTS bookshelf (id INTEGER(10) PRIMARY KEY,book_name varchar(255),book_writer varchar(255),book_star numeric(9,2),read_state varchar(255))")
        #self.sql.commit()
    def book_add(self):
        self.book_name=input("input book name=")
        self.book_writer=input("input book writer=")
        self.book_star=input("input star number=")
        self.read_state=input("input state=")
        self.cursor.execute(f"INSERT INTO bookshelf (book_name,book_writer,book_star,read_state) VALUES('{self.book_name}','{self.book_writer}','{self.book_star}','{self.read_state}')")
        self.sql.commit()
        
    def book_list(self):
        self.cursor.execute("SELECT * FROM bookshelf")
        list=self.cursor.fetchall()
        for i in list:
            for j in i:
                print(j,end=" ")
            print("")
    def book_update(self):
        self.cursor.execute(f"UPDATE bookshelf SET {input('what is update(book_name/book_writer/book_star/read_state')}='{input('value:')}' WHERE id={input('id=')}")
        self.sql.commit()
    def book_del(self):
        self.cursor.execute(f"DELETE FROM bookshelf WHERE id={input('id=')}")
        self.sql.commit()


    