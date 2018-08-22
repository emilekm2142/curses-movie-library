# -*- coding: utf-8 -*-
import view
import time
import models
class Controller():

    def __init__(self):
        super(Controller, self).__init__()
        #Tutaj jest kod kontrollera
        self.database_object = models.DataBase()
        self.database = self.database_object.load()
        self.view_obj=view.View()
        while True:
            choose=self.view_obj.mainmenu()
            if choose=='addform':
                data=self.view_obj.addForm()
                self.addMovie(data[0],data[1],data[2],data[3],data[4])
            elif choose=='browse':
                movie_to_browse = self.view_obj.browse(self.database)
                x = self.view_obj.details(movie_to_browse,self.database)

    def addMovie(self, title, desc, comments, rating, info):
        self.database.append(models.Movie(title.decode('utf-8'), desc, comments, rating.decode('utf-8'), info.decode('utf-8')))
        self.database_object.save(self.database)
