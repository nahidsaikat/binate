import unittest, os, shutil
from script import download


class TestUM(unittest.TestCase):

    def setUp(self):
        self.test_data_dirname = 'testdata'
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.test_data_path = os.path.join(dir_path, self.test_data_dirname)
        os.makedirs(self.test_data_path, exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self.test_data_path)

    def test_script(self):
        download('images.txt', self.test_data_path)
        path, dirs, files = next(os.walk(self.test_data_path))
        file_count = len(files)
        self.assertEqual(file_count, 5)
        self.assertEqual('image-1.jpg' in files, True)
        self.assertEqual('image-2.jpg' in files, True)
        self.assertEqual('image-3.jpg' in files, True)
        self.assertEqual('image-4.jpg' in files, True)
        self.assertEqual('image-5.jpg' in files, True)
 
if __name__ == '__main__':
    unittest.main()
