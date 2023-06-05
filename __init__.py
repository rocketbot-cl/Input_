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
import os
import sys

base_path = tmp_global_obj["basepath"]
cur_path = os.path.join(base_path, 'modules', 'Input_', 'libs')

cur_path_x64 = os.path.join(cur_path, 'Windows' + os.sep +  'x64' + os.sep)
cur_path_x86 = os.path.join(cur_path, 'Windows' + os.sep +  'x86' + os.sep)

if sys.maxsize > 2**32 and cur_path_x64 not in sys.path:
        sys.path.append(cur_path_x64)
if sys.maxsize > 32 and cur_path_x86 not in sys.path:
        sys.path.append(cur_path_x86)

import tkinter as tk
import r_pyautogui as pag


def crear_ventana(text, titulo):
    # Crear la ventana
    ventana = tk.Tk()
    ventana.title(titulo)
    ventana.geometry("400x100")  # Establecer tamaño de la ventana

    # Crear label
    label = tk.Label(ventana, text=text)
    label.pack()

    # Crear el cuadro de texto
    cuadro_texto = tk.Text(ventana, width=30, height=2)
    cuadro_texto.pack()
    

    # Crear el botón de aceptar
    def aceptar():
        global mod_input_texto
        mod_input_texto = cuadro_texto.get(1.0, tk.END)  # Obtener el texto del cuadro
        ventana.destroy()  # Cerrar la ventana
        

    boton_aceptar = tk.Button(ventana, text="Aceptar", command=aceptar)
    boton_aceptar.pack()

    # Mostrar la ventana
    ventana.focus_force()
    ventana.mainloop()

"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module")


if module == "sendText":
    text_ = GetParams('text_')
    title_ = GetParams('title_')
    var_ = GetParams('var_')

    try:
        text = pag.prompt(text=text_, title=titlee_)
        SetVar(var_,text)
    except:
        print("trying second method")
        mod_input_texto = None
    
        crear_ventana(text_, title_)
        try:
            lineas = mod_input_texto.split("\n")
            lineas = lineas[:-1]
            text = "\n".join(lineas)
            SetVar(var_, text)
        except AttributeError as e:
            print(e)
            SetVar(var_, mod_input_texto)
            

    
if module == "sendText2":
    text_ = GetParams('text_')
    title_ = GetParams('title_')
    var_ = GetParams('var_')
    
    mod_input_texto = None
    
    crear_ventana(text_, title_)
    try:
        lineas = mod_input_texto.split("\n")
        lineas = lineas[:-1]
        result = "\n".join(lineas)
        SetVar(var_, result)
    except Exception as e:
        print(e)
        SetVar(var_, mod_input_texto)

