
from maya import models
from maya.service import admin
from maya.service.custom.roleadmin import RoleAdmin
from maya.service.custom.permissionadmin import PermissionAdmin
from maya.service.custom.useradmin import UserAdmin
from maya.service.custom.menuadmin import MenuAdmin


admin.site.register(models.User,UserAdmin)
admin.site.register(models.Role,RoleAdmin)
admin.site.register(models.Permission,PermissionAdmin)
admin.site.register(models.Menu,MenuAdmin)

