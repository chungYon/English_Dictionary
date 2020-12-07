from django.db import models


class Word(models.Model):
    word_text = models.CharField(max_length=200)
    meaning_text = models.CharField(max_length=400)
    synonym_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(verbose_name='date published')

    def __str__(self):
        return self.word_text
