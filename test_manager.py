import unittest
import os
from tasky.manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_tasks.json"
        self.manager = TaskManager(storage_file=self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_task(self):
        task = self.manager.add_task("Test task")
        self.assertEqual(task.description, "Test task")
        self.assertEqual(len(self.manager.list_tasks()), 1)

    def test_complete_task(self):
        task = self.manager.add_task("Test task")
        self.manager.complete_task(task.id)
        self.assertTrue(self.manager.list_tasks()[0].completed)

    def test_delete_task(self):
        task = self.manager.add_task("Test task")
        self.manager.delete_task(task.id)
        self.assertEqual(len(self.manager.list_tasks()), 0)

    def test_persistence(self):
        self.manager.add_task("Persistent task")
        new_manager = TaskManager(storage_file=self.test_file)
        self.assertEqual(len(new_manager.list_tasks()), 1)
        self.assertEqual(new_manager.list_tasks()[0].description, "Persistent task")

if __name__ == "__main__":
    unittest.main()
