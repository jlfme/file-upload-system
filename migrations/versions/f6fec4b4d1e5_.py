"""empty message

Revision ID: f6fec4b4d1e5
Revises: 0e342384f562
Create Date: 2017-09-25 01:34:13.857660

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f6fec4b4d1e5'
down_revision = '0e342384f562'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('upload_picture',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file', sa.String(length=100), nullable=False),
    sa.Column('slug', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('picture')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('picture',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('file', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('slug', mysql.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('upload_picture')
    # ### end Alembic commands ###
