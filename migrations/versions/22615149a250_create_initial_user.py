"""create initial user

Revision ID: 22615149a250
Revises: 5675e877f170
Create Date: 2025-12-29 17:01:20.262603

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from app.core.security import get_password_hash
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Boolean


# revision identifiers, used by Alembic.
revision = "22615149a250"
down_revision= "5675e877f170"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    users_table = sa.table(
        "users",
        sa.column("id", sa.Integer),
        sa.column("username", sa.String),
        sa.column("email", sa.String),
        sa.column("password_hash", sa.String),
        sa.column("is_active", sa.Boolean),
    )

    op.bulk_insert(
        users_table,
        [
            {
                "id": 1,
                "username": "admin",
                "email": "admin@example.com",
                "password_hash": "$2b$12$jd91/zS1CugwLygbgdqls.rwP.H3ogkNoxjp78sDjZwkb7SZ8v2cG",
                "is_active": True,
            }
        ],
    )

def downgrade():
    op.execute("DELETE FROM users WHERE id = 1")




