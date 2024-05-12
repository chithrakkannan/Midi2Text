import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt6.uic import loadUi
from mido import MidiFile

class MainWindow(QDialog):

    def __init__(self):
        super().__init__()
        loadUi("gui.ui", self)
        self.btn_midi_browse.clicked.connect(self.midi_browse)
        self.btn_txt_browse.clicked.connect(self.txt_browse)
        self.btn_start.clicked.connect(self.start_convert)
        

    def midi_browse(self):
        print("Browse (MIDI) Clicked")
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        file_dialog.setNameFilter("MIDI files (*.midi *.mid)")
        if file_dialog.exec():
            file_names = file_dialog.selectedFiles()
            if file_names:
                self.l_midi.setText(file_names[0])
                print("MIDI File Location:", file_names[0])

                try:
                    mid = MidiFile(file_names[0], clip=True)
                    print("MiDi Status : Success")

                except:
                    print("An exception occurred. Retry or Try Different MIDI File")


    def txt_browse(self):
        print("Browse (TXT) Clicked")
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        file_dialog.setNameFilter("Text files (*.txt)")
        if file_dialog.exec():
            file_names = file_dialog.selectedFiles()
            self.l_txt.setText(file_names[0])
            print("Text File Location:", file_names)

    def start_convert(self):
        print("Start (Convert) Clicked")
        if self.l_midi.text() == "" or self.l_midi.text() == "Midi File":
            print("MiDi Not Selected")
            return
        else:
            if self.l_txt.text() == "" or self.l_txt.text() == "Text Destination":
                print("Txt Not Selected, Continues Anyway ")
            print("Converting...")
            try:
                mid = MidiFile(self.l_midi.text(), clip=True)
                print("Conversion Status : Success")

            except:
                print("An exception occurred. Retry or Try Different MIDI File")
        
        
app = QApplication(sys.argv)
mainwindow = MainWindow()
mainwindow.setFixedSize(400, 300)
mainwindow.show()
sys.exit(app.exec())

"""

In the following code, When start_convert is triggerd, It should check the line edit "l_midi" and "l_txt". if either of those are empty, return select Dir; if l_midi is "Midi File" return MiDi is not selected
def midi_browse(self):
        print("Browse (MIDI) Clicked")
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        file_dialog.setNameFilter("MIDI files (*.midi *.mid)")
        if file_dialog.exec():
            file_names = file_dialog.selectedFiles()
            if file_names:
                self.l_midi.setText(file_names[0])
                print("MIDI File Location:", file_names[0])

                try:
                    mid = MidiFile(file_names[0], clip=True)
                    print("MiDi Status : Success")

                except:
                    print("An exception occurred")


    def txt_browse(self):
        print("Browse (TXT) Clicked")
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        file_dialog.setNameFilter("Text files (*.txt)")
        if file_dialog.exec():
            file_names = file_dialog.selectedFiles()
            self.l_txt.setText(file_names[0])
            print("Text File Location:", file_names)

    def start_convert(self):
        print("Start (Convert) Clicked")
        #print("Converting...")
"""
