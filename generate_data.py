from data_generator import DataWriter

from config import DATA_PATH, DATA_SIZE, SCALE, INDEX_COL_NAME, VALUE_COL_NAME


def generate_data():
    data_writer = DataWriter(
        size=DATA_SIZE,
        scale=SCALE,
        index_col_name=INDEX_COL_NAME,
        value_col_name=VALUE_COL_NAME)
    data_writer.generate_and_write(DATA_PATH)

if __name__ == '__main__':
    generate_data()

