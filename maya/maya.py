
from maya import models
from maya.service import admin
from maya.service.custom.roleadmin import RoleAdmin
from maya.service.custom.permissionadmin import PermissionAdmin


class UserAdmin(admin.BaseMayaModel):
    pass

admin.site.register(models.User,UserAdmin)
admin.site.register(models.Role,RoleAdmin)
admin.site.register(models.Permission,PermissionAdmin)

class MenuAdmin(admin.BaseMayaModel):
    pass

admin.site.register(models.Menu,MenuAdmin)

