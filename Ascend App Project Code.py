weekly_total_hours = 0
weekly_projects = 0
daily_hours = []


def calculate_progress(hours_completed, weekly_goal):
    percentage = (hours_completed / weekly_goal) * 100
    return percentage


welcome_message = "Welcome to the Study Tracker!"
print(welcome_message)

# Temporarily changed range from 1, 8 to 1, 3 for testing program
for day in range(1, 3):
    print("\n----- Day", day, "-----")

    hours_coded = int(input("\nEnter hours coded: "))
    hours_studied = int(input("\nEnter hours studied: "))
    projects_built = int(input("\nEnter amount of projects built: "))

    hours_worked = hours_coded + hours_studied

    weekly_total_hours += hours_worked
    weekly_projects += projects_built

    daily_hours.append(hours_worked)

    if hours_worked >= 2:
        print("Good work")
    else:
        print(
            "Insufficient hours. Code + study for at least 2 hours daily to stay on track!")


print("\n----- Weekly Summary: -----")

print("\n""Total weekly hours: ", weekly_total_hours)
print("Total projects built: ", weekly_projects)

if weekly_total_hours >= 30:
    print(
        "\n"f"Weekly Study Hours Goal Achieved! You studied {weekly_total_hours} hours this week. Great Work")
else:
    print(
        "\n"f"Weekly goal not achieved. You studied {weekly_total_hours} hours this week. Make sure to plan ahead next week to make up missed time in order to stay on track!")

if weekly_projects >= 5:
    print(
        f"\nWeekly Project Goal Achieved! You Created {weekly_projects} projects this week. Great Work")
else:
    print(
        f"\nWeekly Project Goal not achieved. You created {weekly_projects} this week")

print("\nDaily Hours: ", daily_hours)

best_hours = max(daily_hours)
best_day = daily_hours.index(best_hours) + 1

print("\nMost Productive Day: Day", best_day)

daily_average = sum(daily_hours) / len(daily_hours)

print("\nDaily average: ", sum(daily_hours) / len(daily_hours))

hours_goal_percentage = calculate_progress(weekly_total_hours, 30)

projects_goal_percentage = (weekly_projects / 5) * 100

print(f"\nWeekly Goal Completion: {hours_goal_percentage:.2f}%")
print(f"\nWeekly Projects Goal Completion: {weekly_projects:.2f}%")

if hours_goal_percentage <= 70:
    print("\nLet's improve next week!")

elif hours_goal_percentage <= 85:
    print("\nGreat week. Keep pushing and use the make-up function to allot time to make up for missed material this week!")

else:
    print("\nExcellent work! Keep building momentum!")

hours_missed = max(0, 30 - weekly_total_hours)

print(f"\nHours Missed: {hours_missed}")

if hours_missed == 0:
    print("No make-up hours needed! Goal achieved!")

else:
    print(f"You need to make up {hours_missed} hours next week.")

if hours_missed > 0:
    makeup_days = int(
        input("How many days will you use to make up missed hours? "))

    if makeup_days > 0:
        hours_per_day = hours_missed / makeup_days

        print(
            f"\nAdd {hours_per_day:.2f} extra hours per day for {makeup_days} days.")

    else:
        print("Please enter at least 1 day.")
