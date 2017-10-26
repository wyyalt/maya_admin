from maya import models
from maya.service import admin
from maya.service.admin import SearchOption


class UserAdmin(admin.BaseMayaModel):
    #option函数
    from maya.service.custom.common import option

    from maya.service.custom.common import checkbox



    list_display = [checkbox,'username','email',option]