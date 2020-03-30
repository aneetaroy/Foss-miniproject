import os
import sys 
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
 
def main(): 
    app = QApplication(sys.argv) 
    w = MyWindow() 
    w.show() 
    sys.exit(app.exec_()) 
 
class MyWindow(QWidget): 
    def __init__(self, *args): 
        QWidget.__init__(self, *args) 
 
  
        label = QLabel(self.tr("Enter PID and Press ENTER"))
        self.le = QLineEdit()
        self.te = QTextEdit()
	
        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(self.le)
        layout.addWidget(self.te)
        self.setLayout(layout) 
	

        self.connect(self.le, SIGNAL("returnPressed(void)"),
                     self.run_command)
	
    def run_command(self):
        cmd = 'cat /proc/1531/environ'
        stdouterr = os.popen4(cmd)[1].read()
        self.te.setText(stdouterr)
  
if __name__ == "__main__": 
    main()

