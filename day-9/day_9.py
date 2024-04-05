# Day 9.2 Travel log | Nested dictionary

travel_log = [
    {
        "country":"Ethiopia",
        "visits":12,
        "cities":["Soddo", "Areka", "Bodit"]
    },
    {
        "country":"Japan",
        "visits":5,
        "cities":["jemica", "Keny", "somalia"]   
    }
]

def add_new_country(country,cities, visits):
    new_country = {}
    new_country["country"] = country
    new_country["cities"] = cities
    new_country["visits"] = visits
    travel_log.append(new_country)
    print(travel_log)
add_new_country("Sudan", 9, ["Soud", "Peri", "Feri"])