from core.Management.Attributes.setters.Credentials.SetLoginCredentials import SetLoginCredentials


class GetLoginCredentials(SetLoginCredentials):
    def __init__(self):
        super(GetLoginCredentials).__init__()

    def get_credentials(self):
        return self.set_credentials
