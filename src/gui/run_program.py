from PySide.QtGui import *
import sys
from customerUI import Welcome

app = QApplication(sys.argv)
form = Welcome()
form.setFocus()
form.show()
app.exec_()
