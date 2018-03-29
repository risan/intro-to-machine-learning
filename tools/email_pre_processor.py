import os
import pickle

def data_path(path):
    dirname = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.abspath(os.path.join(dirname, "../data"))

    return os.path.join(data_dir, path)

def pre_process_email(authors_file = data_path("email/authors.pkl")):
    # Deserializing the authors Python objects (unpickling).
    authors_file_handler = open(authors_file, "r")
    authors = pickle.load(authors_file_handler)
    authors_file_handler.close()
