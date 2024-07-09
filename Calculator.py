import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Simple Calculator')
        self.setGeometry(550, 270, 300, 400)
        self.current_input = ''
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.display = QLabel('0')
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.display.setFixedHeight(50)
        self.display.setStyleSheet("border: 1px solid black; font-size = 24 px;")
        self.layout.addWidget(self.display)
        self.setLayout(self.layout)
        buttons = [
            [('7', self.add_to_input), ('8', self.add_to_input), ('9', self.add_to_input), ('/', self.add_to_input)],
            [('4', self.add_to_input), ('5', self.add_to_input), ('6', self.add_to_input), ('*', self.add_to_input)],
            [('1', self.add_to_input), ('2', self.add_to_input), ('3', self.add_to_input), ('-', self.add_to_input)],
            [('0', self.add_to_input), ('C', self.clear_input), ('=', self.calculate_result), ('+', self.add_to_input)],
        ]
        for row in buttons:
            hbox = QHBoxLayout()
            for text, method in row:
                button = QPushButton(text)
                button.setFixedSize(60,60)
                button.setStyleSheet("font-size = 18 px")
                button.clicked.connect(method)
                hbox.addWidget(button)
            self.layout.addLayout(hbox)
        self.setLayout(self.layout)
    def add_to_input(self):
        button_pressed = self.sender()
        self.current_input += button_pressed.text()
        self.display.setText(self.current_input)
    def clear_input(self):
        self.current_input = '0'
        self.display.setText(self.current_input)
    def calculate_result(self):
        try:
            result = eval(self.current_input)
            self.display.setText(str(result))
            self.current_input = str(result)
        except Exception as e:
            self.display.setText('Error')
            self.current_input = '0'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())
