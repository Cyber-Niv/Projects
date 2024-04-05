import sqlite3

class Database:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS comp(
            id Integer Primary Key,
            name text,
            division text,
            date text,
            email text,
            complaint text   
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # INSERT FUNCTION
    def insert(self,name,division,date,email,complaint):
        self.cur.execute("insert into comp values (NULL,?,?,?,?,?)",
                         (name,division,date,email,complaint))
        self.con.commit()

    # FETCH DATA FROM DB
    def fetch(self):
        self.cur.execute("select * from comp")
        rows = self.cur.fetchall()
        #print(rows)
        return rows

    # DELETE A RECORD FROM DB
    def remove(self,id):
        self.cur.execute("delete from comp where id =?", (id,))
        self.con.commit()

    # UPDATE A RECORD IN DB
    def update(self,id,name, division, date, email, complaint):
        self.cur.execute("update comp set name=?, division=?, date=?, email=?, complaint=? where id=?",
        (name, division, date, email, complaint,id))
        self.con.commit()

#o = Database("complaints.db")
#o.insert("update","dept","30-03-2024","nivedh@gmail.com","No Complaint")
#o.remove("4")
#o.update("3", "update test","DIV I","30-03-2024","update@gmail.com","UPDATED")
#o.fetch()
