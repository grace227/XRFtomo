# #########################################################################
# Copyright (c) 2018, UChicago Argonne, LLC. All rights reserved.         #
#                                                                         #
# Copyright 2018. UChicago Argonne, LLC. This software was produced       #
# under U.S. Government contract DE-AC02-06CH11357 for Argonne National   #
# Laboratory (ANL), which is operated by UChicago Argonne, LLC for the    #
# U.S. Department of Energy. The U.S. Government has rights to use,       #
# reproduce, and distribute this software.  NEITHER THE GOVERNMENT NOR    #
# UChicago Argonne, LLC MAKES ANY WARRANTY, EXPRESS OR IMPLIED, OR        #
# ASSUMES ANY LIABILITY FOR THE USE OF THIS SOFTWARE.  If software is     #
# modified to produce derivative works, such modified software should     #
# be clearly marked, so as not to confuse it with the version available   #
# from ANL.                                                               #
#                                                                         #
# Additionally, redistribution and use in source and binary forms, with   #
# or without modification, are permitted provided that the following      #
# conditions are met:                                                     #
#                                                                         #
#     * Redistributions of source code must retain the above copyright    #
#       notice, this list of conditions and the following disclaimer.     #
#                                                                         #
#     * Redistributions in binary form must reproduce the above copyright #
#       notice, this list of conditions and the following disclaimer in   #
#       the documentation and/or other materials provided with the        #
#       distribution.                                                     #
#                                                                         #
#     * Neither the name of UChicago Argonne, LLC, Argonne National       #
#       Laboratory, ANL, the U.S. Government, nor the names of its        #
#       contributors may be used to endorse or promote products derived   #
#       from this software without specific prior written permission.     #
#                                                                         #
# THIS SOFTWARE IS PROVIDED BY UChicago Argonne, LLC AND CONTRIBUTORS     #
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT       #
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS       #
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL UChicago     #
# Argonne, LLC OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,        #
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,    #
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;        #
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER        #
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT      #
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN       #
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE         #
# POSSIBILITY OF SUCH DAMAGE.                                             #
# #########################################################################


from PyQt5 import QtCore, QtWidgets


class SinogramControlsWidget(QtWidgets.QWidget):

    def __init__(self):
        super(SinogramControlsWidget, self).__init__()
        self.initUI()

    def initUI(self):
        button1size = 250
        buton2size = 122.5
        button3size = 73.3
        button4size = 58.75
        # self.sld = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        # self.sld.setMaximumWidth(button1size)
        # self.sld.setMinimumWidth(button1size)
        # self.lcd = QtWidgets.QLCDNumber(self)
        # self.lcd.setMaximumWidth(button1size)
        # self.lcd.setMinimumWidth(button1size)
        self.combo1 = QtWidgets.QComboBox(self)
        self.combo1.setMaximumWidth(button1size)
        self.combo1.setMinimumWidth(button1size)
        self.btn = QtWidgets.QPushButton('center of mass')
        self.btn.setMaximumWidth(button1size)
        self.btn.setMinimumWidth(button1size)
        self.btn2 = QtWidgets.QPushButton("shift data")
        self.btn2.setMaximumWidth(button1size)
        self.btn2.setMinimumWidth(button1size)
        self.btn3 = QtWidgets.QPushButton("X 10")
        self.btn3.setMaximumWidth(button1size)
        self.btn3.setMinimumWidth(button1size)
        self.btn4 = QtWidgets.QPushButton("/ 10")
        self.btn4.setMaximumWidth(button1size)
        self.btn4.setMinimumWidth(button1size)

        hb = QtWidgets.QHBoxLayout()
        hb.addWidget(self.btn3)
        hb.addWidget(self.btn4)
        self.btn3.setVisible(False)
        self.btn4.setVisible(False)
        self.lbl = QtWidgets.QLabel()
        self.lbl.setText("")
        vb = QtWidgets.QVBoxLayout()
        vb.addWidget(self.combo1)
        vb.addWidget(self.btn)
        vb.addWidget(self.btn2)
        # vb.addWidget(self.lcd)
        # vb.addWidget(self.sld)
        vb.addWidget(self.lbl)
        vb.addLayout(hb)
        self.setLayout(vb)