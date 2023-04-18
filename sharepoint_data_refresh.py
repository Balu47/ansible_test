# Importing modules
import win32com.client
import time

# Opening Excel software using the win32com
File = win32com.client.Dispatch("Excel.Application")

# Opening workbook
Workbook = File.Workbooks.open("salesforce_data.xlsx")

# Refeshing all the shests
Workbook.RefreshAll()

# waiting for 1 min
time.sleep(60)

# Saving the Workbook
Workbook.Save()

# Closing the Excel File
File.Quit()
