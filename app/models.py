from flask_sqlalchemy import SQLAlchemy
from flask import  url_for



db = SQLAlchemy()


class Post(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    userName = db.Column(db.String(255))
    image = db.Column(db.String(255))
    content = db.Column(db.String)
    created_at = db.Column(db.String)
    updated_at = db.Column(db.String)

    @property
    def get_image_url(self):
        return url_for('static', filename=f'posts/images/{self.image}')

    @property
    def get_show_url(self):
        return  url_for('post.show', id=self.id)
    
    @property
    def get_edit_url(self):
        return  url_for('post.edit', id=self.id)

    @property
    def get_delete_url(self):
        return  url_for('post.delete', id= self.id)
