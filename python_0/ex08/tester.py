from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

print(" -- version fait maison -- ")

print(ft_tqdm.__doc__)

for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()

print(" -o- original version  -o- ")

print(tqdm.__doc__)

for elem in tqdm(range(333)):
    sleep(0.005)
print()

print(" -- version fait maison -- ")

for elem in ft_tqdm(range(100)):
    sleep(0.05)
    print(elem)

print(" -o- original version  -o- ")

for elem in tqdm(range(100)):
    sleep(0.005)
    print(elem)

print(" -- version fait maison -- ")

for elem in ft_tqdm(range(1000)):
    sleep(0.005)
    print()

print(" -o- original version  -o- ")

for elem in tqdm(range(1000)):
    sleep(0.005)
    print(elem)

print(" -- version fait maison -- ")

for elem in ft_tqdm(range(600)):
    sleep(0.005)
    print()

print(" -o- original version  -o- ")

for elem in tqdm(range(600)):
    sleep(0.005)
    print(elem)
