import os
import time
import itertools
import re
import cv2
import numpy as np
import pyautogui
from PIL import Image, ImageGrab

########################################## Configuracoes Basicas ###########################################
                                                                                                           #
stack_max_size = 10                                                                                        #
                                                                                                           #
slot_width = 49                                                                                            #
slot_height = 49                                                                                           #
                                                                                                           #
customer_trade_x = 327                                                                                     #
customer_trade_y = 224                                                                                     #
                                                                                                           #
user_trade_x = 327                                                                                         #
user_trade_y = 548                                                                                         #
                                                                                                           #
log_original = r"C:\Program Files (x86)\Grinding Gear Games\Path of Exile\logs\Client.txt"                 #
fila_gerada = r"C:\Users\mathe\Desktop\Sadly_PoE\fila.txt"                                                 #
atendidos = r"C:\Users\mathe\Desktop\Sadly_PoE\atendidos.txt"                                              #
                                                                                                           #
######################################## Currency Stack Size Images ########################################
                                                                                                           #
number_40 = cv2.imread(r"currency_images\numbers\40.png")                                                  #
number_39 = cv2.imread(r"currency_images\numbers\39.png")                                                  #
number_38 = cv2.imread(r"currency_images\numbers\38.png")                                                  #
number_37 = cv2.imread(r"currency_images\numbers\37.png")                                                  #
number_36 = cv2.imread(r"currency_images\numbers\36.png")                                                  #
number_35 = cv2.imread(r"currency_images\numbers\35.png")                                                  #
number_34 = cv2.imread(r"currency_images\numbers\34.png")                                                  #
number_33 = cv2.imread(r"currency_images\numbers\33.png")                                                  #
number_32 = cv2.imread(r"currency_images\numbers\32.png")                                                  #
number_31 = cv2.imread(r"currency_images\numbers\31.png")                                                  #
number_30 = cv2.imread(r"currency_images\numbers\30.png")                                                  #
number_29 = cv2.imread(r"currency_images\numbers\29.png")                                                  #
number_28 = cv2.imread(r"currency_images\numbers\28.png")                                                  #
number_27 = cv2.imread(r"currency_images\numbers\27.png")                                                  #
number_26 = cv2.imread(r"currency_images\numbers\26.png")                                                  #
number_25 = cv2.imread(r"currency_images\numbers\25.png")                                                  #
number_24 = cv2.imread(r"currency_images\numbers\24.png")                                                  #
number_23 = cv2.imread(r"currency_images\numbers\23.png")                                                  #
number_22 = cv2.imread(r"currency_images\numbers\22.png")                                                  #
number_21 = cv2.imread(r"currency_images\numbers\21.png")                                                  #
number_20 = cv2.imread(r"currency_images\numbers\20.png")                                                  #
number_19 = cv2.imread(r"currency_images\numbers\19.png")                                                  #
number_18 = cv2.imread(r"currency_images\numbers\18.png")                                                  #
number_17 = cv2.imread(r"currency_images\numbers\17.png")                                                  #
number_16 = cv2.imread(r"currency_images\numbers\16.png")                                                  #
number_15 = cv2.imread(r"currency_images\numbers\15.png")                                                  #
number_14 = cv2.imread(r"currency_images\numbers\14.png")                                                  #
number_13 = cv2.imread(r"currency_images\numbers\13.png")                                                  #
number_12 = cv2.imread(r"currency_images\numbers\12.png")                                                  #
number_11 = cv2.imread(r"currency_images\numbers\11.png")                                                  #
number_10 = cv2.imread(r"currency_images\numbers\10.png")                                                  #
number_9 = cv2.imread(r"currency_images\numbers\9.png")                                                    #
number_8 = cv2.imread(r"currency_images\numbers\8.png")                                                    #
number_7 = cv2.imread(r"currency_images\numbers\7.png")                                                    #
number_6 = cv2.imread(r"currency_images\numbers\6.png")                                                    #
number_5 = cv2.imread(r"currency_images\numbers\5.png")                                                    #
number_4 = cv2.imread(r"currency_images\numbers\4.png")                                                    #
number_3 = cv2.imread(r"currency_images\numbers\3.png")                                                    #
number_2 = cv2.imread(r"currency_images\numbers\2.png")                                                    #
number_1 = cv2.imread(r"currency_images\numbers\1.png")                                                    #
                                                                                                           #
