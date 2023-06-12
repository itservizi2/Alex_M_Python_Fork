queue = ['Ivan']
print(bool(queue))
# while len(queue) > 0: # Echivalent
while queue:
    print('Hello', queue[0])
    someone_came_in = input('Did someone come in y/n?') == 'y'
    if someone_came_in:
        number_of_people = int(input('How many poeple'))
        for a in range(number_of_people):
            queue.append(input('What is his name?'))
    queue.pop(0)
print('Work done')
