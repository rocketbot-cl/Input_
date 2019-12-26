# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import pyautogui as pag

"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module")


if module == "sendText":
    text_ = GetParams('text_')
    title_ = GetParams('title_')
    var_ = GetParams('var_')

    text = pag.prompt(text=text_, title=title_)

    SetVar(var_,text)

