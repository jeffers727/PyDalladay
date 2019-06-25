from PyQt5.QtWidgets import *


def button_click():
    alert = QMessageBox()
    alert.setText("click.")
    alert.exec_()


def create_tab(tab, name):
    window = QWidget()
    tab.addTab(window, name)
    return window


def get_main_tab():
    layout_tab = QVBoxLayout()
    label = QLabel('Philipo')
    layout_tab.addWidget(label)
    return layout_tab


def get_second_tab():
    layout_tab = QVBoxLayout()
    button = QPushButton("click?")

    button.clicked.connect(button_click)
    layout_tab.addWidget(button)
    return layout_tab


app = QApplication([])

tab = QTabWidget()
tab.resize(300, 200)

# tab1
window1 = create_tab(tab, "tab1")
window1.setLayout(get_main_tab())

# tab2
window2 = create_tab(tab, "tab2")
window2.setLayout(get_second_tab())

tab.show()
app.exec_()
