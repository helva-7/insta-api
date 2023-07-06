from django.shortcuts import render
from instabot import Bot
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AliExpressItem

class AliExpressItemAPIView(APIView):
    def post(self, request):
        image = request.FILES.get('image')
        text = request.data.get('text')
        aliexpress_item = AliExpressItem.objects.create(image=image, text=text)
        # Add Instagram posting logic here
        bot = Bot()
        bot.login(username='zeeverything_anime_morocco', password='fahd@141002@fahd')
        bot.upload_photo(aliexpress_item.image.path, caption=aliexpress_item.text)
        bot.logout()

        return Response({'message': 'Item posted on Instagram'})
        
    