# About Alignment Example.py
# Author: LegendaryPistachio
# Date: 2021-05-11

import flet as ft


# Create various containers
def create_container(alignment, text, bottom_padding=0, margin=None):
    return ft.Container(
        width=200,
        height=200,
        bgcolor=ft.Colors.AMBER,  # Set background color to amber
        border=ft.border.all(color=ft.Colors.BLACK),
        alignment=alignment,
        margin=margin,  # Add margin
        content=ft.Container(  # Use Container to wrap Text
            bgcolor=ft.Colors.BLUE,  # Set background color to blue
            content=ft.Text(  # Use Text instead of ElevatedButton
                value=text,
                color=ft.Colors.WHITE,  # Set text color to white
            ),
            padding=ft.padding.all(0),  # Set padding to 0
        ),
    )


container = create_container(
    ft.alignment.center,
    "Hello, Alignment!",
    bottom_padding=20,
    margin=ft.margin.only(bottom=20),
)
container_1 = create_container(
    ft.alignment.center, "Center", bottom_padding=20, margin=ft.margin.only(bottom=20)
)
container_2 = create_container(
    ft.alignment.top_left,
    "Top Left",
    bottom_padding=20,
    margin=ft.margin.only(bottom=20),
)
container_3 = create_container(
    ft.alignment.top_center,
    "Top Center",
    bottom_padding=20,
    margin=ft.margin.only(bottom=20),
)
container_4 = create_container(
    ft.alignment.top_right,
    "Top Right",
    bottom_padding=20,
    margin=ft.margin.only(bottom=20),
)
container_5 = create_container(
    ft.alignment.center_left,
    "Center Left",
    bottom_padding=20,
    margin=ft.margin.only(bottom=20),
)
container_6 = create_container(
    ft.alignment.center_right,
    "Center Right",
    bottom_padding=20,
    margin=ft.margin.only(bottom=20),
)
container_7 = create_container(
    ft.alignment.bottom_left,
    "Bottom Left",
    bottom_padding=20,
    margin=ft.margin.only(bottom=20),
)
container_8 = create_container(
    ft.alignment.bottom_center,
    "Bottom Center",
    bottom_padding=20,
    margin=ft.margin.only(bottom=20),
)
container_9 = create_container(
    ft.alignment.bottom_right,
    "Bottom Right",
    bottom_padding=20,
    margin=ft.margin.only(bottom=20),
)
container_10 = create_container(
    ft.alignment.Alignment(-0.5, -0.5),
    "Custom (-0.5, -0.5)",
    bottom_padding=20,
    margin=ft.margin.only(bottom=20),
)

# Add all containers to a row
row = ft.Row(
    controls=[
        container,
        container_1,
        container_2,
        container_3,
        container_4,
        container_5,
        container_6,
        container_7,
        container_8,
        container_9,
        container_10,
    ],
    scroll=ft.ScrollMode.ALWAYS,  # Set scrollbar mode
)


# Create a page, set the page title, and add Row directly to the page
def main(page: ft.Page):
    page.title = "Alignment Example"
    page.add(row)


# Display the page
ft.app(target=main)
