# Web page URL
web_page = 'https://contrata.mapfrebhd.com.do/seguros-de-vehiculos/es/#/marca'

# "Todas las marcas" button
todas_las_marcas = '/html/body/div/div/mfc-bus-controller/form/div/main/div/mfc-layout/div/section/mfc-matrix-list/div/fieldset/div/p/a'
search_bar = '/html/body/div/div/mfc-bus-controller/form/div/main/div/mfc-layout/div/section/mfc-group-condition/div/div/mfc-filter-input/div/div/div[1]/input[1]'
back_button = '/html/body/div/div/mfc-bus-controller/form/div/main/div/mfc-layout/div/section/mfc-step-diagram-multi/nav/div/button[1]'
forward_button = '/html/body/div/div/mfc-bus-controller/form/div/main/div/mfc-layout/div/section/mfc-step-diagram-multi/nav/div/button[2]'
clear_search_bar_button = '/html/body/div/div/mfc-bus-controller/form/div/main/div/mfc-layout/div/section/mfc-group-condition/div/div/mfc-filter-input/div/div/div[1]/i'
items_container = '/html/body/div/div/mfc-bus-controller/form/div/main/div/mfc-layout/div/section/mfc-group-condition/div/div/mfc-filter-input/div/div/fieldset/ul'
gas_container = '/html/body/div/div/mfc-bus-controller/form/div/main/div/mfc-layout/div/section/mfc-group-condition/div/div/mfc-vertical-list/fieldset/div/ul'
first_item = '/html/body/div/div/mfc-bus-controller/form/div/main/div/mfc-layout/div/section/mfc-group-condition/div/div/mfc-filter-input/div/div/fieldset/ul/li[1]'
gas_first_item = '/html/body/div/div/mfc-bus-controller/form/div/main/div/mfc-layout/div/section/mfc-group-condition/div/div/mfc-vertical-list/fieldset/div/ul/li[1]'
valor_vehiculo = '/html/body/div/div/mfc-bus-controller/form/div/main/div/mfc-layout/div/section/mfc-group-condition/div/div/mfc-number-field/div/div/div/input'
continuar_button = '/html/body/div/div/mfc-bus-controller/form/div/main/div/mfc-layout/div/section/mfc-group-condition/div/div/mfc-standard-button/nav/div/button'

# Personal data
cedula = '/html/body/div/div/mfc-bus-controller/form/div/main/div/mfc-layout/div/section/mfc-group-condition/div/div/mfc-number-field[1]/div/div/div/input'
email = '/html/body/div/div/mfc-bus-controller/form/div/main/div/mfc-layout/div/section/mfc-group-condition/div/div/mfc-standard-text[1]/div/div[2]/div/div[1]/input'
celular = '/html/body/div/div/mfc-bus-controller/form/div/main/div/mfc-layout/div/section/mfc-group-condition/div/div/mfc-number-field[2]/div/div/div/input'
acuerdos = '/html/body/div/div/mfc-bus-controller/form/div/main/div/mfc-layout/div/section/mfc-group-condition/div/div/mfc-check-box/div/label'
cotizar_button = '/html/body/div/div/mfc-bus-controller/form/div/main/div/mfc-layout/div/section/mfc-group-condition/div/div/mfc-link-button/div/div/button'

# Years available
años = [2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017,
        2016, 2015, 2014, 2013, 2012, 2011]

# "Equipos de gas"
equipos_gas = ['LOVATO', 'NO EQUIPO GAS', 'OTROS', 'ROMANO', 'SISTEMA DE GAS NATURAL APROBADO', 
               'SISTEMA DE GAS NATURAL NO APROBADO', 'TARTARINI']

# "Uso del vehículo"
usos = ['PARTICULAR', 'CARGA', 'COLECTIVO PRIVADO', 'RENTA DE VEHICULOS', 'TURISMO', 'COMERCIAL']


# Valores
valor_minimo = '/html/body/div/div/mfc-bus-controller/form/div/main/div/mfc-layout/div/section/mfc-group-condition/div/div/mfc-standard-range/div/div/div[2]/div[1]/mfc-riched-content/div/p/strong'
valor_maximo = '/html/body/div/div/mfc-bus-controller/form/div/main/div/mfc-layout/div/section/mfc-group-condition/div/div/mfc-standard-range/div/div/div[2]/div[2]/mfc-riched-content/div/p/strong'

# Flujo de selección
# Web Page > Todas las marcas > [collect_items_from_container] > [click on marca from container] > Modelos > 
# [collect_items_from_container] > [click on modelo from container] > Año > [collect_items_from_container] >
# [click on año from container] > ¿Equipo de gas? > [collect_items_from_container] > [click on equipo from container] > 
# Uso del vehículo > [collect_items_from_container] > [click on uso from container] > Zona de circulación >  
# [collect_items_from_container] > [click on zona from container] > Valor del vehículo > [input value in value bar] > 
# click on "continuar button" > input personal data > click on acuerdos > click on cotizar > get quotations
# 

# Quotations prices
trebol_clasico = '/html/body/div/div/mfc-bus-controller/form/div/main/div/mfc-layout/div/section/mfc-group-condition/div/div/mfc-price-model-equity/div/div[1]/div[1]/mfc-main-price/article/div[3]/div/div[1]/p'
trebol_plus = '/html/body/div/div/mfc-bus-controller/form/div/main/div/mfc-layout/div/section/mfc-group-condition/div/div/mfc-price-model-equity/div/div[1]/div[2]/mfc-main-price/article/div[4]/div/div[1]/p'
trebol_plus_premium = '/html/body/div/div/mfc-bus-controller/form/div/main/div/mfc-layout/div/section/mfc-group-condition/div/div/mfc-price-model-equity/div/div[1]/div[3]/mfc-main-price/article/div[3]/div/div[1]/p'






