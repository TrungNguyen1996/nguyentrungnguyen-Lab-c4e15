
from gmail import GMail, Message
from random import choice


# gmail = GMail('nguyentrungnguyenth18@gmail.com','OHOHOHt804')
# msg = Message('Chao anh',to = 'C4E.201708@Gmail.COM',text='anh beo')
# gmail.send(msg)

# html_template = '''
# <p>Em ch&agrave;o anh Huy b&eacute;o!</p>
# <h2><strong>Hum nay b&agrave;i<span style="text-decoration: underline; color: #ff0000;"> kh&oacute; lắm </span><em>anh gi&uacute;p em học nh&eacute;</em>&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-kiss.gif" alt="kiss" /></strong></h2>
# <p><strong>love anh!</strong></p>
# '''

html_template = '''
<p>Đơn xin nghỉ ốm</p>
<p>H&ocirc;m nay em xin nghỉ ốm v&igrave; em bị {{ly_do_nghi}}</p>
'''

tat_ca_ly_do = ['dau dau', 'dau bung', 'ny em om']

ly_do = choice(tat_ca_ly_do)

html_content = html_template.replace('{{ly_do_nghi}}', ly_do)

gmail = GMail('nguyentrungnguyenth18@gmail.com','OHOHOHt804')
msg = Message('Chao anh',to = 'C4E.201708@Gmail.COM',html=html_content)
gmail.send(msg)
