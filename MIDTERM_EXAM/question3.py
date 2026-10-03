import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
)
from PyQt6.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Midterm in OOP")
        self.setGeometry(100, 100, 450, 250)

        # Label: "Enter your fullname:"
        self.label_prompt = QLabel("Enter your fullname:", self)
        self.label_prompt.setGeometry(30, 50, 150, 30)
        self.label_prompt.setStyleSheet("color: red;")

        # Input Field: Entry for Full Name
        self.entry_fullname = QLineEdit(self)
        self.entry_fullname.setGeometry(200, 50, 200, 30)
        self.entry_fullname.setFont(QFont("Arial", 12))

        # Button: "Click to display your Fullname"
        self.btn_display = QPushButton("Click to display your Fullname", self)
        self.btn_display.setGeometry(30, 110, 160, 30)
        self.btn_display.setStyleSheet("color: red;")
        self.btn_display.clicked.connect(self.display_fullname)

        # Output Field: Read-only display line edit
        self.entry_output = QLineEdit(self)
        self.entry_output.setGeometry(200, 110, 200, 30)
        self.entry_output.setFont(QFont("Arial", 12))
        self.entry_output.setReadOnly(True)

    def display_fullname(self):
        # Transfer text from input box to output box
        text = self.entry_fullname.text()
        self.entry_output.setText(text)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())