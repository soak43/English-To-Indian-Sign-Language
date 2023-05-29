# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 12:15:51 2022

@author: Sayali
"""



import os
from nltk.parse.corenlp import CoreNLPParser
from nltk.tree import Tree, ParentedTree
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from time import sleep
from sigmlNumericData import create_sigml
import time


#----------------------------#
def convert_sentence(input_string):
    
    start = time.time()
    java_path = "C:\Program Files\Java\jdk-16.0.2\bin\java.exe"
    os.environ['CLASSPATH'] = java_path

    #tokenize
    input_string = input_string.lower()
    if len(input_string.split()) == 1:
        #return None
        create_sigml(input_string)
    else:
    
        #print("Tokenize done")
        
        sleep(6)
        parser = CoreNLPParser(url='http://localhost:9000')
        #print("Parser set")
    
        englishtree = [tree for tree in parser.parse(input_string.split())]
        #print("Eng tree set")
        parsetree = englishtree[0]
        #print("Parse tree set")
    
        dict = {}
        #print("Dict set")
    
        # parenttree = ParentedTree(node=parsetree, children=[])
        #print("parent tree set")
        parenttree = ParentedTree.fromstring(str(parsetree))
    
        # print("Input Sentence: ", input_string)
        # print("Input Sentence Tree\n")
        # print(parenttree)
        print("\n\n")
    
        for sub in parenttree.subtrees():
            dict[sub.treeposition()] = 0
    
        #----------------------------#
    
        islTree = Tree('ROOT', [])
        i = 0
    
        for sub in parenttree.subtrees():
            if (sub.label() =="NP" and dict[sub.treeposition()] == 0 and dict[sub.parent().treeposition()] == 0):
                dict[sub.treeposition()] = 1
                islTree.insert(i, sub)
                i = i + 1
    
            if(sub.label()=="VP" or sub.label()=="PRP"):
                for sub2 in sub.subtrees():
                    if((sub2.label()=="NP" or sub2.label()=='PRP') and dict[sub2.treeposition()]==0 and dict[sub2.parent().treeposition()]==0):
                        dict[sub2.treeposition()] = 1
                        islTree.insert(i,sub2)
                        i=i+1
    
    
        for sub in parenttree.subtrees():
            for sub2 in sub.subtrees():
                if(len(sub2.leaves())==1 and dict[sub2.treeposition()]==0 and dict[sub2.parent().treeposition()]==0):
                    dict[sub2.treeposition()]=1
                    islTree.insert(i,sub2)
                    i=i+1
    
        parsed_sent = islTree.leaves()
    
        # words = parsed_sent
    
        # print("ISL Tree\n")
        # print(islTree)
        # print("\n\n")
    
        # nltk.download('stopwords')
        # nltk.download('wordnet')
        # print()
    
        stop_words = set(stopwords.words("english"))
    
        lemmantizer = WordNetLemmatizer()
        lemmantized_words = []
    
    
        for w in parsed_sent:
            lemmantized_words.append(lemmantizer.lemmatize(w))
    
        islSentence = ""
    
        for w in lemmantized_words:
            if w not in stop_words:
                islSentence += w
                islSentence += " "
    
    
        print("ISL Sentence\n")
        print(islSentence)
        
        end = time.time()
        print("Time required to parse = ", end-start)
        
        create_sigml(islSentence)
    
'''   
def main():
    sent = input("Enter a sentence = ").lower()
    convert_sentence(sent)

if __name__ == "__main__":
    main()
'''