from maya import models
from maya.service import admin
from maya.service.admin import SearchOption


class PermissionAdmin(admin.BaseMayaModel):
    #option函数
    from maya.service.custom.common import option

    from maya.service.custom.common import checkbox

    # 搜索自定义函数
    def caption(self, option, request):
        from maya.service.admin import FilterList
        from maya import models
        queryset = models.Permission.objects.filter(caption="权限添加")
        return FilterList(option, queryset, request)

    def menu(self, option, request):
        from maya.service.admin import FilterList
        queryset = models.Permission.objects.values_list('menu','menu__caption').distinct()
        return FilterList(option, queryset, request,extend=True)

    list_filter = [
        #SearchOption('caption', False,val_func_name='caption_title'),
        SearchOption('url', False,text_func_name='url_name',val_func_name='url_name'),
        # SearchOption(caption,False),
        SearchOption(menu,False),

    ]

    def permission_url(self, model_obj=None, is_header=False):
        if is_header:
            return "权限-URL"
        else:
            return "%s ---> %s"%(model_obj.caption,model_obj.url)

    list_display = [checkbox,'id',permission_url,'menu',option]
