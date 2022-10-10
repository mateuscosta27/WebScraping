
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1136, 685)
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_top = QtWidgets.QFrame(self.centralwidget)
        self.frame_top.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_top.setStyleSheet("background-color: #0954B2;")
        self.frame_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_btn_menu = QtWidgets.QFrame(self.frame_top)
        self.frame_btn_menu.setMinimumSize(QtCore.QSize(0, 35))
        self.frame_btn_menu.setMaximumSize(QtCore.QSize(100, 35))
        self.frame_btn_menu.setStyleSheet("background-color:#0954B2;")
        self.frame_btn_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_btn_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btn_menu.setObjectName("frame_btn_menu")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_btn_menu)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_menu = QtWidgets.QPushButton(self.frame_btn_menu)
        self.btn_menu.setMinimumSize(QtCore.QSize(100, 35))
        self.btn_menu.setMaximumSize(QtCore.QSize(0, 35))
        self.btn_menu.setStyleSheet("QPushButton{\n"
"    border-style: none;\n"
"    border-width: 2px;\n"
"    font: 75 14pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #0954B2;\n"
"    border-radius: 12px;\n"
"    border-bottom-color: rgb(4, 35, 38);\n"
"    border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: none;\n"
"    border-width: 2px;\n"
"    font: 75 14pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #4195FF;\n"
"    border-radius: 12px;\n"
"    border-bottom-color: rgb(4, 35, 38);\n"
"    border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"    border-style: none;\n"
"    border-width: 2px;\n"
"    font: 75 14pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:#0954B2;\n"
"    border-radius: 8px;\n"
"    border-top-color: rgb(4, 35, 38);\n"
"    border-left-color:  rgb(4, 35, 38);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/menu_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QtCore.QSize(32, 32))
        self.btn_menu.setObjectName("btn_menu")
        self.horizontalLayout_4.addWidget(self.btn_menu)
        self.horizontalLayout_2.addWidget(self.frame_btn_menu)
        self.frame_info = QtWidgets.QFrame(self.frame_top)
        self.frame_info.setStyleSheet("background-color: rgb(9, 84, 178);")
        self.frame_info.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_info.setObjectName("frame_info")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_info)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_2.addWidget(self.frame_info)
        self.gridLayout.addWidget(self.frame_top, 0, 0, 1, 1)
        self.fram_bot = QtWidgets.QFrame(self.centralwidget)
        self.fram_bot.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fram_bot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fram_bot.setObjectName("fram_bot")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fram_bot)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_side = QtWidgets.QFrame(self.fram_bot)
        self.frame_side.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_side.setMaximumSize(QtCore.QSize(0, 16777215))
        self.frame_side.setStyleSheet("background-color: #FFF;\n"
"border: 2px solid;\n"
"border-left: none;\n"
"border-top: none;\n"
"border-bottom:none;\n"
"border-right-color: #0954B2;")
        self.frame_side.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_side.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_side.setObjectName("frame_side")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_side)
        self.verticalLayout.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_coletar = QtWidgets.QPushButton(self.frame_side)
        self.btn_coletar.setMinimumSize(QtCore.QSize(200, 45))
        self.btn_coletar.setMaximumSize(QtCore.QSize(200, 45))
        self.btn_coletar.setBaseSize(QtCore.QSize(0, 0))
        self.btn_coletar.setStyleSheet("QPushButton{\n"
"    border-style: none;\n"
"    border-width: 2px;\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #4195FF;\n"
"    border-radius: 12px;\n"
"    border-bottom-color: rgb(4, 35, 38);\n"
"    border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: none;\n"
"    border-width: 2px;\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #0954B2;\n"
"    border-radius: 12px;\n"
"    border-bottom-color: rgb(4, 35, 38);\n"
"    border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"    border-style: insetset;\n"
"    border-width: 2px;\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #4195FF;\n"
"    border-radius: 8px;\n"
"    border-top-color: rgb(4, 35, 38);\n"
"    border-left-color:  rgb(4, 35, 38);\n"
"}")
        self.btn_coletar.setText("Coletar Dados")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("src/collect_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_coletar.setIcon(icon1)
        self.btn_coletar.setIconSize(QtCore.QSize(45, 45))
        self.btn_coletar.setObjectName("btn_coletar")
        self.verticalLayout.addWidget(self.btn_coletar, 0, QtCore.Qt.AlignHCenter)
        self.btn_visOdds = QtWidgets.QPushButton(self.frame_side)
        self.btn_visOdds.setMinimumSize(QtCore.QSize(190, 45))
        self.btn_visOdds.setMaximumSize(QtCore.QSize(200, 45))
        self.btn_visOdds.setStyleSheet("QPushButton{\n"
"    border-style: none;\n"
"    border-width: 2px;\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #4195FF;\n"
"    border-radius: 12px;\n"
"    border-bottom-color: rgb(4, 35, 38);\n"
"    border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: none;\n"
"    border-width: 2px;\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #0954B2;\n"
"    border-radius: 12px;\n"
"    border-bottom-color: rgb(4, 35, 38);\n"
"    border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"    border-style: insetset;\n"
"    border-width: 2px;\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #4195FF;\n"
"    border-radius: 8px;\n"
"    border-top-color: rgb(4, 35, 38);\n"
"    border-left-color:  rgb(4, 35, 38);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("src/odds_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_visOdds.setIcon(icon2)
        self.btn_visOdds.setIconSize(QtCore.QSize(45, 45))
        self.btn_visOdds.setObjectName("btn_visOdds")
        self.verticalLayout.addWidget(self.btn_visOdds, 0, QtCore.Qt.AlignHCenter)
        self.btn_visJogos = QtWidgets.QPushButton(self.frame_side)
        self.btn_visJogos.setMinimumSize(QtCore.QSize(200, 45))
        self.btn_visJogos.setMaximumSize(QtCore.QSize(200, 45))
        self.btn_visJogos.setStyleSheet("QPushButton{\n"
"    border-style: none;\n"
"    border-width: 2px;\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #4195FF;\n"
"    border-radius: 12px;\n"
"    border-bottom-color: rgb(4, 35, 38);\n"
"    border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: none;\n"
"    border-width: 2px;\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #0954B2;\n"
"    border-radius: 12px;\n"
"    border-bottom-color: rgb(4, 35, 38);\n"
"    border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"    border-style: insetset;\n"
"    border-width: 2px;\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #4195FF;\n"
"    border-radius: 8px;\n"
"    border-top-color: rgb(4, 35, 38);\n"
"    border-left-color:  rgb(4, 35, 38);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("src/games_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_visJogos.setIcon(icon3)
        self.btn_visJogos.setIconSize(QtCore.QSize(45, 45))
        self.btn_visJogos.setObjectName("btn_visJogos")
        self.verticalLayout.addWidget(self.btn_visJogos, 0, QtCore.Qt.AlignHCenter)
        self.btn_visProbabilidades = QtWidgets.QPushButton(self.frame_side)
        self.btn_visProbabilidades.setMinimumSize(QtCore.QSize(200, 45))
        self.btn_visProbabilidades.setMaximumSize(QtCore.QSize(200, 45))
        self.btn_visProbabilidades.setStyleSheet("QPushButton{\n"
"    border-style: none;\n"
"    border-width: 2px;\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #4195FF;\n"
"    border-radius: 12px;\n"
"    border-bottom-color: rgb(4, 35, 38);\n"
"    border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: none;\n"
"    border-width: 2px;\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #0954B2;\n"
"    border-radius: 12px;\n"
"    border-bottom-color: rgb(4, 35, 38);\n"
"    border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"    border-style: insetset;\n"
"    border-width: 2px;\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #4195FF;\n"
"    border-radius: 8px;\n"
"    border-top-color: rgb(4, 35, 38);\n"
"    border-left-color:  rgb(4, 35, 38);\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("src/possibility_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_visProbabilidades.setIcon(icon4)
        self.btn_visProbabilidades.setIconSize(QtCore.QSize(45, 45))
        self.btn_visProbabilidades.setObjectName("btn_visProbabilidades")
        self.verticalLayout.addWidget(self.btn_visProbabilidades, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 383, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.frame_about = QtWidgets.QFrame(self.frame_side)
        self.frame_about.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_about.setStyleSheet("background-color: rgb(9, 84, 178);")
        self.frame_about.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_about.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_about.setObjectName("frame_about")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_about)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_about = QtWidgets.QPushButton(self.frame_about)
        self.btn_about.setMinimumSize(QtCore.QSize(225, 35))
        self.btn_about.setMaximumSize(QtCore.QSize(230, 35))
        self.btn_about.setStyleSheet("QPushButton{\n"
"    border-style: none;\n"
"    border-width: 2px;\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #0954B2;\n"
"    border-bottom-color: rgb(4, 35, 38);\n"
"    border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: none;\n"
"    border-width: 2px;\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #4195FF;\n"
"    border-radius: 12px;\n"
"    border-bottom-color: rgb(4, 35, 38);\n"
"    border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"    border-style: insetset;\n"
"    border-width: 2px;\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #0954B2;\n"
"    border-radius: 8px;\n"
"    border-top-color: rgb(4, 35, 38);\n"
"    border-left-color:  rgb(4, 35, 38);\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("src/about_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_about.setIcon(icon5)
        self.btn_about.setIconSize(QtCore.QSize(25, 25))
        self.btn_about.setAutoDefault(True)
        self.btn_about.setDefault(False)
        self.btn_about.setFlat(False)
        self.btn_about.setObjectName("btn_about")
        self.verticalLayout_2.addWidget(self.btn_about, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.frame_about, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout.addWidget(self.frame_side)
        self.frame_content = QtWidgets.QFrame(self.fram_bot)
        self.frame_content.setStyleSheet("background-color:#0954B2;")
        self.frame_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_content)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_pages = QtWidgets.QFrame(self.frame_content)
        self.frame_pages.setStyleSheet("background-color: #fff;")
        self.frame_pages.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_pages)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pages = QtWidgets.QStackedWidget(self.frame_pages)
        self.pages.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pages.setAutoFillBackground(False)
        self.pages.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pages.setLineWidth(0)
        self.pages.setObjectName("pages")
        self.page_home = QtWidgets.QWidget()
        self.page_home.setObjectName("page_home")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_home)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.page_home)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lb_collect_animation = QtWidgets.QLabel(self.frame_2)
        self.lb_collect_animation.setText("")
        self.lb_collect_animation.setPixmap(QtGui.QPixmap("src/texte_icon.gif"))
        self.lb_collect_animation.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_collect_animation.setObjectName("lb_collect_animation")
        self.verticalLayout_8.addWidget(self.lb_collect_animation)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.page_home)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lb_text_animation = QtWidgets.QLabel(self.frame_4)
        self.lb_text_animation.setMinimumSize(QtCore.QSize(0, 0))
        self.lb_text_animation.setText("")
        self.lb_text_animation.setPixmap(QtGui.QPixmap("src/texte_icon.gif"))
        self.lb_text_animation.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_text_animation.setObjectName("lb_text_animation")
        self.verticalLayout_7.addWidget(self.lb_text_animation)
        self.gridLayout_2.addWidget(self.frame_4, 1, 0, 1, 1)
        self.pages.addWidget(self.page_home)
        self.page_possibilities = QtWidgets.QWidget()
        self.page_possibilities.setMouseTracking(False)
        self.page_possibilities.setTabletTracking(False)
        self.page_possibilities.setObjectName("page_possibilities")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page_possibilities)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame = QtWidgets.QFrame(self.page_possibilities)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_options = QtWidgets.QFrame(self.frame)
        self.frame_options.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_options.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_options.setStyleSheet("background-color: #4195FF;")
        self.frame_options.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_options.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_options.setLineWidth(1)
        self.frame_options.setObjectName("frame_options")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_options)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.rb_DuplaChance = QtWidgets.QRadioButton(self.frame_options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rb_DuplaChance.sizePolicy().hasHeightForWidth())
        self.rb_DuplaChance.setSizePolicy(sizePolicy)
        self.rb_DuplaChance.setMinimumSize(QtCore.QSize(220, 20))
        self.rb_DuplaChance.setMaximumSize(QtCore.QSize(220, 20))
        self.rb_DuplaChance.setStyleSheet("\n"
"QRadioButton{\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QRadioButton:pressed{\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.rb_DuplaChance.setAutoRepeatDelay(300)
        self.rb_DuplaChance.setAutoRepeatInterval(100)
        self.rb_DuplaChance.setObjectName("rb_DuplaChance")
        self.horizontalLayout_6.addWidget(self.rb_DuplaChance)
        self.rb_matchOdds = QtWidgets.QRadioButton(self.frame_options)
        self.rb_matchOdds.setMinimumSize(QtCore.QSize(220, 20))
        self.rb_matchOdds.setMaximumSize(QtCore.QSize(220, 20))
        self.rb_matchOdds.setStyleSheet("\n"
"QRadioButton{\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QRadioButton:pressed{\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.rb_matchOdds.setObjectName("rb_matchOdds")
        self.horizontalLayout_6.addWidget(self.rb_matchOdds)
        self.rb_ambosMarcam = QtWidgets.QRadioButton(self.frame_options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rb_ambosMarcam.sizePolicy().hasHeightForWidth())
        self.rb_ambosMarcam.setSizePolicy(sizePolicy)
        self.rb_ambosMarcam.setMinimumSize(QtCore.QSize(220, 20))
        self.rb_ambosMarcam.setMaximumSize(QtCore.QSize(220, 20))
        self.rb_ambosMarcam.setStyleSheet("\n"
"QRadioButton{\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QRadioButton:pressed{\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.rb_ambosMarcam.setObjectName("rb_ambosMarcam")
        self.horizontalLayout_6.addWidget(self.rb_ambosMarcam)
        self.rb_totalGols = QtWidgets.QRadioButton(self.frame_options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rb_totalGols.sizePolicy().hasHeightForWidth())
        self.rb_totalGols.setSizePolicy(sizePolicy)
        self.rb_totalGols.setMinimumSize(QtCore.QSize(220, 20))
        self.rb_totalGols.setMaximumSize(QtCore.QSize(220, 20))
        self.rb_totalGols.setStyleSheet("\n"
"QRadioButton{\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QRadioButton:pressed{\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.rb_totalGols.setChecked(True)
        self.rb_totalGols.setAutoRepeat(True)
        self.rb_totalGols.setObjectName("rb_totalGols")
        self.horizontalLayout_6.addWidget(self.rb_totalGols)
        self.verticalLayout_5.addWidget(self.frame_options)
        self.frame_tb = QtWidgets.QFrame(self.frame)
        self.frame_tb.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_tb.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_tb.setObjectName("frame_tb")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_tb)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tb_view = QtWidgets.QTableWidget(self.frame_tb)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tb_view.setFont(font)
        self.tb_view.setToolTipDuration(-3)
        self.tb_view.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(193, 193, 193);\n"
"")
        self.tb_view.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_view.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tb_view.setAutoScrollMargin(20)
        self.tb_view.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_view.setDragEnabled(False)
        self.tb_view.setAlternatingRowColors(True)
        self.tb_view.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.tb_view.setIconSize(QtCore.QSize(0, 0))
        self.tb_view.setColumnCount(15)
        self.tb_view.setObjectName("tb_view")
        self.tb_view.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("src/order_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon6)
        self.tb_view.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setIcon(icon6)
        self.tb_view.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setIcon(icon6)
        self.tb_view.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_view.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_view.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_view.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_view.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_view.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_view.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_view.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_view.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_view.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_view.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_view.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_view.setHorizontalHeaderItem(14, item)
        self.tb_view.horizontalHeader().setDefaultSectionSize(175)
        self.tb_view.horizontalHeader().setMinimumSectionSize(50)
        self.tb_view.verticalHeader().setDefaultSectionSize(50)
        self.tb_view.verticalHeader().setSortIndicatorShown(True)
        self.verticalLayout_6.addWidget(self.tb_view)
        self.verticalLayout_5.addWidget(self.frame_tb)
        self.horizontalLayout_5.addWidget(self.frame)
        self.pages.addWidget(self.page_possibilities)
        self.horizontalLayout_3.addWidget(self.pages)
        self.verticalLayout_3.addWidget(self.frame_pages)
        self.frame_commom = QtWidgets.QFrame(self.frame_content)
        self.frame_commom.setMinimumSize(QtCore.QSize(0, 35))
        self.frame_commom.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_commom.setStyleSheet("background-color: #0954B2;\n"
"border-radius: 2px;\n"
"")
        self.frame_commom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_commom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_commom.setObjectName("frame_commom")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_commom)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_commom)
        self.label_2.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"color: #fff;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.verticalLayout_3.addWidget(self.frame_commom)
        self.horizontalLayout.addWidget(self.frame_content)
        self.gridLayout.addWidget(self.fram_bot, 1, 0, 1, 1)
        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)
        self.pages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Modulo Principal"))
        self.btn_menu.setText(_translate("Main", "Menu"))
        self.btn_visOdds.setText(_translate("Main", "Odds Coletadas"))
        self.btn_visJogos.setText(_translate("Main", "Jogos Coletados"))
        self.btn_visProbabilidades.setText(_translate("Main", "Probabilidades"))
        self.btn_about.setText(_translate("Main", "Sobre"))
        self.rb_DuplaChance.setText(_translate("Main", "Dupla Chance"))
        self.rb_matchOdds.setText(_translate("Main", "Match Odds"))
        self.rb_ambosMarcam.setText(_translate("Main", "Ambos Marcam"))
        self.rb_totalGols.setText(_translate("Main", "Total de Gols"))
        self.tb_view.setSortingEnabled(True)
        item = self.tb_view.horizontalHeaderItem(0)
        item.setText(_translate("Main", "New Column"))
        item = self.tb_view.horizontalHeaderItem(1)
        item.setText(_translate("Main", "New Column"))
        item = self.tb_view.horizontalHeaderItem(2)
        item.setText(_translate("Main", "New Column"))
        item = self.tb_view.horizontalHeaderItem(3)
        item.setText(_translate("Main", "New Column"))
        item = self.tb_view.horizontalHeaderItem(4)
        item.setText(_translate("Main", "New Column"))
        item = self.tb_view.horizontalHeaderItem(5)
        item.setText(_translate("Main", "New Column"))
        item = self.tb_view.horizontalHeaderItem(6)
        item.setText(_translate("Main", "New Column"))
        item = self.tb_view.horizontalHeaderItem(7)
        item.setText(_translate("Main", "New Column"))
        item = self.tb_view.horizontalHeaderItem(8)
        item.setText(_translate("Main", "New Column"))
        item = self.tb_view.horizontalHeaderItem(9)
        item.setText(_translate("Main", "New Column"))
        item = self.tb_view.horizontalHeaderItem(10)
        item.setText(_translate("Main", "New Column"))
        item = self.tb_view.horizontalHeaderItem(11)
        item.setText(_translate("Main", "New Column"))
        item = self.tb_view.horizontalHeaderItem(12)
        item.setText(_translate("Main", "New Column"))
        item = self.tb_view.horizontalHeaderItem(13)
        item.setText(_translate("Main", "New Column"))
        item = self.tb_view.horizontalHeaderItem(14)
        item.setText(_translate("Main", "New Column"))
        self.label_2.setText(_translate("Main", "Todos os direitos reservados ©  MaTTecnologia Aplicada 2022"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())