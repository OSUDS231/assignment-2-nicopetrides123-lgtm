initial_height = int(input("starting height of the plant in cm : "))
daily_growth = float(input("daily growth of the plant as a decimal eg 2% is 0.02 : "))
days = int(input("days to simulate : "))
boost_amount = float(input("how much the plant grows instantly every 7th day : "))

final_height = (initial_height * (1 + daily_growth)**days) + (boost_amount * (days // 7))

print(f'After {days} days (with a {boost_amount:.0f} cm boost every 7th day), the plant is {final_height:.2f} cm tall.')
