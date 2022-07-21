from unicodedata import name
import adsk

def material(com_name):
    app = adsk.core.Application.get()
    product = app.activeProduct
    design  = adsk.fusion.Design.cast(product)
    root = design.rootComponent
    allOccs = root.occurrences
    for occs in allOccs:
        lib = adsk.core.MaterialLibrary.cast(None)
        for lib in app.materialLibraries:
            appear = adsk.core.Appearance.cast(None)
            for appear in lib.appearances:
                if appear.name == occs.component.material.appearance.name:
                    prop = adsk.core.Property.cast(None)
                    for prop in appear.appearanceProperties:               
                        if (prop.objectType == adsk.core.ColorProperty.classType()) and ("Color" == prop.name) and (prop.id != "surface_albedo"):
                            colorProp = adsk.core.ColorProperty.cast(prop)
                            val = colorProp.value
                            if val:
                                if occs.component.name == com_name:
                                    name = appear.name
                                    color = f"{str(round(val.red/255,3))} {str(round(val.green/255,3))} {str(round(val.blue/255,3))} {str(round(val.opacity/255,3))}"
                                    return name, color
                            else:
                                color = "0.700 0.700 0.700 1.000"
                                name = "silver"
                                return name, color
                    break