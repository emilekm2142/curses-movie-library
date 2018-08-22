# -*- coding: utf-8 -*-
import time

class Movie():

    def __init__(self, title, desc, comments, rating, info):
        super(Movie, self).__init__()
        self.title = title
        self.comments = comments
        self.rating = rating
        self.desc = desc
        self.info = info


class DataBase():

    def __init__(self):
        super(DataBase, self).__init__()

    def load(self):
        self.base_raw = open("database.txt", 'r')
        movielist = []
        base = self.base_raw.read()
        base = base.split('$')
        print(base)
        for line_num in base:
            if line_num=="\n" or line_num=='':
                pass
            else:
                temponary = line_num.split('|')
                movielist.append(Movie(temponary[1], temponary[2], temponary[3], temponary[4], temponary[5]))
        self.base_raw.close()
        return movielist

    def make(self, filename):
        pass

    def save(self,savedata):
        self.base_raw.close()
        self.base_file = open("database.txt", 'w')
        for i in range(len(savedata)):
            print(savedata[i].title)
            print(savedata[i].desc)
            print(savedata[i].comments)
            print(savedata[i].rating)
            print(savedata[i].info)
            print('\n')

        for i in range(len(savedata)):
            self.base_file.write('id')
            self.base_file.write('|')
            self.base_file.write(savedata[i].title)
            self.base_file.write('|')
            self.base_file.write(savedata[i].desc)
            self.base_file.write('|')
            self.base_file.write(savedata[i].comments)
            self.base_file.write('|')
            self.base_file.write(savedata[i].rating)
            self.base_file.write('|')
            self.base_file.write(savedata[i].info)
            self.base_file.write('$')
        self.base_file.close()