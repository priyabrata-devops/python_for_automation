from user import User
from post import Post
app_user_name = User("priyabrata@gmail.com", "Priyabrata Sahoo", "Pinku@021,", "DevOps Engineer")
app_user_name.get_user_info()

app_user_name.change_job_title("DevOps Trainer")
app_user_name.get_user_info()

new_post = Post("On a secret mission today", app_user_name.name)
new_post.get_post_info()