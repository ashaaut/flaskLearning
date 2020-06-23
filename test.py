from flask import  Flask,redirect,url_for
app=Flask(__name__)

@app.route('/admin/')
def Hello_admin():
    return "hello admin" 

@app.route('/guest/<guest>')
def Hello_guest(guest):
    return "Hello %s as guest "%guest

@app.route('/user/<name>')
def Hello_user(name):
    if name=="admin":
       return redirect(url_for("Hello_admin"))
    else:
       return redirect(url_for("Hello_guest", guest=name))
if __name__=='__main__':
    app.run(debug=True)