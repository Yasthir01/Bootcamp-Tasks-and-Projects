import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
# words of my own
word4 = nlp("dog")
word5 = nlp("bone")

print(word1.similarity(word2))  # cat and monkey
print(word3.similarity(word2))  # banana and monkey
print(word3.similarity(word1))  # banana and cat
print(word4.similarity(word5))  # dog and bone. N.B gets a low-ish score of 0.35

"""What's interesting above is that Banana and Monkey are two things that go well 
together in the real world, but in this analysis it only scored a 
0.45 it terms of the actual words."""


"""
When using the sm model, it outputs the following warning: 
'The model you're using has no word vectors loaded, 
so the result of the Doc.similarity method will be based on the tagger, parser and NER, 
which may not give useful similarity judgements.'

What's interesting is that eventhough we are using this model, we end up getting
a better score for monkey and banana.

"""
