# -*- coding: utf-8 -*-

import json
import os
from janome.tokenizer import Tokenizer

# tokenizerの初期化
tokenizer = Tokenizer()


def make_vocab_file(input_dir_name):
    """
    jsonファイルが入ったディレクトリを読み込んで形態素解析した単語を出力する

    :param input_dir_name -- 読み込むjsonファイルが入ったディレクトリ名 ※対話破綻コーパスのjsonファイルに限る
    """
    input_dir = os.listdir(input_dir_name)

    for file in input_dir:
        path = os.path.join(input_dir_name, file)
        # 入出力ファイルを開く
        with open(path, "r", encoding="utf-8") as f, \
                open("Vocabulary/verb.txt", "w", encoding="utf-8") as v_file, \
                open("Vocabulary/noun.txt", "w", encoding="utf-8") as n_file, \
                open("Vocabulary/adjective.txt", "w", encoding="utf-8") as a_file:
            json_data = json.load(f)
            # コーパスの一つの発話に対して
            for turn in json_data["turns"]:
                token_list = tokenizer.tokenize(turn["utterance"])
                classify_word(token_list, v_file, n_file, a_file)

    print("Succeeded!")


def classify_word(token_list, v_file, n_file, a_file):
    """
    形態素解析された語のリストを品詞(動詞、形容詞、名詞)で分類してそれぞれ別のファイルに保存する

    :param token_list: 形態素解析された語のtokenオブジェクトのリスト

    :param v_file: 動詞の出力ファイル

    :param n_file: 名詞の出力ファイル

    :param a_file: 形容詞の出力ファイル
    """
    for token in token_list:
        part = token.part_of_speech.split(',')[0]    # 品詞
        if part == "動詞":
            v_file.write(token.surface + "\n")
        elif part == "名詞":
            n_file.write(token.surface + "\n")
        elif part == "形容詞":
            a_file.write(token.surface + "\n")


if __name__ == '__main__':
    make_vocab_file("JSON_corpus")

