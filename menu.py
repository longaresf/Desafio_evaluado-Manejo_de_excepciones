class Menu():
    def __init__(self):
        self.menu_options = ['opción_1', 'opción_2', 'opción_3']
        self.selected_option = None
    
    def display_menu(menu_options):
        print("Bienvenidos al menú!")
        for i in range(len(menu_options)):
            print(f"{i+1}. {menu_options[i]}")
        
        while True:
            try:
                user_input = int(input("Seleccione una opción del menú (1, 2 o 3): "))
                if user_input > len(menu_options):
                    raise ValueError("Opción no válida.")
                else:
                    selected_option = user_input - 1
                    Menu.execute_selected_option(menu_options,selected_option)
                    break
            except ValueError as ve:
                print(ve)
            
    def execute_selected_option(menu_options,selected_option):
        print(f'selected_option: {selected_option}')
        if selected_option is not None:
            print(f"\n\n¡Ejecutando la opción: {menu_options[selected_option]}\n")
            Menu.display_menu(menu_options)
            # Aquí iría el código correspondiente
            input("\nPresiona Enter para continuar...")

Menu.display_menu(menu_options=Menu().menu_options)
#Menu.execute_selected_option(1,1)



