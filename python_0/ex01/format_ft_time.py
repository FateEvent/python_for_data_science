import time as tm

since = tm.time()
second_str = str(since)

if isinstance(since, float):
    pos = 0
    while second_str[pos] != '.':
        pos += 1
    i = pos

    while i >= 0:
        if (i * -1 + pos) % 3 == 0 and i * -1 + pos > 0:
            second_str = second_str[:i] + ',' + second_str[i:]
        i -= 1

print(f'Seconds since January 1, 1970: {second_str}', end='')
print(f'or {since:.2e} in scientific notation')
print(tm.strftime('%b %d %Y', tm.gmtime()))
