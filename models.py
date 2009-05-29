import os

def deduce_name(path):
	'''
	Deduce a file/directory name from a path
	'''
	head, tail = os.path.split(path)
	return tail if tail else head

class Folder:
	'''
	Representation of a folder

	name: folder name
	path: full path (absolute or relative) to the file from current directory
	folders: a list of Folders directly under this one
	files: a list of Files directly under this one
	numScans: number of files in this folder that are scans
	'''
	def __init__(self, path, name=None):
		self.name = name if name else deduce_name(path)

		self.path = path
		self.folders = []
		self.files = []
		self.numScans = 0
	
	def __str__(self):
		return self.name

	def scan(self):
		for name in os.listdir(self.path):
			# Do we have a directory?
			if os.path.isdir(os.path.join(self.path, name)):
				self.folders.append(Folder(os.path.join(self.path, name)))
			# Or do we have a file?
			elif os.path.isfile(os.path.join(self.path, name)):
				self.files.append(File(os.path.join(self.path, name)))
		for folder in self.folders:
			folder.scan()

class File:
	'''
	Representation of a file

	name: filename
	path: full path (absolute or relative) to the file from current directory
	extension: file extension
	'''
	def __init__(self, path, name=None):
		self.name = name if name else deduce_name(path)

		self.path = path
		try:
			self.extension = os.path.splitext(self.name)[1]
		except IndexError:
			self.extension = None
	
	def __str__(self):
		return self.name
