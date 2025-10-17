"""add_verification_fields

Revision ID: add_verification_fields
Revises: 2f38a24fbd30
Create Date: 2025-10-12 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'add_verification_fields'
down_revision = '2f38a24fbd30'
branch_labels = None
depends_on = None


def upgrade():
    # Update StudentProfile
    with op.batch_alter_table('student_profiles') as batch_op:
        batch_op.add_column(sa.Column('verification_token',
                            sa.String(100), nullable=True))
        batch_op.add_column(
            sa.Column('verification_sent_at', sa.DateTime(), nullable=True))
        batch_op.add_column(
            sa.Column('verified_at', sa.DateTime(), nullable=True))
        batch_op.alter_column('student_id',
                              existing_type=mysql.VARCHAR(20),
                              nullable=True)
        batch_op.alter_column('school_name',
                              existing_type=mysql.VARCHAR(100),
                              nullable=True)
        batch_op.drop_column('grade_level')
        batch_op.add_column(sa.Column('kelas', sa.String(10), nullable=False))

    # Update TeacherProfile
    with op.batch_alter_table('teacher_profiles') as batch_op:
        batch_op.add_column(sa.Column('verification_token',
                            sa.String(100), nullable=True))
        batch_op.add_column(
            sa.Column('verification_sent_at', sa.DateTime(), nullable=True))
        batch_op.add_column(
            sa.Column('verified_at', sa.DateTime(), nullable=True))
        batch_op.alter_column('school_name',
                              existing_type=mysql.VARCHAR(100),
                              nullable=True)
        batch_op.drop_column('teacher_id')
        batch_op.add_column(sa.Column('nip', sa.String(18), nullable=False))
        batch_op.add_column(
            sa.Column('mata_pelajaran', sa.String(50), nullable=False))


def downgrade():
    # Revert StudentProfile changes
    with op.batch_alter_table('student_profiles') as batch_op:
        batch_op.drop_column('verification_token')
        batch_op.drop_column('verification_sent_at')
        batch_op.drop_column('verified_at')
        batch_op.alter_column('student_id',
                              existing_type=mysql.VARCHAR(20),
                              nullable=False)
        batch_op.alter_column('school_name',
                              existing_type=mysql.VARCHAR(100),
                              nullable=False)
        batch_op.drop_column('kelas')
        batch_op.add_column(
            sa.Column('grade_level', sa.String(10), nullable=False))

    # Revert TeacherProfile changes
    with op.batch_alter_table('teacher_profiles') as batch_op:
        batch_op.drop_column('verification_token')
        batch_op.drop_column('verification_sent_at')
        batch_op.drop_column('verified_at')
        batch_op.alter_column('school_name',
                              existing_type=mysql.VARCHAR(100),
                              nullable=False)
        batch_op.drop_column('nip')
        batch_op.drop_column('mata_pelajaran')
        batch_op.add_column(
            sa.Column('teacher_id', sa.String(20), nullable=False))
