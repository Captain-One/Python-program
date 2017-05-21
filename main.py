import cgi
form1 = cgi.FieldStorage()
name = form1.getvalue("name")
print('Content-type:text/html \n\n')
print('hello web')+name