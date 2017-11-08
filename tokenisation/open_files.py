import re, logging, sys 




"""These functions show how opening files can be conditionally seperated."""

# conifgure logging, because we love logs! 

# LOG_FORM output example = INFO 2017-10-26 21:58:20,336 - test message!
LOG_FORM = '%(levelname)s %(asctime)s - %(message)s'

logging.basicConfig(filename = 'openfiles.txt', 
					level = logging.DEBUG, 
					format = LOG_FORM,
					filemode='w') # get rid of this line to persist logs

logger = logging.getLogger()

# uncomment and run to test logger set up
# logger.info('test message!')


def open_csv(afile):
	"""open and read csv file"""

	try:
		f = open(afile, 'r')
		f1 = f.read() # took an extra step to enable house keeping
		logger.debug("open_csv successfully opened{0}".format(afile))
		f.close() # house keeping
		logger.debug("open_csv successfully closed {0}".format(afile))
		return f1
	except IOError as err:
		logger.debug("something went wrong trying to open {0}. Error: {1}".format(afile, err))
		return err


def open_txt(afile):
	"""open and read a txt file"""

	try:
		f = open(afile, 'r')
		f1 = f.read() # took an extra step to enable house keeping
		logger.debug("open_txt successfully opened{0}".format(afile))
		f.close() # house keeping
		logger.debug("open_txt successfully closed {0}".format(afile))
		return f1
	except IOError as err:
		logger.debug("something went wrong trying to open {0}. Error: {1}".format(afile, err))
		return err


def check_file_type(afile):
	"""check file type (using the file format) and open using right function"""

	pdf = re.compile('[A-Za-z0-9]+\.pdf$')
	csv = re.compile('[A-Za-z0-9]+\.csv$')
	txt = re.compile('[A-Za-z0-9]+\.txt$')

	if bool(pdf.search(afile)) == True:
		# opened_pdf=open_pdf(afile) # needs to be done after finding the right 3rd party libraries
		pass
		# opened_pdf

	elif bool(csv.search(afile)) == True:
		opened_csv = open_csv(afile) 
		logger.debug('check_file_type opened a csv file named {0}'.format(afile))
		return opened_csv
	
	elif bool(txt.search(afile)) == True:
		opened_reg_file = open_txt(afile)
		logger.debug('check_file_type opened a txt file named {0}'.format(afile))
		return opened_reg_file  

	else:
		logger.debug('check_file_type cannot open this file format. File name: {0}'.format(afile))



def open_file(afile):
	"""simple open file function to act as interface to more thorough file checking functions.
		Returns a checked and read file"""

	f = check_file_type(afile)
	logger.debug('open_file successfully opened {0}'.format(afile))
	return f



















