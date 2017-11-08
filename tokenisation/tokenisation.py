import re, logging, csv 

from nltk.corpus import stopwords
from open_files import *


"""
This is a series of simple tokenisation functions. Most of these can be done using NLTK (recommended), 

however, these are my own implementations to illustrate how these functions could be doing their magic 

under the hood.

Furthermore, oftentimes personal tokenisation is required on any given corpus in order to get as accurate results 

as possible. These functions offer some easy to edit, starting strategies to go some wat to achieving those results.
"""



def split_csv_lines(afile):
	"""split csv document into a list of lists. Each sublist corresponds with a line in the doc"""
	f = open_file(afile)
	reader = csv.reader(f)
	logger.debug('split_csv_lines successfully opned and read {0}'.format(afile))
	return [row for row in reader]
 

def split_csv_terms(afile):
	"""split csv document into a list of lists. Each sublist is a list of seperated terms from the line"""

	f = open_file(afile)
	reader = csv.reader(f, delimiter=' ')
	logger.debug('split_csv_terms successfully opned and read {0}'.format(afile)) 
	return [word for row in reader for word in row] 


def unique_csv_terms(afile):
	"""returns a set of unique terms in a csv document"""

	f = open_file(afile)
	reader = csv.reader(f, delimiter=' ')
	logger.debug('unique_csv_terms successfully opned and read {0}'.format(afile))
	uniq_word_set = set(word for row in reader for word in row) # set doesn't allow duplicates
	return uniq_word_set



def remove_punct(afile):
	"""removes punctuation and symbols from a file. I left this as optional because 
	sometimes it's useful to have punct/symbols for analysis. """ 

	f = open_file(afile)
	logger.debug('remove_punct successfully opned and read {0}. Attempting to remove punctuation'.format(afile))
	return f.translate(None, '_+-.,!@#$%^&*();\/|<>"') # replaces given input them with "" wherever found in doc 



# regular file with no explicit lines
def split_file_terms(afile):
	"""split document at space between each work and create a word list"""

	f = remove_punct(afile) # change this to open_file to keep punctuation
	logger.debug('split_file_terms successfully opned and read {0}'.format(afile))
	return [word for word in re.split('\s+', f)]



# regular file with no explicit lines unique word list
def unique_file_terms(afile):
	"""split document at space between each work and create a set of documents unique words"""

	# this goes over every word and ommittes if word is in set already. 
	f = open_file(afile)
	logger.debug('unique_file_terms successfully opned and read {0}'.format(afile))
	unique_words= set(word for word in re.split('\s+', f)) 
	return unique_words



def find_capitals(afile):
	"""In a given document returns all words that start with a capital letter. 
	When use along with remove_stop_words its an easy way to find documents Nouns.""" 

	f = open_file(afile)
	logger.debug('find_capitals successfully opned and read {0}'.format(afile))
	return re.findall('[A-Z]\w+', f) 
	


def remove_stop_words(afile):
	"""returns a stopword free list"""

	f= file_to_term_split(afile)
	logger.debug('remove_stop_words successfully opned, read and split {0}'.format(afile))
	stop_words = stopwords.words('english') # this is from the NLTk library (most common English words) but can easily be replaced with one's own list of stopwords
	return [word for word in f if word not in stop_words] 







