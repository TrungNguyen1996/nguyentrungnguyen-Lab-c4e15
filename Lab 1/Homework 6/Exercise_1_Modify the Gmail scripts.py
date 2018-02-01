# Serious exercises
# Exercise 1:
# Modify the Gmail scripts (im_sick.py) so that it will send your call-in-sick email only once after 7AM.

# Bài tập 1:
# Sửa đổi các tập lệnh Gmail (im_sick.py) để nó gửi email, chỉ gửi thư nghỉ ốm 1 lần sau 7 giờ sáng.

from gmail import GMail, Message
html_content = '''
<p><strong>Anh <span style="text-decoration: underline;">th&acirc;n</span> <em>mến</em></strong></p>
<p><span style="color: #008000; background-color: #993366;"><span style="background-color: #800000;"><strong>Gởi anh Huy &uacute;</strong></span></span><span style="color: #008000;">,</span> anh ơi v&agrave;o chiều nay <span style="background-color: #0000ff;">01/02/2018</span> em c&oacute; đi học tr&ecirc;n trường một ch&uacute;t, mong l&agrave; tự về được sớm th&igrave; qua ngồi vs anh ạ, nếu em về muộn qu&aacute; th&igrave; em về ăn cơm trước r&ugrave;i qua nest lu&ocirc;n anh nh&eacute;&nbsp;</p>
<p>Thử gửi ng&agrave;y 13h05&nbsp; 01/02/2018!</p>
'''
gmail = GMail("nguyentrungnguyenth18@gmail.com", "OHOHOHt804")  # gmail của bản thân
msg = Message("Xin nghỉ ốm", to="nguyentrungnguyenth18@gmail.com", html=html_content)
# huynq.work@gamil.com
gmail.send(msg)
