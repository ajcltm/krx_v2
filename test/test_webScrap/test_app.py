import unittest

from krx_v2.webScrap import app

import os
from pathlib import Path
import pickle

class TestApp(unittest.TestCase):

    def test_scrap(self):
        app.Scraper().execute()

        dir_ = Path.home().joinpath('Desktop', 'krx')
        ls = os.listdir(dir_)
        file_ = ls[0]

        file_dir = dir_.joinpath(file_)
        with open(file_dir, mode='rb') as fr:
            data = pickle.load(fr)

        print(data)

        

if __name__ == '__main__':
    unittest.main()