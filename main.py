import sys

import PyQt6.QtWebEngineWidgets
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QApplication, QHeaderView, QTableWidgetItem
from form import Ui_MainWindow

import gen_markdown


class mywindow(QtWidgets.QMainWindow):

    horParams = []
    horHeaders = ["Список вопросов"]
    gen = gen_markdown.generator()

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.installEventFilter(self)

        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch)

        self.ui.tableWidget.verticalHeader().setVisible(False)

        self.ui.tableWidget.doubleClicked.connect(
            self.tableItemClicked)

        self.ui.textEdit.setReadOnly(True)

        self.ui.AddAnswer.clicked.connect(self.AddAnswer)
        self.ui.Add.clicked.connect(self.Add)
        self.ui.generate.clicked.connect(self.generate)


    def tableItemClicked(self,e):
        selected_row = e.row()
        self.ui.Answer.setText(self.horParams.pop(selected_row))
        self.refreshTable()


    def generate(self):
        self.gen.add_report(self.ui.countVariants.value(),
                            self.ui.convertQestions.isChecked(),
                            self.ui.randomQestions.isChecked(),
                            self.ui.convertAnswer.isChecked(),
                            self.ui.count_q.value())
        f = open("all_list.html", "r")
        self.ui.webEngineView.setHtml(f.read())
        f.close()



    def Add(self):
        self.gen.add_note(
            self.ui.qestion.text(),
            self.horParams
        )
        self.ui.textEdit.setText(self.gen.code)

        self.horParams = []
        self.refreshTable()
        self.ui.qestion.setText("")
        self.ui.Answer.setText("")


    def AddAnswer(self):
        text = self.ui.Answer.text()
        self.horParams.append(text)
        self.refreshTable()


    def refreshTable(self):
        self.ui.tableWidget.setColumnCount(1)
        self.ui.tableWidget.setRowCount(len(self.horParams))

        for i in range(len(self.horParams)):
            self.set_table_item(i)

        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.setHorizontalHeaderLabels(self.horHeaders)



    def set_table_item(self, i):
        newitem = QTableWidgetItem(self.horParams[i])
        newitem.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.ui.tableWidget.setItem(i,0, newitem)


def main_func():
    app = QtWidgets.QApplication([])
    application = mywindow()

    application.show()
    app.installEventFilter(application)
    sys.exit(app.exec())

if __name__ == "__main__":
    main_func()
