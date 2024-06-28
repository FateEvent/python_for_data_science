__version__ = '0.0.1'

from .ft_builtins import ft_filter
from .text_handling import ft_punctuation, check_entry_format, \
    is_integer, prompt_a_prompt
from .Loading import ft_tqdm
from .load_image import ft_load
from .load_csv import load


print('Here are the functions that you can find in ft_package:')
print(ft_filter.__doc__)
print(ft_punctuation.__doc__)
print(check_entry_format.__doc__)
print(is_integer.__doc__)
print(ft_tqdm.__doc__)
print(prompt_a_prompt.__doc__)
print(ft_load.__doc__)
print(load.__doc__)
