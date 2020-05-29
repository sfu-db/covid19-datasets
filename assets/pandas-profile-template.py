import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport

PATH_TO_FILE = "PATH to your csv file (Preferably a URL from the internet)"
FINAL_FILE_NAME = "Name of your dataset"
FINAL_HTML_PATH = "../webpages/" + FINAL_FILE_NAME + ".html"

df = pd.read_csv(PATH_TO_FILE, error_bad_lines=False)
profile = ProfileReport(df, title=FINAL_FILE_NAME, explorative=True)
profile.to_file("../webpages/owiddataset.html")
