def array_of_names(persons: dict) -> list:
    result = []
    for first_name, last_name in persons.items():
        # Capitalize the first letter of both first and last names
        full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
        result.append(full_name)
    return result

if __name__ == "__main__":
    # Example usage from the assignment description
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }
    print(array_of_names(persons))
