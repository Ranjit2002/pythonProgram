import random
class space:
    def __init__(self):
        self.list1 = list()

    def bell(self):
        for i in range(1, 95):
            rand = random.randrange(1, 100)
            # print(f"{i} = {rand}")
            self.list1.append(rand)

    def pr_list(self):
        print(self.list1)

    def mobile(self):
        while True:
            if len(self.list1) < 94:
                pass


a = space()
a.bell()
a.pr_list()
