rkeys = 'ABCDEF_0', 'FEABCD_0', 'DCABFE_1', 'FEBACD_2', 'DCFEBA_3', 'EFABDC_4'
ltn = 'ABCDEF'
# тут будут храниться ключи и алфавит соответственно


class Rotor:
    # прописываем инициализацию класса
    def __init__(self, key):
        # задаем по номеру: референсый ключ, ключ шифровки, сдвиг, при котором вращается следующий ротор
        self.reference_key = ltn
        self.sipher_key = rkeys[key].split('_')[0]
        self.notch = rkeys[key].split('_')[1]
        # предотвращаем ошибку слишком большого сдвига

    # делаем метод для движения ротора
    def move(self, shift=1):
        # реализуем сдвиг на 1 позицию, при переходе лимита
        if shift >= len(self.sipher_key):
            shift = shift % len(self.sipher_key)
        # совершаем сдвиг
        self.reference_key = self.reference_key[shift:] + self.reference_key[:shift]
        self.sipher_key = self.sipher_key[shift:] + self.sipher_key[:shift]
        # для последующего сдвига роторов далее
        if self.reference_key[0] == ltn[int(self.notch)]:
            return True

    # создаем фунцкии для шифровки в 2 стороны
    def pass_forward(self, letter_index):
        return self.sipher_key.find(self.reference_key[letter_index])

    def pass_backward(self, letter_index):
        return self.reference_key.find(self.sipher_key[letter_index])
