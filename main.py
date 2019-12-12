data_from_file = [
    {
        "id":1,
        "places_ive_been": [
            {
                "city": "Ljubljana"
            }
        ]
    }
]
def read_users_from_api():
    ...
def read_data_from_any_file(file_name):
    with open(file_name, "r") as users_file:
        ...
        data = json.loads(users_file.read())
        return data

def print_city(users_list, end_message, message):
    for user_dict in users_list:
        print(message)
        print(user_dict["places_ive_been"][0].get("city"))

print_city(message="Hello", users_list=read_data_from_any_file("users.txt"))
