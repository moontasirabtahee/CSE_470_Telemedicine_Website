"""feedback

Revision ID: 0107de9e4473
Revises: 
Create Date: 2024-05-02 14:59:33.750644

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0107de9e4473'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('appointment')
    with op.batch_alter_table('appointments', schema=None) as batch_op:
        batch_op.alter_column('status',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appointments', schema=None) as batch_op:
        batch_op.alter_column('status',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)

    op.create_table('appointment',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('doctor_id', sa.INTEGER(), nullable=False),
    sa.Column('patient_id', sa.INTEGER(), nullable=False),
    sa.Column('date', sa.DATE(), nullable=False),
    sa.Column('time', sa.TIME(), nullable=False),
    sa.Column('status', sa.VARCHAR(length=64), nullable=True),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctors.id'], ),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
