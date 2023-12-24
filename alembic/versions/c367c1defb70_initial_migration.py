"""initial migration

Revision ID: c367c1defb70
Revises: 
Create Date: 2023-12-16 23:22:56.736389

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from app.database import db

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
    #op.execute(query)

    query = '''
        CREATE TABLE `apps` (
            `id` INT NOT NULL,
            `name` VARCHAR(255) NOT NULL,
            `key` VARCHAR(255) NOT NULL,
            `is_active` TINYINT(1) NOT NULL,
        PRIMARY KEY (`id`));
    '''
    #op.execute(query)
    
    query = '''
        CREATE TABLE `tokens` (
            `id` INT NOT NULL,
            `app` INT NOT NULL,
            `user` INT NOT NULL,
            `device` VARCHAR(255) NOT NULL,
            `token` VARCHAR(255) NOT NULL,
            `dt_create` DATETIME NOT NULL,
            `dt_update` DATETIME NULL,
            `lifetime_in_hours` INT NULL,
        PRIMARY KEY (`id`));
    '''
    #op.execute(query)
    
    # 

    query = '''
        CREATE TABLE `groups` (
            `id` INT NOT NULL AUTO_INCREMENT,
            `alias` VARCHAR(255) NOT NULL,
            `name` VARCHAR(255) NOT NULL,
            `description` TINYTEXT NOT NULL,
            `image` VARCHAR(255) NULL,
            `creator` INT NOT NULL,
            `language` VARCHAR(255) NULL,
            `is_public` TINYINT(1) NOT NULL,
            `is_auto_acceptable` TINYINT(1) NOT NULL,
            `is_raiting` TINYINT(1) NOT NULL,
            `is_archive` TINYINT(1) NOT NULL,
            `country` INT NOT NULL,
            `region` INT NULL,
            `city` INT NULL,
            `address` VARCHAR(255) NULL,
            `link_code` VARCHAR(255) NULL,
        PRIMARY KEY (`id`),
        UNIQUE INDEX `alias_UNIQUE` (`alias` ASC) VISIBLE);
    '''
    #op.execute(query)

    query = '''
        INSERT INTO `apps` 
            (`id`, `name`, `key`, `is_active`) 
        VALUES 
            ('10', 'iPhone client', '123123', '1'),
            ('20', 'Android client', '456456', '1'),
            ('30', 'Web client', '789789', '1'),
            ('40', 'Web admin', '000000', '1');
    '''
    op.execute(query)
    
def downgrade() -> None:
    pass
