import requests
import json
import urllib
import pandas as pd
import io

# from geopy.geocoders import Nominatim

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib as plt

df2 = pd.read_csv(
    "C:/Users/LENOVO/Desktop/Downloads/cleaned.csv",
    low_memory=False,
)

# df2.insert("lat" , "lng", True)
# df.insert(2, "Age", [21, 23, 24, 21], True)
# df2


for i, row in df2.iterrows():
    apiAddress = (
        str(df2.at[i, "geo_type"])
        + ","
        + str(df2.at[i, "region"])
        + ","
        + str(df2.at[i, "transportation_type"])
        + ","
        + str(df2.at[i, "alternative_name"])
        + ","
        + str(df2.at[i, "sub-region"])
        + ","
        + str(df2.at[i, "country"])
    )
    # str(df2.at[i,'region']) + ',' + str(df2.at[i,'sub-region']) + ',' + str(df2.at[i,'country'])
    # print(apiAddress)

    parameters = {
        "key": "xUmR2JrvU751oE9cChNpQBKEf6RvDcyR",
        # "key" : "0Q5LG1er5VP4TnW3s9MK8pn3xxrAUI3D",
        "locations": apiAddress,
    }

    response = requests.get(
        "https://www.mapquestapi.com/geocoding/v1/address", params=parameters
    )

    data = json.loads(response.text)["results"]

    lat = (data[0]["locations"][0]["latLng"]["lat"])

    lng = (data[0]["locations"][0]["latLng"]["lng"])
    df2.at[i, "lat"] = lat
    df2.at[i, "lng"] = lng
    # print(df2)
    df2.to_csv("Geocod.csv")
