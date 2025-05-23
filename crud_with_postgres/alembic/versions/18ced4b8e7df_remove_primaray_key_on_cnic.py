"""Remove primaray key on cnic

Revision ID: 18ced4b8e7df
Revises: 1243f7973b6b
Create Date: 2025-05-14 15:11:30.020772

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '18ced4b8e7df'
down_revision: Union[str, None] = '1243f7973b6b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'name',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('users', 'role',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('users', 'gender',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    op.alter_column('users', 'date_of_birth',
               existing_type=sa.DATE(),
               type_=sa.String(length=25),
               nullable=False)
    op.alter_column('users', 'phone_no',
               existing_type=sa.VARCHAR(length=15),
               nullable=False)
    op.alter_column('users', 'cnic',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'cnic',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    op.alter_column('users', 'phone_no',
               existing_type=sa.VARCHAR(length=15),
               nullable=True)
    op.alter_column('users', 'date_of_birth',
               existing_type=sa.String(length=25),
               type_=sa.DATE(),
               nullable=True)
    op.alter_column('users', 'gender',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    op.alter_column('users', 'role',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('users', 'name',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    # ### end Alembic commands ###
