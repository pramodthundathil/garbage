from django.urls import path 
from .import views

urlpatterns = [
    path("request_collection",views.request_collection, name="request_collection"),
    path("history",views.history, name="history"),
    path("my_requests",views.my_requests, name="my_requests"),
    path("add_items_to_request/<int:pk>",views.add_items_to_request, name="add_items_to_request"),
    path("delete_garbage_from_request/<int:pk>",views.delete_garbage_from_request, name="delete_garbage_from_request"),
 
    path("collection_requests_admin",views.collection_requests_admin, name="collection_requests_admin"),
    path("view_collection_request_single/<int:pk>",views.view_collection_request_single, name="view_collection_request_single"),
    path("assign_driver/<int:pk>",views.assign_driver, name="assign_driver"),
    path("vault_admin", views.vault_admin,name="vault_admin"),

    path("driver_collection_requests",views.driver_collection_requests, name="driver_collection_requests"),
    path("mark_collection_in_progress/<int:pk>",views.mark_collection_in_progress, name="mark_collection_in_progress"),
    path("mark_collection_collected/<int:pk>", views.mark_collection_collected, name="mark_collection_collected"),
    path("driver_collected_garbages",views.driver_collected_garbages, name="driver_collected_garbages"),
    # urls.py
    path('garbage_request/<int:pk>/send_to_vault/', views.send_to_vault, name='send_to_vault'),


    path("collection_requests_staff",views.collection_requests_staff, name="collection_requests_staff"),
    path("view_collection_request_single_staff/<int:pk>",views.view_collection_request_single_staff, name="view_collection_request_single_staff"),
    path("assign_driver_staff/<int:pk>",views.assign_driver_staff, name="assign_driver_staff"),






]