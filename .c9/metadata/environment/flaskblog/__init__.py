{"changed":true,"filter":false,"title":"__init__.py","tooltip":"/flaskblog/__init__.py","value":"from flask import Flask\nfrom flask_sqlalchemy import SQLAlchemy\nfrom flask_bcrypt import Bcrypt \nfrom flask_login import LoginManager\n\napp = Flask(__name__)\napp.config['SECRET_KEY'] = '37d9b26f4a0cda72818c4c6d4e3a9641'\napp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'\ndb = SQLAlchemy(app)\nbcrypt = Bcrypt(app)\nlogin_manager = LoginManager(app)\nlogin_manager.login_view = 'login'\nlogin_manager.login_message_category = 'info'\n\n\nfrom flaskblog import routes\n","undoManager":{"mark":-2,"position":17,"stack":[[{"start":{"row":12,"column":0},"end":{"row":12,"column":36},"action":"insert","lines":["app.config.from_object(config_class)"],"id":135}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":36},"action":"remove","lines":["app.config.from_object(config_class)"],"id":136}],[{"start":{"row":15,"column":33},"end":{"row":15,"column":34},"action":"insert","lines":["_"],"id":137},{"start":{"row":15,"column":34},"end":{"row":15,"column":35},"action":"insert","lines":["c"]},{"start":{"row":15,"column":35},"end":{"row":15,"column":36},"action":"insert","lines":["l"]}],[{"start":{"row":15,"column":35},"end":{"row":15,"column":36},"action":"remove","lines":["l"],"id":138}],[{"start":{"row":15,"column":35},"end":{"row":15,"column":36},"action":"insert","lines":["l"],"id":139},{"start":{"row":15,"column":36},"end":{"row":15,"column":37},"action":"insert","lines":["a"]},{"start":{"row":15,"column":37},"end":{"row":15,"column":38},"action":"insert","lines":["s"]},{"start":{"row":15,"column":38},"end":{"row":15,"column":39},"action":"insert","lines":["s"]}],[{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"remove","lines":["C"],"id":140}],[{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"insert","lines":["c"],"id":141}],[{"start":{"row":15,"column":38},"end":{"row":15,"column":39},"action":"remove","lines":["s"],"id":142},{"start":{"row":15,"column":37},"end":{"row":15,"column":38},"action":"remove","lines":["s"]},{"start":{"row":15,"column":36},"end":{"row":15,"column":37},"action":"remove","lines":["a"]},{"start":{"row":15,"column":35},"end":{"row":15,"column":36},"action":"remove","lines":["l"]},{"start":{"row":15,"column":34},"end":{"row":15,"column":35},"action":"remove","lines":["c"]},{"start":{"row":15,"column":33},"end":{"row":15,"column":34},"action":"remove","lines":["_"]}],[{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"insert","lines":["C"],"id":143}],[{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"remove","lines":["C"],"id":144},{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"remove","lines":["c"]}],[{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"insert","lines":["C"],"id":145}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"insert","lines":["c"],"id":146},{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"insert","lines":["u"]},{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"insert","lines":["r"]},{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"insert","lines":["r"]},{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"insert","lines":["e"]},{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"insert","lines":["n"]},{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"insert","lines":["t"]},{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"insert","lines":["_"]}],[{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"remove","lines":["_"],"id":147},{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"remove","lines":["t"]},{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"remove","lines":["n"]},{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"remove","lines":["e"]},{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"remove","lines":["r"]},{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"remove","lines":["r"]},{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"remove","lines":["u"]},{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"remove","lines":["c"]}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["import os",""],"id":148,"ignore":true},{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"remove","lines":["from flaskblog.config import Config",""]},{"start":{"row":5,"column":0},"end":{"row":9,"column":68},"action":"insert","lines":["","","app = Flask(__name__)","app.config['SECRET_KEY'] = '37d9b26f4a0cda72818c4c6d4e3a9641'","app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get['DATABASE_URL']"]},{"start":{"row":10,"column":16},"end":{"row":10,"column":19},"action":"insert","lines":["app"]},{"start":{"row":11,"column":16},"end":{"row":11,"column":17},"action":"remove","lines":[")"]},{"start":{"row":11,"column":16},"end":{"row":12,"column":0},"action":"insert","lines":["app)",""]},{"start":{"row":13,"column":29},"end":{"row":13,"column":32},"action":"insert","lines":["app"]},{"start":{"row":14,"column":28},"end":{"row":14,"column":34},"action":"remove","lines":["users."]},{"start":{"row":18,"column":0},"end":{"row":34,"column":14},"action":"remove","lines":["def create_app(config_class=Config):","    app = Flask(__name__)","    app.config.from_object(Config)","","    db.init_app(app)","    bcrypt.init_app(app)","    login_manager.init_app(app)","","","    from flaskblog.users.routes import users","    from flaskblog.posts.routes import posts","    from flaskblog.main.routes import main","    app.register_blueprint(users)","    app.register_blueprint(posts)","    app.register_blueprint(main)","","    return app"]},{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"insert","lines":["from flaskblog import routes",""]}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["import os",""],"id":149,"ignore":true},{"start":{"row":4,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["import os","import psycopg2",""]},{"start":{"row":10,"column":37},"end":{"row":10,"column":68},"action":"remove","lines":["=os.environ.get['DATABASE_URL']"]},{"start":{"row":10,"column":37},"end":{"row":10,"column":59},"action":"insert","lines":[" = 'sqlite:///site.db'"]},{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":15},"action":"remove","lines":["import psycopg2"],"id":150}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":9},"action":"remove","lines":["import os"],"id":151}],[{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"remove","lines":["",""],"id":152},{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"remove","lines":["",""]},{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":20},"end":{"row":9,"column":20},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1567126517017}