import sys
from sys import argv
from Repository import repo
from Hat import Hat
from Order import Order
from Supplier import Supplier


def parse_config(config_path):
    with open(config_path) as text:
        lines_list = text.readlines()
    first_line = lines_list[0].strip().split(',')
    num_of_hats = int(first_line[0])
    num_of_suppliers = int(first_line[1])
    for i in range(num_of_hats + 1, num_of_hats + num_of_suppliers + 1):
        line = lines_list[i].strip().split(',')
        repo.suppliers.insert(Supplier(int(line[0]), line[1]))
    for i in range(1, num_of_hats + 1):
        line = lines_list[i].strip().split(',')
        hat = Hat(int(line[0]), line[1], int(line[2]),int(line[3]))
        repo.hats.insert(hat)


def parse_orders(orders_path):
    with open(orders_path) as text:
        lines_list = text.readlines()
    for i in range(0, len(lines_list)):
        line = lines_list[i].strip().split(',')
        hat = repo.hats.find_by_topping(line[1])
        repo.orders.insert(Order(i, line[0], hat.id))
        if hat.quantity > 1:
            repo.hats.update({'quantity': hat.quantity - 1}, {'id': hat.id});
        else:
            repo.hats.delete(hat.id)


class main(argv):
    config_path = argv[1]
    orders_path = argv[2]
    output_path = argv[3]
    #
    repo.create_tables()
    parse_config(config_path)
    parse_orders(orders_path)
    # print
    output_file = open(output_path, "w+")
    for r in repo.get_orders_with_supplier():
        output_file.write('{} {} {} \n'.format(r.topping.decode("utf-8") , r.supplier.decode("utf-8") , r.location.decode("utf-8")))
    output_file.close()
    #
    for r in repo.hats.find_all():
        print('{} {} {} {}'.format(r.id ,r.topping, repo.suppliers.find(r.supplier).name , r.quantity))


    print('finished')
    sys.exit()
