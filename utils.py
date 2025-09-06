def konversi_suhu(nilai, dari, ke):
    dari = dari.lower()
    ke = ke.lower()

    if dari == ke:
        return nilai

    if dari == "c":
        if ke == "f":
            return (nilai * 9/5) + 32
        elif ke == "k":
            return nilai + 273.15

    elif dari == "f":
        if ke == "c":
            return (nilai - 32) * 5/9
        elif ke == "k":
            return (nilai - 32) * 5/9 + 273.15

    elif dari == "k":
        if ke == "c":
            return nilai - 273.15
        elif ke == "f":
            return (nilai - 273.15) * 9/5 + 32

    return f"Error: konversi dari '{dari}' ke '{ke}' tidak valid."
