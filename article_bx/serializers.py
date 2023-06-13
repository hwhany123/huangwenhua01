from rest_framework import serializers
from article_bx.models import bx_clbx
from user_info.serializers import UserDescSerializer







class ArticleBaseSerializer(serializers.HyperlinkedModelSerializer):
    """
    文章序列化器父类
    """
    id = serializers.IntegerField(read_only=True)
    author = UserDescSerializer(read_only=True)


    # 自定义错误信息
    default_error_messages = {
        'incorrect_avatar_id': 'Avatar with id {value} not exists.',
        'incorrect_category_id': 'Category with id {value} not exists.',
        'default': 'No more message here..'
    }

    def check_obj_exists_or_fail(self, model, value, message='default'):
        if not self.default_error_messages.get(message, None):
            message = 'default'

        if not model.objects.filter(id=value).exists() and value is not None:
            self.fail(message, value=value)


class ArticleSerializer(ArticleBaseSerializer):
    class Meta:
        model = bx_clbx
        fields = '__all__'



class ArticleDetailSerializer(ArticleBaseSerializer):
    id = serializers.IntegerField(read_only=True)





    class Meta:
        model = bx_clbx
        fields = '__all__'

# class ArticleSerializer(serializers.HyperlinkedModelSerializer):
#     """博文序列化器"""
#     author = UserDescSerializer(read_only=True)
#     # category 的嵌套序列化字段
#     category = CategorySerializer(read_only=True)
#     # category 的 id 字段，用于创建/更新 category 外键
#     category_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)
#     # tag 字段
#     tags = serializers.SlugRelatedField(
#         queryset=Tag.objects.all(),
#         many=True,
#         required=False,
#         slug_field='text'
#     )
#
#     # 覆写方法，如果输入的标签不存在则创建它
#     def to_internal_value(self, data):
#         tags_data = data.get('tags')
#
#         if tags_data is not None:
#             for text in tags_data:
#                 if not Tag.objects.filter(text=text).exists():
#                     Tag.objects.create(text=text)
#
#         return super().to_internal_value(data)
#
#     # category_id 字段的验证器
#     def validate_category_id(self, value):
#         # 数据存在且传入值不等于None
#         if not Category.objects.filter(id=value).exists() and value != None:
#             raise serializers.ValidationError("Category with id {} not exists.".format(value))
#
#         return value
#
#     class Meta:
#         model = Article
#         fields = '__all__'

# class ArticleDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'
#
#
# class ArticleListSerializer(serializers.ModelSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name="article:detail")
#
#     author = UserDescSerializer(read_only=True)
#
#     class Meta:
#         model = Article
#         fields = [
#             'url',
#             # 'id',
#             'title',
#             'created',
#             'author',
#         ]
# read_only_fields = ['author']

# class ArticleListSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(allow_blank=True, max_length=100)
#     body = serializers.CharField(allow_blank=True)
#     created = serializers.DateTimeField()
#     updated = serializers.DateTimeField()
