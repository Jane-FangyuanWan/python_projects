# takes a users age and resting heart rate, and computes the range of heart rates that correspond to each of the zones above.#
def main():
    age = int(input("Please enter your age: "))
    restHR = int(input("Please enter your resting heart rate: "))

    print("=======================================")

    #
    maxHR = 208 - 0.7*age
    reserveHR = maxHR - restHR
    # calculate Zone 1 heart rate
    hr1a = restHR + 0.5*reserveHR
    hr1b = restHR + 0.6*reserveHR-0.01
    # calculate Zone 2 heart rate
    hr2a = restHR + 0.6*reserveHR
    hr2b = restHR + 0.7*reserveHR-0.01
    # calculate Zone 3 heart rate
    hr3a = restHR + 0.7*reserveHR
    hr3b = restHR + 0.8*reserveHR-0.01
    # calculate Zone 4 heart rate
    hr4a = restHR + 0.8*reserveHR
    hr4b = restHR + 0.93*reserveHR-0.01
    # calculate Zone 5 heart rate
    hr5a = restHR + 0.93*reserveHR
    hr5b = restHR + reserveHR

    print(f"Your heart rate reserve is: {reserveHR:.2f} bpm")
    print("Here is a breakdown of your training zones:")
    print(f"Zone 1: {hr1a:.2f} to {hr1b:.2f} bpm")
    print(f"Zone 2: {hr2a:.2f} to {hr2b:.2f} bpm")
    print(f"Zone 3: {hr3a:.2f} to {hr3b:.2f} bpm")
    print(f"Zone 4: {hr4a:.2f} to {hr4b:.2f} bpm")
    print(f"Zone 5: {hr5a:.2f} to {hr5b:.2f} bpm")

    print("=======================================")


main()
