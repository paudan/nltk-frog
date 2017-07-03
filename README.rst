nltk-frog
============

NLTK interface with `Frog NLP package <https://languagemachines.github.io/frog//>`__

Copyright (C) 2017 Paulius Danenas

Dependencies
------------

-  `Frog <https://languagemachines.github.io/frog//>`__ NLP package
-  Python 2.7 or Python 3
-  `NLTK <http://nltk.org/>`__

Tested with Frog 0.13, Python 2.7/3.5 and NLTK 3.2.4

Installation
------------

Before you install the ``nltk-frog`` package please ensure you have downloaded and installed the
`Frog NLP package <https://languagemachines.github.io/frog//>`__.

Usage
-----

Tagging a sentence from Python:

.. code:: python

    from nltk_frog.taggers import FrogTagger
    tagger = FrogTagger()
    phrase = 'Volkswagen Polo 00-PXX-5 (4NG)'
    tagger.tag(phrase)

Note that, besides passing lists of tokens as defined by NLTK interface class, one can also pass full text strings, without any tokenization performed
previously (as shown in the example above). The output is a list of (token, tag), which is more similar to NLTK contract:

::

    [('Pierre', 'NNP'), ('Vinken', 'NNP'), (',', ','), ('61', 'CD'),
    ('years', 'NNS'), ('old', 'JJ'), (',', ','), ('will', 'MD'),
    ('join', 'VB'), ('the', 'DT'), ('board', 'NN'), ('as', 'IN'),
    ('a', 'DT'), ('nonexecutive', 'JJ'), ('director', 'NN'),
    ('Nov.', 'NNP'), ('29', 'CD'), ('.', '.')]


Named entity recognition (NER)
------------------------------

This module also supports named entity recognition, which allows to tag particular types of entities. Currently, three chunker modifications are possible:

-  ``FrogDefaultChunker`` which uses exclusively chunker information to create a chunker parse tree
-  ``FrogNERChunker`` which exploits only named entity information for such tree generation
-  ``FrogChunker`` which combines both chunking and NER information in chunker parse tree

An example is given below which demonstrates the output of ``FrogChunker``. The input, consistently with NLTK, is the set of (token, tag) entries
(naturally, other NLTK taggers could be used instead of ``FrogTagger``):

.. code:: python

    from nltk_frog.taggers import FrogTagger
    from nltk_frog.chunkers import FrogChunker
    phrase = 'Volkswagen Polo 40-PXH-7 (4NG)'
    tagger = FrogTagger()
    tagged = tagger.tag(phrase)
    chunker = FrogChunker()
    chunker.parse(tagged)

The output is a chunk parse tree with particular types of entities:

::

    (S
      (PER Volkswagen/NNP Polo/NNP)
      (NP 40-PXH-7/TW)
      (/LET
      (NP 4/TW NG/NNP)
      )/LET)

