from rest_framework import permissions


class IsStaffPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if not request.user.is_staff:
            return False
        return super().has_permission(request, view)
    #permet de bloquer l'accès à la création quand acces à liste uniquement
    # il faut ajouter '%(app_label)s.view_%(model_name)s' dans GET pour bloquer l'accès en lecture
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        #'GET':[],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }