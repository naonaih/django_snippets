from django.urls import path

from snippets import views

urlpatterns = [
	path("new/", views.snippets_new, name="snippet_new"),
	path("<int:snippet_id>/", views.snippets_detail, name="snippet_detail"),
	path("<int:snippet_id>/edit/", views.snippets_edit, name="snippet_edit"),
]

