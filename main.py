# -*- coding:utf-8 -*-
from PyQt4.QtGui import *
import gui_v2
import sys
 
class XWindow(QMainWindow, gui_v2.Ui_mainWindow):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        
        # # 버튼 이벤트 핸들러
        # self.btnSave.clicked.connect(self.saveData)
        # self.btnQuit.clicked.connect(self.closed())
    
    # # 저장 버튼 클릭시
    # def saveData(self):
    #     with open("data.csv", "a", encoding="utf-8") as f:
    #         s = "%s,%s,%s\n" % (self.editName.text(),
    #                             self.editCompany.text(),
    #                             self.editAddr.text())
    #         f.write(s)
    #     QMessageBox.information(self, "저장", "성공적으로 저장")
 
    # # 취소 버튼 클릭시
    # def clearData(self):
    #     self.editName.clear()
    #     self.editCompany.clear()
    #     self.editAddr.clear()
 
app = QApplication(sys.argv)
dlg = XWindow()
dlg.show()
app.exec_()