from django.contrib.auth.models import User
from relationship_app.models import UserProfile

# Create users if they don’t already exist
def create_user_if_not_exists(username, password):
    user, created = User.objects.get_or_create(username=username)
    if created:
        user.set_password(password)
        user.save()
        print(f"Created: {username}")
    else:
        print(f"Already exists: {username}")
    return user

# Create users
u1 = create_user_if_not_exists('admin1', 'pass1234')
u2 = create_user_if_not_exists('librarian1', 'pass1234')
u3 = create_user_if_not_exists('member1', 'pass1234')

# Assign roles
u1.profile.role = 'Admin'
u1.profile.save()

u2.profile.role = 'Librarian'
u2.profile.save()

u3.profile.role = 'Member'
u3.profile.save()

print("Roles successfully assigned!")
