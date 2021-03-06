import json
from loguru import logger
import graphene
from graphene import relay
from graphql_relay import to_global_id
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from __blogsley__ import db, iam
from .entity import User
from blogsley_flask.post import Post

from blogsley_flask.jwt import encode_auth_token, decode_auth_token

class UserNode(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node, )

class UserConnection(relay.Connection):
    class Meta:
        node = UserNode

class UserInput(graphene.InputObjectType):
    username = graphene.String()
    email = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()
    password = graphene.String()

class LoginInput(graphene.InputObjectType):
    username = graphene.String()
    password = graphene.String()

class Login(graphene.Mutation):
    class Arguments:
        data = LoginInput(required=True)

    token = graphene.String()

    @staticmethod
    def mutate(self, info, data=None):
        username=data.username
        password=data.password

        logger.info(f"login: {username}, {password}")

        if not username:
            raise Exception('Username missing!')
        if not password:
            raise Exception('Password missing!')

        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            raise Exception('No such user or invalid password!')

        access_token = encode_auth_token(sub=username, id=user.id, role=user.role)
        token = access_token.decode('utf-8')
        logger.info(f"token: {token}")
        return Login(token=token)

class CreateUser(graphene.Mutation):
    class Arguments:
        data = UserInput(required=True)

    id = graphene.ID()

    @staticmethod
    @iam.needs('Admin')
    def mutate(self, info, data=None):
        print('CreateUser')
        user = User(
            username=data.username,
            email=data.email,
            first_name=data.first_name,
            last_name=data.last_name,
            # role='Reader',
            # about_me='I am a Reader'
        )
        user.set_password(data.password)
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
        id = to_global_id(UserNode._meta.name, user.id)
        return CreateUser(id=id)

class UpdateUser(graphene.Mutation):
    class Arguments:
        _id = graphene.ID(required=True)
        data = UserInput(required=True)

    ok = graphene.Boolean()

    @staticmethod
    @iam.needs('Admin')
    def mutate(self, info, _id, data=None):
        user = graphene.Node.get_node_from_global_id(info, _id)
        logger.debug(f"user: {user}")
        user.username = data.username
        user.email = data.email
        user.save()
        ok = True

        return ok

class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @staticmethod
    @iam.needs('Admin')
    def mutate(self, info, id):
        user = graphene.Node.get_node_from_global_id(info, id)
        logger.debug(f"user: {user}")
        db.session.delete(user)
        db.session.commit()
        ok = True

        return ok

class Mutation(graphene.ObjectType):
    login = Login.Field()
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

class Query(graphene.ObjectType):
    user = relay.Node.Field(UserNode)
    all_users = SQLAlchemyConnectionField(UserConnection)
