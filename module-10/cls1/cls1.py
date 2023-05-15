class Character:
    name = None
    x = None
    y = None
    hp = 100
    mp = 100


char_1 = Character()
char_2 = Character()
Character.hp = 300
Character.name = 'New Name'
char_1.name = 'Edelweiss'
char_2.name = 'Gabriel'
print(char_1.name)
print(char_2.name)
char_3 = Character()
char_3.name = '123'
print(Character.name)
print(char_3.name)
