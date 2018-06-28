from PyQt5 import QtCore, QtWidgets, QtGui
import sys, math


class DrawingWidget(QtWidgets.QWidget):
    def __init__(self, data, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.flag = False
        self.distances = data
        self.scale = QtCore.QPointF(1,1)
        self.translate = QtCore.QPointF(0,0)
        self.previous_mouse_pos = QtCore.QPoint(0,0)

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.scale(self.scale.x(),self.scale.y())
        qp.translate(self.translate)
        self.drawBackgrounds(qp)
        if self.flag :
            self.drawDistances(qp)
        qp.end()

    def flag_start(self) :
        self.flag = True
        self.update()

    def flag_stop(self) :
        self.flag = False
        self.update()

    def update_with(self,data) :
        self.distances = data
        self.update()

    def drawBackgrounds(self,qp) :
        midh = self.height()/2
        midw = self.width()/2
        col = QtGui.QColor(0, 0, 0)
        pen = QtGui.QPen(col) 
        pen.setWidth(1)
        brush = QtGui.QBrush(QtGui.QColor(40,40,40))
        qp.setPen(pen)
        maxi = max(midh,midw)
        mini = min(midh,midw)

        for i in range(1,7):
            qp.drawEllipse(QtCore.QPointF(midw,midh), i*midh/6, i*midh/6);

        pen.setWidth(2)
        qp.setBrush(brush)
        Linex = QtCore.QLineF(-midw,midh, self.width()+midw, midh);
        qp.drawLine(Linex)
        Liney = QtCore.QLineF(midw,0, midw, self.height());
        qp.drawLine(Liney)


        angle_mort = [(midw,midh),(midw-maxi,midh+maxi),(midw+maxi,midh+maxi)]
        polygon = self.createPoly(angle_mort)
        qp.setBrush(brush)  
        qp.drawPolygon(polygon)


    def drawDistances(self,qp) :
        midh = self.height()/2
        midw = self.width()/2
        Points = [(midw,midh)]
        for i,d in enumerate(self.distances) :
            if d > 6000 :
                d = 6000
            d = midh/6000*d
            angle_deg = -45+i*270/541
            angle_rad = math.radians(angle_deg)
            Points.append((midw+math.cos(angle_rad)*d,midh-math.sin(angle_rad)*d))
        polygon = self.createPoly(Points)
        pen = QtGui.QPen(QtGui.QColor(0,255,0))
        pen.setWidth(1)
        if self.scale.x() > 5 :
            pen.setWidth(0)
        brush = QtGui.QBrush(QtGui.QColor(153, 255, 102,220))
        qp.setPen(pen)
        qp.setBrush(brush)  
        qp.drawPolygon(polygon)

    def createPoly(self,Points):
        polygon = QtGui.QPolygonF() 
        for point in Points :
            polygon.append(QtCore.QPointF(point[0],point[1]))  
        return polygon

    def wheelEvent (self,event) :
        rescale = self.scale.x()*event.angleDelta().y()/1200
        self.scale += QtCore.QPointF(rescale,rescale) 
        self.update()

    def keyPressEvent(self,event) :
        if event.key() == 16777234 :
            self.translate += QtCore.QPointF(10,0)
        if event.key() == 16777235 :
            self.translate += QtCore.QPointF(0,10)
        if event.key() == 16777236 :
            self.translate += QtCore.QPointF(-10,0)
        if event.key() == 16777237 :
            self.translate += QtCore.QPointF(0,-10)
        self.update()

    def mousePressEvent(self,event) :
        self.setFocus()
        self.setMouseTracking(True)
        self.previous_mouse_pos = event.pos()

    def mouseReleaseEvent(self,event) :
        self.setMouseTracking(False)

    def mouseMoveEvent(self,event) :
        if self.hasMouseTracking() :
            mouse_translate = event.pos() - self.previous_mouse_pos
            self.translate += mouse_translate/self.scale.x()
            self.previous_mouse_pos = event.pos()
            self.update()
