#!/usr/bin/env python

from pathlib import Path
import argparse

from data_generator import DataWriter
from config_parser import parse_default_config

def create_dirs(path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    
def generate_data(**kwargs):
    config = parse_default_config(kwargs['config_fn'])
    data_path = config.get("data_path")
    new_data_path = kwargs.get("data_path")
    if new_data_path:
        data_path = new_data_path
    data_size = config.get("data_size")
    scale = config.get("scale")
    index_col_name = config.get("index_col_name")
    value_col_name = config.get("value_col_name")

    data_writer = DataWriter(data_size, scale, index_col_name, value_col_name)
    create_dirs(data_path)
    print('writing to: ', data_path)
    data_writer.generate_and_write(data_path)

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config_fn",
        default="config/generator_config.yaml",
        type=str)
    parser.add_argument("--data_path", type=str)
    return parser.parse_args()
    
def main():
    args = parse_arguments()
    generate_data(**vars(args))
    
if __name__ == '__main__':
    main()

