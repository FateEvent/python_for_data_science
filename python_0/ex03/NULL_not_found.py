def NULL_not_found(object: any) -> int:

	string = str(type(object))
	string = string[string.find('\'') + 1:string.rfind('\'')]
	print(f'The object is of type {string}')
	return 42