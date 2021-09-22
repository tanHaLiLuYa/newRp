import akshare as ak
import pandas as pd

covid_19_area_search_df = ak.covid_19_area_search(province="四川省", city="成都市",district="金牛区")
print(covid_19_area_search_df)