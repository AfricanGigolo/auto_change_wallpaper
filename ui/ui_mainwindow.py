# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(421, 160)
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_dir = QLineEdit(self.centralwidget)
        self.lineEdit_dir.setObjectName(u"lineEdit_dir")
        self.lineEdit_dir.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit_dir)

        self.pushButton_selectpath = QPushButton(self.centralwidget)
        self.pushButton_selectpath.setObjectName(u"pushButton_selectpath")

        self.horizontalLayout.addWidget(self.pushButton_selectpath)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.spinBox_min = QSpinBox(self.centralwidget)
        self.spinBox_min.setObjectName(u"spinBox_min")
        self.spinBox_min.setMinimum(1)
        self.spinBox_min.setMaximum(3600)

        self.horizontalLayout_3.addWidget(self.spinBox_min)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBox_close = QCheckBox(self.centralwidget)
        self.checkBox_close.setObjectName(u"checkBox_close")

        self.horizontalLayout_4.addWidget(self.checkBox_close)

        self.checkBox_boot = QCheckBox(self.centralwidget)
        self.checkBox_boot.setObjectName(u"checkBox_boot")

        self.horizontalLayout_4.addWidget(self.checkBox_boot)

        self.checkBox_disorder = QCheckBox(self.centralwidget)
        self.checkBox_disorder.setObjectName(u"checkBox_disorder")

        self.horizontalLayout_4.addWidget(self.checkBox_disorder)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_previous = QPushButton(self.centralwidget)
        self.pushButton_previous.setObjectName(u"pushButton_previous")

        self.horizontalLayout_2.addWidget(self.pushButton_previous)

        self.pushButton_next = QPushButton(self.centralwidget)
        self.pushButton_next.setObjectName(u"pushButton_next")

        self.horizontalLayout_2.addWidget(self.pushButton_next)

        self.pushButton_auto = QPushButton(self.centralwidget)
        self.pushButton_auto.setObjectName(u"pushButton_auto")

        self.horizontalLayout_2.addWidget(self.pushButton_auto)

        self.label_status = QLabel(self.centralwidget)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_status)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_msg = QLabel(self.centralwidget)
        self.label_msg.setObjectName(u"label_msg")

        self.horizontalLayout_5.addWidget(self.label_msg)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u5207\u6362\u58c1\u7eb8\u5de5\u5177 by AfricanGigolo", None))
        self.lineEdit_dir.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u56fe\u7247\u5b58\u50a8\u8def\u5f84", None))
        self.pushButton_selectpath.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8f6e\u6362\u6587\u4ef6\u5939", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u8f6e\u6362\u95f4\u9694\uff1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5206\u949f", None))
        self.checkBox_close.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u65f6\u9690\u85cf\u5230\u6258\u76d8", None))
        self.checkBox_boot.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u673a\u81ea\u542f\u52a8", None))
        self.checkBox_disorder.setText(QCoreApplication.translate("MainWindow", u"\u4e71\u5e8f", None))
        self.pushButton_previous.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u5f20", None))
        self.pushButton_next.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u5f20", None))
        self.pushButton_auto.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u8f6e\u6362", None))
        self.label_status.setText(QCoreApplication.translate("MainWindow", u"\u72b6\u6001\u663e\u793a", None))
        self.label_msg.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u4fe1\u606f", None))
    # retranslateUi

