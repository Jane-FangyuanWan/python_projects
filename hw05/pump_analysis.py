# Fangyuan Wan
# Perform analysis on water consumption
import sys


def cal_duration(stripped_line):
    """
    Report the duration of the data file in both hours and days
    """
    THREE = 3
    HOURS_IN_A_DAY = 24
    MINUTES_IN_A_HOUR = 60
    duration_in_hours = len(stripped_line) / MINUTES_IN_A_HOUR
    duration_in_days = round(duration_in_hours / HOURS_IN_A_DAY, THREE)
    print(f"Data covers a total of {duration_in_hours} hours")
    print(f"(That's {duration_in_days} days)\n")


def cal_gallons_produced(stripped_line):
    """
    Report both the total number of gallons produced and the average daily
    consumption.
    """
    THRESHOLD = 200
    TWO = 2
    HOURS_IN_A_DAY = 24
    running_time = 0
    for i in stripped_line:
        if int(i) > THRESHOLD:
            running_time += 1
    gallons_produced = running_time * TWO
    average_daily_comsumption = gallons_produced * HOURS_IN_A_DAY
    print(f"Pump was running for {running_time} minutes,"
          + f" producing {gallons_produced} gallons")
    print(f"(That's {average_daily_comsumption} gallons per day)\n")


def cal_total_power(stripped_line):
    """
    Report the total power used by the pump with Watt minutes and traditional
    Kilowatt Hours (kWh)
    """
    WATTS_PER_MINUTE = 1000
    MINUTES_IN_A_HOUR = 60
    THREE = 3
    total_watts_of_power = 0
    for i in stripped_line:
        total_watts_of_power += int(i)
        total_kwh = round(total_watts_of_power /
                          (WATTS_PER_MINUTE * MINUTES_IN_A_HOUR), THREE)
    print(f"Pump required a total of {total_watts_of_power} watt minutes"
          + " of power")
    print(f"That's {total_kwh} kWh\n")


def cal_time_for_5_100_gallons(stripped_line):
    """
    Print how long it took to consum 5 gallons and 100 gallons of water
    """
    THRESHOLD = 200
    SIX = 6
    TWO = 2
    ONE_HUNDRED = 100
    running_time = 0
    power_produced = 0
    time_to_5gallons = 0
    time_to_100gallons = -1
    for i in stripped_line:
        running_time += 1
        if int(i) > THRESHOLD:
            power_produced += TWO
            if power_produced == SIX:
                time_to_5gallons = running_time
            if power_produced == ONE_HUNDRED:
                time_to_100gallons = running_time
    print(f"It took {time_to_5gallons} minutes of data to reach 5 gallons.")
    print(f"It took {time_to_100gallons} minutes of data" +
          "to reach 100 gallons.\n")


def find_long_runs(stripped_line):
    """
    Report when the pump runs for at least 120 minutes in a row,
    """
    THRESHOLD = 200
    MINUTES_IN_A_ROW_THRESHOLD = 120
    running = False
    run_start_time = -1
    run_duration = 0
    long_runs = []

    for i in range(len(stripped_line)):
        if int(stripped_line[i]) > THRESHOLD:
            if not running:
                run_start_time = i
                running = True
            run_duration += 1
        else:
            if running:
                running = False
                if run_duration > MINUTES_IN_A_ROW_THRESHOLD:
                    long_runs.append((run_duration, run_start_time))
                run_duration = 0

    if long_runs:
        print("Information on water softener recharges:")
        for duration, start_time in long_runs:
            print(f"{duration} minute run started at {start_time + 1}")
        print()


def main():
    """
    Perform analysis on water consumption
    """
    filename = input("Please enter the file name: ")
    filepath = "/Users/janewan/Documents/cs5001/hw05/" + filename
    try:
        f = open(filepath, "r", encoding="utf-8")
    except OSError as e:
        print("Unable to open no_such_file.txt")
        exit()
    stripped_line = f.readlines()

    cal_duration(stripped_line)
    cal_gallons_produced(stripped_line)
    cal_total_power(stripped_line)
    cal_time_for_5_100_gallons(stripped_line)
    find_long_runs(stripped_line)


main()
