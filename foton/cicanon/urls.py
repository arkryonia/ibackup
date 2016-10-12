# ----------------------------------------------------------------------------
# Stdlib imports
# ----------------------------------------------------------------------------
from __future__ import absolute_import



# ============================================================================




# ----------------------------------------------------------------------------
# Core Django imports
# ----------------------------------------------------------------------------

from django.conf.urls import url


# ============================================================================




# ----------------------------------------------------------------------------
# Third-party app imports
# ----------------------------------------------------------------------------




# ============================================================================




# ----------------------------------------------------------------------------
# Imports from our apps
# ----------------------------------------------------------------------------

from . import views
from . import feeds


# ============================================================================


urlpatterns = [


	# Categories URLs
	url(

		regex=r"^categories/$",
		view=views.CategoryListView.as_view(),
		name="list-cats"
	),

	url(

		regex=r"^categories/list/$",
		view=views.CategoryPublicListView.as_view(),
		name="public-list-cats"
	),

	url(
		regex=r"^categories/create/",
		view=views.CategoryCreateView.as_view(),
		name="create-cat"
	),

	url(
		regex=r"^categories/(?P<slug>[-\w]+)/update/$",
		view=views.CategoryUpdateView.as_view(),
		name='update-cat'
	),

	url(
		regex=r"^categories/(?P<slug>[-\w]+)/posts/$",
		view=views.CatPostListView.as_view(),
		name='cat-post-list'
	),


	# Posts URLs

	url(
		regex=r"^posts/$",
		view=views.PostListView.as_view(),
		name="list-posts"
	),

	url(
		regex=r"^$",
		view=views.PostPublicListView.as_view(),
		name="public-list-posts"
	),

	url(
		regex=r"^posts/create/$",
		view=views.PostCreateView.as_view(),
		name="create-post"
	),

	url(
		regex=r"^posts/(?P<slug>[-\w]+)/$",
		view=views.PostDetailView.as_view(),
		name="detail-post"
	),

	url(

		regex=r"^posts/(?P<slug>[-\w]+)/detail/$",
		view=views.PostPublicDetailView.as_view(),
		name="public-detail-post"
	),

	url(

		regex=r"^posts/(?P<slug>[-\w]+)/update/$",
		view=views.PostUpdateView.as_view(),
		name="update-post"
	),

	url(
		regex=r"^posts/(?P<pk>[-\w]+)/pub/$",
		view=views.pub_post,
		name="pub-post"
	),

	url(
		regex=r"^posts/feeds/$",
		view=feeds.LastestPost(),
		name="feeds"
	),

]
