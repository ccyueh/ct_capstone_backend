"""empty message

Revision ID: 11b62f8ced57
Revises: 
Create Date: 2019-09-13 22:04:29.431277

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11b62f8ced57'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('profile_img', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_table('party',
    sa.Column('party_id', sa.Integer(), nullable=False),
    sa.Column('start', sa.DateTime(), nullable=True),
    sa.Column('end', sa.DateTime(), nullable=True),
    sa.Column('party_name', sa.String(length=100), nullable=True),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('voting', sa.Boolean(), nullable=True),
    sa.Column('reveal', sa.Boolean(), nullable=True),
    sa.Column('voting_end', sa.DateTime(), nullable=True),
    sa.Column('host_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['host_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('party_id')
    )
    op.create_table('bottle',
    sa.Column('bottle_id', sa.Integer(), nullable=False),
    sa.Column('producer', sa.String(length=100), nullable=True),
    sa.Column('bottle_name', sa.String(length=100), nullable=True),
    sa.Column('vintage', sa.Integer(), nullable=True),
    sa.Column('label_img', sa.String(length=100), nullable=True),
    sa.Column('party_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['party_id'], ['party.party_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('bottle_id')
    )
    op.create_table('party_guests',
    sa.Column('party_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['party_id'], ['party.party_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], )
    )
    op.create_table('rating',
    sa.Column('rating_id', sa.Integer(), nullable=False),
    sa.Column('stars', sa.Numeric(precision=2, scale=1), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('bottle_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bottle_id'], ['bottle.bottle_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('rating_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rating')
    op.drop_table('party_guests')
    op.drop_table('bottle')
    op.drop_table('party')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
