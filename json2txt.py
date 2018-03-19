# -*- coding: utf-8 -*-

import json
import os
from janome.tokenizer import Tokenizer

# tokenizerの初期化
tokenizer = Tokenizer()


def make_vocab_file(input_dir_name, output_file_name):
    """
    jsonファイルが入ったディレクトリを読み込んで形態素解析した単語を出力する。

    :param input_dir_name -- 読み込むjsonファイルが入ったディレクトリ名 ※対話破綻コーパスのjsonファイルに限る

    :param output_file_name -- 形態素解析した語を出力するテキストファイル名
    """
    input_dir = os.listdir(input_dir_name)
    output_file = open(output_file_name, "w", encoding="utf-8")

    for file in input_dir:
        path = os.path.join(input_dir_name, file)
        with open(path, "r", encoding="utf-8") as f:
            json_data = json.load(f)
            for turn in json_data["turns"]:
                token_list = tokenizer.tokenize(turn["utterance"])
                token = list2str(token_list)
                output_file.write(token + "\n")

    output_file.close()
    print("Succeeded!")


def list2str(words):
    """
    形態素解析した語のリストを改行文字を区切り文字として連結する。

    :param words

    :return: joined_words
    """
    # 以下の文字は除外する
    exceptional_char = [',', '.', '、', '。', '?', '？', '!', '！', '～', 'ー', '「', '」']
    words_list = [word.surface for word in words if word.surface not in exceptional_char]
    joined_words = "\n".join(words_list)
    return joined_words

if __name__ == '__main__':
    make_vocab_file("JSON_corpus", "vocabulary.txt")

