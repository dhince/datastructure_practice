weather = {}
with open("nyc_weather.csv", "r") as wt:
    count = 0
    for line in wt:
        if count == 0:
            pass
        else:
            token = line.split(',')
            weather[token[0]] = float(token[1])
        count += 1
print(weather)
avg = 0
for value in weather.values():
    avg += value
print(avg)