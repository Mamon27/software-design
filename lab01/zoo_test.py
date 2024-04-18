import unittest
from unittest.mock import MagicMock
from animal_manager import AnimalManager

class TestAnimalManager(unittest.TestCase):
    def test_add_animal(self):
        animals = []
        manager = AnimalManager(None, animals)
        
        manager.animal_window = MagicMock()
        
        manager.add_animal_entry = MagicMock()
        manager.species_var = MagicMock()
        
        manager.add_animal_entry.get.return_value = "Лев"
        manager.species_var.get.return_value = "Хижаки"
        
        manager.confirm_add_animal()
        
        self.assertEqual(len(animals), 1)

if __name__ == '__main__':
    unittest.main()
