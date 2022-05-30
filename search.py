import pandas

data = pandas.read_csv("gyms.csv")


def search():
    max_price_gym = int(input("Choose a max gym price: "))
    low_price_gym = int(input("Choose a low gym price: "))
    final_price = data[(data.Price >= low_price_gym) & (data.Price <= max_price_gym)]
    print(final_price)

    area = input("What location are you after?: ")
    area_results = (data.loc[data.Location == area])
    print(area_results)

    user_type = input("What type of gym are you after? Bodybuilding, Powerlifitng, Crossfit or Commercial?: ")
    type_results = (data.loc[data.Type == user_type])
    print(type_results)

    matches = (data.Price >= low_price_gym) & (data.Price <= max_price_gym)
    matches &= data.Location == area
    matches &= data.Type == user_type

    data[matches].to_csv("Final.csv")


search()
