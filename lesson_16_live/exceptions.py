class DatabaseDoesNotExist(Exception):
    pass


class ConnectionTimeOut(Exception):
    pass


def connect_to_database(a, b):
    if a:
        raise DatabaseDoesNotExist()
    if b:
        raise ConnectionTimeOut()


connected = False
while not connected:
    try:
        connect_to_database(input('a'), input('b'))
        connected = True
        break
    except ConnectionTimeOut:
        print('Timeout- retyring')
    except DatabaseDoesNotExist:
        print('Nothing to connect to')
        break
    except Exception:
        print('Something went wrong')
        break
print(connected)
