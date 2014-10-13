#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os

import smallsmilhandler

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

import sys

<<<<<<< HEAD

class KaraokeLocal(smallsmilhandler.SmallSMILHandler):

    def __init__(self, fichero):
        parser = make_parser()
        sHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open(fichero))
        self.lista = sHandler.get_tags()

    def __str__(self):
        exit = ""
        for elemento in self.lista:
            tag = elemento[0]
            atribute = elemento[1]
            exit += '\n' + tag + '\t'
            for value in atribute:
                if atribute[value] != '':
                    exit += value + '=' + "'" + atribute[value] + "'" + '\t'
        return exit

    def do_local(self):
        for elemento in self.lista:
            tag = elemento[0]
            atribute = elemento[1]
            for value in atribute:
                if atribute[value] != '':
                    if value == 'src':
                        recurso = atribute[value]
                        os.system("wget -q " + recurso)
                        lista = recurso.split('/')
                        lista = lista[-1]
                        atribute[value] = lista

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print "Usage: python karaoke.py file.smil"
    else:
        karaoke = KaraokeLocal(sys.argv[1])
        print karaoke.__str__()
        karaoke.do_local()
        print karaoke.__str__()
=======
if __name__ == "__main__":

	parser = make_parser()
	sHandler = smallsmilhandler.SmallSMILHandler()
	parser.setContentHandler(sHandler)
	parser.parse(open(sys.argv[1]))
	lista = sHandler.get_tags()

	for elemento in lista:
		tag = elemento[0]
		atribute = elemento[1]

		for value in atribute:
			if atribute[value] != '':
				if value == 'src':
					recurso = atribute[value]
					os.system("wget -q " + recurso)
					lista = recurso.split('/')
					lista = lista[-1]
					atribute[value] = lista
					print atribute[value]	 

>>>>>>> 42a1da9e7b78adff42274e8929fc5cdcb8e78551
