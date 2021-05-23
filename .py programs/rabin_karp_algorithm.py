import unittest

def rabin_karp(text, pattern):
    """
    Поиск всех вхождений алгоритмом Рабина-Карпа

    Параметры:
    ----------
        text: str
            текст
        pattern: str
            образец

    Возвращаемое значение
    ---------------------
        список позиций в тексте, с которых начинаются вхождения образца
    """
    result = []

    # Менять отсюда =) ---- vvvvv ----

    pass 
    if (text != ''):
        summ = 0
        summ_req = 0
        count = 0

        for i in range (0, len(pattern)):
            summ += ord(text[i])
            summ_req += ord(pattern[i])

        #if summ == summ_req:
            #if text.startswith(pattern):
             #   count+=1
               # print ('Символ, на котором начинаетс включение, стоит под номером 0')"

        for i in range (len(pattern), len(text)):
            #print(summ)
            #print(summ_req)
            if summ == summ_req:
                if text[i-len(pattern):].startswith(pattern):
                    #count+=1
                    #print ('Символ, на котором начинается включение, стоит под номером ',i-len(pattern))
                    k = i-len(pattern)
                    result.append(k)
                    
       
                   

            summ -= ord(text[i - len(pattern)])
            summ += ord(text[i])
        if (text[len(text)-len(pattern):].startswith(pattern)) and (pattern != ''):
                    #count+=1
                    #print ('Символ, на котором начинается включение, стоит под номером ',i-len(pattern))
                    k = len(text)-len(pattern)
                    result.append(k)



       
    #return count

    # Менять до сюда =) ---- ^^^^^ ----
    return result


class RabinKarpTest(unittest.TestCase):
    """Тесты для метода Рабина-Карпа"""

    def setUp(self):
        """Инициализация"""
        self.text1 = 'аxaxaxax'
        self.pattern1 = 'xax'
        self.text2 = 'bababab'
        self.pattern2 = 'bab'

    def test_return_type(self):
        """Проверка того, что функция возвращает список"""
        self.assertIsInstance(
            rabin_karp(self.text1, "x"), list,
            msg="Функция должна возвращать список"
        )

    def test_returns_empty(self):
        """Проверка того, что функция, когда следует, возвращает пустой список"""
        self.assertEqual(
            [], rabin_karp(self.text1, "z"),
            msg="Функция должна возвращать пустой список, если нет вхождений"
        )
        self.assertEqual(
            [], rabin_karp("", self.pattern1),
            msg="Функция должна возвращать пустой список, если текст пустой"
        )
        self.assertEqual(
            [], rabin_karp("", ""),
            msg="Функция должна возвращать пустой список, если текст пустой, даже если образец пустой"
        )

    def test_finds(self):
        """Проверка того, что функция ищет все вхождения непустых образцов"""
        self.assertEqual(
            [1, 3, 5], rabin_karp(self.text1, self.pattern1),
            msg="Функция должна искать все вхождения"
        )
        self.assertEqual(
            [0, 2, 4], rabin_karp(self.text2, self.pattern2),
            msg="Функция должна искать все вхождения"
        )

    def test_finds_all_empties(self):
        """Проверка того, что функция ищет все вхождения пустого образца"""
        self.assertEqual(
            list(range(len(self.text1))), rabin_karp(self.text1, ""),
            msg="Пустая строка должна находиться везде"
        )

# Должно выдать:
# --------------
# Ran ... tests in ...s
# OK

# Запуск тестов
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

    input()
