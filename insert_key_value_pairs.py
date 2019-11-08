import time
import argparse
import sys
import os
import importlib
from os import path
import importlib.util
import binary_tree
from avl_tree import avl
sys.path.append('hash-tables-sahu0957')
hash_functions = importlib.import_module("hash-tables-sahu0957.hash_functions")
hash_tables = importlib.import_module("hash-tables-sahu0957.hash_tables")

def main():
    parser = argparse.ArgumentParser(
            description="creates plots comparing search method efficiency across\
                         multiple data structures")
    parser.add_argument("--data_structure",
                        type=str,
                        help="specify a data structure ('avl', 'binary', or 'hash')",
                        required=True)
    parser.add_argument("--dataset",
                        type=str,
                        help="data file to add to the data structure",
                        required = True)
    parser.add_argument("--data_size",
                        type=int,
                        help="size of the data structure (must be 10,000 or less)")

    args = parser.parse_args()
    
    print("data_structure:" + str(args.data_structure))
    print("data_size:"+ str(args.data_size))
    print("data_file:" + str(args.dataset))
    if path.exists(args.dataset) != True:
        print("data file doesn't exist!")
        sys.exit(1)
    if args.data_size > 10000:
        print("data size too large! Specify between 30 and 10000")
        sys.exit(1)
    elif args.data_size < 30:
        print("data size too small! Specify between 30 and 10000")
    if args.data_structure == "hash":
        # Adding in values
        index = 0
        structure = hash_tables.ChainedHash(20000,
                                            hash_functions.h_rolling)
        keys = []
        values = []
        start = time.time()
        for l in open(args.dataset):
            # for simplicity, we'll just have the key
            # and value be the same
            keys.append(l)
            values.append(l)
            if index < args.data_size:
                structure.add(l, l)
            index += 1
        end = time.time()
        print("add_time:" + str(end-start))
        # Searching those values
        start = time.time()
        for key in keys:
            structure.search(key)
        end = time.time()
        print("search_keys:" + str(end-start))
        # search for nonexistant keys
        start = time.time()
        for key in keys:
            structure.search(key + '_nonexistant')
        end = time.time()
        print("search_nonexistant_time:" + str(end-start))
        sys.exit(0)
    elif args.data_structure == "binary":
        # inserting into root
        root = None
        keys = []
        values = []
        index = 0
        start = time.time()
        for l in open(args.dataset):
            keys.append(l)
            values.append(l)
            if (index < args.data_size):
                root = binary_tree.insert(root, key = l, value = l)
                index = index + 1
        end = time.time()
        print("add_time:" + str(end-start))
        # searching those keys
        start = time.time()
        for key in keys:
            search = binary_tree.search(root, key)
            # search nonexisting keyes
        end = time.time()
        print("searching_present_keys:" + str(end-start))
        start = time.time()
        for key in keys:
            search = binary_tree.search(root, key + '_nonexistant')
        end = time.time()
        print("search_nonexistant_keys:" + str(end-start))
        sys.exit(0)
    elif args.data_structure == "avl":
        # insert our keys
        structure = avl.AVL()
        keys = []
        values = []
        index = 0
        start = time.time()
        for l in open(args.dataset):
            keys.append(l)
            values.append(l)
            if (index < args.data_size):
                structure.insert(l)
            index += 1
        end = time.time()
        print("add_time:" + str(end-start))
        # search the keys above
        start = time.time()
        for key in keys:
            structure.find(key)
        end = time.time()
        print("search_keys:" + str(end-start))
        # search nonexisting keys
        start = time.time()
        for key in keys:
            structure.find(key + '_nonexistant')
        end = time.time()
        print("search_nonexistant_keys:" + str(end-start))
        sys.exit(0)
    else:
        print("data structure not recognized!")
        sys.exit(1)
    print("Unknown error! Exiting!")
    sys.exit(2)

if __name__ == '__main__':
    main()
