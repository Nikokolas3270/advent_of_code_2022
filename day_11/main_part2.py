#!/usr/bin/env python3

monkeyPrefix = "Monkey "
itemsPrefix = "Starting items: "
operationPrefix = "Operation: new = old "
testOperandPrefix = "Test: divisible by "
truePrefix = "If true: throw to monkey "
falsePrefix = "If false: throw to monkey "

monkeys = []

class Monkey:
    def __init__(self):
        self._index = -1
        self._items = []
        self._operation = ''
        self._operand = 0
        self._testOperand = 0
        self._trueMonkeyIndex = -1
        self._falseMonkeyIndex = -1
        self._inspectCount = 0

    def read(self, f):
        while True:
            l = f.readline().strip()
            if not l:
                break
            
            if l.startswith(monkeyPrefix):
                self._index = int(l[len(monkeyPrefix):-1])
            elif l.startswith(itemsPrefix):
                self._items = [int(item.strip()) for item in l[len(itemsPrefix):].split(',')]
            elif l.startswith(operationPrefix):
                self._operation = l[len(operationPrefix)]
                self._operand = l[len(operationPrefix)+2:]
            elif l.startswith(testOperandPrefix):
                self._testOperand = int(l[len(testOperandPrefix):])
            elif l.startswith(truePrefix):
                self._trueMonkeyIndex = int(l[len(truePrefix):])
            elif l.startswith(falsePrefix):
                self._falseMonkeyIndex = int(l[len(falsePrefix):])
            else:
                raise Exception("Unexpected monkey definition line: " + l)

    def playTurn(self):
        items = self._items
        self._items = []
        for item in items:
            if self._operand == "old":
                operand = item
            else:
                operand = int(self._operand)
    
            if self._operation == '+':
                item += operand
            elif self._operation == '*':
                item *= operand
            else:
                raise Exception("Unsupported operation: " + self._operation)
            self._inspectCount += 1
            
            item = item % (13*19*11*17*3*7*5*2)

            newMonkeyIndex = self._falseMonkeyIndex if item % self._testOperand else self._trueMonkeyIndex
            monkeys[newMonkeyIndex]._items.append(item)
    
    def __repr__(self):
        return "[idx: %s, items: %s, op: %s %s, testOpd: %s, true: %s, false: %s , inspCnt: %s]" % (
            self._index,
            self._items,
            self._operation, self._operand,
            self._testOperand,
            self._trueMonkeyIndex,
            self._falseMonkeyIndex,
            self._inspectCount,
        )

with open("input") as f:
    while True:
        m = Monkey()
        m.read(f)
        if m._index == -1:
            break
        if m._index >= len(monkeys):
            monkeys.extend([None] * (m._index + 1 - len(monkeys)))
        monkeys[m._index] = m

    print('\n'.join([repr(m) for m in monkeys]))

    round = 1

    while True:
        for m in monkeys:
            m.playTurn()

        if round == 10000:
            break
        
        round += 1
    
    monkeys.sort(key=lambda m: -m._inspectCount)

    print('\n'.join([repr(m) for m in monkeys]))
    print(monkeys[0]._inspectCount * monkeys[1]._inspectCount)