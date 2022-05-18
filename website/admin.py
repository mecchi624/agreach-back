from django.contrib import admin

# モデルをインポート
from . models import SampleModel

# 管理ツールに登録
admin.site.register(SampleModel)