def all_thing_is_obj(object = None) -> int:

	if object != None:
		types = (bool, int, float, complex, str, list, tuple, set, dict)

		i = 0
		while i < len(types):
			x = isinstance(object, types[i])
			if x == True:
				break
			i += 1

		if i == 4:
			type_str = object + ' is in the kitchen'
		elif i == len(types) or object == None:
			type_str = 'none'
		else:
			type_str = str(types[i])
			type_str = type_str[type_str.find('\'') + 1:type_str.rfind('\'')]

		print(f'{type_str.capitalize()} : {types[i]}')
	return 42
