from datetime import datetime, timedelta
from functools import wraps
import time


def test_runs_faster_than(time_limit):
    """Partea unde cream decoratorul"""

    def partea_cu_decoratorul(funct):
        @wraps(funct)
        def functia_noua_care_se_va_rula_in_locul_la_funct(*args, **kwargs):
            start = datetime.now()
            result = funct(*args, **kwargs)
            end = datetime.now()
            time_completed = end - start
            if time_completed > time_limit:
                raise Exception(f'Function ran slower than {time_limit} it ran for {time_completed}')
            return result

        return functia_noua_care_se_va_rula_in_locul_la_funct

    return partea_cu_decoratorul


@test_runs_faster_than(timedelta(seconds=1, milliseconds=10))
def runs_in_1_second():
    time.sleep(1)


@test_runs_faster_than(timedelta(seconds=1, milliseconds=10))
def runs_in_2_second():
    time.sleep(2)


@test_runs_faster_than(timedelta(seconds=3, milliseconds=10))
def runs_in_3_second():
    time.sleep(3)


runs_in_1_second()
runs_in_2_second()
