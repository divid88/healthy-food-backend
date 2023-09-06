from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, mobile_number, password=None, **extra_fields):
        if not mobile_number:
            raise ValueError("User must have mobile_number address.")
        if not username:
            raise ValueError("User must have username.")
        user = self.model(
            mobile_number=mobile_number,
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)

    def create_superuser(self, username, mobile_number, password=None, **extra_fields):
        super_user = self.create_user(
            username=username,
            mobile_number=mobile_number,
            password=password
        )
        super_user.is_admin = True
        super_user.is_active = True
        super_user.is_staff = True
        super_user.is_superuser = True
        super_user.save(using=self._db)

        return super_user