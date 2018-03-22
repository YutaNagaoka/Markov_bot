import random
from janome.tokenizer import Tokenizer

t = Tokenizer()


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


class Bot2:
    BEGIN = "__BOS__"
    END = "__EOS__"

    def __init__(self, corpus_path, n):
        self.corpus_path = corpus_path
        self.n = n

    def morpheme_analysis(self, sentence):
        """
        1文の形態素解析を行う
        :param sentence: 入力文
        :return: 形態素に分割された文字列型のlist
        """
        token_list = t.tokenize(sentence)
        morphemes = [token.surface for token in token_list]
        return morphemes

    def generate_quartet(self, morphemes):
        """
        形態素に分割された文字列型のlistを四つ組にする
        :param morphemes: 形態素に分割された文字列型のlist
        :return: 四つ組
        """
        if len(morphemes) < 4:
            return []

        quartet = []
        for i in range(len(morphemes) - 3):
            quartet.append(morphemes[i:i+4])

        # BOSを追加
        quartet.insert(0, [self.BEGIN, morphemes[0], morphemes[1], morphemes[2]])
        # EOSを追加
        quartet.append([morphemes[-3], morphemes[-2], morphemes[-1], self.END])

        return quartet

    def txt2quartets(self):
        """
        コーパスの全文を形態素解析して四つ組に分割する
        :return: 四つ組のlist(二次元list)
        """
        quartet_list = []
        with open(self.corpus_path, "r") as corpus:
            for sentence in corpus:
                morphemes = self.morpheme_analysis(sentence)
                quartet = self.generate_quartet(morphemes)
                quartet_list.append(quartet)

        return quartet_list

    def generate_text(self, quartet_list):
        utterance = []

        candidate = [s for s in quartet_list if s[0] == self.BEGIN]
        first_quartet = random.choice(candidate)
        utterance.append(first_quartet[1])
        utterance.append(first_quartet[2])
        utterance.append(first_quartet[3])



if __name__ == '__main__':
    word_len = 10
    bot1 = Bot1("vocabulary.txt", 10)
    bot1.utter()
