import time as tm

since = tm.time()

# second_string = str(seconds)

# pos = 0
# while second_string[pos] != '.':
# 	pos += 1
# i = pos

# while i >= 0:
# 	if (i * -1 + pos) % 3 == 0 and i * -1 + pos > 0:
# 		second_string = second_string[:i] + ',' + second_string[i:]
# 	i -= 1

print(f'Seconds since January 1, 1970: {since} or {since:.2e} in scientific notation')
print(tm.strftime('%b %d %Y', tm.gmtime()))
