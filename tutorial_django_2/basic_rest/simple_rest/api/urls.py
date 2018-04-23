from django.urls import path

from .views import CreateApiView, RudApiView, ListApiView, RetrieveApiView

app_name="rest"
urlpatterns = [
    path('/create/', CreateApiView.as_view(), name="create"),
    path('/list/', ListApiView.as_view(), name="list"),
    path('/update_delete/<int:pk>', RudApiView.as_view(), name="update-delete"),
    path('/specific_blog/<int:pk>', RetrieveApiView.as_view(), name="retrieve"),
]