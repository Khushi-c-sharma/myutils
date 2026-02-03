def irctc_age_checker(age: int):
    """
    Checks age-based eligibility for booking train tickets on IRCTC.

    :param age: Age of the passenger in years
    """
    if age < 0:
        print("Invalid age entered.")
        return

    if age <= 5:
        print("Berth not allotted explicitly. Do you want to book?")
    elif 5 < age <= 10:
        print("Eligible to book a partial ticket.")
    elif age >= 60:
        print("Eligible for 50% concession on ticket fare.")
    else:
        print("Eligible for full ticket without concession.")


irctc_age_checker(3)
irctc_age_checker(8)
irctc_age_checker(65)
irctc_age_checker(30)
