def dibujar_no_con_si():
    si = "si"
    no = [
        [si, si, si, si, "  ", si, "  ", si, si, si, si],
        [si, "  ", "  ", si, "  ", si, si, "  ", "  ", si],
        [si, "  ", "  ", si, "  ", si, "  ", si, "  ", si],
        [si, "  ", "  ", si, "  ", si, "  ", "  ", si, si],
        [si, "  ", "  ", si, "  ", si, "  ", "  ", "  ", si],
        [si, "  ", "  ", si, "  ", si, "  ", "  ", "  ", si],
        [si, "  ", "  ", si, "  ", si, "  ", "  ", "  ", si],
        [si, "  ", "  ", si, "  ", si, "  ", "  ", "  ", si],
        [si, "  ", "  ", si, "  ", si, "  ", "  ", "  ", si],
        [si, si, si, si, "  ", si, "  ", "  ", "  ", si]
    ]

    for fila in no:
        print("".join(fila))

dibujar_no_con_si()
