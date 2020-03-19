import random


def get_random_array(max_size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(max_size)]