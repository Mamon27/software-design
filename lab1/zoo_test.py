import unittest
from unittest.mock import patch
import tkinter as tk
from zoo_app import ZooApp, DataEntryDialog

class TestZooApp(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()

    @patch("tkinter.simpledialog.askstring", return_value="Test Worker")
    def test_add_worker_to_listbox(self, mock_askstring):
        app = ZooApp(self.root)
        
        # Перед тестуванням додамо тестового співробітника в `listbox_workers`
        app.listbox_workers.insert(tk.END, "Test Worker - Option1")
        app.add_worker()

        # Перевіряємо, чи правильно додано співробітника
        self.assertIn("Test Worker", str(app.listbox_workers.get(0)))

    def tearDown(self):
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()
