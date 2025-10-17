"""add_reset_password_fields

Revision ID: add_reset_password_fields
Revises: add_verification_fields
Create Date: 2025-10-12 10:30:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'add_reset_password_fields'
down_revision = 'add_verification_fields'
branch_labels = None
depends_on = None


def upgrade():
    # Add reset password fields to users table
    with op.batch_alter_table('users') as batch_op:
        batch_op.add_column(
            sa.Column('reset_token', sa.String(100), nullable=True))
        batch_op.add_column(sa.Column('reset_token_sent_at',
                            sa.DateTime(), nullable=True))
        batch_op.create_unique_constraint(
            'uq_users_reset_token', ['reset_token'])


def downgrade():
    # Remove reset password fields from users table
    with op.batch_alter_table('users') as batch_op:
        batch_op.drop_constraint('uq_users_reset_token', type_='unique')
        batch_op.drop_column('reset_token')
        batch_op.drop_column('reset_token_sent_at')
