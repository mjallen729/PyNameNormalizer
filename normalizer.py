import re

# A name is considered normalized if it fits the regular expression below
regex = r'([A-Z][a-zA-Z]+) ([A-Z][a-zA-Z]+)'

def normalize(name_list: list[str], stripString: bool) -> list[list[str]]:
    normalized = list()
    unnormalized = list()

    for name in name_list:
        if stripString:
            name = name.strip()

        match = re.match(regex, name)
        
        if match:
            normalized.append(name)

        else:
            unnormalized.append(name)

    return [normalized, unnormalized]

if __name__ == '__main__':
    normalized_names = [
        "Alice Baker", "David Jones", "Emily Clark", "Robert Smith",
        "Michael Brown", "Sarah Garcia", "William Johnson", "Jennifer Miller",
        "Charles Williams", "Elizabeth Davis", "Matthew Lopez", "Laura Hernandez",
        "Christopher Lee", "Amanda Moore", "Richard Taylor", "Nicole Garcia",
        "Daniel Thomas", "Ashley Rodriguez", "Joseph Allen", "Evelyn King",
        "James Wright", "Katherine Garcia", "Andrew Hernandez", "Samantha Lopez",
        "Brian Moore"
    ]

    unnormalized_names = [
        "alice baker",  # lowercase
        "david",        # single name
        "Emily  Clark",  # extra space
        "Robert-Smith",  # hyphenated
        " Michael Brown",  # leading space
        "Sarah",         # single name
        " William Johnson",  # leading space
        "jennífer miller",  # non-ascii character
        "Charles",       # single name
        "Elizabeth123",  # alphanumeric characters
    ]

    all_names = normalized_names + unnormalized_names

    norm, unnorm = normalize(all_names)
    assert(len(norm) == len(normalized_names))
    assert(len(unnorm) == len(unnormalized_names))