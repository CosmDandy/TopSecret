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
    if temp > max_temp:
        max_temp = temp
        max_temp_t = str(hours) + ":" + str(minutes)
    if pressure < min_pressure:
        min_pressure = pressure
        min_pressure_t = str(hours) + ":" + str(minutes)
    mid_wet += wet
    minutes += inter
    if minutes >= 60:
        hours += 1
        minutes = minutes - 60
print("Самая высокая температура: ", max_temp_t, ", ", max_temp)
print("Самое низкое давление: ", min_pressure_t, ", ", min_pressure)
print("Среднее значение влажности: ", mid_wet / n)
