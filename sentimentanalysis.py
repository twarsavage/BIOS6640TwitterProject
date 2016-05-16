

#import nltk
#nltk.download()

def demo_liu_hu_lexicon(sentence, plot=False):
    """
    Basic example of sentiment classification using Liu and Hu opinion lexicon.
    This function simply counts the number of positive, negative and neutral words
    in the sentence and classifies it depending on which polarity is more represented.
    Words that do not appear in the lexicon are considered as neutral.

    :param sentence: a sentence whose polarity has to be classified.
    :param plot: if True, plot a visual representation of the sentence polarity.
    """
    from nltk.corpus import opinion_lexicon
    from nltk.tokenize import treebank

    tokenizer = treebank.TreebankWordTokenizer()
    pos_words = 0
    neg_words = 0
    tokenized_sent = [word.lower() for word in tokenizer.tokenize(sentence)]

    x = list(range(len(tokenized_sent))) # x axis for the plot
    y = []

    for word in tokenized_sent:
        if word in opinion_lexicon.positive():
            pos_words += 1
            y.append(1) # positive
        elif word in opinion_lexicon.negative():
            neg_words += 1
            y.append(-1) # negative
        else:
            y.append(0) # neutral

    if (pos_words+neg_words) > 0:
        return (pos_words-neg_words)/float(pos_words+neg_words)
    else:
        return 0



#sample
#finalengsamp = finaleng.sample(frac=.1).copy()
finalengsamp = finaleng.copy()

#check performance
import time

start = time.time()
#demo_liu_hu_lexicon(Sentence)
#demo_liu_hu_lexicon(Sentence1)
finalengsamp['sentiment'] = finalengsamp['text'].map(demo_liu_hu_lexicon)
end = time.time()
print(end-start)


finalengsamp.to_csv('/home/ubuntu/Desktop/sentiment.csv',encoding='utf-8')






