from blog import app, db
from blog.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return dict(
        db=db,
        User=User,
        Post=Post
    )


if __name__ == '__main__':
    app.run(debug=True)
