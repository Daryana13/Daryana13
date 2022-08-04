# #Парадигмы ООП Абстракция объект характер.свойствами, которые отличают его
# #Инкопсуляия -согласно которому сложность реализаии программного компонента должна
# # быть спрятана за его интрефейсом
# # Наследование -способ создания нового класса на основе уже существующего,
# # при котором класс-потомок заимствует своства и методы родительского класса и
# # также добавляет обстенные
# #Полиморфизм-поддержка нескольких реализаи на основе интерфейса
# # class Human:   # Класс
# #     pass
# # my_human = Human    #экземпляр класса
# # print(dir(Human))   #Список атрибут можно получить командой dir
#
# # class Human:
# #
# #
# #
# #     def __init__(self, name, age):
# #         self.name = name      #
# #         self.age = age
# #     def walk(self, km):
# #         if km > 5:
# #             return f'Я не могу пройти {km} км'
# #         else:
# #             return f'Я могу пройти {km} км'
# # my_human = Human('Darya', 33)
# # km = int(input('Введите км: '))
# # print(my_human.walk(km))
# # print(my_human.name)
# # print(dir(my_human))
# # print(my_human.age)
#
# class Car:
#     default_color = "Green"    #Статические поля(переменные класса
#     default_weight = 5000
#
#     def __init__(self, color, model):    #Динамические поля
#         self.color = color
#         self.model = model
#
#     def turn_on(self):
#         pass
# my_car = Car('red', 3000)
# my_car.color = input('Введите цвет')
# print(my_car.model)
# print(my_car.color)
# #self - ссылка на текущий экземпляр класса
#
#
# #Метды ООП
# #Методы экземпляра класса доступны только после создания экземпляра,чтобы вызвать такой метод,
# # нужно обратится к экземпляру
# #Статический метод -это обычные функции, которые помещены в класс для удобства и
# # распологается в области видимости этого класса,
# # чаще всего это вспомогательный код. чтобы создать статический метод, нужно обратится @staticmethod
# class Phone():
#     @staticmethod
#     def model_hash(model):
#         if model == 'I785':
#             return 34565
#         elif model =='K498':
#             return 45567
#         else:
#             return None
# Phone.model_hash('I785')
# my_phone Phone('red', 'I785')
# my_phone.chek_sim('MTS')
# print(Phone.model_hash('I785'))

#Родительский класс
class Phone:
    #Инииализатор
    def __init__(self):
        self.is_on = False

        #Включаем телефон
    def turn_on(self):
        self.is_on = True

        #Если телефон включен, делаем звонок
    def call(self):
        if self.is_on:
            print('Making call...')
        #Уноаследованный класс
class MobilePhone(Phone):
    #добавляем новое свойство battery
    def __init__(self):
        super().__init__()
        self.battery = 0

    #заряжаем телефон на велечину переданного значения
    def charge(self, num):
        self.battery = num
        print(f'Chargign battery up to ... {self.battery}%')
my_mobile_phone = MobilePhone()
my_mobile_phone.charge(70)
print(dir(my_mobile_phone))

