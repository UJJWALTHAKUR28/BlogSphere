from flask import  render_template, url_for, flash, redirect, request,abort
import secrets
from PIL import Image
import os
#we can fix this importing user and post here
from flaskapp import app,db,Bcrypt1
from flaskapp.forms import RegistrationForm, LoginForm, UpdateAccountForm,AddNewPost,RequestResetForm,ResetPasswordForm
from flaskapp.models import User,Post
from flask_login import login_user,current_user,logout_user,login_required
from flask_mail import Message
#this is the first we have created a module now e hae put this in models.py to make it paackakged structred
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
#     password = db.Column(db.String(60), nullable=False)
#     posts = db.relationship('Post', backref='author', lazy=True)

#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}', '{self.image_file}')"


# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     content = db.Column(db.Text, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     def __repr__(self):
#         return f"Post('{self.title}', '{self.date_posted}')"
@app.route("/")
@app.route("/home")
def home():
    page=request.args.get('page',1,type=int)
    posts=Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=5)
    return render_template('home.html', posts=posts)
@app.route("/about")
def about():
    return render_template('about.html', title='About')
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password= Bcrypt1.generate_password_hash(form.password.data.encode('utf-8'))
        hashed_password = hashed_password.decode('utf-8')
        user=User(username= form.username.data,email= form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}! You are now able to login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and Bcrypt1.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            next_page=request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _,f_ext =os.path.splitext(form_picture.filename)
    picture_fn= random_hex+ f_ext
    picture_path = os.path.join(app.root_path,'static/profile',picture_fn)
    output_size=(125,125)
    i=Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn
@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
             picture_file =save_picture(form.picture.data)
             current_user.image_file =picture_file
        current_user.username =form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your Account has been updated",'Success')
        return redirect(url_for('account'))
    elif request.method=='GET':
        form.username.data=current_user.username
        form.email.data = current_user.email
    image_file = url_for('static',filename='profile/'+current_user.image_file)
    return render_template('account.html', title='Account',image_file=image_file,form=form)
@app.route("/post/new",methods=["GET","POST"])
@login_required
def newpost():
    form = AddNewPost()
    if form.validate_on_submit():
        post= Post(title=form.title.data,content=form.content.data,author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!','success')
        return redirect(url_for('home'))
    return render_template('post.html',title="ADD POST",form=form,legend="New Post") 
@app.route("/post/<int:post_id>")
def post(post_id):
    #post=Post.query.get(post_id)
    post= Post.query.get_or_404(post_id)
    return render_template("post_.html",title=post.title,post=post)
@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post =Post.query.get_or_404(post_id)
    if post.author!=current_user:
        abort(403)
    form=AddNewPost()
    if form.validate_on_submit():
        post.title= form.title.data
        post.content= form.content.data
        db.session.commit()
        flash("Your post has been updated!",'success')
        return redirect(url_for('post',post_id=post.id))
    elif request.method == 'GET':
        form.title.data=post.title
        form.content.data=post.content
    return render_template('post.html',title="Update POST",form=form,legend="Update Post") 
@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post =Post.query.get_or_404(post_id)
    if post.author!=current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Your post has been deleted!",'success')
    return redirect(url_for('home'))

@app.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user.html', posts=posts, user=user)

def send_reset_email(user):
    token=user.get_reset_token()
    msg=Message('Password Reset P]Request',sender='noreply@demo.com',recipients=[user.email])
    msg.body=f'''TO RESET YOUR PASSWORD VISIT THE FOLLOWING LINK:
    {url_for('reset_token',token=token,_external=True)}
    If yoy did not make this request then simply ingnore this email'''
    #mail(msg)
    
@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            # send_reset_email(user)
            flash('An email has been sent with instructions to reset your password.', 'info')
        else:
            flash('No account found with that email address.', 'warning')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@app.route("/reset_password/<token>",methods=['GET','POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user=User.verify_reset_token(token)
    if user is None:
        flash("That is an invalid token or expired token",'warning')
        return redirect(url_for('reset_request'))
    form= ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password= Bcrypt1.generate_password_hash(form.password.data.encode('utf-8'))
        hashed_password = hashed_password.decode('utf-8')
        user.password=hashed_password
        db.session.commit()
        flash(f'Account created for {form.username.data}! You are now able to login', 'success')
        return redirect(url_for('login'))
    return render_template('reset_token.html',title='Reset Password',form=form)
