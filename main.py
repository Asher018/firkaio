import random


def give_random_word():
    dictionary = ["dog", "cat", "house", "head", "number", "tree", "sky", "sun", "boat", "elbow", "chimney",
                  "computer",
                  "flag", "bird", "fish", "money", "bow", "axe", "scissors", "glasses"]
    return random.choice(dictionary)


if __name__ == '__main__':
    print(give_random_word())
