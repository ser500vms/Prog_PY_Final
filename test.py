import datetime as dt
from script import print_data

with open('data.csv', 'r', encoding='utf-8') as file:
    data = list(file.readlines())

result = [''.join(data[i:i + 4]) for i in range(0, len(data), 4)]
print(result)
for i in range(len(result)):
    if '2024-02-18' in result[i]:
        print(result[i])

# now = dt.datetime.now(dt.timezone.utc).astimezone()
# time_format = "%Y-%m-%d %H:%M:%S"
# x = f'{now:{time_format}}'
# b = [''.join(x[i:i + 4]) for i in range(0, len(x), 4)]
# for i in range(len(b)):
#     print(b[i])
# if '01' and '2024' and '18' in x:
#     print(x)
