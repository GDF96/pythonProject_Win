# string join
week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

print(",".join(week_days[1:4])) # instead of ',', also before join is possible: '\n' for next row or adding a text "goes into"

print ( )

print("\n".join(week_days))

print ( )

for day in week_days:
    print(day)

print ( )

for day in week_days:
    print(day, "*", sep="-")

print ( )

for day in week_days:
    print(day, "*", sep="-", end="")