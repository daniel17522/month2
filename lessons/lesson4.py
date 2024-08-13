#принципы ооп абстракция, множ наследование
from lesson3 import Nowella,Book

# супер класс - object

class Manga(Nowella):

    def reads(self):
        print(f'я люблю мангу: {self.title}')


manga=Manga('берсерк','кентаро миура',2500,'70x70')
# manga.reads()
# print(manga)
#MRO-порядок выполнения методов
# print(Manga.mro())
class Anime(Nowella,):

    def __init__(self, title, author, price, pnj,name):
        Nowella.__init__(self,title, author, price, pnj)


    def reads(self):
        Book.reads(self)


anime=Anime('Naruto','кисимото',2500,'70x70','beka')
print(anime)
anime.reads()
anime.anime()

print(Anime.mro())

# print(Anime.mro())

# не нарушать порядок наследования
# в цепочке классов только у одного класса должны быть магические методы