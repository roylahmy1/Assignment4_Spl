from Supplier import Supplier

class Suppliers:

    def __init__(self, connection):
        self.connection = connection

    def insert(self, supplier):
        self.connection.execute("""
                INSERT INTO Suppliers (id, name)
                VALUES (?,?)
        """, [supplier.id, supplier.name])

    def find(self, supplier_id):
        c = self.connection.cursor()
        c.execute("""
            SELECT id, name FROM Suppliers WHERE id = ?
        """, [supplier_id])
        return Supplier(*c.fetchone())

    def find_all(self):
        c = self.connection.cursor()
        all = c.execute("""
            SELECT id, name FROM Suppliers
        """).fetchall()
        return [Supplier(*row) for row in all]
