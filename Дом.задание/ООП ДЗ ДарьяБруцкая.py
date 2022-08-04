class StrOrNumber:
    def __init__(self, a):
        self.a = a
        self.b = self.a.lower()
        self.c = self.b.replace(' ', '').replace(',', '')  # убираем пробелы или запятые
        self.sum1 = 0
        self.sum2 = 0
        self.l1 = []
        self.l2 = []


    def result(self):

        if self.c.isdigit():

            self.sum = sum(int(i) for i in self.b if int(i) % 2 == 0)
            self.mult = self.sum * my_input.len()

            return f"{self.sum} * {my_input.len()} = {self.mult}"

        elif self.c.isalpha():

            self.c = list(self.c)
            self.l1 = []
            self.l2 = []
            for i in self.c:
                if i in 'aeiouy':
                    self.sum1 += 1
                    self.l1.append(i)
                else:
                    self.sum2 += 1
                    self.l2.append(i)

            if self.sum1 * self.sum2 <= len(self.a):
                return ''.join(self.l1)
            else:
                return ''.join(self.l2)

    def len(self):
        return len(self.a)


my_input = StrOrNumber(input('Введите строку или число '))


print(my_input.a)
print('Длина', my_input.len())
print('Результат', my_input.result())