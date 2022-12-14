"""Add Product Table name products

Revision ID: c3e0103f3245
Revises: 690ed1dd46e8
Create Date: 2022-10-23 17:02:47.159195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3e0103f3245'
down_revision = '690ed1dd46e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('sku', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('measure', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], name='product_category_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='product_pkey')
    )
    # ### end Alembic commands ###
