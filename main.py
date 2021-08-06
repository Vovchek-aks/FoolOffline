import random as rnd


class Card:
    SUITS = list('бтчп')

    def __init__(self, suit: str, value: int):
        if suit not in Card.SUITS:
            raise ValueError
        if not 5 <= value <= 13:
            raise ValueError

        self.__SUIT = suit
        self.__VALUE = value

    def __name_of_value(self) -> str:
        return str(self.__VALUE) if self.__VALUE < 10 else 'ВДКТ'[self.__VALUE - 10]

    def __str__(self):
        return self.__SUIT + self.__name_of_value()

    def get_suit(self) -> str:
        return self.__SUIT

    def get_value(self) -> int:
        return self.__VALUE


class Joker:
    @staticmethod
    def get_stack() -> list:
        stack = []

        for i in Card.SUITS:
            for j in range(5, 14):
                stack.append(Card(i, j))

        return stack

    @staticmethod
    def print_stack(stack: list) -> None:
        for i in stack:
            print(i)

    @staticmethod
    def __get_real_card_value(card: Card, tc: str) -> int:
        return card.get_value() * (10 if card.get_suit() == tc else 1)

    @staticmethod
    def can_beat(c1: Card, c2: Card, tc: str) -> bool:
        return Joker.__get_real_card_value(c1, tc) > \
               Joker.__get_real_card_value(c2, tc)


class BaseStepper:
    def get_step(self, cards: list, is_defence: bool) -> tuple:
        raise NotImplementedError


class StepFromInput(BaseStepper):
    def get_step(self, cards: list, is_defence: bool) -> tuple:
        if is_defence:
            pass
        else:
            pass

    def __not_defence_input(self):
        pass


class Player:
    def __init__(self, cards: list, stepper: BaseStepper):
        self.__cards = cards
        self.__stepper = stepper

    def do_step(self, cards: list, is_defence: bool) -> tuple:
        return self.__stepper.get_step(cards, is_defence)


