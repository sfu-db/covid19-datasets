import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport

PATH_TO_FILE = "http://www.bccdc.ca/Health-Info-Site/Documents/BCCDC_COVID19_Dashboard_Case_Details.csv"
FINAL_FILE_NAME = "BC-COVID19"
FINAL_HTML_PATH = "../webpages/" + FINAL_FILE_NAME + ".html"

df = pd.read_csv(PATH_TO_FILE, error_bad_lines=False)
profile = ProfileReport(df, title=FINAL_FILE_NAME, explorative=True)
profile.to_file(FINAL_HTML_PATH)