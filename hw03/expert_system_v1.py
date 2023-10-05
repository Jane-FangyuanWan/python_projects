'''
A fever diagnosis system asks users input and predict the relevant symptoms
'''

POSSIBLE_SYMPTOMS1 = "Possibilities include pneumonia or infection of airways"
POSSIBLE_SYMPTOMS2 = "Possibilities include viral infection"
POSSIBLE_SYMPTOMS3 = "Possibilities include a throat infection."
POSSIBLE_SYMPTOMS4 = "Possibilities include kidney infection."
POSSIBLE_SYMPTOMS5 = "Possibilities include a urinary tract Infection."
POSSIBLE_SYMPTOMS6 = "Possiblities sunstroke or heat exhaustion."
POSSIBLE_SYMPTOMS7 = "Possibilities include menigitis."
POSSIBLE_SYMPTOMS8 = "Possibilities include digestive tract infection."
INSUFFICIENT_INFO = "Insufficient information to list possibilities."


def if_aching_bone():
    '''
    The below function starts with asking users if they have aching bones or
    aching joints and provides relevant symptoms
    '''
    if input("Do you have aching bones or aching joints?") == "yes":
        print(POSSIBLE_SYMPTOMS2)
        exit()
    else:
        if input("Do you have a rash?") == "yes":
            print(INSUFFICIENT_INFO)
            exit()
        else:
            if input("Do you have a sore throat?") == "yes":
                print(POSSIBLE_SYMPTOMS3)
                exit()
            else:
                if input("Do you have back pain just above the waist with \
chills and fever?") == "yes":
                    print(POSSIBLE_SYMPTOMS4)
                    exit()
                else:
                    if input("Do you have pain urinating or are urinating more\
 often?") == "yes":
                        print(POSSIBLE_SYMPTOMS5)
                        exit()
                    else:
                        if input("Have you spent the day in the sun or in hot \
condtions?") == "yes":
                            print(POSSIBLE_SYMPTOMS6)
                            exit()
                        else:
                            print(INSUFFICIENT_INFO)
                            exit()


def main():
    '''
    System starts with asking users if they are coughing and provides relevant
    symptoms
    '''
    print("Fever Diagnosis System (Respond to yes/no)")
    if input("Are you coughing?") == "yes":
        if (input("Are you short of breath or wheezing or coughing up phlegm?")
                == "yes"):
            print(POSSIBLE_SYMPTOMS1)
            exit()
        else:
            if input("Do you have a headache?") == "yes":
                print(POSSIBLE_SYMPTOMS2)
                exit()
            else:
                if_aching_bone()
    else:
        if input("Do you have a headache?") == "yes":
            if input("Are are experiencing any of the following: pain when\
 bending your head forward, nausea or vomiting, bright light hurting your\
 eyes, drowsiness or confusion?") == "yes":
                print(POSSIBLE_SYMPTOMS7)
                exit()
            else:
                if input("Are you vomiting or had diarrhea?") == "yes":
                    print(POSSIBLE_SYMPTOMS8)
                    exit()
                else:
                    if_aching_bone()
        else:
            if_aching_bone()


main()
