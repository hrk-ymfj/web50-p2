from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

# Register your models here.
# models.pyに存在する全モデルを、管理者サイトで変更可能にする
admin.site.register(User)
admin.site.register(Category)
admin.site.register(AuctionListing)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(Watchlist)

