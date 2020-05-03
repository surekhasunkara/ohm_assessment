"""update point location and tiers

Revision ID: 1b26ac146d11
Revises: 00000000
Create Date: 2020-05-02 16:41:27.091238

"""

# revision identifiers, used by Alembic.
revision = '1b26ac146d11'
down_revision = '00000000'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.execute('''UPDATE user 
            SET point_balance = 5000
            WHERE user_id = 1
        ''')

    op.execute('''INSERT INTO rel_user 
            (user_id, rel_lookup, attribute)
            VALUES (2, 'LOCATION', 'USA')
            ''')

    op.execute('''UPDATE user 
                SET tier = 'Silver'
                WHERE user_id = 3
            ''')


def downgrade():
    pass
