plant1 = "Wheat"
plant1_likes_sun = True
plant1_water_amount = 2
plant1_likes_wind = False

plant2 = "Apple"
plant2_likes_sun = True
plant2_water_amount = 3
plant2_likes_wind = True

plant3 = "Peace Lily"
plant3_likes_sun = False
plant3_water_amount = 1
plant3_likes_wind = False

user_input = input("How is the weather to day?\ninput format: Hot/Rainy number Windy/No wind\nFor example: Hot 0 Windy\n").lower().split()
rain = True if user_input[0] == "rainy" else False
water_amount = int(user_input[1])
windy = True if user_input[2] == "windy" else False
if rain:
    print(f"{plant1} and {plant2} like rain")
else:
    print(f"{plant3} doesn't like rain")

if water_amount < 2:
    print(f"{plant3} like this amount of water")
elif water_amount > 1 and water_amount < 3:
    print(f"{plant1} like this amount of water")
else:
    print(f"{plant2} like this amount of water")

if windy:
    print(f"{plant2} likes wind")
else:
    print(f"{plant1} and {plant3} doesn't like wind")

plant1_snow_amount = 2
plant2_snow_amount = 10
plant3_snow_amount = 1
snow_amount = int(input("How many inches of snow?\n"))
if snow_amount > plant1_snow_amount:
    print(f"{plant2} died from snow")
if snow_amount > plant2_snow_amount:
    print(f"{plant2} died from snow")
if snow_amount > plant3_snow_amount:
    print(f"{plant3} died from snow")