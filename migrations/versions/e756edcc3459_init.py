"""init

Revision ID: e756edcc3459
Revises: 
Create Date: 2023-03-04 22:23:02.286134

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e756edcc3459'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('poster_name', sa.String(length=100), nullable=False),
    sa.Column('poster_avatar', sa.String(length=256), nullable=True),
    sa.Column('pic', sa.String(length=256), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('views_count', sa.Integer(), nullable=True),
    sa.Column('likes_count', sa.Integer(), nullable=True),
    sa.Column('comment_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('pk')
    )
    op.create_table('comment',
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('commenter_name', sa.String(length=100), nullable=False),
    sa.Column('comment', sa.String(length=256), nullable=True),
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.pk'], ),
    sa.PrimaryKeyConstraint('pk')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    op.drop_table('post')
    # ### end Alembic commands ###
