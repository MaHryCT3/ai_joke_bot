from app.db.engine import engine
from app.db.mappers import start_mapping_table_from_domain
from app.db.models.base import BaseModel


start_mapping_table_from_domain()


# Создание таблиц
BaseModel.metadata.create_all(engine)
