import sys
from PySide6.QtWidgets import(
    QMainWindow, QWidget, QApplication, QVBoxLayout,
    QHBoxLayout, QLabel, QPushButton, QDockWidget, QListWidget,
    QProgressBar, QTabWidget, QToolButton, QTreeView, QGroupBox, QLineEdit, QGridLayout, QComboBox
    
)
from PySide6.QtCore import Slot , Qt , QSize
from PySide6.QtGui import QIcon , QStandardItem, QStandardItemModel


import os


class ExpenseWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Track Expense")
        self.initUI()
        
    def initUI(self):
        self.layout = QHBoxLayout()

        self.groupbox = QGroupBox("Expense")
        self.groupbox_layout = QGridLayout()
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

        self.groupbox_layout.addWidget(self.type_lbl, 0,0)
        self.groupbox_layout.addWidget(self.type_box, 0,1)
        
        
        self.groupbox_layout.addWidget(self.amount_lbl, 1,0)
        self.groupbox_layout.addWidget(self.amount, 1,1)
        
        self.groupbox_layout.addWidget(self.note_lbl, 2,0)
        self.groupbox_layout.addWidget(self.note_input, 2,1)
        
        self.groupbox_layout.addWidget(self.payment_lbl, 3,0)
        self.groupbox_layout.addWidget(self.payment_box, 3,1)
        
        self.groupbox_layout.addWidget(self.submit_btn, 4 , 1 , 1 , 1)
        self.groupbox.setLayout(self.groupbox_layout)
        
        self.layout.addWidget(self.groupbox)
        self.setLayout(self.layout)
        
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseWindow()
    window.show()
    sys.exit(app.exec())