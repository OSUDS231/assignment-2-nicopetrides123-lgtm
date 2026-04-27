initial_height = float(input("starting height of the plant in cm : "))
daily_growth = float(input("daily growth of the plant as a decimal eg 2% is 0.02 : "))
target_height = float(input("target height of the plant in cm : "))
boost_amount = float(input("how much the plant grows instantly every 7th day : "))
current_height = float(initial_height)
days = 0

while current_height < target_height:
    days += 1
    current_height *= (1 + daily_growth)

    if days % 7 == 0:
        current_height += boost_amount

print( f'After {days} days (with a {boost_amount:.1f} cm boost every 7th day), the plant reaches at least {target_height:.0f} cm.')
