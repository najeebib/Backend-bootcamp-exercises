from .user import User
class SocialMediaPlatform:
    """ class that represents a social media platform """
    def __init__(self):
        """ initlize the social media platform object """
        self.users = []
        self.posts = []
    # time complexity: O(n) * O(1) = O(n)
    def register_user(self, username):
        """ register a user if the username is unique 
        
        :param username: the user name to be registered
        """
        # time complexity: O(n)
        if not self._is_username_taken(username):
            user = User(username)
            self.users.append(user)
    # time complexity: O(n)
    def _is_username_taken(self, username):
        """ check if a user exists with the given name 
        
        :param username: the user name we want to check

        return: a boolean value if the user is in or not
        """
        for user in self.users:
            if user.username == username:
                return True
        return False
    # time complexity: O(n)
    def get_user_by_username(self, username):
        """ search the users list for a user with same name and returns the user object

        :param username: name of user we want to search for

        return: user object if it was fount else return none 
        """
        for user in self.users:
            if user.username == username:
                return user
        return None
    # time complexity: O(n)
    def add_post(self, post):
        """ add a post to the posts list

        : param post: a dictionary that will have the name of user and the message  
        """
        self.posts.append(post)
    # time complexity: O(n^2)
    def generate_timeline(self, username):
        """ generate the timeline of posts for a given user.

        
        :param username: name of user we want to generate the timeline for

        Returns: a list of posts in the timeline.
        """
        user = self.get_user_by_username(username)
        if not user:
            return []

        timeline = []
        for followed_user in user.following:
            for post in self.posts:
                if post['username'] == followed_user:
                    timeline.append(post)
        return timeline
