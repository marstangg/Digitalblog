{"filter":false,"title":"forms.py","tooltip":"/flaskblog/forms.py","undoManager":{"mark":9,"position":9,"stack":[[{"start":{"row":0,"column":0},"end":{"row":21,"column":33},"action":"remove","lines":["from flask_wtf import FlaskForm","from wtforms import StringField, PasswordField, SubmitField, BooleanField","from wtforms.validators import DataRequired, Length, Email, EqualTo","","","class RegistrationForm(FlaskForm):","    username = StringField('Username',","                           validators=[DataRequired(), Length(min=2, max=20)])","    email = StringField('Email',","                        validators=[DataRequired(), Email()])","    password = PasswordField('Password', validators=[DataRequired()])","    confirm_password = PasswordField('Confirm Password',","                                     validators=[DataRequired(), EqualTo('password')])","    submit = SubmitField('Sign Up')","","","class LoginForm(FlaskForm):","    email = StringField('Email',","                        validators=[DataRequired(), Email()])","    password = PasswordField('Password', validators=[DataRequired()])","    remember = BooleanField('Remember Me')","    submit = SubmitField('Login')"],"id":4}],[{"start":{"row":0,"column":0},"end":{"row":21,"column":33},"action":"insert","lines":["from flask_wtf import FlaskForm","from wtforms import StringField, PasswordField, SubmitField, BooleanField","from wtforms.validators import DataRequired, Length, Email, EqualTo","","","class RegistrationForm(FlaskForm):","    username = StringField('Username',","                           validators=[DataRequired(), Length(min=2, max=20)])","    email = StringField('Email',","                        validators=[DataRequired(), Email()])","    password = PasswordField('Password', validators=[DataRequired()])","    confirm_password = PasswordField('Confirm Password',","                                     validators=[DataRequired(), EqualTo('password')])","    submit = SubmitField('Sign Up')","","","class LoginForm(FlaskForm):","    email = StringField('Email',","                        validators=[DataRequired(), Email()])","    password = PasswordField('Password', validators=[DataRequired()])","    remember = BooleanField('Remember Me')","    submit = SubmitField('Login')"],"id":5}],[{"start":{"row":0,"column":0},"end":{"row":21,"column":33},"action":"remove","lines":["from flask_wtf import FlaskForm","from wtforms import StringField, PasswordField, SubmitField, BooleanField","from wtforms.validators import DataRequired, Length, Email, EqualTo","","","class RegistrationForm(FlaskForm):","    username = StringField('Username',","                           validators=[DataRequired(), Length(min=2, max=20)])","    email = StringField('Email',","                        validators=[DataRequired(), Email()])","    password = PasswordField('Password', validators=[DataRequired()])","    confirm_password = PasswordField('Confirm Password',","                                     validators=[DataRequired(), EqualTo('password')])","    submit = SubmitField('Sign Up')","","","class LoginForm(FlaskForm):","    email = StringField('Email',","                        validators=[DataRequired(), Email()])","    password = PasswordField('Password', validators=[DataRequired()])","    remember = BooleanField('Remember Me')","    submit = SubmitField('Login')"],"id":6}],[{"start":{"row":0,"column":0},"end":{"row":32,"column":33},"action":"insert","lines":["from flask_wtf import FlaskForm","from wtforms import StringField, PasswordField, SubmitField, BooleanField","from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError","from flaskblog.models import User","","","class RegistrationForm(FlaskForm):","    username = StringField('Username',","                           validators=[DataRequired(), Length(min=2, max=20)])","    email = StringField('Email',","                        validators=[DataRequired(), Email()])","    password = PasswordField('Password', validators=[DataRequired()])","    confirm_password = PasswordField('Confirm Password',","                                     validators=[DataRequired(), EqualTo('password')])","    submit = SubmitField('Sign Up')","","    def validate_username(self, username):","        user = User.query.filter_by(username=username.data).first()","        if user:","            raise ValidationError('That username is taken. Please choose a different one.')","","    def validate_email(self, email):","        user = User.query.filter_by(email=email.data).first()","        if user:","            raise ValidationError('That email is taken. Please choose a different one.')","","","class LoginForm(FlaskForm):","    email = StringField('Email',","                        validators=[DataRequired(), Email()])","    password = PasswordField('Password', validators=[DataRequired()])","    remember = BooleanField('Remember Me')","    submit = SubmitField('Login')"],"id":7}],[{"start":{"row":0,"column":0},"end":{"row":32,"column":33},"action":"remove","lines":["from flask_wtf import FlaskForm","from wtforms import StringField, PasswordField, SubmitField, BooleanField","from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError","from flaskblog.models import User","","","class RegistrationForm(FlaskForm):","    username = StringField('Username',","                           validators=[DataRequired(), Length(min=2, max=20)])","    email = StringField('Email',","                        validators=[DataRequired(), Email()])","    password = PasswordField('Password', validators=[DataRequired()])","    confirm_password = PasswordField('Confirm Password',","                                     validators=[DataRequired(), EqualTo('password')])","    submit = SubmitField('Sign Up')","","    def validate_username(self, username):","        user = User.query.filter_by(username=username.data).first()","        if user:","            raise ValidationError('That username is taken. Please choose a different one.')","","    def validate_email(self, email):","        user = User.query.filter_by(email=email.data).first()","        if user:","            raise ValidationError('That email is taken. Please choose a different one.')","","","class LoginForm(FlaskForm):","    email = StringField('Email',","                        validators=[DataRequired(), Email()])","    password = PasswordField('Password', validators=[DataRequired()])","    remember = BooleanField('Remember Me')","    submit = SubmitField('Login')"],"id":8},{"start":{"row":0,"column":0},"end":{"row":55,"column":92},"action":"insert","lines":["from flask_wtf import FlaskForm","from flask_wtf.file import FileField, FileAllowed","from flask_login import current_user","from wtforms import StringField, PasswordField, SubmitField, BooleanField","from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError","from flaskblog.models import User","","","class RegistrationForm(FlaskForm):","    username = StringField('Username',","                           validators=[DataRequired(), Length(min=2, max=20)])","    email = StringField('Email',","                        validators=[DataRequired(), Email()])","    password = PasswordField('Password', validators=[DataRequired()])","    confirm_password = PasswordField('Confirm Password',","                                     validators=[DataRequired(), EqualTo('password')])","    submit = SubmitField('Sign Up')","","    def validate_username(self, username):","        user = User.query.filter_by(username=username.data).first()","        if user:","            raise ValidationError('That username is taken. Please choose a different one.')","","    def validate_email(self, email):","        user = User.query.filter_by(email=email.data).first()","        if user:","            raise ValidationError('That email is taken. Please choose a different one.')","","","class LoginForm(FlaskForm):","    email = StringField('Email',","                        validators=[DataRequired(), Email()])","    password = PasswordField('Password', validators=[DataRequired()])","    remember = BooleanField('Remember Me')","    submit = SubmitField('Login')","","","class UpdateAccountForm(FlaskForm):","    username = StringField('Username',","                           validators=[DataRequired(), Length(min=2, max=20)])","    email = StringField('Email',","                        validators=[DataRequired(), Email()])","    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])","    submit = SubmitField('Update')","","    def validate_username(self, username):","        if username.data != current_user.username:","            user = User.query.filter_by(username=username.data).first()","            if user:","                raise ValidationError('That username is taken. Please choose a different one.')","","    def validate_email(self, email):","        if email.data != current_user.email:","            user = User.query.filter_by(email=email.data).first()","            if user:","                raise ValidationError('That email is taken. Please choose a different one.')"]}],[{"start":{"row":0,"column":0},"end":{"row":55,"column":92},"action":"remove","lines":["from flask_wtf import FlaskForm","from flask_wtf.file import FileField, FileAllowed","from flask_login import current_user","from wtforms import StringField, PasswordField, SubmitField, BooleanField","from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError","from flaskblog.models import User","","","class RegistrationForm(FlaskForm):","    username = StringField('Username',","                           validators=[DataRequired(), Length(min=2, max=20)])","    email = StringField('Email',","                        validators=[DataRequired(), Email()])","    password = PasswordField('Password', validators=[DataRequired()])","    confirm_password = PasswordField('Confirm Password',","                                     validators=[DataRequired(), EqualTo('password')])","    submit = SubmitField('Sign Up')","","    def validate_username(self, username):","        user = User.query.filter_by(username=username.data).first()","        if user:","            raise ValidationError('That username is taken. Please choose a different one.')","","    def validate_email(self, email):","        user = User.query.filter_by(email=email.data).first()","        if user:","            raise ValidationError('That email is taken. Please choose a different one.')","","","class LoginForm(FlaskForm):","    email = StringField('Email',","                        validators=[DataRequired(), Email()])","    password = PasswordField('Password', validators=[DataRequired()])","    remember = BooleanField('Remember Me')","    submit = SubmitField('Login')","","","class UpdateAccountForm(FlaskForm):","    username = StringField('Username',","                           validators=[DataRequired(), Length(min=2, max=20)])","    email = StringField('Email',","                        validators=[DataRequired(), Email()])","    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])","    submit = SubmitField('Update')","","    def validate_username(self, username):","        if username.data != current_user.username:","            user = User.query.filter_by(username=username.data).first()","            if user:","                raise ValidationError('That username is taken. Please choose a different one.')","","    def validate_email(self, email):","        if email.data != current_user.email:","            user = User.query.filter_by(email=email.data).first()","            if user:","                raise ValidationError('That email is taken. Please choose a different one.')"],"id":9},{"start":{"row":0,"column":0},"end":{"row":55,"column":92},"action":"insert","lines":["from flask_wtf import FlaskForm","from flask_wtf.file import FileField, FileAllowed","from flask_login import current_user","from wtforms import StringField, PasswordField, SubmitField, BooleanField","from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError","from flaskblog.models import User","","","class RegistrationForm(FlaskForm):","    username = StringField('Username',","                           validators=[DataRequired(), Length(min=2, max=20)])","    email = StringField('Email',","                        validators=[DataRequired(), Email()])","    password = PasswordField('Password', validators=[DataRequired()])","    confirm_password = PasswordField('Confirm Password',","                                     validators=[DataRequired(), EqualTo('password')])","    submit = SubmitField('Sign Up')","","    def validate_username(self, username):","        user = User.query.filter_by(username=username.data).first()","        if user:","            raise ValidationError('That username is taken. Please choose a different one.')","","    def validate_email(self, email):","        user = User.query.filter_by(email=email.data).first()","        if user:","            raise ValidationError('That email is taken. Please choose a different one.')","","","class LoginForm(FlaskForm):","    email = StringField('Email',","                        validators=[DataRequired(), Email()])","    password = PasswordField('Password', validators=[DataRequired()])","    remember = BooleanField('Remember Me')","    submit = SubmitField('Login')","","","class UpdateAccountForm(FlaskForm):","    username = StringField('Username',","                           validators=[DataRequired(), Length(min=2, max=20)])","    email = StringField('Email',","                        validators=[DataRequired(), Email()])","    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])","    submit = SubmitField('Update')","","    def validate_username(self, username):","        if username.data != current_user.username:","            user = User.query.filter_by(username=username.data).first()","            if user:","                raise ValidationError('That username is taken. Please choose a different one.')","","    def validate_email(self, email):","        if email.data != current_user.email:","            user = User.query.filter_by(email=email.data).first()","            if user:","                raise ValidationError('That email is taken. Please choose a different one.')"]}],[{"start":{"row":0,"column":0},"end":{"row":55,"column":92},"action":"remove","lines":["from flask_wtf import FlaskForm","from flask_wtf.file import FileField, FileAllowed","from flask_login import current_user","from wtforms import StringField, PasswordField, SubmitField, BooleanField","from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError","from flaskblog.models import User","","","class RegistrationForm(FlaskForm):","    username = StringField('Username',","                           validators=[DataRequired(), Length(min=2, max=20)])","    email = StringField('Email',","                        validators=[DataRequired(), Email()])","    password = PasswordField('Password', validators=[DataRequired()])","    confirm_password = PasswordField('Confirm Password',","                                     validators=[DataRequired(), EqualTo('password')])","    submit = SubmitField('Sign Up')","","    def validate_username(self, username):","        user = User.query.filter_by(username=username.data).first()","        if user:","            raise ValidationError('That username is taken. Please choose a different one.')","","    def validate_email(self, email):","        user = User.query.filter_by(email=email.data).first()","        if user:","            raise ValidationError('That email is taken. Please choose a different one.')","","","class LoginForm(FlaskForm):","    email = StringField('Email',","                        validators=[DataRequired(), Email()])","    password = PasswordField('Password', validators=[DataRequired()])","    remember = BooleanField('Remember Me')","    submit = SubmitField('Login')","","","class UpdateAccountForm(FlaskForm):","    username = StringField('Username',","                           validators=[DataRequired(), Length(min=2, max=20)])","    email = StringField('Email',","                        validators=[DataRequired(), Email()])","    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])","    submit = SubmitField('Update')","","    def validate_username(self, username):","        if username.data != current_user.username:","            user = User.query.filter_by(username=username.data).first()","            if user:","                raise ValidationError('That username is taken. Please choose a different one.')","","    def validate_email(self, email):","        if email.data != current_user.email:","            user = User.query.filter_by(email=email.data).first()","            if user:","                raise ValidationError('That email is taken. Please choose a different one.')"],"id":10},{"start":{"row":0,"column":0},"end":{"row":32,"column":33},"action":"insert","lines":["from flask_wtf import FlaskForm","from wtforms import StringField, PasswordField, SubmitField, BooleanField","from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError","from flaskblog.models import User","","","class RegistrationForm(FlaskForm):","    username = StringField('Username',","                           validators=[DataRequired(), Length(min=2, max=20)])","    email = StringField('Email',","                        validators=[DataRequired(), Email()])","    password = PasswordField('Password', validators=[DataRequired()])","    confirm_password = PasswordField('Confirm Password',","                                     validators=[DataRequired(), EqualTo('password')])","    submit = SubmitField('Sign Up')","","    def validate_username(self, username):","        user = User.query.filter_by(username=username.data).first()","        if user:","            raise ValidationError('That username is taken. Please choose a different one.')","","    def validate_email(self, email):","        user = User.query.filter_by(email=email.data).first()","        if user:","            raise ValidationError('That email is taken. Please choose a different one.')","","","class LoginForm(FlaskForm):","    email = StringField('Email',","                        validators=[DataRequired(), Email()])","    password = PasswordField('Password', validators=[DataRequired()])","    remember = BooleanField('Remember Me')","    submit = SubmitField('Login')"]}],[{"start":{"row":29,"column":20},"end":{"row":29,"column":24},"action":"remove","lines":["    "],"id":11},{"start":{"row":29,"column":16},"end":{"row":29,"column":20},"action":"remove","lines":["    "]},{"start":{"row":29,"column":12},"end":{"row":29,"column":16},"action":"remove","lines":["    "]},{"start":{"row":29,"column":8},"end":{"row":29,"column":12},"action":"remove","lines":["    "]},{"start":{"row":29,"column":4},"end":{"row":29,"column":8},"action":"remove","lines":["    "]},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":29,"column":0},"end":{"row":29,"column":1},"action":"insert","lines":[" "],"id":12},{"start":{"row":29,"column":1},"end":{"row":29,"column":2},"action":"insert","lines":[" "]},{"start":{"row":29,"column":2},"end":{"row":29,"column":3},"action":"insert","lines":[" "]},{"start":{"row":29,"column":3},"end":{"row":29,"column":4},"action":"insert","lines":[" "]}],[{"start":{"row":0,"column":0},"end":{"row":32,"column":33},"action":"remove","lines":["from flask_wtf import FlaskForm","from wtforms import StringField, PasswordField, SubmitField, BooleanField","from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError","from flaskblog.models import User","","","class RegistrationForm(FlaskForm):","    username = StringField('Username',","                           validators=[DataRequired(), Length(min=2, max=20)])","    email = StringField('Email',","                        validators=[DataRequired(), Email()])","    password = PasswordField('Password', validators=[DataRequired()])","    confirm_password = PasswordField('Confirm Password',","                                     validators=[DataRequired(), EqualTo('password')])","    submit = SubmitField('Sign Up')","","    def validate_username(self, username):","        user = User.query.filter_by(username=username.data).first()","        if user:","            raise ValidationError('That username is taken. Please choose a different one.')","","    def validate_email(self, email):","        user = User.query.filter_by(email=email.data).first()","        if user:","            raise ValidationError('That email is taken. Please choose a different one.')","","","class LoginForm(FlaskForm):","    email = StringField('Email',","    validators=[DataRequired(), Email()])","    password = PasswordField('Password', validators=[DataRequired()])","    remember = BooleanField('Remember Me')","    submit = SubmitField('Login')"],"id":13},{"start":{"row":0,"column":0},"end":{"row":22,"column":0},"action":"insert","lines":["from flask_wtf import FlaskForm","from wtforms import StringField, PasswordField, SubmitField, BooleanField","from wtforms.validators import DataRequired, Length, Email, EqualTo","","","class RegistrationForm(FlaskForm):","    username = StringField('Username',","                           validators=[DataRequired(), Length(min=2, max=20)])","    email = StringField('Email',","                        validators=[DataRequired(), Email()])","    password = PasswordField('Password', validators=[DataRequired()])","    confirm_password = PasswordField('Confirm Password',","                                     validators=[DataRequired(), EqualTo('password')])","    submit = SubmitField('Sign Up')","","","class LoginForm(FlaskForm):","    email = StringField('Email',","                        validators=[DataRequired(), Email()])","    password = PasswordField('Password', validators=[DataRequired()])","    remember = BooleanField('Remember Me')","    submit = SubmitField('Login')",""]}]]},"ace":{"folds":[],"scrolltop":91,"scrollleft":0,"selection":{"start":{"row":22,"column":0},"end":{"row":22,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":4,"state":"start","mode":"ace/mode/python"}},"timestamp":1566617863219,"hash":"8a1fea516e3afa7c487ca89eab45843c19df2a8e"}