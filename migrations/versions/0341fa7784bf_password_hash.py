"""password hash

Revision ID: 0341fa7784bf
Revises: e22c6b3be382
Create Date: 2019-04-24 15:53:25.114517

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0341fa7784bf'
down_revision = 'e22c6b3be382'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=255), nullable=True))
    op.drop_column('users', 'password_secure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###