import reflex as rx

#Sombras
shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"

#Fuentes
main_font = "sans-serif"

#Colores
blue = "#A7C6ED"
red = "#f0bbc0"

#Estilo del input
input_style = dict(
    font_family=main_font,
    padding="1em",
    box_shadow=shadow,
    width="60vw",
    height="auto",
)

#Estilo del boton de añadir
add_button_style = dict(
    font_family=main_font,
    border_width="2.5px",
    padding="1em",
    box_shadow=shadow,
    width="20vw",
    height="100%",
    background_color=blue,
)

#Estilo de la caja para la lista
listbox_style = dict(
    width="80vw",
)

#Estilo de la tarjeta de producto
prod_card_style = dict(
    padding="20px",
    border_radius="10px",
    background_color="#222",
    margin_bottom="15px",
    shadow="md",
    width="100%",
    position="relative"

)

#Estilo del scroll
scrollbar_style = dict(
    height="auto",
    style="scroll",
    scrollbars="vertical",
)

#Estilo del título
heading_style = dict(
    font_family=main_font,
    fontweight="bold",
    font_size="2em",
    color=blue,
    text_align="center",
    margin="1em",
)

prod_name_style = dict(
    font_family=main_font,
    font_size="20px",
    color= "#fff",
    font_weight= "bold",
)

prod_category_style = dict(
    font_size= "16px",
    color= "#AFCBFF",
)

drawer_content_style = dict(
    top="auto",
    right="auto",
    height="100%",
    width="20em",
    padding="2em",
    ackground_color="auto"
)

drawer_buttons_style = dict(
    font_family=main_font,
    border_width="2.5px",
    padding="1em",
    box_shadow=shadow,
    background_color=blue,
)

drawer_input_style = dict(
    font_family=main_font,
    padding="1em",
    box_shadow=shadow,
    width="auto",
    height="auto",
)

remove_button_style = dict(
    font_family=main_font,
    background_color=red,
    width="25px",
    height="25px",
)
