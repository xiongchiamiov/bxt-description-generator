# -*- coding: utf-8 -*-

from glob import glob
import json
import os
import sys
from models import Folder
from PyQt4.QtCore import QUrl, Qt, SIGNAL, SLOT, pyqtSignal, pyqtSlot, QString
from PyQt4.QtGui import *
from PyQt4.QtWebKit import QWebView

class QFileChooser(QWidget):
	directoryChanged = pyqtSignal(QString)
	
	def __init__(self, parent=None, directory=''):
		QWidget.__init__(self, parent)
		
		wrapper = QHBoxLayout(parent)
		self.lineEdit = QLineEdit(directory)
		pushButton = QPushButton('Browse')
		wrapper.addWidget(self.lineEdit)
		wrapper.addWidget(pushButton)
		
		self.directoryChanged.connect(self.change_directory)
		self.connect(pushButton, SIGNAL('clicked()'),
		             self, SLOT('choose_file()'))
		
		self.setLayout(wrapper)
	
	@pyqtSlot()
	def choose_file(self):
		directory = QFileDialog.getExistingDirectory(parent=self, directory=self.lineEdit.displayText())
		self.directoryChanged.emit(directory)
	
	def change_directory(self, directory):
		self.lineEdit.setText(directory)

class QTemplatePreview(QWidget):
	templateChanged = pyqtSignal(QString, dict)
	sourceGenerated = pyqtSignal(QString)
	
	def __init__(self, name, parent=None):
		QWidget.__init__(self, parent)
		self.name = name
		self.data = json.load(open('templates/%s.json' % name))
		
		wrapper = QHBoxLayout(parent)
		
		image = QPixmap("templates/%s.jpg" % name)
		imageWrapper = QLabel()
		imageWrapper.setPixmap(image)
		wrapper.addWidget(imageWrapper)
		
		label = QLabel()
		label.setText(self.data['description'])
		label.setWordWrap(True)
		label.setAlignment(Qt.AlignTop)
		wrapper.addWidget(label)
		
		self.setLayout(wrapper)
	
	@pyqtSlot()
	def mousePressEvent(self, event):
		self.templateChanged.emit(self.name, self.data['customizations'])
		
		source = '''\
<html>
<head></head>
<body>
Hello.
</body>
</html>
'''
		self.sourceGenerated.emit(source)

class QCustomizationBox(QWidget):
	def __init__(self, parent=None, name='', value=''):
		QWidget.__init__(self, parent)
		
		wrapper = QHBoxLayout(parent)
		wrapper.addWidget(QLineEdit(value))
		wrapper.addWidget(QLabel(name))
		
		self.setLayout(wrapper)

class QFileTreeSelector(QTreeWidget):
	def change_directory(self, directory):
		self.clear()
		# we need to convert from a QString to a normal Python string
		root = Folder(str(directory))
		# fill out our Folder/File tree
		root.scan()
		# and then turn it into something we can display
		self.addTopLevelItems(self.create_tree(root).takeChildren())
	
	# this should take in a Folder
	@staticmethod
	def create_tree(folder):
		root = QTreeWidgetItem([folder.name])
		
		for childFolder in folder.folders:
			child = QFileTreeSelector.create_tree(childFolder)
			# is it a directory empty of files we want (eg 'Scans' folder)?
			if child.childCount():
				root.addChild(child)
		for musicFile in folder.files['music']:
			root.addChild(QTreeWidgetItem([musicFile.name]))
		
		return root

class Ui_MainWindow(QWidget):
	def __init__(self, parent=None):
		QWidget.__init__(self, parent)
		
		self.setWindowTitle("bxt-description-generator")
		
		# give us an overall layout to put things in
		wrapper = QHBoxLayout()
		
		## Left Tabs
		tabWidget = QTabWidget()
		
		### File Tab
		fileTab = QWidget()
		fileTabWrapper = QVBoxLayout(fileTab)
		
		directory = os.getenv('HOME') if os.getenv('HOME') else os.getenv('HOMEPATH')
		fileChooser = QFileChooser(directory=directory)
		fileTabWrapper.addWidget(fileChooser)
		
		fileTreeSelector = QFileTreeSelector()
		fileChooser.directoryChanged.connect(fileTreeSelector.change_directory)
		
		fileTabWrapper.addWidget(fileTreeSelector)
		
		tabWidget.addTab(fileTab, 'Files')
		
		### Template Tab
		templateTab = QWidget()
		templateTabWrapper = QVBoxLayout(templateTab)
		
		templateGroup = QGroupBox('Templates')
		templateGroupWrapper = QVBoxLayout(templateGroup)
		templatePreviews = []
		for filename in glob('templates/*.json'):
			# create preview, but get just the template name from the filename
			templatePreviews.append(QTemplatePreview(filename.replace('templates/', '').replace('.json', '')))
		for templatePreview in templatePreviews:
			templateGroupWrapper.addWidget(templatePreview)
			templatePreview.templateChanged.connect(self.set_previews)
		templateTabWrapper.addWidget(templateGroup)
		
		customizationsGroup = QGroupBox('Customizations')
		self.customizationsGroupWrapper = QVBoxLayout(customizationsGroup)
		templateTabWrapper.addWidget(customizationsGroup)
		
		saveWidget = QHBoxLayout()
		saveWidget.addWidget(QLabel('Save new template as: '))
		saveWidget.addWidget(QLineEdit())
		saveWidget.addWidget(QPushButton('Save'))
		templateTabWrapper.addLayout(saveWidget)
		
		tabWidget.addTab(templateTab, 'Template')
		
		wrapper.addWidget(tabWidget)
		
		## Right Tabs
		rightTabWidget = QTabWidget()
		
		### Preview
		previewTab = QWidget()
		preview = QWebView(previewTab)
		for templatePreview in templatePreviews:
			templatePreview.sourceGenerated.connect(lambda source: preview.setHtml(source))
		rightTabWidget.addTab(preview, 'Preview')
		
		### Source
		sourceTab = QWidget()
		sourceDisplay = QPlainTextEdit(sourceTab)
		sourceDisplay.setReadOnly(True)
		for templatePreview in templatePreviews:
			templatePreview.sourceGenerated.connect(sourceDisplay.setPlainText)
		rightTabWidget.addTab(sourceTab, 'Source')
		
		wrapper.addWidget(rightTabWidget)
		
		self.setLayout(wrapper)
		self.resize(800, 600)
	
	def set_previews(self, name, customizations):
		# get rid of all the customizations we've got currently
		while self.customizationsGroupWrapper.count():
			# we get back a QWidgetItem, so we need to pull the actual QWidget out
			widget = self.customizationsGroupWrapper.itemAt(0).widget()
			self.customizationsGroupWrapper.removeWidget(widget)
			# for whatever reason, just removing it and/or destroying it
			# doesn't do what we want...
			widget.setParent(None)
		
		# and add in our new ones
		for key, value in customizations.items():
			self.customizationsGroupWrapper.addWidget(QCustomizationBox(name=key, value=value))


if __name__ == "__main__":
	app = QApplication(sys.argv)
	myapp = Ui_MainWindow()
	myapp.show()
	sys.exit(app.exec_())

#from PyQt4 import QtCore; QtCore.pyqtRemoveInputHook();	import pudb; pudb.set_trace()
