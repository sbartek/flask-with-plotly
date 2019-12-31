import os

import numpy as np
import pandas as pd

class BrownianDataGenerator:

    def __init__(self, size, scale):
        self.size = size
        self.scale = scale

    def generate(self):
        sequence = np.random.normal(loc=0.0, scale=self.scale, size=self.size)
        return np.cumsum(sequence)
        
        
class SequenceWriter:

    def __init__(self, index_col_name, value_col_name):
        self.index_col_name = index_col_name
        self.value_col_name = value_col_name

    def write(self, sequence, output_fn):
        
        data_record = []
        for i in range(len(sequence)):
            data_record.append(
                f"{{\"{self.index_col_name}\":{i}," +
                f"\"{self.value_col_name}\":{sequence[i]}}}")

        json_string = "[" + ",".join(data_record) + "]"
        with open(output_fn, 'w') as f:
            f.write(json_string)

class DataWriter:

    def __init__(
            self,
            data_size,
            scale,
            index_col_name,
            value_col_name):

        self.data_generator = BrownianDataGenerator(data_size, scale)
        self.sequence_writer = SequenceWriter(index_col_name, value_col_name)

    def generate_and_write(self, output_fn):
        sequence = self.data_generator.generate()
        self.sequence_writer.write(sequence, output_fn)

class DataReader:

    def data_frame(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"File {path} does not exist!")
        return pd.read_json(path, orient='records')
        
