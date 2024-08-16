# ООП
# принципы ООП


class Book:
    strr = 400
    # методы
    def __init__(self, title, author, color):
        self.title = title
        self.author = author
        self.color = color

        def __len__(self):
            return len(self.title + self.author + self.color)

        beka = Book('Этомир', 'beka', 'black',)


        # def info(self):
        #     print(self.title,self.color,self.strr,self.author)
#
# # объект\экземпляр класса
# gород_воров=Book('город воров','Каныкей','зеленый')
# kапитанская_дочка=Book('Капитанская дочка','Пушкин','серый')
#
# print(gород_воров.strr)



def a(b):
    print(b)


