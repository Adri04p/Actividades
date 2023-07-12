# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 22:20:48 2023

@author: SYSTEMarket
"""

# Definición de excepción personalizada
class MovimientoInvalidoError(Exception):
    def __init__(self, comando):
        self.comando = comando

    def __str__(self):
        return f"El comando de movimiento '{self.comando}' es inválido"


# Clase Robot
class Robot:
    def __init__(self, posicion_x, posicion_y):
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y


# Clase ControladorRobot
class ControladorRobot:
    def crear_robot(self, posicion_x, posicion_y):
        return Robot(posicion_x, posicion_y)

    def mover_robot(self, robot, comando):
        if comando == "adelante":
            robot.posicion_y += 1
        elif comando == "atrás":
            robot.posicion_y -= 1
        elif comando == "izquierda":
            robot.posicion_x -= 1
        elif comando == "derecha":
            robot.posicion_x += 1
        elif comando == "salir":
            raise SystemExit
        else:
            raise MovimientoInvalidoError(comando)

        if not self._es_movimiento_valido(robot):
            raise MovimientoInvalidoError(comando)

    def _es_movimiento_valido(self, robot):
        return -1 <= robot.posicion_x <= 1 and -1 <= robot.posicion_y <= 1


# Clase VistaRobot
class VistaRobot:
    def solicitar_comando(self):
        return input("Ingrese un comando de movimiento para el robot: ")

    def mostrar_error(self, mensaje):
        print("¡Error:", mensaje, "!")


# Clase AplicacionRobot
class AplicacionRobot:
    def iniciar(self):
        controlador = ControladorRobot()
        vista = VistaRobot()

        robot = controlador.crear_robot(0, 0)

        while True:
            comando = vista.solicitar_comando()

            try:
                controlador.mover_robot(robot, comando)
            except MovimientoInvalidoError as error:
                vista.mostrar_error(str(error))
            except SystemExit:
                break
            else:
                print("El robot se mueve a la posición ({}, {}).".format(robot.posicion_x, robot.posicion_y))


# Bloque principal
if __name__ == "__main__":
    aplicacion = AplicacionRobot()
    aplicacion.iniciar()
