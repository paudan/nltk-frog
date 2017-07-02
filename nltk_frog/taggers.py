from nltk.tag.api import TaggerI
from frog import Frog, FrogOptions


class FrogTagger(TaggerI):

    def __init__(self):
        # Disable multiword recognition, which is performed by the chunker
        options = FrogOptions(parser=False, mwu=False)
        self.__frog = Frog(options)

    def tag(self, sentences):

        if isinstance(sentences, list):
            _input = ''
            for sent in sentences:
                if isinstance(sent, list):
                    _input += ' '.join((x for x in sent))
                else:
                    _input += ' ' + sent
            _input = _input.lstrip()
            _input += '\n'
        else:
            _input = sentences
        self.__output = self.__frog.process(_input)
        print(self.__output)
        return [(token['text'], token['pos'].split('(')[0]) for token in self.__output]

    def get_tag_probabilities(self):
        if self.__output is None:
            return []
        return [(token['text'], token['posprob']) for token in self.__output]

    def get_lemmas(self):
        if self.__output is None:
            return []
        return [(token['text'], token['lemma']) for token in self.__output]

    def get_morph(self):
        if self.__output is None:
            return []
        return [(token['text'], token['morph']) for token in self.__output]