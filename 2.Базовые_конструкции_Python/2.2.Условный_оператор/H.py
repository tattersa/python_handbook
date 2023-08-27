sentence = input()


def check_sentence(x):
    if "зайка" in x or "Зайка" in x:
        return True
    else:
        return False


if check_sentence(sentence):
    print("YES")
else:
    print("NO")
