import random

# 5. Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):


def get_jokes_adv(jokes_count, uniq=False):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    for i in range(jokes_count):
        if not (len(nouns) and len(adverbs) and len(adjectives)):
            break
        noun = random.choice(nouns)
        adverb = random.choice(adverbs)
        adjective = random.choice(adjectives)
        jokes.append(f"{noun} {adverb} {adjective}")

        if uniq:
            nouns.remove(noun)
            adverbs.remove(adverb)
            adjectives.remove(adjective)
    return jokes


print(get_jokes_adv(4, False))
print(get_jokes_adv(53, False))
print(get_jokes_adv(63, True))
