from .component import Component

class Head(Component):
    def __init__(self, template, name, title, email, phone, address,
                 github_link, github_account, linkedin_link,
                 linkedin_account, twitter_handle, twitter_link):
        super().__init__(template)

        self.params = {
            'name': name,
            'title': title,
            'email': email,
            'phone': phone,
            'address': address,
            'github_link': github_link,
            'github_account': github_account,
            'linkedin_link': linkedin_link,
            'linkedin_account': linkedin_account,
            'twitter_link': twitter_link,
            'twitter_handle': twitter_handle
        }
