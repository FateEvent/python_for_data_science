def NULL_not_found(object: any = 'empty string') -> int:

    if object != 'empty string':

        if object == '':
            string = 'Empty'
        elif object != object:
            string = 'Cheese'
        elif object is False:
            string = 'Fake'
        elif object == 0:
            string = 'Zero'
        elif object is None:
            string = 'Nothing'
        else:
            print("Type not found")
            return 1

        print(f'{string}: {object} {type(object)}')
        return 0
