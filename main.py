import os.path

from ui.ui_mainwindow import Ui_MainWindow

from PySide6.QtWidgets import QMainWindow
from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from PySide6.QtCore import Qt
import sys
from changer import WallpaperChanger
from config import *
from PIL import Image
from pystray import MenuItem


CONFIG_DIR = "workDir"
CONFIG_DURATION = "duration"
CONFIG_CLOSE = "close"
CONFIG_BOOT = "boot"
CONFIG_DISORDER = "disorder"


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()  # 加载UI转换成的代码窗口
        self.ui.setupUi(self)
        self.__connect()
        self.changer: WallpaperChanger = None
        self.flag_running = False
        self.__init_config()
        self.__init_ui()

    def __init_config(self):
        self.config = get_config()
        if len(self.config.items()) == 0:
            self.config[CONFIG_DIR] = os.path.abspath(".")
            self.config[CONFIG_DURATION] = 1
            self.config[CONFIG_CLOSE] = True
            self.config[CONFIG_BOOT] = False
            self.config[CONFIG_DISORDER] = False
            set_config(self.config)

    def __init_ui(self):
        self.ui.lineEdit_dir.setText(self.config[CONFIG_DIR])
        self.ui.spinBox_min.setValue(self.config[CONFIG_DURATION])
        self.ui.checkBox_close.setChecked(self.config[CONFIG_CLOSE])
        self.ui.checkBox_boot.setChecked(self.config[CONFIG_BOOT])
        self.ui.checkBox_disorder.setChecked(self.config[CONFIG_DISORDER])
        self.ui.label_msg.setText("")
        self.ui.label_status.setText("当前是手动切换模式")

    def __save_config(self):
        self.config[CONFIG_DIR] = self.ui.lineEdit_dir.text()
        self.config[CONFIG_DURATION] = self.ui.spinBox_min.value()
        self.config[CONFIG_CLOSE] = self.ui.checkBox_close.isChecked()
        self.config[CONFIG_BOOT] = self.ui.checkBox_boot.isChecked()
        self.config[CONFIG_DISORDER] = self.ui.checkBox_disorder.isChecked()
        set_config(self.config)

    @Slot()
    def __open_dir_selector(self):
        old_directory = self.ui.lineEdit_dir.text()
        if old_directory == "":
            old_directory = "./"
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "getExistingDirectory", old_directory)
        if directory != "":
            self.ui.lineEdit_dir.setText(directory)
            if directory != old_directory:
                self.__update_changer()
                self.__save_config()

    def __connect(self):
        self.ui.pushButton_selectpath.clicked.connect(self.__open_dir_selector)
        self.ui.pushButton_next.clicked.connect(self.__next)
        self.ui.pushButton_previous.clicked.connect(self.__previous)
        self.ui.pushButton_auto.clicked.connect(self.__auto_run)
        self.ui.checkBox_disorder.stateChanged.connect(self.__auto_boot_changed)

    @Slot(Qt.CheckState)
    def __auto_boot_changed(self, checked):
        print("auto boot changed:", checked)
        if checked == Qt.CheckState.Checked:
            self.config[CONFIG_BOOT] = True
        else:
            self.config[CONFIG_BOOT] = False

    def __update_changer(self):
        if self.changer is not None:
            self.changer.stop()
        self.changer = WallpaperChanger(self.ui.lineEdit_dir.text())

    def __no_pic_err(self):
        QtWidgets.QMessageBox(self, "错误", "请检查目录下是否存在图片！")

    @Slot()
    def __previous(self):
        if self.changer.valid() != 0:
            self.__no_pic_err()
        self.changer.previous()

    @Slot()
    def __next(self):
        if self.changer.valid() != 0:
            self.__no_pic_err()
        self.changer.next()

    @Slot()
    def __auto_run(self):
        if self.flag_running is False:
            self.changer.set_disorder(self.ui.checkBox_disorder.isChecked())
            self.changer.set_duration(int(self.ui.spinBox_min.text()))
            self.changer.run()
            if self.changer.is_running():
                self.__switch_to_running_ui()
                self.flag_running = True
        else:
            self.changer.stop()
            self.__switch_to_stop_ui()
            self.flag_running = False

    def __switch_to_running_ui(self):
        self.ui.lineEdit_dir.setEnabled(False)
        self.ui.pushButton_selectpath.setEnabled(False)
        self.ui.spinBox_min.setEnabled(False)
        self.ui.checkBox_disorder.setEnabled(False)
        self.ui.checkBox_boot.setEnabled(False)
        self.ui.checkBox_close.setEnabled(False)
        self.ui.label_status.setText("running")
        self.ui.label_status.setStyleSheet("color:green")
        self.ui.pushButton_auto.setText("停止轮换")

    def __switch_to_stop_ui(self):
        self.ui.lineEdit_dir.setEnabled(True)
        self.ui.pushButton_selectpath.setEnabled(True)
        self.ui.spinBox_min.setEnabled(True)
        self.ui.checkBox_disorder.setEnabled(True)
        self.ui.checkBox_boot.setEnabled(True)
        self.ui.checkBox_close.setEnabled(True)
        self.ui.label_status.setText("stopped")
        self.ui.label_status.setStyleSheet("color:red")
        self.ui.pushButton_auto.setText("自动轮换")

    def __output_msg(self, msg, color="black"):
        self.ui.label_msg.setText(msg)
        self.ui.label_msg.setStyleSheet("color:%s" % color)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = MainWindow()
    gui.show()
    sys.exit(app.exec())
