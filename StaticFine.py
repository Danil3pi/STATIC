'''Документация'''

import collections
def get_keys_dict(text: str) -> dict:
    '''Считываем символы в тексте.'''
    return collections.Counter(text)

def get_text(file_name: str) -> str:
    '''Получаем текст.'''
    with open(file_name, encoding='utf-8') as file:
        return file.read()

TEXT = get_text('text.txt')
KEYS_DICT = get_keys_dict(TEXT.lower())
print(KEYS_DICT)

class Hand():
    '''
        У рук свое название.
    '''
    def __init__(self, name, **kwargs) -> None:
        self.name = name
        self.fingers = {
            'forefinger' : Finger(kwargs['forefinger']), # Указательный палец
            'middle_finger' : Finger(kwargs['middle_finger']),
            'ring_finger' : Finger(kwargs['ring_finger']),
            'little_finger' : Finger(kwargs['little_finger']),
        }

    def print_info(self) -> None:
        """просто для информации"""
        print('{} рука!'.format(self.name))
        for finger, key in self.fingers.items():
            print('НАГРУЗКА НА {} ПАЛЕЦ: '.format(finger),key.stress)

'''
Как создавать пальцы для разных рук?

'''

class Finger():
    '''
    Один палец - это словарь из {клавиша:количество_нажатий}.
    Каждый палец имеет свою нагрузку.
    '''
    def __init__(self, keys_set) -> None:
        '''
        stress - нагрузка на палец
        '''
        self.stress = 0
        self.keys_set = keys_set

        self.update_finger_presses()
        self.update_stress()

    def update_finger_presses(self) -> None:
        '''Обновление нажатий пальца.'''
        for key in self.keys_set.keys():
            if key in KEYS_DICT.keys():
                self.keys_set[key] = KEYS_DICT[key]
    
    def update_stress(self) -> None:
        '''Обновление нагрузки пальца.'''
        self.stress = sum(self.keys_set.values())

    

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
    left_hand = LeftHand('left')
    right_hand = RightHand('right')

    left_hand.print_info()
    right_hand.print_info()


if __name__ == '__main__':
    main()



