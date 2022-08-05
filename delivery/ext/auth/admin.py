from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import Model


class UserAdmin(ModelView):
    """Interface Admin para usuários"""
    