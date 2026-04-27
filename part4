initial_height = float(input("initial_height : "))
daily_growth = float(input("daily_growth : "))
target_height = float(input("target_height : "))
days = int(input("days : "))
boost_amount = float(input("boost_amount : "))

best_interval = -1


for interval in range(days, 0, -1):
    current_height = initial_height


    for d in range(1, days + 1):
        current_height *= (1 + daily_growth)
        if d % interval == 0:
            current_height += boost_amount

    if current_height >= target_height:
        best_interval = interval
        break

if best_interval != -1:
    print(
        f"To reach at least {target_height:.0f} cm in {days} days, apply a {boost_amount:.1f} cm boost every {best_interval} days.")
else:
    print(f"Target height not achievable within {days} days, even with daily boosts.")
