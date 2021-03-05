from flask import Flask, render_template, request, session, redirect, url_for, g


class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'



users = []
users.append(User(id=1, username='Ori', password='123'))
users.append(User(id=2, username='Dana', password='123'))
users.append(User(id=2, username='Adi', password='123'))
users.append(User(id=2, username='Ben', password='123'))




app = Flask(__name__)
app.secret_key = 'ksfashfqn23t828mt239mjio24tcny014tcnyny8nhu-0mt=2t21cvtp2m493m0-cvn3 y0819nf61m-5u1c0'


@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user



@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))

        return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))

    return render_template('profile.html')

if __name__ == "__main__":
    app.run(debug=True)