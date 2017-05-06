import unittest
def shaiba(x, y, dx, dy):
    if x + dx < 100 and y + dy < 100:
        x = x + dx
        y = y + dy
    if x + dx > 100 and y + dy < 100:
        x = x - dx
        y = y + dy
    if y + dy > 100:
        x = x - dx
        y = y - dy
    if x - dx < 0:
        x = x + dx
        y = y - dy
    if y - dy < 0:
        x = x + dx
        y = y + dy
    if y + dy > 100 and y - dy < 0: # В случае если скорость DY сильно больше коррдинаты y и при сложении и при вычитании, например Y=20, а DY = 90 (на самом деле DY от 80 уже поставит нас с транное положение) получается, что шайба выходит за границу поля и в случае умножения и в случае вычитания. Вопроса два - правильно ли я ставлю условие в коде, если да, то могу ли я оставить Y без изменений, но меняя X, такое решение нормально?
        y = y
        x = x + dx
    if x + dx > 100 and x - dx < 0: # То же условие я делаю для X и DX
        x = x
        y = y + dy
    return x, y

#2) Вопрос про тестирование. Я пишу такой тест:

class TestShaiba(unittest.TestCase):
    def test_next_shaiba_calculated_plus_speed(self): 
        self.assertEqual(list(next_shaiba(81, 20, 5, 3)), [86, 23, 5, 3])
