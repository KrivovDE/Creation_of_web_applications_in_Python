# TODO здесь писать код

class Student:
    def __init__(self, num, name, surname, group, perf):
        self.info = [num, name, surname, group, perf]

    def print_info(self):
        print('{num}) {name} {surname}, group {group}, средний балл - {perf}'.format(
            num = self.info[0], name = self.info[1], surname= self.info[2],
            group = self.info[3], perf = self.info[4]))
    def perf(self):
        return self.info[4]

student_list = [Student(index, 'Иван', 'Иванов', f'РТ-15{index}',
                        index if index < 6 else 11 - index)
                for index in range(1, 11)]

for i_student in student_list:
    i_student.print_info()
print()

student_list.sort(key = lambda x: Student.perf(self=x), reverse=True)

for i_student in student_list:
    i_student.print_info()