# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 20:02:31 2022

@author: Sayali
"""

from nltk.parse.corenlp import CoreNLPServer
import nltk
import os
# The server needs to know the location of the following files:
#   - stanford-corenlp-X.X.X.jar
#   - stanford-corenlp-X.X.X-models.jar
STANFORD = os.path.join("models", "stanford-corenlp-full-2018-02-27")

# Create the server
server = CoreNLPServer(
   os.path.join(STANFORD, "C:\Stanford CoreNLPParser\stanford-corenlp-4.4.0\stanford-corenlp-4.4.0.jar"),
   os.path.join(STANFORD, "C:\Stanford CoreNLPParser\stanford-corenlp-4.4.0\stanford-corenlp-4.4.0-models.jar"),    
)

# Start the server in the background
server.start()

from  nltk.parse.corenlpnltk.pa  import CoreNLPParser

parser = CoreNLPParser()
parse = next(parser.raw_parse("I put the book in the box on the table."))