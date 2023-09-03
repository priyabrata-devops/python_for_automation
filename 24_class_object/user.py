class User:
    def __init__(self, email_id, full_name, current_password, job_title):
        self.email = email_id
        self.name = full_name
        self.password = current_password
        self.current_job_title = job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name}, currently work as a {self.current_job_title}. You can contact them at {self.email}")