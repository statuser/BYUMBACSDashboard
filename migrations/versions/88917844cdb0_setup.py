"""Setup

Revision ID: 88917844cdb0
Revises: 
Create Date: 2021-12-14 16:58:33.275228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88917844cdb0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('address1', sa.String(length=128), nullable=True),
    sa.Column('address2', sa.String(length=128), nullable=True),
    sa.Column('city', sa.String(length=64), nullable=True),
    sa.Column('state', sa.String(length=64), nullable=True),
    sa.Column('zipCode', sa.String(length=64), nullable=True),
    sa.Column('country', sa.String(length=64), nullable=True),
    sa.Column('numberEmployees', sa.Integer(), nullable=True),
    sa.Column('relationship', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_roles_name'), ['name'], unique=True)

    op.create_table('advocate',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('companyId', sa.Integer(), nullable=False),
    sa.Column('firstName', sa.String(length=128), nullable=True),
    sa.Column('lastName', sa.String(length=128), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('linkedin', sa.String(length=128), nullable=True),
    sa.Column('phone', sa.String(length=16), nullable=True),
    sa.Column('numberHelped', sa.Integer(), nullable=True),
    sa.Column('companyStart', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['companyId'], ['company.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    op.create_table('company_note',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('companyId', sa.Integer(), nullable=False),
    sa.Column('author', sa.Integer(), nullable=False),
    sa.Column('noteType', sa.String(length=64), nullable=True),
    sa.Column('note', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['author'], ['user.id'], ),
    sa.ForeignKeyConstraint(['companyId'], ['company.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstName', sa.String(length=128), nullable=True),
    sa.Column('middleName', sa.String(length=128), nullable=True),
    sa.Column('lastName', sa.String(length=128), nullable=True),
    sa.Column('studentEmail', sa.String(length=128), nullable=True),
    sa.Column('phone', sa.String(length=16), nullable=True),
    sa.Column('classYear', sa.String(length=4), nullable=True),
    sa.Column('linkedIn', sa.String(length=128), nullable=True),
    sa.Column('intent', sa.String(length=128), nullable=True),
    sa.Column('attitude', sa.String(length=128), nullable=True),
    sa.Column('photo', sa.LargeBinary(), nullable=True),
    sa.Column('lastUpdate', sa.DateTime(), nullable=True),
    sa.Column('jobStatus', sa.String(length=64), nullable=True),
    sa.Column('createdDate', sa.DateTime(), nullable=True),
    sa.Column('userID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['userID'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('education',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('studentId', sa.Integer(), nullable=True),
    sa.Column('school', sa.String(length=128), nullable=True),
    sa.Column('startDate', sa.DateTime(), nullable=True),
    sa.Column('endDate', sa.DateTime(), nullable=True),
    sa.Column('degree', sa.String(length=64), nullable=True),
    sa.Column('program', sa.String(length=64), nullable=True),
    sa.Column('gpa', sa.Float(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['studentId'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('info_interview',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('studentId', sa.Integer(), nullable=False),
    sa.Column('companyId', sa.Integer(), nullable=True),
    sa.Column('advocateId', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('helpful', sa.String(length=10), nullable=True),
    sa.Column('gaveRef', sa.Boolean(), nullable=True),
    sa.Column('note', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['advocateId'], ['advocate.id'], ),
    sa.ForeignKeyConstraint(['companyId'], ['company.id'], ),
    sa.ForeignKeyConstraint(['studentId'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('job_application',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('studentId', sa.Integer(), nullable=False),
    sa.Column('companyId', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('position', sa.String(length=128), nullable=True),
    sa.Column('interestLevel', sa.Integer(), nullable=True),
    sa.Column('confidenceLevel', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['companyId'], ['company.id'], ),
    sa.ForeignKeyConstraint(['studentId'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('job_offer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('studentId', sa.Integer(), nullable=False),
    sa.Column('companyId', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('position', sa.String(length=128), nullable=True),
    sa.Column('interestLevel', sa.Integer(), nullable=True),
    sa.Column('compensation', sa.Float(), nullable=True),
    sa.Column('bonus', sa.Float(), nullable=True),
    sa.Column('movingExpenses', sa.Boolean(), nullable=True),
    sa.Column('stockOptions', sa.Boolean(), nullable=True),
    sa.Column('totalPackage', sa.Float(), nullable=True),
    sa.Column('intention', sa.String(length=32), nullable=True),
    sa.ForeignKeyConstraint(['companyId'], ['company.id'], ),
    sa.ForeignKeyConstraint(['studentId'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lamp_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('companyId', sa.Integer(), nullable=True),
    sa.Column('studentId', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['companyId'], ['company.id'], ),
    sa.ForeignKeyConstraint(['studentId'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mock_interview',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('studentId', sa.Integer(), nullable=False),
    sa.Column('companyId', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('position', sa.String(length=128), nullable=True),
    sa.Column('interviewerName', sa.String(length=128), nullable=True),
    sa.Column('note', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['companyId'], ['company.id'], ),
    sa.ForeignKeyConstraint(['studentId'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('real_interview',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('studentId', sa.Integer(), nullable=False),
    sa.Column('companyId', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('round', sa.String(length=10), nullable=True),
    sa.Column('offerConfidence', sa.Integer(), nullable=True),
    sa.Column('position', sa.String(length=128), nullable=True),
    sa.Column('note', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['companyId'], ['company.id'], ),
    sa.ForeignKeyConstraint(['studentId'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('resume',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('studentId', sa.Integer(), nullable=True),
    sa.Column('companyId', sa.Integer(), nullable=True),
    sa.Column('startDate', sa.DateTime(), nullable=True),
    sa.Column('endDate', sa.DateTime(), nullable=True),
    sa.Column('jobTitle', sa.String(length=128), nullable=True),
    sa.Column('compensation', sa.String(length=32), nullable=True),
    sa.Column('duties', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['companyId'], ['company.id'], ),
    sa.ForeignKeyConstraint(['studentId'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student_note',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('studentId', sa.Integer(), nullable=False),
    sa.Column('author', sa.Integer(), nullable=False),
    sa.Column('noteType', sa.String(length=64), nullable=True),
    sa.Column('note', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author'], ['user.id'], ),
    sa.ForeignKeyConstraint(['studentId'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student_note')
    op.drop_table('resume')
    op.drop_table('real_interview')
    op.drop_table('mock_interview')
    op.drop_table('lamp_list')
    op.drop_table('job_offer')
    op.drop_table('job_application')
    op.drop_table('info_interview')
    op.drop_table('education')
    op.drop_table('student')
    op.drop_table('company_note')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    op.drop_table('advocate')
    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_roles_name'))

    op.drop_table('roles')
    op.drop_table('company')
    # ### end Alembic commands ###