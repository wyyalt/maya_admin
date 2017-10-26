from django.http.request import QueryDict
from django.urls import reverse
from django.utils.safestring import mark_safe

def option(self, model_obj=None, is_header=False):
    """
    自定义操作按钮
    :param model_obj:
    :return:
    """
    if is_header:
        return "操作"
    else:
        # reverse url
        base_edit_url = reverse("{0}:{1}_{2}_change".format(
            self.site.namespace,
            self.model_class._meta.app_label,
            self.model_class._meta.model_name
        ),
            args=(model_obj.pk,)
        )
        base_del_url = reverse("{0}:{1}_{2}_delete".format(
            self.site.namespace,
            self.model_class._meta.app_label,
            self.model_class._meta.model_name
        ),
            args=(model_obj.pk,)
        )

        base_detail_url = reverse("{0}:{1}_{2}_detail".format(
            self.site.namespace,
            self.model_class._meta.app_label,
            self.model_class._meta.model_name
        ),
            args=(model_obj.pk,)
        )

        param_dict = QueryDict(mutable=True)
        param_dict['_change_filter'] = self.request.GET.urlencode()

        edit_url = "{0}?{1}".format(base_edit_url, param_dict.urlencode())
        del_url = "{0}?{1}".format(base_del_url, param_dict.urlencode())
        detail_url = "{0}?{1}".format(base_detail_url, param_dict.urlencode())

        option = """
        <a href='{0}'><span style="margin-right:3px" class="glyphicon glyphicon-edit" aria-hidden="true"></span>编辑</a> 
        <a href='{1}'><span style="margin-right:3px" class="glyphicon glyphicon-remove" aria-hidden="true"></span>删除</a> 
        <a href='{2}'><span style="margin-right:5px" class="glyphicon glyphicon-folder-open" aria-hidden="true"></span>查看详细</a> 
        """.format(edit_url, del_url, detail_url)

        return mark_safe(option)

def checkbox(self, model_obj=None, is_header=False):
    if is_header:
        return mark_safe("<input id='check_all' type='checkbox'>")
    else:
        return mark_safe("<input name='pk' type='checkbox' value='{0}'>".format(model_obj.pk))