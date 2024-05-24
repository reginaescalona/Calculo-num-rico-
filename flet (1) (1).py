import funciones # type: ignore
import numpy as np
import flet as ft


def main(pagina: ft.Page):

    def calcular_GaussJordan(e): 
        cadena=fila2_tab1.controls[0].value.replace(" ", "")
        if(funciones.verificar_digitos(cadena) and funciones.verificar_combinaciones_invalidas(cadena) and funciones.formateo(cadena) and funciones.iguales(cadena)  and funciones.es_cuadrada(cadena)):
                
                a = np.array(funciones.sacar_matrizA(cadena)) 
                b = np.array(funciones.sacar_matrizB(cadena))

                vector_solucion = funciones.gaussElim(a,b) 
                fila2_tab1.controls[1].text_align = "center"
                texto = "Solucion\n"
                for i in range(len(vector_solucion)):
                    texto+= "x" + str(i) + " = " + str(round(vector_solucion[i] , 4)) + "\n"
                fila2_tab1.controls[1].value = texto
                pagina.update()
        else:
                dlg = ft.AlertDialog(
                    title=ft.Text("Entrada incorrecta")
                )
                pagina.dialog = dlg
                dlg.open = True
                pagina.update()

    def evento_limpiar(e):
        fila2_tab1.controls[0].value = ""
        fila2_tab1.controls[1].value = ""
        pagina.update()

    fila1_tab1= ft.Row(
        controls=[
            ft.Text("\ningrese la matriz"),
            ft.Text("\nRespuesta"),
        ],
        alignment= "center",
        spacing=340,
    )

    fila2_tab1= ft.Row(
        controls=[
           ft.TextField(label="Gauss-Jordan", multiline=True , text_align="center" , min_lines=8),
           ft.TextField(label="resultado", multiline=True , text_align="center" , min_lines=8),

        ],
        alignment= "center",
        spacing=100,

    )
    fila3_tab1= ft.Row(
        controls=[ 
            ft.ElevatedButton(text="calcular", width=200,height=50 , on_click=calcular_GaussJordan , ),
            ft.ElevatedButton(text="borrar", width=200,height=50 , on_click =evento_limpiar ),
        ],
        alignment= "center",
        spacing=200,
    )

    columna1_tab1= ft.Column(
        controls=[
            fila1_tab1,
            fila2_tab1,
            ft.Row(controls=[ft.Text("")]),
            fila3_tab1,
        ]
    )
    def evento_calcular_sistemas_numericos(e):
        
        cadena = fila2_tab2.controls[0].value.replace("\n" , "") 

        dlg = ft.AlertDialog(
            title=ft.Text("Entrada incorrecta, colocar solo los numeros correspondientes al sistema numerico seleccionado ")
        )


        if fila3_tab2.controls[1].value == "Binario":

            if funciones.binario(cadena): 


                texto = "Conversiones numericas\n\n"
                texto += "Ternario: " + funciones.decimal_ternario(decimal) + "\n"
                
                texto += "Octal: " + funciones.decimal_octal(decimal) + "\n"
                texto += "Decimal: " + str(decimal) + "\n"
                texto += "Hexadecimal: " + funciones.decimal_hexadecimal(decimal)
                fila2_tab2.controls[1].value = texto
                pagina.update()
            else:
                pagina.dialog = dlg
                dlg.open = True
                pagina.update()

        elif fila3_tab2.controls[1].value == "Ternario":
            
            if funciones.ternario(cadena):

                decimal = funciones.llevar_decimal(cadena , 3) 

                texto = "Conversiones numericas\n\n"
                texto += "Binario: " + funciones.decimal_binario(decimal) + "\n"
                
                texto += "Octal: " + funciones.decimal_octal(decimal) + "\n"
                texto += "Decimal: " + str(decimal) + "\n"
                texto += "Hexadecimal: " + funciones.decimal_hexadecimal(decimal)
                fila2_tab2.controls[1].value = texto
                pagina.update()
            else:
                pagina.dialog = dlg
                dlg.open = True
                pagina.update()

       

          
        
        elif fila3_tab2.controls[1].value == "Octal":

            if funciones.octal(cadena):

                decimal = funciones.llevar_decimal(cadena , 8) 

                
                texto = "Conversiones numericas\n\n"
                texto += "Binario: " + funciones.decimal_binario(decimal) + "\n"
                texto += "Ternario: " + funciones.decimal_ternario(decimal) + "\n"
                
                texto += "Decimal: " + str(decimal) + "\n"
                texto += "Hexadecimal: " + funciones.decimal_hexadecimal(decimal)
                fila2_tab2.controls[1].value = texto
                pagina.update()
            else:
                pagina.dialog = dlg
                dlg.open = True
                pagina.update()

        elif fila3_tab2.controls[1].value == "Decimal":

            if funciones.decimal(cadena):

                decimal = funciones.llevar_decimal(cadena , 10) 
                texto = "Conversiones numericas\n\n"
                texto += "Binario: " + funciones.decimal_binario(decimal) + "\n"
                texto += "Ternario: " + funciones.decimal_ternario(decimal) + "\n"
                
                texto += "Octal: " + funciones.decimal_octal(decimal) + "\n"
                texto += "Hexadecimal: " + funciones.decimal_hexadecimal(decimal)
                fila2_tab2.controls[1].value = texto
                pagina.update()
            else:
                pagina.dialog = dlg
                dlg.open = True
                pagina.update()

        elif fila3_tab2.controls[1].value == "Hexadecimal":

            if funciones.hexadecimal(cadena):

                decimal = funciones.llevar_decimal(cadena , 16) 
                texto = "Conversiones numericas\n\n"
                texto += "Binario: " + funciones.decimal_binario(decimal) + "\n"
                texto += "Ternario: " + funciones.decimal_ternario(decimal) + "\n"
                
                texto += "Octal: " + funciones.decimal_octal(decimal) + "\n"
                texto += "Decimal: " + str(decimal)
                fila2_tab2.controls[1].value = texto
                pagina.update()
            else:
                pagina.dialog = dlg
                dlg.open = True
                pagina.update()

    def evento_limpiar_sistemas_numericos(e):
        fila2_tab2.controls[0].value = ""
        fila2_tab2.controls[1].value = ""
        pagina.update()

    fila1_tab2= ft.Row(
        controls=[
            ft.Text("\ningrese un numero"),
            ft.Text("\nRespuesta"),
        ],
        alignment= "center",
        spacing=340,
    )

    fila2_tab2= ft.Row(
        controls=[
           ft.TextField(label="Conversor numerico", multiline=True , text_align="center" , min_lines=8),
           ft.TextField(label="resultado", multiline=True , text_align="center" , min_lines=8),

        ],
        alignment= "center",
        spacing=100,

    )
    fila3_tab2= ft.Row(
        controls=[ 
            ft.ElevatedButton(text="calcular", width=200,height=50 , on_click=evento_calcular_sistemas_numericos, ),
            ft.Dropdown(
                width=140,
                options=[
                    ft.dropdown.Option("Binario"),
                    ft.dropdown.Option("Ternario"),
                   
                    ft.dropdown.Option("Octal"),
                    ft.dropdown.Option("Decimal"),
                    ft.dropdown.Option("Hexadecimal")
                ],
                value="Binario"
            ),
            ft.ElevatedButton(text="borrar", width=200,height=50 , on_click =evento_limpiar_sistemas_numericos ),
        ],
        alignment= "center",
        spacing=70,
    )

    columna1_tab2= ft.Column(
        controls=[
            fila1_tab2,
            fila2_tab2,
            ft.Row(controls=[ft.Text("")]),
            fila3_tab2,
        ]
    )

    pagina.title ="conversor numerico "
    barra = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Conversion numerica",
                content=columna1_tab2
            ),
            ft.Tab(
                text="sistema de ecuaciones",
                content=columna1_tab1,

            )

        ],
        expand=1
    )

   

   
 


    pagina.add(barra)

ft.app(main)

