import unittest
from unittest.mock import MagicMock
from animal_manager import AnimalManager

class TestAnimalManager(unittest.TestCase):
    def test_add_animal(self):
        animals = []
        manager = AnimalManager(None, animals)
        
        # Создаем заглушку для атрибута animal_window
        manager.animal_window = MagicMock()
        
        # Создаем поддельные объекты для add_animal_entry и species_var
        manager.add_animal_entry = MagicMock()
        manager.species_var = MagicMock()
        
        # Задаем значения, которые будут возвращать методы get() этих объектов
        manager.add_animal_entry.get.return_value = "Лев"
        manager.species_var.get.return_value = "Хижаки"
        
        # Добавляем животное
        manager.confirm_add_animal()
        
        # Проверяем, что список animals содержит одно животное
        self.assertEqual(len(animals), 1)

if __name__ == '__main__':
    unittest.main()
