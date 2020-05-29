import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport

PATH_TO_FILE = "PATH TO THE XLSX file"
FINAL_FILE_NAME = "acaps-dataset"
FINAL_HTML_PATH = "../webpages/" + FINAL_FILE_NAME + ".html"

df = pd.ExcelFile(PATH_TO_FILE)
df1 = pd.read_excel(df,"Database")
profile = ProfileReport(df1, title=FINAL_FILE_NAME, explorative=True)
profile.to_file(FINAL_HTML_PATH)
