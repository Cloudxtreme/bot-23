from sqlalchemy import (
    Table,
    Column,
    ForeignKey,
    Index,
    Integer,
    Text,
    String,
    DateTime,
)

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
    backref,
)

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

group_permissions = Table('group_permissions', Base.metadata,
                          Column('group_id', Integer, ForeignKey('group.id')),
                          Column('permission_id', Integer,
                                 ForeignKey('permission.id'))
                         )


class Permission(Base):
    'List of permissions for groups'
    __tablename__ = 'permission'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Permission({})>'.format(self.name)


class Group(Base):
    'List of group of users'
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    permissions = relationship('Permission',
                               secondary=group_permissions,
                               backref='goups')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Group({})>'.format(self.name)


class User(Base):
    'List of users'
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    login = Column(String(50), unique=True)
    password = Column(Text, nullable=False)
    group_id = Column(Integer, ForeignKey('group.id'))
    group = relationship('Group', backref=backref('users', order_by=login))

    def __init__(self, login):
        self.login = login

    def __repr__(self):
        return '<User({})>'.format(self.login)


class TwitterAccount(Base):
    'List of twitter accounts'
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    login = Column(String(20), unique=True)

    def __init__(self, login):
        self.login = login

    def __repr__(self):
        return '<TwitterAccount({})>'.format(self.login)


class Tweet(Base):
    'List of tweets'
    __tablename__ = 'tweet'
    id = Column(Integer, primary_key=True)
    text = Column(String(140), nullable=False)
    account_id = Column(Integer, ForeignKey('account.id'))
    account = relationship('TwitterAccount',
                           backref=backref('tweets', order_by=id))
    send_again = Column(DateTime)

    def __init__(self, text, account):
        self.text = text[:140]
        self.account = account

    def __repr__(self):
        return '<Tweet(id={0}, account={1})>'.format(self.id,
                                                     self.account.login)
