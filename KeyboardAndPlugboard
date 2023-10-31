# создаем класс приема и вывода информации, чтобы больше не беспокоиться о том, чтобы делать цифры буквами и наоборот

class KeyPlugBoard:
    # при инициализации класса опциональным аргументом принимаем коммутаторы в количестве,
    # которое мы ограничим уже в пользовательском интерфейсе, чтобы не загромождать класс ввода-вывода
    def __init__(self, *commutators):
        # задаем два ключа для реализации коммутаторов:
        # первый - референсный (исходный алфавит), второй - для изменений
        self.reference_key = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        self.commutator_key = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        # провряем, нужно ли вносить изменения
        if commutators:
            for pair in commutators:
                pair = sorted(pair.split('-'))
                # коммутаторы должны иметь вид "БУКВА1-БУКВА2", где 1 и 2 - буквы, заменяемые друг другом
                index_one = self.reference_key.find(pair[0])
                index_two = self.reference_key.find(pair[1])
                self.commutator_key = self.commutator_key[:index_one] + pair[1] + self.commutator_key[index_one +
                    1:index_two] + pair[0] + self.commutator_key[index_two + 1:]
                # собираем измененный ключ с помощью срезов

    def inp(self, letter):
        return 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'.find(letter.upper())

    def outp(self, index):
        return 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'[index]
