from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask('__main__')






db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
db.__init__(app)



class Student(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    userName = db.Column(db.String)
    image = db.Column(db.String)
    content = db.Column(db.String)
    created_at = db.Column(db.date)
    updated_at = db.Column(db.date)

    @property
    def get_image_url(self):
        return url_for('static', filename=f'posts/images/{self.image}')

    # @property
    # def get_show_url(self):
    #     return  url_for('students.show', id=self.id)

    # @property
    # def get_delete_url(self):
    #     return  url_for('students.delete', id= self.id)


postData = [
    {
        'userName':'Maged',
        'title':'Flask Project',
        'content':'Hello in my Project',
        'image':'pic1.jpg',
        'created_at':'6/10/2023',
        'modified_at':'7/10/2023'
    },{
        'userName':'Khaled',
        'title':'Django Project',
        'content':'Welcome in my Project',
        'image':'pic2.jpg',
        'created_at':'9/10/2023',
        'modified_at':'10/10/2023'
    },{
        'userName':'Ahmed',
        'title':'JS Project',
        'content':'Hello in our Project',
        'image':'pic3.jpg',
        'created_at':'19/10/2023',
        'modified_at':'20/10/2023'
    },
]


@app.route('/posts',methods=['GET'],endpoint='post.home')
def postList():
    return render_template('posts/home.html',posts=postData)


if __name__ == '__main__':
    app.run(debug=True)


