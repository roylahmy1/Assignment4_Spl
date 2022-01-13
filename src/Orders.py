from Order import Order

class Orders:

    def __init__(self, connection):
        self.connection = connection

    def insert(self, order):
        self.connection.execute("""
                INSERT INTO Orders (id, location, hat)
                VALUES (?,?,?)
        """, [order.id, order.location, order.hat])

    def find(self, order_id):
        c = self.connection.cursor()
        c.execute("""
            SELECT * FROM Orders WHERE id = ?
        """, [order_id])
        return Order(*c.fetchone())

    def find_all(self):
        c = self.connection.cursor()
        all = c.execute("""
            SELECT * FROM Orders
        """).fetchall()
        return [Order(*row) for row in all]
