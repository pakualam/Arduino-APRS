#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Aprs Decode Test
# Generated: Wed Dec  5 09:01:43 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import audio
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import afsk
import display
import sip
import sys


class aprs_decode_test(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Aprs Decode Test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Aprs Decode Test")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "aprs_decode_test")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 48000

        ##################################################
        # Blocks
        ##################################################
        self.show_text_0 = display.show_text()
        self._show_text_0_win = sip.wrapinstance(self.show_text_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._show_text_0_win)
        self.fft_filter_xxx_0 = filter.fft_filter_fff(1, (firdes.band_pass(1,samp_rate,1e3,2.5e3,250,firdes.WIN_BLACKMAN)), 1)
        self.fft_filter_xxx_0.declare_sample_delay(0)
        self.audio_source_0 = audio.source(samp_rate, '', True)
        self.afsk_afsk1200_0 = afsk.afsk1200(samp_rate,4)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.afsk_afsk1200_0, 0), (self.show_text_0, 0))    
        self.connect((self.audio_source_0, 0), (self.fft_filter_xxx_0, 0))    
        self.connect((self.fft_filter_xxx_0, 0), (self.afsk_afsk1200_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "aprs_decode_test")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.fft_filter_xxx_0.set_taps((firdes.band_pass(1,self.samp_rate,1e3,2.5e3,250,firdes.WIN_BLACKMAN)))


def main(top_block_cls=aprs_decode_test, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()