#########################################################
# PDF Password cracker
#
# Trys all the passwords in a wordlist against the PDF File
# Its not threaded so is quite slow but can be handy in some situations
#
#
#       REQUIRES PDFMINER FROM http://www.unixuser.org/~euske/python/pdfminer/
#
#       Usage:
#       python PDFCrack.py -p [wordlist] -f [pdf file]
#
#
# Kurtis Brown
# http://www.kurtisebear.com
# @kurtisebearuk
#
#########################################################


from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
import sys
import optparse
import string




# Parse Options
author = "Kurtis Brown"
Contact = "Kurtis@kurtisebear.com, @kurtisbearuk"

desc = "I made %prog for a specific task where I had a wordlist I knew the pdf password was in, I hope other people can find some use in it"

parser = optparse.OptionParser(description=desc)
parser.add_option('-p', '--password', help='Password List File', dest='passwordFile', action='store', type='string')
parser.add_option('-f', '--pdf', help='PDF File', dest='PDFFile', action='store', type='string')

(opts, args) = parser.parse_args()



if opts.passwordFile is None:
        parser.print_help()
        exit(-1)
if opts.PDFFile is None:
        parser.print_help()
        exit(-1)


## test password on pdf
def check_pdf_password(pdf, password):
        fp = open(pdf, 'rb')
        parser = PDFParser(fp)
        doc = PDFDocument()
        parser.set_document(doc)
        doc.set_parser(parser)
        doc.initialize(password)
	try:
                if doc.is_extractable:
                        return "The PDF Password Is: " + password
                else:
                        print "."
        except Exceptions:
                        return "."


## Open the wordlist and select the pdf
wordlist = open(opts.passwordFile, 'r')
pdf = opts.PDFFile

## Go through each password
for password in wordlist:
        password = password.rstrip('\n')
        check_pdf_password(pdf,password)
        print ".."




