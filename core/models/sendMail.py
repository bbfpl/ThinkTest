import smtplib,os
from jinja2 import Template
from email.mime.text import MIMEText
# from email.header import Header
from config import Config
from tool import Tool
class SendMail():
    def __init__(self):
        # 发送人邮箱
        self.email_smtp = Config.get_config('emailSmtp')
        # 发送人邮箱
        self.email_sender = Config.get_config('emailSender')
        # 发送人邮箱授权码
        self.email_passwd = Config.get_config('emailPasswd')
        # 收件人邮箱
        self.email_receivers = Config.get_config('emailReceivers')
        # 收件人邮箱
        self.email_subject = Config.get_config('emailSubject')
        # 邮件html模板
        self.email_tpl = Config.get_config('emailTpl')

    def send(self,subject='发邮Html邮件测试',content=""):
        # subject 主题
        # content 内容
        msg = MIMEText(content,'html','utf-8')
        msg['Subject'] = subject
        msg['From'] = self.email_sender
        msg['To'] = self.email_receivers
        try:
            s = smtplib.SMTP_SSL(self.email_smtp,465)
            s.login(self.email_sender,self.email_passwd)
            s.sendmail(self.email_sender,self.email_receivers,msg.as_string())
            print('发送成功')
        except:
            print('发送失败')

    def run(self,data={}):
        # 获取mail_html路径
        if self.email_tpl == 'default':
            html_path = os.path.dirname(__file__) + '/mailTpl/mail_html.txt'
        else:
            html_path = self.email_tpl
        # print(html_path)
        # 基础模板文件
        html_code = Tool().open_file(html_path)
        # 数据
        data['title'] = self.email_subject
        html = Template(html_code).render(data)
        # print(html)
        # 发送邮件
        self.send(self.email_subject,html)

if __name__ == '__main__':
    SendMail().run()