######################################## Currency Type Check Images ########################################
                                                                                                           #
alchemy_frag = cv2.imread(r"currency_images\currencies\alchemy_orb\alchemy.png")                           #
alteration_frag = cv2.imread(r"currency_images\currencies\alteration_orb\alteration.png")                  #
anullment_frag = cv2.imread(r"currency_images\currencies\annulment\annulment.png")                         #
augmentation_frag = cv2.imread(r"currency_images\currencies\augmentation_orb\augmentation.png")            #
chance_frag = cv2.imread(r"currency_images\currencies\chance_orb\chance.png")                              #
chaos_frag = cv2.imread(r"currency_images\currencies\chaos_orb\chaos.png")                                 #
chromatic_frag = cv2.imread(r"currency_images\currencies\chromatic_orb\chromatic.png")                     #
divine_frag = cv2.imread(r"currency_images\currencies\divine_orb\divine.png")                              #
exalted_frag = cv2.imread(r"currency_images\currencies\exalted_orb\exalted.png")                           #
fusing_frag = cv2.imread(r"currency_images\currencies\fusing_orb\fusing.png")                              #
gpc_frag = cv2.imread(r"currency_images\currencies\gpc_orb\gpc.png")                                       #
jeweller_frag = cv2.imread(r"currency_images\currencies\jeweller_orb\jewellers.png")                       #
regal_frag = cv2.imread(r"currency_images\currencies\regal_orb\regal.png")                                 #
regret_frag = cv2.imread(r"currency_images\currencies\regret_orb\regret.png")                              #
scouring_frag = cv2.imread(r"currency_images\currencies\scouring_orb\scouring.png")                        #
transmutation_frag = cv2.imread(r"currency_images\currencies\transmutation_orb\transmutation.png")         #
vaal_frag = cv2.imread(r"currency_images\currencies\vaal_orb\vaal.png")                                    #
                                                                                                           #
########################################## Dictionary organization #########################################
                                                                                                           #
currencies_types = {                                                                                       #
    'alchemy' : alchemy_frag,                                                                              #
    'alteration' : alteration_frag,                                                                        #
    'Annulment' : anullment_frag,                                                                          #
    'augmentation' : augmentation_frag,                                                                    #
    'chance' : chance_frag,                                                                                #
    'chaos' : chaos_frag,                                                                                  #
    'chrome' :  chromatic_frag,                                                                            #
    'divine' : divine_frag,                                                                                #
    'exalted' : exalted_frag,                                                                              #
    'fusing' : fusing_frag,                                                                                #
    'gcp' : gpc_frag,                                                                                      #
    'jeweller\'s' : jeweller_frag,                                                                         #
    'regal' : regal_frag,                                                                                  #
    'regret' : regret_frag,                                                                                #
    'scouring' : scouring_frag,                                                                            #
    'transmutation' : transmutation_frag,                                                                  #
    'vaal' : vaal_frag                                                                                     #
}                                                                                                          #
                                                                                                           #
number_files = {                                                                                           #
    1 : number_1,                                                                                          #
    2 : number_2,                                                                                          #
    3 : number_3,                                                                                          #
    4 : number_4,                                                                                          #
    5 : number_5,                                                                                          #
    6 : number_6,                                                                                          #
    7 : number_7,                                                                                          #
    8 : number_8,                                                                                          #
    9 : number_9,                                                                                          #
    10 : number_10,                                                                                        #
    11 : number_11,                                                                                        #
    12 : number_12,                                                                                        #
    13 : number_13,                                                                                        #
    14 : number_14,                                                                                        #
    15 : number_15,                                                                                        #
    16 : number_16,                                                                                        #
    17 : number_17,                                                                                        #
    18 : number_18,                                                                                        #
    19 : number_19,                                                                                        #
    20 : number_20,                                                                                        #
    21 : number_21,                                                                                        #
    22 : number_22,                                                                                        #
    23 : number_23,                                                                                        #
    24 : number_24,                                                                                        #
    25 : number_25,                                                                                        #
    26 : number_26,                                                                                        #
    27 : number_27,                                                                                        #
    28 : number_28,                                                                                        #
    29 : number_29,                                                                                        #
    30 : number_30,                                                                                        #
    31 : number_31,                                                                                        #
    32 : number_32,                                                                                        #
    33 : number_33,                                                                                        #
    34 : number_34,                                                                                        #
    35 : number_35,                                                                                        #
    36 : number_36,                                                                                        #
    37 : number_37,                                                                                        #
    38 : number_38,                                                                                        #
    39 : number_39,                                                                                        #
    40 : number_40                                                                                         #
}                                                                                                          #
                                                                                                           #
