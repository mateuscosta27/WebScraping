# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.setWindowModality(Qt.ApplicationModal)
        Main.resize(1134, 686)
        icon = QIcon()
        icon.addFile(u"./src/main_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        Main.setWindowIcon(icon)
        Main.setIconSize(QSize(70, 70))
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_10 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 60))
        self.frame_top.setMaximumSize(QSize(16777215, 60))
        self.frame_top.setStyleSheet(u"background-color: #0954B2;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_btn_menu = QFrame(self.frame_top)
        self.frame_btn_menu.setObjectName(u"frame_btn_menu")
        self.frame_btn_menu.setMinimumSize(QSize(185, 60))
        self.frame_btn_menu.setMaximumSize(QSize(185, 60))
        self.frame_btn_menu.setStyleSheet(u"background-color:#0954B2;")
        self.frame_btn_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_btn_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_btn_menu)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_menu = QPushButton(self.frame_btn_menu)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setMinimumSize(QSize(75, 60))
        self.btn_menu.setMaximumSize(QSize(180, 60))
        self.btn_menu.setStyleSheet(u"QPushButton{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #0954B2;\n"
"	border-radius: 15px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #4195FF;\n"
"	border-radius: 5px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:#0954B2;\n"
"	border-radius: 8px;\n"
"	border-top-color: rgb(4, 35, 38);\n"
"	border-left-color:  rgb(4, 35, 38);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"./src/menu_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon1)
        self.btn_menu.setIconSize(QSize(50, 50))

        self.horizontalLayout_4.addWidget(self.btn_menu, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_btn_menu)

        self.frame_info = QFrame(self.frame_top)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setMinimumSize(QSize(0, 0))
        self.frame_info.setStyleSheet(u"background-color: rgb(9, 84, 178);")
        self.frame_info.setFrameShape(QFrame.NoFrame)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_info)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.frame_info)


        self.verticalLayout_10.addWidget(self.frame_top)

        self.fram_bot = QFrame(self.centralwidget)
        self.fram_bot.setObjectName(u"fram_bot")
        self.fram_bot.setFrameShape(QFrame.NoFrame)
        self.fram_bot.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.fram_bot)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_side = QFrame(self.fram_bot)
        self.frame_side.setObjectName(u"frame_side")
        self.frame_side.setMinimumSize(QSize(0, 0))
        self.frame_side.setMaximumSize(QSize(0, 16777215))
        self.frame_side.setSizeIncrement(QSize(0, 0))
        self.frame_side.setStyleSheet(u"background-color: #FFF;\n"
"border: 2px solid;\n"
"border-left: none;\n"
"border-top: none;\n"
"border-bottom:none;\n"
"border-right-color: #0954B2;")
        self.frame_side.setFrameShape(QFrame.NoFrame)
        self.frame_side.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_side)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 45, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_buttons = QFrame(self.frame_side)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setStyleSheet(u"border:none;")
        self.frame_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_buttons)
        self.verticalLayout.setSpacing(35)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 0, 0, 0)
        self.btn_coletar = QPushButton(self.frame_buttons)
        self.btn_coletar.setObjectName(u"btn_coletar")
        self.btn_coletar.setMinimumSize(QSize(200, 45))
        self.btn_coletar.setMaximumSize(QSize(200, 45))
        self.btn_coletar.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.btn_coletar.setFont(font)
        self.btn_coletar.setStyleSheet(u"QPushButton{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #4195FF;\n"
"	border-radius: 12px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #0954B2;\n"
"	border-radius: 12px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	border-style: insetset;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #4195FF;\n"
"	border-radius: 8px;\n"
"	border-top-color: rgb(4, 35, 38);\n"
"	border-left-color:  rgb(4, 35, 38);\n"
"}")
        self.btn_coletar.setInputMethodHints(Qt.ImhNone)
        icon2 = QIcon()
        icon2.addFile(u"./src/collect_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_coletar.setIcon(icon2)
        self.btn_coletar.setIconSize(QSize(45, 30))

        self.verticalLayout.addWidget(self.btn_coletar)

        self.btn_visJogos = QPushButton(self.frame_buttons)
        self.btn_visJogos.setObjectName(u"btn_visJogos")
        self.btn_visJogos.setMinimumSize(QSize(200, 45))
        self.btn_visJogos.setMaximumSize(QSize(200, 45))
        self.btn_visJogos.setStyleSheet(u"QPushButton{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #4195FF;\n"
"	border-radius: 12px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #0954B2;\n"
"	border-radius: 12px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	border-style: insetset;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #4195FF;\n"
"	border-radius: 8px;\n"
"	border-top-color: rgb(4, 35, 38);\n"
"	border-left-color:  rgb(4, 35, 38);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"./src/games_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_visJogos.setIcon(icon3)
        self.btn_visJogos.setIconSize(QSize(45, 30))

        self.verticalLayout.addWidget(self.btn_visJogos)

        self.btn_visProbabilidades = QPushButton(self.frame_buttons)
        self.btn_visProbabilidades.setObjectName(u"btn_visProbabilidades")
        self.btn_visProbabilidades.setMinimumSize(QSize(200, 45))
        self.btn_visProbabilidades.setMaximumSize(QSize(200, 45))
        self.btn_visProbabilidades.setStyleSheet(u"QPushButton{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #4195FF;\n"
"	border-radius: 12px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #0954B2;\n"
"	border-radius: 12px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	border-style: insetset;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #4195FF;\n"
"	border-radius: 8px;\n"
"	border-top-color: rgb(4, 35, 38);\n"
"	border-left-color:  rgb(4, 35, 38);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"./src/possibility_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_visProbabilidades.setIcon(icon4)
        self.btn_visProbabilidades.setIconSize(QSize(45, 30))

        self.verticalLayout.addWidget(self.btn_visProbabilidades)

        self.btn_previsoes = QPushButton(self.frame_buttons)
        self.btn_previsoes.setObjectName(u"btn_previsoes")
        self.btn_previsoes.setMinimumSize(QSize(200, 45))
        self.btn_previsoes.setMaximumSize(QSize(200, 45))
        self.btn_previsoes.setStyleSheet(u"QPushButton{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #4195FF;\n"
"	border-radius: 12px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #0954B2;\n"
"	border-radius: 12px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	border-style: insetset;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #4195FF;\n"
"	border-radius: 8px;\n"
"	border-top-color: rgb(4, 35, 38);\n"
"	border-left-color:  rgb(4, 35, 38);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"./src/odds_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_previsoes.setIcon(icon5)
        self.btn_previsoes.setIconSize(QSize(45, 30))

        self.verticalLayout.addWidget(self.btn_previsoes)

        self.btn_calculator = QPushButton(self.frame_buttons)
        self.btn_calculator.setObjectName(u"btn_calculator")
        self.btn_calculator.setMinimumSize(QSize(200, 45))
        self.btn_calculator.setMaximumSize(QSize(200, 45))
        self.btn_calculator.setStyleSheet(u"QPushButton{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #4195FF;\n"
"	border-radius: 12px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #0954B2;\n"
"	border-radius: 12px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	border-style: insetset;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #4195FF;\n"
"	border-radius: 8px;\n"
"	border-top-color: rgb(4, 35, 38);\n"
"	border-left-color:  rgb(4, 35, 38);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"./src/calculator_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_calculator.setIcon(icon6)
        self.btn_calculator.setIconSize(QSize(45, 30))

        self.verticalLayout.addWidget(self.btn_calculator)


        self.verticalLayout_2.addWidget(self.frame_buttons)

        self.verticalSpacer_2 = QSpacerItem(20, 383, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.frame_about = QFrame(self.frame_side)
        self.frame_about.setObjectName(u"frame_about")
        self.frame_about.setMinimumSize(QSize(0, 0))
        self.frame_about.setMaximumSize(QSize(16777215, 16777215))
        self.frame_about.setStyleSheet(u"background-color: rgb(9, 84, 178);")
        self.frame_about.setFrameShape(QFrame.NoFrame)
        self.frame_about.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_about)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 1)
        self.btn_about = QPushButton(self.frame_about)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setMinimumSize(QSize(225, 35))
        self.btn_about.setMaximumSize(QSize(230, 35))
        self.btn_about.setStyleSheet(u"QPushButton{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #0954B2;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #4195FF;\n"
"	border-radius: 12px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	border-style: insetset;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #0954B2;\n"
"	border-radius: 8px;\n"
"	border-top-color: rgb(4, 35, 38);\n"
"	border-left-color:  rgb(4, 35, 38);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"src/about_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_about.setIcon(icon7)
        self.btn_about.setIconSize(QSize(25, 25))
        self.btn_about.setAutoDefault(True)
        self.btn_about.setFlat(False)

        self.horizontalLayout_12.addWidget(self.btn_about)


        self.verticalLayout_2.addWidget(self.frame_about)


        self.horizontalLayout.addWidget(self.frame_side)

        self.frame_content = QFrame(self.fram_bot)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setStyleSheet(u"background-color:#0954B2;")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_content)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_pages = QFrame(self.frame_content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setStyleSheet(u"background-color: #fff;")
        self.frame_pages.setFrameShape(QFrame.NoFrame)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_pages)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(self.frame_pages)
        self.pages.setObjectName(u"pages")
        self.pages.setLayoutDirection(Qt.LeftToRight)
        self.pages.setAutoFillBackground(False)
        self.pages.setStyleSheet(u"")
        self.pages.setFrameShape(QFrame.StyledPanel)
        self.pages.setFrameShadow(QFrame.Sunken)
        self.pages.setLineWidth(0)
        self.page_view_games = QWidget()
        self.page_view_games.setObjectName(u"page_view_games")
        self.verticalLayout_11 = QVBoxLayout(self.page_view_games)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_options_games = QFrame(self.page_view_games)
        self.frame_options_games.setObjectName(u"frame_options_games")
        self.frame_options_games.setMinimumSize(QSize(0, 30))
        self.frame_options_games.setStyleSheet(u"background-color: #4195FF;")
        self.frame_options_games.setFrameShape(QFrame.StyledPanel)
        self.frame_options_games.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_options_games)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.rb_games_betano = QRadioButton(self.frame_options_games)
        self.rb_games_betano.setObjectName(u"rb_games_betano")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rb_games_betano.sizePolicy().hasHeightForWidth())
        self.rb_games_betano.setSizePolicy(sizePolicy)
        self.rb_games_betano.setMinimumSize(QSize(220, 20))
        self.rb_games_betano.setMaximumSize(QSize(220, 20))
        self.rb_games_betano.setStyleSheet(u"\n"
"QRadioButton{\n"
"	font: 75 12pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QRadioButton:pressed{\n"
"	font: 75 12pt \"MS Shell Dlg 2\";\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.rb_games_betano.setAutoRepeatDelay(300)
        self.rb_games_betano.setAutoRepeatInterval(100)

        self.horizontalLayout_10.addWidget(self.rb_games_betano)

        self.rb_games_esporte365 = QRadioButton(self.frame_options_games)
        self.rb_games_esporte365.setObjectName(u"rb_games_esporte365")
        self.rb_games_esporte365.setMinimumSize(QSize(200, 20))
        self.rb_games_esporte365.setMaximumSize(QSize(200, 20))
        self.rb_games_esporte365.setStyleSheet(u"\n"
"QRadioButton{\n"
"	font: 75 12pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QRadioButton:pressed{\n"
"	font: 75 12pt \"MS Shell Dlg 2\";\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_10.addWidget(self.rb_games_esporte365)

        self.rb_games_pixbet = QRadioButton(self.frame_options_games)
        self.rb_games_pixbet.setObjectName(u"rb_games_pixbet")
        self.rb_games_pixbet.setMinimumSize(QSize(220, 20))
        self.rb_games_pixbet.setMaximumSize(QSize(220, 20))
        self.rb_games_pixbet.setStyleSheet(u"\n"
"QRadioButton{\n"
"	font: 75 12pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QRadioButton:pressed{\n"
"	font: 75 12pt \"MS Shell Dlg 2\";\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_10.addWidget(self.rb_games_pixbet)


        self.verticalLayout_11.addWidget(self.frame_options_games)

        self.frame_tb_games = QFrame(self.page_view_games)
        self.frame_tb_games.setObjectName(u"frame_tb_games")
        self.frame_tb_games.setFrameShape(QFrame.StyledPanel)
        self.frame_tb_games.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_tb_games)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.tb_view_games = QTableWidget(self.frame_tb_games)
        if (self.tb_view_games.columnCount() < 15):
            self.tb_view_games.setColumnCount(15)
        icon8 = QIcon()
        icon8.addFile(u"./src/order_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem.setFont(font1);
        __qtablewidgetitem.setIcon(icon8);
        self.tb_view_games.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem1.setFont(font1);
        __qtablewidgetitem1.setIcon(icon8);
        self.tb_view_games.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem2.setFont(font1);
        __qtablewidgetitem2.setIcon(icon8);
        self.tb_view_games.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem3.setFont(font1);
        __qtablewidgetitem3.setIcon(icon8);
        self.tb_view_games.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem4.setFont(font1);
        __qtablewidgetitem4.setIcon(icon8);
        self.tb_view_games.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem5.setFont(font1);
        __qtablewidgetitem5.setIcon(icon8);
        self.tb_view_games.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font1);
        __qtablewidgetitem6.setIcon(icon8);
        self.tb_view_games.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font1);
        __qtablewidgetitem7.setIcon(icon8);
        self.tb_view_games.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font1);
        __qtablewidgetitem8.setIcon(icon8);
        self.tb_view_games.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font1);
        __qtablewidgetitem9.setIcon(icon8);
        self.tb_view_games.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font1);
        __qtablewidgetitem10.setIcon(icon8);
        self.tb_view_games.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font1);
        __qtablewidgetitem11.setIcon(icon8);
        self.tb_view_games.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font1);
        __qtablewidgetitem12.setIcon(icon8);
        self.tb_view_games.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font1);
        __qtablewidgetitem13.setIcon(icon8);
        self.tb_view_games.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font1);
        __qtablewidgetitem14.setIcon(icon8);
        self.tb_view_games.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        self.tb_view_games.setObjectName(u"tb_view_games")
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dlg 2"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.tb_view_games.setFont(font2)
        self.tb_view_games.setToolTipDuration(-3)
        self.tb_view_games.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"background-color:rgb(243, 243, 243);\n"
