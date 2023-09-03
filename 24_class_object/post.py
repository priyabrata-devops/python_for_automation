class Post:
    def __init__(self, quoted_message, author_name):
        self.message = quoted_message
        self.author = author_name
    
    def get_post_info(self):
        print(f"Post: {self.message} written by {self.author}")
    