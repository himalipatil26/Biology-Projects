def classify_plant():
    print("---- Plant Classification Tool ----")

    leaf_type = input("Leaf type (simple/compound): ").lower()
    venation = input("Leaf venation (parallel/reticulate/none): ").lower()
    symmetry = input("Flower symmetry (radial/bilateral/none): ").lower()
    seeds = input("Seeds present? (yes/no): ").lower()
    vascular = input("Vascular tissue present? (yes/no): ").lower()

    # ----------- Logic -------------
    if vascular == "no" and seeds == "no":
        return "Bryophyte"

    if vascular == "yes" and seeds == "no":
        return "Pteridophyte"

    if vascular == "yes" and seeds == "yes":
        # Gymnosperm vs Angiosperm
        if symmetry == "none":
            return "Gymnosperm"

        # Angiosperms
        # Monocot vs Dicot
        if venation == "parallel" and leaf_type == "simple":
            return "Angiosperm (Monocot)"
        else:
            return "Angiosperm (Dicot)"

    return "Could not classify — check inputs."


result = classify_plant()
print("\nPlant Group:", result)
