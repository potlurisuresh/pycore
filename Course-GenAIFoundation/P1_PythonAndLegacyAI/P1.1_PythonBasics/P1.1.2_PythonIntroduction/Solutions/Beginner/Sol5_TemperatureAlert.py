"""
Solution: Beginner Assignment 5 - Temperature Alert

This solution demonstrates:
- Loop iteration over lists
- Type conversion with int()
- Counter variables
- Conditional logic inside loops
"""

# Input data
temps = ["29", "31", "27", "35", "30"]

# Step 1-4: Loop, convert, check, and count
hot_day_count = 0
hot_day_threshold = 30

print("Temperature Analysis:")
print("-" * 30)

for temp_str in temps:
    # Step 2: Convert string to integer
    temp = int(temp_str)
    
    # Step 3: Check if hot day
    if temp >= hot_day_threshold:
        hot_day_count += 1
        print("Day with temp {}°C: HOT ⚠️".format(temp))
    else:
        print("Day with temp {}°C: Normal".format(temp))

# Step 4: Print total hot days
print("-" * 30)
print("Total hot days (>= 30°C): {}".format(hot_day_count))

# Alternative approach - more concise
print("\n--- Alternative Approach ---")
temps_2 = ["29", "31", "27", "35", "30"]
hot_days = sum(1 for t in temps_2 if int(t) >= 30)
print("Result: {} hot days".format(hot_days))
