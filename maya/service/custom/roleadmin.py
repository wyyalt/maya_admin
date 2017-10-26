from maya.service import admin


class RoleAdmin(admin.BaseMayaModel):

    from maya.service.custom.common import option

    list_display = ['caption',option]