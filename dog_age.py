def dog_age(human_years):
    if human_years <= 0:
        return "Invalid age"
    elif human_years <= 2:
        return human_years * 10.5
    else:
        return 21 + (human_years - 2) * 4


print(dog_age(1))
print(dog_age(2))
print(dog_age(3))
print(dog_age(-1))
