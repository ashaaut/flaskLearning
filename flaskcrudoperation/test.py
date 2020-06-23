from flask import  Flask,render_template
app=Flask(__name__)

@app.route('/admin/')
def Hello_admin():
    return render_template('productioninfo.html')

if __name__=='__main__':
    app.run(debug=True)