import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport
df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv", error_bad_lines=False)
profile = ProfileReport(df, title='Pandas Profiling Report', explorative=True)
profile.to_file("../webpages/owiddataset.html")
