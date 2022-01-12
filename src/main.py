from sys import argv
from Repository import repo
from src import Hat
from src.Order import Order
from src.Supplier import Supplier


def parse_config(config):
    with open(config) as text:
        lines_list = text.readlines()
    first_line = lines_list[0].strip().split(',')
    num_of_hats = first_line[0]
    num_of_suppliers = first_line[1]
    for i in range(1, num_of_hats + 1):
        line = lines_list[i].strip().split(',')
        repo.hats.insert(Hat(line[0], line[1], line[2], line[3]))
    for i in range(num_of_hats + 1, num_of_hats + num_of_suppliers + 1):
        line = lines_list[i].strip().split(',')
        repo.suppliers.insert(Supplier(line[0], line[1]))


def parse_orders(orders):
    with open(orders) as text:
        lines_list = text.readlines()
    for i in range(0, len(lines_list)):
        line = lines_list[i].strip().split(',')
        repo.orders.insert(Order(i, line[0], repo.hats.find(topping = line[1]).))


def print_db():
    repo.


class main(argv):
    config = argv[0]
    orders = argv[1]
    true_output = argv[2]
    true_database = argv[3]
