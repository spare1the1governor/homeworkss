def draw_christmas_tree(size):
    for i in range(size):
        spaces = size - i - 1
        stars = 2 * i + 1
        print(" " * spaces + "*" * stars)
    for i in range(2):  # Ствол из 2 строк
        print(" " * (size - 1) + "*")

draw_christmas_tree(7)
