class Address:
    def __init__(self, street: str, city: str, state: str, country: str, neighborhood: str) -> None:
        self.__street = street
        self.__city = city
        self.__state = state
        self.__country = country
        self.__neighborhood = neighborhood

    def get_street(self) -> str:
        return self.__street

    def get_city(self) -> str:
        return self.__city

    def get_state(self) -> str:
        return self.__state

    def get_country(self) -> str:
        return self.__country

    def get_neighborhood(self) -> str:
        return self.__neighborhood

    def set_street(self, street: str) -> None:
        self.__street = street

    def set_city(self, city: str) -> None:
        self.__city = city

    def set_state(self, state: str) -> None:
        self.__state = state

    def set_country(self, country: str) -> None:
        self.__country = country

    def set_neighborhood(self, neighborhood: str) -> None:
        self.__neighborhood = neighborhood

    def __str__(self) -> str:
        return f"{self.__street}, {self.__neighborhood}, {self.__city}, {self.__state}, {self.__country}"

    