class Listlnstance:
    """
    Примесный класс, реализующий получение форматированной строки при вызове
    функций print() и str() с экземпляром в виде аргумента, через наследование
    метода str, реализованного здесь.
    Отображает только атрибуты экземпляра.
    self - экземпляр самого нижнего класса в дереве наследования.
    Во избежание конфликтов с именами атрибутов клиентских классов использует
    имена вида __Х.
    """
    def __str__(self):
        self.__visited = {}
        return '<Instance of {0}, address {1}:\n{2}{3}>'.format(
            self.__class__.__name__ , # Имя клиентского класса
            id(self),                 # Адрес экземпляра
            self.__attrnames(self, 0),
            self.__listclass(self.__class__, 4))

    def __listclass(self, aClass, indent):
        dots = "." * indent
        if aClass in self.__visited:
            return '\n{0}<Class {1}:, address {2}: (see above)>\n'.format(
                dots,
                aClass.__name__,
                id(aClass))
        else:
            self.__visited[aClass] = True
            genabove = (self.__listclass(c, indent+4) for c in aClass.__bases__)
            return '\n{0}<Class {1}, address {2}.\n{3}{4}{5}>\n'.format(
                dots,
                aClass.__name__,
                id(aClass),
                self.__attrnames(aClass, indent),
                ''.join(genabove),
                dots)

    def __attrnames(self, obj, indent):
        spaces = ' ' * (indent + 4)
        result =''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + '{0}=<>\n'.format(attr)
            else:
                result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))
        return result


if __name__ == "__main__":
    class Spam(Listlnstance):
        def __init__(self):
            self.data1 = 'food'
            self.data2 = 'meat'

    x= Spam()
    print(x)