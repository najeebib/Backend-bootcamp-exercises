from .user import User
class ImprovedSocialMediaPlatform:
    """ class that represents a social media platform """
    def __init__(self):
        """ initlize the social media platform object """
        self.users = {}
        self.posts = []
    # time complexity: O(1)
    def register_user(self, username):
        """ register a user if the username is unique 
        
        :param username: the user name to be registered
        """
        # time complexity: O(1)
        if username not in self.users:
            user = User(username)
            self.users[username] = user

    # time complexity: O(1)
    def get_user_by_username(self, username):
        """ search the users list for a user with same name and returns the user object

        :param username: name of user we want to search for

        return: user object if it was fount else return none 
        """
        return self.users.get(username, None)
    # time complexity: O(n)
    def add_post(self, post):
        """ add a post to the posts list

        : param post: a dictionary that will have the name of user and the message  
        """
        self.posts.append(post)
    # time complexity: O(n)
    def generate_timeline(self, username):
        """ generate the timeline of posts for a given user.

        
        :param username: name of user we want to generate the timeline for

        Returns: a list of posts in the timeline.
        """
        user = self.get_user_by_username(username)
        if not user:
            return []
        # we improved the time complexity here by checking if the post username is in the user's following
        # instead of going through all users and checking if the user follows them or not
        timeline = []
        for post in self.posts:
            if post['username'] in user.following:
                timeline.append(post)
        return timeline
