#!/usr/bin/env python3

import username_generator
import unittest


class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    # number of usernames

    def test_default_6_usernames(self):
        args = {'num': 6, 'underscores': False, 'no_print': True, 'fname': '',
                'max_size': 255, 'min_size': 0, 'indentation': 0,
                'no_intro': True, 'return_val': True}
        uname = username_generator.main(args=args)
        self.assertEqual(len(uname), 6)

    def test_1_usernames(self):
        args = {'num': 1, 'underscores': False, 'no_print': True, 'fname': '',
                'max_size': 255, 'min_size': 0, 'indentation': 0,
                'no_intro': True, 'return_val': True}
        uname = username_generator.main(args=args)
        self.assertEqual(len(uname), 1)

    def test_100_usernames(self):
        args = {'num': 100, 'underscores': False, 'no_print': True, 'fname': '',
                'max_size': 255, 'min_size': 0, 'indentation': 0,
                'no_intro': True, 'return_val': True}
        uname = username_generator.main(args=args)
        self.assertEqual(len(uname), 100)

    # camelcase / underscores

    def test_camelcase_usernames_have_no_underscores(self):
        args = {'num': 10, 'underscores': False, 'no_print': True, 'fname': '',
                'max_size': 255, 'min_size': 0, 'indentation': 0,
                'no_intro': True, 'return_val': True}
        unames = username_generator.main(args=args)
        n_underscores = sum(uname.count("_") for uname in unames)
        self.assertEqual(n_underscores, 0)

    def test_camelcase_usernames_have_two_capital_letters(self):
        args = {'num': 10, 'underscores': False, 'no_print': True, 'fname': '',
                'max_size': 255, 'min_size': 0, 'indentation': 0,
                'no_intro': True, 'return_val': True}
        unames = username_generator.main(args=args)
        n_caps = sum(sum(1 for char in un if char.isupper()) for un in unames)
        self.assertEqual(n_caps, 20)

    def test_underscore_usernames_have_underscore(self):
        args = {'num': 10, 'underscores': True, 'no_print': True, 'fname': '',
                'max_size': 255, 'min_size': 0, 'indentation': 0,
                'no_intro': True, 'return_val': True}
        unames = username_generator.main(args=args)
        n_underscores = sum(uname.count("_") for uname in unames)
        self.assertEqual(n_underscores, 10)

    def test_underscore_usernames_have_no_capital_letters(self):
        args = {'num': 10, 'underscores': True, 'no_print': True, 'fname': '',
                'max_size': 255, 'min_size': 0, 'indentation': 0,
                'no_intro': True, 'return_val': True}
        unames = username_generator.main(args=args)
        n_caps = sum(sum(1 for char in un if char.isupper()) for un in unames)
        self.assertEqual(n_caps, 0)

    # size

    def test_words_greater_than_7(self):
        args = {'num': 10, 'underscores': False, 'no_print': True, 'fname': '',
                'max_size': 255, 'min_size': 7, 'indentation': 0,
                'no_intro': True, 'return_val': True}
        unames = username_generator.main(args=args)
        max_size = len(max(unames))
        self.assertEqual(max_size >= 7, True)

    def test_words_greater_than_7(self):
        args = {'num': 10, 'underscores': False, 'no_print': True, 'fname': '',
                'max_size': 255, 'min_size': 7, 'indentation': 0,
                'no_intro': True, 'return_val': True}
        unames = username_generator.main(args=args)
        max_size = len(max(unames))
        self.assertEqual(max_size >= 7, True)

    def test_words_less_than_14(self):
        args = {'num': 10, 'underscores': False, 'no_print': True, 'fname': '',
                'max_size': 14, 'min_size': 0, 'indentation': 0,
                'no_intro': True, 'return_val': True}
        unames = username_generator.main(args=args)
        max_size = len(max(unames))
        self.assertEqual(max_size <= 14, True)

    # indentation

    def test_default_formatting_4_spaces_start(self):
        args = {'num': 10, 'underscores': False, 'no_print': True, 'fname': '',
                'max_size': 14, 'min_size': 0, 'indentation': 4,
                'no_intro': True, 'return_val': True}
        unames = username_generator.main(args=args)
        valid_start_spaces = all(uname.startswith(" " * 4) for uname in unames)
        self.assertEqual(valid_start_spaces, True)

    def test_default_formatting_4_spaces_start(self):
        args = {'num': 10, 'underscores': False, 'no_print': True, 'fname': '',
                'max_size': 14, 'min_size': 0, 'indentation': 4,
                'no_intro': True, 'return_val': True}
        unames = username_generator.main(args=args)
        n_spaces = sum(uname.count(" ") for uname in unames)
        self.assertEqual(n_spaces, 40)

    def test_indentation_no_spaces(self):
        args = {'num': 10, 'underscores': False, 'no_print': True, 'fname': '',
                'max_size': 14, 'min_size': 0, 'indentation': 0,
                'no_intro': True, 'return_val': True}
        unames = username_generator.main(args=args)
        n_spaces = sum(uname.count(" ") for uname in unames)
        self.assertEqual(n_spaces, 0)

    # excpetions

    def test_except_number_of_usernames_greater_than_10000(self):
        args = {'num': 10001, 'underscores': False, 'no_print': True,
                'fname': '', 'max_size': 255, 'min_size': 0, 'indentation': 0,
                'no_intro': True, 'return_val': True}
        self.assertRaises(ValueError, username_generator.check_arguments, args)

    def test_except_min_size_greater_than_max(self):
        args = {'num': 10, 'underscores': False, 'no_print': True, 'fname': '',
                'max_size': 0, 'min_size': 14, 'indentation': 0,
                'no_intro': True, 'return_val': True}
        self.assertRaises(ValueError, username_generator.check_arguments, args)

    def test_exception_min_size_greater_than_14(self):
        args = {'num': 10, 'underscores': False, 'no_print': True, 'fname': '',
                'max_size': 255, 'min_size': 15, 'indentation': 0,
                'no_intro': True, 'return_val': True}
        self.assertRaises(ValueError, username_generator.check_arguments, args)

    def test_exception_max_size_less_than_8(self):
        args = {'num': 10, 'underscores': False, 'no_print': True, 'fname': '',
                'max_size': 7, 'min_size': 0, 'indentation': 0,
                'no_intro': True, 'return_val': True}
        self.assertRaises(ValueError, username_generator.check_arguments, args)


if __name__ == '__main__':
    unittest.main()
