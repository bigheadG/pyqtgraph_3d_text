'''
import pyqtgraph.examples
pyqtgraph.examples.run()
'''

import pyqtgraph as pg
import pyqtgraph.opengl as gl
from pyqtgraph.Qt import mkQApp ,QtGui
import numpy as np
 

app = mkQApp("GLTextItem Example")

gvw = gl.GLViewWidget()
gvw.show()
gvw.setWindowTitle('pyqtgraph example: GLTextItem')

griditem = gl.GLGridItem()
griditem.setSize(10, 10)
griditem.setSpacing(1, 1)
gvw.addItem(griditem)


def coordText(gl,gview,x=None,y=None,z=None,fontSize = None):
	axisitem = gl.GLAxisItem()
	axisitem.setSize(x=x,y=y,z=z)
	gview.addItem(axisitem)
	size = 10 if fontSize == None else fontSize
	xo = np.linspace(1, x, x)
	yo = np.linspace(1, y, y)
	zo = np.linspace(1, z, z)
	
	for i in range(len(xo)):
		axisX = gl.GLTextItem(pos=(xo[i], 0.0, 0.0),  text=f'{xo[i]}' if i != len(xo)-1 else 'X' ,color=(255, 127, 127, 255),font=QtGui.QFont('Helvetica', size))
		gview.addItem(axisX)
	for i in range(len(yo)):
		axisY = gl.GLTextItem(pos=( 0.0, yo[i], 0.0), text=f'{yo[i]}' if i != len(yo)-1 else 'Y' ,color=(127, 255, 127, 255),font=QtGui.QFont('Helvetica', size))
		gview.addItem(axisY)
	for i in range(len(zo)):
		axisZ = gl.GLTextItem(pos=( 0.0, 0.0, zo[i]), text=f'{zo[i]}' if i != len(zo)-1 else 'Z' ,color=(127, 127, 255, 255),font=QtGui.QFont('Helvetica', size))
		gview.addItem(axisZ)

coordText(gl,gvw,x=5,y=5,z=5,fontSize = 12)

if __name__ == '__main__':
  pg.exec()

