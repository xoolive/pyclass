from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    age: int
    grades: list[float] = field(default_factory=list)

    def average(self) -> float:
        return sum(self.grades) / len(self.grades) if self.grades else 0.0


alice = Student(name="Alice", age=20, grades=[15.0, 20.0, 18.0])
bob = Student(name="Bob", age=22)
charlie = Student(name="Charlie", age=19, grades=[12.0, 8.0])

sorted([alice, bob, charlie], key=lambda student: student.average(), reverse=True)
# [Student(name='Alice', age=20, grades=[15.0, 20.0, 18.0]), Student(name='Charlie', age=19, grades=[12.0, 8.0]), Student(name='Bob', age=22, grades=[])]
