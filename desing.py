
################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resourse_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(581, 346)
        MainWindow.setFocusPolicy(Qt.NoFocus)
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        icon = QIcon()
        icon.addFile(u":/icons/icons8-calc-100.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: #151515;\n"
"	font-family: Montserrat;\n"
"	font-size: 16pt;\n"
"	font-weight: 600;\n"
"}\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	background-color: #18181a;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #242426;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #303031;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"font-size: 15pt;\n"
"color: #757576;")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label)

        self.input = QLineEdit(self.centralwidget)
        self.input.setObjectName(u"input")
        sizePolicy.setHeightForWidth(self.input.sizePolicy().hasHeightForWidth())
        self.input.setSizePolicy(sizePolicy)
        self.input.setStyleSheet(u"font-size: 30pt;\n"
"border: none;\n"
"color: #757576;")
        self.input.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.input)

        self.Layout_buttons = QGridLayout()
        self.Layout_buttons.setSpacing(1)
        self.Layout_buttons.setObjectName(u"Layout_buttons")
        self.Button_cos = QPushButton(self.centralwidget)
        self.Button_cos.setObjectName(u"Button_cos")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Button_cos.sizePolicy().hasHeightForWidth())
        self.Button_cos.setSizePolicy(sizePolicy1)
        self.Button_cos.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_cos.setStyleSheet(u"QPushButton {\n"
"	background-color: #2a2a2c;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #3d3d3f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #4f4f51;\n"
"}")

        self.Layout_buttons.addWidget(self.Button_cos, 2, 1, 1, 1)

        self.Button_lg = QPushButton(self.centralwidget)
        self.Button_lg.setObjectName(u"Button_lg")
        sizePolicy1.setHeightForWidth(self.Button_lg.sizePolicy().hasHeightForWidth())
        self.Button_lg.setSizePolicy(sizePolicy1)
        self.Button_lg.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_lg.setStyleSheet(u"QPushButton {\n"
"	background-color: #2a2a2c;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #3d3d3f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #4f4f51;\n"
"}")

        self.Layout_buttons.addWidget(self.Button_lg, 4, 0, 1, 1)

        self.Button_atan = QPushButton(self.centralwidget)
        self.Button_atan.setObjectName(u"Button_atan")
        sizePolicy1.setHeightForWidth(self.Button_atan.sizePolicy().hasHeightForWidth())
        self.Button_atan.setSizePolicy(sizePolicy1)
        self.Button_atan.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_atan.setStyleSheet(u"QPushButton {\n"
"	background-color: #2a2a2c;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #3d3d3f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #4f4f51;\n"
"}")

        self.Layout_buttons.addWidget(self.Button_atan, 3, 0, 1, 1)

        self.Button_root = QPushButton(self.centralwidget)
        self.Button_root.setObjectName(u"Button_root")
        sizePolicy1.setHeightForWidth(self.Button_root.sizePolicy().hasHeightForWidth())
        self.Button_root.setSizePolicy(sizePolicy1)
        self.Button_root.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_root.setStyleSheet(u"QPushButton {\n"
"	background-color: #2a2a2c;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #3d3d3f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #4f4f51;\n"
"}")

        self.Layout_buttons.addWidget(self.Button_root, 2, 2, 1, 1)

        self.Button_4 = QPushButton(self.centralwidget)
        self.Button_4.setObjectName(u"Button_4")
        sizePolicy1.setHeightForWidth(self.Button_4.sizePolicy().hasHeightForWidth())
        self.Button_4.setSizePolicy(sizePolicy1)
        self.Button_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.Layout_buttons.addWidget(self.Button_4, 2, 3, 1, 1)

        self.Button_acos = QPushButton(self.centralwidget)
        self.Button_acos.setObjectName(u"Button_acos")
        sizePolicy1.setHeightForWidth(self.Button_acos.sizePolicy().hasHeightForWidth())
        self.Button_acos.setSizePolicy(sizePolicy1)
        self.Button_acos.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_acos.setStyleSheet(u"QPushButton {\n"
"	background-color: #2a2a2c;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #3d3d3f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #4f4f51;\n"
"}")

        self.Layout_buttons.addWidget(self.Button_acos, 2, 0, 1, 1)

        self.Button_v = QPushButton(self.centralwidget)
        self.Button_v.setObjectName(u"Button_v")
        sizePolicy1.setHeightForWidth(self.Button_v.sizePolicy().hasHeightForWidth())
        self.Button_v.setSizePolicy(sizePolicy1)
        self.Button_v.setMinimumSize(QSize(0, 0))
        self.Button_v.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_v.setStyleSheet(u"QPushButton {\n"
"	background-color: #2a2a2c;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #3d3d3f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #4f4f51;\n"
"}")

        self.Layout_buttons.addWidget(self.Button_v, 0, 0, 1, 1)

        self.Button_split = QPushButton(self.centralwidget)
        self.Button_split.setObjectName(u"Button_split")
        sizePolicy1.setHeightForWidth(self.Button_split.sizePolicy().hasHeightForWidth())
        self.Button_split.setSizePolicy(sizePolicy1)
        self.Button_split.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_split.setStyleSheet(u"")

        self.Layout_buttons.addWidget(self.Button_split, 0, 6, 1, 1)

        self.Button_multiply = QPushButton(self.centralwidget)
        self.Button_multiply.setObjectName(u"Button_multiply")
        sizePolicy1.setHeightForWidth(self.Button_multiply.sizePolicy().hasHeightForWidth())
        self.Button_multiply.setSizePolicy(sizePolicy1)
        self.Button_multiply.setCursor(QCursor(Qt.PointingHandCursor))

        self.Layout_buttons.addWidget(self.Button_multiply, 1, 6, 1, 1)

        self.Button_asin = QPushButton(self.centralwidget)
        self.Button_asin.setObjectName(u"Button_asin")
        sizePolicy1.setHeightForWidth(self.Button_asin.sizePolicy().hasHeightForWidth())
        self.Button_asin.setSizePolicy(sizePolicy1)
        self.Button_asin.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_asin.setStyleSheet(u"QPushButton {\n"
"	background-color: #2a2a2c;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #3d3d3f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #4f4f51;\n"
"}")

        self.Layout_buttons.addWidget(self.Button_asin, 1, 0, 1, 1)

        self.Button_6 = QPushButton(self.centralwidget)
        self.Button_6.setObjectName(u"Button_6")
        sizePolicy1.setHeightForWidth(self.Button_6.sizePolicy().hasHeightForWidth())
        self.Button_6.setSizePolicy(sizePolicy1)
        self.Button_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.Layout_buttons.addWidget(self.Button_6, 2, 5, 1, 1)

        self.Button_scobs = QPushButton(self.centralwidget)
        self.Button_scobs.setObjectName(u"Button_scobs")
        sizePolicy1.setHeightForWidth(self.Button_scobs.sizePolicy().hasHeightForWidth())
        self.Button_scobs.setSizePolicy(sizePolicy1)
        self.Button_scobs.setCursor(QCursor(Qt.PointingHandCursor))

        self.Layout_buttons.addWidget(self.Button_scobs, 0, 4, 1, 1)

        self.Button_BACKSPACE = QPushButton(self.centralwidget)
        self.Button_BACKSPACE.setObjectName(u"Button_percent")
        sizePolicy1.setHeightForWidth(self.Button_BACKSPACE.sizePolicy().hasHeightForWidth())
        self.Button_BACKSPACE.setSizePolicy(sizePolicy1)
        self.Button_BACKSPACE.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/outline_keyboard_backspace_white_48dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_BACKSPACE.setIcon(icon1)
        self.Button_BACKSPACE.setIconSize(QSize(25, 25))

        self.Layout_buttons.addWidget(self.Button_BACKSPACE, 0, 5, 1, 1)

        self.Button_plus = QPushButton(self.centralwidget)
        self.Button_plus.setObjectName(u"Button_plus")
        sizePolicy1.setHeightForWidth(self.Button_plus.sizePolicy().hasHeightForWidth())
        self.Button_plus.setSizePolicy(sizePolicy1)
        self.Button_plus.setCursor(QCursor(Qt.PointingHandCursor))

        self.Layout_buttons.addWidget(self.Button_plus, 3, 6, 1, 1)

        self.Button_equally = QPushButton(self.centralwidget)
        self.Button_equally.setObjectName(u"Button_equally")
        sizePolicy1.setHeightForWidth(self.Button_equally.sizePolicy().hasHeightForWidth())
        self.Button_equally.setSizePolicy(sizePolicy1)
        self.Button_equally.setCursor(QCursor(Qt.PointingHandCursor))

        self.Layout_buttons.addWidget(self.Button_equally, 4, 6, 1, 1)

        self.Button_minus = QPushButton(self.centralwidget)
        self.Button_minus.setObjectName(u"Button_minus")
        sizePolicy1.setHeightForWidth(self.Button_minus.sizePolicy().hasHeightForWidth())
        self.Button_minus.setSizePolicy(sizePolicy1)
        self.Button_minus.setCursor(QCursor(Qt.PointingHandCursor))

        self.Layout_buttons.addWidget(self.Button_minus, 2, 6, 1, 1)

        self.Button_8 = QPushButton(self.centralwidget)
        self.Button_8.setObjectName(u"Button_8")
        sizePolicy1.setHeightForWidth(self.Button_8.sizePolicy().hasHeightForWidth())
        self.Button_8.setSizePolicy(sizePolicy1)
        self.Button_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_8.setStyleSheet(u"")

        self.Layout_buttons.addWidget(self.Button_8, 1, 4, 1, 1)

        self.Button_plusminus = QPushButton(self.centralwidget)
        self.Button_plusminus.setObjectName(u"Button_plusminus")
        sizePolicy1.setHeightForWidth(self.Button_plusminus.sizePolicy().hasHeightForWidth())
        self.Button_plusminus.setSizePolicy(sizePolicy1)
        self.Button_plusminus.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_plusminus.setStyleSheet(u"QPushButton {\n"
"	background-color: #2a2a2c;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #3d3d3f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #4f4f51;\n"
"}")

        self.Layout_buttons.addWidget(self.Button_plusminus, 0, 2, 1, 1)

        self.Button_C = QPushButton(self.centralwidget)
        self.Button_C.setObjectName(u"Button_C")
        sizePolicy1.setHeightForWidth(self.Button_C.sizePolicy().hasHeightForWidth())
        self.Button_C.setSizePolicy(sizePolicy1)
        self.Button_C.setCursor(QCursor(Qt.PointingHandCursor))

        self.Layout_buttons.addWidget(self.Button_C, 0, 3, 1, 1)

        self.Button_x1 = QPushButton(self.centralwidget)
        self.Button_x1.setObjectName(u"Button_x1")
        sizePolicy1.setHeightForWidth(self.Button_x1.sizePolicy().hasHeightForWidth())
        self.Button_x1.setSizePolicy(sizePolicy1)
        self.Button_x1.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_x1.setStyleSheet(u"QPushButton {\n"
"	background-color: #2a2a2c;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #3d3d3f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #4f4f51;\n"
"}")

        self.Layout_buttons.addWidget(self.Button_x1, 0, 1, 1, 1)

        self.Button_sin = QPushButton(self.centralwidget)
        self.Button_sin.setObjectName(u"Button_sin")
        sizePolicy1.setHeightForWidth(self.Button_sin.sizePolicy().hasHeightForWidth())
        self.Button_sin.setSizePolicy(sizePolicy1)
        self.Button_sin.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_sin.setStyleSheet(u"QPushButton {\n"
"	background-color: #2a2a2c;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #3d3d3f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #4f4f51;\n"
"}")

        self.Layout_buttons.addWidget(self.Button_sin, 1, 1, 1, 1)

        self.Button_1x = QPushButton(self.centralwidget)
        self.Button_1x.setObjectName(u"Button_1x")
        sizePolicy1.setHeightForWidth(self.Button_1x.sizePolicy().hasHeightForWidth())
        self.Button_1x.setSizePolicy(sizePolicy1)
        self.Button_1x.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_1x.setStyleSheet(u"QPushButton {\n"
"	background-color: #2a2a2c;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #3d3d3f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #4f4f51;\n"
"}")

        self.Layout_buttons.addWidget(self.Button_1x, 1, 2, 1, 1)

        self.Button_7 = QPushButton(self.centralwidget)
        self.Button_7.setObjectName(u"Button_7")
        sizePolicy1.setHeightForWidth(self.Button_7.sizePolicy().hasHeightForWidth())
        self.Button_7.setSizePolicy(sizePolicy1)
        self.Button_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.Layout_buttons.addWidget(self.Button_7, 1, 3, 1, 1)

        self.Button_9 = QPushButton(self.centralwidget)
        self.Button_9.setObjectName(u"Button_9")
        sizePolicy1.setHeightForWidth(self.Button_9.sizePolicy().hasHeightForWidth())
        self.Button_9.setSizePolicy(sizePolicy1)
        self.Button_9.setCursor(QCursor(Qt.PointingHandCursor))

        self.Layout_buttons.addWidget(self.Button_9, 1, 5, 1, 1)

        self.Button_comma = QPushButton(self.centralwidget)
        self.Button_comma.setObjectName(u"Button_comma")
        sizePolicy1.setHeightForWidth(self.Button_comma.sizePolicy().hasHeightForWidth())
        self.Button_comma.setSizePolicy(sizePolicy1)
        self.Button_comma.setCursor(QCursor(Qt.PointingHandCursor))

        self.Layout_buttons.addWidget(self.Button_comma, 4, 5, 1, 1)

        self.Button_0 = QPushButton(self.centralwidget)
        self.Button_0.setObjectName(u"Button_0")
        sizePolicy1.setHeightForWidth(self.Button_0.sizePolicy().hasHeightForWidth())
        self.Button_0.setSizePolicy(sizePolicy1)
        self.Button_0.setCursor(QCursor(Qt.PointingHandCursor))

        self.Layout_buttons.addWidget(self.Button_0, 4, 3, 1, 2)

        self.Button_3 = QPushButton(self.centralwidget)
        self.Button_3.setObjectName(u"Button_3")
        sizePolicy1.setHeightForWidth(self.Button_3.sizePolicy().hasHeightForWidth())
        self.Button_3.setSizePolicy(sizePolicy1)
        self.Button_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.Layout_buttons.addWidget(self.Button_3, 3, 5, 1, 1)

        self.Button_tan = QPushButton(self.centralwidget)
        self.Button_tan.setObjectName(u"Button_tan")
        sizePolicy1.setHeightForWidth(self.Button_tan.sizePolicy().hasHeightForWidth())
        self.Button_tan.setSizePolicy(sizePolicy1)
        self.Button_tan.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_tan.setStyleSheet(u"QPushButton {\n"
"	background-color: #2a2a2c;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #3d3d3f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #4f4f51;\n"
"}")

        self.Layout_buttons.addWidget(self.Button_tan, 3, 1, 1, 1)

        self.Button_2 = QPushButton(self.centralwidget)
        self.Button_2.setObjectName(u"Button_2")
        sizePolicy1.setHeightForWidth(self.Button_2.sizePolicy().hasHeightForWidth())
        self.Button_2.setSizePolicy(sizePolicy1)
        self.Button_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.Layout_buttons.addWidget(self.Button_2, 3, 4, 1, 1)

        self.Button_1 = QPushButton(self.centralwidget)
        self.Button_1.setObjectName(u"Button_1")
        sizePolicy1.setHeightForWidth(self.Button_1.sizePolicy().hasHeightForWidth())
        self.Button_1.setSizePolicy(sizePolicy1)
        self.Button_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.Layout_buttons.addWidget(self.Button_1, 3, 3, 1, 1)

        self.Button_e = QPushButton(self.centralwidget)
        self.Button_e.setObjectName(u"Button_e")
        sizePolicy1.setHeightForWidth(self.Button_e.sizePolicy().hasHeightForWidth())
        self.Button_e.setSizePolicy(sizePolicy1)
        self.Button_e.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_e.setStyleSheet(u"QPushButton {\n"
"	background-color: #2a2a2c;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #3d3d3f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #4f4f51;\n"
"}")

        self.Layout_buttons.addWidget(self.Button_e, 4, 2, 1, 1)

        self.Button_ln = QPushButton(self.centralwidget)
        self.Button_ln.setObjectName(u"Button_ln")
        sizePolicy1.setHeightForWidth(self.Button_ln.sizePolicy().hasHeightForWidth())
        self.Button_ln.setSizePolicy(sizePolicy1)
        self.Button_ln.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_ln.setStyleSheet(u"QPushButton {\n"
"	background-color: #2a2a2c;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #3d3d3f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #4f4f51;\n"
"}")

        self.Layout_buttons.addWidget(self.Button_ln, 3, 2, 1, 1)

        self.Button_Pi = QPushButton(self.centralwidget)
        self.Button_Pi.setObjectName(u"Button_Pi")
        sizePolicy1.setHeightForWidth(self.Button_Pi.sizePolicy().hasHeightForWidth())
        self.Button_Pi.setSizePolicy(sizePolicy1)
        self.Button_Pi.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Pi.setStyleSheet(u"QPushButton {\n"
"	background-color: #2a2a2c;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #3d3d3f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #4f4f51;\n"
"}")

        self.Layout_buttons.addWidget(self.Button_Pi, 4, 1, 1, 1)

        self.Button_5 = QPushButton(self.centralwidget)
        self.Button_5.setObjectName(u"Button_5")
        sizePolicy1.setHeightForWidth(self.Button_5.sizePolicy().hasHeightForWidth())
        self.Button_5.setSizePolicy(sizePolicy1)
        self.Button_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.Layout_buttons.addWidget(self.Button_5, 2, 4, 1, 1)

        self.Layout_buttons.setColumnMinimumWidth(0, 60)
        self.Layout_buttons.setColumnMinimumWidth(1, 60)
        self.Layout_buttons.setColumnMinimumWidth(2, 60)
        self.Layout_buttons.setColumnMinimumWidth(3, 60)
        self.Layout_buttons.setColumnMinimumWidth(4, 60)
        self.Layout_buttons.setColumnMinimumWidth(5, 60)
        self.Layout_buttons.setColumnMinimumWidth(6, 60)
        self.Layout_buttons.setRowMinimumHeight(0, 40)
        self.Layout_buttons.setRowMinimumHeight(1, 40)
        self.Layout_buttons.setRowMinimumHeight(2, 40)
        self.Layout_buttons.setRowMinimumHeight(3, 40)
        self.Layout_buttons.setRowMinimumHeight(4, 40)

        self.verticalLayout.addLayout(self.Layout_buttons)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.input.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Button_cos.setText(QCoreApplication.translate("MainWindow", u"cos", None))
        self.Button_lg.setText(QCoreApplication.translate("MainWindow", u"lg", None))
        self.Button_atan.setText(QCoreApplication.translate("MainWindow", u"atan", None))
        self.Button_root.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.Button_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.Button_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.Button_acos.setText(QCoreApplication.translate("MainWindow", u"acos", None))
        self.Button_v.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.Button_split.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
