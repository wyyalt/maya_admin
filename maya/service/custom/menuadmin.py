from maya.service import admin


class MenuAdmin(admin.BaseMayaModel):

    from maya.service.custom.common import option
    from maya.service.custom.common import checkbox

    list_display = [checkbox,'caption','parent',option]