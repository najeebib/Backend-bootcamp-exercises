class User:
    """ class that represents a user in a social media platform """
    def __init__(self, username):
        """ initilize a user object with a username 
        
        :param username: the user's username
        """
        self.username = username
        self.following = []
    # time complexity: O(n)
    def follow(self, other_user):
        """ follow another user 
        
        :param other_user: the user to follow
        """
        if other_user not in self.following:
            self.following.append(other_user)
    # time complexity: O(1)
    def post_message(self, message):
        """
        Post a message.
        
        Parameters:
        :param message: The message to be posted.
        
        Returns: a dictionary representing the posted message with the username and message content.
        """

        post = {'username': self.username, 'message': message}
        return post