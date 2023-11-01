refkeys = 'ABCDEF', 'CFAEDB', 'FEDCBA'

# делаем рефлектор заменимым на другие версии себя
class Reflector:
    def __init__(self, num=1):
        self.reflection_key = refkeys[num]

  # создаем функционал класса
    def reflect(self, letter_index):
        return self.reflection_key.find('ABCDEF'[letter_index])
