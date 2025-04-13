import os
from functools import wraps


def log(filename=None):
    """Декоратор для логирования выполнения функций"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            global log_msg
            module_dir = os.path.dirname(__file__)
            try:
                result = func(*args, **kwargs)
                log_msg = (
                    f"{func.__name__} started ok. Inputs: {args}, {kwargs}.\n"
                    f"{func.__name__} finished with result: {result}\n"
                )
            except Exception as e:
                log_msg = f"{func.__name__} ошибка: {type(e).__name__}: {str(e)}. " f"Inputs: {args}, {kwargs}\n"
                raise
            finally:
                if filename:
                    full_path = os.path.join(module_dir, filename)
                    os.makedirs(os.path.dirname(full_path), exist_ok=True)
                    with open(full_path, "a", encoding="utf-8") as f:
                        f.write(log_msg)
                else:
                    print(log_msg)
            return result

        return wrapper

    return decorator


# Пример использования
@log("my_log.txt")
def example_function(x, y):
    return x + y


# example_function(1, 2)
