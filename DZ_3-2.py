"""
 В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
 Не учитывать знаки препинания и регистр символов.
 За основу возьмите любую статью из википедии или из документации к языку.
"""

PUNTATION_MARKS = '.,;!?—:()\',\"«»“„[]{}'
counter = {}


def delete_punctuation_marks(text):
    for letter in PUNTATION_MARKS:
        text = text.replace(letter, ' ')

    return text


def calc_word_in_text(text):
    text = delete_punctuation_marks(text).lower()
    text_lst = text.split()

    for word in text_lst:
        if not counter.get(word):
            counter.setdefault(word, 1)
        else:
            counter[word] += 1

    return sort_counter_words(counter)[:10]


def sort_counter_words(counter):
    counter_lst = list(counter.items())
    counter_lst.sort(key=lambda x: x[1], reverse=True)
    return counter_lst


if __name__ == '__main__':
    text = """Совообра́зные (лат. Strigiformes) — отряд, включающий более 200 видов птиц преимущественно средней величины (от мелких до крупных), распространённых во всех частях света, кроме Антарктики и некоторых островов. В отряде два современных семейства: совиные, или настоящие совы, а также сипуховые.

Совообразные обладают крупной головой и большими глазами. Клюв короткий, загнутый, когти острые, загнутые. Окраска покровительственная (маскирующая). Большинство видов охотятся ночью, в связи с чем имеют мягкое оперение и бесшумный полёт."""
    print(*calc_word_in_text(text))