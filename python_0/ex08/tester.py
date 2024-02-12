from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

# print(ft_tqdm.__doc__)

for elem in ft_tqdm(range(333)):
    sleep(0.005)
    # print(elem)
print()

# print(tqdm.__doc__)

# for elem in tqdm(range(333)):
#     sleep(0.005)
#     print(elem)
# print()

# for elem in tqdm(range(1000)):
#     sleep(0.005)
# print()

# for elem in tqdm(range(600)):
#     sleep(0.005)
# print()

# for elem in tqdm(range(565)):
#     sleep(0.005)
# print()
