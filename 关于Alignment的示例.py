# 关于Alignment的示例.py
# 作者：传奇开心果
# 日期：2021-05-11


import flet as ft


# 创建各个容器
def create_container(alignment, text, bottom_padding=0, margin=None):
    return ft.Container(
        width=200,
        height=200,
        bgcolor=ft.Colors.AMBER,  # 设置背景色为琥珀色
        border=ft.border.all(color=ft.Colors.BLACK),
        alignment=alignment,
        margin=margin,  # 添加外边距
        content=ft.Container(  # 使用 Container 包裹 Text
            bgcolor=ft.Colors.BLUE,  # 设置背景色为蓝色
            content=ft.Text(  # 使用 Text 替代 ElevatedButton
                value=text,
                color=ft.Colors.WHITE,  # 设置文字颜色为白色
            ),
            padding=ft.padding.all(0),  # 将内边距设置为0
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

# 将所有容器添加到一个行中
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
    scroll=ft.ScrollMode.ALWAYS,  # 设置滚动条模式
)


# 创建一个页面，设置页面标题，并将 Row 直接添加到页面中
def main(page: ft.Page):
    page.title = "Alignment Example"
    page.add(row)


# 显示页面
ft.app(target=main)
