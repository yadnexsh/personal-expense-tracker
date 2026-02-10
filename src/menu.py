import sys
from PySide6.QtWidgets import(
    QMainWindow, QWidget, QApplication, QVBoxLayout,
    QHBoxLayout, QLabel, QPushButton, QDockWidget, QListWidget,
    QProgressBar, QTabWidget, QToolButton, QTreeView, QGroupBox, QLineEdit, QGridLayout, QComboBox, QDateEdit
    
)

from qt_material import apply_stylesheet

from PySide6.QtCore import Slot , Qt , QSize, QDate
from PySide6.QtGui import QIcon , QStandardItem, QStandardItemModel


import os


class ExpenseWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Track Expense")
        self.resize(500,200)
        self.initUI()
        
    def initUI(self):
        self.main_layout = QVBoxLayout()
        self.vbox1 = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        

        # -------------- EXPENSE GROUP -------------
        
        self.expense_group = QGroupBox("Expense")
        self.expense_group_layout = QGridLayout()
        
        self.submit_btn = QPushButton("Submit")
        
        self.type_lbl = QLabel("Type")
        self.type_box = QComboBox()
        self.type_box.addItems(["Foods", "Transportation", "Communication", "Entertainment", "Others"])
        
        self.note_lbl = QLabel("Note")
        self.note_input = QLineEdit()
        self.note_input.setPlaceholderText("Description")
        
        self.amount_lbl = QLabel("Amount")
        self.amount = QLineEdit()
        self.amount.setPlaceholderText("Enter Final Amount")
        
        self.method_box_lbl = QLabel("Method")
        self.method_box = QComboBox()
        self.method_box.addItems(["UPI", "Cash", "Credit Card", "Debit Card", "Others"])

        self.expense_group_layout.addWidget(self.type_lbl, 0,0)
        self.expense_group_layout.addWidget(self.type_box, 0,1)
        
        
        self.expense_group_layout.addWidget(self.amount_lbl, 1,0)
        self.expense_group_layout.addWidget(self.amount, 1,1)
        
        self.expense_group_layout.addWidget(self.note_lbl, 2,0)
        self.expense_group_layout.addWidget(self.note_input, 2,1)
        
        self.expense_group_layout.addWidget(self.method_box_lbl, 3,0)
        self.expense_group_layout.addWidget(self.method_box, 3,1)
        
        self.expense_group.setLayout(self.expense_group_layout)
        # self.expense_group.resize(100 , 50)
        # text = self.type_box.item
        
        # --------- DATE GROUP ------------
        
        self.date_group = QGroupBox("Date")
        
        self.date_layout = QGridLayout()
        self.date_group.setLayout(self.date_layout)
        
        self.date = QDateEdit()
        self.date.setDate(QDate.currentDate())
        self.date.setCalendarPopup(True) 
        self.date.setAlignment(Qt.AlignCenter)
        
        current_date = QDate.currentDate()
        self.result_label = QLabel("Selected Date- \n" + self.date.date().toString("dd/MM/yyyy"))
        self.current_date_label = QLabel(f"Today's Date -\n" + current_date.toString("dd/MM/yyyy"))
        
        self.date.dateChanged.connect(self.update_date_label)
        
        self.date_layout.addWidget(self.current_date_label, 0,0)
        self.date_layout.addWidget(self.result_label, 0,1)
        
        self.date_layout.addWidget(self.date, 1,0,1,2)
        self.date_layout.setAlignment(Qt.AlignCenter)
        
        # ----------- STATEMENT GROUP ---------------
        self.statement_group = QGroupBox("Statement")
        self.statement_layout = QVBoxLayout(self.statement_group)
        
        self.statement_lbl = QLabel("None")
        self.statement_layout.addWidget(self.statement_lbl)
        
        self.submit_btn.clicked.connect(self.update_statement_label)
        
        # ------------ ERROR GROUP -----------
        self.error_group = QGroupBox("Errors")
        self.error_layout = QVBoxLayout(self.error_group)
        
        self.error_lbl = QLabel("None")
        self.error_layout.addWidget(self.error_lbl)
        self.error_group.setHidden(True)
        
        self.submit_btn.clicked.connect(self.update_error_label)
        # ----------- LAYOUT -----------------
        
        self.hbox1.addWidget(self.expense_group, 3)
        self.hbox1.addWidget(self.date_group, 2)
        
        self.vbox1.addLayout(self.hbox1)
        
        self.main_layout.addLayout(self.vbox1)
        
        self.main_layout.addWidget(self.statement_group)
        self.main_layout.addWidget(self.error_group)
        
        self.main_layout.addWidget(self.submit_btn)
        
        
        self.setLayout(self.main_layout)
        
        
        
        
    @Slot()
    def update_date_label(self, date_obj):
        """Updates the label text when the date is changed."""
        formatted_date = date_obj.toString("dd/MM/yyyy")
        self.result_label.setText(f"Selected Date -\n {formatted_date}")
        
    @Slot()
    def update_error_label(self):
        """Updates the error text when the error occurs."""
        self.error_group.setHidden(False)
        error = self.error_lbl.text()
        
        if not error:
            error = "None"
            
        self.error_lbl.setText(f"{error}")
        
    @Slot()
    def update_statement_label(self):
        """Updates the statement text when the data is changed."""
        
        type = self.type_box.currentText()
        amount = self.amount.text()
        method = self.method_box.currentText()
        date = self.date.date().toString("dd/MM/yyyy")
        note = self.note_input.text()
        
        if not note:
            note = "None"
        
        if not amount:
            amount = "None"
            
        self.statement_lbl.setText(f"Type : {type} | Amount : {amount} | Method : {method}\nNote : {note} | Date : {date}\n")

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseWindow()
    apply_stylesheet(app, theme='dark_amber.xml')
    window.show()
    sys.exit(app.exec())