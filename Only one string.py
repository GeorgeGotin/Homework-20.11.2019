print(list(map(lambda x: x** 0.5, list(filter(lambda x: x % 5 == 0 and (x % 100)/10 == 7, range(10000000))))))
