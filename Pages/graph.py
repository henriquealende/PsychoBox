import pandas as pd

from expandGraph import *
from Database.database import *
from Utils.graph_utils import *
from Utils.filter_utils import *   
##############################################################################

class UI_Buttons_Graph():
    def __init__(self):
        super(UI_Buttons_Graph, self).__init__()

        global pathExport, dados

    def graphButton(self):
       if self.online:
            self.ui.rightContent.setCurrentWidget(self.ui.graphPage)

    def importButton(self):
        global path
        importAdress = QFileDialog.getOpenFileName(self,'Open file','','WAV files (*.wav)')
        importPathname = importAdress[0]
        filename = os.path.basename(str(importPathname))
        path = os.path.dirname(str(importPathname))
        self.ui.listWidget2.addItem(filename)

    def selectItem(self):
        global path, pathExport   

        #presetImport(self, domain)
        filename = str(self.ui.listWidget2.currentItem().text())  
        self.pathname = (path + '/' + filename)
        #selectMulti(self, metrics, domain, samplingBox)
        pathExport = self.pathname
        self.ui.plot.setEnabled(True)

#    def getPathname(self):
#        return pathExport

    def expandGraph(self, type):
        global dados
        dados = ['metrics', 'domain', 'samplingBox']
        dados[0] = 'Time-Frequency'
        dados[1] = 'Time'
        dados[2] ='Linear'
        self.gp = Expand_Graph(dados, pathExport, type)
        self.gp.show()


    def showSettings(self, x):
        if x == 'show':
            self.gp.frame_21.show()
            self.gp.pushButton2.hide()
            self.gp.pushButton2_2.show()
        else:
            self.gp.frame_21.hide()
            self.gp.pushButton2.show()
            self.gp.pushButton2_2.hide()

    def changeGraph(self):
        metrics = self.gp.mainBox.currentText()
        domain = self.gp.domainBox.currentText()
        samplingBox = self.gp.samplingBox.currentText()
        self.chartview = getGraph(self, metrics, domain, samplingBox, type ='plot', window='expand')


    def saveGraph(self):
        from Utils.graph_utils import chartView
        #global chartView
        x = chartView
        fileName, _ = QFileDialog.getSaveFileName(
            self, "Save Image", r"H:\Image", "Image Files (*.png *.jpg *.bmp)")
        fileName = fileName + '.png'
        image = x.grab()
        #image.scaled(1000, 1000)
        image.save(fileName)

#    def saveData(self):
#        from Utils.graph_utils import x, y
#        lista_xy = list(zip(x, y))
#        df = pd.DataFrame(lista_xy, columns=['x', 'y'])
#        name = QFileDialog.getSaveFileName(self, 'Save File', filter='*.csv')
#        df.to_csv(name[0], index = False, sep = ";")

