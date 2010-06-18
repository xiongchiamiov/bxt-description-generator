# -*- coding: utf-8 -*-

import sys
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
	sourceGenerated = pyqtSignal(QString)
	
	def __init__(self, parent=None, description='', thumb=''):
		QWidget.__init__(self, parent)
		
		wrapper = QHBoxLayout(parent)
		
		image = QPixmap(thumb)
		imageWrapper = QLabel()
		imageWrapper.setPixmap(image)
		wrapper.addWidget(imageWrapper)
		
		label = QLabel()
		label.setText(description)
		label.setWordWrap(True)
		label.setAlignment(Qt.AlignTop)
		wrapper.addWidget(label)
		
		self.setLayout(wrapper)
	
	@pyqtSlot()
	def mousePressEvent(self, event):
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

class QFileTreeSelector(QTreeView):
	def __init__(self, parent=None, directory=''):
		QTreeView.__init__(self, parent)
		
		self.filesystem = QFileSystemModel()
		self.setModel(self.filesystem)
		self.setRootIndex(self.filesystem.setRootPath(directory))
	
	def change_directory(self, directory):
		self.setRootIndex(self.filesystem.setRootPath(directory))

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
		
		directory = '/home/pearson/Documents'
		fileChooser = QFileChooser(directory=directory)
		fileTabWrapper.addWidget(fileChooser)
		
		fileTreeSelector = QFileTreeSelector(directory=directory)
		fileChooser.directoryChanged.connect(fileTreeSelector.change_directory)
		
		fileTabWrapper.addWidget(fileTreeSelector)
		
		tabWidget.addTab(fileTab, 'Files')
		
		### Template Tab
		templateTab = QWidget()
		templateTabWrapper = QVBoxLayout(templateTab)
		
		templateGroup = QGroupBox('Templates')
		templateGroupWrapper = QVBoxLayout(templateGroup)
		templatePreviews = []
		for i in range(3):
			templatePreviews.append(QTemplatePreview(thumb='thumbs/rorando.jpg', description='Nullam non sem et mi porta aliquet eget non odio. Proin vehicula dapibus tortor, a venenatis tortor venenatis in. Pellentesque ultricies diam vitae mauris iaculis tristique. Praesent metus tortor, dictum nec consequat id, aliquet ut dui. Curabitur vestibulum condimentum fermentum. Phasellus quam tellus, scelerisque et pretium a, suscipit eget risus. Duis pharetra bibendum dolor, a porta metus consequat a.'))
		for templatePreview in templatePreviews:
			templateGroupWrapper.addWidget(templatePreview)
		templateTabWrapper.addWidget(templateGroup)
		
		customizationsGroup = QGroupBox('Customizations')
		customizationsGroupWrapper = QVBoxLayout(customizationsGroup)
		customizationsGroupWrapper.addWidget(QCustomizationBox(name='Outline', value='#FFF'))
		customizationsGroupWrapper.addWidget(QCustomizationBox(name='Text', value='#000'))
		customizationsGroupWrapper.addWidget(QCustomizationBox(name='Font-size', value='12pt'))
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


if __name__ == "__main__":
	app = QApplication(sys.argv)
	myapp = Ui_MainWindow()
	myapp.show()
	sys.exit(app.exec_())
