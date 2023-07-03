from collections import deque

my_queue = deque(['Marius', 'Ion', 'Victor'])
while my_queue:
    print('queue is', my_queue)
    now_processing = my_queue.pop()
    print("Now processing", now_processing)
    new_customer = input('New customer name or empty')
    if new_customer:
        is_priority = input('Is priority (y/n)')
        if is_priority == 'y':
            my_queue.appendleft(new_customer)
        else:
            my_queue.append(new_customer)
