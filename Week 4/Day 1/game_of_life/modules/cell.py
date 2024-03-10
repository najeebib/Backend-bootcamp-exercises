class Cell:
    def __init__(self, status: str, position: tuple) -> None:
        """ Construct a class 'Cell <Cell>' 
        
        :param staus: an integer that represents the status of the cell (alive or dead)
        :param position: a tuple that has the position of the cell on the board (the board is a 2d list)

        """
        self._status = status
        self._position = position

    def get_status(self):
        """ Return the status value """
        return self._status
    
    def get_position(self):
        """ Return the position value """
        return self._position
    
    def change_status(self, status):
        """ Change the status value

        :param status: the new status which will be put as the value 
        """
        self._status = status