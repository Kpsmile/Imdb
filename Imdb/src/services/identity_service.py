class IdentityService(object):
    def __init__(self, operations):
        self.operations = operations

    def get_user_role(self, token):
        """

        :param token:
        :return:
        """
        user_role= self.operations.get_user_role(username = token)
        return user_role.role_type
