def strict(func):

    def wrapper(*args, **kwargs):
        # Получаем информацию о типах аргументов из прототипа функции
        annotations = func.__annotations__

        # Проверяем, что аргументы соответствуют типам в прототипе
        for i, arg in enumerate(args):
            if annotations:
                expected_type = list(annotations.values())[i]
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Аргумент {list(annotations.keys())[i]} должен быть типа {expected_type}, а не {type(arg)}")

        # Проверяем, что ключевые аргументы соответствуют типам
        for key, value in kwargs.items():
            if annotations:
                expected_type = annotations[key]
                if not isinstance(value, expected_type):
                    raise TypeError(f"Ключевой аргумент {key} должен быть типа {expected_type}, а не {type(value)}")
        # Вызываем исходную функцию
        return func(*args, **kwargs)

    return wrapper
