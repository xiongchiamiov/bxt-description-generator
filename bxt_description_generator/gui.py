# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import QUrl, Qt
from PyQt4.QtGui import *
from PyQt4.QtWebKit import QWebView

class QFileChooser(QWidget):
	def __init__(self, parent=None, directory=''):
		QWidget.__init__(self, parent)
		
		wrapper = QHBoxLayout(parent)
		wrapper.addWidget(QLineEdit(directory))
		wrapper.addWidget(QPushButton('Browse'))
		
		self.setLayout(wrapper)

class QTemplatePreview(QWidget):
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

class QCustomizationBox(QWidget):
	def __init__(self, parent=None, name='', value=''):
		QWidget.__init__(self, parent)
		
		wrapper = QHBoxLayout(parent)
		wrapper.addWidget(QLineEdit(value))
		wrapper.addWidget(QLabel(name))
		
		self.setLayout(wrapper)

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
		
		#fileTabWrapper.addWidget(QFileDialog())
		fileTabWrapper.addWidget(QFileChooser(directory='/home/pearson/Documents'))
		
		fileTree = QTreeWidget()
		fileList = [QTreeWidgetItem(['foo']), QTreeWidgetItem(['bar']), QTreeWidgetItem(['baz'])]
		fileList[0].addChildren([QTreeWidgetItem(['foo1']), QTreeWidgetItem(['foo2'])])
		fileList[0].child(0).addChild(QTreeWidgetItem(['foo1a']))
		fileTree.addTopLevelItems(fileList)
		fileTabWrapper.addWidget(fileTree)
		
		tabWidget.addTab(fileTab, 'Files')
		
		### Template Tab
		templateTab = QWidget()
		templateTabWrapper = QVBoxLayout(templateTab)
		
		templateGroup = QGroupBox('Templates')
		templateGroupWrapper = QVBoxLayout(templateGroup)
		templateGroupWrapper.addWidget(QTemplatePreview(thumb='thumbs/rorando.jpg', description='Nullam non sem et mi porta aliquet eget non odio. Proin vehicula dapibus tortor, a venenatis tortor venenatis in. Pellentesque ultricies diam vitae mauris iaculis tristique. Praesent metus tortor, dictum nec consequat id, aliquet ut dui. Curabitur vestibulum condimentum fermentum. Phasellus quam tellus, scelerisque et pretium a, suscipit eget risus. Duis pharetra bibendum dolor, a porta metus consequat a.'))
		templateGroupWrapper.addWidget(QTemplatePreview(thumb='thumbs/rorando.jpg', description='Nullam non sem et mi porta aliquet eget non odio. Proin vehicula dapibus tortor, a venenatis tortor venenatis in. Pellentesque ultricies diam vitae mauris iaculis tristique. Praesent metus tortor, dictum nec consequat id, aliquet ut dui. Curabitur vestibulum condimentum fermentum. Phasellus quam tellus, scelerisque et pretium a, suscipit eget risus. Duis pharetra bibendum dolor, a porta metus consequat a.'))
		templateGroupWrapper.addWidget(QTemplatePreview(thumb='thumbs/rorando.jpg', description='Nullam non sem et mi porta aliquet eget non odio. Proin vehicula dapibus tortor, a venenatis tortor venenatis in. Pellentesque ultricies diam vitae mauris iaculis tristique. Praesent metus tortor, dictum nec consequat id, aliquet ut dui. Curabitur vestibulum condimentum fermentum. Phasellus quam tellus, scelerisque et pretium a, suscipit eget risus. Duis pharetra bibendum dolor, a porta metus consequat a.'))
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
		#preview.setHtml(source)
		preview.setUrl(QUrl('http://google.com'))
		rightTabWidget.addTab(preview, 'Preview')
		
		### Source
		sourceTab = QWidget()
		sourceDisplay = QPlainTextEdit(sourceTab)
		sourceDisplay.setReadOnly(True)
		rightTabWidget.addTab(sourceTab, 'Source')
		
		wrapper.addWidget(rightTabWidget)
		
		self.setLayout(wrapper)
		self.resize(800, 600)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	myapp = Ui_MainWindow()
	myapp.show()
	sys.exit(app.exec_())
