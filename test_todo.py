import unittest
import todoo as op

class Testtodo(unittest.TestCase):

    def setUp(self):
        op.tasks = []

    def test_add(self):
        self.assertEqual(op.add_task('hello'),'hello')
        self.assertEqual(op.add_task('work'),'work')

    def test_view1(self):
        op.add_task('hello')
        op.add_task('work')
        self.assertEqual(op.view_task(),['hello', 'work'])

    def test_remove(self):
        op.add_task('hello')
        op.add_task('work')
        self.assertEqual(op.remove_task(),'hello')
        self.assertEqual(op.remove_task(),'work')

    def test_view(self):
        self.assertEqual(op.view_task(),['hello','work'])
