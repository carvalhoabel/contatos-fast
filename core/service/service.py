import json
from unicodedata import name
from core.dao.dao_contatos import DAOContatos
from core.models.contatos import Contatos
from core.utils.validators import (
    check_email, valid_chars, str_len, mobile_checker
)


class Service:
    """This class is for check data, if it be a success,
    go to dao and try do persist, else, return an error.
    """

    # checkrs functions
    checkes = {
        'check_email': check_email,
        'valid_chars': valid_chars,
        'str_len': str_len,
        'mobile_checker': mobile_checker,
    }

    def __init__(self) -> None:
        """New Contatos Service.
        """
        self._daocontatos = DAOContatos()

    @property
    def daocontatos(self) -> DAOContatos:
        return self._daocontatos

    def create_contato(self, contato: Contatos) -> json:
        """This method is for create a new Contato.

        Args:
            contato (Contatos): Json data object.

        Returns:
            json: data with result.
        """
        create = self._check_create_update(contato=contato)
        create = json.loads(create)
        if create['codes'] != 200:
            return json.dumps(create)
        else:
            return self.daocontatos.create(
                name=contato.name,
                email=contato.email,
                mobile=contato.mobile,
                tag=contato.tag,
            )

    def read_all_contatos(self) -> json:
        """Get All Contacts.

        Returns:
            json: data inside json.
        """
        return self.daocontatos.read()

    def read_contato_by_id(self, id: int) -> json:
        """Get Contato By Id.

        Args:
            id (int): id to search Contato.

        Returns:
            json: data with result.
        """
        try:
            id = int(id)
        except ValueError:
            return self._simple_json(406, 'Search Error: id must be numeric.')
        return self.daocontatos.read_by_id(id=id)

    def read_contato_by_name(self, name: str) -> json:
        """Get Contato By Name.

        Args:
            name (str): name to search Contato.

        Returns:
            json: data with result.
        """
        if not isinstance(name, str):
            return self._simple_json(406, 'Error: name must be string.')
        return self.daocontatos.read_by_name(name=name)

    def read_contato_by_tag(self, tag: str) -> json:
        """Get Contato By Name.

        Args:
            tag (str): tag to search Contatos.

        Returns:
            json: data with result.
        """
        if not isinstance(tag, str):
            return self._simple_json(406, 'Error: tag must be string.')
        return self.daocontatos.read_by_tag(tag=tag)

    def update_contato(self, id: int, contato: Contatos) -> json:
        """Update a Contato.

        Args:
            id (int): Contato id.
            contato (Contatos): json representation.

        Returns:
            json: data with code and msg.
        """
        try:
            id = int(id)
        except ValueError:
            return self._simple_json(406, 'Update Error: id must be numeric.')
        update = self._check_create_update(contato=contato)
        update = json.loads(update)
        if update['codes'] != 200:
            return json.dumps(update)
        else:
            return self.daocontatos.update(
                name=contato.name,
                email=contato.email,
                mobile=contato.mobile,
                tag=contato.tag,
            )

    def delete_contato_by_id(self, id: int) -> json:
        """Delete Contato By Id.

        Args:
            id (int): id to search Contato.

        Returns:
            json: data with result.
        """
        try:
            id = int(id)
        except ValueError:
            return self._simple_json(406, 'Delete Error: id must be numeric.')
        return self.daocontatos.delete(id=id)

    # auxiliary methods ++++++++++++++++++++++++++++++++++++++++++++++++

    def _check_create_update(self, contato: Contatos) -> json:
        """This method is a central manager to check data to
        save and update methods.

        Args:
            contato (Contatos): instance with required data.

        Returns:
            json: json with code and msg.
        """
        # required function to sent as data
        def space(wd: str):
            return ' ' == wd
        funcs = (str.isalpha, space)
        funcs = (_ for _ in funcs)
        if not isinstance(contato, Contatos):
            return self._simple_json(codes=406, msg=' error: invalid contato instance.')
        elif not self.checkes['str_len'](contato.name, 80):
            return self._simple_json(codes=406, msg=' error: invalid name lenght.')
        elif not self.checkes['valid_chars'](contato.name, funcs):
            return self._simple_json(codes=406, msg=' error: invalid name character')
        elif not self.checkes['check_email'](contato.email):
            return self._simple_json(codes=406, msg=' error: invalid email.')
        elif not self.checkes['mobile_checker'](contato.mobile):
            return self._simple_json(codes=406, msg=' error: invalid mobile number.')
        elif not self.checkes['str_len'](contato.tag, 255, null=True):
            return self._simple_json(codes=406, msg=' error: invalid tag.')
        else:
            return self._simple_json(codes=200, msg='Success!')

    def _simple_json(self, codes: int, msg: str) -> json:
        """Simple json method return.

        Args:
            codes (int): status codes.
            msg (str): msg.

        Returns:
            json: json with information.
        """
        if not isinstance(codes, int) and not isinstance(msg, str):
            msg, codes = '', 0
        return json.dumps(
            {
                'codes': codes,
                'msg': msg
            }
        )
