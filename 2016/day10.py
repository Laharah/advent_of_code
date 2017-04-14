import re
from common import Input
from pprint import pprint

BOTS = {}
OUTPUTS = {}
INIT = []


class Bot:
    def __init__(self, send_low, send_high):
        self.values = set()
        self.compairisons = set()
        self.send_low  = send_low
        self.send_high = send_high


def load_instructions(fin):
    for line in fin:
        if line.startswith('bot'):
            parse_bot(line)
        elif line.startswith('value'):
            parse_value(line)
    return


def parse_bot(line):
    # bot 7 gives low to bot 148 and high to bot 22
    match = re.match(
        r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)', line)
    bot, low_type, low_id, high_type, high_id = match.groups()
    if bot in BOTS:
        raise ValueError('bot {} already assigned!'.format(bot))
    BOTS[bot] = Bot((low_type, low_id), (high_type, high_id))


def parse_value(line):
    # value 23 goes to bot 8
    match = re.match(r'value (\d+) goes to bot (\d+)', line)
    value, bot = match.groups()
    INIT.append((int(value), bot))


def simulate():
    for value, bot in INIT:
        BOTS[bot].values.add(value)
    flag = True
    while flag:
        flag = False
        for bot_id, bot in BOTS.items():
            if len(bot.values) == 2:
                flag = True
                low, high = sorted(bot.values)
                send(*bot.send_low, low)
                send(*bot.send_high, high)
                bot.values.clear()


def send(to_type, to_id, value):
    if to_type == 'bot':
        bot = BOTS[to_id]
        bot.values.add(value)
        if len(bot.values) > 2:
            raise ValueError("bot {} is full and cannot receive".format(to_id))
        if 61 in bot.values and 17 in bot.values:
            print('ANSWER FOUND: BOT {} compairs 61 and 17'.format(to_id))
    elif to_type == 'output':
        try:
            OUTPUTS[to_id].add(value)
        except KeyError:
            OUTPUTS[to_id] = {value}
    return


if __name__ == '__main__':
    load_instructions(Input(10))
    simulate()
    to_mult = []
    for i in range(3):
        i = str(i)
        pprint(OUTPUTS[i])
        to_mult.append(OUTPUTS[i].pop())
    a, b, c = to_mult
    print(a * b * c)
