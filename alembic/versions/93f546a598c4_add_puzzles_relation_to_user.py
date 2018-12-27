"""add puzzles relation to user

Revision ID: 93f546a598c4
Revises: 
Create Date: 2018-12-26 15:31:29.085295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93f546a598c4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("puzzles", sa.Column('user_id', sa.Integer()))
    op.create_foreign_key("fk_user_puzzle", "puzzles",
                          "users", ["user_id"], ["id"])


def downgrade():
    op.drop_column("puzzles", "user_id")
