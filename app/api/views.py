from flask import jsonify, request, url_for, current_app
from . import api
from ..models import Post, Comment

@api.route('/get_post/')
def get_posts():
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.paginate(
        page, per_page=20,
        error_out=False)
    posts = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_posts', page=page - 1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_posts', page=page + 1)
    return jsonify({
        'posts': [post.to_json() for post in posts],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })


@api.route('/get_post_comment/')
def get_post_comments():
    post_id = request.args.get('post_id',type=int)
    comments = Comment.query.filter_by(post_doc_id=post_id).all()
    return jsonify({
        'comment': [comment.to_json() for comment in comments],
    })
