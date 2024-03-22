# Original list of guests
guests = ['Arthur Morgan', 'John Marston', 'Bruce Wayne']

# Print a message indicating only two people can be invited for dinner
print("Sorry, we can only invite two people for dinner.")

# Remove guests from the list until only two names remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, but we can't invite you to dinner.")

# Print a message to each of the two remaining guests, letting them know they're still invited
for guest in guests:
    print(f"Dear {guest},\nYou're still invited to the dinner. Please join us!\n")

# Use del to remove the last two names from the list
del guests[:]

# Print the list to make sure it's empty
print("Guest list after removing the last two names:", guests)
