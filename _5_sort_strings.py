def sort_list_of_strings(strings):
    sorted_strings = sorted(strings, key=lambda x: x.lower())
    return sorted_strings

# Example usage
strings = ["Apple", "banana", "cat", "Dog", "Elephant"]
sorted_strings = sort_list_of_strings(strings)
print(sorted_strings)