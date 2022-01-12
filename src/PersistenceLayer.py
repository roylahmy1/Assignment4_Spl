class PersistenceLayer:

    def __init__(self):
        self.conn = sqlite3.connect(‘myDB.db’)

        def close(self):
            self.conn.commit()
            self.conn.close()

        def create_tables(self): …  # same code as before
        def insert_student(self, id, name): …  # same code as before
        def insert_assignment(self, id, output): …  # same code as before
        def insert_grade(self, sID, assID, grade): …  # same code as before

        def get_assignment_expected_output(self, assID):
            c = self.conn.cursor()
            c.execute("""SELECT output FROM assignments WHERE id = ? 
		   """, [assID])
            return c.fetchone()[0]

        def get_all_grades(self):
            c = self.conn.cursor()
            return c.execute("""SELECT students.name, assignment.id, grade
           FROM students JOIN grades 
           ON students.id = grades.sID""").fetchall()

    psl = PersistenceLayer()  # persistence layer object (psl) is a singleton
    atexit.register(psl.close)  # register pls object to automatically run its close() method
