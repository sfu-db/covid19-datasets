import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport

PATH_TO_FILE = "https://data.humdata.org/dataset/e1a91ae0-292d-4434-bc75-bf863d4608ba/resource/e53c0034-a320-450f-aaeb-0e476f462464/download/acaps-_covid19_government_measures_dataset.xlsx"
FINAL_FILE_NAME = "acaps-dataset"
FINAL_HTML_PATH = "../webpages/" + FINAL_FILE_NAME + ".html"

df = pd.ExcelFile(PATH_TO_FILE)
df1 = pd.read_excel(df,"Database")
profile = ProfileReport(df1, title=FINAL_FILE_NAME, explorative=True)
profile.to_file(FINAL_HTML_PATH)
