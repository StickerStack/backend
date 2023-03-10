from datetime import datetime

from sqlalchemy import (TIMESTAMP, Boolean, Column, Integer, MetaData, String,
                        Table)

metadata = MetaData()


user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column(
        'email', String(length=320),
        unique=True, index=True, nullable=False),
    Column('hashed_password', String(length=1024), nullable=False),
    Column('bio', String, nullable=True),
    Column('is_active', Boolean, default=True, nullable=False),
    Column('is_superuser', Boolean, default=False, nullable=False),
    Column('is_verified', Boolean, default=False, nullable=False),
    Column('added', TIMESTAMP, default=datetime.utcnow),
    Column('email_token', String, nullable=True)
)
