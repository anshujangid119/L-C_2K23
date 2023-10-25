class Human:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__heart_pumping = True

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def is_heart_pumping(self):
        return self.__heart_pumping

    def introduce(self,gender="unknown"):
        print(f"Hello, I am {self.__name}, and I am {self.__age} years old. And my gender is {gender}")

    def perform_health_check(self):
        if self.__heart_pumping:
            print(f"{self.__name}'s heart is pumping. {self.__name} is alive.")
        else:
            print(f"{self.__name}'s heart is not pumping. {self.__name} is not alive.")

class Male(Human):
    def __init__(self, name, age):
        super().__init__(name, age)

    def introduce(self):
        super().introduce("male")

class Female(Human):
    def __init__(self, name, age):
        super().__init__(name, age)

    def introduce(self):
        super().introduce("female")

male = Male("Ram", 35)
female = Female("Radha", 28)
male.introduce()
male.perform_health_check()
female.introduce()
female.perform_health_check()
female._Human__heart_pumping = False
female.perform_health_check()
