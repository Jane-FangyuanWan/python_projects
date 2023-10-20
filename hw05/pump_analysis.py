import sys


def main():
    filename = input("Please enter the file name: ")
    filepath = "/Users/janewan/Documents/cs5001/hw05/" + filename
    try:
        f = open(filepath, "r", encoding="utf-8")
    except OSError as e:
        print("Unable to open no_such_file.txt")
        return()
    
    stripped_line = f.readlines()

    total_watts_of_power = 0
    for i in stripped_line:
        total_watts_of_power += int(i)
    print(total_watts_of_power)   
   
    HOURS_IN_A_DAY = 24
    MINUTES_IN_A_HOUR = 60
    WATTS_PER_MINUTE = 1000



def cal_duration(total_watts_of_power): 
    """
    Report the duration of the data file in both hours and days
    """
    duration_in_hours = total_watts_of_power//(WATTS_PER_MINUTE * MINUTES_IN_A_HOUR)
    duration_in_days = duration_in_hours/ HOURS_IN_A_DAY
    print(duration_in_hours)
    print(duration_in_days)
    

def cal_gallons_produced(stripped_line):
    """
    Report both the total number of gallons produced and the average daily consumption.
    """

    #find out the length of time the pump is running 




    """
    Report the total power used by the pump with Watt minutes and traditional Kilowatt Hours (kWh)
    """
    """
    Print how long it took to consum 5 gallons and 100 gallons of water
    """
