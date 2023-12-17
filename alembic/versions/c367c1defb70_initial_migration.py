"""initial migration

Revision ID: c367c1defb70
Revises: 
Create Date: 2023-12-16 23:22:56.736389

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c367c1defb70'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    query = '''
        CREATE TABLE `users` (
            `id` INT NOT NULL AUTO_INCREMENT,
            `email` VARCHAR(255) NOT NULL,
            `is_email_verified` TINYINT(1) NOT NULL,
            `name` VARCHAR(255) NULL,
            `password` VARCHAR(255) NOT NULL,
            `is_active` TINYINT(1) NOT NULL,
            `is_superuser` TINYINT(1) NOT NULL,
            `about_me` TINYTEXT NULL,
            `image` VARCHAR(255) NULL,
            `last_language` VARCHAR(45) NULL,
            `dt_registration` DATETIME NOT NULL,
            `progress_dt_start` DATETIME NULL,
            `progress_dt_update` DATETIME NULL,
            `hidden_admin_comment` VARCHAR(255) NULL,
        PRIMARY KEY (`id`));
    '''


def downgrade() -> None:
    pass
