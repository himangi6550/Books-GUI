# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'm6.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Form(object):
    pr=0
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(417, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lb1 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lb1.setFont(font)
        self.lb1.setObjectName("lb1")
        self.horizontalLayout.addWidget(self.lb1)
        self.t1 = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setItalic(True)
        self.t1.setFont(font)
        self.t1.setObjectName("t1")
        self.horizontalLayout.addWidget(self.t1)
        self.pb1 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pb1.setFont(font)
        self.pb1.setObjectName("pb1")
        self.horizontalLayout.addWidget(self.pb1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.t2 = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setItalic(True)
        self.t2.setFont(font)
        self.t2.setObjectName("t2")
        self.verticalLayout.addWidget(self.t2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lb2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb2.setFont(font)
        self.lb2.setObjectName("lb2")
        self.horizontalLayout_3.addWidget(self.lb2)
        self.t3 = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setItalic(True)
        self.t3.setFont(font)
        self.t3.setObjectName("t3")
        self.horizontalLayout_3.addWidget(self.t3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lb3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb3.setFont(font)
        self.lb3.setObjectName("lb3")
        self.horizontalLayout_2.addWidget(self.lb3)
        self.t4 = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setItalic(True)
        self.t4.setFont(font)
        self.t4.setObjectName("t4")
        self.horizontalLayout_2.addWidget(self.t4)
        self.pb2 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pb2.setFont(font)
        self.pb2.setObjectName("pb2")
        self.horizontalLayout_2.addWidget(self.pb2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lb4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb4.setFont(font)
        self.lb4.setObjectName("lb4")
        self.horizontalLayout_4.addWidget(self.lb4)
        self.t5 = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setItalic(True)
        self.t5.setFont(font)
        self.t5.setObjectName("t5")
        self.horizontalLayout_4.addWidget(self.t5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.pb1.clicked.connect(self.btn1)
        self.pb2.clicked.connect(self.btn2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lb1.setText(_translate("Form", "Book Title: "))
        self.pb1.setText(_translate("Form", "Find Price"))
        self.lb2.setText(_translate("Form", "Price :"))
        self.lb3.setText(_translate("Form", "Quantity :"))
        self.pb2.setText(_translate("Form", "Find Total"))
        self.lb4.setText(_translate("Form", "Total :"))

    def btn1(self):
        import sqlite3
        txt=self.t1.text()
        MyBooks=sqlite3.connect('books.db')
        curbooks=MyBooks.cursor()
        curbooks.execute("select * from book where Title=="+"'"+ txt +"';")
        record1=curbooks.fetchone()
        if record1==None:
            self.t2.setText("Book not found")
            
        else:
            self.t2.setText("Book found")
            self.pr=record1[-1]
            self.t3.setText(str(self.pr))

        
    def btn2(self):
        qty=int(self.t4.text())
        total=self.pr*qty
        self.t5.setText(str(total))
        
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
