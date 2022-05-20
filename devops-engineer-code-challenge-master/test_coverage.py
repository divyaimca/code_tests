import unittest
from unittest import result
import log_parser

class TestMain(unittest.TestCase):
    def test_valid_date(self):
        arg = '01/Jan/2021' 
        result = log_parser.valid_day(arg)
        self.assertTrue(result)

    def test_inalid_date(self):
        arg = '01/Foo/2021' 
        result = log_parser.valid_day(arg)
        self.assertFalse(result)

    def test_inalid_date1(self):
        arg = '0/Mar/2021' 
        result = log_parser.valid_day(arg)
        self.assertFalse(result)    

    def test_None_date(self):
        arg = None 
        result = log_parser.valid_day(arg)
        self.assertFalse(result)

    def test_Null_date(self):
        arg = '' 
        result = log_parser.valid_day(arg)
        self.assertFalse(result)

    def test_valid_log_file(self):
        arg = 'sample.log'
        result = log_parser.read_log_file(arg)[0]
        self.assertTrue(result)

    def test_invalid_log_file(self):
        arg = 'sampleeee.logg'
        result = log_parser.read_log_file(arg)[1]
        self.assertIsInstance(result, FileNotFoundError)

    def test_request_count(self):
        arg = [log_parser.read_log_file('sample.log'), '01/Dec/2011']
        result = log_parser.number_of_requests(arg[0][1], arg[1])    
        self.assertEqual(result, 2822)

    def test_get_post_ratio(self):
        arg = [log_parser.read_log_file('sample.log'), '01/Dec/2011']
        result = log_parser.get_post_ratio(arg[0][1], arg[1])
        self.assertEqual(result, '960.53%') 

    def test_top_3_user_agents(self):
        arg = [log_parser.read_log_file('sample.log'), '02/Dec/2011']
        result = log_parser.most_frequent_user_agents(arg[0][1], arg[1])
        self.assertListEqual(result, ['Mozilla/5.0', 'Mozilla/4.0', 'WordPress/3.2.1']) 

    def test_top_3_user_agents_in(self):
        arg = [log_parser.read_log_file('sample.log'), '01/Dec/2011']
        result = log_parser.most_frequent_user_agents(arg[0][1], arg[1])
        self.assertIn('Mozilla/5.0', result)

    def test_main_log_parser_requests(self):
        log_file_1, date, action = 'sample.log', '03/Dec/2011', 'number_of_requests'
        result = log_parser.main(log_file_1, date, action)
        self.assertEqual(result, 604)     

    def test_main_log_parser_user_agents(self):
        log_file_1, date, action = 'sample.log', '01/Dec/2011', 'most_frequent_user_agents'
        result = log_parser.main(log_file_1, date, action)
        self.assertListEqual(result, ['Mozilla/5.0', 'Mozilla/4.0', 'WordPress/3.2.1']) 

    def test_main_log_parser_ratio(self):
        log_file_1, date, action = 'sample.log', '02/Dec/2011', 'get_post_ratio'
        result = log_parser.main(log_file_1, date, action)
        self.assertEqual(result, '828.99%')

    def test_main_log_parser_none(self):
        log_file_1, date, action = 'sample.log', '02/Dec/2011', ''
        result = log_parser.main(log_file_1, date, action)
        self.assertEqual(result, (['Mozilla/5.0', 'Mozilla/4.0', 'WordPress/3.2.1'], '828.99%', 2572)) 

    def test_main_log_parser_all(self):
        log_file_1, date, action = 'sample.log', '03/Dec/2011', 'all'
        result = log_parser.main(log_file_1, date, action)
        self.assertEqual(result, (['Mozilla/5.0', 'Mozilla/4.0', 'WordPress/3.2.1'], '812.12%', 604))                    








unittest.main()