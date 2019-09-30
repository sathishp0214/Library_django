# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models  
from django.contrib.auth.models import User
class Bookdata(models.Model):  
    bookid = models.IntegerField()  
    bookname = models.CharField   
    bookpublisher = models.CharField(max_length=50)  
    class Meta:  
        db_table = "library"

class login_users(models.Model):
    user = models.ForeignKey(User)
    book_id = models.IntegerField()
    book_names = models.CharField(max_length=75)
    book_publisher = models.CharField(max_length=50)
    class Meta:  
        db_table = "login_users"

class make_query(models.Model):
    Name = models.CharField('Name:',max_length=20)  
    email = models.EmailField('Email_ID:')  
    mobile = models.IntegerField("Mobile_No:")
    message = models.CharField('Message:',max_length=300)
    class Meta:  
        db_table = "user_queries"



