# Part A: Grade Reporter

# Given scores
scores = [72, 45, 90, 61, 38]

# Initialize trackers for pass/fail counts and total sum
passes = 0
fails = 0
total_sum = 0

# Loop through each score to evaluate grades and accumulate statistics
for score in scores:
    # Add score to total sum for average calculation later
    total_sum += score

    # Determine grade and pass/fail status
    if score >= 80:
        grade = "A"
        passes += 1
    elif score >= 70:
        grade = "B"
        passes += 1
    elif score >= 50:
        grade = "C"
        passes += 1
    else:
        grade = "F"
        fails += 1

    # Print score with its grade
    print(f"Score: {score} -> Grade: {grade}")

# Calculate average
average = total_sum / len(scores)

# Display summary statistics
print("\n--- Summary ---")
print(f"Passed: {passes}")
print(f"Failed: {fails}")
print(f"Average score: {round(average, 1)}")