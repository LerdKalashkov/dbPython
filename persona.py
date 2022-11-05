import logging as log
class Persona:
    def __init__(self, id_persona, nombre, apellido, email) -> None:
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def __str__(self) -> str:
        return f'''
        ID: {self._id_persona}, 
        Nombre: {self._nombre}, 
        Apellido: {self._apellido}, 
        Email: {self._email},
        '''
        
    #ID

    @property
    def id_persona(self):
        return self._id_persona 

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    #nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    #apellido

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    
    #email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

if __name__ == '__main__':

    persona0 = Persona(0, 'Jose', 'Fernandez', 'example@mail.com')
    print(persona0)
    log.debug(persona0)
    