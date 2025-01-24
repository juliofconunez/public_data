
# Web Page Url
web_page = 'https://www.armalotu.com.do/armalotu'
# Click on a general spot, used as close dropdown button mainly in "Tu Vehiculo" form
close_drop = '/html/body/app-root/app-armalotu/div/form'

# Start Button of Landing Page
arma_tu_seguro = '/html/body/app-root/app-armalotu/div/section[1]/div/div/div[2]/a'

# Types of vehicles menu
automovil = '/html/body/app-root/app-armalotu/div/div[1]/div/div[2]/ul/li[1]/div'
jeepeta_minivan = '/html/body/app-root/app-armalotu/div/div[1]/div/div[2]/ul/li[2]/div'
camionetas_furgonetas = '/html/body/app-root/app-armalotu/div/div[1]/div/div[2]/ul/li[3]/div'
vehiculos_pesados = '/html/body/app-root/app-armalotu/div/div[1]/div/div[2]/ul/li[4]/div'
motocicletas_otros = '/html/body/app-root/app-armalotu/div/div[1]/div/div[2]/ul/li[5]/div'

# Types of insurance
seguro_full = '/html/body/app-root/app-armalotu/div/form/div/div[1]/div[4]/div/div/label'
seguro_ley = '/html/body/app-root/app-armalotu/div/form/div/div[1]/div[5]/div/div/label'

# "Tu Vehiculo" Form

# Marca
marca_input = '/html/body/app-root/app-armalotu/div/form/div/div[1]/div[7]/div/div/div[2]/div/ng-select/div/div/div[2]/input'
marca_scroll_host = '/html/body/app-root/app-armalotu/div/form/div/div[1]/div[7]/div/div/div[2]/div/ng-select/ng-dropdown-panel/div'
# Element under scroll host containing items
marca_items = '/html/body/app-root/app-armalotu/div/form/div/div[1]/div[7]/div/div/div[2]/div/ng-select/ng-dropdown-panel/div/div[2]'

# Modelo
modelo_input = '/html/body/app-root/app-armalotu/div/form/div/div[1]/div[7]/div/div/div[3]/div/ng-select/div/div/div[2]/input'
modelo_scroll_host = '/html/body/app-root/app-armalotu/div/form/div/div[1]/div[7]/div/div/div[3]/div/ng-select/ng-dropdown-panel/div'
# Element under scroll host containing items
modelo_items = '/html/body/app-root/app-armalotu/div/form/div/div[1]/div[7]/div/div/div[3]/div/ng-select/ng-dropdown-panel/div/div[2]'

# Año
# Año is a select type of element, not input
año_select = '/html/body/app-root/app-armalotu/div/form/div/div[1]/div[7]/div/div/div[4]/div/select'
# The element año select contains all the options for that field

# Valor asegurado
# This is a free input with no options
# This only shows up when selecting full insurance
valor_asegurado = '/html/body/app-root/app-armalotu/div/form/div/div[1]/div[7]/div/div/div[5]/div/input'

# Tipo de vehículo
# "Tipo de vehículos" are always these:
tipos = ['Auto/Station (4 cil./4 pasajeros)',
         'Auto/Station (>4 - 6 cil./4 pasajeros)',
         'Auto/Station (>6 cil./4 pasajeros)']
# Input field for the "tipos"
tipo_vehiculo_input = '/html/body/app-root/app-armalotu/div/form/div/div[1]/div[7]/div/div/div[6]/div/ng-select/div/div/div[2]/input'
tipo_vehiculo_scroll_host = '/html/body/app-root/app-armalotu/div/form/div/div[1]/div[7]/div/div/div[6]/div/ng-select/ng-dropdown-panel/div'
# Although in this there are not that much element to scroll, to maintain uniformity I do this the same
tipo_vehiculo_items = '/html/body/app-root/app-armalotu/div/form/div/div[1]/div[7]/div/div/div[6]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]'

# Uso del vehículo
# This is another select type element. So good.
# Usos list:
usos = [' COMPETENCIAS ',
        ' ESCUELA DE APRENDIZAJES ',
        ' MILITAR ',
        ' MUNICIPAL ',
        ' PERSONAL/PRIVADO ',
        ' SERVICIOS A DOMICILIO ',
        ' TAXI ',
        ' TAXI TURISTICO ',
        ' VENDEDOR ']

# uso field select element
uso_vehiculo = '/html/body/app-root/app-armalotu/div/form/div/div[1]/div[7]/div/div/div[7]/div/select'
# under this select element are all options

# Guardar y continuar button
nextbtn = '/html/body/app-root/app-armalotu/div/form/div/div[3]/div/div/div[2]/button'

# Header of "Condiciones Especiales"
# This header appears when you cannot obtain a quotation on the page
# so they just ask for your data to get in contact with you 
condiciones_especiales = '/html/body/ngb-modal-window/div/div/div[1]/h5'

# Alert that price is not correct for the selection
price_incorrect = '/html/body/div/div/div/div[1]'



## Showing quotation

# "Tu vehiculo es" element
tu_vehiculo = '/html/body/app-root/app-armalotu/div/div[2]/div/div[1]/div[3]/div/div[1]/div[1]/div/div[1]/div/input'
# This is to read text and present in final result of quotation

# "Valor asegurado" also to read and show. Is always zero with basic insurance. Can obtain it from
# previous "valor_asegurado"

# "Aditamentos" extra options for the insurance to cover. To select at the quotation page.
aditamentos = '/html/body/app-root/app-armalotu/div/div[2]/div/div[1]/div[3]/div/div[1]/div[1]/div/div[2]/div/input'

# To read cobertura selected in quotation page
cobertura = '/html/body/app-root/app-armalotu/div/div[2]/div/div[1]/div[3]/div/div[1]/div[1]/div/div[4]/div/strong[1]/span'
# This is full or basic insurance only

# "Prima anual" this is the price for the insurance selected. Anually.
prima_anual = '/html/body/app-root/app-armalotu/div/div[2]/div/div[1]/div[3]/div/div[1]/div[1]/div/div[4]/div/div[2]/span'

# "Ajustalo a tu medida" button 
# Since in the basic stages of this scraper is not to use, you can ignore it.
ajustalo = '/html/body/app-root/app-armalotu/div/div[2]/div/div[1]/div[3]/div/div[1]/div[1]/div/div[4]/div/strong[2]/em/h6'








