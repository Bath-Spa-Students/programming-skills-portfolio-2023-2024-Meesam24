# List of places to visit
places_to_visit = ['Longyearbyen', 'Bath', 'Michigan', 'British Columbia', 'Alaska']

# Print the list in its original order
print("Original order:", places_to_visit)

# Print the list in alphabetical order using sorted() without modifying the original list
print("Sorted in alphabetical order:", sorted(places_to_visit))

# Print the list to show it's still in its original order
print("Original order after sorted():", places_to_visit)

# Print the list in reverse alphabetical order using sorted() without modifying the original list
print("Sorted in reverse alphabetical order:", sorted(places_to_visit, reverse=True))

# Print the list to show it's still in its original order
print("Original order after sorted() in reverse:", places_to_visit)

# Change the order of the list using reverse() and print it
places_to_visit.reverse()
print("Reversed order:", places_to_visit)

# Change the order of the list again using reverse() to revert to the original order and print it
places_to_visit.reverse()
print("Reverted back to original order:", places_to_visit)

# Change the order of the list using sort() to store it in alphabetical order and print it
places_to_visit.sort()
print("Sorted in alphabetical order using sort():", places_to_visit)

# Change the order of the list using sort() to store it in reverse alphabetical order and print it
places_to_visit.sort(reverse=True)
print("Sorted in reverse alphabetical order using sort():", places_to_visit)
