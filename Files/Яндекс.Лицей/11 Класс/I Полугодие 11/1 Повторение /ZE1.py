hours = int(input())
minutes = int(input())
inter = int(input())
n = int(input())
max_temp, min_pressure = 0, 1000
max_temp_t = min_pressure_t = mid_wet = 0
for i in range(n):
    temp = int(input())
    wet = int(input())
    pressure = int(input())
    if abs(temp) > max_temp:
        max_temp = temp
        if minutes < 10:
            max_temp_t = str(hours) + ":" + "0" + str(minutes)
        else:
            max_temp_t = str(hours) + ":" + str(minutes)
    if pressure < min_pressure:
        min_pressure = pressure
        if minutes < 10:
            min_pressure_t = str(hours) + ":" + "0" + str(minutes)
        else:
            min_pressure_t = str(hours) + ":" + str(minutes)
    mid_wet += wet
    minutes += inter
    if minutes >= 60:
        hours += 1
        minutes = minutes - 60
        if hours == 24:
            hours = 0
if round(mid_wet / n, 2) == mid_wet / n:
    mid_wet = str(mid_wet / n) + "0"
else:
    mid_wet = round(mid_wet / n, 2)
print("Самая высокая температура: ", max_temp_t, ", ", max_temp)
print("Самое низкое давление: ", min_pressure_t, ", ", min_pressure)
print("Среднее значение влажности: ", mid_wet)
