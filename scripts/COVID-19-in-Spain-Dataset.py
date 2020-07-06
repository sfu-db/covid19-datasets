import pandas as pd
from pandas_profiling import ProfileReport

### File 1/9: nacional_covid19.csv ###

PATH_TO_FILE = "nacional_covid19.csv"
FINAL_FILE_NAME = "nacional_covid19"
FINAL_HTML_PATH = "../webpages/COVID-19-in-Spain-Dataset/" + FINAL_FILE_NAME + ".html"

df1 = pd.read_csv(PATH_TO_FILE, error_bad_lines=False)
print(df1.info())
profile = ProfileReport(df1, title=FINAL_FILE_NAME, explorative=True)
profile.to_file(FINAL_HTML_PATH)

### File 2/9: nacional_covid19_rango_edad.csv ###

PATH_TO_FILE = "nacional_covid19_rango_edad.csv"
FINAL_FILE_NAME = "nacional_covid19_rango_edad"
FINAL_HTML_PATH = "../webpages/COVID-19-in-Spain-Dataset/" + FINAL_FILE_NAME + ".html"

df2 = pd.read_csv(PATH_TO_FILE, error_bad_lines=False)
print(df2.info())
profile = ProfileReport(df2, title=FINAL_FILE_NAME, explorative=True)
profile.to_file(FINAL_HTML_PATH)

### File 3/9: ccaa_camas_uci_2017.csv ###

PATH_TO_FILE = "ccaa_camas_uci_2017.csv"
FINAL_FILE_NAME = "ccaa_camas_uci_2017"
FINAL_HTML_PATH = "../webpages/COVID-19-in-Spain-Dataset/" + FINAL_FILE_NAME + ".html"

df3 = pd.read_csv(PATH_TO_FILE, error_bad_lines=False)
print(df3.info())
profile = ProfileReport(df3, title=FINAL_FILE_NAME, explorative=True)
profile.to_file(FINAL_HTML_PATH)

### File 4/9: ccaa_covid19_altas_long.csv ###

PATH_TO_FILE = "ccaa_covid19_altas_long.csv"
FINAL_FILE_NAME = "ccaa_covid19_altas_long"
FINAL_HTML_PATH = "../webpages/COVID-19-in-Spain-Dataset/" + FINAL_FILE_NAME + ".html"

df4 = pd.read_csv(PATH_TO_FILE, error_bad_lines=False)
print(df4.info())
profile = ProfileReport(df4, title=FINAL_FILE_NAME, explorative=True)
profile.to_file(FINAL_HTML_PATH)

### File 5/9: ccaa_covid19_casos_long.csv ###

PATH_TO_FILE = "ccaa_covid19_casos_long.csv"
FINAL_FILE_NAME = "ccaa_covid19_casos_long"
FINAL_HTML_PATH = "../webpages/COVID-19-in-Spain-Dataset/" + FINAL_FILE_NAME + ".html"

df5 = pd.read_csv(PATH_TO_FILE, error_bad_lines=False)
print(df5.info())
profile = ProfileReport(df5, title=FINAL_FILE_NAME, explorative=True)
profile.to_file(FINAL_HTML_PATH)

### File 6/9: ccaa_covid19_fallecidos_long.csv ###

PATH_TO_FILE = "ccaa_covid19_fallecidos_long.csv"
FINAL_FILE_NAME = "ccaa_covid19_fallecidos_long"
FINAL_HTML_PATH = "../webpages/COVID-19-in-Spain-Dataset/" + FINAL_FILE_NAME + ".html"

df6 = pd.read_csv(PATH_TO_FILE, error_bad_lines=False)
print(df6.info())
profile = ProfileReport(df6, title=FINAL_FILE_NAME, explorative=True)
profile.to_file(FINAL_HTML_PATH)

### File 7/9: ccaa_covid19_hospitalizados_long.csv ###

PATH_TO_FILE = "ccaa_covid19_hospitalizados_long.csv"
FINAL_FILE_NAME = "ccaa_covid19_hospitalizados_long"
FINAL_HTML_PATH = "../webpages/COVID-19-in-Spain-Dataset/" + FINAL_FILE_NAME + ".html"

df7 = pd.read_csv(PATH_TO_FILE, error_bad_lines=False)
print(df7.info())
profile = ProfileReport(df7, title=FINAL_FILE_NAME, explorative=True)
profile.to_file(FINAL_HTML_PATH)

### File 8/9: ccaa_covid19_mascarillas.csv ###

PATH_TO_FILE = "ccaa_covid19_mascarillas.csv"
FINAL_FILE_NAME = "ccaa_covid19_mascarillas"
FINAL_HTML_PATH = "../webpages/COVID-19-in-Spain-Dataset/" + FINAL_FILE_NAME + ".html"

df8 = pd.read_csv(PATH_TO_FILE, error_bad_lines=False)
print(df8.info())
profile = ProfileReport(df8, title=FINAL_FILE_NAME, explorative=True)
profile.to_file(FINAL_HTML_PATH)

### File 9/9: ccaa_covid19_uci_long ###

PATH_TO_FILE = "ccaa_covid19_uci_long.csv"
FINAL_FILE_NAME = "ccaa_covid19_uci_long"
FINAL_HTML_PATH = "../webpages/COVID-19-in-Spain-Dataset/" + FINAL_FILE_NAME + ".html"

df9 = pd.read_csv(PATH_TO_FILE, error_bad_lines=False)
print(df9.info())
profile = ProfileReport(df9, title=FINAL_FILE_NAME, explorative=True)
profile.to_file(FINAL_HTML_PATH)