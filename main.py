import sys
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView, QApplication
from MainWindow import Ui_MainWindow


def get_items():
    con = sqlite3.connect("coffee.sqlite")

    cur = con.cursor()

    result = cur.execute("""
    SELECT * FROM coffee
    """).fetchall()

    print(len(result))

    con.close()
    return result

#change
class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.update_result()

    def update_result(self):
        items = get_items()
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setRowCount(len(items))
        parse_data = items
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'название сорта', 'степень обжарки', 'молотый', 'описание вкуса', 'цена',
             'объем упаковки'])
        for i, elem in enumerate(parse_data):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
