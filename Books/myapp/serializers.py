from rest_framework import serializers
from .models import Book
import os


class BookListSerailizer(serializers.ModelSerializer):

    # picture = serializers.SerializerMethodField('')
    # picture = serializers.ImageField(
    #         max_length=None, use_url=True
    #     )
    
    class Meta:
        model = Book
        fields = ['id','title','description','author','year','picture','pdf']


    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.picture.url
        return request.build_absolute_uri(photo_url)
    
    def get_pdf_url(self,obj):
        request = self.context.get('request')
        pdf_url = obj.pdf.url
        return request.build_absolute_uri(pdf_url)
    


    # def get_image_url(self, obj):
    #     return obj.picture.url