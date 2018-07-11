import unittest, sys
import pdb
sys.path.insert(0, '..')
from part_1_ctes import *
from part_2_ctes import *
from sql_runner import SQLRunner


class TestCTEs(unittest.TestCase):

    def test_use_cte_to_determine_average_sale(self):
        sql_runner = SQLRunner()
        cursor = sql_runner.execute_seed_file()

        def test_range(result, val1, val2):
            if val1 < result < val2:
                return True
            else:
                return False

        pdb.set_trace()
        result = cursor.execute(use_cte_to_determine_average_sale()).fetchall()[0][0]
        self.assertTrue(test_range(result, 57.2, 57.3))

        def test_cte_name(fn):
            query_str = fn()
            if "average_sales" in query_str:
                return True
            else:
                return False
        self.assertTrue(test_cte_name(use_cte_to_determine_average_sale), "CTE should be called 'average_sales'")

    def test_select_all_above_average_sales(self):
        sql_runner = SQLRunner()
        cursor = sql_runner.execute_seed_file()

        result = [(3, 3, '2018-04-22', 1, 60), (7, 7, '2018-04-23', 1, 80), (8, 8, '2018-04-21', 2, 90), (9, 9, '2018-04-22', 2, 80), (10, 10, '2018-04-22', 2, 80), (11, 11, '2018-04-22', 2, 70), (12, 12, '2018-04-23', 2, 90), (13, 13, '2018-04-23', 2, 80), (24, 24, '2018-04-21', 5, 100), (26, 26, '2018-04-22', 5, 75), (28, 8, '2018-04-21', 2, 90), (29, 8, '2018-04-21', 2, 90), (30, 8, '2018-04-21', 2, 90), (32, 24, '2018-04-21', 5, 100), (33, 24, '2018-04-21', 5, 100), (34, 24, '2018-04-21', 5, 100)]
        self.assertEqual(cursor.execute(select_all_above_average_sales()).fetchall(), result)

        def test_cte_name(fn):
            query_str = fn()
            if "average_sales" in query_str:
                return True
            else:
                return False
        self.assertTrue(test_cte_name(use_cte_to_determine_average_sale), "CTE should be called 'average_sales'")

    def test_cte_deletes_duplicates(self):
        sql_runner = SQLRunner()
        cursor = sql_runner.execute_seed_file()
        cursor = sql_runner.execute_cte_deletes_duplicates()

        result = [(27,)]
        self.assertEqual(cursor.execute("SELECT COUNT(*) FROM sales;").fetchall(), result)

    def test_correct_above_avg_sales(self):
        sql_runner = SQLRunner()
        cursor = sql_runner.execute_seed_file()
        cursor = sql_runner.execute_cte_deletes_duplicates()
        result = [('Manhattan', '2018-04-22', 60), ('Manhattan', '2018-04-23', 80), ('Brooklyn', '2018-04-21', 90), ('Brooklyn', '2018-04-22', 80), ('Brooklyn', '2018-04-22', 80), ('Brooklyn', '2018-04-22', 70), ('Brooklyn', '2018-04-23', 90), ('Brooklyn', '2018-04-23', 80), ('London', '2018-04-21', 100), ('London', '2018-04-22', 75)]
        self.assertEqual(cursor.execute(correct_above_avg_sales()).fetchall(), result)
