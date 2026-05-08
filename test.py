from PySide6.QtCore import QDate, Qt

# Get current date
date = QDate.currentDate()

# Formats
print(date.toString(Qt.DateFormat.ISODate))  # 2023-10-27
print(date.toString("dd/MM/yyyy"))         # 27/10/2023
print(date.toString("dddd, MMMM d, yyyy")) # Friday, October 27, 2023
