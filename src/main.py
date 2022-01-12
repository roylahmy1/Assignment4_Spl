import sys
from sys import argv
from Repository import repo
from src import Hat
from src.Order import Order
from src.Supplier import Supplier


def parse_config(config_path):
    with open(config_path) as text:
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


def parse_orders(orders_path):
    with open(orders_path) as text:
        lines_list = text.readlines()
    for i in range(0, len(lines_list)):
        line = lines_list[i].strip().split(',')
        hat = repo.hats.find({'topping': line[1]})[0]
        repo.orders.insert(Order(i, line[0], hat[0]))
        if hat.quantity > 1:
            repo.hats.update({'quantity': hat.quantity - 1}, {'id': hat.id});
        else:
            repo.hats.delete({'id': hat.id});


class main(argv):
    config_path = argv[1]
    orders_path = argv[2]
    output_path = argv[3]
    #
    parse_config(config_path)
    parse_orders(orders_path)
    # print
    output_file = open(output_path, "w+")
    for r in repo.get_orders_with_supplier():
        output_file.write(r + "\r\n")
    output_file.close()
    sys.exit()
