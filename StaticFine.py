'''Документация'''

import collections

class Hand():
    '''
        У рук свое название.
    '''
    def __init__(self,name, **kwargs) -> None:
        self.name = name
        self.fingers = {
            'forefinger' : Finger(kwargs['forefinger']), # Указательный палец
            'middle_finger' : Finger(kwargs['middle_finger']),
            'ring_finger' : Finger(kwargs['ring_finger']),
            'little_finger' : Finger(kwargs['little_finger']),
        }
'''
Как создавать пальцы для разных рук?

'''

class Finger():
    '''Один палец - это словарь из {клавиша:количество_нажатий}.
    Каждый палец имеет свою нагрузку.
    '''
    def __init__(self, keys_set) -> None:
        '''
        stress - нагрузка на палец
        '''
        self.stress = 0
        self.keys_set = keys_set

    def count_finger_stress(self):
        pass


class LeftHand(Hand):
    def __init__(self, name) -> None:
        '''
            Нагрузка на руку складывается из нагрузок для пальцев.
        '''
        super().__init__(
            name,
            forefinger={'4': 0, ';': 0, '5': 0, 'к': 0, 'а': 0, 'м': 0,
                    'е': 0, 'п': 0, 'и': 0},
            middle_finger={'3': 0, 'у': 0, 'в': 0, 'с': 0},
            ring_finger={'2': 0, 'ц': 0, 'ы': 0, 'ч': 0},
            little_finger= {'1': 0, '!': 0, 'й': 0, 'ф': 0, 'я': 0}
        )


class RightHand(Hand):
    def __init__(self, name) -> None:
        super().__init__(name,
            forefinger={'7': 0, '?': 0, ':': 0, '6': 0, 'г': 0, 'о': 0, 'ь': 0,
                    'н': 0, 'р': 0, 'т': 0},
            middle_finger={'8': 0, 'ш': 0, 'л': 0, 'б': 0},
            ring_finger={'9': 0, 'щ': 0, 'д': 0, 'ю': 0},
            little_finger= {'0': 0, 'з': 0, 'ж': 0, '.': 0, ',': 0}
        )

#Или можно сделать наследование от руки для правой и левой
def main():
    with open('text.txt', encoding='utf-8') as file:
        TEXT = file.read()
    
    left_hand = LeftHand('left')
    right_hand = RightHand('right')

    print(left_hand.fingers)


if __name__ == '__main__':
    main()



