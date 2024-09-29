from tests_12_4 import Runner
import unittest
import logging


class TestRunner(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            boy = Runner('boy', -5)
            for _ in range(1, 11):
                boy.walk()
            self.assertEqual(boy.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            return logging.warning(f'Неверная скорость для {Runner.__name__}', exc_info=True)
            
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            logging.info('"test_run" выполнен успешно')
            men = Runner(777)
            for _ in range(1, 11):
                men.run()
            self.assertEqual(men.distance, 100)  # FAILED (failures=1) 101 != 100
        except TypeError:
            return logging.warning('Неверный тип данных для объекта Runner', exc_info=True)
            
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        child = Runner('child')
        runner = Runner('runner')
        for _ in range(1, 11):
            child.walk()
            runner.run()
        self.assertNotEqual(child.distance, runner.distance)



