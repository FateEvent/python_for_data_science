import datetime as dt

first_date = dt.datetime(1970, 1, 1)
time_since = dt.datetime.now() - first_date
seconds = time_since.total_seconds()
second_string = str(seconds)

pos = second_string.find('.')
i = pos

while i >= 0:
	if (i * -1 + pos) % 3 == 0 and i * -1 + pos > 0:
		second_string = second_string[:i] + ',' + second_string[i:]
	i -= 1

print(f'Seconds since January 1, 1970: {second_string} or {seconds:.2e} in scientific notation')
print(dt.datetime.today().strftime('%b %d %Y'))
