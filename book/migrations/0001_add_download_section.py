# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Book.book_file'
        db.add_column('book_book', 'book_file',
                      self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Book.book_file'
        db.delete_column('book_book', 'book_file')


    models = {
        'book.author': {
            'Meta': {'object_name': 'Author'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'headshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'book.book': {
            'Meta': {'object_name': 'Book'},
            'add_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'annotation': ('django.db.models.fields.TextField', [], {'default': "'\\xd0\\x9e\\xd0\\xbf\\xd0\\xb8\\xd1\\x81\\xd0\\xb0\\xd0\\xbd\\xd0\\xb8\\xd0\\xb5 \\xd0\\xbe\\xd1\\x82\\xd1\\x81\\xd1\\x83\\xd1\\x82\\xd1\\x81\\xd1\\x82\\xd0\\xb2\\xd1\\x83\\xd0\\xb5\\xd1\\x82('", 'blank': 'True'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['book.Author']", 'symmetrical': 'False', 'blank': 'True'}),
            'book_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'oblojka': ('django.db.models.fields.files.ImageField', [], {'default': "'imag_book/none.jpg'", 'max_length': '100', 'blank': 'True'}),
            'podseria': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'res_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'serias': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['book.Seria']", 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url_l': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'book.seria': {
            'Meta': {'object_name': 'Seria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['book']