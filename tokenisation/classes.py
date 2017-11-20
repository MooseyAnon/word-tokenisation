from tokenisation import *


"""This is all the Filefunction in this foler organised into classes for oop usage"""

class OpenInput:
	def __init__(self):
		self.output = None

	def _open_standard(self, someinput):
		try:
			with open(someinput, 'r') as af:
				self.output = af.read() 
				return self.output
		except IOError:
			logger.debug('open_standard could not open this {0}'.format(someinput))


	def _open_csv(self, someinput):
		try:
			with open(someinput, 'rb') as af:
				self.output = list(af)
				return self.output
		except IOError:
			logger.debug('open_csv could not open this {0}'.format(someinput))

	def _check_file_type(self, someinput):
		"""check file type (using the file format) and open using right function"""

		pdf = re.compile('[A-Za-z0-9]+\.pdf$')
		csv = re.compile('[A-Za-z0-9]+\.csv$')
		txt = re.compile('[A-Za-z0-9]+\.txt$')

		if bool(pdf.search(someinput)) == True:
			# opened_pdf=open_pdf(afile) # needs to be done after finding the right 3rd party libraries
			pass
			# opened_pdf

		elif bool(csv.search(someinput)) == True:
			opened_csv = self._open_csv(someinput) 
			logger.debug('check_file_type opened a csv file named {0}'.format(someinput))
			return opened_csv
		
		elif bool(txt.search(someinput)) == True:
			opened_reg_file = self._open_standard(someinput)
			logger.debug('check_file_type opened a txt file named {0}'.format(someinput))
			return opened_reg_file  

		else:
			logger.debug('check_file_type cannot open this file format. File name: {0}'.format(someinput))


	def open_file(self, someinput):
		"""simple open file function to act as interface to more thorough file checking functions.
			Returns a checked and read file"""

		f = self._check_file_type(someinput)
		logger.debug('open_file successfully opened {0}'.format(someinput))
		return f




class TextTokeniser(OpenInput):
	def __init__(self):
		OpenInput.__init__(self)
		self.output = []
		self.stopwords = []

	def  default_tokens(self, someinput):
		f = self.open_file(someinput)
		logger.debug('default_tokens successfully opned and read {0}'.format(someinput))
		self.output=[word for word in re.split('\s+', f)]
		return self.output

	def punct_free_tokens(self, someinput):
		f = self.open_file(someinput)
		logger.debug('punct_free_tokens successfully opned and read {0}. Attempting to remove punctuation'.format(someinput))
		self.output = [word for word in re.split('\s+', f.translate(None, '_+-.,!@#$%^&*();\/|<>"'))] # replaces given input them with "" wherever found in doc 
		return self.output

	def document_vocab(self, someinput):
		self.output = set(self.punct_free_tokens(someinput))
		logger.debug('unique_tokens successfully opned and read {0}'.format(someinput))
		return self.output

	def capital_tokens(self, someinput):
		f= self.open_file(someinput)
		self.output = [word for word in re.findall('[A-Z]\w+', f)]
		return self.output

	def split_newline_chars(someinput):

		f = self.open_file(someinput)
		self.output = [line for line in re.split('\n+', f)]
		return self.output


	def remove_stop_words(self, readfile, swf=None):

		if swf:
			try:
				self.stopwords = default_tokens(swf)
			except:
				logger.debug('remove_stop_words could not open your stopword file reverting to default')
		else:
			self.stopwords = default_tokens('test_stop_words.txt') # come from list of most common english words

		rf = default_tokens(readfile)

		self.output = [word for word in rf if word not in self.stopwords]
		return  self.output




	
class CSVTokeniser(OpenInput):
	def __init__(self):
		OpenInput.__init__(self)
		self.output= []

	def csv_lines(self, someinput):

		f = self.open_file(someinput)
		reader = csv.reader(f)
		logger.debug('csv_lines successfully opned and read {0}'.format(someinput))
		self.output = [row for row in reader]
		return self.output 

	def csv_tokens(self, someinput):

		f = self.open_file(someinput)
		reader = csv.reader(f, delimiter=' ')
		logger.debug('csv_tokens successfully opned and read {0}'.format(someinput)) 
		self.output = [word for row in reader for word in row] 
		return self.output


	def punct_free_lines(self, someinput):
		f = self.open_file(someinput)
		self.output = []
		for line in f:
			data = line.translate(None, '_+-.,!@#$%^&*();\/|<>"')
			self.output.append([data])
		return self.output

	def csv_vocab(self, someinput):
		self.output = set(self.csv_tokens(someinput))
		return self.output

	def csv_capitals(self, someinput):
		"""returns capital letter words in each line of file"""
		f = self.open_file(someinput)
		self.output = []
		for line in f:
			data= re.findall('[A-Z]\w+', line)
			self.output.append(data)
		return self.output









