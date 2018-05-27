class Bot2_neo:
    BEGIN = "__BOS__"
    END = "__EOS__"

    def __init__(self, corpus_path):
        self.corpus_path = corpus_path
        self.triplet_list = self.DB2triplet()
        
    def utter(self):
        """
        n回発話し、ユーザとのインターフェースになる
        """
        triplet_list = self.triplet_list
        utterance = self.generate_text(triplet_list)
        print utterance
        
    def generate_text(self, triplet_list):
        """
        ランダムな1文を生成する
        :param triplet_list: 三つ組のlist
        :return: 生成された1文
        """
        utterance = []

        candidate = []
        for s in triplet_list:
            if s[0] == self.BEGIN:
                candidate.append(s)
        first_triplet = random.choice(candidate)
        utterance.append(first_triplet[1])
        utterance.append(first_triplet[2])

        while utterance[-1] != self.END:
            prefix1 = utterance[-2]
            prefix2 = utterance[-1]
            # エラー処理
            try:
                triplet = self.search_triplet(triplet_list, (prefix1, prefix2))
            except IndexError:
                return "error"
            utterance.append(triplet[2])

        result = "".join(utterance[:-1])
        return result
        
    def search_triplet(triplet_list, prefixes):
        """
        三つ組のlistの中から条件(prefixes)に適する三つ組を取得
        :param triplet_list: 三つ組のlist
        :param prefixes: 条件(prefix1, prefix2)
        :return: 三つ組
        """
        candidate = []
        for triplet in triplet_list:
            if triplet[0] == prefixes[0] and triplet[1] == prefixes[1]:
                candidate.append(triplet)

        result = random.choice(candidate)
        return result

    def DB2triplet(self):
        """
        3-gramで分割されたコーパスを読み込む
        :return: 三つ組のlist(二次元list)
        """
        triplet_list = []

        with open(self.corpus_path, "r", encoding="utf-8") as corpus:
            for triplet in corpus:
                t_list = triplet.strip().split(",")
                triplet_list.append(t_list)

        return triplet_list
