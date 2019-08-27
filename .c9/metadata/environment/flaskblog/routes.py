{"filter":false,"title":"routes.py","tooltip":"/flaskblog/routes.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":88,"column":8},"end":{"row":88,"column":9},"action":"remove","lines":[" "],"id":827},{"start":{"row":88,"column":4},"end":{"row":88,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":88,"column":4},"end":{"row":88,"column":5},"action":"insert","lines":[" "],"id":828},{"start":{"row":88,"column":5},"end":{"row":88,"column":6},"action":"insert","lines":[" "]},{"start":{"row":88,"column":6},"end":{"row":88,"column":7},"action":"insert","lines":[" "]}],[{"start":{"row":87,"column":12},"end":{"row":87,"column":16},"action":"insert","lines":["    "],"id":829}],[{"start":{"row":87,"column":12},"end":{"row":87,"column":16},"action":"remove","lines":["    "],"id":830}],[{"start":{"row":87,"column":12},"end":{"row":87,"column":16},"action":"insert","lines":["    "],"id":831}],[{"start":{"row":87,"column":12},"end":{"row":87,"column":16},"action":"remove","lines":["    "],"id":832}],[{"start":{"row":87,"column":12},"end":{"row":87,"column":13},"action":"insert","lines":[" "],"id":833}],[{"start":{"row":86,"column":12},"end":{"row":86,"column":16},"action":"insert","lines":["    "],"id":834}],[{"start":{"row":86,"column":12},"end":{"row":86,"column":16},"action":"remove","lines":["    "],"id":835},{"start":{"row":86,"column":8},"end":{"row":86,"column":12},"action":"remove","lines":["    "]}],[{"start":{"row":86,"column":8},"end":{"row":86,"column":9},"action":"insert","lines":["`"],"id":836}],[{"start":{"row":86,"column":8},"end":{"row":86,"column":9},"action":"remove","lines":["`"],"id":837}],[{"start":{"row":86,"column":8},"end":{"row":86,"column":12},"action":"insert","lines":["    "],"id":838}],[{"start":{"row":86,"column":12},"end":{"row":86,"column":13},"action":"insert","lines":[" "],"id":839}],[{"start":{"row":87,"column":12},"end":{"row":87,"column":13},"action":"remove","lines":[" "],"id":846}],[{"start":{"row":86,"column":8},"end":{"row":86,"column":12},"action":"remove","lines":["    "],"id":847}],[{"start":{"row":86,"column":8},"end":{"row":86,"column":9},"action":"insert","lines":[" "],"id":848},{"start":{"row":86,"column":9},"end":{"row":86,"column":10},"action":"insert","lines":[" "]},{"start":{"row":86,"column":10},"end":{"row":86,"column":11},"action":"insert","lines":[" "]}],[{"start":{"row":88,"column":6},"end":{"row":88,"column":8},"action":"insert","lines":["  "],"id":849}],[{"start":{"row":89,"column":7},"end":{"row":89,"column":8},"action":"insert","lines":[" "],"id":850}],[{"start":{"row":90,"column":7},"end":{"row":90,"column":8},"action":"insert","lines":[" "],"id":851}],[{"start":{"row":92,"column":7},"end":{"row":92,"column":8},"action":"insert","lines":[" "],"id":852}],[{"start":{"row":91,"column":7},"end":{"row":91,"column":8},"action":"insert","lines":[" "],"id":853}],[{"start":{"row":92,"column":7},"end":{"row":92,"column":8},"action":"insert","lines":[" "],"id":855}],[{"start":{"row":91,"column":8},"end":{"row":91,"column":9},"action":"insert","lines":[" "],"id":856}],[{"start":{"row":90,"column":7},"end":{"row":90,"column":8},"action":"insert","lines":[" "],"id":857},{"start":{"row":89,"column":7},"end":{"row":89,"column":8},"action":"insert","lines":[" "]}],[{"start":{"row":88,"column":7},"end":{"row":88,"column":8},"action":"insert","lines":[" "],"id":858}],[{"start":{"row":88,"column":9},"end":{"row":88,"column":10},"action":"remove","lines":[" "],"id":859}],[{"start":{"row":86,"column":11},"end":{"row":86,"column":12},"action":"insert","lines":[" "],"id":860}],[{"start":{"row":87,"column":12},"end":{"row":87,"column":13},"action":"insert","lines":[" "],"id":861}],[{"start":{"row":73,"column":12},"end":{"row":73,"column":13},"action":"remove","lines":["e"],"id":864},{"start":{"row":73,"column":11},"end":{"row":73,"column":12},"action":"remove","lines":["m"]},{"start":{"row":73,"column":10},"end":{"row":73,"column":11},"action":"remove","lines":["a"]},{"start":{"row":73,"column":9},"end":{"row":73,"column":10},"action":"remove","lines":["n"]},{"start":{"row":73,"column":8},"end":{"row":73,"column":9},"action":"remove","lines":["_"]},{"start":{"row":73,"column":7},"end":{"row":73,"column":8},"action":"remove","lines":["f"]},{"start":{"row":73,"column":6},"end":{"row":73,"column":7},"action":"remove","lines":[" "]}],[{"start":{"row":73,"column":6},"end":{"row":73,"column":7},"action":"remove","lines":[","],"id":865}],[{"start":{"row":72,"column":30},"end":{"row":72,"column":31},"action":"remove","lines":["."],"id":866}],[{"start":{"row":72,"column":30},"end":{"row":72,"column":31},"action":"insert","lines":["_"],"id":867}],[{"start":{"row":89,"column":46},"end":{"row":89,"column":47},"action":"insert","lines":[" "],"id":868}],[{"start":{"row":0,"column":0},"end":{"row":100,"column":0},"action":"remove","lines":["import os","import secrets","from flask import render_template, url_for, flash, redirect, request","from flaskblog import app, db, bcrypt","from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm","from flaskblog.models import User, Post","from flask_login import login_user, current_user, logout_user, login_required","","posts = [","    {","        'author': ' Marcus Tang',","        'title': 'Blog Post 1',","        'content': 'First post content',","        'date_posted': 'April 20, 2019'","    },","    {","        'author': 'Billy Jean',","        'title': 'Blog Post 2',","        'content': 'Second post content',","        'date_posted': 'April 22, 2019'","    }","]","","","@app.route('/')","@app.route('/home')","def home():","    return render_template('home.html', posts=posts)","","","@app.route('/about')","def about():","    return render_template('about.html', title='About')","","","@app.route('/register', methods=['GET', 'POST'])","def register():","    if current_user.is_authenticated:","        return redirect(url_for('home'))","    form = RegistrationForm()","    if form.validate_on_submit():","        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')","        user = User(username=form.username.data, email=form.email.data, password=hashed_password)","        db.session.add(user)","        db.session.commit()","        flash('Your account has been created! You can now login!', 'success')","        return redirect(url_for('login'))","    return render_template('register.html', title='Register', form=form)","","","@app.route('/login', methods=['GET', 'POST'])","def login():","    if current_user.is_authenticated:","        return redirect(url_for('home'))","    form = LoginForm()","    if form.validate_on_submit():","        user = User.query.filter_by(email=form.email.data).first()","        if user and bcrypt.check_password_hash(user.password, form.password.data):","            login_user(user, remember=form.remember.data)","            next_page = request.args.get('next')","            return redirect(next_page) if next_page else redirect(url_for('home'))","        else:    ","            flash('Login Unsuccessful. Please check username and password', 'danger')","    return render_template('login.html', title='Login', form=form)","    ","","@app.route('/logout')","def logout():","    logout_user()","    return redirect(url_for('home'))","    ","def save_picture(form_picture):    ","    random_hex = secrets.token_hex(8)","    _, f_ext = os.path.splitext(form_picture.filename)  # _ is used as a throwaway variable name so editor wont have \"unused app error\"","    picture_fn = random_hex + f_ext","    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)","    form_picture.save(picture_path)","    ","    return picture_fn","    ","@app.route('/account', methods=['GET', 'POST'])","@login_required","def account():","    form = UpdateAccountForm()","    if form.validate_on_submit():","         if form.picture.data:","             picture_file =  save_picture(form.picture.data)","             current_user.image_file = picture_file","         current_user.username = form.username.data","         current_user.email = form.emaill.data ","         db.session.commit()","         flash('Account Updated', 'success')","         return redirect(url_for('account'))","    elif request.method == 'GET':","        form.username.data = current_user.username","        form.email.data = current_user.email","    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)","    return render_template('account.html', title='Account',image_file=image_file, form=form)","","       ",""],"id":869},{"start":{"row":0,"column":0},"end":{"row":107,"column":0},"action":"insert","lines":["import os","import secrets","from PIL import Image","from flask import render_template, url_for, flash, redirect, request","from flaskblog import app, db, bcrypt","from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm","from flaskblog.models import User, Post","from flask_login import login_user, current_user, logout_user, login_required","","","posts = [","    {","        'author': 'Corey Schafer',","        'title': 'Blog Post 1',","        'content': 'First post content',","        'date_posted': 'April 20, 2018'","    },","    {","        'author': 'Jane Doe',","        'title': 'Blog Post 2',","        'content': 'Second post content',","        'date_posted': 'April 21, 2018'","    }","]","","","@app.route(\"/\")","@app.route(\"/home\")","def home():","    return render_template('home.html', posts=posts)","","","@app.route(\"/about\")","def about():","    return render_template('about.html', title='About')","","","@app.route(\"/register\", methods=['GET', 'POST'])","def register():","    if current_user.is_authenticated:","        return redirect(url_for('home'))","    form = RegistrationForm()","    if form.validate_on_submit():","        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')","        user = User(username=form.username.data, email=form.email.data, password=hashed_password)","        db.session.add(user)","        db.session.commit()","        flash('Your account has been created! You are now able to log in', 'success')","        return redirect(url_for('login'))","    return render_template('register.html', title='Register', form=form)","","","@app.route(\"/login\", methods=['GET', 'POST'])","def login():","    if current_user.is_authenticated:","        return redirect(url_for('home'))","    form = LoginForm()","    if form.validate_on_submit():","        user = User.query.filter_by(email=form.email.data).first()","        if user and bcrypt.check_password_hash(user.password, form.password.data):","            login_user(user, remember=form.remember.data)","            next_page = request.args.get('next')","            return redirect(next_page) if next_page else redirect(url_for('home'))","        else:","            flash('Login Unsuccessful. Please check email and password', 'danger')","    return render_template('login.html', title='Login', form=form)","","","@app.route(\"/logout\")","def logout():","    logout_user()","    return redirect(url_for('home'))","","","def save_picture(form_picture):","    random_hex = secrets.token_hex(8)","    _, f_ext = os.path.splitext(form_picture.filename)","    picture_fn = random_hex + f_ext","    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)","","    output_size = (125, 125)","    i = Image.open(form_picture)","    i.thumbnail(output_size)","    i.save(picture_path)","","    return picture_fn","","","@app.route(\"/account\", methods=['GET', 'POST'])","@login_required","def account():","    form = UpdateAccountForm()","    if form.validate_on_submit():","        if form.picture.data:","            picture_file = save_picture(form.picture.data)","            current_user.image_file = picture_file","        current_user.username = form.username.data","        current_user.email = form.email.data","        db.session.commit()","        flash('Your account has been updated!', 'success')","        return redirect(url_for('account'))","    elif request.method == 'GET':","        form.username.data = current_user.username","        form.email.data = current_user.email","    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)","    return render_template('account.html', title='Account',","                           image_file=image_file, form=form)",""]}],[{"start":{"row":12,"column":19},"end":{"row":12,"column":33},"action":"remove","lines":["Corey Schafer'"],"id":871}],[{"start":{"row":12,"column":19},"end":{"row":12,"column":20},"action":"insert","lines":["M"],"id":872},{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"insert","lines":["a"]},{"start":{"row":12,"column":21},"end":{"row":12,"column":22},"action":"insert","lines":["r"]},{"start":{"row":12,"column":22},"end":{"row":12,"column":23},"action":"insert","lines":["c"]},{"start":{"row":12,"column":23},"end":{"row":12,"column":24},"action":"insert","lines":["u"]},{"start":{"row":12,"column":24},"end":{"row":12,"column":25},"action":"insert","lines":["s"]}],[{"start":{"row":12,"column":25},"end":{"row":12,"column":26},"action":"insert","lines":[" "],"id":873},{"start":{"row":12,"column":26},"end":{"row":12,"column":27},"action":"insert","lines":["T"]},{"start":{"row":12,"column":27},"end":{"row":12,"column":28},"action":"insert","lines":["a"]}],[{"start":{"row":12,"column":27},"end":{"row":12,"column":28},"action":"remove","lines":["a"],"id":874}],[{"start":{"row":12,"column":27},"end":{"row":12,"column":28},"action":"insert","lines":["n"],"id":875}],[{"start":{"row":12,"column":27},"end":{"row":12,"column":28},"action":"remove","lines":["n"],"id":876}],[{"start":{"row":12,"column":27},"end":{"row":12,"column":28},"action":"insert","lines":["a"],"id":877},{"start":{"row":12,"column":28},"end":{"row":12,"column":29},"action":"insert","lines":["n"]},{"start":{"row":12,"column":29},"end":{"row":12,"column":30},"action":"insert","lines":["g"]},{"start":{"row":12,"column":30},"end":{"row":12,"column":31},"action":"insert","lines":["'"]}],[{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"remove","lines":["0"],"id":878},{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"remove","lines":["2"]},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"remove","lines":[" "]},{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"remove","lines":["l"]},{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"remove","lines":["i"]},{"start":{"row":15,"column":26},"end":{"row":15,"column":27},"action":"remove","lines":["r"]},{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"remove","lines":["p"]}],[{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"insert","lines":["u"],"id":879},{"start":{"row":15,"column":26},"end":{"row":15,"column":27},"action":"insert","lines":["g"]}],[{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"insert","lines":[" "],"id":880},{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"insert","lines":["2"]},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"insert","lines":["8"]}],[{"start":{"row":15,"column":35},"end":{"row":15,"column":36},"action":"remove","lines":["8"],"id":881}],[{"start":{"row":15,"column":35},"end":{"row":15,"column":36},"action":"insert","lines":["9"],"id":882}],[{"start":{"row":21,"column":37},"end":{"row":21,"column":38},"action":"remove","lines":["8"],"id":883}],[{"start":{"row":21,"column":37},"end":{"row":21,"column":38},"action":"insert","lines":["9"],"id":884}],[{"start":{"row":21,"column":31},"end":{"row":21,"column":32},"action":"remove","lines":["1"],"id":885}],[{"start":{"row":21,"column":31},"end":{"row":21,"column":32},"action":"insert","lines":["0"],"id":886}],[{"start":{"row":21,"column":31},"end":{"row":21,"column":32},"action":"remove","lines":["0"],"id":887}],[{"start":{"row":21,"column":31},"end":{"row":21,"column":32},"action":"insert","lines":["9"],"id":888}],[{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"remove","lines":["l"],"id":889},{"start":{"row":21,"column":27},"end":{"row":21,"column":28},"action":"remove","lines":["i"]},{"start":{"row":21,"column":26},"end":{"row":21,"column":27},"action":"remove","lines":["r"]},{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"remove","lines":["p"]}],[{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"insert","lines":["u"],"id":890}],[{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"remove","lines":["u"],"id":891}],[{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"insert","lines":["u"],"id":892},{"start":{"row":21,"column":26},"end":{"row":21,"column":27},"action":"insert","lines":["g"]},{"start":{"row":21,"column":27},"end":{"row":21,"column":28},"action":"insert","lines":["u"]}],[{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"insert","lines":["s"],"id":893},{"start":{"row":21,"column":29},"end":{"row":21,"column":30},"action":"insert","lines":["t"]}],[{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"remove","lines":[" "],"id":894}],[{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"insert","lines":["u"],"id":895},{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"insert","lines":["s"]},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"insert","lines":["t"]}],[{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"insert","lines":[" "],"id":896}],[{"start":{"row":18,"column":23},"end":{"row":18,"column":24},"action":"remove","lines":[" "],"id":897},{"start":{"row":18,"column":22},"end":{"row":18,"column":23},"action":"remove","lines":["e"]},{"start":{"row":18,"column":21},"end":{"row":18,"column":22},"action":"remove","lines":["n"]},{"start":{"row":18,"column":20},"end":{"row":18,"column":21},"action":"remove","lines":["a"]}],[{"start":{"row":18,"column":20},"end":{"row":18,"column":21},"action":"insert","lines":["o"],"id":898},{"start":{"row":18,"column":21},"end":{"row":18,"column":22},"action":"insert","lines":["h"]},{"start":{"row":18,"column":22},"end":{"row":18,"column":23},"action":"insert","lines":["n"]}],[{"start":{"row":18,"column":23},"end":{"row":18,"column":24},"action":"insert","lines":[" "],"id":899}],[{"start":{"row":107,"column":0},"end":{"row":108,"column":0},"action":"insert","lines":["",""],"id":900},{"start":{"row":108,"column":0},"end":{"row":108,"column":1},"action":"insert","lines":["#"]}],[{"start":{"row":108,"column":0},"end":{"row":108,"column":1},"action":"remove","lines":["#"],"id":901}],[{"start":{"row":108,"column":0},"end":{"row":108,"column":1},"action":"insert","lines":["@"],"id":902},{"start":{"row":108,"column":1},"end":{"row":108,"column":2},"action":"insert","lines":["a"]},{"start":{"row":108,"column":2},"end":{"row":108,"column":3},"action":"insert","lines":["o"]},{"start":{"row":108,"column":3},"end":{"row":108,"column":4},"action":"insert","lines":["o"]}],[{"start":{"row":108,"column":3},"end":{"row":108,"column":4},"action":"remove","lines":["o"],"id":903},{"start":{"row":108,"column":2},"end":{"row":108,"column":3},"action":"remove","lines":["o"]}],[{"start":{"row":108,"column":2},"end":{"row":108,"column":3},"action":"insert","lines":["p"],"id":904},{"start":{"row":108,"column":3},"end":{"row":108,"column":4},"action":"insert","lines":["p"]},{"start":{"row":108,"column":4},"end":{"row":108,"column":5},"action":"insert","lines":["."]},{"start":{"row":108,"column":5},"end":{"row":108,"column":6},"action":"insert","lines":["t"]},{"start":{"row":108,"column":6},"end":{"row":108,"column":7},"action":"insert","lines":["o"]},{"start":{"row":108,"column":7},"end":{"row":108,"column":8},"action":"insert","lines":["u"]},{"start":{"row":108,"column":8},"end":{"row":108,"column":9},"action":"insert","lines":["t"]},{"start":{"row":108,"column":9},"end":{"row":108,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":108,"column":9},"end":{"row":108,"column":10},"action":"remove","lines":["e"],"id":905},{"start":{"row":108,"column":8},"end":{"row":108,"column":9},"action":"remove","lines":["t"]},{"start":{"row":108,"column":7},"end":{"row":108,"column":8},"action":"remove","lines":["u"]},{"start":{"row":108,"column":6},"end":{"row":108,"column":7},"action":"remove","lines":["o"]},{"start":{"row":108,"column":5},"end":{"row":108,"column":6},"action":"remove","lines":["t"]}],[{"start":{"row":108,"column":5},"end":{"row":108,"column":6},"action":"insert","lines":["r"],"id":906},{"start":{"row":108,"column":6},"end":{"row":108,"column":7},"action":"insert","lines":["u"]}],[{"start":{"row":108,"column":6},"end":{"row":108,"column":7},"action":"remove","lines":["u"],"id":907}],[{"start":{"row":108,"column":6},"end":{"row":108,"column":7},"action":"insert","lines":["o"],"id":908},{"start":{"row":108,"column":7},"end":{"row":108,"column":8},"action":"insert","lines":["u"]},{"start":{"row":108,"column":8},"end":{"row":108,"column":9},"action":"insert","lines":["t"]},{"start":{"row":108,"column":9},"end":{"row":108,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":108,"column":10},"end":{"row":108,"column":12},"action":"insert","lines":["()"],"id":909}],[{"start":{"row":108,"column":11},"end":{"row":108,"column":13},"action":"insert","lines":["\"\""],"id":910}],[{"start":{"row":108,"column":12},"end":{"row":108,"column":13},"action":"insert","lines":["/"],"id":911},{"start":{"row":108,"column":13},"end":{"row":108,"column":14},"action":"insert","lines":["p"]},{"start":{"row":108,"column":14},"end":{"row":108,"column":15},"action":"insert","lines":["o"]},{"start":{"row":108,"column":15},"end":{"row":108,"column":16},"action":"insert","lines":["s"]},{"start":{"row":108,"column":16},"end":{"row":108,"column":17},"action":"insert","lines":["t"]}],[{"start":{"row":108,"column":17},"end":{"row":108,"column":18},"action":"insert","lines":["/"],"id":912},{"start":{"row":108,"column":18},"end":{"row":108,"column":19},"action":"insert","lines":["n"]},{"start":{"row":108,"column":19},"end":{"row":108,"column":20},"action":"insert","lines":["e"]},{"start":{"row":108,"column":20},"end":{"row":108,"column":21},"action":"insert","lines":["w"]}],[{"start":{"row":108,"column":23},"end":{"row":109,"column":0},"action":"insert","lines":["",""],"id":913}],[{"start":{"row":108,"column":23},"end":{"row":109,"column":0},"action":"remove","lines":["",""],"id":914}],[{"start":{"row":108,"column":23},"end":{"row":108,"column":24},"action":"insert","lines":["d"],"id":915}],[{"start":{"row":108,"column":23},"end":{"row":108,"column":24},"action":"remove","lines":["d"],"id":916}],[{"start":{"row":108,"column":23},"end":{"row":109,"column":0},"action":"insert","lines":["",""],"id":917},{"start":{"row":109,"column":0},"end":{"row":109,"column":1},"action":"insert","lines":["d"]},{"start":{"row":109,"column":1},"end":{"row":109,"column":2},"action":"insert","lines":["e"]},{"start":{"row":109,"column":2},"end":{"row":109,"column":3},"action":"insert","lines":["f"]}],[{"start":{"row":109,"column":3},"end":{"row":109,"column":4},"action":"insert","lines":[" "],"id":918},{"start":{"row":109,"column":4},"end":{"row":109,"column":5},"action":"insert","lines":["n"]},{"start":{"row":109,"column":5},"end":{"row":109,"column":6},"action":"insert","lines":["e"]},{"start":{"row":109,"column":6},"end":{"row":109,"column":7},"action":"insert","lines":["w"]}],[{"start":{"row":109,"column":7},"end":{"row":109,"column":9},"action":"insert","lines":["()"],"id":919}],[{"start":{"row":109,"column":9},"end":{"row":109,"column":10},"action":"insert","lines":[":"],"id":920}],[{"start":{"row":109,"column":7},"end":{"row":109,"column":8},"action":"insert","lines":["_"],"id":921},{"start":{"row":109,"column":8},"end":{"row":109,"column":9},"action":"insert","lines":["p"]},{"start":{"row":109,"column":9},"end":{"row":109,"column":10},"action":"insert","lines":["o"]},{"start":{"row":109,"column":10},"end":{"row":109,"column":11},"action":"insert","lines":["s"]},{"start":{"row":109,"column":11},"end":{"row":109,"column":12},"action":"insert","lines":["t"]}],[{"start":{"row":108,"column":23},"end":{"row":109,"column":0},"action":"insert","lines":["",""],"id":922},{"start":{"row":109,"column":0},"end":{"row":109,"column":1},"action":"insert","lines":["@"]},{"start":{"row":109,"column":1},"end":{"row":109,"column":2},"action":"insert","lines":["l"]},{"start":{"row":109,"column":2},"end":{"row":109,"column":3},"action":"insert","lines":["o"]},{"start":{"row":109,"column":3},"end":{"row":109,"column":4},"action":"insert","lines":["g"]},{"start":{"row":109,"column":4},"end":{"row":109,"column":5},"action":"insert","lines":["i"]},{"start":{"row":109,"column":5},"end":{"row":109,"column":6},"action":"insert","lines":["n"]}],[{"start":{"row":109,"column":6},"end":{"row":109,"column":7},"action":"insert","lines":["_"],"id":923},{"start":{"row":109,"column":7},"end":{"row":109,"column":8},"action":"insert","lines":["r"]},{"start":{"row":109,"column":8},"end":{"row":109,"column":9},"action":"insert","lines":["e"]},{"start":{"row":109,"column":9},"end":{"row":109,"column":10},"action":"insert","lines":["q"]},{"start":{"row":109,"column":10},"end":{"row":109,"column":11},"action":"insert","lines":["u"]},{"start":{"row":109,"column":11},"end":{"row":109,"column":12},"action":"insert","lines":["i"]},{"start":{"row":109,"column":12},"end":{"row":109,"column":13},"action":"insert","lines":["r"]},{"start":{"row":109,"column":13},"end":{"row":109,"column":14},"action":"insert","lines":["e"]},{"start":{"row":109,"column":14},"end":{"row":109,"column":15},"action":"insert","lines":["d"]}],[{"start":{"row":110,"column":15},"end":{"row":111,"column":0},"action":"insert","lines":["",""],"id":924},{"start":{"row":111,"column":0},"end":{"row":111,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":111,"column":4},"end":{"row":111,"column":60},"action":"insert","lines":[" return render_template('account.html', title='Account',"],"id":925}],[{"start":{"row":111,"column":35},"end":{"row":111,"column":36},"action":"remove","lines":["t"],"id":926},{"start":{"row":111,"column":34},"end":{"row":111,"column":35},"action":"remove","lines":["n"]},{"start":{"row":111,"column":33},"end":{"row":111,"column":34},"action":"remove","lines":["u"]},{"start":{"row":111,"column":32},"end":{"row":111,"column":33},"action":"remove","lines":["o"]},{"start":{"row":111,"column":31},"end":{"row":111,"column":32},"action":"remove","lines":["c"]},{"start":{"row":111,"column":30},"end":{"row":111,"column":31},"action":"remove","lines":["c"]},{"start":{"row":111,"column":29},"end":{"row":111,"column":30},"action":"remove","lines":["a"]}],[{"start":{"row":111,"column":29},"end":{"row":111,"column":30},"action":"insert","lines":["c"],"id":927},{"start":{"row":111,"column":30},"end":{"row":111,"column":31},"action":"insert","lines":["r"]},{"start":{"row":111,"column":31},"end":{"row":111,"column":32},"action":"insert","lines":["e"]},{"start":{"row":111,"column":32},"end":{"row":111,"column":33},"action":"insert","lines":["a"]},{"start":{"row":111,"column":33},"end":{"row":111,"column":34},"action":"insert","lines":["t"]},{"start":{"row":111,"column":34},"end":{"row":111,"column":35},"action":"insert","lines":["e"]}],[{"start":{"row":111,"column":35},"end":{"row":111,"column":36},"action":"insert","lines":["_"],"id":928},{"start":{"row":111,"column":36},"end":{"row":111,"column":37},"action":"insert","lines":["p"]},{"start":{"row":111,"column":37},"end":{"row":111,"column":38},"action":"insert","lines":["o"]},{"start":{"row":111,"column":38},"end":{"row":111,"column":39},"action":"insert","lines":["s"]},{"start":{"row":111,"column":39},"end":{"row":111,"column":40},"action":"insert","lines":["t"]}],[{"start":{"row":111,"column":55},"end":{"row":111,"column":63},"action":"remove","lines":["Account'"],"id":929}],[{"start":{"row":111,"column":55},"end":{"row":111,"column":56},"action":"insert","lines":["N"],"id":930},{"start":{"row":111,"column":56},"end":{"row":111,"column":57},"action":"insert","lines":["e"]},{"start":{"row":111,"column":57},"end":{"row":111,"column":58},"action":"insert","lines":["w"]}],[{"start":{"row":111,"column":58},"end":{"row":111,"column":59},"action":"insert","lines":[" "],"id":931},{"start":{"row":111,"column":59},"end":{"row":111,"column":60},"action":"insert","lines":["p"]}],[{"start":{"row":111,"column":59},"end":{"row":111,"column":60},"action":"remove","lines":["p"],"id":932}],[{"start":{"row":111,"column":59},"end":{"row":111,"column":60},"action":"insert","lines":["P"],"id":933},{"start":{"row":111,"column":60},"end":{"row":111,"column":61},"action":"insert","lines":["o"]},{"start":{"row":111,"column":61},"end":{"row":111,"column":62},"action":"insert","lines":["s"]},{"start":{"row":111,"column":62},"end":{"row":111,"column":63},"action":"insert","lines":["t"]},{"start":{"row":111,"column":63},"end":{"row":111,"column":64},"action":"insert","lines":["'"]}],[{"start":{"row":111,"column":4},"end":{"row":111,"column":5},"action":"remove","lines":[" "],"id":934}],[{"start":{"row":0,"column":0},"end":{"row":8,"column":0},"action":"remove","lines":["import os","import secrets","from PIL import Image","from flask import render_template, url_for, flash, redirect, request","from flaskblog import app, db, bcrypt","from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm","from flaskblog.models import User, Post","from flask_login import login_user, current_user, logout_user, login_required",""],"id":935},{"start":{"row":0,"column":0},"end":{"row":9,"column":77},"action":"insert","lines":["","Learn more or give us feedback","import os","import secrets","from PIL import Image","from flask import render_template, url_for, flash, redirect, request, abort","from flaskblog import app, db, bcrypt","from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm","from flaskblog.models import User, Post","from flask_login import login_user, current_user, logout_user, login_required"]}],[{"start":{"row":0,"column":0},"end":{"row":9,"column":77},"action":"remove","lines":["","Learn more or give us feedback","import os","import secrets","from PIL import Image","from flask import render_template, url_for, flash, redirect, request, abort","from flaskblog import app, db, bcrypt","from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm","from flaskblog.models import User, Post","from flask_login import login_user, current_user, logout_user, login_required"],"id":936},{"start":{"row":0,"column":0},"end":{"row":7,"column":77},"action":"insert","lines":["import os","import secrets","from PIL import Image","from flask import render_template, url_for, flash, redirect, request, abort","from flaskblog import app, db, bcrypt","from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm","from flaskblog.models import User, Post","from flask_login import login_user, current_user, logout_user, login_required"]}],[{"start":{"row":107,"column":0},"end":{"row":110,"column":64},"action":"remove","lines":["@app.route(\"/post/new\")","@login_required","def new_post():","    return render_template('create_post.html', title='New Post',"],"id":937},{"start":{"row":107,"column":0},"end":{"row":156,"column":36},"action":"insert","lines":["@app.route(\"/post/new\", methods=['GET', 'POST'])","@login_required","def new_post():","    form = PostForm()","    if form.validate_on_submit():","        post = Post(title=form.title.data, content=form.content.data, author=current_user)","        db.session.add(post)","        db.session.commit()","        flash('Your post has been created!', 'success')","        return redirect(url_for('home'))","    return render_template('create_post.html', title='New Post',","                           form=form, legend='New Post')","","","@app.route(\"/post/<int:post_id>\")","def post(post_id):","    post = Post.query.get_or_404(post_id)","    return render_template('post.html', title=post.title, post=post)","","","@app.route(\"/post/<int:post_id>/update\", methods=['GET', 'POST'])","@login_required","def update_post(post_id):","    post = Post.query.get_or_404(post_id)","    if post.author != current_user:","        abort(403)","    form = PostForm()","    if form.validate_on_submit():","        post.title = form.title.data","        post.content = form.content.data","        db.session.commit()","        flash('Your post has been updated!', 'success')","        return redirect(url_for('post', post_id=post.id))","    elif request.method == 'GET':","        form.title.data = post.title","        form.content.data = post.content","    return render_template('create_post.html', title='Update Post',","                           form=form, legend='Update Post')","","","@app.route(\"/post/<int:post_id>/delete\", methods=['POST'])","@login_required","def delete_post(post_id):","    post = Post.query.get_or_404(post_id)","    if post.author != current_user:","        abort(403)","    db.session.delete(post)","    db.session.commit()","    flash('Your post has been deleted!', 'success')","    return redirect(url_for('home'))"]}]]},"ace":{"folds":[],"scrolltop":1397,"scrollleft":0,"selection":{"start":{"row":156,"column":36},"end":{"row":156,"column":36},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":81,"state":"start","mode":"ace/mode/python"}},"timestamp":1566932252425,"hash":"22733b0e0d2bd4e9adc5f4c0d0e0bcb438699dd2"}