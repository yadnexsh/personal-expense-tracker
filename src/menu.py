import sys
import os
import json
from datetime import datetime


from PySide6.QtWidgets import (
    QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QGroupBox, QLineEdit, QGridLayout,
    QComboBox, QDateEdit
)


from PySide6.QtCore import Slot, Qt, QDate
from qt_material import apply_stylesheet



class ExpenseWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Track Expense")
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
        
        self.payment_lbl = QLabel("Payment Type")
        self.payment_box = QComboBox()
        self.payment_box.addItems(["UPI", "Cash", "Credit Card", "Debit Card", "Others"])

        self.expense_group_layout.addWidget(self.type_lbl, 0,0)
        self.expense_group_layout.addWidget(self.type_box, 0,1)
        
        
        self.expense_group_layout.addWidget(self.amount_lbl, 1,0)
        self.expense_group_layout.addWidget(self.amount, 1,1)
        
        self.expense_group_layout.addWidget(self.note_lbl, 2,0)
        self.expense_group_layout.addWidget(self.note_input, 2,1)
        
        self.expense_group_layout.addWidget(self.payment_lbl, 3,0)
        self.expense_group_layout.addWidget(self.payment_box, 3,1)
        
        self.expense_group.setLayout(self.expense_group_layout)
        
        
        # --------- DATE GROUP ------------
        
        self.date_group = QGroupBox("Date")
        
        self.date_layout = QVBoxLayout()
        self.date_group.setLayout(self.date_layout)
        
        self.date = QDateEdit()
        self.date.setDate(QDate.currentDate())
        self.date.setCalendarPopup(True) 
        
        current_date = QDate.currentDate()
        self.result_label = QLabel('Selected Date: ' + self.date.date().toString("dd/MM/yyyy"))
        self.current_date_label = QLabel(f"Today's Date:" + current_date.toString("dd/MM/yyyy"))
        
        
        self.date_layout.addWidget(self.current_date_label)
        self.date_layout.addWidget(self.date)
        self.date_layout.addWidget(self.result_label)
        self.date_layout.setAlignment(Qt.AlignCenter)
        
        
        # ----------- LAYOUT -----------------
        
        self.hbox1.addWidget(self.expense_group)
        self.hbox1.addWidget(self.date_group)
        
        self.vbox1.addLayout(self.hbox1)
        
        self.main_layout.addLayout(self.vbox1)
        self.main_layout.addWidget(self.submit_btn)
        
        
        self.setLayout(self.main_layout)
        
        
        self.date.dateChanged.connect(self.update_label)
        
    def update_label(self, date_obj):
        """Updates the label text when the date is changed."""
        formatted_date = date_obj.toString(Qt.DateFormat.ISODate)
        self.result_label.setText(f'Selected Date: {formatted_date}')
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseWindow()
    window.show()
    sys.exit(app.exec())
