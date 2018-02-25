"""Add two columns

Revision ID: 7140a89f902c
Revises: 
Create Date: 2018-02-25 14:22:50.658704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7140a89f902c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('songs',sa.Column('created_at',sa.DateTime))
    op.add_column('songs',sa.Column('updated_at',sa.DateTime))


def downgrade():
    pass
