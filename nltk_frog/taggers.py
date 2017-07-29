from nltk.tag.api import TaggerI
from pynlpl.formats import folia
from frog import Frog, FrogOptions


class FrogTagger(TaggerI):

    def __init__(self, **kwargs):
        # Disable multiword recognition, which is performed by the chunker
        options = FrogOptions(parser=False, mwu=False, xmlIn=True, **kwargs)
        self.__frog = Frog(options)

    def tag(self, sentences):

        if isinstance(sentences, list):
            doc = folia.Document(id='nltk-sentence')
            folia_sent = doc.add(folia.Text)
            for sent in sentences:
                folia_sent.add(folia.Word, sent)
            _input = doc
        else:
            _input = sentences
        self.__output = self.__frog.process(_input)
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