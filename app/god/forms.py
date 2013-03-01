from flask.ext.wtf import Form, TextField, PasswordField, BooleanField, RecaptchaField
from flask.ext.wtf import Required, Email, EqualTo

class LoginForm(Form):
	user_id = TextField('ID', [Required()])
	password = PasswordField('Password', [Required()])
