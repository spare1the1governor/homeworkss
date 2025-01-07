def calculate_distance(p1: tuple, p2: tuple) -> float:
    """Вычисляет евклидово расстояние между двумя точками."""
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5


def plan_route(houses):
    """Находит оптимальный маршрут для Санты."""
    if not houses:
        return "Нет домов для посещения!", 0

    # Начальная точка (Северный полюс)
    start = (0, 0)
    route = [start]
    total_distance = 0

    # Список доступных домов
    remaining_houses = houses.copy()
    current_position = start

    while remaining_houses:
        # Найти ближайший дом
        next_house = min(remaining_houses, key=lambda house: calculate_distance(current_position, house))
        # Обновить расстояние и маршрут
        total_distance += calculate_distance(current_position, next_house)
        route.append(next_house)
        current_position = next_house
        remaining_houses.remove(next_house)

    # Возврат на Северный полюс
    total_distance += calculate_distance(current_position, start)
    route.append(start)

    return route, round(total_distance, 2)

# Пример использования
houses = [(2, 3), (-1, 5), (4, -2)]
route, total_distance = plan_route(houses)

print("Дома:", houses, end="\n\n")
route_formatted = route.copy()
route_formatted[0] = route_formatted[-1] = "Северный полюс"
route_formatted = " -> ".join([str(i) for i in route_formatted])
print("Рассчитанный маршрут:", route_formatted, end="\n\n", sep="\n")
print("Общее расстояние:", total_distance)


