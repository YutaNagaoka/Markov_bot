import random


def bot(corpus, word_len):
    """
    マルコフ連鎖によって文章を作成する。
    :param corpus: 単語ごとに開業したテキストファイル
    :param word_len: 作成する文の単語数
    """
    vocab_file = open(corpus, "r", encoding="utf-8")
    vocab_list = []
    for vocab in vocab_file:
        vocab_list.append(vocab)

    for i in range(10):
        utterance = random.sample(vocab_list, k=word_len)
        utterance = [s.strip("\n") for s in utterance]
        utterance = "".join(utterance)
        print(utterance)


if __name__ == '__main__':
    word_len = 10
    bot("vocabulary.txt", word_len)
