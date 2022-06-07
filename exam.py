from pywebio.input import *
from pywebio.output import *
from flask import Flask
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH


app = Flask(__name__)



def exam():
	c = 0

	name = input("Enter your name to start the exam", type="text")

	q1 = radio("Which is not a programming language?",["Python","Java","HTML","C++"])
	if q1 == "HTML":
		c+=1

	q2 = radio("Base language for websites?",["Python","Java","HTML","C++"])
	if q2 == "HTML":
		c+=1

	q3 = radio("Secondary memory is also called....?",["RAM","Virtual Memory","VRAM","ROM"])
	if q3 == "ROM":
		c+=1

	q4 = radio("Can we create web appliations with C++?",["Yes","No"])
	if q4 == "Yes":
		c+=1

	q5 = radio("Which is not a framework?",["Vue","Angular","Flask","JavaScript"])
	if q5 == "JavaScript":
		c+=1

	if c>3:
		put_text(name +", your score is "+ str(c))
		style(put_text("Result : Passed"),"color:green")
	else:
		put_text(name +", your score is "+ str(c))
		style(put_text("Result : Failed"),"color:red")

	put_text("Thank you for your participation..")


app.add_url_rule('/','webio_view', webio_view(exam),methods=['GET','POST','OPTIONS'])
app.run(host='localhost', port=5000)


