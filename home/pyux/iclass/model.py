#!/usr/bin/python

class Model():
    def __init__(self, name, city):
        self.n=name
        self.cy=city
        self.__age=19

    def show_md(self):
        i=('%s from %s' % (self.n, self.cy))
        print(i)

    def modlook(self, drs, clr, numer):
        self.dr=drs
        self.cl=clr
        self.num=numer
        u=('%d : %s in %s %s' % (self.num, self.n, self.cl, self.dr))
        print(u)

    def input_age(self):
        w=('%s : %d' % (self.n, self.__age))
        print(w)

class Look(Model):
    def __init__(self, name, city, dress, color):
        super().__init__(name, city)
        self.d=dress
        self.c=color

    def show_lk(self):
        y=('%s in %s %s' % (self.n, self.c, self.d))
        print(y)

mod1=Model('Brook','NY')
mod2=Model('Kaia','NY')
mod3=Model('Umi','Tokyo')

mod2.show_md()
mod3.show_md()

mod1.modlook('skirt','black', 2)
mod2.modlook('top','purpl', 9)
mod3.input_age()

print("***** new class *****")
look1=Look('Miut','NY','skirt','black')
look2=Look('Branda','NY','blouse','red')

look1.show_lk()
look1.show_md()
look2.show_lk()
