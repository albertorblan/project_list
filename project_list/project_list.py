import reflex as rx
from project_list import state
from project_list import style


def drawer() -> rx.Component:
    return rx.drawer.root(
        rx.drawer.trigger(rx.button("☰", style=style.drawer_buttons_style)),
        rx.drawer.overlay(z_index="5"),
        rx.drawer.portal(
            rx.drawer.content(
                rx.flex(
                    rx.drawer.close(rx.box(rx.button("·", style=style.drawer_buttons_style))),

                    rx.vstack(
                        rx.input(
                            placeholder="Superercado",
                            style = style.drawer_input_style,
                            value=state.InputState.marketplace,
                            on_change=state.InputState.set_marketplace,
                        ),

                        rx.input(
                            placeholder="Ubicación",
                            style=style.drawer_input_style,
                            value=state.InputState.location,
                            on_change=state.InputState.set_location,
                        ),

                        rx.button(
                            "Guardar",
                            style=style.drawer_buttons_style,
                            on_click=state.InputState.save,
                        ),

                        align_items="center"
                    ),

                    align_items="start",
                    direction="column",
                    spacing="50px",
                ),
                style=style.drawer_content_style
            )
        ),
        direction="left",
    )


# Componente para el input de productos
def input_text() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Añade un producto... ",
            value=state.InputState.product,
            style=style.input_style,
            on_change=state.InputState.set_product,
        ),
        rx.button(
            "+",
            style=style.add_button_style,
            on_click=state.InputState.classify_product
        ),
        justify="center",
        spacing="10px",
    )


# Componente para mostrar una tarjeta de producto
def product_card(product) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(product['Producto'], style=style.prod_name_style),
            rx.text(f"Categoría: {product['Categoria']}", style=style.prod_category_style),
            rx.text(f"Precio: {product['Precio']}", style=style.prod_category_style),
            position="relative",
        ),

        rx.box(
            remove_button(product["id"]),
            position="absolute",
            top="10px",
            right="10px",
        ),

        style=style.prod_card_style,
    )


# Componente para listar productos
def product_list() -> rx.Component:
    return rx.vstack(
        rx.foreach(
            state.InputState.product_list,
            lambda product: product_card(product)  # Crear tarjetas de productos
        ),
        align_items="center",
        spacing="10px",
    )


# Componente del título principal
def title() -> rx.Component:
    return rx.center(
        rx.heading("Project List", style=style.heading_style),
    )

def loading_spinner() -> rx.Component:
    return rx.spinner(
        size="3",
        loading=state.InputState.is_loading,
    )

def remove_button(product_id) -> rx.Component:
    return rx.button(
        "·",
        style=style.remove_button_style,
        on_click=state.InputState.remove(product_id),
    )


# Página principal de la aplicación
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.hstack(
                drawer(),
                title(),
                loading_spinner(),
                align_items="center",
            ),
            rx.scroll_area(
                product_list(),
                height="70vh",
                width="100%",
                scrollbars="vertical",
            ),
            input_text(),
            align_items="center",
        ),
        height="100vh",
        width="100vw",
    )


# Inicialización de la aplicación
app = rx.App()
app.add_page(index)
