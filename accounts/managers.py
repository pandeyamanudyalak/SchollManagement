from django.contrib.auth.models import BaseUserManager



class CustomUserManager(BaseUserManager):
    def create_user(self, college_id, user_id, financial_year, password=None):
        if not college_id:
            raise ValueError("College ID is required.")
        if not user_id:
            raise ValueError("User ID is required.")
        if not financial_year:
            raise ValueError("Financial Year is required.")

        user = self.model(
            college_id=college_id,
            user_id=user_id,
            financial_year=financial_year,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, college_id, user_id, financial_year, password=None):
        user = self.create_user(college_id, user_id, financial_year, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user