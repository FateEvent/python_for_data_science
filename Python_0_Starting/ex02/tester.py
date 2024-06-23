from find_ft_type import all_thing_is_obj

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj(False)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")

print(all_thing_is_obj(10))

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False

all_thing_is_obj(Nothing)
all_thing_is_obj(Garlic)
all_thing_is_obj(Zero)
all_thing_is_obj(Empty)
all_thing_is_obj(Fake)
all_thing_is_obj(False)
print(all_thing_is_obj())
