import unittest
from sort_data import align_data, align_head

class Test_Sort_Data(unittest.TestCase):
    texts = [['andy', 'natasha', 'Ivan'], ['serhii', 'Dima', 'Dmytro'], ['Roman', 'Nazar', 'Pavlo']]
    align_head_result = [['  Name1   ', ' Name2  ', 'Name3 '], ['andy      ', 'natasha ', 'Ivan  '], ['serhii    ', 'Dima    ', 'Dmytro'], ['Roman     ', 'Nazar   ', 'Pavlo ']]
    align_data_result = [['andy      ', 'natasha ', 'Ivan  '], ['serhii    ', 'Dima    ', 'Dmytro'], ['Roman     ', 'Nazar   ', 'Pavlo ']]
    enter_size = [10, 8, 6]
    head = [['Name1', 'Name2', 'Name3']]

    def test_align_head(self):
        get_align_head = align_head(self.head, self.enter_size)
        self.assertEqual(get_align_head, self.align_head_result)


    def test_align_data(self):
        get_align_data = align_data(self.texts, self.enter_size)
        self.assertEqual(get_align_data, self.align_data_result)



unittest.main()