#if QT_CONFIG(shortcut)
        self.Button_split.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.Button_multiply.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
#if QT_CONFIG(shortcut)
        self.Button_multiply.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.Button_asin.setText(QCoreApplication.translate("MainWindow", u"asin", None))
        self.Button_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.Button_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.Button_scobs.setText(QCoreApplication.translate("MainWindow", u"( )", None))
        self.Button_BACKSPACE.setText("")
#if QT_CONFIG(shortcut)
        self.Button_BACKSPACE.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.Button_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.Button_plus.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.Button_equally.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.Button_equally.setShortcut(QCoreApplication.translate("MainWindow", u"=, Return, Enter", None))
#endif // QT_CONFIG(shortcut)
        self.Button_minus.setText(QCoreApplication.translate("MainWindow", u"\u2212", None))
#if QT_CONFIG(shortcut)
        self.Button_minus.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.Button_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.Button_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.Button_plusminus.setText(QCoreApplication.translate("MainWindow", u"\u00b1", None))
        self.Button_C.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.Button_x1.setText(QCoreApplication.translate("MainWindow", u"!", None))
        self.Button_sin.setText(QCoreApplication.translate("MainWindow", u"sin", None))
        self.Button_1x.setText(QCoreApplication.translate("MainWindow", u"1/x", None))
        self.Button_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.Button_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.Button_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.Button_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.Button_comma.setText(QCoreApplication.translate("MainWindow", u",", None))
#if QT_CONFIG(shortcut)
        self.Button_comma.setShortcut(QCoreApplication.translate("MainWindow", u",, .", None))
#endif // QT_CONFIG(shortcut)
        self.Button_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.Button_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.Button_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.Button_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.Button_tan.setText(QCoreApplication.translate("MainWindow", u"tan", None))
        self.Button_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.Button_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.Button_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.Button_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.Button_e.setText(QCoreApplication.translate("MainWindow", u"e", None))
        self.Button_ln.setText(QCoreApplication.translate("MainWindow", u"ln", None))
        self.Button_Pi.setText(QCoreApplication.translate("MainWindow", u"\u03c0", None))
        self.Button_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.Button_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

