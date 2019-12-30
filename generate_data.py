#!/usr/bin/env python

import argparse

from data_generator import DataWriter

from config import DATA_PATH, DATA_SIZE, SCALE, INDEX_COL_NAME, VALUE_COL_NAME

def generate_data(data_path, data_size, scale, index_col_name, value_col_name):
    data_writer = DataWriter(data_size, scale, index_col_name, value_col_name)
    data_writer.generate_and_write(data_path)

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", default=DATA_PATH, type=str)
    parser.add_argument("--data_size", default=DATA_SIZE, type=int)
    parser.add_argument("--scale", default=SCALE, type=int)
    parser.add_argument("--index_col_name", default=INDEX_COL_NAME, type=str)
    parser.add_argument("--value_col_name", default=VALUE_COL_NAME, type=str)
    return parser.parse_args()
    
def main():
    args = parse_arguments()
    generate_data(**vars(args))
    
if __name__ == '__main__':
    main()

