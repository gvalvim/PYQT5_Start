#import libraries
import sys
import os

from PyQt5 import uic, QtWidgets

ui_path = os.path.dirname(os.path.abspath(__file__))

#Change the NAME with the name of your UI file with out the .ui
class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        uic.loadUi(os.path.join(ui_path, "NAME.ui"), self)

        #Add buttons here and connect to the functions


    #Add function here



if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
