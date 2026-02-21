from warehouse import Warehouse
from argparse import ArgumentParser
import os


def main():
    """
    This is a translation of the assignment given to us in the
    Fundamentals Data Structures course (original language - C++)

    A copy of the assignment (the source code for this translation)
    has been included in the repository (.\fdshw1.cpp)

    Short version of the assignment:
        A .txt file is provided with weights and uuids of crates
        The program must create a Warehouse (a class-container for the code) that contains:
            - 10 Shelves that form a node-backed linked list
                ~ each shelf can store up to 4 crates and 1000kgs
            - Arrival Queue - node-backed queue in which the crates are stored before processing
                ~ no weight or size limitations
            - Sorting Floor
                ~ only defined and still unused, but will be used to sort crates in the future

        The crates in the text file are ordered in such a way that it's trivial to fit them in the shelves
        without the need of any kind of sorting algorithm or lookaheads

    For simplicity, crates will be replaced with (uuid, weight) tuples
    :return:
    """

    argparser = ArgumentParser()
    argparser.add_argument('-filename', default='crates.txt', nargs='?')
    args = argparser.parse_args()

    if not os.path.exists(args.filename):
        print(f'File \'{args.filename}\' does not exist')
        return

    # temporary storage for crates
    # for optimisation, we could directly add the crates to the Warehouse, but requirements exist ¯\_(ツ)_/¯
    crates = []

    # read the file
    with open(args.filename) as file:
        for line in file:
            weight, uuid = line.split()
            weight = int(weight)
            crates.append((uuid, weight))

    # instantiate warehouse
    w = Warehouse(crates)

    # make a copy of the head of the shelves linked list
    head = w.shelves_head

    for x in range(3, -1, -1):
        head_copy = head
        # print(' ', end='')
        while head_copy is not None:
            msg = '| ' + ('-'*7) + ' '
            # if head_copy.crates[x] is not None:
            if x in range(len(head_copy.crates)):
                uuid, weight = head_copy.crates[x]
                msg = f'| {uuid} {weight}{" "*(5-len(str(weight)))}'
            print(msg, end='')
            head_copy = head_copy.next
        print()

    # validate output
    print(w.validate())


if __name__ == '__main__':
    main()
