# 16 - Minutes to Hours and Minutes
# Breaks total minutes into hours + leftover minutes.

total_minutes = 275

hours = total_minutes // 60
minutes = total_minutes % 60

print(f"{total_minutes} minutes = {hours} hour(s) and {minutes} minute(s)")
