import random


class Bot1:
    def __init__(self, corpus, word_length):
        self.corpus = corpus
        self.word_length = word_length

    def utter(self):
        vocab_file = open(self.corpus, "r", encoding="utf-8")
        vocab_list = [vocab for vocab in vocab_file]

        for i in range(10):
            utterance = random.sample(vocab_list, k=self.word_length)
            utterance = [s.strip("\n") for s in utterance]
            utterance = "".join(utterance)
            print(utterance)


if __name__ == '__main__':
    word_len = 10
    bot1 = Bot1("vocabulary.txt", 10)
    bot1.utter()
