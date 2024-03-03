total_money = 50  # Total money in pounds
usb_stick_price = 6  # Price of each USB stick in pounds

# Calculate how many USB sticks she can buy
num_usb_sticks = total_money // usb_stick_price

# Calculate how much money she will have left
money_left = total_money % usb_stick_price

# Print the results
print("She can buy", num_usb_sticks, "USB sticks.")
print("She will have £", money_left, "left.")
