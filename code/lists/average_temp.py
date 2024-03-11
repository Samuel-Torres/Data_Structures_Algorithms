import array

num_of_days = int(input("How Many Days of Temp? "))
temps = array.array('i')

for i in range(0, num_of_days):
    day_x_temp = int(input(f"Day {i + 1}'s high temp: "))
    temps.append(day_x_temp)

sum_of_temps = sum(temps)
total_days = len(temps)


def get_average_temp(temp_sum, num_days):
    return temp_sum / num_days


average_temperature = get_average_temp(sum_of_temps, total_days)


def get_above_avg(avg_temp):
    days_above_average = 0
    for day in temps:
        if day > average_temperature:
            days_above_average += 1
    return days_above_average


print(
    f"The average temp was: {average_temperature} and there were {get_above_avg(average_temperature)} days above average!")
