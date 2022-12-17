class Person:
  def __init__(object, name, age, money):
    object.name = name
    object.age = format(age)
    object.money = money

  def myfunc(abc):
    print("Hello my name is " + abc.name)
  
  def myfunc2(self):
    print("and mi olders " + self.age)

  def myfunc3(self):
    print("so i need money  " + format(self.money) + "$")


p1 = Person("John", 36, 1000000000)
p1.myfunc()
p1.myfunc2()
p1.myfunc3()
#Пока что не работает, как кокатенировать не пойму цифры и буквы(str & int)
#пишут что можно сделать с помощью format()  но пока фиг его знает
# change numbers-int on numbers-str
# add format for age