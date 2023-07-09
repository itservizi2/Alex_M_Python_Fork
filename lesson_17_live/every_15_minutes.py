import time
from datetime import datetime, timedelta

while True:
    a = input('In how much time should I run (second)')
    minutes = int(a)
    should_run_at_time = datetime.now() + timedelta(seconds=minutes)
    print(f'Program will run at {should_run_at_time}')
    should_run = datetime.now() >= should_run_at_time
    while not should_run:
        time.sleep(1)
        should_run = datetime.now() >= should_run_at_time
    # Part where it's running
    print('Im running')
