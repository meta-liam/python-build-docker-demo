# test_str.py
import unittest
import my_work

class TestDownCsvMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_work(self):
        rs =my_work.get_report_task({"start": "2022-04-01", "stop":"2022-04-15"})
        print(rs)

if __name__ == '__main__':
    unittest.main()

# python test_save_db.py