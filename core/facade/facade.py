import json
from core.models.contatos import Contatos
from core.service.service import Service


class Facade:
    """API Facade Access.
    """

    _service = Service()

    def __init__(self) -> None:
        """New Facade Contatos.
        """
        pass

    # contatos service

    def create_contato(self, contato: Contatos) -> json:
        """This method is for create a new Contato.

        Args:
            contato (Contatos): Json data object.

        Returns:
            json: data with result.
        """
        return self._service.create_contato(contato=contato)

    def read_all_contatos(self) -> json:
        """Get All Contacts.

        Returns:
            json: data inside json.
        """
        return self._service.read_all_contatos()

    def read_contato_by_id(self, id: int) -> json:
        """Get Contato By Id.

        Args:
            id (int): id to search Contato.

        Returns:
            json: data with result.
        """
        return self._service.read_contato_by_id(id=id)

    def read_contato_by_name(self, name: str) -> json:
        """Get Contato By Name.

        Args:
            name (str): name to search Contato.

        Returns:
            json: data with result.
        """
        return self._service.read_contato_by_name(name=name)

    def read_contato_by_tag(self, tag: str) -> json:
        """Get Contato By Name.

        Args:
            tag (str): tag to search Contatos.

        Returns:
            json: data with result.
        """
        return self._service.read_contato_by_tag(tag=tag)

    def update_contato(self, id: int, contato: Contatos) -> json:
        """Update a Contato.

        Args:
            id (int): Contato id.
            contato (Contatos): json representation.

        Returns:
            json: data with code and msg.
        """
        return self._service.update_contato(id=id, contato=contato)

    def delete_contato_by_id(self, id: int) -> json:
        """Delete Contato By Id.

        Args:
            id (int): id to search Contato.

        Returns:
            json: data with result.
        """
        return self._service.delete_contato_by_id(id=id)
