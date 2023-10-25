# from flask import render_template, url_for, request, redirect



# @app.route('/posts',methods=['GET'],endpoint='post.home')
# def postList():
#     posts = Post.query.all()
#     return render_template('posts/home.html',posts=posts)


# @app.route('/create',methods=['GET','POST'],endpoint='post.create')
# def createPost():
#     if request.method == 'POST':

        
#         post = Post(**request.form)

#         f = request.files['image']
#         f.save(secure_filename(f.filename))


#         db.session.add(post)
#         db.session.commit()
#         return redirect(url_for('post.home'))
#     return render_template('posts/create.html')

# @app.route('/edit/<int:id>',methods=['GET','POST'],endpoint='post.edit')
# def editPost(id):
#     post = Post.query.get_or_404(id)
#     if post:

#         if request.method == 'POST':

#             post.title = request.form['title']
#             post.content = request.form['content']
#             post.userName = request.form['userName']
#             post.image = request.form['image']
#             db.session.commit()

#             return render_template('posts/show.html',post=post)


#         return render_template('posts/edit.html',post=post)
        
#     return 'Post not exist'
    

# @app.route('/show/<int:id>',methods=['GET'],endpoint='post.show')
# def showPost(id):
#     post = Post.query.get_or_404(id)
#     if post:
#         return render_template('posts/show.html',post=post)
#     return 'Post not exist'

# @app.route('/delete/<int:id>',methods=['GET'],endpoint='post.delete')
# def deletePost(id):
#     post = Post.query.get_or_404(id)
#     if post :
#         db.session.delete(post)
#         db.session.commit()
#     return redirect(url_for('post.home'))


# if __name__ == '__main__':
#     app.run(debug=True)


