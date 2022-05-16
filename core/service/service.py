import json
from core.dao.dao_contatos import DAOContatos
from core.models.tb_contatos import TbContatos
from core.models.contatos import Contatos


class Service:
    """This class is for check data, if it be a success,
    go to dao and try do persist, else, return an error.
    """

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
        pass

    def read_all_contatos(self) -> json:
        """Get All Contacts.

        Returns:
            json: data inside json.
        """
        pass

    def read_contato_by_id(self, id: int) -> json:
        """Get Contato By Id.

        Args:
            id (int): id to search Contato.

        Returns:
            json: data with result.
        """
        pass

    def read_contato_by_name(self, name: str) -> json:
        """Get Contato By Name.

        Args:
            name (str): name to search Contato.

        Returns:
            json: data with result.
        """
        pass

    def read_contato_by_tag(self, tag: str) -> json:
        """Get Contato By Name.

        Args:
            tag (str): tag to search Contatos.

        Returns:
            json: data with result.
        """
        pass

    def update_contato(self, id: int, contato: Contatos) -> json:
        """Update a Contato.

        Args:
            id (int): Contato id.
            contato (Contatos): json representation.

        Returns:
            json: data with code and msg.
        """
        pass

    def delete_contato_by_id(self, id: int) -> json:
        """Delete Contato By Id.

        Args:
            id (int): id to search Contato.

        Returns:
            json: data with result.
        """
        pass
