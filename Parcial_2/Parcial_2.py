import reflex as rx

# Lista de curiosidades
curiosidades = [
    {
        "titulo": "El Sol no es una bola de fuego",
        "descripcion": "Es una esfera de plasma sostenida por su propia gravedad.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/c/c3/Solar_sys8.jpg",
        "url": "https://es.wikipedia.org/wiki/Sol"
    },
    {
        "titulo": "Lluvia de diamantes",
        "descripcion": "En Neptuno y Urano puede llover diamantes debido a la presión extrema.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/5/56/Neptune_Full.jpg",
        "url": "https://es.wikipedia.org/wiki/Neptuno_(planeta)"
    },
    {
        "titulo": "Un día en Venus",
        "descripcion": "Dura más que un año en Venus: su rotación es más lenta que su traslación.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/e/e5/Venus-real_color.jpg",
        "url": "https://es.wikipedia.org/wiki/Venus_(planeta)"
    },
    {
        "titulo": "El espacio es silencioso",
        "descripcion": "No hay aire, por tanto, no hay sonido.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Hubble_Ultra_Deep_Field_part_d.jpg",
        "url": "https://es.wikipedia.org/wiki/Espacio_exterior"
    },
    {
        "titulo": "Estrellas de neutrones",
        "descripcion": "Una cucharadita pesa más de mil millones de toneladas.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/f/fb/Noirlab2218a_Neutron_Star_Merger_in_the_Early_Universe.jpg",
        "url": "https://es.wikipedia.org/wiki/Estrella_de_neutrones"
    },
    {
        "titulo": "Agujeros negros distorsionan el tiempo",
        "descripcion": "La gravedad extrema ralentiza el tiempo.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Black_hole_-_Messier_87_crop_max_res.jpg/1024px-Black_hole_-_Messier_87_crop_max_res.jpg",
        "url": "https://es.wikipedia.org/wiki/Agujero_negro"
    },
    {
        "titulo": "La ISS viaja a 28.000 km/h",
        "descripcion": "Da la vuelta a la Tierra en solo 90 minutos.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/The_station_pictured_from_the_SpaceX_Crew_Dragon_5_%28cropped%29.jpg/1920px-The_station_pictured_from_the_SpaceX_Crew_Dragon_5_%28cropped%29.jpg",
        "url": "https://es.wikipedia.org/wiki/Estaci%C3%B3n_Espacial_Internacional"
    },
    {
        "titulo": "Gravedad lunar reducida",
        "descripcion": "En la Luna pesas 1/6 de lo que pesas en la Tierra.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/e/e1/FullMoon2010.jpg",
        "url": "https://es.wikipedia.org/wiki/Luna"
    },
    {
        "titulo": "Saturno podría flotar",
        "descripcion": "Es tan poco denso que flotaría en agua.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/c/c7/Saturn_during_Equinox.jpg",
        "url": "https://es.wikipedia.org/wiki/Saturno_(planeta)"
    },
    {
        "titulo": "Miles de exoplanetas descubiertos",
        "descripcion": "Muchos parecidos a la Tierra han sido detectados.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/4/43/Chart_of_exoplanet_because_5000th_discovery.png",
        "url": "https://es.wikipedia.org/wiki/Exoplaneta"
    },
]

# Estado
class State(rx.State):
    cantidad: int = 4

    def ver_mas(self):
        if self.cantidad < len(curiosidades):
            self.cantidad += 2

    def ver_menos(self):
        if self.cantidad > 4:
            self.cantidad = 4

# Página principal
def index():
    return rx.box(
        rx.vstack(
            rx.heading("Curiosidades del Espacio", size="9", margin_bottom="1em"),
            rx.hstack(
                *[
                    rx.cond(
                        State.cantidad > i,
                        rx.card(
                            rx.image(
                                src=c["imagen"],
                                width="100%",
                                height="150px",
                                object_fit="cover",
                                border_radius="8px"
                            ),
                            rx.text(c["titulo"], weight="bold", margin_top="0.5em"),
                            rx.text(c["descripcion"]),
                            rx.link("Leer más", href=c["url"], is_external=True, color="skyblue", margin_top="0.5em"),
                            padding="1em",
                            margin="1em",
                            border_radius="10px",
                            background_color="#1a1a1a",
                            color="white",
                            box_shadow="0 4px 8px rgba(255, 255, 255, 0.2)",
                            width="250px"
                        )
                    )
                    for i, c in enumerate(curiosidades)
                ],
                wrap="wrap",
                justify="center"
            ),
            rx.cond(
                State.cantidad < len(curiosidades),
                rx.button("Ver más", on_click=State.ver_mas, color_scheme="purple", margin_top="1em"),
                rx.button("Ver menos", on_click=State.ver_menos, color_scheme="red", margin_top="1em")
            ),
            padding="2em",
            align="center"
        ),
        background_image="url('assets/espacio.png')",
        background_size="cover",
        background_position="center",
        background_repeat="no-repeat",
        min_height="100vh"
    )

# App
app = rx.App()
app.add_page(index)