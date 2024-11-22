class MyClass(TypedDict):
    name: ReadOnly[str]
    elephants: int

x = MyClass(name='Hannibal', elephants=38)
x.name = 'Scipio'
