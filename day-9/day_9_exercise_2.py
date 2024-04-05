# Day 9.2 Nesting



capitals = {
    "Germany":"Berlin",
    "France":"Paris"
}



# travel_log = {
#     "France":["Paris", "Lille", "Dijon"],
#     "Germany":["Berlin", "Hamburg", "Stuttgart"]
# }

# travel_logs = {
#     "France":{
#         "cities_visited":["Paris", "Lille", "Dijon"], "total_visits":12
#     },
#     "Germany":{
#         "cities_visited":["Berlin", "Hamburg", "Stuttgart"], "total_visits":5
#     }
# }

travel_log =  [
    {
        "country":"France",
        "cities_visited":["Paris", "Lille", "Dion"],
        "total_visits":12
    },
  {
        "country":"Germany",
        "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
        "total_visits":5
    },
]


def add_new_country(country_visited, total_visits, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = total_visits
    new_country["cities"] = cities_visited

    travel_log.append(new_country)
    print(travel_log)



add_new_country("Russia", 2, ["Moscow", "Saint", "Ethiopia"])
