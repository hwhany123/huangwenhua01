from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    仅管理员用户可进行修改
    其他用户仅可查看
    """

    def has_permission(self, request, view):
        print(request.user)
        # 对所有人允许 GET, HEAD or OPTIONS 请求.
        #if request.method in permissions.SAFE_METHODS:
            #return True
        print('状态1', request.user.is_staff)
        print('状态3', request.user)
        print('状态4', request.user.is_superuser)
        if request.user.is_staff==True:
            print('状态2',request.user.is_staff)
            return True


        # 仅管理员可进行其他操作
        return request.user.is_superuser
        #return True
