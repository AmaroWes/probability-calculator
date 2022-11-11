import copy
import random


class Hat:
    
    def __init__(self, **kargs):
        self.contents = list()
        self.val = list(kargs.values())
        self.colors = list(kargs.keys())
        self.conversor(self.val, self.colors)

    def conversor(self, val, colors):
        for i in range(len(colors)):
            for c in range(val[i]):
                self.contents.append(colors[i])

    def draw(self, num):
        aux_list = list()
        if num > len(self.contents):
            return self.contents
        for n in range(num):
            x = random.randint(0, len(self.contents) - 1)
            aux_list.append(self.contents[x])
            self.contents.remove(self.contents[x])
        return aux_list
            


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    cont = 0
    expected = list()
    colors = list(expected_balls.keys())
    val = list(expected_balls.values())

    for x in range(len(val)):
        for i in range(val[x]):
            expected.append(colors[x])

    for n in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        real_amount = hat_copy.draw(num_balls_drawn)
        for i in range(len(expected)):
            if expected[i] in real_amount:
                position = real_amount.index(expected[i])
                real_amount.remove(real_amount[position])
                if len(real_amount) == num_balls_drawn - len(expected):
                    cont += 1
                
    return cont / num_experiments 
