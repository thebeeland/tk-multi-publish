"""
Copyright (c) 2013 Shotgun Software, Inc
----------------------------------------------------
"""

import tank
from tank.platform.qt import QtCore, QtGui

class GroupHeader(QtGui.QWidget):
    """
    """
    def __init__(self, group_name, parent=None):
        """
        Construction
        """
        QtGui.QWidget.__init__(self, parent)
    
        # set up the UI
        from .ui.group_header import Ui_GroupHeader
        self._ui = Ui_GroupHeader() 
        self._ui.setupUi(self)
        
        self.name = group_name
        
    @property
    def name(self):
        return self._ui.name_label.toPlainText()
    @name.setter
    def name(self, value):
        self._ui.name_label.setText(value)