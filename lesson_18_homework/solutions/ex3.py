'''
Creati un decorator numit benchmark_time care va calcula timpul executiei fiecarei functii care o decoreaza.

Decoratorul va afisa la consola in secunde timpul in care a fost executat functia care este decorata.

Bonus points daca gasiti o metoda de a afisa si numele functiei care a fost executata.
'''
import time
from functools import wraps


def benchmark_time(func):
    """Decorator pentru a masura executia timpuli"""

    @wraps(func)
    def wrapper():
        function_name = func.__name__
        t1 = time.time()
        result = func()
        t2 = time.time() - t1
        print(f"Functia {str(function_name)} a fost executat in {t2} seconds")
        return result

    return wrapper


@benchmark_time
def functie_obisnuita():
    """Functie care doarme 1.3 secunde"""
    time.sleep(1.3)


functie_obisnuita()
