class Wm():
    def __init__(self, n, c):
        self.n=n
        self.c=c

    def show_wm(self):
        y="{} : {}" .format(self.n, self.c)
        print(y)

    def name(self):
        print(self.n)

class Md(Wm):
    def __init__(self, n, c, r):
        super().__init__(n, c)
        self.r=r

    def name(self):
        print(self.n)

    def show_md(self):
        x="It's {} from {}!".format(self.n, self.c)
        print(x)

    def rzmr(self):
        print("{} has {} razmer".format(self.n,self.r))

wm1=Wm("Ivvi", "Void")
wm1.show_wm()

md1=Md("Ruth", "NY", "42")
md1.show_wm()
md1.show_md()
md1.rzmr()
u="{} : {} __ {}".format(wm1.n, md1.c, md1.r)
print(u)
wm1.name()
md1.name()

