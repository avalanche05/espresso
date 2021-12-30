import sys
import sqlite3

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView, QApplication, QWidget, \
    QDialog
from MainWindow import Ui_MainWindow
from Form import Ui_Form

COLUMNS = ['id', 'title', 'roasting', 'ground', 'description', 'price', 'volume']


def add_item(values):
    con = sqlite3.connect("coffee.sqlite")

    cur = con.cursor()

    for i in range(len(values)):
        if type(values[i]) is str:
            values[i] = f'"{values[i]}"'
        else:
            values[i] = str(values[i])

    values = ', '.join(values)
    cur.execute(f"""
        INSERT INTO coffee(title,roasting ,ground,description,price, volume)
         VALUES({values})
        """).fetchall()
    con.commit()
    con.close()


def get_items():
    con = sqlite3.connect("coffee.sqlite")

    cur = con.cursor()

    result = cur.execute("""
    SELECT * FROM coffee
    """).fetchall()

    con.close()
    return result


def modify_table(id_, column, value):
    con = sqlite3.connect("coffee.sqlite")

    cur = con.cursor()

    if type(value) is str:
        value = f"'{value}'"
    else:
        value = str(value)

    cur.execute(f"""
        UPDATE coffee
        SET {column} = {value}
        WHERE id = {id_}
        """).fetchall()

    con.commit()
    con.close()


class Form(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.saveButton.clicked.connect(self.run)

    def run(self):
        try:
            title = self.title.text()
            roasting = int(self.roasting.text())
            ground = int(self.is_ground.isChecked())
            description = self.description.toPlainText()
            price = int(self.price.text())
            volume = int(self.price.text())

            add_item([title, roasting, ground, description, price, volume])

            self.close()
        except Exception as e:
            print(e)
            print('Ошибка. Введённые данные некорректны.')


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.update_result()
        self.form = Form()

        self.pushButton.clicked.connect(self.start_form)
        self.tableWidget.itemChanged.connect(self.item_changed)

    def start_form(self):
        self.form.setWindowModality(Qt.ApplicationModal)
        self.form.exec_()
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

    def item_changed(self):
        row = self.tableWidget.currentRow()
        col = self.tableWidget.currentColumn()
        value = self.tableWidget.currentItem().text()

        if col == COLUMNS.index('id') and value != str(row + 1):
            self.statusBar().showMessage('Менять ID запрещено', 2000)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(row + 1)))
            return
        elif col == COLUMNS.index('id'):
            return
        modify_table(row + 1, COLUMNS[col], value)
        self.statusBar().showMessage('База данных обновлена', 2000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
