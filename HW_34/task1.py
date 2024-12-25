class BaseTeaException(Exception):
    pass


class Sugar:

    def __init__(self, kind):
        self.kind = kind
        if not self._validate_kind(kind):
            raise ValueError("Invalid sugar type")

    @staticmethod
    def _validate_kind(kind):
        if kind == "brown" or kind == "white":
            return kind


class Tea:
    @staticmethod
    def _validate_kind(kind):
        return kind in ("green", "black")

    def __init__(self, kind):
        self.kind = kind
        if not self._validate_kind(kind):
            raise ValueError("Invalid tea type")


class TeaCup:
    def __init__(self):
        self.sweetness = 0
        self.fullness = 0
        self.tea = None

    def pour_water(self, amount=None):
        if amount is None:
            self.fullness = 1
            return self.fullness
        elif 0 <= amount <= 1:
            self.fullness += amount
            if self.fullness > 1:
                raise BaseTeaException("Attempt to pour too much water")
            return self.fullness

    def drink(self, amount=None):
        if amount is None:
            self.fullness = 0
            return self.fullness
        elif 0 <= amount <= 1:
            self.fullness -= amount
            if self.fullness < 0:
                raise BaseTeaException("Attempt to drink beyond available amount")
            return self.fullness

    def is_full(self):
        if self.fullness == 1:
            return True
        else:
            return False

    def __add__(self, other):
        if isinstance(other, Sugar):
            self.sweetness += 1
            return self
        elif isinstance(other, Tea):
            self.tea = other.kind
            return self
        else:
            raise TypeError("Can only add Sugar or Tea to a TeaCup")

    def __sub__(self, other):
        if isinstance(other, Sugar):
            self.sweetness -= 1
            if self.sweetness < 0:
                raise ValueError("Amount of sugar can't be negative")
            return self
        else:
            raise TypeError("Can only subtract Sugar from TeaCup")
