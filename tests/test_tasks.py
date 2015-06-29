from unittest import TestCase

from main import add_task, tasks


class TestTasks(TestCase):

    def test_add_tasks(self):
        add_task('01.01.2015', 'Make coffee')
        self.assertEqual(tasks, [['01.01.2015', 'Make coffee']])


