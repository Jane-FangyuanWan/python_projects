def main ():
    in_string = input("Please answer 'yes' or 'no': ").lower()
    while(not(in_string == 'yes' or 'no')):
        in_string = input("You must answer 'yes' or 'no': ")
    print("Thank you for your satisfactory answer")

main()