"""Empty Init

Revision ID: 1bfcc5a180bc
Revises: cfe32a234d14
Create Date: 2025-12-30 10:19:19.355854

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1bfcc5a180bc'
down_revision: Union[str, None] = 'cfe32a234d14'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
