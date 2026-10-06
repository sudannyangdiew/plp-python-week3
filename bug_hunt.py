count = 1
total = 0

# BUG: Missing colon at the end of the while loop line caused a SyntaxError.
# BUG: Off-by-one condition 'count < 5' excluded 5, summing to 10 instead of 15. Fixed to 'count <= 5'.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: String concatenation '+' with an integer total caused a TypeError. Replaced with an f-string.
print(f"Sum of 1 to 5 is: {total}")