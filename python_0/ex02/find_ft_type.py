def all_thing_is_obj(object: any) -> int:

	string = str(type(object))
	string = string[string.find('\'') + 1:string.rfind('\'')]
	print(f'The object is of type {string}')
	return 42
