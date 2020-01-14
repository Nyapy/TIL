class Korea:
    def __init__(self, name,population, captial):
        self.name = name
        self.population = population
        self.capital = captial

    def show(self):
        print(
            """
            국가의 이름은 {} 입니다.
            국가의 인구는 {} 입니다.
            국가의 수도는 {} 입니다.
            """.format(self.name, self.population, self.capital)
        )
    def show2(self, abc):
        print('abc :', abc)