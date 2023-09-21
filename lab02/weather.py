temperatures = [
    (65, 53),
    (71, 49),
    (76, 50),
    (68, 53),
    (65, 54),
    (65, 55),
    (65, 56),
    (62, 53),
    (62, 52),
    (61, 51)
]

temperature_differences = [high - low for high, low in temperatures]

average_temperature = sum([sum(temp) / 2 for temp in temperatures]) / len(temperatures)

highest_temperature = max([high for high, _ in temperatures])
highest_temperature_in_celsius = (highest_temperature - 32)* 5/9

print("Differences between highest and lowest temperature: {:.2f} °F".format(max(temperature_differences)))
print("Average temperature for 10-day forescats: {:.2f} °F".format(average_temperature))
print("Highest temperature in Celsius: {:.2f} °C".format(highest_temperature_in_celsius))

