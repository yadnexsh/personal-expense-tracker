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
        self.resize(500, 200)
        
        # Output / expense.json
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.root_dir = os.path.dirname(os.path.abspath(self.current_dir))
        self.output_dir = os.path.join(self.root_dir, "output")
        self.filename = "expenses.json"
        self.output_file_path = os.path.join(self.output_dir , self.filename)
        
        self.initUI()
        
    # ---------------- UI ----------------
    
    def initUI(self):
        
        self.main_layout = QVBoxLayout()
        self.vbox1 = QVBoxLayout()
        self.hbox1 = QHBoxLayout()
        
        # -------------- EXPENSE GROUP -------------
        
        self.expense_group = QGroupBox("Expense")
        self.expense_group_layout = QGridLayout()
        
        
        self.type_lbl = QLabel("Type")
        self.type_box = QComboBox()
        self.type_box.addItems(
            ["Foods", "Transportation", "Communication", "Entertainment", "Others"]
        )
        
        self.note_lbl = QLabel("Note")
        self.note_input = QLineEdit()
        self.note_input.setPlaceholderText("Description")
        
        self.amount_lbl = QLabel("Amount")
        self.amount = QLineEdit()
        self.amount.setPlaceholderText("Enter Final Amount")
        
        self.method_box_lbl = QLabel("Method")
        self.method_box = QComboBox()
        self.method_box.addItems(
            ["UPI", "Cash", "Credit Card", "Debit Card", "Others"]
        )
        
        self.expense_group_layout.addWidget(self.type_lbl, 0, 0)
        self.expense_group_layout.addWidget(self.type_box, 0, 1)
        
        self.expense_group_layout.addWidget(self.amount_lbl, 1, 0)
        self.expense_group_layout.addWidget(self.amount, 1, 1)
        
        self.expense_group_layout.addWidget(self.note_lbl, 2, 0)
        self.expense_group_layout.addWidget(self.note_input, 2, 1)
        
        self.expense_group_layout.addWidget(self.method_box_lbl, 3, 0)
        self.expense_group_layout.addWidget(self.method_box, 3, 1)
        
        self.expense_group.setLayout(self.expense_group_layout)
        
        # --------- DATE GROUP ------------
        
        self.date_group = QGroupBox("Date")
        self.date_layout = QGridLayout()
        
        self.date = QDateEdit()
        self.date.setDate(QDate.currentDate())
        self.date.setCalendarPopup(True)
        self.date.setAlignment(Qt.AlignCenter)
        
        current_date = QDate.currentDate()
        
        self.result_label = QLabel(
            "Selected Date- \n" + self.date.date().toString("dd/MM/yyyy")
        )
        
        self.current_date_label = QLabel(
            "Today's Date -\n" + current_date.toString("dd/MM/yyyy")
        )
        
        self.date.dateChanged.connect(self.update_date_label)
        
        self.date_layout.addWidget(self.current_date_label, 0, 0)
        self.date_layout.addWidget(self.result_label, 0, 1)
        self.date_layout.addWidget(self.date, 1, 0, 1, 2)
        
        self.date_group.setLayout(self.date_layout)
        
        # ----------- STATEMENT GROUP ---------------
        
        self.statement_group = QGroupBox("Statement")
        self.statement_layout = QVBoxLayout(self.statement_group)
        
        self.statement_lbl = QLabel("None")
        self.statement_layout.addWidget(self.statement_lbl)
        
        # ----------- ERROR GROUP  ---------------
        
        self.error_group = QGroupBox("Errors")
        self.error_layout = QVBoxLayout(self.error_group)
        
        self.error_lbl = QLabel("None")
        self.error_layout.addWidget(self.error_lbl)
        
        self.error_group.setHidden(True)
        
        # Submit Btn
        
        self.submit_btn = QPushButton("Submit")
        self.submit_btn.clicked.connect(self.save_entry)
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
        
    # ---------------- Date label update ----------------
    
    @Slot()
    def update_date_label(self, date_obj):
        formatted_date = date_obj.toString("dd/MM/yyyy")
        self.result_label.setText(f"Selected Date- \n {formatted_date}")
        
    # ---------------- Error behavior----------------
    
    @Slot()
    def update_error_label(self):
        self.error_group.setHidden(False)
        
        error = self.error_lbl.text()
        
        if not error:
            error = "None"
            
        self.error_lbl.setText(error)
        
    # ---------------- JSON save ----------------
    
    def save_expense(self, data):
        
        if not os.path.exists(self.output_file_path):
            with open(self.output_file_path, "w") as f:
                json.dump([], f)
                
        with open(self.output_file_path, "r") as f:
            expenses = json.load(f)
            
        expenses.append(data)
        
        with open(self.output_file_path, "w") as f:
            json.dump(expenses, f, indent=4)
            
            
    # ---------------- Submit logic ----------------
    
    @Slot()
    def save_entry(self):
        
        type_val = self.type_box.currentText()
        amount = self.amount.text()
        method = self.method_box.currentText()
        date_given = self.date.date().toString("dd/MM/yyyy")
        note = self.note_input.text() or "None"
        
        expense_data = {
            "type": type_val,
            "amount": amount,
            "note": note,
            "method": method,
            "date_given": date_given,
            "date_created": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        
        self.save_expense(expense_data)
        
        self.statement_lbl.setText(
            f"Type : {type_val} | Amount : {amount} | Method : {method}\n"
            f"Note : {note} | Date : {date_given}\n"
        )
        
        self.amount.clear()
        self.note_input.clear()
        
        
        
        
        
# ---------------- Run ----------------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme="dark_amber.xml")
    window = ExpenseWindow()
    window.show()
    sys.exit(app.exec())
