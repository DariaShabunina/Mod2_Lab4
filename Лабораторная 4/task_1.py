class Building:
    def __init__(self, name: str, architect: str, date: int):
        """
        Создание и подготовка к работе объекта "Здание"
        :param name: Название здания
        :param architect: Архитектор здания
        :param date: Год построки здания
        Примеры:
        >>> building = Building("Автостоянка на 200 м.м.", "Иванов И.И.", 2018) # инициализация экземпляра класса
        """
        self._name = None
        self.set_name(name)
        self._architect = None
        self.set_architect(architect)
        self._date = None
        self.set_date(date)

    def set_name(self, new_name: str) -> None:
        """
        Определяет допустимость вводных данных
        :param new_name: Название здания
        :raise TypeError: Если введено некорректное значение (тип)
        Примеры:
        >>> building = Building("Автостоянка на 200 м.м.", "Иванов И.И.", 2018)
        >>> building.set_name("Автостоянка на 500 м.м.")
        """
        if not isinstance(new_name, str):
            raise TypeError("Поле название здания должно быть типа str")
        self._name = new_name

    def set_architect(self, new_author: str) -> None:
        """
        Определяет допустимость вводных данных
        :param new_author: Архитектор здания
        :raise TypeError: Если введено некорректное значение (тип)
        Примеры:
        >>> building = Building("Автостоянка на 200 м.м.", "Иванов И.И.", 2018)
        >>> building.set_architect("Петров П.П.")
        """
        if not isinstance(new_author, str):
            raise TypeError("Поле архитектор здания должно быть типа str")
        self._architect = new_author

    def set_date(self, new_date: int) -> None:
        """
        Определяет допустимость вводных данных
        :param new_date: Год построки здания
        :raise TypeError: Если введено некорректное значение (тип)
        Примеры:
        >>> building = Building("Автостоянка на 200 м.м.", "Иванов И.И.", 2018)
        >>> building.set_date(2019)
        """
        if not isinstance(new_date, int):
            raise TypeError("Поле год построки здания должно быть типа int")
        self._date = new_date

    def duration(self, cur_date: int) -> int:
        """
        Определяет допустимость вводных данных
        :param cur_date: Текущи год
        :raise TypeError: Если введено некорректное значение (тип)
        :return: Срок эксплуатации здания
        Примеры:
        >>> building = Building("Автостоянка на 200 м.м.", "Иванов И.И.", 2018)
        >>> dur = building.duration(2021)
        """
        if not isinstance(cur_date, int):
            raise TypeError("Год должен быть типа int")
        return cur_date - self._date

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._name!r}, {self._architect!r}, {self._date})'

    def __str__(self) -> str:
        return f'Здание "{self._name}"'


class ResidentBuilding(Building):
    def __init__(self, name: str, architect: str, num_rooms, date: int):
        """
        Создание и подготовка к работе объекта "Здание"
        :param name: Название здания
        :param architect: Архитектор здания
        :param num_rooms: Количество квартир
        :param date: Год построки здания
        Примеры:
        >>> res_building = ResidentBuilding("Жилой дом", "Иванов И.И.", 500, 2018) # инициализация экземпляра класса
        """
        super().__init__(name, architect, date)
        self.num_rooms = num_rooms
        self._name = None
        self.set_name(name)

    def set_name(self, new_name: str) -> None:
        """
        Определяет допустимость вводных данных
        :param new_name: Название здания
        :raise TypeError: Если введено некорректное значение (тип)
        :raise ValueError: Если поле не содержит Жилой
        Примеры:
        >>> res_building = ResidentBuilding("Жилой дом", "Иванов И.И.", 500, 2018)
        >>> res_building.set_name("Жилой дом на 500 квартир")
        """
        if not isinstance(new_name, str):
            raise TypeError("Поле название здания должно быть типа str")
        if not("Жилой" in new_name ):
            raise ValueError("Поле название здания должно содержать Жилой")
        self._name = new_name

    @property
    def num_rooms(self) -> int:
        return self._num_rooms

    @num_rooms.setter
    def num_rooms(self, new_num_rooms: int) -> None:
        if not isinstance(new_num_rooms, int):
            raise TypeError("Количество квартир должно быть типа int")
        if new_num_rooms <= 0:
            raise ValueError("Количество квартир должно быть положительным числом")
        self._num_rooms = new_num_rooms

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._name!r}, {self._architect!r}, {self._num_rooms}, {self._date})'


building = Building("Название1", "Архитекор1", 2020)
print(str(building))
print(repr(building))
building.set_date(2000)
building.set_name("Название2")
building.set_architect("Архитекор2")
print(repr(building))
print(building.duration(2023))

res_building = ResidentBuilding("Жилой Название1", "Архитекор1", 500, 2020)
print(str(res_building))
print(repr(res_building))
res_building.set_date(2000)
res_building.set_name("Жилой Название2")
res_building.set_architect("Архитекор2")
res_building.num_rooms = 600
print(repr(res_building))
print(res_building.duration(2023))
#end