"")
        self.tb_view_games.setFrameShape(QFrame.StyledPanel)
        self.tb_view_games.setFrameShadow(QFrame.Sunken)
        self.tb_view_games.setAutoScrollMargin(20)
        self.tb_view_games.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_view_games.setDragEnabled(False)
        self.tb_view_games.setAlternatingRowColors(True)
        self.tb_view_games.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.tb_view_games.setIconSize(QSize(0, 0))
        self.tb_view_games.setTextElideMode(Qt.ElideRight)
        self.tb_view_games.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tb_view_games.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tb_view_games.setSortingEnabled(True)
        self.tb_view_games.setColumnCount(15)
        self.tb_view_games.horizontalHeader().setMinimumSectionSize(50)
        self.tb_view_games.horizontalHeader().setDefaultSectionSize(150)
        self.tb_view_games.verticalHeader().setVisible(False)
        self.tb_view_games.verticalHeader().setDefaultSectionSize(50)
        self.tb_view_games.verticalHeader().setProperty("showSortIndicator", True)

        self.verticalLayout_14.addWidget(self.tb_view_games)


        self.verticalLayout_11.addWidget(self.frame_tb_games)

        self.pages.addWidget(self.page_view_games)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.gridLayout_2 = QGridLayout(self.page_home)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_home_top = QFrame(self.page_home)
        self.frame_home_top.setObjectName(u"frame_home_top")
        self.frame_home_top.setFrameShape(QFrame.StyledPanel)
        self.frame_home_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_home_top)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lb_collect_animation = QLabel(self.frame_home_top)
        self.lb_collect_animation.setObjectName(u"lb_collect_animation")
        self.lb_collect_animation.setPixmap(QPixmap(u"src/texte_icon.gif"))
        self.lb_collect_animation.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.lb_collect_animation)


        self.gridLayout_2.addWidget(self.frame_home_top, 0, 0, 1, 1)

        self.frame_home_bottom = QFrame(self.page_home)
        self.frame_home_bottom.setObjectName(u"frame_home_bottom")
        self.frame_home_bottom.setMinimumSize(QSize(0, 0))
        self.frame_home_bottom.setMaximumSize(QSize(16777215, 150))
        self.frame_home_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_home_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_home_bottom)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lb_text_animation = QLabel(self.frame_home_bottom)
        self.lb_text_animation.setObjectName(u"lb_text_animation")
        self.lb_text_animation.setMinimumSize(QSize(0, 0))
        self.lb_text_animation.setPixmap(QPixmap(u"src/texte_icon.gif"))
        self.lb_text_animation.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.lb_text_animation)


        self.gridLayout_2.addWidget(self.frame_home_bottom, 1, 0, 1, 1)

        self.pages.addWidget(self.page_home)
        self.page_preview = QWidget()
        self.page_preview.setObjectName(u"page_preview")
        self.page_preview.setMinimumSize(QSize(0, 0))
        self.verticalLayout_9 = QVBoxLayout(self.page_preview)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_options_camp = QFrame(self.page_preview)
        self.frame_options_camp.setObjectName(u"frame_options_camp")
        self.frame_options_camp.setMinimumSize(QSize(0, 0))
        self.frame_options_camp.setMaximumSize(QSize(16777215, 100))
        self.frame_options_camp.setStyleSheet(u"background-color: #4195FF;")
        self.frame_options_camp.setFrameShape(QFrame.StyledPanel)
        self.frame_options_camp.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_options_camp)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_search_teams = QFrame(self.frame_options_camp)
        self.frame_search_teams.setObjectName(u"frame_search_teams")
        self.frame_search_teams.setMinimumSize(QSize(0, 30))
        self.frame_search_teams.setMaximumSize(QSize(16777215, 16777215))
        self.frame_search_teams.setFrameShape(QFrame.StyledPanel)
        self.frame_search_teams.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_search_teams)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_season = QFrame(self.frame_search_teams)
        self.frame_season.setObjectName(u"frame_season")
        self.frame_season.setMaximumSize(QSize(16777215, 80))
        self.frame_season.setFrameShape(QFrame.StyledPanel)
        self.frame_season.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_season)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_side_options_season = QToolButton(self.frame_season)
        self.btn_side_options_season.setObjectName(u"btn_side_options_season")
        self.btn_side_options_season.setMinimumSize(QSize(0, 20))
        self.btn_side_options_season.setMaximumSize(QSize(16777215, 16777215))
        self.btn_side_options_season.setStyleSheet(u"QToolButton{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #0954B2;\n"
"	border-radius: 2px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QToolButton:hover{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(26, 60, 102);\n"
"	border-radius: 2px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QToolButton:pressed{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:#0954B2;\n"
"	border-radius: 2px;\n"
"	border-top-color: rgb(4, 35, 38);\n"
"	border-left-color:  rgb(4, 35, 38);\n"
"}")
        self.btn_side_options_season.setIconSize(QSize(16, 16))
        self.btn_side_options_season.setPopupMode(QToolButton.DelayedPopup)
        self.btn_side_options_season.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        self.btn_side_options_season.setAutoRaise(True)

        self.gridLayout_4.addWidget(self.btn_side_options_season, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(1088, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.btn_update_base = QPushButton(self.frame_season)
        self.btn_update_base.setObjectName(u"btn_update_base")
        self.btn_update_base.setMinimumSize(QSize(100, 30))
        self.btn_update_base.setMaximumSize(QSize(100, 30))
        self.btn_update_base.setStyleSheet(u"QPushButton{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #0954B2;\n"
"	border-radius: 8px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(26, 60, 102);\n"
"	border-radius: 8px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:#0954B2;\n"
"	border-radius: 8px;\n"
"	border-top-color: rgb(4, 35, 38);\n"
"	border-left-color:  rgb(4, 35, 38);\n"
"}")

        self.gridLayout_4.addWidget(self.btn_update_base, 0, 2, 1, 1)


        self.verticalLayout_16.addWidget(self.frame_season)

        self.frame_teams_bottom = QFrame(self.frame_search_teams)
        self.frame_teams_bottom.setObjectName(u"frame_teams_bottom")
        self.frame_teams_bottom.setMinimumSize(QSize(0, 0))
        self.frame_teams_bottom.setMaximumSize(QSize(16777215, 200))
        self.frame_teams_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_teams_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_teams_bottom)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_side_season = QFrame(self.frame_teams_bottom)
        self.frame_side_season.setObjectName(u"frame_side_season")
        self.frame_side_season.setMinimumSize(QSize(0, 0))
        self.frame_side_season.setMaximumSize(QSize(16777215, 0))
        self.frame_side_season.setFrameShape(QFrame.StyledPanel)
        self.frame_side_season.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_side_season)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(10)
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.cb_camp = QComboBox(self.frame_side_season)
        icon9 = QIcon()
        icon9.addFile(u"./src/list_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.addItem(icon9, "")
        self.cb_camp.setObjectName(u"cb_camp")
        self.cb_camp.setMinimumSize(QSize(0, 40))
        self.cb_camp.setMaximumSize(QSize(300, 40))
        font3 = QFont()
        font3.setPointSize(12)
        self.cb_camp.setFont(font3)
        self.cb_camp.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.cb_camp.setIconSize(QSize(16, 16))

        self.gridLayout_6.addWidget(self.cb_camp, 0, 0, 1, 1)

        self.cb_games = QComboBox(self.frame_side_season)
        self.cb_games.addItem(icon9, "")
        self.cb_games.addItem(icon9, "")
        self.cb_games.addItem(icon9, "")
        self.cb_games.setObjectName(u"cb_games")
        self.cb_games.setMinimumSize(QSize(0, 40))
        self.cb_games.setMaximumSize(QSize(300, 40))
        self.cb_games.setFont(font3)
        self.cb_games.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.cb_games.setIconSize(QSize(16, 16))

        self.gridLayout_6.addWidget(self.cb_games, 0, 1, 1, 1)

        self.le_team1 = QLineEdit(self.frame_side_season)
        self.le_team1.setObjectName(u"le_team1")
        self.le_team1.setMinimumSize(QSize(200, 40))
        self.le_team1.setMaximumSize(QSize(200, 40))
        self.le_team1.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_6.addWidget(self.le_team1, 0, 2, 1, 1)

        self.le_team2 = QLineEdit(self.frame_side_season)
        self.le_team2.setObjectName(u"le_team2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_team2.sizePolicy().hasHeightForWidth())
        self.le_team2.setSizePolicy(sizePolicy1)
        self.le_team2.setMinimumSize(QSize(200, 40))
        self.le_team2.setMaximumSize(QSize(200, 40))
        self.le_team2.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_6.addWidget(self.le_team2, 0, 3, 1, 1)

        self.btn_search = QPushButton(self.frame_side_season)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setMinimumSize(QSize(150, 40))
        self.btn_search.setMaximumSize(QSize(150, 35))
        self.btn_search.setSizeIncrement(QSize(0, 0))
        font4 = QFont()
        font4.setFamilies([u"MS Shell Dlg 2"])
        font4.setPointSize(14)
        font4.setBold(False)
        font4.setItalic(False)
        self.btn_search.setFont(font4)
        self.btn_search.setStyleSheet(u"QPushButton{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #0954B2;\n"
"	border-radius: 8px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(26, 60, 102);\n"
"	border-radius: 8px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:#0954B2;\n"
"	border-radius: 8px;\n"
"	border-top-color: rgb(4, 35, 38);\n"
"	border-left-color:  rgb(4, 35, 38);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"./src/search_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search.setIcon(icon10)
        self.btn_search.setIconSize(QSize(35, 35))

        self.gridLayout_6.addWidget(self.btn_search, 0, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(59, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 0, 5, 1, 1)


        self.horizontalLayout_6.addWidget(self.frame_side_season)


        self.verticalLayout_16.addWidget(self.frame_teams_bottom)


        self.verticalLayout_13.addWidget(self.frame_search_teams)


        self.verticalLayout_9.addWidget(self.frame_options_camp)

        self.frame_preview = QFrame(self.page_preview)
        self.frame_preview.setObjectName(u"frame_preview")
        self.frame_preview.setFrameShape(QFrame.StyledPanel)
        self.frame_preview.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_preview)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tb_preview = QTableWidget(self.frame_preview)
        if (self.tb_preview.columnCount() < 15):
            self.tb_preview.setColumnCount(15)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem15.setFont(font1);
        __qtablewidgetitem15.setIcon(icon8);
        self.tb_preview.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem16.setFont(font1);
        __qtablewidgetitem16.setIcon(icon8);
        self.tb_preview.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem17.setFont(font1);
        __qtablewidgetitem17.setIcon(icon8);
        self.tb_preview.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem18.setFont(font1);
        __qtablewidgetitem18.setIcon(icon8);
        self.tb_preview.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem19.setFont(font1);
        __qtablewidgetitem19.setIcon(icon8);
        self.tb_preview.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem20.setFont(font1);
        __qtablewidgetitem20.setIcon(icon8);
        self.tb_preview.setHorizontalHeaderItem(5, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font1);
        __qtablewidgetitem21.setIcon(icon8);
        self.tb_preview.setHorizontalHeaderItem(6, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font1);
        __qtablewidgetitem22.setIcon(icon8);
        self.tb_preview.setHorizontalHeaderItem(7, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font1);
        __qtablewidgetitem23.setIcon(icon8);
        self.tb_preview.setHorizontalHeaderItem(8, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font1);
        __qtablewidgetitem24.setIcon(icon8);
        self.tb_preview.setHorizontalHeaderItem(9, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font1);
        __qtablewidgetitem25.setIcon(icon8);
        self.tb_preview.setHorizontalHeaderItem(10, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFont(font1);
        __qtablewidgetitem26.setIcon(icon8);
        self.tb_preview.setHorizontalHeaderItem(11, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font1);
        __qtablewidgetitem27.setIcon(icon8);
        self.tb_preview.setHorizontalHeaderItem(12, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFont(font1);
        __qtablewidgetitem28.setIcon(icon8);
        self.tb_preview.setHorizontalHeaderItem(13, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFont(font1);
        __qtablewidgetitem29.setIcon(icon8);
        self.tb_preview.setHorizontalHeaderItem(14, __qtablewidgetitem29)
        self.tb_preview.setObjectName(u"tb_preview")
        self.tb_preview.setFont(font2)
        self.tb_preview.setToolTipDuration(-3)
        self.tb_preview.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"background-color:rgb(243, 243, 243);\n"
"")
        self.tb_preview.setFrameShape(QFrame.StyledPanel)
        self.tb_preview.setFrameShadow(QFrame.Sunken)
        self.tb_preview.setAutoScrollMargin(20)
        self.tb_preview.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_preview.setDragEnabled(False)
        self.tb_preview.setAlternatingRowColors(True)
        self.tb_preview.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.tb_preview.setIconSize(QSize(0, 0))
        self.tb_preview.setTextElideMode(Qt.ElideRight)
        self.tb_preview.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tb_preview.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tb_preview.setSortingEnabled(True)
        self.tb_preview.setColumnCount(15)
        self.tb_preview.horizontalHeader().setMinimumSectionSize(50)
        self.tb_preview.horizontalHeader().setDefaultSectionSize(150)
        self.tb_preview.verticalHeader().setVisible(False)
        self.tb_preview.verticalHeader().setDefaultSectionSize(50)
        self.tb_preview.verticalHeader().setProperty("showSortIndicator", True)

        self.verticalLayout_12.addWidget(self.tb_preview)


        self.verticalLayout_9.addWidget(self.frame_preview)

        self.pages.addWidget(self.page_preview)
        self.page_possibilities = QWidget()
        self.page_possibilities.setObjectName(u"page_possibilities")
        self.page_possibilities.setMouseTracking(False)
        self.page_possibilities.setTabletTracking(False)
        self.horizontalLayout_5 = QHBoxLayout(self.page_possibilities)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page_possibilities)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: #4195FF;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_options = QFrame(self.frame)
        self.frame_options.setObjectName(u"frame_options")
        self.frame_options.setMinimumSize(QSize(0, 0))
        self.frame_options.setMaximumSize(QSize(16777215, 100))
        self.frame_options.setStyleSheet(u"background-color: #4195FF;")
        self.frame_options.setFrameShape(QFrame.NoFrame)
        self.frame_options.setFrameShadow(QFrame.Plain)
        self.frame_options.setLineWidth(1)
        self.gridLayout_3 = QGridLayout(self.frame_options)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_btn_options = QFrame(self.frame_options)
        self.frame_btn_options.setObjectName(u"frame_btn_options")
        self.frame_btn_options.setMinimumSize(QSize(0, 30))
        self.frame_btn_options.setMaximumSize(QSize(16777215, 30))
        self.frame_btn_options.setStyleSheet(u"background-color: #4195FF;")
        self.frame_btn_options.setFrameShape(QFrame.NoFrame)
        self.frame_btn_options.setFrameShadow(QFrame.Plain)
        self.gridLayout_5 = QGridLayout(self.frame_btn_options)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 5)
        self.btn_side_options_pssib = QToolButton(self.frame_btn_options)
        self.btn_side_options_pssib.setObjectName(u"btn_side_options_pssib")
        self.btn_side_options_pssib.setMinimumSize(QSize(0, 20))
        self.btn_side_options_pssib.setMaximumSize(QSize(16777215, 16777215))
        self.btn_side_options_pssib.setStyleSheet(u"QToolButton{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #0954B2;\n"
"	border-radius: 2px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QToolButton:hover{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(26, 60, 102);\n"
"	border-radius: 2px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QToolButton:pressed{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:#0954B2;\n"
"	border-radius: 2px;\n"
"	border-top-color: rgb(4, 35, 38);\n"
"	border-left-color:  rgb(4, 35, 38);\n"
"}")
        self.btn_side_options_pssib.setIconSize(QSize(16, 16))
        self.btn_side_options_pssib.setPopupMode(QToolButton.DelayedPopup)
        self.btn_side_options_pssib.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        self.btn_side_options_pssib.setAutoRaise(True)

        self.gridLayout_5.addWidget(self.btn_side_options_pssib, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(864, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame_btn_options, 0, 0, 1, 1)

        self.frame_side_options = QFrame(self.frame_options)
        self.frame_side_options.setObjectName(u"frame_side_options")
        self.frame_side_options.setMinimumSize(QSize(0, 0))
        self.frame_side_options.setMaximumSize(QSize(16777215, 0))
        self.frame_side_options.setStyleSheet(u"background-color: #4195FF;")
        self.frame_side_options.setFrameShape(QFrame.NoFrame)
        self.frame_side_options.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_side_options)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(10, 0, 0, 40)
        self.lb_comb_oods = QLabel(self.frame_side_options)
        self.lb_comb_oods.setObjectName(u"lb_comb_oods")
        self.lb_comb_oods.setMinimumSize(QSize(0, 30))
        self.lb_comb_oods.setMaximumSize(QSize(16777215, 30))
        self.lb_comb_oods.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.lb_comb_oods, 0, 0, 1, 1)

        self.spin_odds = QDoubleSpinBox(self.frame_side_options)
        self.spin_odds.setObjectName(u"spin_odds")
        self.spin_odds.setMinimumSize(QSize(70, 30))
        self.spin_odds.setMaximumSize(QSize(70, 30))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(False)
        self.spin_odds.setFont(font5)
        self.spin_odds.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.spin_odds, 0, 1, 1, 1)

        self.cb_filter_odds = QComboBox(self.frame_side_options)
        self.cb_filter_odds.addItem("")
        self.cb_filter_odds.addItem("")
        self.cb_filter_odds.setObjectName(u"cb_filter_odds")
        self.cb_filter_odds.setMinimumSize(QSize(0, 30))
        self.cb_filter_odds.setFont(font2)
        self.cb_filter_odds.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.cb_filter_odds, 0, 2, 1, 1)

        self.cb_filter_odds_2 = QComboBox(self.frame_side_options)
        self.cb_filter_odds_2.addItem("")
        self.cb_filter_odds_2.addItem("")
        self.cb_filter_odds_2.setObjectName(u"cb_filter_odds_2")
        self.cb_filter_odds_2.setMinimumSize(QSize(150, 30))
        self.cb_filter_odds_2.setFont(font2)
        self.cb_filter_odds_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.cb_filter_odds_2, 0, 3, 1, 1)

        self.btn_filter = QPushButton(self.frame_side_options)
        self.btn_filter.setObjectName(u"btn_filter")
        self.btn_filter.setMinimumSize(QSize(100, 30))
        self.btn_filter.setStyleSheet(u"QPushButton{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #0954B2;\n"
"	border-radius: 8px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(26, 60, 102);\n"
"	border-radius: 8px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:#0954B2;\n"
"	border-radius: 8px;\n"
"	border-top-color: rgb(4, 35, 38);\n"
"	border-left-color:  rgb(4, 35, 38);\n"
"}")

        self.gridLayout.addWidget(self.btn_filter, 0, 4, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(420, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 0, 5, 1, 1)


        self.gridLayout_3.addWidget(self.frame_side_options, 1, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_options)

        self.frame_tb = QFrame(self.frame)
        self.frame_tb.setObjectName(u"frame_tb")
        self.frame_tb.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_tb.setFrameShape(QFrame.StyledPanel)
        self.frame_tb.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_tb)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.tb_view = QTableWidget(self.frame_tb)
        if (self.tb_view.columnCount() < 15):
            self.tb_view.setColumnCount(15)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem30.setFont(font1);
        __qtablewidgetitem30.setIcon(icon8);
        self.tb_view.setHorizontalHeaderItem(0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem31.setFont(font1);
        __qtablewidgetitem31.setIcon(icon8);
        self.tb_view.setHorizontalHeaderItem(1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem32.setFont(font1);
        __qtablewidgetitem32.setIcon(icon8);
        self.tb_view.setHorizontalHeaderItem(2, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem33.setFont(font1);
        __qtablewidgetitem33.setIcon(icon8);
        self.tb_view.setHorizontalHeaderItem(3, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem34.setFont(font1);
        __qtablewidgetitem34.setIcon(icon8);
        self.tb_view.setHorizontalHeaderItem(4, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem35.setFont(font1);
        __qtablewidgetitem35.setIcon(icon8);
        self.tb_view.setHorizontalHeaderItem(5, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setFont(font1);
        __qtablewidgetitem36.setIcon(icon8);
        self.tb_view.setHorizontalHeaderItem(6, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setFont(font1);
        __qtablewidgetitem37.setIcon(icon8);
        self.tb_view.setHorizontalHeaderItem(7, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setFont(font1);
        __qtablewidgetitem38.setIcon(icon8);
        self.tb_view.setHorizontalHeaderItem(8, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setFont(font1);
        __qtablewidgetitem39.setIcon(icon8);
        self.tb_view.setHorizontalHeaderItem(9, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setFont(font1);
        __qtablewidgetitem40.setIcon(icon8);
        self.tb_view.setHorizontalHeaderItem(10, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setFont(font1);
        __qtablewidgetitem41.setIcon(icon8);
        self.tb_view.setHorizontalHeaderItem(11, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setFont(font1);
        __qtablewidgetitem42.setIcon(icon8);
        self.tb_view.setHorizontalHeaderItem(12, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setFont(font1);
        __qtablewidgetitem43.setIcon(icon8);
        self.tb_view.setHorizontalHeaderItem(13, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setFont(font1);
        __qtablewidgetitem44.setIcon(icon8);
        self.tb_view.setHorizontalHeaderItem(14, __qtablewidgetitem44)
        self.tb_view.setObjectName(u"tb_view")
        self.tb_view.setFont(font2)
        self.tb_view.setToolTipDuration(-3)
        self.tb_view.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"background-color:rgb(243, 243, 243);\n"
"")
        self.tb_view.setFrameShape(QFrame.StyledPanel)
        self.tb_view.setFrameShadow(QFrame.Raised)
        self.tb_view.setAutoScrollMargin(20)
        self.tb_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_view.setDragEnabled(False)
        self.tb_view.setAlternatingRowColors(True)
        self.tb_view.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.tb_view.setIconSize(QSize(0, 0))
        self.tb_view.setTextElideMode(Qt.ElideRight)
        self.tb_view.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tb_view.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tb_view.setSortingEnabled(True)
        self.tb_view.setColumnCount(15)
        self.tb_view.horizontalHeader().setMinimumSectionSize(50)
        self.tb_view.horizontalHeader().setDefaultSectionSize(150)
        self.tb_view.verticalHeader().setVisible(False)
        self.tb_view.verticalHeader().setDefaultSectionSize(50)
        self.tb_view.verticalHeader().setProperty("showSortIndicator", True)

        self.verticalLayout_6.addWidget(self.tb_view)


        self.verticalLayout_5.addWidget(self.frame_tb)


        self.horizontalLayout_5.addWidget(self.frame)

        self.pages.addWidget(self.page_possibilities)

        self.horizontalLayout_3.addWidget(self.pages)


        self.verticalLayout_3.addWidget(self.frame_pages)

        self.frame_footer = QFrame(self.frame_content)
        self.frame_footer.setObjectName(u"frame_footer")
        self.frame_footer.setMinimumSize(QSize(0, 35))
        self.frame_footer.setMaximumSize(QSize(16777215, 35))
        self.frame_footer.setStyleSheet(u"background-color: #0954B2;\n"
"border-radius: 2px;\n"
"")
        self.frame_footer.setFrameShape(QFrame.NoFrame)
        self.frame_footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_footer)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lb_commom = QLabel(self.frame_footer)
        self.lb_commom.setObjectName(u"lb_commom")
        self.lb_commom.setStyleSheet(u"font: 75 9pt \"MS Shell Dlg 2\";\n"
"color: #fff;\n"
"")
        self.lb_commom.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lb_commom)


        self.verticalLayout_3.addWidget(self.frame_footer)


        self.horizontalLayout.addWidget(self.frame_content)


        self.verticalLayout_10.addWidget(self.fram_bot)

        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)

        self.btn_about.setDefault(False)
        self.pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Modulo Principal", None))
        self.btn_menu.setText("")
#if QT_CONFIG(shortcut)
        self.btn_menu.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.btn_coletar.setText(QCoreApplication.translate("Main", u"Coletar Odds       ", None))
        self.btn_visJogos.setText(QCoreApplication.translate("Main", u"Visualizar Jogos    ", None))
        self.btn_visProbabilidades.setText(QCoreApplication.translate("Main", u"Possibilidaes         ", None))
        self.btn_previsoes.setText(QCoreApplication.translate("Main", u"Previs\u00f5es              ", None))
        self.btn_calculator.setText(QCoreApplication.translate("Main", u"Calculadora           ", None))
        self.btn_about.setText(QCoreApplication.translate("Main", u"Sobre", None))
        self.rb_games_betano.setText(QCoreApplication.translate("Main", u"Jogos Betano", None))
        self.rb_games_esporte365.setText(QCoreApplication.translate("Main", u"Esporte365", None))
        self.rb_games_pixbet.setText(QCoreApplication.translate("Main", u"Jogos Pixbet", None))
        ___qtablewidgetitem = self.tb_view_games.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem1 = self.tb_view_games.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem2 = self.tb_view_games.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem3 = self.tb_view_games.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem4 = self.tb_view_games.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem5 = self.tb_view_games.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem6 = self.tb_view_games.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem7 = self.tb_view_games.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem8 = self.tb_view_games.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem9 = self.tb_view_games.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem10 = self.tb_view_games.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem11 = self.tb_view_games.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem12 = self.tb_view_games.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem13 = self.tb_view_games.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem14 = self.tb_view_games.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Main", u"New Column", None));
        self.lb_collect_animation.setText("")
        self.lb_text_animation.setText("")
        self.btn_side_options_season.setText(QCoreApplication.translate("Main", u"...", None))
        self.btn_update_base.setText(QCoreApplication.translate("Main", u"Atualizar Base", None))
        self.cb_camp.setItemText(0, QCoreApplication.translate("Main", u"Argentina Primera Division", None))
        self.cb_camp.setItemText(1, QCoreApplication.translate("Main", u"Australian A-League", None))
        self.cb_camp.setItemText(2, QCoreApplication.translate("Main", u"Austrian T-Mobile Bundesliga", None))
        self.cb_camp.setItemText(3, QCoreApplication.translate("Main", u"Barclays Premier League", None))
        self.cb_camp.setItemText(4, QCoreApplication.translate("Main", u"Belgian Jupiler League", None))
        self.cb_camp.setItemText(5, QCoreApplication.translate("Main", u"Brasileiro S\u00e9rie A", None))
        self.cb_camp.setItemText(6, QCoreApplication.translate("Main", u"Chinese Super League", None))
        self.cb_camp.setItemText(7, QCoreApplication.translate("Main", u"Danish SAS-Ligaen", None))
        self.cb_camp.setItemText(8, QCoreApplication.translate("Main", u"Dutch Eredivisie", None))
        self.cb_camp.setItemText(9, QCoreApplication.translate("Main", u"English League Championship", None))
        self.cb_camp.setItemText(10, QCoreApplication.translate("Main", u"English League One", None))
        self.cb_camp.setItemText(11, QCoreApplication.translate("Main", u"English League Two", None))
        self.cb_camp.setItemText(12, QCoreApplication.translate("Main", u"FA Women's Super League", None))
        self.cb_camp.setItemText(13, QCoreApplication.translate("Main", u"French Ligue 1", None))
        self.cb_camp.setItemText(14, QCoreApplication.translate("Main", u"French Ligue 2", None))
        self.cb_camp.setItemText(15, QCoreApplication.translate("Main", u"German 2. Bundesliga", None))
        self.cb_camp.setItemText(16, QCoreApplication.translate("Main", u"German Bundesliga", None))
        self.cb_camp.setItemText(17, QCoreApplication.translate("Main", u"Greek Super League", None))
        self.cb_camp.setItemText(18, QCoreApplication.translate("Main", u"Italy Serie A", None))
        self.cb_camp.setItemText(19, QCoreApplication.translate("Main", u"Italy Serie B", None))
        self.cb_camp.setItemText(20, QCoreApplication.translate("Main", u"Japanese J League", None))
        self.cb_camp.setItemText(21, QCoreApplication.translate("Main", u"Major League Soccer", None))
        self.cb_camp.setItemText(22, QCoreApplication.translate("Main", u"Mexican Primera Division Torneo Apertura", None))
        self.cb_camp.setItemText(23, QCoreApplication.translate("Main", u"Mexican Primera Division Torneo Clausura", None))
        self.cb_camp.setItemText(24, QCoreApplication.translate("Main", u"NWSL Challenge Cup", None))
        self.cb_camp.setItemText(25, QCoreApplication.translate("Main", u"National Women's Soccer League", None))
        self.cb_camp.setItemText(26, QCoreApplication.translate("Main", u"Norwegian Tippeligaen", None))
        self.cb_camp.setItemText(27, QCoreApplication.translate("Main", u"Portuguese Liga", None))
        self.cb_camp.setItemText(28, QCoreApplication.translate("Main", u"Russian Premier Liga", None))
        self.cb_camp.setItemText(29, QCoreApplication.translate("Main", u"Scottish Premiership", None))
        self.cb_camp.setItemText(30, QCoreApplication.translate("Main", u"South African ABSA Premier League", None))
        self.cb_camp.setItemText(31, QCoreApplication.translate("Main", u"Spanish Primera Division", None))
        self.cb_camp.setItemText(32, QCoreApplication.translate("Main", u"Spanish Segunda Division", None))
        self.cb_camp.setItemText(33, QCoreApplication.translate("Main", u"Swedish Allsvenskan", None))
        self.cb_camp.setItemText(34, QCoreApplication.translate("Main", u"Swiss Raiffeisen Super League", None))
        self.cb_camp.setItemText(35, QCoreApplication.translate("Main", u"Turkish Turkcell Super Lig", None))
        self.cb_camp.setItemText(36, QCoreApplication.translate("Main", u"UEFA Champions League", None))
        self.cb_camp.setItemText(37, QCoreApplication.translate("Main", u"UEFA Europa Conference League", None))
        self.cb_camp.setItemText(38, QCoreApplication.translate("Main", u"UEFA Europa League", None))
        self.cb_camp.setItemText(39, QCoreApplication.translate("Main", u"United Soccer League", None))

        self.cb_games.setItemText(0, QCoreApplication.translate("Main", u"Todos", None))
        self.cb_games.setItemText(1, QCoreApplication.translate("Main", u"Jogos Futuros", None))
        self.cb_games.setItemText(2, QCoreApplication.translate("Main", u"Jogos Passados", None))

        self.le_team1.setPlaceholderText(QCoreApplication.translate("Main", u"Mandante", None))
        self.le_team2.setPlaceholderText(QCoreApplication.translate("Main", u"Visitante", None))
#if QT_CONFIG(whatsthis)
        self.btn_search.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.btn_search.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.btn_search.setText(QCoreApplication.translate("Main", u"Pesquisar", None))
        ___qtablewidgetitem15 = self.tb_preview.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem16 = self.tb_preview.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem17 = self.tb_preview.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem18 = self.tb_preview.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem19 = self.tb_preview.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem20 = self.tb_preview.horizontalHeaderItem(5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem21 = self.tb_preview.horizontalHeaderItem(6)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem22 = self.tb_preview.horizontalHeaderItem(7)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem23 = self.tb_preview.horizontalHeaderItem(8)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem24 = self.tb_preview.horizontalHeaderItem(9)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem25 = self.tb_preview.horizontalHeaderItem(10)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem26 = self.tb_preview.horizontalHeaderItem(11)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem27 = self.tb_preview.horizontalHeaderItem(12)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem28 = self.tb_preview.horizontalHeaderItem(13)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem29 = self.tb_preview.horizontalHeaderItem(14)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("Main", u"New Column", None));
        self.btn_side_options_pssib.setText(QCoreApplication.translate("Main", u"...", None))
        self.lb_comb_oods.setText(QCoreApplication.translate("Main", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Odds mair que:</span></p></body></html>", None))
        self.cb_filter_odds.setItemText(0, QCoreApplication.translate("Main", u"Todos", None))
        self.cb_filter_odds.setItemText(1, QCoreApplication.translate("Main", u"Somente oportunidades", None))

        self.cb_filter_odds_2.setItemText(0, QCoreApplication.translate("Main", u"Dados Pixbet", None))
        self.cb_filter_odds_2.setItemText(1, QCoreApplication.translate("Main", u"Dados Betano", None))

        self.btn_filter.setText(QCoreApplication.translate("Main", u"Filtrar", None))
        ___qtablewidgetitem30 = self.tb_view.horizontalHeaderItem(0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem31 = self.tb_view.horizontalHeaderItem(1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem32 = self.tb_view.horizontalHeaderItem(2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem33 = self.tb_view.horizontalHeaderItem(3)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem34 = self.tb_view.horizontalHeaderItem(4)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem35 = self.tb_view.horizontalHeaderItem(5)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem36 = self.tb_view.horizontalHeaderItem(6)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem37 = self.tb_view.horizontalHeaderItem(7)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem38 = self.tb_view.horizontalHeaderItem(8)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem39 = self.tb_view.horizontalHeaderItem(9)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem40 = self.tb_view.horizontalHeaderItem(10)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem41 = self.tb_view.horizontalHeaderItem(11)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem42 = self.tb_view.horizontalHeaderItem(12)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem43 = self.tb_view.horizontalHeaderItem(13)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("Main", u"New Column", None));
        ___qtablewidgetitem44 = self.tb_view.horizontalHeaderItem(14)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("Main", u"New Column", None));
        self.lb_commom.setText(QCoreApplication.translate("Main", u"Todos os direitos reservados \u00a9  MaTTecnologia Aplicada 2022", None))
    # retranslateUi

