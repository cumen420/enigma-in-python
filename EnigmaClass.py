from ROTORCLASS import Rotor
from KEYBOARDCLASS import Keyboard
from REFLECTORCLASS import Reflector


class Enigma:
    # прописываем инициализацию
    def __init__(self, left_rotor, middle_rotor, right_rotor, reflector, *commutators):
        # роторы должны представлять собой объекты класса Rotor
        # роторы пакуются в список, чтобы допустить замену единственного ротора в ходе работы
        # без перезадачи переменной
        self.rotors = [left_rotor, middle_rotor, right_rotor]
        # рефлектор представляет собой объект класса Reflector
        self.reflector = reflector
        # коммутаторы опциональны, пакуются, запоминаются, тоже в список
        self.commutators = commutators
        self.shift = [0, 0, 0]
        self.boards = Keyboard(self.commutators)

    # задаем возможность сменить сдвиг каждого ротора
    def set_shift(self, shift, rotor=0):
        self.rotors[rotor].move(shift, move_adjacent=False)
        self.shift[rotor] = shift
        # в этом методе не предусмотрено взаимодействие роторов, он создан для настройки исходного положения

    # задаем возможность сменить ротор
    def set_rotor(self, rotor, position=0):
        self.rotors[position] = rotor

    # задаем возможность сменить коммутаторы
    def add_commutators(self, *commutators):
        if commutators:
            commutators = list(commutators)
        if self.commutators:
            self.commutators = list(self.commutators)
        # проверяем, есть ли такие коммутаторы в списке и добавляем по надобности
        for commutator in commutators:
            if commutator not in self.commutators:
                self.commutators.append(commutator)
        self.boards = Keyboard(self.commutators)
        # обновляем клавиатуру и панель коммутаторов

    # делаем шифровку до рефлектора
    def keyboard_to_reflector(self, letter_index):
        # проводим через роторы
        for n in range(2, -1, -1):
            letter_index = self.rotors[n].pass_forward(letter_index)
        return letter_index

    def reflector_to_keyboard(self, letter_index):
        # см предыдущий, но наоборот
        for n in range(3):
            letter_index = self.rotors[n].pass_backward(letter_index)
        return letter_index

    # отражаем букву
    def reflect(self, letter_index):
        return self.reflector.reflect(letter_index)

    # собираем кусочки в 1 функцию
    def encode(self, letter):
        # переводим букву в индекс, проводим до рефлектора и назад от него
        letter = self.boards.inp(letter)
        letter = self.keyboard_to_reflector(letter)
        letter = self.reflect(letter)
        letter = self.reflector_to_keyboard(letter)
        # двигаем роторы
        if self.rotors[2].move():
            if self.rotors[1].move():
                self.rotors[0].move()
        # возвращаем букву по индексу
        letter = self.boards.outp(letter)
        return letter
