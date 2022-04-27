# import all necessary library:
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import csv
import os
import logging

logging.basicConfig(
    filename="LOGS.log",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
)


#class webscraperr:
    def wsc():
        logging.info("this is a start of my code and i am try to fetch data from web ")
        try:
            url = requests.get("https://covid19.apple.com/mobility.com")
            soup = BeautifulSoup(url.content, "html.parser")
            links = soup.find_all("a")
            all_links = []
            for link in links:
                all_links.append(link.get("href"))
                datalink = "https://covid19-static.cdn-apple.com/covid19-mobility-data/2211HotfixDev7/v3/en-us/applemobilitytrends-2022-03-31.csv"
                data = pd.read_csv(datalink, low_memory=False)

            # print(data)
            # Converting the result as dataframe and saving it as csv file
            def check_dir(directory):
                directory = os.path.dirname("D:\annapython proj")
                if not os.path.exists(directory):
                    os.makedirs(directory)
                    data_frame = pd.DataFrame(data)
                    data_frame.to_csv("final_output.csv")
                    df = pd.read_csv("final_output.csv")


            check_dir()
            logging.info("now it is successful")

        except Exception as e:
            logging.error("Errog has happend ")
            logging.exception("Exception occured " + str(e))
            print("data has not fetched:")

    wsc())