import numpy as np

"""
sbux = np.loadtxt("sbux.csv", usecols=(0, 1, 4), skiprows=1, delimiter=",",
                  dtype={'names': ('date', 'open', 'close'),
                         formats': ('datetime64[D]', 'f4', 'f4')})'

"sbux.csv" — имя файла (или сюда же можно передать объект файла, такой пример вы увидите в следующей задаче урока), из которого считываются данные.
usecols — список колонок, которые нужно использовать. Если параметр не указан, считываются все колонки.
skiprows — количество рядов в начале файла, которые нужно пропустить. В нашем случае пропущен ряд заголовков. По умолчанию (если значение параметра не указано явно) skiprows = 0.
delimiter — разделитель столбцов в одной строке, в csv-файлах это запятая, по умолчанию разделителем является любой пробел (в том числе — знак табуляции).
dtype — словарь из названий колонок (переменных) и типов хранящихся в них значений. NumPy использует свою собственную систему типов, и названия именно этих типов нужно указать. По умолчанию функция попытается самостоятельно угадать, какому типу принадлежат подаваемые на вход значения.

"""
from urllib.request import urlopen
f = urlopen('https://stepic.org/media/attachments/lesson/16462/boston_houses.csv')

arr = np.loadtxt(f, skiprows=1, delimiter=",")
# print(arr.shape)
print(arr.mean(axis=0))