from collections import defaultdict


def best_sender(messages, senders):
    result_dict = defaultdict(int)

    for k, v in zip(messages, senders):
        result_dict[v] += len(k.split())

    return sorted(result_dict.items(),
                  key=lambda x: (x[1], x[0]), reverse=True)[0][0]


messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
senders = ['Sam Fisher', 'Linda', 'Sam Fisher']

print(best_sender(messages, senders))