from rest_framework.permissions import BasePermission



class IsCustomerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["HEAD", "OPTIONS", "GET"]:
            return True
        return obj.customer == request.user


class CanViewStatisticsPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm("store_app.can_view_statistics")
