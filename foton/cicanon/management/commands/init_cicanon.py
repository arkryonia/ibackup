# ----------------------------------------------------------------------------
# Stdlib imports
# ----------------------------------------------------------------------------
from __future__ import absolute_import



# ============================================================================




# ----------------------------------------------------------------------------
# Core Django imports
# ----------------------------------------------------------------------------

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Group

# ============================================================================




# ----------------------------------------------------------------------------
# Third-party app imports
# ----------------------------------------------------------------------------




# ============================================================================




# ----------------------------------------------------------------------------
# Imports from our apps
# ----------------------------------------------------------------------------




# ============================================================================



class Command(BaseCommand):
	def handle(self, *args, **options):
		content_type = ContentType.objects.get_for_model(User)

		# Create "Is Author permission"
		author = Permission.objects.create(
					codename='is_author',
                    name='Is Author',
                    content_type=content_type
         		)

		# Create author group
		group = Group.objects.create(name="author")

		# Add "auth.is_author" permission to author group
		group.permissions.add(author, )


		# Create "auth.is_editor" permission
		editor = Permission.objects.create(
					codename='is_editor',
                    name='Is Editor',
                    content_type=content_type
                )

		# Create "editor" group
		group = Group.objects.create(name="editor")

		# Add "auth.is_editor" and "auth.is_author" permission to editor group
		group.permissions.add(author, editor,)

		# Create an editor
		u = User.objects.create_user(username='editor', password='pass')
		u.groups.add(group)
