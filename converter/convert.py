#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, getopt
import codecs
import json

def load_data(filename):
    """Load Atom Snippets data from json
    :filename: Atom Snippets json file
    :returns: json atom data
    """
    snippets_file = open(filename)
    # data = snippets_file.read().decode('utf-8')
    atom_snippets_fixture = json.load(snippets_file)
    return atom_snippets_fixture

def convert(atom_snippet):
    """Convert Atom snippet to UltiSnippet
    :data: Atom snippet
    :returns: UtilSnippet
    """
    snippet = ('snippet %(trigger)s "%(description)s"\n' 
            % {
                'trigger': (atom_snippet['displayText']).replace(" ", ""),
                'description': (atom_snippet['description']).replace("\"", "\'")
                } +
            '%s\n' % atom_snippet['snippet'] +
            'endsnippet')
    return snippet

def convert_snippets(atom_snippets_file, new_filename):
    """Convert atom snippets 
    from file to UltiSnippets

    :atom_snippets_file: a file path of atom snippets
    :new_filename: new UltiSnippets file
    """
    atom_snippets = load_data(atom_snippets_file)
    result_snippets = ''
    for snippet in atom_snippets:
        result_snippets += convert(snippet) + '\n\n'

    result_file = codecs.open(new_filename, "w", encoding='utf8')
    result_file.write(result_snippets)
    result_file.close()

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   convert_snippets(inputfile, outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])
