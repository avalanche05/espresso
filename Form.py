# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(328, 581)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.id = QtWidgets.QLineEdit(Form)
        self.id.setObjectName("id")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.id)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.title = QtWidgets.QLineEdit(Form)
        self.title.setObjectName("title")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.title)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.roasting = QtWidgets.QLineEdit(Form)
        self.roasting.setObjectName("roasting")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.roasting)
        self.is_ground = QtWidgets.QRadioButton(Form)
        self.is_ground.setObjectName("is_ground")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.is_ground)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.description = QtWidgets.QPlainTextEdit(Form)
        self.description.setObjectName("description")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.description)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.price = QtWidgets.QLineEdit(Form)
        self.price.setObjectName("price")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.price)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.volume = QtWidgets.QLineEdit(Form)
        self.volume.setObjectName("volume")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.volume)
        self.saveButton = QtWidgets.QPushButton(Form)
        self.saveButton.setObjectName("saveButton")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.SpanningRole, self.saveButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Новый сорт"))
        self.label.setText(_translate("Form", "ID"))
        self.label_2.setText(_translate("Form", "Название сорта"))
        self.label_3.setText(_translate("Form", "Степень обжарки"))
        self.is_ground.setText(_translate("Form", "молотый"))
        self.label_4.setText(_translate("Form", "Описание вкуса"))
        self.label_5.setText(_translate("Form", "Цена"))
        self.label_6.setText(_translate("Form", "Объём упаковки"))
        self.saveButton.setText(_translate("Form", "Сохранить"))
