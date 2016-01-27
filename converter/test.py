import json
from pprint import pprint
from convert import convert

def load_fixture():
    snippets_file = open('./fixture.json')
    atom_snippets_fixture = json.load(snippets_file)
    return atom_snippets_fixture  

def test_convert():
    data = load_fixture()[0]
    result = (
    'snippet audio.dispose(audioHandle) "Releases audio memory associated with the handle."\n' +
    'audio.dispose( ${1:audioHandle} )\n' + 
    'endsnippet')
    assert result == convert(data)
