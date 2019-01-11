import pandas as pd

# read excel file
filename = "stat_104102.xlsx"
sheet_name = "Sheet0"
book = pd.read_excel(filename, sheet_name = sheet_name, header =2, skipfooter=2)
book = book.sort_values([2015], ascending = False)
print(book)
