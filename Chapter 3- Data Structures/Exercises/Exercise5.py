# Original list of guests
guests = ["Arthur Morgan", "John Marston", "Peter Parker"]

# Print a message stating the guest who can't make it
guest_cant_make_it = 'Peter Parker'
print(f"Unfortunately, {guest_cant_make_it} can't make it to the dinner.")

# Modify the list to replace the guest who can't make it with a new guest
new_guest = 'Bruce Wayne'
guests.remove(guest_cant_make_it)
guests.append(new_guest)

# Print a new set of invitation messages
for guest in guests:
    print(f"Dear {guest},\nYou are invited to the dinner. Please join us!\n")

print("New invitations have been sent out successfully.")
