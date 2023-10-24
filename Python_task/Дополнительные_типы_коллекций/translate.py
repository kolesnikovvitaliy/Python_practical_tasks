import sys
from string import ascii_lowercase


def coding(text: str, key: dict[str]) -> str:
    return "".join([key[j] if j in key else j
                    for i in text for j in i.lower()])


def create_dict_key(items: str) -> dict[str: str]:
    return {k: v for k, v in zip(ascii_lowercase, items)}


if __name__ == '__main__':
    key, text = sys.stdin.read().splitlines()
    dict_key = create_dict_key(key)
    result = coding(text, dict_key)
    sys.stdout.write(result + '\n')


# from string import ascii_letters

# translator = str.maketrans(ascii_letters, input() * 2)

# print(input().translate(translator))
