import requests
from loguru import logger

import graphene
from graphene import relay
from graphql_relay import to_global_id
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from rx import Observable

from __blogsley__ import app
from __blogsley__ import db
from blogsley_flask.jwt import decode_auth_token, load_user

from blogsley_flask.user import User
from .entity import Post
from .hub import hub, PostSubscriber, PostEvent

class PostNode(SQLAlchemyObjectType):
    class Meta:
        model = Post
        interfaces = (relay.Node, )

class PostConnection(relay.Connection):
    class Meta:
        node = PostNode

class PostInput(graphene.InputObjectType):
    title = graphene.String()
    block = graphene.String()
    body = graphene.String()

class CreatePost(graphene.Mutation):
    class Arguments:
        data = PostInput(required=True)

    id = graphene.ID()

    @staticmethod
    def mutate(self, info, data=None):
        user = load_user(info)
        user_id = user.id
        logger.debug('create post')
        logger.debug(f"user: {user}")
        post = Post(title=data.title, block=data.block, body=data.body, owner_id=user_id)
        db.session.add(post)
        db.session.commit()
        # db.session.flush()
        db.session.refresh(post)
        #logger.debug(post)
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
        logger.debug('update post')
        # get the JWT
        token = decode_auth_token(info.context)
        logger.debug(f"token: {token}")
        post = graphene.Node.get_node_from_global_id(info, id)
        #logger.debug(post)
        post.title = data.title
        post.block = data.block
        post.body = data.body
        db.session.commit()

        event = PostEvent(id, 'update')
        hub.send(event)

        ok = True
        return ok

class PublishPost(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        data = PostInput(required=True)
        
    ok = graphene.Boolean()

    @staticmethod
    def mutate(self, info, id, data):
        logger.debug('publish post')
        # get the JWT
        token = decode_auth_token(info.context)
        logger.debug(f"token: {token}")
        # post = Post.query.get(id)
        post = graphene.Node.get_node_from_global_id(info, id)
        #logger.debug(post)
        post.title = data.title
        post.block = data.block
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
        logger.debug('delete post')
        # get the JWT
        token = decode_auth_token(info.context)
        logger.debug(f"token: {token}")
        post = graphene.Node.get_node_from_global_id(info, id)
        #logger.debug(post)
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

    def resolve_post_by(self, info, slug):
        query = PostNode.get_query(info)  # SQLAlchemy query
        return query.filter_by(slug=slug).first()


class Subscription(graphene.ObjectType):
    post_events = graphene.Field(PostEvent, id=graphene.ID())
    def resolve_post_events(self, info, id=None):
        logger.debug('post events subscription')
        def push_post(observer):
            logger.debug('subscribe to post')
            subscriber = PostSubscriber(observer, id)
            hub.subscribe(subscriber)
        source = Observable.create(push_post)
        return source
