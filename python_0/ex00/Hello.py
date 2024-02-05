ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"

new_list = list(ft_tuple)
new_list[1] = "France!"
ft_tuple = tuple(new_list)

new_set = set(("Hello", "Mulhouse!"))
ft_set.clear()
ft_set.update(new_set)

ft_dict["Hello"] = "42Mulhouse!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