############################################################################################################

class pedido_completo:
    def __init__(self, cliente, valor_meu, valor_cliente, tipo_meu, tipo_cliente):
        self.cliente = cliente
        self.valor_meu = valor_meu
        self.valor_cliente = valor_cliente
        self.tipo_meu = tipo_meu
        self.tipo_cliente = tipo_cliente

def procura_ofertas(substring, log, fila, atendidos):
    with open(log) as a, open(fila, 'a') as b, open(atendidos) as c:
        Clist = [line.rstrip() for line in c]
        for line in a:
            if substring in line:
                if line.rstrip('\r\n') not in Clist:
                    b.write(line + '\n')

def atender_fila(fila, atendidos):
    with open(fila) as a, open(atendidos, "a") as b:
        pedido = a.readline()
        b.write(pedido + "\n")
        pedido = pedido[60:]
        pedido = re.split(":", pedido)
        nome_cliente = pedido[0]
        pedido.remove(nome_cliente)
        pedido = pedido[0]
        pedido = pedido[26:]
        pedido = re.split(" for", pedido)
        valor_usuario = pedido[0]
        pedido = pedido[1]
        valor_usuario = re.split("\s", valor_usuario)
        tipo_usuario = valor_usuario[1]
        valor_usuario = valor_usuario[0]
        pedido = pedido[4:]
        pedido = re.split(" in", pedido)
        pedido = pedido[0]
        pedido = re.split("\s", pedido)
        valor_comprador = pedido[0]
        tipo_comprador = pedido[1]
        pedido_final = pedido_completo(nome_cliente, valor_usuario, valor_comprador, tipo_usuario, tipo_comprador)
        return pedido_final

def confere_cliente(ini_x, ini_y, slot_width, slot_height, currency_value, currency_type):
    currency_sum = 0
    x = ini_x
    y = ini_y
    slot_var_x = slot_width
    slot_var_y = slot_height
    while x < 925:
        while y < 460:
            num = stack_max_size
            printscreen = ImageGrab.grab(bbox = (x, y, (slot_width + x), (slot_height + y))).save("printscreen.png")
            printscreen = cv2.imread("printscreen.png")
            curr_type = cv2.matchTemplate(printscreen, currency_type, cv2.TM_CCOEFF_NORMED)
            threshold = 0.8
            if np.amax(curr_type) >= threshold:
                while num >= 1:
                    number = cv2.matchTemplate(printscreen, number_files[num], cv2.TM_CCOEFF_NORMED)
                    if np.amax(number) >= threshold:
                        currency_sum = currency_sum + num
                        break
                    else:
                        num = num - 1
            y += 51
            slot_var_y += 51
        x += 51
        slot_var_x += 51
        y = ini_y
        slot_var_y = slot_height
    if currency_sum >= currency_value:
        return 1
    else:
        return 0

if confere_cliente(customer_trade_x, customer_trade_y, slot_width, slot_height, 40, chaos_frag) == 1:
    print("Troca funcionando corretamente!")

if confere_cliente(customer_trade_x, customer_trade_y, slot_width, slot_height, 40, chaos_frag) == 0:
    print("Troca deu errado!")

# currency_value = confere_cliente(customer_trade_x, customer_trade_y, slot_width, slot_height)
# print(currency_value)

# def confere_usuario(ini_x, ini_y, slot_width, slot_height):
#     x = ini_x
#     y = ini_y
#     while x < 950:
#         while y < 810:


# procura_ofertas('like to buy your', log_original, fila_gerada, atendidos)
# pedido01 = atender_fila(fila_gerada, atendidos)
# print(pedido01.cliente)