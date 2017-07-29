from nltk.chunk import conlltags2tree
from nltk.chunk.api import ChunkParserI
from frog import Frog, FrogOptions
from pynlpl.formats import folia


class AbstractFrogChunker(ChunkParserI):

    _frog = None

    def __init__(self, **kwargs):
        self._frog = Frog(FrogOptions(parser=False, mwu=False, tok=False, xmlIn=True, **kwargs))

    def __get_folia_doc__(self, tokens):
        doc = folia.Document(id='nltk-sentence')
        folia_sent = doc.add(folia.Text)
        for tok, pos in tokens:
            word = folia_sent.add(folia.Word, tok)
            word.add(folia.PosAnnotation(None, set='custom', cls=pos))
        return doc

    def __create_tree__(self, tokens, key):
        _input = self.__get_folia_doc__(tokens)
        __output = self._frog.process(_input)
        for token in __output:
            token['pos'] = token['pos'].split('(')[0]
            if token['pos'].startswith('SPEC'):
                token['pos'] = 'NNP'
        return conlltags2tree([(token['text'], token['pos'], token[key]) for token in __output ])

    def parse(self, tokens):
        raise NotImplementedError()


class FrogDefaultChunker(AbstractFrogChunker):

    def parse(self, tokens):
        return self.__create_tree__(tokens, 'chunker')


class FrogNERChunker(AbstractFrogChunker):

    def parse(self, tokens):
        return self.__create_tree__(tokens, 'ner')


class FrogChunker(AbstractFrogChunker):

    def parse(self, tokens):
        _input = self.__get_folia_doc__(tokens)
        __output = self._frog.process(_input)
        for token in __output:
            token['pos'] = token['pos'].split('(')[0]
            if token['pos'].startswith('SPEC'):
                token['pos'] = 'NNP'
            if token['chunker'] != 'O' and token['ner'] == 'O':
                token['ner'] = token['chunker']
        return conlltags2tree([(token['text'], token['pos'], token['ner']) for token in __output ])
