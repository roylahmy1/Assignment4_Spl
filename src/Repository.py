import atexit
import sqlite3

from Hats import Hats
from Suppliers import Suppliers
from Orders import Orders
from DAO import DAO
from OrdersWithSupplier import OrderWithSupplier


_conn = sqlite3.connect('database.db')


class Repository(object):
    def __init__(self):
        self._conn = sqlite3.connect('database.db')
        self._conn.text_factory = bytes
        self.hats = Hats(self._conn) #DAO(Hat, self._conn)
        self.suppliers = Suppliers(self._conn) #DAO(Supplier, self._conn)
        self.orders =  Orders(self._conn) #DAO(Order, self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
            DROP TABLE IF EXISTS 'suppliers'
        """)
        self._conn.executescript("""
            CREATE TABLE suppliers (
                id                 INTEGER     PRIMARY KEY,
                name                  TEXT      NOT NULL
            );
            
        """)
        self._conn.executescript("""
            DROP TABLE IF EXISTS 'hats'
        """)
        self._conn.executescript("""
            CREATE TABLE hats (
                id      INTEGER         PRIMARY KEY,
                topping    TEXT        NOT NULL,
                supplier    INTEGER      NOT NULL,
                quantity   INTEGER       NOT NULL,
                
                FOREIGN KEY(supplier) REFERENCES suppliers(id)
            );

        """)
        self._conn.executescript("""
            DROP TABLE IF EXISTS 'orders'
        """)
        self._conn.executescript("""
            CREATE TABLE orders (
                id      INTEGER     PRIMARY KEY,
                location  INTEGER     NOT NULL,
                hat           INTEGER     NOT NULL,
                FOREIGN KEY(hat)     REFERENCES hats(id)
            );
        """)

    def get_orders_with_supplier(self):
        c = self._conn.cursor()
        #

        alls = c.execute("""
            SELECT location FROM orders
        """).fetchall()


        #
        all = c.execute("""
            SELECT hats.topping, suppliers.name, orders.location 
            FROM orders
            JOIN hats ON hats.id = orders.hat
            JOIN suppliers ON suppliers.id = hats.supplier
        """).fetchall()

        return [OrderWithSupplier(*row) for row in all]


# see code in previous version...

# singleton
repo = Repository()
atexit.register(repo._close)
