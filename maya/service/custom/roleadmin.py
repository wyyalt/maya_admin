from maya.service import admin


class RoleAdmin(admin.BaseMayaModel):

    from maya.service.custom.common import option
    from maya.service.custom.common import checkbox

    list_display = [checkbox,'caption',option]