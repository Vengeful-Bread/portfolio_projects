grades = ((100, False),(100, False),(100, False),(100, False),(100, False)) # In each nested tuple, (grade, honors boolean)

for completed_class in grades:
    (grade, isHonors) = completed_class
    print(f"You got a {grade}, but it is {isHonors}.")