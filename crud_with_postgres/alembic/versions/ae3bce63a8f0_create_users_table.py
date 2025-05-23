"""create users table

Revision ID: ae3bce63a8f0
Revises: 
Create Date: 2025-05-13 10:53:24.435803

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ae3bce63a8f0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('role', sa.String(length=50), nullable=False),
    sa.Column('skills', sa.String(length=100), nullable=True),
    sa.Column('course', sa.String(length=50), nullable=True),
    sa.Column('gender', sa.String(length=20), nullable=False),
    sa.Column('date_of_birth', sa.String(length=25), nullable=False),
    sa.Column('phone_no', sa.String(length=15), nullable=False),
    sa.Column('address', sa.Text(), nullable=True),
    sa.Column('qualification', sa.String(length=50), nullable=True),
    sa.Column('cnic', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id', 'cnic'),
    sa.UniqueConstraint('cnic'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
