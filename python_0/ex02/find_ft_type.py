def all_thing_is_obj(object: any = 'empty string') -> int:

    if object != 'empty string' and object is not None:
        types = (str, list, tuple, set, dict)

        i = 0
        while i < len(types):
            x = isinstance(object, types[i])
            if x:
                break
            i += 1

        if i == 0:
            type_str = f'{object} is in the kitchen : {types[i]}'
        elif i == len(types) or object is None:
            type_str = 'Type not found'
        else:
            type_str = str(types[i])
            type_str = type_str[type_str.find('\'') + 1:type_str.rfind('\'')]
            type_str = f'{type_str.capitalize()} : {types[i]}'

        print(type_str)
        return 42
