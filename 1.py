# def decor_times(fuu):
#     def wrap(*args, **kwargs):
#         start = time.time()
#         res = fuu(*args, **kwargs)
#         dt = time.time() - start
#         print (f"Время работы: {dt} сек")
#         return res
#     return wrap
#
# @decor_times
# def two_sum(one_number: int, two_number: int):
#     try:
#         print(one_number + two_number)
#     except TypeError:
#         print("Ghjdthnt nbfs lfyys[")
#

# two_sum = decor_times(two_sum)

# two_sum(9, 4)

# timed_run = Timer(partial(two_sum(9, 4))).timeit(number=10000)
# print(timed_run)


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(f"Привет меня зовут {self.name} мне {self.age} лет.")
#

cat1 = Cat("Васька", 6)

d = {}
d[cat1] = "sidc"
print(d)


def foo(dict_num):
    sorted_k = sorted(dict_num.items(), key=lambda item: item[1])
    print(sorted_k[0][0], sorted_k[1][0])


people = {"Вася": 25, "Петя": 30, "Маша": 20}

foo(people)


@user_router.get("/full_user_statistics/")
async def get_full_user_statistics_in_unit(user_id: uuid.UUID, list_unit_id: list[uuid.UUID]) -> list[UnitsStruct]:

    return UsersService.get_full_user_statistics_in_unit(user_id, list_unit_id)



    @classmethod
    def get_full_user_statistics_in_unit(cls, user_id: uuid.UUID, list_unit_id: list[uuid.UUID]) -> list[UnitsStruct]:

        statistics = []

        for unit in list_unit_id:
            try:
                counts = {"count_tasks": 0, "in_progress": 0, "under_review": 0, "completed": 0, "not_completed": 0}
                unit = UnitsStruct.model_validate(cls._db.session.query(UnitModel).filter_by(id=unit).one())
                for task in unit.tasks:
                    if task.users_id == user_id:
                        counts["count_tasks"] += 1
                        if task.status == "выполняется":
                            counts["in_progress"] += 1
                        elif task.status == "на проверке":
                            counts["under_review"] += 1
                        elif task.status == "завершена":
                            counts["completed"] += 1
                        elif task.status == "не выполнена":
                            counts["not_completed"] += 1
                unit.count_tasks_without_parent = counts
                statistics.append(unit)
            except NoResultFound as e:
                raise HTTPException(status_code=404, detail="Направление не найдено") from e
            except ValidationError as e:
                raise HTTPException(status_code=400, detail="Ошибка валидации данных о направлении") from e
            except Exception as e:
                raise HTTPException(status_code=400, detail=str(e)) from e
        return statistics
LVTDD21B8PD564322
