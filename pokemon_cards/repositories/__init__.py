from typing import Optional, List, Dict, Any, Union

from sqlalchemy.orm import load_only

from flask_sqlalchemy import SQLAlchemy


class BaseRepository(object):
    """
    base class for all of the repos
    """

    def __init__(self, model):
        db = SQLAlchemy()
        self.db_session = db.session
        self.model = model

    def get_records(self, only: Optional[List[str]] = None):
        """
        Get all records of this model from database

        :param only:
        :return: record(s)
        """
        query = self.db_session.query(self.model)
        if only:
            query = query.options(load_only(*only))
        return query.all()

    def get_by_id(self, record_id: Union[int, str], only: Optional[List[str]] = None):
        """
        Get a record from database by id

        :param record_id:
        :param only:
        :return: id(s)
        """
        query = self.db_session.query(self.model).filter(self.model.id == record_id)
        if only:
            query = query.options(load_only(*only))
        return query.one_or_none()

    def create_record(self, create_data: Dict[str, Any], commit: bool = True):
        """
        Create a new record in database

        :param create_data:
        :param commit:
        :return: record
        """
        record = self.model(**create_data)
        self.db_session.add(record)
        if commit:
            self.db_session.commit()
        return record

    def bulk_create_records(self, create_data_list: List[Dict[str, Any]], commit: bool = True):
        """
        Bulk create data in one transaction
        """
        self.db_session.bulk_insert_mappings(self.model, create_data_list)
        if commit:
            self.db_session.commit()
        return None

    def update_record(self, record_id: Union[int, str], update_data: Dict[str, Any], commit: bool = True):
        """
        Update a record in database by id

        :param record_id:
        :param update_data:
        :param commit:
        :return: count (number of updated rows)
        """
        query = self.db_session.query(self.model).filter(self.model.id == record_id)
        count = query.update(update_data, synchronize_session=False)
        if commit:
            self.db_session.commit()
        return count

    def delete_record(self, record_id: Union[int, str], commit: bool = True):
        """
        Delete a record from database by id

        :param record_id:
        :param commit:
        :return: count (number of updated rows)
        """
        query = self.db_session.query(self.model).filter(self.model.id == record_id)
        count = query.delete(synchronize_session=False)
        if commit:
            self.db_session.commit()
        return count
