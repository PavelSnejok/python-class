# student_score = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 74,
#     "Draco": 74,
#     "Neville": 62,
# }
#
# student_grades = {}
#
# for key in student_score:
#     if student_score[key] > 90:
#         student_grades[key] = "Outstanding"
#     elif student_score[key] > 80:
#         student_grades[key] = "Exceeds Expectations"
#     elif student_score[key] > 70:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"
#
# print(student_grades)

################

# travel_log = {
#     "France": {"citities_visited": ["Paris", "Little", "Dijon"]},
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }
#
# print(travel_log[0])

###########

country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log.
def add_new_country(name, time_visited, cities_visited):
    travel_log.append({"country": name, "visits": time_visited, "cities": cities_visited})


# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
