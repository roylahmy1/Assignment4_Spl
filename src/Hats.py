from Hat import Hat

class Hats:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, hat):
        self.connection.execute("""
                INSERT INTO Hats (id, topping, supplier, quantity)
                VALUES (?,?,?,?)
        """, [hat.id, hat.topping, hat.supplier, hat.quantity])

    def find(self, hat_id):
        c = self.connection.cursor()
        c.execute("""
            SELECT * FROM Hats WHERE id = ?
        """, [hat_id])
        return Hat(*c.fetchone())

    def find_by_topping(self, topping):
        c = self.connection.cursor()
        c.execute("""
            SELECT * FROM Hats WHERE topping = ?
        """, [topping])
        return Hat(*c.fetchone())

    def find_all(self):
        c = self.connection.cursor()
        all = c.execute("""
            SELECT * FROM Hats
        """).fetchall()
        return [Hat(*row) for row in all]

    def delete(self, hat_id):
        stmt = 'DELETE FROM Hats WHERE id = {}'.format(hat_id)

        c = self.connection.cursor()
        c.execute(stmt)

    def update(self, set_values, cond):
        set_column_names = set_values.keys()
        set_params = set_values.values()

        cond_column_names = cond.keys()
        cond_params = cond.values()

        params = list(set_params) + list(cond_params)

        stmt = 'UPDATE Hats SET {} WHERE {}'.format(', '.join([set + '=?' for set in set_column_names]),
                                                  ' AND '.join([cond + '=?' for cond in cond_column_names]))

        self.connection.execute(stmt, params)