import time as tm

since = tm.time()

print(f'Seconds since January 1, 1970: {since:,.2f}', end=' ')
print(f'or {since:.2e} in scientific notation')
print(tm.strftime('%b %d %Y', tm.gmtime()))
