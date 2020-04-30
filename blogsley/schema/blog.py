import requests

import graphene
from graphene import relay
from graphql_relay import to_global_id
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from rx import Observable

from blogsley.config import app
from blogsley.config import db
from blogsley.models.users import User
from blogsley.models.blog import Post
from blogsley.jwt import decode_auth_token, load_user

class PostNode(SQLAlchemyObjectType):
    class Meta:
        model = Post
        interfaces = (relay.Node, )

class PostConnection(relay.Connection):
    class Meta:
        node = PostNode

class PostInput(graphene.InputObjectType):
    title = graphene.String()
    model = graphene.String()
    body = graphene.String()

class CreatePost(graphene.Mutation):
    class Arguments:
        data = PostInput(required=True)

    id = graphene.ID()

    @staticmethod
    def mutate(self, info, data=None):
        user = load_user(info)
        user_id = user.id
        print(user)
        post = Post(title=data.title, model=data.model, body=data.body, owner_id=user_id)
        db.session.add(post)
        db.session.commit()
        # db.session.flush()
        db.session.refresh(post)
        print(post)
        #id = post.id
        id = to_global_id(PostNode._meta.name, post.id)

        return CreatePost(id=id)

class UpdatePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        data = PostInput(required=True)
        
    ok = graphene.Boolean()

    @staticmethod
    def mutate(self, info, id, data):
        # get the JWT
        token = decode_auth_token(info.context)
        print(token)
        post = graphene.Node.get_node_from_global_id(info, id)
        print(post)
        post.title = data.title
        post.model = data.model
        post.body = data.body
        db.session.commit()

        ok = True
        return ok

class PublishPost(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        data = PostInput(required=True)
        
    ok = graphene.Boolean()

    @staticmethod
    def mutate(self, info, id, data):
        # get the JWT
        token = decode_auth_token(info.context)
        print(token)
        # post = Post.query.get(id)
        post = graphene.Node.get_node_from_global_id(info, id)
        print(post)
        post.title = data.title
        post.model = data.model
        post.body = data.body
        db.session.commit()

        publishHook = app.config.get('PUBLISH_HOOK')
        r = requests.post(publishHook, data = {'key':'value'})
        ok = True
        return ok

class DeletePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(self, info, id):
        # get the JWT
        token = decode_auth_token(info.context)
        print(token)
        post = graphene.Node.get_node_from_global_id(info, id)
        print(post)
        db.session.delete(post)
        db.session.commit()
        ok = True

        return ok

class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    publish_post = PublishPost.Field()
    delete_post = DeletePost.Field()

class Query(graphene.ObjectType):
    post = relay.Node.Field(PostNode)
    all_posts = SQLAlchemyConnectionField(PostConnection)
    post_by = graphene.Field(PostNode, slug=graphene.String())
    # post_by = graphene.Field(lambda: graphene.List(PostNode), slug=graphene.String())

    def resolve_post_by(parent, info, slug):
        query = PostNode.get_query(info)  # SQLAlchemy query
        return query.filter_by(slug=slug).first()


class PostEvent(graphene.ObjectType):
    kind = graphene.String()
    def __init__(self, id, kind='UPDATE'):
        super().__init__()
        '''
        self.id = id
        self.kind = kind
        '''

def push_post(observer):
    observer.on_next(PostEvent(0, 'UPDATE'))

class Subscription(graphene.ObjectType):
    post_events = graphene.Field(PostEvent, id=graphene.ID())
    def resolve_post_events(root, info, id=None):
        print('post events subscription')
        source = Observable.create(push_post)
        print(source)
        return source
