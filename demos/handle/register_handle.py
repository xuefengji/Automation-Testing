from demos.page.register_page import RegisterPage
class RegisterHandle(object):
    def __init__(self):
        self.register_p = RegisterPage()
    #输入邮箱
    def send_user_email(self,email):
        self.register_p.get_user_mail().send_keys(email)

    #输入用户名
    def send_user_name(self,username):
        self.register_p.get_user_name().send_keys(username)

    #输入密码
    def send_user_pwd(self,password):
        self.register_p.get_user_password().send_keys(password)


    #输入验证码
    def send_user_code(self,code):
        self.register_p.get_user_code().send_keys(code)