import re
import operator


class Solution:
    def calculate(self, s):
        operations = {'*': operator.mul,
                      '/': operator.floordiv,
                      '+': operator.add,
                      '-': operator.sub}
        symbol_set = set(operations.keys())
        while True:
            for i, c in enumerate(s):
                if c in ('*', '/') and i != 0:
                    symbol, op = c, operations[c]
                    pattern = re.compile(f'(([0-9 ]+)\\{symbol}([0-9 ]+))')
                    groups = pattern.search(s).groups()

                    value = str(op(int(groups[1]), int(groups[2])))

                    s = s.replace(groups[0], value, 1)
            else:
                while True:
                    for i, c in enumerate(s):
                        if c in ('+', '-') and i != 0:
                            symbol, op = c, operations[c]
                            pattern = re.compile(f'((\-?[0-9 ]+)\\{symbol}([0-9 ]+))')
                            groups = pattern.search(s).groups()
                            value = str(op(int(groups[1]), int(groups[2])))
                            s = s.replace(groups[0], value, 1)
                    else:
                        return int(s)
