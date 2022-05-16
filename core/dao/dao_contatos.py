import json
from core.models.tb_contatos import TbContatos
from core.persist.persist import Database


class DAOContatos:
    """This class is a DAO to manipulate database.
    """

    def __init__(self) -> None:
        """New DAO Contatos."""
        TbContatos.create_table()

    def _selecter(self, data: tuple) -> dict:
        return {
            'id': data[0],
            'name': data[1],
            'email': data[2],
            'mobile': data[3],
            'info': data[4],
        }

    def _template(self, data: list, codes: int, msg: str) -> dict:
        return {'data': data, 'codes': codes, 'msg': msg}

    # create

    def create(self, **kwargs) -> json:
        """Create a new Contato.

        Returns:
            json: with code of error or success.
        """
        try:
            Database.open_it()
            created = (TbContatos.insert(**kwargs).execute())
            return json.dumps(
                {'codes': 201, 'msg': 'Success! Creeated a New Contact.'}
            ) if created.id > 0 else json.dumps(
                {'codes': 406, 'msg': 'Error! Invalid Datas.'}
            )
        finally:
            Database.close_it()

    # read all

    def read(self) -> json:
        """Read all Contatos.

        Returns:
            json: data return.
        """
        try:
            data = []
            Database.open_it()
            contatos = (TbContatos.select())
            if not contatos:
                return json.dumps(
                    self._template(data, 404, 'HTTP Error: Not Found.')
                )
            for contato in contatos:
                data.extend(self._selecter(data=contato))
            return json.dumps(
                self._template(data, 200, 'Success! All Contacts Found.')
            )
        finally:
            Database.close_it()

    # read by id

    def read_by_id(self, id: int) -> json:
        """Read Contato By Id.

        Args:
            id (int): Id data to search contato.

        Returns:
            json: json with the result.
        """
        try:
            data = self._template([], 0, '')
            Database.open_it()
            contatos = (TbContatos.select().where(TbContatos.id == id))
            if not contatos:
                data['codes'] = 404
                data['msg'] = 'HTTP Error: Not Found.'
            else:
                data['data'].append(self._selecter(data=contatos))
                data['codes'] = 200
                data['msg'] = 'Success! Contact Found.'
            return json.dumps(data)
        finally:
            Database.close_it()

    # read by name

    def read_by_name(self, name: str) -> json:
        """Read Contato By Id.

        Args:
            name (str): Contact Name..

        Returns:
            json: json with the result.
        """
        try:
            data = self._template([], 0, '')
            Database.open_it()
            contatos = (TbContatos.select().where(TbContatos.name == name))
            if not contatos:
                data['codes'] = 404
                data['msg'] = 'HTTP Error: Not Found.'
            else:
                data['data'].append(self._selecter(data=contatos))
                data['codes'] = 200
                data['msg'] = 'Success! Contact Found.'
            return json.dumps(data)
        finally:
            Database.close_it()

    # update

    def update(self, id: int, **kwargs) -> json:
        """Update a contact.

        Args:
            id (int): Make update search by id.

        Returns:
            json: data inserts to this json file.
        """
        try:
            data = self._template(None, 0, '')
            del data['data']
            Database.open_it()
            updated = (TbContatos.update(
                **kwargs).where(TbContatos.id == id).execute()
            )
            if updated < 1:
                data['msg'] = 'HTTPError: Not Updated.'
                data['codes'] = 404
            else:
                data['msg'] = 'Success! Contact Updated.'
                data['codes'] = 200
            return json.dumps(data)
        finally:
            Database.close_it()

    # delete

    def delete(self, id: int) -> json:
        """Delete Contato by id.

        Args:
            id (int): primary key.

        Returns:
            json: json with result.
        """
        try:
            data = self._template(None, 0, '')
            del data['data']
            Database.open_it()
            deleted = (TbContatos.delete().where(TbContatos.id == id))
            if not deleted:
                data['codes'] = 404
                data['msg'] = 'HTTP Error: Not Deleted.'
            else:
                data['codes'] = 200
                data['msg'] = 'Success! Contact Deleted.'
            return json.dumps(data)
        finally:
            Database.close_it()
