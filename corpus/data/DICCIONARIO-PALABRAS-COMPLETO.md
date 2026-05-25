# Lista completa del diccionario (corpus lexico)

Generado desde `corpus/data/corpus_bilingue_v5.csv` (solo filas `record_type = lexico`).

En la app, la imagen de cada entrada usa **espanol + categoria** (componente `DictionaryTermImage` → `fetchTermImage`). Para armar descargas, la clave practica es la **pareja espanol + categoria**; si varias filas comparten la misma pareja, una imagen puede servir para todas.

- **Total entradas lexicas:** 3922
- **Pares unicos (espanol + categoria) para imagen:** 3720
- **Checklist PNG IA** (pares unicos vs disco `generadas-img-ia-solo`): tabla mas abajo; resumen y lista de archivos listos en `corpus/data/DICCIONARIO-IMAGENES-SOLO-RESUMEN.md`. Refrescar: `python scripts/annotate_diccionario_imagenes_solo.py`.

## Estado PNG IA solo (`corpus/generadas-img-ia-solo`)

Cada fila de *Pares unicos* se cruza con `prompts_solo_full.jsonl` por **`id`** y se comprueba si existe el archivo **`corpus/generadas-img-ia-solo/<ruta>.png`**.

- **Pares en esta tabla:** 3720
- **Ids resueltos en JSONL:** 3720
- **PNG ya presentes en disco:** 636 (17.1 %)
- **Marcados en curso** (`solo_generacion_en_curso.txt`): 0
- **Ids sin fila en JSONL (revisar):** 0

Para generar nuevas imagenes: prompts en `corpus/generadas-img-ia-solo/prompts_solo_full.jsonl`; assets Cursor `solo__<categoria>__<stem>.png`; luego `python scripts/sync_solo_imagenes_desde_assets.py`.
Mientras generas un lote, pon sus `id` o `dest_rel` en `corpus/data/solo_generacion_en_curso.txt` (una por linea) y vuelve a ejecutar este script para ver `- [~] en curso` en la tabla.

Para **refrescar** esta columna y el resumen: `python scripts/annotate_diccionario_imagenes_solo.py`

### Por categoria (pares unicos)

| categoria | PNG listos | Faltan | Total pares |
|-----------|------------|--------|-------------|
| `alimentos` | 23 | 0 | 23 |
| `ambientales` | 25 | 0 | 25 |
| `animales` | 65 | 0 | 65 |
| `astros` | 5 | 0 | 5 |
| `colores` | 9 | 0 | 9 |
| `cuerpo_humano` | 21 | 3 | 24 |
| `diccionario_general` | 265 | 3081 | 3346 |
| `frutas_verduras` | 24 | 0 | 24 |
| `herramientas` | 17 | 0 | 17 |
| `muebles_inmuebles` | 15 | 0 | 15 |
| `nombres_propios` | 20 | 0 | 20 |
| `numeros` | 58 | 0 | 58 |
| `parentescos` | 13 | 0 | 13 |
| `plantas_medicinales` | 20 | 0 | 20 |
| `saludos` | 1 | 0 | 1 |
| `utiles_hogar` | 18 | 0 | 18 |
| `vocabulario_general` | 37 | 0 | 37 |

## Pares unicos (prioritario para imagenes)

| # | id (ejemplo) | espanol | categoria | PNG `generadas-img-ia-solo` |
|---|----------------|---------|-----------|------------------------------|
| 1 | `LEX-00260` | Arracacha | alimentos | - [x] `alimentos/arracacha.png` |
| 2 | `LEX-00258` | Arveja | alimentos | - [x] `alimentos/arveja.png` |
| 3 | `LEX-00266` | Caigua | alimentos | - [x] `alimentos/caigua.png` |
| 4 | `LEX-00263` | Carne | alimentos | - [x] `alimentos/carne.png` |
| 5 | `LEX-00276` | Cebolla | alimentos | - [x] `alimentos/cebolla.png` |
| 6 | `LEX-00280` | Chachafruto | alimentos | - [x] `alimentos/chachafruto.png` |
| 7 | `LEX-00261` | Chicha | alimentos | - [x] `alimentos/chicha.png` |
| 8 | `LEX-00262` | Choclo | alimentos | - [x] `alimentos/choclo.png` |
| 9 | `LEX-00268` | Cidra | alimentos | - [x] `alimentos/cidra.png` |
| 10 | `LEX-00272` | Cilantro | alimentos | - [x] `alimentos/cilantro.png` |
| 11 | `LEX-00269` | Coles | alimentos | - [x] `alimentos/coles.png` |
| 12 | `LEX-00279` | Frijol | alimentos | - [x] `alimentos/frijol.png` |
| 13 | `LEX-00271` | Maiz | alimentos | - [x] `alimentos/maiz.png` |
| 14 | `LEX-00278` | Mani | alimentos | - [x] `alimentos/mani.png` |
| 15 | `LEX-00273` | Mote | alimentos | - [x] `alimentos/mote.png` |
| 16 | `LEX-00277` | Ollucos | alimentos | - [x] `alimentos/ollucos.png` |
| 17 | `LEX-00265` | Papa | alimentos | - [x] `alimentos/papa.png` |
| 18 | `LEX-00275` | Platano | alimentos | - [x] `alimentos/platano.png` |
| 19 | `LEX-00264` | Remolacha | alimentos | - [x] `alimentos/remolacha.png` |
| 20 | `LEX-00270` | Sancocho | alimentos | - [x] `alimentos/sancocho.png` |
| 21 | `LEX-00267` | Sopa | alimentos | - [x] `alimentos/sopa.png` |
| 22 | `LEX-00274` | Yuca | alimentos | - [x] `alimentos/yuca.png` |
| 23 | `LEX-00259` | Zapallo | alimentos | - [x] `alimentos/zapallo.png` |
| 24 | `LEX-00340` | Agua | ambientales | - [x] `ambientales/agua.png` |
| 25 | `LEX-00316` | Arbol caucho | ambientales | - [x] `ambientales/arbol_caucho.png` |
| 26 | `LEX-00321` | Arbol de cera | ambientales | - [x] `ambientales/arbol_de_cera.png` |
| 27 | `LEX-00330` | Arcoiris | ambientales | - [x] `ambientales/arcoiris.png` |
| 28 | `LEX-00331` | Arena | ambientales | - [x] `ambientales/arena.png` |
| 29 | `LEX-00318` | Arrayan | ambientales | - [x] `ambientales/arrayan.png` |
| 30 | `LEX-00336` | Cerro | ambientales | - [x] `ambientales/cerro.png` |
| 31 | `LEX-00320` | Chonta | ambientales | - [x] `ambientales/chonta.png` |
| 32 | `LEX-00319` | Chusque | ambientales | - [x] `ambientales/chusque.png` |
| 33 | `LEX-00327` | Derrumbe | ambientales | - [x] `ambientales/derrumbe.png` |
| 34 | `LEX-00337` | Flor | ambientales | - [x] `ambientales/flor.png` |
| 35 | `LEX-00328` | Fuego | ambientales | - [x] `ambientales/fuego.png` |
| 36 | `LEX-00332` | Lluvia | ambientales | - [x] `ambientales/lluvia.png` |
| 37 | `LEX-00323` | Metal o hierro | ambientales | - [x] `ambientales/metal_o_hierro.png` |
| 38 | `LEX-00333` | Nevado | ambientales | - [x] `ambientales/nevado.png` |
| 39 | `LEX-00334` | Nube | ambientales | - [x] `ambientales/nube.png` |
| 40 | `LEX-00324` | Paja | ambientales | - [x] `ambientales/paja.png` |
| 41 | `LEX-00329` | Piedra | ambientales | - [x] `ambientales/piedra.png` |
| 42 | `LEX-00335` | Planta | ambientales | - [x] `ambientales/planta.png` |
| 43 | `LEX-00325` | Rama | ambientales | - [x] `ambientales/rama.png` |
| 44 | `LEX-00322` | Roble | ambientales | - [x] `ambientales/roble.png` |
| 45 | `LEX-00338` | Tierra organica | ambientales | - [x] `ambientales/tierra_organica.png` |
| 46 | `LEX-00326` | Trueno | ambientales | - [x] `ambientales/trueno.png` |
| 47 | `LEX-00339` | Viento | ambientales | - [x] `ambientales/viento.png` |
| 48 | `LEX-00317` | Yarumo | ambientales | - [x] `ambientales/yarumo.png` |
| 49 | `LEX-00171` | Aguila | animales | - [x] `animales/aguila.png` |
| 50 | `LEX-00075` | aguti o guatuza | animales | - [x] `animales/aguti_o_guatuza.png` |
| 51 | `LEX-00138` | Alacran | animales | - [x] `animales/alacran.png` |
| 52 | `LEX-00170` | Arana | animales | - [x] `animales/arana.png` |
| 53 | `LEX-00168` | Ardilla | animales | - [x] `animales/ardilla.png` |
| 54 | `LEX-00167` | Armadillo | animales | - [x] `animales/armadillo.png` |
| 55 | `LEX-00131` | Avispa | animales | - [x] `animales/avispa.png` |
| 56 | `LEX-00136` | Babosa | animales | - [x] `animales/babosa.png` |
| 57 | `LEX-00129` | Borugo | animales | - [x] `animales/borugo.png` |
| 58 | `LEX-00159` | Buho | animales | - [x] `animales/buho.png` |
| 59 | `LEX-00153` | Caballo | animales | - [x] `animales/caballo.png` |
| 60 | `LEX-00155` | Cabra | animales | - [x] `animales/cabra.png` |
| 61 | `LEX-00139` | Cangrejo | animales | - [x] `animales/cangrejo.png` |
| 62 | `LEX-00120` | Carpintero | animales | - [x] `animales/carpintero.png` |
| 63 | `LEX-00068` | cerdo | animales | - [x] `animales/cerdo.png` |
| 64 | `LEX-00137` | Chamon | animales | - [x] `animales/chamon.png` |
| 65 | `LEX-00141` | Chicharra | animales | - [x] `animales/chicharra.png` |
| 66 | `LEX-00135` | Cienpies | animales | - [x] `animales/cienpies.png` |
| 67 | `LEX-00151` | Codorniz | animales | - [x] `animales/codorniz.png` |
| 68 | `LEX-00149` | Colibri | animales | - [x] `animales/colibri.png` |
| 69 | `LEX-00140` | Comadreja | animales | - [x] `animales/comadreja.png` |
| 70 | `LEX-00156` | Condor | animales | - [x] `animales/condor.png` |
| 71 | `LEX-00154` | Conejo | animales | - [x] `animales/conejo.png` |
| 72 | `LEX-00132` | Cucaracha | animales | - [x] `animales/cucaracha.png` |
| 73 | `LEX-00125` | Cusumbo | animales | - [x] `animales/cusumbo.png` |
| 74 | `LEX-00152` | Cuy | animales | - [x] `animales/cuy.png` |
| 75 | `LEX-00144` | Gallina | animales | - [x] `animales/gallina.png` |
| 76 | `LEX-00130` | Gallinazo | animales | - [x] `animales/gallinazo.png` |
| 77 | `LEX-00145` | Gallo | animales | - [x] `animales/gallo.png` |
| 78 | `LEX-00126` | Garrapata | animales | - [x] `animales/garrapata.png` |
| 79 | `LEX-00162` | Gato | animales | - [x] `animales/gato.png` |
| 80 | `LEX-00121` | Gorrion | animales | - [x] `animales/gorrion.png` |
| 81 | `LEX-00123` | Guacharaca | animales | - [x] `animales/guacharaca.png` |
| 82 | `LEX-00163` | Guatin | animales | - [x] `animales/guatin.png` |
| 83 | `LEX-00172` | Gusano | animales | - [x] `animales/gusano.png` |
| 84 | `LEX-00070` | hocico del puerco | animales | - [x] `animales/hocico_del_puerco.png` |
| 85 | `LEX-00071` | horqueta para puerco | animales | - [x] `animales/horqueta_para_puerco.png` |
| 86 | `LEX-00128` | Lagartija | animales | - [x] `animales/lagartija.png` |
| 87 | `LEX-00160` | Leon | animales | - [x] `animales/leon.png` |
| 88 | `LEX-00134` | Libelula | animales | - [x] `animales/libelula.png` |
| 89 | `LEX-00142` | Lobo | animales | - [x] `animales/lobo.png` |
| 90 | `LEX-00166` | Lombriz | animales | - [x] `animales/lombriz.png` |
| 91 | `LEX-00175` | Loro | animales | - [x] `animales/loro.png` |
| 92 | `LEX-00127` | Mariquita | animales | - [x] `animales/mariquita.png` |
| 93 | `LEX-00161` | Mono | animales | - [x] `animales/mono.png` |
| 94 | `LEX-00157` | Murcielago | animales | - [x] `animales/murcielago.png` |
| 95 | `LEX-00165` | Oveja | animales | - [x] `animales/oveja.png` |
| 96 | `LEX-00169` | Paloma | animales | - [x] `animales/paloma.png` |
| 97 | `LEX-00124` | Pato | animales | - [x] `animales/pato.png` |
| 98 | `LEX-00073` | pecari | animales | - [x] `animales/pecari.png` |
| 99 | `LEX-00176` | Pez | animales | - [x] `animales/pez.png` |
| 100 | `LEX-00072` | pezuña del puerco | animales | - [x] `animales/pezuña_del_puerco.png` |
| 101 | `LEX-00150` | Piojo | animales | - [x] `animales/piojo.png` |
| 102 | `LEX-00069` | puerco | animales | - [x] `animales/puerco.png` |
| 103 | `LEX-00164` | Pulga | animales | - [x] `animales/pulga.png` |
| 104 | `LEX-00122` | Rana | animales | - [x] `animales/rana.png` |
| 105 | `LEX-00173` | Raton | animales | - [x] `animales/raton.png` |
| 106 | `LEX-00074` | saino | animales | - [x] `animales/saino.png` |
| 107 | `LEX-00133` | Sapo | animales | - [x] `animales/sapo.png` |
| 108 | `LEX-00174` | Serpiente | animales | - [x] `animales/serpiente.png` |
| 109 | `LEX-00146` | Tigre | animales | - [x] `animales/tigre.png` |
| 110 | `LEX-00158` | Vaca | animales | - [x] `animales/vaca.png` |
| 111 | `LEX-00147` | Venado | animales | - [x] `animales/venado.png` |
| 112 | `LEX-00143` | Zancudo | animales | - [x] `animales/zancudo.png` |
| 113 | `LEX-00148` | Zarigueya | animales | - [x] `animales/zarigueya.png` |
| 114 | `LEX-00343` | Cometa | astros | - [x] `astros/cometa.png` |
| 115 | `LEX-00341` | Estrella | astros | - [x] `astros/estrella.png` |
| 116 | `LEX-00342` | Luna | astros | - [x] `astros/luna.png` |
| 117 | `LEX-00345` | Planeta Tierra | astros | - [x] `astros/planeta_tierra.png` |
| 118 | `LEX-00344` | Sol | astros | - [x] `astros/sol.png` |
| 119 | `LEX-00067` | Amarillo | colores | - [x] `colores/amarillo.png` |
| 120 | `LEX-00059` | Anaranjado | colores | - [x] `colores/anaranjado.png` |
| 121 | `LEX-00061` | Azul | colores | - [x] `colores/azul.png` |
| 122 | `LEX-00064` | Blanco | colores | - [x] `colores/blanco.png` |
| 123 | `LEX-00066` | Gris | colores | - [x] `colores/gris.png` |
| 124 | `LEX-00065` | Negro | colores | - [x] `colores/negro.png` |
| 125 | `LEX-00062` | Rojo | colores | - [x] `colores/rojo.png` |
| 126 | `LEX-00063` | Rojo encendido | colores | - [x] `colores/rojo_encendido.png` |
| 127 | `LEX-00060` | Verde | colores | - [x] `colores/verde.png` |
| 128 | `LEX-00207` | Barriga | cuerpo_humano | - [x] `cuerpo_humano/barriga.png` |
| 129 | `LEX-00211` | Boca | cuerpo_humano | - [x] `cuerpo_humano/boca.png` |
| 130 | `LEX-00200` | Brazo | cuerpo_humano | - [x] `cuerpo_humano/brazo.png` |
| 131 | `LEX-00213` | Cabello | cuerpo_humano | - [x] `cuerpo_humano/cabello.png` |
| 132 | `LEX-00192` | Cabeza | cuerpo_humano | - [x] `cuerpo_humano/cabeza.png` |
| 133 | `LEX-00202` | Cerebro | cuerpo_humano | - [x] `cuerpo_humano/cerebro.png` |
| 134 | `LEX-00209` | Corazon | cuerpo_humano | - [x] `cuerpo_humano/corazon.png` |
| 135 | `LEX-00191` | Cuello | cuerpo_humano | - [x] `cuerpo_humano/cuello.png` |
| 136 | `LEX-00208` | Diente | cuerpo_humano | - [x] `cuerpo_humano/diente.png` |
| 137 | `LEX-00201` | Garganta | cuerpo_humano | - [x] `cuerpo_humano/garganta.png` |
| 138 | `LEX-00190` | Hombro | cuerpo_humano | - [x] `cuerpo_humano/hombro.png` |
| 139 | `LEX-00212` | Hueso | cuerpo_humano | - [x] `cuerpo_humano/hueso.png` |
| 140 | `LEX-00205` | Lengua | cuerpo_humano | - [x] `cuerpo_humano/lengua.png` |
| 141 | `LEX-00199` | Mano | cuerpo_humano | - [x] `cuerpo_humano/mano.png` |
| 142 | `LEX-00196` | Nariz | cuerpo_humano | - [x] `cuerpo_humano/nariz.png` |
| 143 | `LEX-00210` | Ojo | cuerpo_humano | - [x] `cuerpo_humano/ojo.png` |
| 144 | `LEX-00203` | Ombligo | cuerpo_humano | - [x] `cuerpo_humano/ombligo.png` |
| 145 | `LEX-00206` | Oreja | cuerpo_humano | - [x] `cuerpo_humano/oreja.png` |
| 146 | `LEX-00195` | Pene | cuerpo_humano | - [ ] falta |
| 147 | `LEX-00193` | Pie | cuerpo_humano | - [x] `cuerpo_humano/pie.png` |
| 148 | `LEX-00198` | Pierna | cuerpo_humano | - [x] `cuerpo_humano/pierna.png` |
| 149 | `LEX-00197` | Rodilla | cuerpo_humano | - [x] `cuerpo_humano/rodilla.png` |
| 150 | `LEX-00194` | Seno | cuerpo_humano | - [ ] falta |
| 151 | `LEX-00204` | Vagina | cuerpo_humano | - [ ] falta |
| 152 | `LEXR-01379` | !Hola! (saludando a un hombre) | diccionario_general | - [x] `diccionario_general/!_hola!_(saludando_a_un_hombre).png` |
| 153 | `LEXR-01659` | !Hola! (saludando a una mujer o a varias personas) | diccionario_general | - [x] `diccionario_general/!_hola!_(saludando_a_una_mujer_o_a_varias_personas).png` |
| 154 | `LEXR-02682` | (culebra no venenosa) | diccionario_general | - [x] `diccionario_general/(culebra_no_venenosa).png` |
| 155 | `LEXR-01180` | (especie de bejuco) | diccionario_general | - [x] `diccionario_general/(especie_de_bejuco).png` |
| 156 | `LEXR-02042` | (especie de madera, que usan para labrar cucharas) | diccionario_general | - [x] `diccionario_general/(especie_de_madera,_que_usan_para_labrar_cucharas).png` |
| 157 | `LEXR-00412` | (especie de planta medicinal) | diccionario_general | - [x] `diccionario_general/(especie_de_planta_medicinal).png` |
| 158 | `LEXR-00398` | (especie de árbol) | diccionario_general | - [x] `diccionario_general/(especie_de_árbol).png` |
| 159 | `LEXR-00732` | (planta medicinal) | diccionario_general | - [x] `diccionario_general/(planta_medicinal).png` |
| 160 | `LEXR-00826` | (planta silvestre, que se usa para jabón) | diccionario_general | - [x] `diccionario_general/(planta_silvestre,_que_se_usa_para_jabón).png` |
| 161 | `LEXR-03307` | (planta) | diccionario_general | - [x] `diccionario_general/(planta).png` |
| 162 | `LEXR-01555` | (planta, que da sabor a la comida) | diccionario_general | - [x] `diccionario_general/(planta,_que_da_sabor_a_la_comida).png` |
| 163 | `LEXR-03022` | (yerba que enloquece) | diccionario_general | - [x] `diccionario_general/(yerba_que_enloquece).png` |
| 164 | `LEXR-03828` | 1. abrirse 2. montar a horcajadas | diccionario_general | - [x] `diccionario_general/1._abrirse_2._montar_a_horcajadas.png` |
| 165 | `LEXR-02191` | 1. adelante; 2. primero | diccionario_general | - [x] `diccionario_general/1._adelante;_2._primero.png` |
| 166 | `LEXR-02707` | 1. adelgazar; 2. rematar, acabar un trabajo | diccionario_general | - [x] `diccionario_general/1._adelgazar;_2._rematar,_acabar_un_trabajo.png` |
| 167 | `LEXR-00395` | 1. adormecer, causar sueño 2. acostar | diccionario_general | - [x] `diccionario_general/1._adormecer,_causar_sueño_2._acostar.png` |
| 168 | `LEXR-03762` | 1. adulto, maduro, título de respeto a mayores; 2. jecho, en sazón (fruta, etc.) | diccionario_general | - [x] `diccionario_general/1._adulto,_maduro,_título_de_respeto_a_mayores;_2._jecho,_en_sazón_(fruta,_etc._).png` |
| 169 | `LEXR-03297` | 1. agacharse; 2. prender candela | diccionario_general | - [x] `diccionario_general/1._agacharse;_2._prender_candela.png` |
| 170 | `LEXR-03879` | 1. agarrar por la cola; 2. (fig) fingir ser partidario de | diccionario_general | - [x] `diccionario_general/1._agarrar_por_la_cola;_2._(fig)_fingir_ser_partidario_de.png` |
| 171 | `LEXR-03524` | 1. alimentar; 2. hacer un flavor | diccionario_general | - [x] `diccionario_general/1._alimentar;_2._hacer_un_flavor.png` |
| 172 | `LEXR-02994` | 1. alzar, levantar, quitar; 2. edificar casa | diccionario_general | - [x] `diccionario_general/1._alzar,_levantar,_quitar;_2._edificar_casa.png` |
| 173 | `LEXR-01797` | 1. así 2. como, parecido | diccionario_general | - [x] `diccionario_general/1._así_2._como,_parecido.png` |
| 174 | `LEXR-02066` | 1. bajar algo (de arriba para abajo); 2. desensillar | diccionario_general | - [x] `diccionario_general/1._bajar_algo_(de_arriba_para_abajo);_2._desensillar.png` |
| 175 | `LEXR-02867` | 1. blandir (repetidas veces); 2. recoger con cuchara) | diccionario_general | - [x] `diccionario_general/1._blandir_(repetidas_veces);_2._recoger_con_cuchara).png` |
| 176 | `LEXR-01100` | 1. botar (repetidas veces); 2. apedrear | diccionario_general | - [x] `diccionario_general/1._botar_(repetidas_veces);_2._apedrear.png` |
| 177 | `LEXR-02731` | 1. caer encima de; 2. ser vencido | diccionario_general | - [x] `diccionario_general/1._caer_encima_de;_2._ser_vencido.png` |
| 178 | `LEXR-01948` | 1. cazar animales; 2. ladrar | diccionario_general | - [x] `diccionario_general/1._cazar_animales;_2._ladrar.png` |
| 179 | `LEXR-03580` | 1. cepillar, labrar madera; 2. rebanar | diccionario_general | - [x] `diccionario_general/1._cepillar,_labrar_madera;_2._rebanar.png` |
| 180 | `LEXR-03702` | 1. cercar; 2. cerrar los ojos | diccionario_general | - [x] `diccionario_general/1._cercar;_2._cerrar_los_ojos.png` |
| 181 | `LEXR-03727` | 1. chupar 2. absorbar 3. fumar (tobaco) | diccionario_general | - [x] `diccionario_general/1._chupar_2._absorbar_3._fumar_(tobaco).png` |
| 182 | `LEXR-01435` | 1. comer; 2. mascar coca, mambear; 3. picar | diccionario_general | - [x] `diccionario_general/1._comer;_2._mascar_coca,_mambear;_3._picar.png` |
| 183 | `LEXR-02540` | 1. contagiar, contaminar 2. perjudicar | diccionario_general | - [x] `diccionario_general/1._contagiar,_contaminar_2._perjudicar.png` |
| 184 | `LEXR-01395` | 1. contestar 2. comprometerse | diccionario_general | - [x] `diccionario_general/1._contestar_2._comprometerse.png` |
| 185 | `LEXR-02933` | 1. conversar, platicar, charlar 2. orar | diccionario_general | - [x] `diccionario_general/1._conversar,_platicar,_charlar_2._orar.png` |
| 186 | `LEXR-03394` | 1. cosechar, cortar café, fríjol; 2. desplumar | diccionario_general | - [x] `diccionario_general/1._cosechar,_cortar_café,_fríjol;_2._desplumar.png` |
| 187 | `LEXR-01694` | 1. cosechar, segar, cortar; 2. esquilar | diccionario_general | - [x] `diccionario_general/1._cosechar,_segar,_cortar;_2._esquilar.png` |
| 188 | `LEXR-01295` | 1. crecer (largo); 2. prolongarse, alargarse | diccionario_general | - [x] `diccionario_general/1._crecer_(largo);_2._prolongarse,_alargarse.png` |
| 189 | `LEXR-00907` | 1. cruzarse en el camino, entrecruzarse; 2. quitar tiempo, interrupir | diccionario_general | - [x] `diccionario_general/1._cruzarse_en_el_camino,_entrecruzarse;_2._quitar_tiempo,_interrupir.png` |
| 190 | `LEXR-00903` | 1. dar sabor, condimentar; 2. penetrar (ej. humo) | diccionario_general | - [x] `diccionario_general/1._dar_sabor,_condimentar;_2._penetrar_(ej._humo).png` |
| 191 | `LEXR-00987` | 1. dar sombra 2. servir como padrinos en las bodas | diccionario_general | - [x] `diccionario_general/1._dar_sombra_2._servir_como_padrinos_en_las_bodas.png` |
| 192 | `LEXR-00941` | 1. dar, conceder; 2. saludar, dar la mano | diccionario_general | - [x] `diccionario_general/1._dar,_conceder;_2._saludar,_dar_la_mano.png` |
| 193 | `LEXR-03204` | 1. dejar 2. designar 3. derrotar | diccionario_general | - [x] `diccionario_general/1._dejar_2._designar_3._derrotar.png` |
| 194 | `LEXR-03861` | 1. dejar pasar (para abajo) 2. celebrar fiesta | diccionario_general | - [x] `diccionario_general/1._dejar_pasar_(para_abajo)_2._celebrar_fiesta.png` |
| 195 | `LEXR-01348` | 1. delgado; 2.tono muy agudo (música) | diccionario_general | - [x] `diccionario_general/1._delgado;_2._tono_muy_agudo_(música).png` |
| 196 | `LEXR-01357` | 1. derrumbar 2. arar, sacar paladas | diccionario_general | - [x] `diccionario_general/1._derrumbar_2._arar,_sacar_paladas.png` |
| 197 | `LEXR-02136` | 1. derrumbarse; 2. mudar pluma | diccionario_general | - [x] `diccionario_general/1._derrumbarse;_2._mudar_pluma.png` |
| 198 | `LEXR-01739` | 1. despedazar 2. dar cambio (dinero) | diccionario_general | - [x] `diccionario_general/1._despedazar_2._dar_cambio_(dinero).png` |
| 199 | `LEXR-03758` | 1. despulpar 2. castrar (animales) | diccionario_general | - [x] `diccionario_general/1._despulpar_2._castrar_(animales).png` |
| 200 | `LEXR-00644` | 1. desyerbar, limpiar maleza; 2. desnudar, desvestir | diccionario_general | - [x] `diccionario_general/1._desyerbar,_limpiar_maleza;_2._desnudar,_desvestir.png` |
| 201 | `LEXR-01097` | 1. desyerbar, limpiar maleza; 2. juguetear | diccionario_general | - [x] `diccionario_general/1._desyerbar,_limpiar_maleza;_2._juguetear.png` |
| 202 | `LEXR-01334` | 1. desyerbar; 2. desvestir | diccionario_general | - [x] `diccionario_general/1._desyerbar;_2._desvestir.png` |
| 203 | `LEXR-03320` | 1. echar ramas; 2. tener vástago | diccionario_general | - [x] `diccionario_general/1._echar_ramas;_2._tener_vástago.png` |
| 204 | `LEXR-03370` | 1. el agua; 2. líquido | diccionario_general | - [x] `diccionario_general/1._el_agua;_2._líquido.png` |
| 205 | `LEXR-02807` | 1. el cuero, la piel 2. la cáscara, corteza de árbol | diccionario_general | - [x] `diccionario_general/1._el_cuero,_la_piel_2._la_cáscara,_corteza_de_árbol.png` |
| 206 | `LEXR-02537` | 1. el gato (mamífero); 2. el espíritu guardián (vitywe’sh) | diccionario_general | - [ ] falta |
| 207 | `LEXR-02951` | 1. el hombro, brazo 2. la brazada (medida | diccionario_general | - [x] `diccionario_general/1._el_hombro,_brazo_2._la_brazada_(medida.png` |
| 208 | `LEXR-02883` | 1. enderezar, alinear 2. rectificar | diccionario_general | - [x] `diccionario_general/1._enderezar,_alinear_2._rectificar.png` |
| 209 | `LEXR-03194` | 1. endurecer 2. cuajar (leche) | diccionario_general | - [x] `diccionario_general/1._endurecer_2._cuajar_(leche).png` |
| 210 | `LEXR-01156` | 1. enterrar, sepular; 2. hundirse | diccionario_general | - [x] `diccionario_general/1._enterrar,_sepular;_2._hundirse.png` |
| 211 | `LEXR-02230` | 1. escarmenar lana, cardar; 2. cosechar maíz | diccionario_general | - [x] `diccionario_general/1._escarmenar_lana,_cardar;_2._cosechar_maíz.png` |
| 212 | `LEXR-02727` | 1. estar agradecido, agradecer; 2. saludar, despedir, besar | diccionario_general | - [x] `diccionario_general/1._estar_agradecido,_agradecer;_2._saludar,_despedir,_besar.png` |
| 213 | `LEXR-02455` | 1. estar enfermo; 2. morir, fallecer | diccionario_general | - [x] `diccionario_general/1._estar_enfermo;_2._morir,_fallecer.png` |
| 214 | `LEXR-01819` | 1. frotar, fregar, ungir, untar; 2. afilar (machete, hacha); 3. restregar trigo (con un mazo) | diccionario_general | - [ ] falta |
| 215 | `LEXR-00629` | 1. gemir, gritar (de dolor) 2. mugir (vaca); 3. chillar; 4. relinchar (caballo), 5. cacarear (gallina), 6. maullar (gato) | diccionario_general | - [ ] falta |
| 216 | `LEXR-01946` | 1. golpear; 2. derribar, tumbar; 3. trillar | diccionario_general | - [ ] falta |
| 217 | `LEXR-02121` | 1. grueso, robusto; 2. nota muy baja (música) | diccionario_general | - [ ] falta |
| 218 | `LEXR-03058` | 1. guardar dieta; 2. guardar día de fiesta | diccionario_general | - [ ] falta |
| 219 | `LEXR-03226` | 1. hacer desyerbar 2. hacer entretenerse | diccionario_general | - [ ] falta |
| 220 | `LEXR-02912` | 1. hacer equivocar, hacer desviar 2. engañar | diccionario_general | - [ ] falta |
| 221 | `LEXR-00401` | 1. hacer sonar (un instrumento) 2. crujir los dientes 3. alborotar | diccionario_general | - [ ] falta |
| 222 | `LEXR-01562` | 1. hacer; 2. designar; 3. redimir | diccionario_general | - [ ] falta |
| 223 | `LEXR-00728` | 1. inclinar la cabeza; 2. quedar humillado | diccionario_general | - [ ] falta |
| 224 | `LEXR-03759` | 1. indígena páez 2. gente, persona | diccionario_general | - [ ] falta |
| 225 | `LEXR-03653` | 1. Intercambiar; 2. transformar | diccionario_general | - [ ] falta |
| 226 | `LEXR-02350` | 1. la boca; 2. el idioma; 3. el saludo; 4. asunto, noticia, razón | diccionario_general | - [ ] falta |
| 227 | `LEXR-01983` | 1. la comadreja (mamífero) 2. ser sobrenatural (mohán o moján) | diccionario_general | - [ ] falta |
| 228 | `LEXR-02356` | 1. la espuma 2. planta medicinal | diccionario_general | - [ ] falta |
| 229 | `LEXR-01781` | 1. la madeja de lana escarmenada 2. la pluma | diccionario_general | - [ ] falta |
| 230 | `LEXR-02560` | 1. la nalga, asentaderas; 2. fondo | diccionario_general | - [ ] falta |
| 231 | `LEXR-03688` | 1. los antepasados; 2. oficiales salientes | diccionario_general | - [ ] falta |
| 232 | `LEXR-03701` | 1. madurar; 2. envejecerse | diccionario_general | - [ ] falta |
| 233 | `LEXR-02884` | 1. mandar hacer 2. hacer celebrar misa | diccionario_general | - [ ] falta |
| 234 | `LEXR-03668` | 1. moder (perro, culebra); 2. picar | diccionario_general | - [ ] falta |
| 235 | `LEXR-02472` | 1. moler, exprimir 2. ordeñar vaca | diccionario_general | - [ ] falta |
| 236 | `LEXR-02076` | 1. nacer; 2. reventar (pollito) | diccionario_general | - [ ] falta |
| 237 | `LEXR-00429` | 1. pegarse a 2. asociarse con | diccionario_general | - [ ] falta |
| 238 | `LEXR-00749` | 1. pensar, acordarse; 2. confiar en; 3. dudar, vacilar; 4. sentirse triste, pensativo | diccionario_general | - [ ] falta |
| 239 | `LEXR-02052` | 1. poner atravesado (palo) 2. cruzar las piernas | diccionario_general | - [ ] falta |
| 240 | `LEXR-00924` | 1. poner en la cepo 2. poner horqueta (al puerco) | diccionario_general | - [ ] falta |
| 241 | `LEXR-03898` | 1. poner nombre; 2. bautizar | diccionario_general | - [ ] falta |
| 242 | `LEXR-03330` | 1. poner, colocar encima de 2. averiguar, investigar | diccionario_general | - [ ] falta |
| 243 | `LEXR-03521` | 1. poner, inyectar; 2. nombrar en un puesto | diccionario_general | - [ ] falta |
| 244 | `LEXR-01463` | 1. prometer 2. enterarse | diccionario_general | - [ ] falta |
| 245 | `LEXR-01065` | 1. quedarse 2. ser salvo 3. ser condenado | diccionario_general | - [ ] falta |
| 246 | `LEXR-03321` | 1. rasgar, romper; 2. changuar, separar hebras (de cabuya o bejuco) | diccionario_general | - [ ] falta |
| 247 | `LEXR-01312` | 1. repartir comida (entre varias personas) 2. meter caña (en la trapiche) | diccionario_general | - [ ] falta |
| 248 | `LEXR-03078` | 1. sacar 2. traducir | diccionario_general | - [ ] falta |
| 249 | `LEXR-00953` | 1. salir 2. nacer 3. resultar | diccionario_general | - [ ] falta |
| 250 | `LEXR-01353` | 1. saltar (repetidas veces); 2. palpitar, latir | diccionario_general | - [ ] falta |
| 251 | `LEXR-01763` | 1. secarse; 2. agotarse | diccionario_general | - [ ] falta |
| 252 | `LEXR-02880` | 1. sentarse 2. posar (ave) 3. aterrizar (avión) | diccionario_general | - [ ] falta |
| 253 | `LEXR-01422` | 1. tejer (jigra, ruana); 2. techar, empajar una casa | diccionario_general | - [ ] falta |
| 254 | `LEXR-03554` | 1. trabar, eredar 2. acornear | diccionario_general | - [ ] falta |
| 255 | `LEXR-03235` | 1. traer, llevar; 2. vestirse | diccionario_general | - [ ] falta |
| 256 | `LEXR-02571` | 1. untar 2. curtir (cuero) 3. desfibrar cabuya | diccionario_general | - [ ] falta |
| 257 | `LEXR-01011` | 1. uña (de persona); 2. dedo (medida, anchura de un dedo); 3. garra (de ave); 4. casco (de caballo); 5. pezuña (de animal) | diccionario_general | - [ ] falta |
| 258 | `LEXR-02942` | 1. ver, encontrar; 2. conseguir, hallar | diccionario_general | - [ ] falta |
| 259 | `LEXR-01084` | 1. vástago, renuevo de árbol o planta; 2. vástago, persona descendiente de otra | diccionario_general | - [ ] falta |
| 260 | `LEXR-01542` | 1. zafar, quitar 2. desenfrenar | diccionario_general | - [ ] falta |
| 261 | `LEXR-03343` | ?por qué? | diccionario_general | - [ ] falta |
| 262 | `LEXR-03139` | a favor de | diccionario_general | - [ ] falta |
| 263 | `LEXR-03855` | a la derecha | diccionario_general | - [x] `diccionario_general/a_la_derecha.png` |
| 264 | `LEXR-01158` | a la orilla de | diccionario_general | - [ ] falta |
| 265 | `LEXR-02714` | a orillas de | diccionario_general | - [x] `diccionario_general/a_orillas_de.png` |
| 266 | `LEXR-02783` | a tocar tambor | diccionario_general | - [x] `diccionario_general/a_tocar_tambor.png` |
| 267 | `LEXR-02315` | a través de, a lo largo de | diccionario_general | - [ ] falta |
| 268 | `LEXR-02494` | a un lado de | diccionario_general | - [ ] falta |
| 269 | `LEXR-03252` | a ver | diccionario_general | - [ ] falta |
| 270 | `LEXR-01830` | abadonado, cosa desechada | diccionario_general | - [x] `diccionario_general/abadonado,_cosa_desechada.png` |
| 271 | `LEXR-01774` | abajo | diccionario_general | - [x] `diccionario_general/abajo.png` |
| 272 | `LEXR-01249` | abajo en la quebrada | diccionario_general | - [x] `diccionario_general/abajo_en_la_quebrada.png` |
| 273 | `LEXR-01557` | abandonar | diccionario_general | - [ ] falta |
| 274 | `LEXR-02901` | abeja, abejón | diccionario_general | - [x] `diccionario_general/abeja,_abejón.png` |
| 275 | `LEXR-01961` | abiertamente, patente | diccionario_general | - [ ] falta |
| 276 | `LEXR-02249` | abogar, intervenir en un asunto | diccionario_general | - [ ] falta |
| 277 | `LEXR-03313` | abollar | diccionario_general | - [x] `diccionario_general/abollar.png` |
| 278 | `LEXR-02675` | abonar | diccionario_general | - [x] `diccionario_general/abonar.png` |
| 279 | `LEXR-01655` | abrigarse | diccionario_general | - [x] `diccionario_general/abrigarse.png` |
| 280 | `LEXR-01877` | abrir | diccionario_general | - [x] `diccionario_general/abrir.png` |
| 281 | `LEXR-02944` | abrir la boca | diccionario_general | - [x] `diccionario_general/abrir_la_boca.png` |
| 282 | `LEXR-01243` | abrirse, rajarse | diccionario_general | - [ ] falta |
| 283 | `LEXR-02411` | abuelo | diccionario_general | - [x] `diccionario_general/abuelo.png` |
| 284 | `LEXR-02059` | abuelo o abuela con nieto o nieta | diccionario_general | - [x] `diccionario_general/abuelo_o_abuela_con_nieto_o_nieta.png` |
| 285 | `LEXR-02966` | abundar, rendir | diccionario_general | - [ ] falta |
| 286 | `LEXR-00961` | aburrirse | diccionario_general | - [x] `diccionario_general/aburrirse.png` |
| 287 | `LEXR-00984` | acabar | diccionario_general | - [ ] falta |
| 288 | `LEXR-02008` | acabarse, darse por terminado | diccionario_general | - [ ] falta |
| 289 | `LEXR-03089` | acercar, arrimar | diccionario_general | - [ ] falta |
| 290 | `LEXR-03383` | acercarse voluntariamente | diccionario_general | - [ ] falta |
| 291 | `LEXR-01600` | acertadamente, sin equivocarse | diccionario_general | - [ ] falta |
| 292 | `LEXR-03478` | achicar, comprimir, reducir de tamaño | diccionario_general | - [ ] falta |
| 293 | `LEXR-01125` | aclarar el día | diccionario_general | - [ ] falta |
| 294 | `LEXR-02514` | aclarar, despejarse | diccionario_general | - [ ] falta |
| 295 | `LEXR-02461` | aclarar, ponerse claro | diccionario_general | - [ ] falta |
| 296 | `LEXR-00649` | aclarar, volverse claro (líquido) | diccionario_general | - [ ] falta |
| 297 | `LEXR-02842` | acogollar, echar cogollo | diccionario_general | - [ ] falta |
| 298 | `LEXR-02581` | acompañar | diccionario_general | - [x] `diccionario_general/acompañar.png` |
| 299 | `LEXR-01770` | aconjesar | diccionario_general | - [ ] falta |
| 300 | `LEXR-00664` | acontecer, suceder | diccionario_general | - [ ] falta |
| 301 | `LEXR-02168` | acortar (ej. estribos) | diccionario_general | - [ ] falta |
| 302 | `LEXR-00518` | acortar, caerse el pelo | diccionario_general | - [ ] falta |
| 303 | `LEXR-03302` | acortar, mermar | diccionario_general | - [ ] falta |
| 304 | `LEXR-01294` | acortarse | diccionario_general | - [ ] falta |
| 305 | `LEXR-02202` | activo | diccionario_general | - [ ] falta |
| 306 | `LEXR-03904` | activo, hábil | diccionario_general | - [ ] falta |
| 307 | `LEXR-02715` | acusar, presentar queja contra otra persona | diccionario_general | - [ ] falta |
| 308 | `LEXR-00680` | acá arriba | diccionario_general | - [ ] falta |
| 309 | `LEXR-03253` | acá, aquí | diccionario_general | - [ ] falta |
| 310 | `LEXR-02265` | adelantarse | diccionario_general | - [ ] falta |
| 311 | `LEXR-02459` | adelgazarse | diccionario_general | - [ ] falta |
| 312 | `LEXR-01913` | adentro | diccionario_general | - [ ] falta |
| 313 | `LEXR-01292` | adivino, persona que siente sensaciones | diccionario_general | - [ ] falta |
| 314 | `LEXR-01218` | adueñarse | diccionario_general | - [ ] falta |
| 315 | `LEXR-01713` | adulterio, inmoralidad | diccionario_general | - [ ] falta |
| 316 | `LEXR-03574` | adulto, mayor de edad | diccionario_general | - [ ] falta |
| 317 | `LEXR-01649` | adúltero/a | diccionario_general | - [ ] falta |
| 318 | `LEXR-00939` | afilar | diccionario_general | - [ ] falta |
| 319 | `LEXR-00719` | aflojar | diccionario_general | - [ ] falta |
| 320 | `LEXR-03818` | aflojar, dar campo | diccionario_general | - [ ] falta |
| 321 | `LEXR-02047` | aflojarse | diccionario_general | - [ ] falta |
| 322 | `LEXR-03671` | afta | diccionario_general | - [ ] falta |
| 323 | `LEXR-03850` | afuera | diccionario_general | - [ ] falta |
| 324 | `LEXR-03665` | agacharse (repetidas veces) | diccionario_general | - [ ] falta |
| 325 | `LEXR-02088` | agradable, apetecible | diccionario_general | - [ ] falta |
| 326 | `LEXR-01831` | agradable, sabroso, saludable, bien (de salud) | diccionario_general | - [ ] falta |
| 327 | `LEXR-00446` | agredirse (mutuamente) | diccionario_general | - [ ] falta |
| 328 | `LEXR-00823` | agrio, fermentado | diccionario_general | - [ ] falta |
| 329 | `LEXR-00750` | agua bendita | diccionario_general | - [x] `diccionario_general/agua_bendita.png` |
| 330 | `LEXR-01698` | agua fría | diccionario_general | - [x] `diccionario_general/agua_fría.png` |
| 331 | `LEXR-03305` | agua hervida | diccionario_general | - [x] `diccionario_general/agua_hervida.png` |
| 332 | `LEXR-03037` | agua hirviendo | diccionario_general | - [x] `diccionario_general/agua_hirviendo.png` |
| 333 | `LEXR-02818` | aguacero | diccionario_general | - [x] `diccionario_general/aguacero.png` |
| 334 | `LEXR-01212` | aguado | diccionario_general | - [ ] falta |
| 335 | `LEXR-01565` | aguantar | diccionario_general | - [ ] falta |
| 336 | `LEXR-03168` | agudo, puntiagudo | diccionario_general | - [ ] falta |
| 337 | `LEXR-01486` | agujerear, taladrar, perforar | diccionario_general | - [ ] falta |
| 338 | `LEXR-02802` | agutí | diccionario_general | - [ ] falta |
| 339 | `LEXR-01428` | agutí, guatuza, tuza (mamífero) | diccionario_general | - [x] `diccionario_general/agutí,_guatuza,_tuza_(mamífero).png` |
| 340 | `LEXR-03616` | agutí, guatín (mamífero roedor) | diccionario_general | - [ ] falta |
| 341 | `LEXR-02376` | ahijada | diccionario_general | - [ ] falta |
| 342 | `LEXR-02267` | ahijado | diccionario_general | - [ ] falta |
| 343 | `LEXR-03786` | ahogarse | diccionario_general | - [ ] falta |
| 344 | `LEXR-03115` | ahorcarse | diccionario_general | - [ ] falta |
| 345 | `LEXR-01454` | ahorrar (comida o dinero) | diccionario_general | - [ ] falta |
| 346 | `LEXR-03018` | ahorrar (varias cosas) | diccionario_general | - [ ] falta |
| 347 | `LEXR-01902` | ahumado | diccionario_general | - [ ] falta |
| 348 | `LEXR-03724` | ahumar | diccionario_general | - [ ] falta |
| 349 | `LEXR-02925` | ahuyentar pájaros | diccionario_general | - [ ] falta |
| 350 | `LEXR-00557` | ahí | diccionario_general | - [ ] falta |
| 351 | `LEXR-01264` | ajeno | diccionario_general | - [ ] falta |
| 352 | `LEXR-01806` | al amor, la misericordia | diccionario_general | - [ ] falta |
| 353 | `LEXR-01507` | al año pasado | diccionario_general | - [ ] falta |
| 354 | `LEXR-03057` | al borde de | diccionario_general | - [ ] falta |
| 355 | `LEXR-03740` | al canto de gallo | diccionario_general | - [x] `diccionario_general/al_canto_de_gallo.png` |
| 356 | `LEXR-00910` | al lado de | diccionario_general | - [ ] falta |
| 357 | `LEXR-01864` | al lado do | diccionario_general | - [ ] falta |
| 358 | `LEXR-01964` | al otro lado de la cordillera (ej. Tierradentro) | diccionario_general | - [ ] falta |
| 359 | `LEXR-00996` | al ponerse el sol | diccionario_general | - [x] `diccionario_general/al_ponerse_el_sol.png` |
| 360 | `LEXR-02853` | al principio | diccionario_general | - [ ] falta |
| 361 | `LEXR-00449` | al salir el sol | diccionario_general | - [x] `diccionario_general/al_salir_el_sol.png` |
| 362 | `LEXR-02627` | al través, horizontal | diccionario_general | - [ ] falta |
| 363 | `LEXR-01716` | ala de sombrero | diccionario_general | - [x] `diccionario_general/ala_de_sombrero.png` |
| 364 | `LEXR-02723` | alacrán | diccionario_general | - [ ] falta |
| 365 | `LEXR-03548` | alambre | diccionario_general | - [x] `diccionario_general/alambre.png` |
| 366 | `LEXR-00431` | alargar | diccionario_general | - [ ] falta |
| 367 | `LEXR-00923` | alcanzar | diccionario_general | - [ ] falta |
| 368 | `LEXR-02524` | alcanzar (en el camino) | diccionario_general | - [ ] falta |
| 369 | `LEXR-02041` | alcanzar a tocar, lograr tocar | diccionario_general | - [ ] falta |
| 370 | `LEXR-03666` | alchucha (planta comestible) | diccionario_general | - [x] `diccionario_general/alchucha_(planta_comestible).png` |
| 371 | `LEXR-02243` | alegrar | diccionario_general | - [ ] falta |
| 372 | `LEXR-01956` | alero | diccionario_general | - [ ] falta |
| 373 | `LEXR-01509` | aletear | diccionario_general | - [ ] falta |
| 374 | `LEXR-02341` | algo que ha sido escogido | diccionario_general | - [ ] falta |
| 375 | `LEXR-01411` | algo templado (freno) | diccionario_general | - [ ] falta |
| 376 | `LEXR-01773` | algo, bien | diccionario_general | - [ ] falta |
| 377 | `LEXR-01925` | alguacil | diccionario_general | - [ ] falta |
| 378 | `LEXR-00578` | aligerar | diccionario_general | - [ ] falta |
| 379 | `LEXR-03094` | alimentar, dar de comer | diccionario_general | - [x] `diccionario_general/alimentar,_dar_de_comer.png` |
| 380 | `LEXR-01664` | alisar | diccionario_general | - [ ] falta |
| 381 | `LEXR-01604` | aliviar | diccionario_general | - [ ] falta |
| 382 | `LEXR-02520` | aliviarse (de un dolor) | diccionario_general | - [ ] falta |
| 383 | `LEXR-00416` | allí | diccionario_general | - [ ] falta |
| 384 | `LEXR-01459` | alrededor | diccionario_general | - [ ] falta |
| 385 | `LEXR-01585` | altar dorado | diccionario_general | - [ ] falta |
| 386 | `LEXR-03091` | alumbrar a otro | diccionario_general | - [ ] falta |
| 387 | `LEXR-01375` | alumbrar, iluminar | diccionario_general | - [ ] falta |
| 388 | `LEXR-00535` | alumno de la escuela | diccionario_general | - [ ] falta |
| 389 | `LEXR-00443` | alzar | diccionario_general | - [ ] falta |
| 390 | `LEXR-01548` | alzar (repetidas veces) | diccionario_general | - [ ] falta |
| 391 | `LEXR-01439` | alzar era | diccionario_general | - [ ] falta |
| 392 | `LEXR-03742` | amamantar | diccionario_general | - [ ] falta |
| 393 | `LEXR-02492` | amanecer (el día) | diccionario_general | - [ ] falta |
| 394 | `LEXR-01873` | amanecer (la persona) | diccionario_general | - [ ] falta |
| 395 | `LEXR-02609` | amansar | diccionario_general | - [ ] falta |
| 396 | `LEXR-03773` | amansar, domesticar | diccionario_general | - [ ] falta |
| 397 | `LEXR-01573` | amargar, ponerse amargo | diccionario_general | - [ ] falta |
| 398 | `LEXR-02091` | amarillento | diccionario_general | - [ ] falta |
| 399 | `LEXR-01251` | amarillo | diccionario_general | - [ ] falta |
| 400 | `LEXR-01993` | amarillo claro | diccionario_general | - [ ] falta |
| 401 | `LEXR-02282` | amarrar (varias veces) | diccionario_general | - [ ] falta |
| 402 | `LEXR-00714` | amarrar nudo | diccionario_general | - [ ] falta |
| 403 | `LEXR-03660` | amarrar varias vueltas | diccionario_general | - [ ] falta |
| 404 | `LEXR-02019` | amarrar, atara | diccionario_general | - [ ] falta |
| 405 | `LEXR-03662` | amarse (mutuamente) | diccionario_general | - [ ] falta |
| 406 | `LEXR-03061` | amañarse, acostumbrarse | diccionario_general | - [ ] falta |
| 407 | `LEXR-02309` | ambos | diccionario_general | - [ ] falta |
| 408 | `LEXR-02820` | ambos lados, de lado a lado (opuesto) | diccionario_general | - [ ] falta |
| 409 | `LEXR-02491` | amontonar | diccionario_general | - [ ] falta |
| 410 | `LEXR-03760` | amor, misericordia | diccionario_general | - [ ] falta |
| 411 | `LEXR-03484` | ampolla | diccionario_general | - [ ] falta |
| 412 | `LEXR-02602` | ampollarse | diccionario_general | - [ ] falta |
| 413 | `LEXR-02107` | anaco | diccionario_general | - [ ] falta |
| 414 | `LEXR-01111` | anaco abierto | diccionario_general | - [ ] falta |
| 415 | `LEXR-01367` | anaco tubular | diccionario_general | - [ ] falta |
| 416 | `LEXR-00512` | anca | diccionario_general | - [ ] falta |
| 417 | `LEXR-02234` | ancho, anchura | diccionario_general | - [ ] falta |
| 418 | `LEXR-00504` | Andaquí (indígena de la tribu Andaquí) | diccionario_general | - [ ] falta |
| 419 | `LEXR-03780` | andar, caminar | diccionario_general | - [ ] falta |
| 420 | `LEXR-01901` | andas (para llevar cadáveres) | diccionario_general | - [ ] falta |
| 421 | `LEXR-00442` | angosto, estecho | diccionario_general | - [ ] falta |
| 422 | `LEXR-02217` | anguilla (ave) | diccionario_general | - [ ] falta |
| 423 | `LEXR-02336` | anillo, sortija | diccionario_general | - [ ] falta |
| 424 | `LEXR-01414` | animal domesticado | diccionario_general | - [x] `diccionario_general/animal_domesticado.png` |
| 425 | `LEXR-02130` | animal doméstico | diccionario_general | - [x] `diccionario_general/animal_doméstico.png` |
| 426 | `LEXR-00752` | animal salvaje | diccionario_general | - [x] `diccionario_general/animal_salvaje.png` |
| 427 | `LEXR-03258` | animal salvaje, fiera, el demonio | diccionario_general | - [x] `diccionario_general/animal_salvaje,_fiera,_el_demonio.png` |
| 428 | `LEXR-01984` | anochecer | diccionario_general | - [ ] falta |
| 429 | `LEXR-02367` | ansia, náusea | diccionario_general | - [ ] falta |
| 430 | `LEXR-02412` | anteayer, antier | diccionario_general | - [ ] falta |
| 431 | `LEXR-03644` | antenoche | diccionario_general | - [ ] falta |
| 432 | `LEXR-02161` | antepasados | diccionario_general | - [ ] falta |
| 433 | `LEXR-02079` | anzuelo | diccionario_general | - [ ] falta |
| 434 | `LEXR-00413` | apagar | diccionario_general | - [ ] falta |
| 435 | `LEXR-00576` | apagarse | diccionario_general | - [ ] falta |
| 436 | `LEXR-02051` | aparar | diccionario_general | - [ ] falta |
| 437 | `LEXR-01004` | aparar agua | diccionario_general | - [x] `diccionario_general/aparar_agua.png` |
| 438 | `LEXR-03068` | aparecer, estar presente | diccionario_general | - [ ] falta |
| 439 | `LEXR-00968` | aparte, separado | diccionario_general | - [ ] falta |
| 440 | `LEXR-02174` | apelldio | diccionario_general | - [ ] falta |
| 441 | `LEXR-00448` | apellido | diccionario_general | - [ ] falta |
| 442 | `LEXR-01823` | apisonar | diccionario_general | - [ ] falta |
| 443 | `LEXR-00548` | aplastar | diccionario_general | - [ ] falta |
| 444 | `LEXR-01950` | aplastar (repetidas veces), hacer arepa | diccionario_general | - [ ] falta |
| 445 | `LEXR-00798` | aplaudir (dar repetidas palmadas) | diccionario_general | - [ ] falta |
| 446 | `LEXR-00985` | aprender | diccionario_general | - [ ] falta |
| 447 | `LEXR-02074` | apresurarse, tener tiempo | diccionario_general | - [ ] falta |
| 448 | `LEXR-03719` | apretado | diccionario_general | - [ ] falta |
| 449 | `LEXR-00407` | apretar | diccionario_general | - [ ] falta |
| 450 | `LEXR-02058` | apretarse | diccionario_general | - [ ] falta |
| 451 | `LEXR-01857` | aprisa, rápido, pronto | diccionario_general | - [ ] falta |
| 452 | `LEXR-02921` | apuntar (un arma) | diccionario_general | - [ ] falta |
| 453 | `LEXR-02839` | aquí | diccionario_general | - [ ] falta |
| 454 | `LEXR-01419` | araña | diccionario_general | - [x] `diccionario_general/araña.png` |
| 455 | `LEXR-02448` | arbusto, usan la hoja para lastimaduras | diccionario_general | - [ ] falta |
| 456 | `LEXR-00408` | arco de noche | diccionario_general | - [ ] falta |
| 457 | `LEXR-03657` | arco del día | diccionario_general | - [ ] falta |
| 458 | `LEXR-03398` | arder | diccionario_general | - [ ] falta |
| 459 | `LEXR-00638` | ardilla | diccionario_general | - [x] `diccionario_general/ardilla.png` |
| 460 | `LEXR-01207` | arenoso | diccionario_general | - [ ] falta |
| 461 | `LEXR-02278` | arete | diccionario_general | - [ ] falta |
| 462 | `LEXR-03629` | argumentar | diccionario_general | - [ ] falta |
| 463 | `LEXR-02886` | arisco, esquivo | diccionario_general | - [ ] falta |
| 464 | `LEXR-02970` | armadillo | diccionario_general | - [x] `diccionario_general/armadillo.png` |
| 465 | `LEXR-02736` | arracacha | diccionario_general | - [ ] falta |
| 466 | `LEXR-01121` | arrancar | diccionario_general | - [ ] falta |
| 467 | `LEXR-03377` | arrancar espigas | diccionario_general | - [ ] falta |
| 468 | `LEXR-02743` | arrancar, desarraigar | diccionario_general | - [ ] falta |
| 469 | `LEXR-01122` | arrancarse | diccionario_general | - [ ] falta |
| 470 | `LEXR-00527` | arreglar | diccionario_general | - [ ] falta |
| 471 | `LEXR-02291` | arreglar un asunto | diccionario_general | - [ ] falta |
| 472 | `LEXR-01193` | arrendar (terreno) | diccionario_general | - [ ] falta |
| 473 | `LEXR-02070` | arriba | diccionario_general | - [ ] falta |
| 474 | `LEXR-01471` | arrodillarse | diccionario_general | - [ ] falta |
| 475 | `LEXR-02939` | arrollar, arremangar | diccionario_general | - [ ] falta |
| 476 | `LEXR-02635` | arrugar | diccionario_general | - [ ] falta |
| 477 | `LEXR-01120` | arrugarse | diccionario_general | - [ ] falta |
| 478 | `LEXR-03768` | asaltador | diccionario_general | - [ ] falta |
| 479 | `LEXR-00758` | asaltar, agredir | diccionario_general | - [ ] falta |
| 480 | `LEXR-00776` | asar | diccionario_general | - [ ] falta |
| 481 | `LEXR-01194` | asco, cosa desagrable | diccionario_general | - [ ] falta |
| 482 | `LEXR-01870` | asentadero de la olla | diccionario_general | - [x] `diccionario_general/asentadero_de_la_olla.png` |
| 483 | `LEXR-01708` | asfixiarse | diccionario_general | - [ ] falta |
| 484 | `LEXR-01843` | asno | diccionario_general | - [ ] falta |
| 485 | `LEXR-02154` | asociarse con | diccionario_general | - [ ] falta |
| 486 | `LEXR-00705` | asomar | diccionario_general | - [ ] falta |
| 487 | `LEXR-01679` | astilla | diccionario_general | - [ ] falta |
| 488 | `LEXR-02821` | asunto de terrenos | diccionario_general | - [ ] falta |
| 489 | `LEXR-02036` | asustar a otra persona | diccionario_general | - [ ] falta |
| 490 | `LEXR-01886` | así, asimismo | diccionario_general | - [ ] falta |
| 491 | `LEXR-02718` | atar palos verticales | diccionario_general | - [ ] falta |
| 492 | `LEXR-00602` | atardecer | diccionario_general | - [ ] falta |
| 493 | `LEXR-01176` | atarraya | diccionario_general | - [ ] falta |
| 494 | `LEXR-03691` | atemorizarse | diccionario_general | - [ ] falta |
| 495 | `LEXR-00505` | atento | diccionario_general | - [ ] falta |
| 496 | `LEXR-03385` | atizar (la lumbre) | diccionario_general | - [x] `diccionario_general/atizar_(la_lumbre).png` |
| 497 | `LEXR-03183` | atizar la candela | diccionario_general | - [ ] falta |
| 498 | `LEXR-03202` | atragantarse | diccionario_general | - [ ] falta |
| 499 | `LEXR-02296` | atrancar | diccionario_general | - [ ] falta |
| 500 | `LEXR-03158` | atrapar, coger con trampa | diccionario_general | - [ ] falta |
| 501 | `LEXR-03549` | atravesar, cruzar, pasar al otro lado | diccionario_general | - [ ] falta |
| 502 | `LEXR-03196` | atrás, detrás | diccionario_general | - [ ] falta |
| 503 | `LEXR-02439` | aventajar | diccionario_general | - [ ] falta |
| 504 | `LEXR-02158` | aventar | diccionario_general | - [ ] falta |
| 505 | `LEXR-03460` | aventar trigo | diccionario_general | - [x] `diccionario_general/aventar_trigo.png` |
| 506 | `LEXR-02419` | avergonzar, causar pena | diccionario_general | - [ ] falta |
| 507 | `LEXR-03913` | avisar (al mismo tiempo que hace otra cosa) | diccionario_general | - [ ] falta |
| 508 | `LEXR-00905` | avisar (repetidas veces o a varias personas) | diccionario_general | - [ ] falta |
| 509 | `LEXR-01934` | avisar, anunciar, informar, señalar | diccionario_general | - [ ] falta |
| 510 | `LEXR-03783` | avisar, traer un mensaje | diccionario_general | - [ ] falta |
| 511 | `LEXR-03294` | aviso, anuncio | diccionario_general | - [ ] falta |
| 512 | `LEXR-03142` | avispa | diccionario_general | - [x] `diccionario_general/avispa.png` |
| 513 | `LEXR-03684` | avispa (insecto) | diccionario_general | - [x] `diccionario_general/avispa_(insecto).png` |
| 514 | `LEXR-01710` | avispado, vivo | diccionario_general | - [ ] falta |
| 515 | `LEXR-00485` | avío (comida para el camino) | diccionario_general | - [ ] falta |
| 516 | `LEXR-03541` | ayer | diccionario_general | - [ ] falta |
| 517 | `LEXR-01681` | ayudar (por turno) | diccionario_general | - [ ] falta |
| 518 | `LEXR-02713` | ayudar, apoyar | diccionario_general | - [ ] falta |
| 519 | `LEXR-00633` | ayudarse (mutuamente) | diccionario_general | - [ ] falta |
| 520 | `LEXR-00573` | ayunar | diccionario_general | - [ ] falta |
| 521 | `LEXR-02354` | azul celeste | diccionario_general | - [ ] falta |
| 522 | `LEXR-01944` | azul claro | diccionario_general | - [ ] falta |
| 523 | `LEXR-01043` | azul subido | diccionario_general | - [ ] falta |
| 524 | `LEXR-03686` | azul, verde | diccionario_general | - [ ] falta |
| 525 | `LEXR-00451` | añadir, pegar con goma | diccionario_general | - [ ] falta |
| 526 | `LEXR-02444` | baba | diccionario_general | - [ ] falta |
| 527 | `LEXR-01105` | bagazo | diccionario_general | - [ ] falta |
| 528 | `LEXR-03016` | bailador | diccionario_general | - [ ] falta |
| 529 | `LEXR-00403` | bailar | diccionario_general | - [x] `diccionario_general/bailar.png` |
| 530 | `LEXR-01947` | baile de la boda | diccionario_general | - [ ] falta |
| 531 | `LEXR-01040` | baile de la chucha | diccionario_general | - [ ] falta |
| 532 | `LEXR-02470` | baile de la chucha (un año después de edificar una casa) | diccionario_general | - [ ] falta |
| 533 | `LEXR-03372` | baile de un niño muerto | diccionario_general | - [ ] falta |
| 534 | `LEXR-02387` | baile en una minga | diccionario_general | - [ ] falta |
| 535 | `LEXR-00729` | bajar | diccionario_general | - [x] `diccionario_general/bajar.png` |
| 536 | `LEXR-03509` | bajar, descender | diccionario_general | - [ ] falta |
| 537 | `LEXR-01206` | bajar, descender, caber, ponserse el sol | diccionario_general | - [ ] falta |
| 538 | `LEXR-01992` | bajar, desmontar | diccionario_general | - [ ] falta |
| 539 | `LEXR-02268` | bajar, desmontar (de una bestia) | diccionario_general | - [ ] falta |
| 540 | `LEXR-01213` | bajo (estatura) | diccionario_general | - [ ] falta |
| 541 | `LEXR-01662` | balanza, romana | diccionario_general | - [ ] falta |
| 542 | `LEXR-00524` | banca (para sentarse) | diccionario_general | - [ ] falta |
| 543 | `LEXR-02667` | barato | diccionario_general | - [ ] falta |
| 544 | `LEXR-01942` | barbasco (planta venenosa) | diccionario_general | - [x] `diccionario_general/barbasco_(planta_venenosa).png` |
| 545 | `LEXR-01397` | barranco | diccionario_general | - [ ] falta |
| 546 | `LEXR-02926` | barrer | diccionario_general | - [ ] falta |
| 547 | `LEXR-00899` | barretón | diccionario_general | - [ ] falta |
| 548 | `LEXR-01393` | barsino | diccionario_general | - [ ] falta |
| 549 | `LEXR-01637` | batata | diccionario_general | - [ ] falta |
| 550 | `LEXR-03467` | bautizado | diccionario_general | - [ ] falta |
| 551 | `LEXR-02558` | bautizo | diccionario_general | - [ ] falta |
| 552 | `LEXR-03411` | bayo | diccionario_general | - [ ] falta |
| 553 | `LEXR-02670` | bayo cariblanco | diccionario_general | - [ ] falta |
| 554 | `LEXR-01161` | bañarse | diccionario_general | - [ ] falta |
| 555 | `LEXR-03200` | bañarse (con remedio) | diccionario_general | - [ ] falta |
| 556 | `LEXR-01998` | beber (lo ajeno) | diccionario_general | - [x] `diccionario_general/beber_(lo_ajeno).png` |
| 557 | `LEXR-02896` | beber, tomar | diccionario_general | - [ ] falta |
| 558 | `LEXR-00537` | bejuco | diccionario_general | - [ ] falta |
| 559 | `LEXR-03164` | bendecir | diccionario_general | - [ ] falta |
| 560 | `LEXR-03812` | bien tejido (jigra, canasta, ruana) | diccionario_general | - [x] `diccionario_general/bien_tejido_(jigra,_canasta,_ruana).png` |
| 561 | `LEXR-02103` | bien, bueno | diccionario_general | - [ ] falta |
| 562 | `LEXR-02377` | bienes, posesiones | diccionario_general | - [ ] falta |
| 563 | `LEXR-03003` | bienestar, felicidad | diccionario_general | - [ ] falta |
| 564 | `LEXR-03421` | bigote, barba | diccionario_general | - [ ] falta |
| 565 | `LEXR-03274` | billete | diccionario_general | - [ ] falta |
| 566 | `LEXR-02109` | biznieto, biznieta | diccionario_general | - [ ] falta |
| 567 | `LEXR-01038` | blanco | diccionario_general | - [ ] falta |
| 568 | `LEXR-01537` | blanco (persona de raza blanca) | diccionario_general | - [ ] falta |
| 569 | `LEXR-02361` | blancuzco | diccionario_general | - [ ] falta |
| 570 | `LEXR-00841` | blandir (bastón) | diccionario_general | - [ ] falta |
| 571 | `LEXR-01868` | blando | diccionario_general | - [ ] falta |
| 572 | `LEXR-01118` | blanquear | diccionario_general | - [ ] falta |
| 573 | `LEXR-00657` | bobo, tímido | diccionario_general | - [ ] falta |
| 574 | `LEXR-00632` | boca abajo | diccionario_general | - [ ] falta |
| 575 | `LEXR-02156` | bordón, bastón | diccionario_general | - [ ] falta |
| 576 | `LEXR-01954` | borrachero (árbol venenosa y narcótico) | diccionario_general | - [ ] falta |
| 577 | `LEXR-01850` | borrar, limpiar (fregando) | diccionario_general | - [ ] falta |
| 578 | `LEXR-03778` | botar (al viento), regar, arrojar | diccionario_general | - [ ] falta |
| 579 | `LEXR-00662` | botar, tirar | diccionario_general | - [ ] falta |
| 580 | `LEXR-01409` | bramar | diccionario_general | - [ ] falta |
| 581 | `LEXR-01485` | brea | diccionario_general | - [x] `diccionario_general/brea.png` |
| 582 | `LEXR-03052` | breve | diccionario_general | - [x] `diccionario_general/breve.png` |
| 583 | `LEXR-00908` | brillar | diccionario_general | - [ ] falta |
| 584 | `LEXR-02496` | bromeador, chistoso | diccionario_general | - [ ] falta |
| 585 | `LEXR-02891` | bromear, chancear | diccionario_general | - [ ] falta |
| 586 | `LEXR-03137` | bueno, fino | diccionario_general | - [ ] falta |
| 587 | `LEXR-01303` | burlar | diccionario_general | - [ ] falta |
| 588 | `LEXR-03146` | burlar, hacer burla | diccionario_general | - [ ] falta |
| 589 | `LEXR-02117` | buscar | diccionario_general | - [ ] falta |
| 590 | `LEXR-00595` | búho | diccionario_general | - [ ] falta |
| 591 | `LEXR-03198` | caballo | diccionario_general | - [x] `diccionario_general/caballo.png` |
| 592 | `LEXR-00993` | cabecear | diccionario_general | - [ ] falta |
| 593 | `LEXR-01588` | cabra | diccionario_general | - [x] `diccionario_general/cabra.png` |
| 594 | `LEXR-00945` | cabuyal, roza de cabuya | diccionario_general | - [ ] falta |
| 595 | `LEXR-00605` | cada | diccionario_general | - [ ] falta |
| 596 | `LEXR-02028` | cada saliente del vértice de techo | diccionario_general | - [ ] falta |
| 597 | `LEXR-02598` | cadera | diccionario_general | - [ ] falta |
| 598 | `LEXR-01096` | cadáver | diccionario_general | - [ ] falta |
| 599 | `LEXR-00469` | caer | diccionario_general | - [ ] falta |
| 600 | `LEXR-01510` | caer encima de | diccionario_general | - [ ] falta |
| 601 | `LEXR-01285` | caer granizo, granizar | diccionario_general | - [x] `diccionario_general/caer_granizo,_granizar.png` |
| 602 | `LEXR-02365` | caer rayo | diccionario_general | - [x] `diccionario_general/caer_rayo.png` |
| 603 | `LEXR-03792` | cafeto (árbol) | diccionario_general | - [x] `diccionario_general/cafeto_(árbol).png` |
| 604 | `LEXR-01760` | calabazo (en forma de gancho) | diccionario_general | - [x] `diccionario_general/calabazo_(en_forma_de_gancho).png` |
| 605 | `LEXR-01621` | calabazo (en forma embudo) | diccionario_general | - [x] `diccionario_general/calabazo_(en_forma_embudo).png` |
| 606 | `LEXR-02452` | calabazo (para sevir chicha) | diccionario_general | - [x] `diccionario_general/calabazo_(para_sevir_chicha).png` |
| 607 | `LEXR-01320` | calambre | diccionario_general | - [x] `diccionario_general/calambre.png` |
| 608 | `LEXR-03528` | calavera | diccionario_general | - [x] `diccionario_general/calavera.png` |
| 609 | `LEXR-03361` | caldo | diccionario_general | - [x] `diccionario_general/caldo.png` |
| 610 | `LEXR-00487` | calentar | diccionario_general | - [x] `diccionario_general/calentar.png` |
| 611 | `LEXR-01112` | calentar (a otro) | diccionario_general | - [ ] falta |
| 612 | `LEXR-00482` | calentarse | diccionario_general | - [ ] falta |
| 613 | `LEXR-01025` | caliente | diccionario_general | - [x] `diccionario_general/caliente.png` |
| 614 | `LEXR-00465` | callado | diccionario_general | - [ ] falta |
| 615 | `LEXR-01619` | callar, hacer callar | diccionario_general | - [ ] falta |
| 616 | `LEXR-03231` | callo | diccionario_general | - [ ] falta |
| 617 | `LEXR-03392` | calmarse, cesar | diccionario_general | - [x] `diccionario_general/calmarse,_cesar.png` |
| 618 | `LEXR-02000` | calumniar, criticar | diccionario_general | - [ ] falta |
| 619 | `LEXR-03112` | calvo | diccionario_general | - [x] `diccionario_general/calvo.png` |
| 620 | `LEXR-02372` | cambiar de aspecto | diccionario_general | - [ ] falta |
| 621 | `LEXR-02485` | camino de herradura | diccionario_general | - [x] `diccionario_general/camino_de_herradura.png` |
| 622 | `LEXR-03374` | campo de coca | diccionario_general | - [x] `diccionario_general/campo_de_coca.png` |
| 623 | `LEXR-01863` | candelilla (insecto) | diccionario_general | - [x] `diccionario_general/candelilla_(insecto).png` |
| 624 | `LEXR-01570` | cangrejo | diccionario_general | - [x] `diccionario_general/cangrejo.png` |
| 625 | `LEXR-03731` | cansar, fatigar | diccionario_general | - [x] `diccionario_general/cansar,_fatigar.png` |
| 626 | `LEXR-01012` | cansarse | diccionario_general | - [ ] falta |
| 627 | `LEXR-00456` | canturrear | diccionario_general | - [x] `diccionario_general/canturrear.png` |
| 628 | `LEXR-01986` | capa de maíz | diccionario_general | - [x] `diccionario_general/capa_de_maíz.png` |
| 629 | `LEXR-00531` | cara a cara | diccionario_general | - [x] `diccionario_general/cara_a_cara.png` |
| 630 | `LEXR-01162` | caracol | diccionario_general | - [x] `diccionario_general/caracol.png` |
| 631 | `LEXR-02701` | carbón, brasa | diccionario_general | - [x] `diccionario_general/carbón,_brasa.png` |
| 632 | `LEXR-03756` | cardar lana | diccionario_general | - [x] `diccionario_general/cardar_lana.png` |
| 633 | `LEXR-02759` | careto, cariblanco | diccionario_general | - [ ] falta |
| 634 | `LEXR-01832` | cargadera (de la jigra) | diccionario_general | - [ ] falta |
| 635 | `LEXR-03067` | cargar | diccionario_general | - [x] `diccionario_general/cargar.png` |
| 636 | `LEXR-03887` | cargar a cuestas | diccionario_general | - [x] `diccionario_general/cargar_a_cuestas.png` |
| 637 | `LEXR-01513` | cargar debajo del brazo | diccionario_general | - [x] `diccionario_general/cargar_debajo_del_brazo.png` |
| 638 | `LEXR-03885` | cargar sobre sí mismo | diccionario_general | - [ ] falta |
| 639 | `LEXR-00932` | caripaspada, de mejillas rosadas | diccionario_general | - [ ] falta |
| 640 | `LEXR-02299` | carna pulpa | diccionario_general | - [x] `diccionario_general/carna_pulpa.png` |
| 641 | `LEXR-02349` | carne de la cadera | diccionario_general | - [ ] falta |
| 642 | `LEXR-02323` | caro | diccionario_general | - [ ] falta |
| 643 | `LEXR-03049` | carpintero | diccionario_general | - [x] `diccionario_general/carpintero.png` |
| 644 | `LEXR-03811` | carrizo de guadua | diccionario_general | - [x] `diccionario_general/carrizo_de_guadua.png` |
| 645 | `LEXR-02779` | casar, legalizar matrimonio | diccionario_general | - [ ] falta |
| 646 | `LEXR-01049` | casarse (dícese de la mujer) | diccionario_general | - [ ] falta |
| 647 | `LEXR-01730` | casarse (dícese del hombre) | diccionario_general | - [ ] falta |
| 648 | `LEXR-01080` | casarse, formar pareja | diccionario_general | - [ ] falta |
| 649 | `LEXR-00511` | casco (del caballo) | diccionario_general | - [x] `diccionario_general/casco_(del_caballo).png` |
| 650 | `LEXR-00579` | casi | diccionario_general | - [ ] falta |
| 651 | `LEXR-02478` | caspi (árbol) | diccionario_general | - [x] `diccionario_general/caspi_(árbol).png` |
| 652 | `LEXR-02607` | castaño | diccionario_general | - [x] `diccionario_general/castaño.png` |
| 653 | `LEXR-02271` | castellano (idioma) | diccionario_general | - [ ] falta |
| 654 | `LEXR-03379` | castrar, capar | diccionario_general | - [ ] falta |
| 655 | `LEXR-03375` | causar dolor o enfermedad | diccionario_general | - [ ] falta |
| 656 | `LEXR-01723` | causar hambre | diccionario_general | - [ ] falta |
| 657 | `LEXR-01446` | causar pereza, desanimar | diccionario_general | - [ ] falta |
| 658 | `LEXR-03077` | causar sentir ’señas’ | diccionario_general | - [ ] falta |
| 659 | `LEXR-03610` | causar sombra | diccionario_general | - [ ] falta |
| 660 | `LEXR-01936` | cavar cámara lateral para enterrar | diccionario_general | - [ ] falta |
| 661 | `LEXR-02420` | cavar zanja | diccionario_general | - [ ] falta |
| 662 | `LEXR-03427` | cavar, abrir hoyo, ahuecar | diccionario_general | - [x] `diccionario_general/cavar,_abrir_hoyo,_ahuecar.png` |
| 663 | `LEXR-01491` | cazador | diccionario_general | - [x] `diccionario_general/cazador.png` |
| 664 | `LEXR-01374` | caña de maíz | diccionario_general | - [x] `diccionario_general/caña_de_maíz.png` |
| 665 | `LEXR-01896` | cañaduzal | diccionario_general | - [x] `diccionario_general/cañaduzal.png` |
| 666 | `LEXR-03498` | celebrar en baile | diccionario_general | - [ ] falta |
| 667 | `LEXR-03914` | celos | diccionario_general | - [ ] falta |
| 668 | `LEXR-01553` | centella (planta) | diccionario_general | - [x] `diccionario_general/centella_(planta).png` |
| 669 | `LEXR-02138` | cerca | diccionario_general | - [x] `diccionario_general/cerca.png` |
| 670 | `LEXR-02628` | cerca a | diccionario_general | - [ ] falta |
| 671 | `LEXR-00454` | cerca de alambre | diccionario_general | - [x] `diccionario_general/cerca_de_alambre.png` |
| 672 | `LEXR-01275` | cerca de cabuya | diccionario_general | - [ ] falta |
| 673 | `LEXR-03628` | cerca de carrizo | diccionario_general | - [ ] falta |
| 674 | `LEXR-00881` | cerca de lechero | diccionario_general | - [ ] falta |
| 675 | `LEXR-01328` | cerca de palos verticales | diccionario_general | - [ ] falta |
| 676 | `LEXR-03124` | cerca hecha de palos verticales | diccionario_general | - [ ] falta |
| 677 | `LEXR-01002` | cercar la hortaliza | diccionario_general | - [ ] falta |
| 678 | `LEXR-03084` | cerco de lechero | diccionario_general | - [ ] falta |
| 679 | `LEXR-01130` | cerdo, marrano, puerco | diccionario_general | - [x] `diccionario_general/cerdo,_marrano,_puerco.png` |
| 680 | `LEXR-02649` | cernidor, cernedor, cedazo, susunga | diccionario_general | - [x] `diccionario_general/cernidor,_cernedor,_cedazo,_susunga.png` |
| 681 | `LEXR-00582` | cernir, cerner, colar | diccionario_general | - [ ] falta |
| 682 | `LEXR-01653` | cerote (árbol) | diccionario_general | - [ ] falta |
| 683 | `LEXR-01192` | cerrado | diccionario_general | - [ ] falta |
| 684 | `LEXR-03339` | cerrar la boca | diccionario_general | - [ ] falta |
| 685 | `LEXR-02513` | cerrar, tapar, cubrir | diccionario_general | - [ ] falta |
| 686 | `LEXR-03635` | ceñirse | diccionario_general | - [ ] falta |
| 687 | `LEXR-03710` | ceñirse, amarrar (con correa o chumbe) | diccionario_general | - [ ] falta |
| 688 | `LEXR-03002` | chachafruto (árbol) | diccionario_general | - [x] `diccionario_general/chachafruto_(árbol).png` |
| 689 | `LEXR-01044` | chamuscar | diccionario_general | - [ ] falta |
| 690 | `LEXR-02342` | chamón (ave dañina) | diccionario_general | - [ ] falta |
| 691 | `LEXR-03924` | chasquear, rechinar | diccionario_general | - [ ] falta |
| 692 | `LEXR-03249` | chicga de caña, guarapo | diccionario_general | - [ ] falta |
| 693 | `LEXR-01362` | chicha de maíz | diccionario_general | - [ ] falta |
| 694 | `LEXR-00387` | chicha dulce de maíz | diccionario_general | - [ ] falta |
| 695 | `LEXR-03874` | chicha fermentada | diccionario_general | - [ ] falta |
| 696 | `LEXR-00683` | chicharrón | diccionario_general | - [ ] falta |
| 697 | `LEXR-01259` | chiflar | diccionario_general | - [ ] falta |
| 698 | `LEXR-02830` | chiflar (repetidas veces) | diccionario_general | - [ ] falta |
| 699 | `LEXR-01634` | chirriar | diccionario_general | - [ ] falta |
| 700 | `LEXR-00631` | chistoso | diccionario_general | - [ ] falta |
| 701 | `LEXR-03648` | chocar con | diccionario_general | - [ ] falta |
| 702 | `LEXR-00922` | choclo cocido | diccionario_general | - [ ] falta |
| 703 | `LEXR-01754` | chorrear | diccionario_general | - [ ] falta |
| 704 | `LEXR-03241` | chorrear, escurrir | diccionario_general | - [ ] falta |
| 705 | `LEXR-02018` | choza, con techo de paja | diccionario_general | - [ ] falta |
| 706 | `LEXR-01133` | chulco (plana medicinal) | diccionario_general | - [ ] falta |
| 707 | `LEXR-03275` | chulco (planta medicinal) | diccionario_general | - [x] `diccionario_general/chulco_(planta_medicinal).png` |
| 708 | `LEXR-03858` | chupar caña | diccionario_general | - [ ] falta |
| 709 | `LEXR-02001` | chuzar (aprovechando ausencia del dueño) | diccionario_general | - [ ] falta |
| 710 | `LEXR-01349` | chuzar, punzar | diccionario_general | - [ ] falta |
| 711 | `LEXR-02937` | cidrayota | diccionario_general | - [ ] falta |
| 712 | `LEXR-03098` | ciempiés | diccionario_general | - [ ] falta |
| 713 | `LEXR-03128` | ciertamente | diccionario_general | - [ ] falta |
| 714 | `LEXR-00754` | cierto, ciertamente | diccionario_general | - [ ] falta |
| 715 | `LEXR-01252` | cinchar, asegurar la silla con cincha | diccionario_general | - [ ] falta |
| 716 | `LEXR-03356` | cinturón | diccionario_general | - [ ] falta |
| 717 | `LEXR-02768` | ciruelo (árbol) | diccionario_general | - [ ] falta |
| 718 | `LEXR-03530` | claro de huevo | diccionario_general | - [x] `diccionario_general/claro_de_huevo.png` |
| 719 | `LEXR-00994` | clavar varias estacas | diccionario_general | - [ ] falta |
| 720 | `LEXR-02043` | clavar, acuñar (teja, maíz), abrochar, abotonar | diccionario_general | - [ ] falta |
| 721 | `LEXR-02391` | clavar, poner estaca | diccionario_general | - [ ] falta |
| 722 | `LEXR-03624` | cloquear | diccionario_general | - [ ] falta |
| 723 | `LEXR-01525` | coatí, cusumbe | diccionario_general | - [ ] falta |
| 724 | `LEXR-03490` | cobijarse con otra persona | diccionario_general | - [ ] falta |
| 725 | `LEXR-02384` | cobijarse, taparse | diccionario_general | - [ ] falta |
| 726 | `LEXR-01345` | cobrador | diccionario_general | - [ ] falta |
| 727 | `LEXR-00755` | cobrar una deuda | diccionario_general | - [ ] falta |
| 728 | `LEXR-00480` | coca | diccionario_general | - [ ] falta |
| 729 | `LEXR-03422` | cocer | diccionario_general | - [ ] falta |
| 730 | `LEXR-02646` | cocido | diccionario_general | - [ ] falta |
| 731 | `LEXR-00717` | cocinar | diccionario_general | - [x] `diccionario_general/cocinar.png` |
| 732 | `LEXR-03045` | cocinar yerba | diccionario_general | - [x] `diccionario_general/cocinar_yerba.png` |
| 733 | `LEXR-00988` | coger (algo que viene del rumbo opuesto), apañar | diccionario_general | - [ ] falta |
| 734 | `LEXR-00975` | coger rastro (repetidas veces) | diccionario_general | - [ ] falta |
| 735 | `LEXR-01231` | coger sin permiso | diccionario_general | - [ ] falta |
| 736 | `LEXR-01028` | coger, llevar en la mano | diccionario_general | - [ ] falta |
| 737 | `LEXR-03559` | cogollo | diccionario_general | - [ ] falta |
| 738 | `LEXR-00946` | cogollo de fique | diccionario_general | - [ ] falta |
| 739 | `LEXR-01386` | cojear | diccionario_general | - [ ] falta |
| 740 | `LEXR-02989` | cojo | diccionario_general | - [ ] falta |
| 741 | `LEXR-00873` | colerín | diccionario_general | - [ ] falta |
| 742 | `LEXR-00802` | colgado | diccionario_general | - [ ] falta |
| 743 | `LEXR-03890` | colgante | diccionario_general | - [ ] falta |
| 744 | `LEXR-01442` | colgar | diccionario_general | - [ ] falta |
| 745 | `LEXR-02877` | colgar (varias cosas) | diccionario_general | - [ ] falta |
| 746 | `LEXR-03350` | colgarse, ahorcarse | diccionario_general | - [ ] falta |
| 747 | `LEXR-00600` | colibrí, esmeralda | diccionario_general | - [x] `diccionario_general/colibrí,_esmeralda.png` |
| 748 | `LEXR-01030` | colocar espantapájaros (en los sembrados) | diccionario_general | - [ ] falta |
| 749 | `LEXR-01684` | color claro | diccionario_general | - [ ] falta |
| 750 | `LEXR-01382` | colorado, rojizo | diccionario_general | - [ ] falta |
| 751 | `LEXR-01943` | columna vertebral | diccionario_general | - [ ] falta |
| 752 | `LEXR-03301` | columpiar | diccionario_general | - [ ] falta |
| 753 | `LEXR-01630` | comadreja | diccionario_general | - [ ] falta |
| 754 | `LEXR-01661` | comején | diccionario_general | - [ ] falta |
| 755 | `LEXR-01381` | comer | diccionario_general | - [x] `diccionario_general/comer.png` |
| 756 | `LEXR-00825` | comer demasiado | diccionario_general | - [x] `diccionario_general/comer_demasiado.png` |
| 757 | `LEXR-01668` | comer lo ajeno | diccionario_general | - [x] `diccionario_general/comer_lo_ajeno.png` |
| 758 | `LEXR-00763` | comestible | diccionario_general | - [ ] falta |
| 759 | `LEXR-03496` | cometer adulterio | diccionario_general | - [ ] falta |
| 760 | `LEXR-02086` | cometer falta, incumplir, ser indigno | diccionario_general | - [ ] falta |
| 761 | `LEXR-02146` | comida, alimento | diccionario_general | - [ ] falta |
| 762 | `LEXR-01900` | como si fuera | diccionario_general | - [ ] falta |
| 763 | `LEXR-02789` | como, ¿cómo? | diccionario_general | - [ ] falta |
| 764 | `LEXR-03382` | comoquiera | diccionario_general | - [ ] falta |
| 765 | `LEXR-02163` | compartir | diccionario_general | - [ ] falta |
| 766 | `LEXR-00523` | compartir el llanto de otro | diccionario_general | - [ ] falta |
| 767 | `LEXR-00433` | compartir el sufrimiento de otro | diccionario_general | - [ ] falta |
| 768 | `LEXR-01803` | compartir la comida de otro | diccionario_general | - [ ] falta |
| 769 | `LEXR-00722` | compartir la tristeza de otro | diccionario_general | - [ ] falta |
| 770 | `LEXR-00434` | compartir tristeza de otro | diccionario_general | - [ ] falta |
| 771 | `LEXR-02123` | compartir, colaborar | diccionario_general | - [ ] falta |
| 772 | `LEXR-01449` | completar | diccionario_general | - [ ] falta |
| 773 | `LEXR-02557` | comprado, compra | diccionario_general | - [ ] falta |
| 774 | `LEXR-01340` | comprador, que compra | diccionario_general | - [ ] falta |
| 775 | `LEXR-03643` | comprometida (la novia) | diccionario_general | - [ ] falta |
| 776 | `LEXR-01579` | con | diccionario_general | - [ ] falta |
| 777 | `LEXR-00435` | con las uñas, garras | diccionario_general | - [ ] falta |
| 778 | `LEXR-00942` | con sabor de humo | diccionario_general | - [ ] falta |
| 779 | `LEXR-01219` | con señal, marca | diccionario_general | - [ ] falta |
| 780 | `LEXR-03404` | con ustedes | diccionario_general | - [ ] falta |
| 781 | `LEXR-02775` | conciencia | diccionario_general | - [ ] falta |
| 782 | `LEXR-00950` | conciliar | diccionario_general | - [ ] falta |
| 783 | `LEXR-01660` | condenar | diccionario_general | - [ ] falta |
| 784 | `LEXR-03690` | condolerse, compartir la flicción de otro | diccionario_general | - [ ] falta |
| 785 | `LEXR-01211` | conejo | diccionario_general | - [x] `diccionario_general/conejo.png` |
| 786 | `LEXR-03641` | conejo (mamífero) | diccionario_general | - [x] `diccionario_general/conejo_(mamífero).png` |
| 787 | `LEXR-03106` | confesar (al cura) | diccionario_general | - [ ] falta |
| 788 | `LEXR-01958` | confluencia de dos ríos o quebradas | diccionario_general | - [ ] falta |
| 789 | `LEXR-00883` | confrontar | diccionario_general | - [ ] falta |
| 790 | `LEXR-02920` | confundir, perturbar | diccionario_general | - [ ] falta |
| 791 | `LEXR-03863` | congelarse | diccionario_general | - [ ] falta |
| 792 | `LEXR-02887` | conocimiento | diccionario_general | - [ ] falta |
| 793 | `LEXR-03903` | consolar | diccionario_general | - [ ] falta |
| 794 | `LEXR-02495` | consolarse | diccionario_general | - [ ] falta |
| 795 | `LEXR-03520` | consolarse (mutuamente) | diccionario_general | - [ ] falta |
| 796 | `LEXR-03566` | contagiarse | diccionario_general | - [ ] falta |
| 797 | `LEXR-03025` | contagioso | diccionario_general | - [ ] falta |
| 798 | `LEXR-01878` | contaminar | diccionario_general | - [ ] falta |
| 799 | `LEXR-02108` | contar, medir, pesar | diccionario_general | - [ ] falta |
| 800 | `LEXR-03312` | contar, relatar | diccionario_general | - [ ] falta |
| 801 | `LEXR-00769` | contentar | diccionario_general | - [ ] falta |
| 802 | `LEXR-02186` | contento | diccionario_general | - [ ] falta |
| 803 | `LEXR-02668` | contestación | diccionario_general | - [ ] falta |
| 804 | `LEXR-03480` | contestar (repetidas veces) | diccionario_general | - [ ] falta |
| 805 | `LEXR-01530` | contigo, con usted | diccionario_general | - [ ] falta |
| 806 | `LEXR-02762` | conversación, plática, charla | diccionario_general | - [ ] falta |
| 807 | `LEXR-01331` | conversar, charlar | diccionario_general | - [ ] falta |
| 808 | `LEXR-02483` | convivir, cohabitar | diccionario_general | - [ ] falta |
| 809 | `LEXR-02721` | coral (víbora) | diccionario_general | - [ ] falta |
| 810 | `LEXR-00452` | corar (varias cosas) | diccionario_general | - [ ] falta |
| 811 | `LEXR-02287` | corazón de buey | diccionario_general | - [ ] falta |
| 812 | `LEXR-01949` | corcovear | diccionario_general | - [ ] falta |
| 813 | `LEXR-03703` | corredor | diccionario_general | - [ ] falta |
| 814 | `LEXR-01016` | correr | diccionario_general | - [x] `diccionario_general/correr.png` |
| 815 | `LEXR-03349` | correr brisa | diccionario_general | - [ ] falta |
| 816 | `LEXR-02615` | corriente del río tendido | diccionario_general | - [ ] falta |
| 817 | `LEXR-03300` | cortar | diccionario_general | - [ ] falta |
| 818 | `LEXR-01493` | cortar (en muchos pedazos) | diccionario_general | - [ ] falta |
| 819 | `LEXR-02135` | cortar (en varios pedazos) | diccionario_general | - [ ] falta |
| 820 | `LEXR-03066` | cortar, trozar | diccionario_general | - [ ] falta |
| 821 | `LEXR-01055` | cortarse | diccionario_general | - [ ] falta |
| 822 | `LEXR-02508` | cortarse (a sí mismo) | diccionario_general | - [ ] falta |
| 823 | `LEXR-03659` | cortarse (el pelo) | diccionario_general | - [ ] falta |
| 824 | `LEXR-01624` | corto | diccionario_general | - [ ] falta |
| 825 | `LEXR-02975` | cosa agradable | diccionario_general | - [ ] falta |
| 826 | `LEXR-01117` | cosa gruesa | diccionario_general | - [ ] falta |
| 827 | `LEXR-03347` | cosa usada, no nueva | diccionario_general | - [ ] falta |
| 828 | `LEXR-00463` | cosechar | diccionario_general | - [ ] falta |
| 829 | `LEXR-01650` | coser, costurar | diccionario_general | - [ ] falta |
| 830 | `LEXR-01526` | cosquillas | diccionario_general | - [ ] falta |
| 831 | `LEXR-03886` | cosquilloso | diccionario_general | - [ ] falta |
| 832 | `LEXR-02360` | costura | diccionario_general | - [ ] falta |
| 833 | `LEXR-02096` | coyuntura del pie | diccionario_general | - [ ] falta |
| 834 | `LEXR-00650` | crear fama | diccionario_general | - [ ] falta |
| 835 | `LEXR-01891` | crecer | diccionario_general | - [ ] falta |
| 836 | `LEXR-03755` | crecer (el monte) | diccionario_general | - [ ] falta |
| 837 | `LEXR-01045` | creer | diccionario_general | - [ ] falta |
| 838 | `LEXR-02549` | crespo | diccionario_general | - [ ] falta |
| 839 | `LEXR-03837` | creyente, que confía en Dios | diccionario_general | - [ ] falta |
| 840 | `LEXR-02888` | criar hijos | diccionario_general | - [ ] falta |
| 841 | `LEXR-00978` | criatura, bebé | diccionario_general | - [ ] falta |
| 842 | `LEXR-02988` | crin | diccionario_general | - [ ] falta |
| 843 | `LEXR-01183` | crudo | diccionario_general | - [ ] falta |
| 844 | `LEXR-01129` | cruzar, pasar al otro lado | diccionario_general | - [ ] falta |
| 845 | `LEXR-03407` | cráneo | diccionario_general | - [ ] falta |
| 846 | `LEXR-02619` | cual, cualquier, alguno | diccionario_general | - [ ] falta |
| 847 | `LEXR-02752` | cualquiera | diccionario_general | - [ ] falta |
| 848 | `LEXR-00892` | cualquiera, quienquiera | diccionario_general | - [ ] falta |
| 849 | `LEXR-01969` | cuando | diccionario_general | - [ ] falta |
| 850 | `LEXR-00422` | cuando, ¿cuándo?, ¿a qué horas? | diccionario_general | - [ ] falta |
| 851 | `LEXR-01388` | cuandoquiera, cualquier hora | diccionario_general | - [ ] falta |
| 852 | `LEXR-00385` | cuandoquiera, siempre | diccionario_general | - [ ] falta |
| 853 | `LEXR-02620` | cuanto | diccionario_general | - [ ] falta |
| 854 | `LEXR-03053` | cuanto (distancia), ¿cuánto? | diccionario_general | - [ ] falta |
| 855 | `LEXR-02577` | cuanto, ¿cuánto? | diccionario_general | - [ ] falta |
| 856 | `LEXR-01731` | cuartilla | diccionario_general | - [ ] falta |
| 857 | `LEXR-02215` | cuarto | diccionario_general | - [ ] falta |
| 858 | `LEXR-03181` | cuatro | diccionario_general | - [ ] falta |
| 859 | `LEXR-01479` | cubios | diccionario_general | - [ ] falta |
| 860 | `LEXR-03553` | cubrir, tapar (con cobija) | diccionario_general | - [ ] falta |
| 861 | `LEXR-03687` | cubrirse (ej. con un pañolón) | diccionario_general | - [ ] falta |
| 862 | `LEXR-01089` | cucarrón | diccionario_general | - [ ] falta |
| 863 | `LEXR-00736` | cuchara | diccionario_general | - [x] `diccionario_general/cuchara.png` |
| 864 | `LEXR-03255` | cuchara (hecha de calabaza) | diccionario_general | - [x] `diccionario_general/cuchara_(hecha_de_calabaza).png` |
| 865 | `LEXR-01894` | cuenca del ojo | diccionario_general | - [ ] falta |
| 866 | `LEXR-01029` | cuerno, cacho | diccionario_general | - [ ] falta |
| 867 | `LEXR-03479` | cuidar de, vigilar (en ausencia del dueño) | diccionario_general | - [ ] falta |
| 868 | `LEXR-02833` | culpable | diccionario_general | - [ ] falta |
| 869 | `LEXR-01626` | culpar, juzgar | diccionario_general | - [ ] falta |
| 870 | `LEXR-03188` | cumbrera de la casa, caballete | diccionario_general | - [x] `diccionario_general/cumbrera_de_la_casa,_caballete.png` |
| 871 | `LEXR-02304` | cumplir, llevar a cabo | diccionario_general | - [ ] falta |
| 872 | `LEXR-01272` | curar, dar remedio, medicinar | diccionario_general | - [ ] falta |
| 873 | `LEXR-01502` | curuba | diccionario_general | - [ ] falta |
| 874 | `LEXR-02306` | curíbano (planta) | diccionario_general | - [x] `diccionario_general/curíbano_(planta).png` |
| 875 | `LEXR-02845` | cuí, conejillo de indias | diccionario_general | - [x] `diccionario_general/cuí,_conejillo_de_indias.png` |
| 876 | `LEXR-00529` | cuñada con cuñada | diccionario_general | - [ ] falta |
| 877 | `LEXR-03387` | cuñado con cuñada | diccionario_general | - [ ] falta |
| 878 | `LEXR-02007` | cuñado con cuñado | diccionario_general | - [ ] falta |
| 879 | `LEXR-00445` | cámara lateral para entierro | diccionario_general | - [ ] falta |
| 880 | `LEXR-02143` | cáscara de huevo | diccionario_general | - [x] `diccionario_general/cáscara_de_huevo.png` |
| 881 | `LEXR-01280` | cóndor | diccionario_general | - [x] `diccionario_general/cóndor.png` |
| 882 | `LEXR-02575` | danta | diccionario_general | - [ ] falta |
| 883 | `LEXR-03471` | dar a la hija en casamiento, permitir a la hija casarse | diccionario_general | - [ ] falta |
| 884 | `LEXR-03459` | dar asco, desagradar | diccionario_general | - [ ] falta |
| 885 | `LEXR-03015` | dar ataque | diccionario_general | - [ ] falta |
| 886 | `LEXR-00904` | dar bofetadas | diccionario_general | - [ ] falta |
| 887 | `LEXR-03893` | dar calambre | diccionario_general | - [ ] falta |
| 888 | `LEXR-01430` | dar de beber | diccionario_general | - [x] `diccionario_general/dar_de_beber.png` |
| 889 | `LEXR-02906` | dar de beber (a varias personas, o varias veces) | diccionario_general | - [ ] falta |
| 890 | `LEXR-00757` | dar de beber (varias veces) | diccionario_general | - [x] `diccionario_general/dar_de_beber_(varias_veces).png` |
| 891 | `LEXR-00759` | dar fruto, cargar | diccionario_general | - [ ] falta |
| 892 | `LEXR-02172` | dar hipo | diccionario_general | - [ ] falta |
| 893 | `LEXR-03817` | dar la mano, saludar | diccionario_general | - [ ] falta |
| 894 | `LEXR-01358` | dar latigo | diccionario_general | - [ ] falta |
| 895 | `LEXR-02386` | dar látigo | diccionario_general | - [ ] falta |
| 896 | `LEXR-02815` | dar látigo (repetidas veces) | diccionario_general | - [ ] falta |
| 897 | `LEXR-02171` | dar paliza | diccionario_general | - [ ] falta |
| 898 | `LEXR-01470` | dar paliza (repetidas veces) | diccionario_general | - [ ] falta |
| 899 | `LEXR-01549` | dar rabia | diccionario_general | - [ ] falta |
| 900 | `LEXR-01124` | dar rejo, castigar | diccionario_general | - [ ] falta |
| 901 | `LEXR-01524` | dar sed, causar sed | diccionario_general | - [ ] falta |
| 902 | `LEXR-00490` | dar un paso | diccionario_general | - [ ] falta |
| 903 | `LEXR-01037` | dar varios pasos | diccionario_general | - [ ] falta |
| 904 | `LEXR-01417` | dar volteretas | diccionario_general | - [ ] falta |
| 905 | `LEXR-03631` | dar vuelta | diccionario_general | - [ ] falta |
| 906 | `LEXR-01056` | dar vuelta alrededor de | diccionario_general | - [ ] falta |
| 907 | `LEXR-00544` | dar vuelta, girar | diccionario_general | - [ ] falta |
| 908 | `LEXR-03131` | darle un ataque | diccionario_general | - [ ] falta |
| 909 | `LEXR-03072` | darse por terminado (un pleito) | diccionario_general | - [ ] falta |
| 910 | `LEXR-02503` | darse, producirse (plantas) | diccionario_general | - [ ] falta |
| 911 | `LEXR-03269` | dañarse | diccionario_general | - [ ] falta |
| 912 | `LEXR-00733` | de abajo | diccionario_general | - [ ] falta |
| 913 | `LEXR-03288` | de antemano | diccionario_general | - [ ] falta |
| 914 | `LEXR-02778` | de aquí | diccionario_general | - [ ] falta |
| 915 | `LEXR-00862` | de arriba para abajo | diccionario_general | - [ ] falta |
| 916 | `LEXR-03565` | de donde, ¿de dónde? | diccionario_general | - [ ] falta |
| 917 | `LEXR-02612` | de dos en dos | diccionario_general | - [ ] falta |
| 918 | `LEXR-01990` | de la misma edad | diccionario_general | - [ ] falta |
| 919 | `LEXR-03340` | de la misma tribu páez | diccionario_general | - [ ] falta |
| 920 | `LEXR-00912` | de lado, al soslayo | diccionario_general | - [ ] falta |
| 921 | `LEXR-02640` | de mal genio, bravo | diccionario_general | - [ ] falta |
| 922 | `LEXR-03209` | de presto, un momento | diccionario_general | - [ ] falta |
| 923 | `LEXR-01639` | de un lado a otro | diccionario_general | - [ ] falta |
| 924 | `LEXR-02828` | de una vez, directamente | diccionario_general | - [ ] falta |
| 925 | `LEXR-01974` | decir malas palabras | diccionario_general | - [ ] falta |
| 926 | `LEXR-01110` | decolgar, desengarzar | diccionario_general | - [ ] falta |
| 927 | `LEXR-02089` | defecar (repetidas veces) | diccionario_general | - [ ] falta |
| 928 | `LEXR-03911` | defecar, cagar (animales) | diccionario_general | - [ ] falta |
| 929 | `LEXR-00721` | defender, amparar, salvar | diccionario_general | - [ ] falta |
| 930 | `LEXR-03230` | defenderse | diccionario_general | - [ ] falta |
| 931 | `LEXR-01975` | deja pasar (al través) | diccionario_general | - [ ] falta |
| 932 | `LEXR-00389` | dejar acompañar, permitir acompañar | diccionario_general | - [ ] falta |
| 933 | `LEXR-00860` | dejar bajo custodia de otro | diccionario_general | - [ ] falta |
| 934 | `LEXR-03497` | dejar crecer el pelo | diccionario_general | - [ ] falta |
| 935 | `LEXR-02916` | dejar fermentar | diccionario_general | - [ ] falta |
| 936 | `LEXR-03286` | dejar hablar, permitir hablar | diccionario_general | - [ ] falta |
| 937 | `LEXR-03075` | dejar hervir | diccionario_general | - [x] `diccionario_general/dejar_hervir.png` |
| 938 | `LEXR-00865` | dejar mojar | diccionario_general | - [ ] falta |
| 939 | `LEXR-01365` | dejar pasar (para arriba) | diccionario_general | - [ ] falta |
| 940 | `LEXR-01116` | dejar pasar más tiempo | diccionario_general | - [ ] falta |
| 941 | `LEXR-01717` | dejar pegar, permitir pegar | diccionario_general | - [ ] falta |
| 942 | `LEXR-01648` | dejar robar | diccionario_general | - [ ] falta |
| 943 | `LEXR-01596` | dejar tocar, permitir tocar | diccionario_general | - [ ] falta |
| 944 | `LEXR-00470` | dejarse alcanzar | diccionario_general | - [ ] falta |
| 945 | `LEXR-02574` | dejarse coger | diccionario_general | - [ ] falta |
| 946 | `LEXR-02902` | dejarse engañar | diccionario_general | - [ ] falta |
| 947 | `LEXR-01874` | delgado | diccionario_general | - [ ] falta |
| 948 | `LEXR-02313` | demorar | diccionario_general | - [ ] falta |
| 949 | `LEXR-00474` | demorar (hasta mediodía) | diccionario_general | - [ ] falta |
| 950 | `LEXR-00653` | demorar (poco tiempo) | diccionario_general | - [ ] falta |
| 951 | `LEXR-01287` | demostrar sueño, transnochar | diccionario_general | - [ ] falta |
| 952 | `LEXR-02917` | derecho, recto | diccionario_general | - [ ] falta |
| 953 | `LEXR-00725` | derramar (líquido) | diccionario_general | - [ ] falta |
| 954 | `LEXR-02022` | derramarse, desbordarse | diccionario_general | - [ ] falta |
| 955 | `LEXR-01400` | derretirse | diccionario_general | - [ ] falta |
| 956 | `LEXR-01480` | derribar, tumbar | diccionario_general | - [ ] falta |
| 957 | `LEXR-01745` | desaparecer, ocultarse | diccionario_general | - [ ] falta |
| 958 | `LEXR-01640` | desarraigarse | diccionario_general | - [ ] falta |
| 959 | `LEXR-02097` | desatar | diccionario_general | - [ ] falta |
| 960 | `LEXR-03563` | desatar nudo | diccionario_general | - [ ] falta |
| 961 | `LEXR-03472` | desbaratar (varias cosas) | diccionario_general | - [ ] falta |
| 962 | `LEXR-00974` | descansar | diccionario_general | - [ ] falta |
| 963 | `LEXR-00609` | descargarse, librarse de | diccionario_general | - [ ] falta |
| 964 | `LEXR-02527` | descascarar | diccionario_general | - [ ] falta |
| 965 | `LEXR-01658` | descendiente | diccionario_general | - [ ] falta |
| 966 | `LEXR-01142` | desclavar (un clavo), desbotonar | diccionario_general | - [ ] falta |
| 967 | `LEXR-01289` | desclavar, desprenderse, zafarse | diccionario_general | - [ ] falta |
| 968 | `LEXR-03133` | descolgar (varias cosas), quitar | diccionario_general | - [ ] falta |
| 969 | `LEXR-01369` | descolgar, quitar | diccionario_general | - [ ] falta |
| 970 | `LEXR-01385` | descolgarse, librarse de, desechar una acusación | diccionario_general | - [ ] falta |
| 971 | `LEXR-02434` | desconocer | diccionario_general | - [ ] falta |
| 972 | `LEXR-00796` | desconocido | diccionario_general | - [ ] falta |
| 973 | `LEXR-03618` | descoser (una costura) | diccionario_general | - [ ] falta |
| 974 | `LEXR-01651` | descoser (varias costuras) | diccionario_general | - [ ] falta |
| 975 | `LEXR-02957` | descoyuntar | diccionario_general | - [ ] falta |
| 976 | `LEXR-02792` | descoyuntar, dislocar | diccionario_general | - [ ] falta |
| 977 | `LEXR-02310` | descoyuntarse | diccionario_general | - [ ] falta |
| 978 | `LEXR-02162` | descuido | diccionario_general | - [ ] falta |
| 979 | `LEXR-01297` | desde la niñez | diccionario_general | - [ ] falta |
| 980 | `LEXR-03866` | desde, de donde | diccionario_general | - [ ] falta |
| 981 | `LEXR-03540` | desear | diccionario_general | - [ ] falta |
| 982 | `LEXR-01865` | desenfundar (machete), dar a luz | diccionario_general | - [ ] falta |
| 983 | `LEXR-03113` | desenredar | diccionario_general | - [ ] falta |
| 984 | `LEXR-01580` | desenvolver | diccionario_general | - [ ] falta |
| 985 | `LEXR-01953` | desenvuelto | diccionario_general | - [ ] falta |
| 986 | `LEXR-01558` | deseo, voluntad | diccionario_general | - [ ] falta |
| 987 | `LEXR-03649` | desgajar | diccionario_general | - [ ] falta |
| 988 | `LEXR-02766` | desgajar (varias veces o varias ramas) | diccionario_general | - [ ] falta |
| 989 | `LEXR-03572` | desgajarse, desprenderse | diccionario_general | - [ ] falta |
| 990 | `LEXR-02335` | desgarjarse, desprenderse | diccionario_general | - [ ] falta |
| 991 | `LEXR-02065` | desgarrar (varias tiras) | diccionario_general | - [ ] falta |
| 992 | `LEXR-02398` | desgarrarse (en varias partes) | diccionario_general | - [ ] falta |
| 993 | `LEXR-03599` | desgranar | diccionario_general | - [ ] falta |
| 994 | `LEXR-03483` | desgranar, cosechar | diccionario_general | - [ ] falta |
| 995 | `LEXR-03744` | deshincharse | diccionario_general | - [ ] falta |
| 996 | `LEXR-02737` | deshojar | diccionario_general | - [ ] falta |
| 997 | `LEXR-02573` | deshojar (maíz) | diccionario_general | - [ ] falta |
| 998 | `LEXR-03504` | desmenuzar, hacer polvo de | diccionario_general | - [ ] falta |
| 999 | `LEXR-03833` | desmoronar | diccionario_general | - [ ] falta |
| 1000 | `LEXR-00997` | desnudarse, desvestirse | diccionario_general | - [ ] falta |
| 1001 | `LEXR-02588` | desnudo, pelado | diccionario_general | - [ ] falta |
| 1002 | `LEXR-03266` | despajar | diccionario_general | - [ ] falta |
| 1003 | `LEXR-03122` | despedazarse (en varias partes) | diccionario_general | - [ ] falta |
| 1004 | `LEXR-03788` | despegar, quitar coas pegada | diccionario_general | - [ ] falta |
| 1005 | `LEXR-02142` | despertar | diccionario_general | - [ ] falta |
| 1006 | `LEXR-02985` | despertar (a otro) | diccionario_general | - [ ] falta |
| 1007 | `LEXR-01582` | desplomarse, tambalear | diccionario_general | - [ ] falta |
| 1008 | `LEXR-00496` | desplumar | diccionario_general | - [ ] falta |
| 1009 | `LEXR-02600` | despreciado, odiado | diccionario_general | - [ ] falta |
| 1010 | `LEXR-00677` | despreciar | diccionario_general | - [ ] falta |
| 1011 | `LEXR-03190` | despreciar, odiar | diccionario_general | - [ ] falta |
| 1012 | `LEXR-03761` | despreciarse (mutuamente) | diccionario_general | - [ ] falta |
| 1013 | `LEXR-03552` | desprecio | diccionario_general | - [ ] falta |
| 1014 | `LEXR-00495` | desprender | diccionario_general | - [ ] falta |
| 1015 | `LEXR-00689` | desprenderse | diccionario_general | - [ ] falta |
| 1016 | `LEXR-02613` | después (posterioridad de tiempo) | diccionario_general | - [ ] falta |
| 1017 | `LEXR-00688` | destetar | diccionario_general | - [ ] falta |
| 1018 | `LEXR-01748` | destructivo | diccionario_general | - [ ] falta |
| 1019 | `LEXR-01035` | desvelar, no dejar dormir | diccionario_general | - [ ] falta |
| 1020 | `LEXR-01871` | detener, retener | diccionario_general | - [ ] falta |
| 1021 | `LEXR-01022` | deudor | diccionario_general | - [ ] falta |
| 1022 | `LEXR-02604` | devolver | diccionario_general | - [ ] falta |
| 1023 | `LEXR-02329` | dibujo | diccionario_general | - [ ] falta |
| 1024 | `LEXR-01688` | dibujo que usan para el chumbe | diccionario_general | - [ ] falta |
| 1025 | `LEXR-01057` | dicho | diccionario_general | - [ ] falta |
| 1026 | `LEXR-02764` | diente delantero | diccionario_general | - [ ] falta |
| 1027 | `LEXR-01592` | diez | diccionario_general | - [ ] falta |
| 1028 | `LEXR-00647` | dificultad | diccionario_general | - [ ] falta |
| 1029 | `LEXR-02457` | difunto, a | diccionario_general | - [ ] falta |
| 1030 | `LEXR-02972` | difícil | diccionario_general | - [ ] falta |
| 1031 | `LEXR-03175` | Dios | diccionario_general | - [ ] falta |
| 1032 | `LEXR-02551` | disfrazarse (pintar la cara) | diccionario_general | - [ ] falta |
| 1033 | `LEXR-03577` | disgustarse | diccionario_general | - [ ] falta |
| 1034 | `LEXR-00672` | disminuir | diccionario_general | - [ ] falta |
| 1035 | `LEXR-01216` | distinto, diferente, extraño | diccionario_general | - [ ] falta |
| 1036 | `LEXR-01547` | dividirse, separarse, bifurcarse | diccionario_general | - [ ] falta |
| 1037 | `LEXR-00457` | divulgar | diccionario_general | - [ ] falta |
| 1038 | `LEXR-02440` | dizque | diccionario_general | - [ ] falta |
| 1039 | `LEXR-03391` | doblar | diccionario_general | - [ ] falta |
| 1040 | `LEXR-02940` | doblar, encorvar (repetidas veces) | diccionario_general | - [ ] falta |
| 1041 | `LEXR-02032` | doler | diccionario_general | - [ ] falta |
| 1042 | `LEXR-00428` | donde, adonde, ¿dónde? ¿adónde? | diccionario_general | - [ ] falta |
| 1043 | `LEXR-03589` | donde, ¿de dónde? (para abajo), ¿por dónde? | diccionario_general | - [ ] falta |
| 1044 | `LEXR-00612` | dondequiera | diccionario_general | - [ ] falta |
| 1045 | `LEXR-01425` | dorarse | diccionario_general | - [ ] falta |
| 1046 | `LEXR-00410` | dormilón | diccionario_general | - [ ] falta |
| 1047 | `LEXR-00598` | dormir, acostarse | diccionario_general | - [ ] falta |
| 1048 | `LEXR-02982` | dorotea (ave) | diccionario_general | - [ ] falta |
| 1049 | `LEXR-01451` | dos | diccionario_general | - [ ] falta |
| 1050 | `LEXR-01769` | dueño de la casa | diccionario_general | - [ ] falta |
| 1051 | `LEXR-01350` | dulce (sabor) | diccionario_general | - [ ] falta |
| 1052 | `LEXR-03547` | durar | diccionario_general | - [ ] falta |
| 1053 | `LEXR-02399` | duro (sonido) | diccionario_general | - [ ] falta |
| 1054 | `LEXR-01977` | débil | diccionario_general | - [ ] falta |
| 1055 | `LEXR-02990` | días hábiles | diccionario_general | - [ ] falta |
| 1056 | `LEXR-03892` | echado boca abajp, postrado | diccionario_general | - [ ] falta |
| 1057 | `LEXR-00944` | echar (líquido en varias ollas) | diccionario_general | - [ ] falta |
| 1058 | `LEXR-00384` | echar (líquido) | diccionario_general | - [ ] falta |
| 1059 | `LEXR-02691` | echar (varias veces o varias cosas | diccionario_general | - [ ] falta |
| 1060 | `LEXR-02929` | echar agua (ej. en el bautismo) | diccionario_general | - [x] `diccionario_general/echar_agua_(ej._en_el_bautismo).png` |
| 1061 | `LEXR-03189` | echar en | diccionario_general | - [ ] falta |
| 1062 | `LEXR-02405` | echar espigas (maíz), salir la espiga | diccionario_general | - [ ] falta |
| 1063 | `LEXR-00617` | echar fuera, ahuyentar | diccionario_general | - [ ] falta |
| 1064 | `LEXR-01503` | echar grano, cargar | diccionario_general | - [ ] falta |
| 1065 | `LEXR-01500` | echar granos, apuntar | diccionario_general | - [ ] falta |
| 1066 | `LEXR-02347` | echar hojas | diccionario_general | - [ ] falta |
| 1067 | `LEXR-03431` | echar humo, evaporar, quemar incienso | diccionario_general | - [ ] falta |
| 1068 | `LEXR-03923` | echar la culpa, juzgar | diccionario_general | - [ ] falta |
| 1069 | `LEXR-02358` | echar los cimientos (al edificar una casa) | diccionario_general | - [ ] falta |
| 1070 | `LEXR-02424` | echar mano a | diccionario_general | - [ ] falta |
| 1071 | `LEXR-01088` | echar suertes | diccionario_general | - [ ] falta |
| 1072 | `LEXR-03561` | echar una clueca | diccionario_general | - [ ] falta |
| 1073 | `LEXR-02292` | echarse (gallina), empollar | diccionario_general | - [x] `diccionario_general/echarse_(gallina),_empollar.png` |
| 1074 | `LEXR-02857` | econtrarse con otro que viene de rumbo opuesto y seguir adelante | diccionario_general | - [ ] falta |
| 1075 | `LEXR-00766` | ehcar (granos) | diccionario_general | - [ ] falta |
| 1076 | `LEXR-03243` | el abdomen | diccionario_general | - [ ] falta |
| 1077 | `LEXR-02831` | el abejorro, abejón (insecto) | diccionario_general | - [ ] falta |
| 1078 | `LEXR-02585` | el abono | diccionario_general | - [x] `diccionario_general/el_abono.png` |
| 1079 | `LEXR-01800` | el abuelo | diccionario_general | - [ ] falta |
| 1080 | `LEXR-01238` | el abuelo, bisabuelo | diccionario_general | - [ ] falta |
| 1081 | `LEXR-02554` | el aguacate (fruto) | diccionario_general | - [x] `diccionario_general/el_aguacate_(fruto).png` |
| 1082 | `LEXR-02289` | el aguardiente | diccionario_general | - [ ] falta |
| 1083 | `LEXR-03177` | el agüinche | diccionario_general | - [ ] falta |
| 1084 | `LEXR-00399` | el ahijado | diccionario_general | - [ ] falta |
| 1085 | `LEXR-03723` | el ajo | diccionario_general | - [x] `diccionario_general/el_ajo.png` |
| 1086 | `LEXR-03721` | el ají (planta, usada como condimento) | diccionario_general | - [x] `diccionario_general/el_ají_(planta,_usada_como_condimento).png` |
| 1087 | `LEXR-01501` | el ají picante (planta, usada como condimento) | diccionario_general | - [ ] falta |
| 1088 | `LEXR-03826` | el ají pimentón (planta, usada como condimento) | diccionario_general | - [ ] falta |
| 1089 | `LEXR-03050` | el ala | diccionario_general | - [x] `diccionario_general/el_ala.png` |
| 1090 | `LEXR-01690` | el alacrán (arácnido venenoso) | diccionario_general | - [ ] falta |
| 1091 | `LEXR-00716` | el alfarero | diccionario_general | - [ ] falta |
| 1092 | `LEXR-01175` | el algodón | diccionario_general | - [x] `diccionario_general/el_algodón.png` |
| 1093 | `LEXR-03853` | el alguacil | diccionario_general | - [ ] falta |
| 1094 | `LEXR-02712` | el aliso (árbol) | diccionario_general | - [x] `diccionario_general/el_aliso_(árbol).png` |
| 1095 | `LEXR-01903` | el almud | diccionario_general | - [x] `diccionario_general/el_almud.png` |
| 1096 | `LEXR-02616` | el amero (envoltura de maíz) | diccionario_general | - [x] `diccionario_general/el_amero_(envoltura_de_maíz).png` |
| 1097 | `LEXR-02962` | el amigo | diccionario_general | - [ ] falta |
| 1098 | `LEXR-03845` | el anaco (de lana) | diccionario_general | - [ ] falta |
| 1099 | `LEXR-02980` | el andamio | diccionario_general | - [ ] falta |
| 1100 | `LEXR-03143` | el animal | diccionario_general | - [ ] falta |
| 1101 | `LEXR-02474` | el antebrazo | diccionario_general | - [ ] falta |
| 1102 | `LEXR-01319` | el apodo | diccionario_general | - [ ] falta |
| 1103 | `LEXR-02978` | el arbusto | diccionario_general | - [ ] falta |
| 1104 | `LEXR-01137` | el arco iris | diccionario_general | - [ ] falta |
| 1105 | `LEXR-03064` | el arco, de forma arqueda | diccionario_general | - [ ] falta |
| 1106 | `LEXR-02765` | el armadillo (mamífero) | diccionario_general | - [x] `diccionario_general/el_armadillo_(mamífero).png` |
| 1107 | `LEXR-03417` | el arrayán (árbol) | diccionario_general | - [ ] falta |
| 1108 | `LEXR-00803` | el arroz | diccionario_general | - [ ] falta |
| 1109 | `LEXR-01794` | el ascua, carbón encendido | diccionario_general | - [ ] falta |
| 1110 | `LEXR-00952` | el asiento | diccionario_general | - [ ] falta |
| 1111 | `LEXR-02599` | el asno (mamífero) | diccionario_general | - [ ] falta |
| 1112 | `LEXR-03804` | el ataúd | diccionario_general | - [ ] falta |
| 1113 | `LEXR-02673` | el ayudante, que ayuda | diccionario_general | - [ ] falta |
| 1114 | `LEXR-02546` | el ayudante, que ayudará | diccionario_general | - [ ] falta |
| 1115 | `LEXR-03371` | el ayuno | diccionario_general | - [ ] falta |
| 1116 | `LEXR-03074` | el año | diccionario_general | - [ ] falta |
| 1117 | `LEXR-01534` | el año pasado | diccionario_general | - [ ] falta |
| 1118 | `LEXR-03109` | el baile | diccionario_general | - [ ] falta |
| 1119 | `LEXR-03210` | el barro, lodo | diccionario_general | - [ ] falta |
| 1120 | `LEXR-02013` | el bimbo, pisco, pavo común (ave) | diccionario_general | - [ ] falta |
| 1121 | `LEXR-03283` | el blanco (de raza blanca) | diccionario_general | - [ ] falta |
| 1122 | `LEXR-02959` | el bordón | diccionario_general | - [ ] falta |
| 1123 | `LEXR-01490` | el borracho | diccionario_general | - [ ] falta |
| 1124 | `LEXR-02308` | el brujo, hechicero | diccionario_general | - [ ] falta |
| 1125 | `LEXR-03186` | el bulto | diccionario_general | - [ ] falta |
| 1126 | `LEXR-03511` | el búho, la lechuza (ave) | diccionario_general | - [x] `diccionario_general/el_búho,_la_lechuza_(ave).png` |
| 1127 | `LEXR-02702` | el caballo | diccionario_general | - [x] `diccionario_general/el_caballo.png` |
| 1128 | `LEXR-03654` | el cadáver | diccionario_general | - [ ] falta |
| 1129 | `LEXR-01202` | el café | diccionario_general | - [ ] falta |
| 1130 | `LEXR-03736` | el calabazo (para líquidos) | diccionario_general | - [ ] falta |
| 1131 | `LEXR-01170` | el calabazo, la vasija rústica, totuma | diccionario_general | - [ ] falta |
| 1132 | `LEXR-02741` | el calcañar, el talón | diccionario_general | - [ ] falta |
| 1133 | `LEXR-03765` | el calcañar, talón | diccionario_general | - [ ] falta |
| 1134 | `LEXR-01657` | el caldo, la sopa | diccionario_general | - [ ] falta |
| 1135 | `LEXR-03336` | el camino | diccionario_general | - [ ] falta |
| 1136 | `LEXR-02153` | el canasto, cesto | diccionario_general | - [ ] falta |
| 1137 | `LEXR-00663` | el cangrejo (crustáceo) | diccionario_general | - [ ] falta |
| 1138 | `LEXR-03261` | el cangrejo, alacrán (arácnido) | diccionario_general | - [ ] falta |
| 1139 | `LEXR-02622` | el canto, la canción | diccionario_general | - [ ] falta |
| 1140 | `LEXR-02570` | el capitán | diccionario_general | - [ ] falta |
| 1141 | `LEXR-03630` | el caracol | diccionario_general | - [ ] falta |
| 1142 | `LEXR-01591` | el carate (especie de sarna) | diccionario_general | - [ ] falta |
| 1143 | `LEXR-02587` | el cardo (planta) | diccionario_general | - [ ] falta |
| 1144 | `LEXR-02875` | el carpintero | diccionario_general | - [ ] falta |
| 1145 | `LEXR-01456` | el carpintero (ave) | diccionario_general | - [ ] falta |
| 1146 | `LEXR-00382` | el carrete de barro para asentar olla | diccionario_general | - [x] `diccionario_general/el_carrete_de_barro_para_asentar_olla.png` |
| 1147 | `LEXR-01931` | el carrizo | diccionario_general | - [ ] falta |
| 1148 | `LEXR-03789` | el carrizo (sirve para flauta) | diccionario_general | - [x] `diccionario_general/el_carrizo_(sirve_para_flauta).png` |
| 1149 | `LEXR-03333` | el carángano (insecto) | diccionario_general | - [ ] falta |
| 1150 | `LEXR-00686` | el caserío, pueblo, poblado | diccionario_general | - [ ] falta |
| 1151 | `LEXR-02024` | el castellano, español (idioma) | diccionario_general | - [ ] falta |
| 1152 | `LEXR-00666` | el caudal, corriente del rió | diccionario_general | - [ ] falta |
| 1153 | `LEXR-00592` | el cañaduzal | diccionario_general | - [ ] falta |
| 1154 | `LEXR-02855` | el cañuto | diccionario_general | - [ ] falta |
| 1155 | `LEXR-01082` | el cedro (árbol) | diccionario_general | - [x] `diccionario_general/el_cedro_(árbol).png` |
| 1156 | `LEXR-03324` | el cerro | diccionario_general | - [ ] falta |
| 1157 | `LEXR-03250` | el charco, lago | diccionario_general | - [ ] falta |
| 1158 | `LEXR-03298` | el chicao (ave amarillo) | diccionario_general | - [ ] falta |
| 1159 | `LEXR-02892` | el chiguaco (ave) | diccionario_general | - [ ] falta |
| 1160 | `LEXR-01001` | el choclo, mazorca de maíz tierno | diccionario_general | - [ ] falta |
| 1161 | `LEXR-00972` | el chorrizo | diccionario_general | - [ ] falta |
| 1162 | `LEXR-01123` | el cielo | diccionario_general | - [ ] falta |
| 1163 | `LEXR-00560` | el ciempiés | diccionario_general | - [ ] falta |
| 1164 | `LEXR-02553` | el ciempiés (miriápodo) | diccionario_general | - [ ] falta |
| 1165 | `LEXR-00959` | el cinturón, la correa | diccionario_general | - [ ] falta |
| 1166 | `LEXR-02099` | el cohete | diccionario_general | - [ ] falta |
| 1167 | `LEXR-02238` | el col, repollo (planta comestible) | diccionario_general | - [ ] falta |
| 1168 | `LEXR-02919` | el colmillo | diccionario_general | - [ ] falta |
| 1169 | `LEXR-01048` | el comején | diccionario_general | - [ ] falta |
| 1170 | `LEXR-02481` | el comején (insecto) | diccionario_general | - [ ] falta |
| 1171 | `LEXR-03285` | el compadre | diccionario_general | - [ ] falta |
| 1172 | `LEXR-00630` | el compañero, la compañera | diccionario_general | - [ ] falta |
| 1173 | `LEXR-03386` | el concuñado | diccionario_general | - [ ] falta |
| 1174 | `LEXR-03899` | el consejero, que aconseja | diccionario_general | - [ ] falta |
| 1175 | `LEXR-03215` | el consejo | diccionario_general | - [ ] falta |
| 1176 | `LEXR-02935` | el cordón umbilical | diccionario_general | - [ ] falta |
| 1177 | `LEXR-00492` | el cordón, látigo | diccionario_general | - [ ] falta |
| 1178 | `LEXR-00409` | el corral | diccionario_general | - [ ] falta |
| 1179 | `LEXR-02218` | el corral de ovejas | diccionario_general | - [x] `diccionario_general/el_corral_de_ovejas.png` |
| 1180 | `LEXR-02841` | el corredor (de la casa) | diccionario_general | - [ ] falta |
| 1181 | `LEXR-01477` | el corredor (de la casa), sitio cubierto | diccionario_general | - [ ] falta |
| 1182 | `LEXR-02918` | el costal | diccionario_general | - [ ] falta |
| 1183 | `LEXR-00534` | el coto, bocio | diccionario_general | - [ ] falta |
| 1184 | `LEXR-03442` | el creador | diccionario_general | - [ ] falta |
| 1185 | `LEXR-01920` | el cucarachero (ave) | diccionario_general | - [ ] falta |
| 1186 | `LEXR-02589` | el cucarrón, escarabajo (insecto) | diccionario_general | - [ ] falta |
| 1187 | `LEXR-01452` | el cucharón (de madera) | diccionario_general | - [x] `diccionario_general/el_cucharón_(de_madera).png` |
| 1188 | `LEXR-02038` | el cuchillo | diccionario_general | - [ ] falta |
| 1189 | `LEXR-00771` | el cuerpo | diccionario_general | - [ ] falta |
| 1190 | `LEXR-00424` | el culantro (planta) | diccionario_general | - [ ] falta |
| 1191 | `LEXR-00436` | el cura, sacerdote | diccionario_general | - [ ] falta |
| 1192 | `LEXR-02502` | el curandero | diccionario_general | - [ ] falta |
| 1193 | `LEXR-03682` | el curandero, hechicero | diccionario_general | - [ ] falta |
| 1194 | `LEXR-03001` | el curíbano (planta medicinal) | diccionario_general | - [ ] falta |
| 1195 | `LEXR-02657` | el cusumbe, coatí (mamífero) | diccionario_general | - [ ] falta |
| 1196 | `LEXR-01455` | el cuí, conejillo de indias (mamífero) | diccionario_general | - [ ] falta |
| 1197 | `LEXR-00618` | el cuñado (entre hombres) | diccionario_general | - [ ] falta |
| 1198 | `LEXR-01541` | el cuñado, la cuñada (entre los dos sexos) | diccionario_general | - [ ] falta |
| 1199 | `LEXR-01343` | el cántaro | diccionario_general | - [ ] falta |
| 1200 | `LEXR-01521` | el dedo | diccionario_general | - [ ] falta |
| 1201 | `LEXR-03601` | el dedo cordial o de en medio | diccionario_general | - [ ] falta |
| 1202 | `LEXR-03042` | el dedo del pie | diccionario_general | - [ ] falta |
| 1203 | `LEXR-03323` | el desfiladero | diccionario_general | - [ ] falta |
| 1204 | `LEXR-03337` | el diablo | diccionario_general | - [ ] falta |
| 1205 | `LEXR-02010` | el diente | diccionario_general | - [ ] falta |
| 1206 | `LEXR-01467` | el diluvio | diccionario_general | - [ ] falta |
| 1207 | `LEXR-00562` | el dinero, la plata, moneda | diccionario_general | - [ ] falta |
| 1208 | `LEXR-02650` | el dolor | diccionario_general | - [ ] falta |
| 1209 | `LEXR-02630` | el domingo | diccionario_general | - [ ] falta |
| 1210 | `LEXR-00552` | el dormilón (ave nocturna) | diccionario_general | - [ ] falta |
| 1211 | `LEXR-01922` | el dueño, la dueña | diccionario_general | - [ ] falta |
| 1212 | `LEXR-02535` | el durazno (fruta) | diccionario_general | - [x] `diccionario_general/el_durazno_(fruta).png` |
| 1213 | `LEXR-03452` | el día, tiempo | diccionario_general | - [ ] falta |
| 1214 | `LEXR-02155` | el empeine | diccionario_general | - [ ] falta |
| 1215 | `LEXR-01759` | el encenillo (árbol, usado para leña) | diccionario_general | - [ ] falta |
| 1216 | `LEXR-01529` | el enemigo | diccionario_general | - [ ] falta |
| 1217 | `LEXR-02772` | el enfermo, el paciente | diccionario_general | - [ ] falta |
| 1218 | `LEXR-03423` | el enojo, la ira | diccionario_general | - [ ] falta |
| 1219 | `LEXR-02767` | el enrizo, puerco espín (mamífero) | diccionario_general | - [ ] falta |
| 1220 | `LEXR-00396` | el escoplo (herramienta) | diccionario_general | - [ ] falta |
| 1221 | `LEXR-02014` | el espejo | diccionario_general | - [ ] falta |
| 1222 | `LEXR-01603` | el esposo, marido | diccionario_general | - [ ] falta |
| 1223 | `LEXR-03047` | el esqueleto | diccionario_general | - [ ] falta |
| 1224 | `LEXR-02680` | el estómago, la barriga | diccionario_general | - [ ] falta |
| 1225 | `LEXR-00870` | el esófago | diccionario_general | - [ ] falta |
| 1226 | `LEXR-02614` | el extranjero | diccionario_general | - [ ] falta |
| 1227 | `LEXR-01628` | el extranjero, forastero | diccionario_general | - [ ] falta |
| 1228 | `LEXR-01701` | el filo | diccionario_general | - [ ] falta |
| 1229 | `LEXR-02327` | el fiscal (oficial) | diccionario_general | - [ ] falta |
| 1230 | `LEXR-03432` | el flautista | diccionario_general | - [ ] falta |
| 1231 | `LEXR-03569` | el fornicador | diccionario_general | - [ ] falta |
| 1232 | `LEXR-01810` | el frendo | diccionario_general | - [ ] falta |
| 1233 | `LEXR-00744` | el fríjol | diccionario_general | - [ ] falta |
| 1234 | `LEXR-02733` | el fuete | diccionario_general | - [ ] falta |
| 1235 | `LEXR-01229` | el gallinazo, galembo (ave) | diccionario_general | - [x] `diccionario_general/el_gallinazo,_galembo_(ave).png` |
| 1236 | `LEXR-03008` | el gallo | diccionario_general | - [x] `diccionario_general/el_gallo.png` |
| 1237 | `LEXR-01443` | el garabato | diccionario_general | - [ ] falta |
| 1238 | `LEXR-02016` | el gavilán (ave) | diccionario_general | - [ ] falta |
| 1239 | `LEXR-01538` | el gobernador (del resguardo) | diccionario_general | - [ ] falta |
| 1240 | `LEXR-00709` | el gobernante, mandatario | diccionario_general | - [ ] falta |
| 1241 | `LEXR-00685` | el gorgojo (insecto) | diccionario_general | - [ ] falta |
| 1242 | `LEXR-02863` | el gorrion | diccionario_general | - [ ] falta |
| 1243 | `LEXR-03834` | el granizo | diccionario_general | - [ ] falta |
| 1244 | `LEXR-02087` | el grano, la pepita | diccionario_general | - [ ] falta |
| 1245 | `LEXR-02882` | el grillo (insecto) | diccionario_general | - [x] `diccionario_general/el_grillo_(insecto).png` |
| 1246 | `LEXR-01635` | el guarapo, chicha de caña de azúcar | diccionario_general | - [ ] falta |
| 1247 | `LEXR-00472` | el guerrillero | diccionario_general | - [ ] falta |
| 1248 | `LEXR-03134` | el guineo (especie de plátano pequeño) | diccionario_general | - [ ] falta |
| 1249 | `LEXR-01945` | el gusano | diccionario_general | - [ ] falta |
| 1250 | `LEXR-01687` | el gusano, larva | diccionario_general | - [ ] falta |
| 1251 | `LEXR-03397` | el hacha | diccionario_general | - [x] `diccionario_general/el_hacha.png` |
| 1252 | `LEXR-02595` | el hambre, escasez | diccionario_general | - [ ] falta |
| 1253 | `LEXR-03195` | el helecho | diccionario_general | - [ ] falta |
| 1254 | `LEXR-01923` | el hermano (respecto a la mujer) | diccionario_general | - [ ] falta |
| 1255 | `LEXR-00824` | el hermano de en medio | diccionario_general | - [ ] falta |
| 1256 | `LEXR-03464` | el hermano, la hermana (del mismo sexo) | diccionario_general | - [ ] falta |
| 1257 | `LEXR-03551` | el hielo | diccionario_general | - [ ] falta |
| 1258 | `LEXR-03638` | el higuerón, canela de páramo (árbol) | diccionario_general | - [ ] falta |
| 1259 | `LEXR-01299` | el higuillo (árbol) | diccionario_general | - [ ] falta |
| 1260 | `LEXR-02166` | el hijo | diccionario_general | - [ ] falta |
| 1261 | `LEXR-01063` | el hijo mayor | diccionario_general | - [ ] falta |
| 1262 | `LEXR-00896` | el hijo menor | diccionario_general | - [ ] falta |
| 1263 | `LEXR-03674` | el hocico del puerco | diccionario_general | - [ ] falta |
| 1264 | `LEXR-03413` | el hombre (adulto) | diccionario_general | - [ ] falta |
| 1265 | `LEXR-03901` | el hombro | diccionario_general | - [ ] falta |
| 1266 | `LEXR-02986` | el homicida | diccionario_general | - [ ] falta |
| 1267 | `LEXR-02664` | el homicida, asesino | diccionario_general | - [ ] falta |
| 1268 | `LEXR-00425` | el hongo (planta) | diccionario_general | - [x] `diccionario_general/el_hongo_(planta).png` |
| 1269 | `LEXR-03797` | el hormiguero | diccionario_general | - [ ] falta |
| 1270 | `LEXR-00973` | el horno | diccionario_general | - [ ] falta |
| 1271 | `LEXR-01601` | el huarango (árbol) | diccionario_general | - [ ] falta |
| 1272 | `LEXR-03332` | el hueco, hoyo, agujero, cueva | diccionario_general | - [ ] falta |
| 1273 | `LEXR-03314` | el hueso | diccionario_general | - [ ] falta |
| 1274 | `LEXR-03872` | el huevo | diccionario_general | - [ ] falta |
| 1275 | `LEXR-01842` | el humo | diccionario_general | - [ ] falta |
| 1276 | `LEXR-02362` | el huso (palo para hilar) | diccionario_general | - [ ] falta |
| 1277 | `LEXR-02943` | el huérfano, guacho | diccionario_general | - [ ] falta |
| 1278 | `LEXR-01060` | el hígado | diccionario_general | - [ ] falta |
| 1279 | `LEXR-02098` | el húmero, hueso del brazo | diccionario_general | - [ ] falta |
| 1280 | `LEXR-00467` | el idioma castellano, español | diccionario_general | - [ ] falta |
| 1281 | `LEXR-02817` | el idioma páez | diccionario_general | - [ ] falta |
| 1282 | `LEXR-02484` | el infierno | diccionario_general | - [ ] falta |
| 1283 | `LEXR-01926` | el invierno, tiempo de invierno | diccionario_general | - [ ] falta |
| 1284 | `LEXR-01981` | el jabón | diccionario_general | - [ ] falta |
| 1285 | `LEXR-01466` | el jefe | diccionario_general | - [ ] falta |
| 1286 | `LEXR-00958` | el jornalero | diccionario_general | - [ ] falta |
| 1287 | `LEXR-00886` | el jueves | diccionario_general | - [ ] falta |
| 1288 | `LEXR-01041` | el juez (oficial del cabildo) | diccionario_general | - [ ] falta |
| 1289 | `LEXR-03145` | el junco (arbusto) | diccionario_general | - [ ] falta |
| 1290 | `LEXR-03315` | el lado del fogón | diccionario_general | - [ ] falta |
| 1291 | `LEXR-01854` | el lado opuesto | diccionario_general | - [ ] falta |
| 1292 | `LEXR-02710` | el ladrón | diccionario_general | - [ ] falta |
| 1293 | `LEXR-01735` | el lagartijo | diccionario_general | - [ ] falta |
| 1294 | `LEXR-02373` | el lechero (árbol) | diccionario_general | - [ ] falta |
| 1295 | `LEXR-03289` | el león (mamífero) | diccionario_general | - [ ] falta |
| 1296 | `LEXR-02179` | el león, puma (mamífero) | diccionario_general | - [x] `diccionario_general/el_león,_puma_(mamífero).png` |
| 1297 | `LEXR-03678` | el limón (fruta) | diccionario_general | - [ ] falta |
| 1298 | `LEXR-03436` | el linaje, la raza, el descendiente | diccionario_general | - [ ] falta |
| 1299 | `LEXR-02974` | el loro (ave) | diccionario_general | - [x] `diccionario_general/el_loro_(ave).png` |
| 1300 | `LEXR-01967` | el lugar | diccionario_general | - [ ] falta |
| 1301 | `LEXR-01826` | el lugar de habitación, morada | diccionario_general | - [ ] falta |
| 1302 | `LEXR-00806` | el lulo (planta) | diccionario_general | - [ ] falta |
| 1303 | `LEXR-01058` | el lunes | diccionario_general | - [ ] falta |
| 1304 | `LEXR-03088` | el líder (de un conjunto de músicos) | diccionario_general | - [ ] falta |
| 1305 | `LEXR-02794` | el maestro, que enseña | diccionario_general | - [ ] falta |
| 1306 | `LEXR-03620` | el maizal (depués de cosechar) | diccionario_general | - [ ] falta |
| 1307 | `LEXR-02637` | el malacate | diccionario_general | - [ ] falta |
| 1308 | `LEXR-00962` | el mambe | diccionario_general | - [ ] falta |
| 1309 | `LEXR-03579` | el mar | diccionario_general | - [ ] falta |
| 1310 | `LEXR-00549` | el martingalvis (árbol) | diccionario_general | - [ ] falta |
| 1311 | `LEXR-01876` | el matón | diccionario_general | - [ ] falta |
| 1312 | `LEXR-00423` | el mazo | diccionario_general | - [ ] falta |
| 1313 | `LEXR-03619` | el maíz | diccionario_general | - [x] `diccionario_general/el_maíz.png` |
| 1314 | `LEXR-03672` | el mediodía | diccionario_general | - [ ] falta |
| 1315 | `LEXR-01805` | el mejicano (calabaza) | diccionario_general | - [ ] falta |
| 1316 | `LEXR-00804` | el mellizo | diccionario_general | - [ ] falta |
| 1317 | `LEXR-02351` | el mensajero | diccionario_general | - [ ] falta |
| 1318 | `LEXR-00872` | el mentón, cumbamba (voz Quechua) | diccionario_general | - [ ] falta |
| 1319 | `LEXR-00835` | el metal, hierro | diccionario_general | - [ ] falta |
| 1320 | `LEXR-02952` | el meñique | diccionario_general | - [ ] falta |
| 1321 | `LEXR-00990` | el miércoles | diccionario_general | - [ ] falta |
| 1322 | `LEXR-02850` | el molino | diccionario_general | - [ ] falta |
| 1323 | `LEXR-00426` | el mono, mico (mamífero) | diccionario_general | - [x] `diccionario_general/el_mono,_mico_(mamífero).png` |
| 1324 | `LEXR-03039` | el mosquito | diccionario_general | - [ ] falta |
| 1325 | `LEXR-02755` | el mote | diccionario_general | - [ ] falta |
| 1326 | `LEXR-01855` | el muchacho | diccionario_general | - [ ] falta |
| 1327 | `LEXR-01611` | el muchaco | diccionario_general | - [ ] falta |
| 1328 | `LEXR-03581` | el muchilero (ave) | diccionario_general | - [ ] falta |
| 1329 | `LEXR-03536` | el murcielago (mamífero) | diccionario_general | - [ ] falta |
| 1330 | `LEXR-02799` | el musgo | diccionario_general | - [ ] falta |
| 1331 | `LEXR-01147` | el muslo | diccionario_general | - [ ] falta |
| 1332 | `LEXR-03640` | el músculo | diccionario_general | - [ ] falta |
| 1333 | `LEXR-01767` | el nevado | diccionario_general | - [ ] falta |
| 1334 | `LEXR-01962` | el nevado (ej. Nevado de Huila) | diccionario_general | - [ ] falta |
| 1335 | `LEXR-01450` | el nido | diccionario_general | - [ ] falta |
| 1336 | `LEXR-00808` | el nieto, la nieta | diccionario_general | - [ ] falta |
| 1337 | `LEXR-02751` | el niño, la niña | diccionario_general | - [ ] falta |
| 1338 | `LEXR-01768` | el nombre | diccionario_general | - [ ] falta |
| 1339 | `LEXR-01380` | el nudillo (planta) | diccionario_general | - [ ] falta |
| 1340 | `LEXR-02082` | el ojo | diccionario_general | - [ ] falta |
| 1341 | `LEXR-01699` | el ojo de agua, manatial | diccionario_general | - [ ] falta |
| 1342 | `LEXR-01617` | el ombligo | diccionario_general | - [ ] falta |
| 1343 | `LEXR-00636` | el oriente, este | diccionario_general | - [ ] falta |
| 1344 | `LEXR-02241` | el oro (metal) | diccionario_general | - [ ] falta |
| 1345 | `LEXR-00966` | el oso (mamífero) | diccionario_general | - [ ] falta |
| 1346 | `LEXR-02258` | el ovillo | diccionario_general | - [ ] falta |
| 1347 | `LEXR-01168` | el oído | diccionario_general | - [ ] falta |
| 1348 | `LEXR-02623` | el padrastro | diccionario_general | - [ ] falta |
| 1349 | `LEXR-01390` | el padre | diccionario_general | - [ ] falta |
| 1350 | `LEXR-00545` | el padre, papá | diccionario_general | - [ ] falta |
| 1351 | `LEXR-01301` | el padrino | diccionario_general | - [ ] falta |
| 1352 | `LEXR-00572` | el pajonal | diccionario_general | - [ ] falta |
| 1353 | `LEXR-01532` | el paladar | diccionario_general | - [ ] falta |
| 1354 | `LEXR-03367` | el palo del huso | diccionario_general | - [ ] falta |
| 1355 | `LEXR-02803` | el palo del telar (lanzadera) | diccionario_general | - [ ] falta |
| 1356 | `LEXR-01271` | el paludismo | diccionario_general | - [ ] falta |
| 1357 | `LEXR-00521` | el pariente (de la misma raza) | diccionario_general | - [ ] falta |
| 1358 | `LEXR-01543` | el pasto | diccionario_general | - [ ] falta |
| 1359 | `LEXR-01610` | el pastor de ovejas | diccionario_general | - [x] `diccionario_general/el_pastor_de_ovejas.png` |
| 1360 | `LEXR-01073` | el patio | diccionario_general | - [ ] falta |
| 1361 | `LEXR-00702` | el pavo de monte (ave) | diccionario_general | - [ ] falta |
| 1362 | `LEXR-01674` | el pecado | diccionario_general | - [ ] falta |
| 1363 | `LEXR-03505` | el pecador | diccionario_general | - [ ] falta |
| 1364 | `LEXR-02469` | el pecho, la teta | diccionario_general | - [ ] falta |
| 1365 | `LEXR-02928` | el pedazo | diccionario_general | - [ ] falta |
| 1366 | `LEXR-02005` | el pedernal (para prender candela) | diccionario_general | - [ ] falta |
| 1367 | `LEXR-02225` | el peine | diccionario_general | - [ ] falta |
| 1368 | `LEXR-01031` | el pelo del cuerpo | diccionario_general | - [ ] falta |
| 1369 | `LEXR-03709` | el pelo, cabello | diccionario_general | - [ ] falta |
| 1370 | `LEXR-02987` | el pene | diccionario_general | - [ ] falta |
| 1371 | `LEXR-03292` | el pepino | diccionario_general | - [ ] falta |
| 1372 | `LEXR-02173` | el perrito, cachorro | diccionario_general | - [ ] falta |
| 1373 | `LEXR-01438` | el perro | diccionario_general | - [x] `diccionario_general/el_perro.png` |
| 1374 | `LEXR-02900` | el pescado, pez | diccionario_general | - [x] `diccionario_general/el_pescado,_pez.png` |
| 1375 | `LEXR-02407` | el pescador | diccionario_general | - [ ] falta |
| 1376 | `LEXR-02709` | el peso (moneda) | diccionario_general | - [ ] falta |
| 1377 | `LEXR-02056` | el peón, jornalero | diccionario_general | - [ ] falta |
| 1378 | `LEXR-02328` | el pico (herramienta) | diccionario_general | - [ ] falta |
| 1379 | `LEXR-03557` | el pie, la pierna (de persona), la pata (de animal) | diccionario_general | - [ ] falta |
| 1380 | `LEXR-01840` | el piojo (insecto) | diccionario_general | - [ ] falta |
| 1381 | `LEXR-02219` | el pisco, pavo (ave) | diccionario_general | - [ ] falta |
| 1382 | `LEXR-02170` | el pisón | diccionario_general | - [ ] falta |
| 1383 | `LEXR-01889` | el plano, la llanura, el llano | diccionario_general | - [ ] falta |
| 1384 | `LEXR-02069` | el plátano (de tierrra templada) | diccionario_general | - [ ] falta |
| 1385 | `LEXR-03895` | el plátano (planta) | diccionario_general | - [ ] falta |
| 1386 | `LEXR-00880` | el poder | diccionario_general | - [ ] falta |
| 1387 | `LEXR-01109` | el pollo | diccionario_general | - [ ] falta |
| 1388 | `LEXR-01559` | el polvo | diccionario_general | - [ ] falta |
| 1389 | `LEXR-01316` | el polvo (del camino) | diccionario_general | - [ ] falta |
| 1390 | `LEXR-00635` | el poniente, oeste, occidente | diccionario_general | - [ ] falta |
| 1391 | `LEXR-03271` | el poporo | diccionario_general | - [ ] falta |
| 1392 | `LEXR-01429` | el pozo | diccionario_general | - [ ] falta |
| 1393 | `LEXR-01332` | el pozo de barro (para hacer teja) | diccionario_general | - [ ] falta |
| 1394 | `LEXR-01750` | el preso | diccionario_general | - [ ] falta |
| 1395 | `LEXR-01606` | el primero, los primeros | diccionario_general | - [ ] falta |
| 1396 | `LEXR-01246` | el primo, la prima (del mismo sexo) | diccionario_general | - [ ] falta |
| 1397 | `LEXR-00980` | el primogénito (primer hijo) | diccionario_general | - [ ] falta |
| 1398 | `LEXR-03344` | el pueblo, caserío | diccionario_general | - [ ] falta |
| 1399 | `LEXR-02300` | el puerco, cerdo, marrano | diccionario_general | - [x] `diccionario_general/el_puerco,_cerdo,_marrano.png` |
| 1400 | `LEXR-01594` | el pulgar | diccionario_general | - [ ] falta |
| 1401 | `LEXR-02849` | el pulmón | diccionario_general | - [ ] falta |
| 1402 | `LEXR-02281` | el pus | diccionario_general | - [ ] falta |
| 1403 | `LEXR-01761` | el puño | diccionario_general | - [ ] falta |
| 1404 | `LEXR-02077` | el pájaro | diccionario_general | - [ ] falta |
| 1405 | `LEXR-00768` | el pájaro carpintero | diccionario_general | - [ ] falta |
| 1406 | `LEXR-00565` | el páramo (terreno desierto, elevado y sin vegetación) | diccionario_general | - [ ] falta |
| 1407 | `LEXR-02406` | el que hace | diccionario_general | - [ ] falta |
| 1408 | `LEXR-00853` | el que mete la caña en el otro lado del trapiche | diccionario_general | - [ ] falta |
| 1409 | `LEXR-01636` | el que recibe cañaen el trapiche | diccionario_general | - [ ] falta |
| 1410 | `LEXR-03823` | el queso | diccionario_general | - [ ] falta |
| 1411 | `LEXR-01836` | el rabo (de gallina) | diccionario_general | - [ ] falta |
| 1412 | `LEXR-01424` | el rancho, cobertizo | diccionario_general | - [ ] falta |
| 1413 | `LEXR-02395` | el rastrojo | diccionario_general | - [ ] falta |
| 1414 | `LEXR-02591` | el ratón (mamífero roedor) | diccionario_general | - [ ] falta |
| 1415 | `LEXR-02254` | el rayo | diccionario_general | - [ ] falta |
| 1416 | `LEXR-00885` | el rayo (que quema) | diccionario_general | - [ ] falta |
| 1417 | `LEXR-03076` | el rejo | diccionario_general | - [ ] falta |
| 1418 | `LEXR-00667` | el remedio, medicina | diccionario_general | - [ ] falta |
| 1419 | `LEXR-02400` | el renacuajo, cría de la rana | diccionario_general | - [ ] falta |
| 1420 | `LEXR-00871` | el res, el ganado (animal doméstico) | diccionario_general | - [ ] falta |
| 1421 | `LEXR-02192` | el retoño | diccionario_general | - [ ] falta |
| 1422 | `LEXR-00890` | el rezandero | diccionario_general | - [ ] falta |
| 1423 | `LEXR-02247` | el riachuelo | diccionario_general | - [ ] falta |
| 1424 | `LEXR-00989` | el rincón, la esquina | diccionario_general | - [ ] falta |
| 1425 | `LEXR-02897` | el riñón | diccionario_general | - [ ] falta |
| 1426 | `LEXR-01808` | el roble (árbol) | diccionario_general | - [ ] falta |
| 1427 | `LEXR-02030` | el río | diccionario_general | - [ ] falta |
| 1428 | `LEXR-02584` | el sapo (batracio) | diccionario_general | - [x] `diccionario_general/el_sapo_(batracio).png` |
| 1429 | `LEXR-00455` | el sapo pequeño | diccionario_general | - [ ] falta |
| 1430 | `LEXR-01777` | el sarampión | diccionario_general | - [ ] falta |
| 1431 | `LEXR-01817` | el sebo | diccionario_general | - [ ] falta |
| 1432 | `LEXR-02239` | el sembrado | diccionario_general | - [ ] falta |
| 1433 | `LEXR-02555` | el sepulcro, cementario | diccionario_general | - [ ] falta |
| 1434 | `LEXR-03153` | el sereno | diccionario_general | - [ ] falta |
| 1435 | `LEXR-02838` | el señor, patrón | diccionario_general | - [ ] falta |
| 1436 | `LEXR-02228` | el siervo, que sirve | diccionario_general | - [ ] falta |
| 1437 | `LEXR-00789` | el sitio | diccionario_general | - [ ] falta |
| 1438 | `LEXR-00822` | el sobaco, axila | diccionario_general | - [ ] falta |
| 1439 | `LEXR-01757` | el sol | diccionario_general | - [ ] falta |
| 1440 | `LEXR-03650` | el soldado | diccionario_general | - [ ] falta |
| 1441 | `LEXR-01032` | el suegro | diccionario_general | - [ ] falta |
| 1442 | `LEXR-02654` | el sueño | diccionario_general | - [ ] falta |
| 1443 | `LEXR-02499` | el sábado | diccionario_general | - [ ] falta |
| 1444 | `LEXR-01483` | el tallo de maíz | diccionario_general | - [ ] falta |
| 1445 | `LEXR-02761` | el tamal, el bollo (envuelto de maíz) | diccionario_general | - [ ] falta |
| 1446 | `LEXR-02938` | el tamo | diccionario_general | - [ ] falta |
| 1447 | `LEXR-02414` | el telar | diccionario_general | - [ ] falta |
| 1448 | `LEXR-02747` | el temblor (de tierra) | diccionario_general | - [ ] falta |
| 1449 | `LEXR-03334` | el ternero | diccionario_general | - [ ] falta |
| 1450 | `LEXR-03151` | el teñidero (árbol, que se usa para teñir de negro) | diccionario_general | - [ ] falta |
| 1451 | `LEXR-01709` | el tigrillo | diccionario_general | - [ ] falta |
| 1452 | `LEXR-02284` | el tigrillo (mamífero) | diccionario_general | - [ ] falta |
| 1453 | `LEXR-02662` | el tizón | diccionario_general | - [ ] falta |
| 1454 | `LEXR-01848` | el tobillo, la espinilla | diccionario_general | - [ ] falta |
| 1455 | `LEXR-01171` | el toro | diccionario_general | - [ ] falta |
| 1456 | `LEXR-02134` | el toromonte (ave) | diccionario_general | - [ ] falta |
| 1457 | `LEXR-03360` | el trabajador | diccionario_general | - [ ] falta |
| 1458 | `LEXR-02538` | el trabajo, empleo | diccionario_general | - [ ] falta |
| 1459 | `LEXR-00957` | el trapiche | diccionario_general | - [ ] falta |
| 1460 | `LEXR-00760` | el trapiche de mano | diccionario_general | - [ ] falta |
| 1461 | `LEXR-01554` | el trigal | diccionario_general | - [ ] falta |
| 1462 | `LEXR-02859` | el trigo | diccionario_general | - [ ] falta |
| 1463 | `LEXR-01351` | el troje, granero | diccionario_general | - [ ] falta |
| 1464 | `LEXR-02569` | el trompo (juguete) | diccionario_general | - [ ] falta |
| 1465 | `LEXR-01980` | el trueno, rayo, relámpago | diccionario_general | - [ ] falta |
| 1466 | `LEXR-00780` | el tumor, absceso | diccionario_general | - [ ] falta |
| 1467 | `LEXR-01908` | el tío (hermano de la mamá) | diccionario_general | - [ ] falta |
| 1468 | `LEXR-00476` | el tío (hermano del papá) | diccionario_general | - [ ] falta |
| 1469 | `LEXR-01197` | el umbral | diccionario_general | - [ ] falta |
| 1470 | `LEXR-00536` | el uvillo (fruta silvestre comestible) | diccionario_general | - [ ] falta |
| 1471 | `LEXR-02945` | el vado | diccionario_general | - [ ] falta |
| 1472 | `LEXR-01686` | el valle | diccionario_general | - [ ] falta |
| 1473 | `LEXR-00784` | el verano | diccionario_general | - [ ] falta |
| 1474 | `LEXR-00509` | el vestido (de mujer) | diccionario_general | - [ ] falta |
| 1475 | `LEXR-02184` | el vientre | diccionario_general | - [ ] falta |
| 1476 | `LEXR-02798` | el viernes | diccionario_general | - [ ] falta |
| 1477 | `LEXR-01988` | el viudo | diccionario_general | - [ ] falta |
| 1478 | `LEXR-03802` | el vómito | diccionario_general | - [ ] falta |
| 1479 | `LEXR-01997` | el yerno | diccionario_general | - [ ] falta |
| 1480 | `LEXR-03910` | el yucal | diccionario_general | - [ ] falta |
| 1481 | `LEXR-01940` | el zamarro | diccionario_general | - [ ] falta |
| 1482 | `LEXR-02199` | el zancudo | diccionario_general | - [ ] falta |
| 1483 | `LEXR-01959` | el zanjón de agua | diccionario_general | - [ ] falta |
| 1484 | `LEXR-03492` | el zapallo rayado | diccionario_general | - [ ] falta |
| 1485 | `LEXR-00541` | el zapato | diccionario_general | - [x] `diccionario_general/el_zapato.png` |
| 1486 | `LEXR-01163` | el zorro (mamífero) | diccionario_general | - [ ] falta |
| 1487 | `LEXR-02127` | el zurrón (botija de piel para guarapo) | diccionario_general | - [ ] falta |
| 1488 | `LEXR-01827` | el águila (ave) | diccionario_general | - [ ] falta |
| 1489 | `LEXR-02128` | el ánima (del difunto) | diccionario_general | - [ ] falta |
| 1490 | `LEXR-00698` | el ídolo | diccionario_general | - [ ] falta |
| 1491 | `LEXR-03867` | el último hijo, a | diccionario_general | - [ ] falta |
| 1492 | `LEXR-03474` | ellos, ellas | diccionario_general | - [ ] falta |
| 1493 | `LEXR-00558` | ellos, ellas, aquellos, aquellas | diccionario_general | - [ ] falta |
| 1494 | `LEXR-00460` | embarrar | diccionario_general | - [ ] falta |
| 1495 | `LEXR-03830` | embijarse | diccionario_general | - [ ] falta |
| 1496 | `LEXR-03871` | emborracharse | diccionario_general | - [ ] falta |
| 1497 | `LEXR-02340` | embotado | diccionario_general | - [ ] falta |
| 1498 | `LEXR-00651` | embotarse | diccionario_general | - [ ] falta |
| 1499 | `LEXR-03041` | empachar | diccionario_general | - [ ] falta |
| 1500 | `LEXR-00926` | empajar | diccionario_general | - [ ] falta |
| 1501 | `LEXR-03114` | empeorar, aumentar más y más | diccionario_general | - [ ] falta |
| 1502 | `LEXR-02860` | emperzar, comenzar | diccionario_general | - [ ] falta |
| 1503 | `LEXR-01210` | empezar | diccionario_general | - [ ] falta |
| 1504 | `LEXR-01363` | empezar a hervir, burbjear | diccionario_general | - [x] `diccionario_general/empezar_a_hervir,_burbjear.png` |
| 1505 | `LEXR-01247` | empezar, emprender (un trabajo) | diccionario_general | - [ ] falta |
| 1506 | `LEXR-02582` | empobrecerse | diccionario_general | - [ ] falta |
| 1507 | `LEXR-03155` | empujar | diccionario_general | - [ ] falta |
| 1508 | `LEXR-00838` | empujar (con violencia) | diccionario_general | - [ ] falta |
| 1509 | `LEXR-01008` | empujar (repetidas veces) | diccionario_general | - [ ] falta |
| 1510 | `LEXR-01798` | en esta tierra, en este mundo | diccionario_general | - [ ] falta |
| 1511 | `LEXR-00888` | en forma de bola | diccionario_general | - [ ] falta |
| 1512 | `LEXR-01955` | en frente de la casa | diccionario_general | - [ ] falta |
| 1513 | `LEXR-03475` | en frente de, delante de, ante | diccionario_general | - [ ] falta |
| 1514 | `LEXR-03896` | en la otra semana | diccionario_general | - [ ] falta |
| 1515 | `LEXR-03120` | en medio de | diccionario_general | - [ ] falta |
| 1516 | `LEXR-03449` | en medio de, entre | diccionario_general | - [ ] falta |
| 1517 | `LEXR-03763` | en seco (tierra firme) | diccionario_general | - [ ] falta |
| 1518 | `LEXR-03354` | en sueños | diccionario_general | - [ ] falta |
| 1519 | `LEXR-03424` | en tiempo de luna | diccionario_general | - [ ] falta |
| 1520 | `LEXR-01536` | en todas partes | diccionario_general | - [ ] falta |
| 1521 | `LEXR-02264` | en vano, inútilmente | diccionario_general | - [ ] falta |
| 1522 | `LEXR-02144` | en vano, sin motivo, de nada | diccionario_general | - [ ] falta |
| 1523 | `LEXR-00580` | en vez... | diccionario_general | - [ ] falta |
| 1524 | `LEXR-01273` | en, de | diccionario_general | - [ ] falta |
| 1525 | `LEXR-03726` | encabado | diccionario_general | - [ ] falta |
| 1526 | `LEXR-01071` | encargar | diccionario_general | - [ ] falta |
| 1527 | `LEXR-01307` | encargo | diccionario_general | - [ ] falta |
| 1528 | `LEXR-01546` | encender, alumbrar | diccionario_general | - [ ] falta |
| 1529 | `LEXR-00877` | encerrar, encarcelar | diccionario_general | - [ ] falta |
| 1530 | `LEXR-02836` | encogerse | diccionario_general | - [ ] falta |
| 1531 | `LEXR-01214` | encogerse (tela) | diccionario_general | - [ ] falta |
| 1532 | `LEXR-03439` | encomendar | diccionario_general | - [ ] falta |
| 1533 | `LEXR-02330` | encontrar (algo que otro ha perdido) | diccionario_general | - [ ] falta |
| 1534 | `LEXR-01614` | encontrarse con otro | diccionario_general | - [ ] falta |
| 1535 | `LEXR-01081` | encontrarse con otro (que viene del rumbo opuesto | diccionario_general | - [ ] falta |
| 1536 | `LEXR-02453` | encorvado | diccionario_general | - [ ] falta |
| 1537 | `LEXR-03063` | encorvarse | diccionario_general | - [ ] falta |
| 1538 | `LEXR-03463` | encorvarse, inclinarse | diccionario_general | - [ ] falta |
| 1539 | `LEXR-02530` | endemoniado | diccionario_general | - [ ] falta |
| 1540 | `LEXR-01847` | enderezarse | diccionario_general | - [ ] falta |
| 1541 | `LEXR-03767` | endulzar | diccionario_general | - [ ] falta |
| 1542 | `LEXR-02541` | endurecer | diccionario_general | - [ ] falta |
| 1543 | `LEXR-00415` | enemistarse, hacerse enemigos | diccionario_general | - [ ] falta |
| 1544 | `LEXR-00772` | enfadarse | diccionario_general | - [ ] falta |
| 1545 | `LEXR-02223` | enfadarse, enojarse (mutuamente) | diccionario_general | - [ ] falta |
| 1546 | `LEXR-00849` | enfermarse, sufrir dolores de parto | diccionario_general | - [ ] falta |
| 1547 | `LEXR-00833` | enfermedad contagiosa | diccionario_general | - [ ] falta |
| 1548 | `LEXR-02025` | enfermedad de granos | diccionario_general | - [ ] falta |
| 1549 | `LEXR-02083` | enfermedad de los ojos | diccionario_general | - [ ] falta |
| 1550 | `LEXR-01575` | enfermo | diccionario_general | - [ ] falta |
| 1551 | `LEXR-03482` | enfilarse (según cierto orden) | diccionario_general | - [ ] falta |
| 1552 | `LEXR-03546` | enflaquecerse | diccionario_general | - [ ] falta |
| 1553 | `LEXR-02774` | enflaquecerse, delilitarse | diccionario_general | - [ ] falta |
| 1554 | `LEXR-01453` | enfriar, refrescar | diccionario_general | - [ ] falta |
| 1555 | `LEXR-02958` | enfriarse | diccionario_general | - [ ] falta |
| 1556 | `LEXR-03852` | enganchar, abrochar | diccionario_general | - [ ] falta |
| 1557 | `LEXR-00845` | engañarse | diccionario_general | - [ ] falta |
| 1558 | `LEXR-03026` | engordarse | diccionario_general | - [ ] falta |
| 1559 | `LEXR-01790` | enjuagar | diccionario_general | - [ ] falta |
| 1560 | `LEXR-02370` | enlazar | diccionario_general | - [ ] falta |
| 1561 | `LEXR-03564` | enloquecerse | diccionario_general | - [ ] falta |
| 1562 | `LEXR-00493` | enmohecerse | diccionario_general | - [ ] falta |
| 1563 | `LEXR-01656` | ennegrecer, ponerse negro | diccionario_general | - [ ] falta |
| 1564 | `LEXR-03251` | enojarse | diccionario_general | - [ ] falta |
| 1565 | `LEXR-02547` | enojarse (mutuamente) | diccionario_general | - [ ] falta |
| 1566 | `LEXR-01290` | enorgullecerse | diccionario_general | - [ ] falta |
| 1567 | `LEXR-03232` | enorgullecerse, sentirse orgulloso | diccionario_general | - [ ] falta |
| 1568 | `LEXR-01146` | enraizar | diccionario_general | - [ ] falta |
| 1569 | `LEXR-00569` | enredarse | diccionario_general | - [ ] falta |
| 1570 | `LEXR-00510` | enriquecerse, ser rico | diccionario_general | - [ ] falta |
| 1571 | `LEXR-01108` | enrollado | diccionario_general | - [ ] falta |
| 1572 | `LEXR-00628` | enrollar | diccionario_general | - [ ] falta |
| 1573 | `LEXR-00846` | enrollarse, enredarse | diccionario_general | - [ ] falta |
| 1574 | `LEXR-01306` | ensanchar | diccionario_general | - [ ] falta |
| 1575 | `LEXR-02638` | ensartar | diccionario_general | - [ ] falta |
| 1576 | `LEXR-00607` | ensayar, probar, tratar de | diccionario_general | - [ ] falta |
| 1577 | `LEXR-01113` | enseñanza | diccionario_general | - [ ] falta |
| 1578 | `LEXR-00983` | enseñar | diccionario_general | - [ ] falta |
| 1579 | `LEXR-01266` | ensillado | diccionario_general | - [ ] falta |
| 1580 | `LEXR-00563` | ensillar | diccionario_general | - [ ] falta |
| 1581 | `LEXR-01517` | ensuciar, tiznar | diccionario_general | - [ ] falta |
| 1582 | `LEXR-01734` | entenado, a | diccionario_general | - [ ] falta |
| 1583 | `LEXR-02596` | entenderse | diccionario_general | - [ ] falta |
| 1584 | `LEXR-02869` | entiesar, ponerse tieso | diccionario_general | - [ ] falta |
| 1585 | `LEXR-02810` | entonces | diccionario_general | - [ ] falta |
| 1586 | `LEXR-02403` | entrar | diccionario_general | - [ ] falta |
| 1587 | `LEXR-02991` | entrar brevemente | diccionario_general | - [ ] falta |
| 1588 | `LEXR-01799` | entre los de la misma tribu páez | diccionario_general | - [ ] falta |
| 1589 | `LEXR-03734` | entre ustedes, unos con otros | diccionario_general | - [ ] falta |
| 1590 | `LEXR-00622` | entregar voluntariamente | diccionario_general | - [ ] falta |
| 1591 | `LEXR-02659` | entregar, pagar deuda | diccionario_general | - [ ] falta |
| 1592 | `LEXR-02544` | entregarse voluntariamente | diccionario_general | - [ ] falta |
| 1593 | `LEXR-03864` | entristecer, causar tristeza | diccionario_general | - [ ] falta |
| 1594 | `LEXR-03080` | entristecer, hacer sufrir | diccionario_general | - [ ] falta |
| 1595 | `LEXR-02322` | entumirse | diccionario_general | - [ ] falta |
| 1596 | `LEXR-01577` | envejecerse (hombre o cosa) | diccionario_general | - [ ] falta |
| 1597 | `LEXR-01749` | envejercerse (mujer) | diccionario_general | - [ ] falta |
| 1598 | `LEXR-01696` | envoltura | diccionario_general | - [ ] falta |
| 1599 | `LEXR-01317` | envolver | diccionario_general | - [ ] falta |
| 1600 | `LEXR-02011` | envolver (repetidas veces) | diccionario_general | - [ ] falta |
| 1601 | `LEXR-01026` | envolver, enrollar | diccionario_general | - [ ] falta |
| 1602 | `LEXR-01224` | equivocarse, desviarse, dejarse engeñar | diccionario_general | - [ ] falta |
| 1603 | `LEXR-02823` | erizar | diccionario_general | - [ ] falta |
| 1604 | `LEXR-01408` | erizar (varias veces) | diccionario_general | - [ ] falta |
| 1605 | `LEXR-03123` | erizo, puerco espín | diccionario_general | - [ ] falta |
| 1606 | `LEXR-01461` | error, equivocación | diccionario_general | - [ ] falta |
| 1607 | `LEXR-02552` | eructar | diccionario_general | - [ ] falta |
| 1608 | `LEXR-02507` | escama (de pescado) | diccionario_general | - [ ] falta |
| 1609 | `LEXR-02666` | escampar | diccionario_general | - [ ] falta |
| 1610 | `LEXR-03523` | escancel (planta medicinal) | diccionario_general | - [ ] falta |
| 1611 | `LEXR-01569` | escarbar | diccionario_general | - [ ] falta |
| 1612 | `LEXR-03884` | escarbar (con uña) | diccionario_general | - [ ] falta |
| 1613 | `LEXR-02075` | escarbar, arar | diccionario_general | - [ ] falta |
| 1614 | `LEXR-01816` | escoba | diccionario_general | - [ ] falta |
| 1615 | `LEXR-01885` | escoger | diccionario_general | - [ ] falta |
| 1616 | `LEXR-00654` | escogido | diccionario_general | - [ ] falta |
| 1617 | `LEXR-02232` | esconder | diccionario_general | - [ ] falta |
| 1618 | `LEXR-03438` | esconderse | diccionario_general | - [ ] falta |
| 1619 | `LEXR-01755` | escopeta | diccionario_general | - [ ] falta |
| 1620 | `LEXR-01914` | escribano, escribiente | diccionario_general | - [ ] falta |
| 1621 | `LEXR-02160` | escrito | diccionario_general | - [ ] falta |
| 1622 | `LEXR-03602` | escritura | diccionario_general | - [ ] falta |
| 1623 | `LEXR-01177` | escuchar, oir | diccionario_general | - [ ] falta |
| 1624 | `LEXR-03508` | escuela | diccionario_general | - [ ] falta |
| 1625 | `LEXR-00943` | escupir | diccionario_general | - [ ] falta |
| 1626 | `LEXR-03533` | escupir en | diccionario_general | - [ ] falta |
| 1627 | `LEXR-03538` | ese, esa | diccionario_general | - [ ] falta |
| 1628 | `LEXR-00731` | eslabón (hierro para afilar o para sacar fuego del pedernal) | diccionario_general | - [ ] falta |
| 1629 | `LEXR-01378` | esmeralda, colibrí (ave) | diccionario_general | - [ ] falta |
| 1630 | `LEXR-02811` | esos, esas | diccionario_general | - [ ] falta |
| 1631 | `LEXR-03737` | esparcir | diccionario_general | - [ ] falta |
| 1632 | `LEXR-02257` | especie de planta | diccionario_general | - [ ] falta |
| 1633 | `LEXR-02881` | especie de árbol | diccionario_general | - [ ] falta |
| 1634 | `LEXR-01638` | esperar | diccionario_general | - [ ] falta |
| 1635 | `LEXR-03921` | esperarse, ponerse espeso | diccionario_general | - [ ] falta |
| 1636 | `LEXR-01597` | espesarse, ponerse espeso | diccionario_general | - [ ] falta |
| 1637 | `LEXR-03229` | espeso | diccionario_general | - [ ] falta |
| 1638 | `LEXR-03156` | espeso (miel, goma, etc.) | diccionario_general | - [ ] falta |
| 1639 | `LEXR-03207` | espiar | diccionario_general | - [ ] falta |
| 1640 | `LEXR-03121` | espiga de trigo | diccionario_general | - [ ] falta |
| 1641 | `LEXR-01196` | espina de cabuya | diccionario_general | - [ ] falta |
| 1642 | `LEXR-03462` | espina dorsal | diccionario_general | - [ ] falta |
| 1643 | `LEXR-01888` | espinarse, chuzar | diccionario_general | - [ ] falta |
| 1644 | `LEXR-01087` | esponjarse, hincharse | diccionario_general | - [ ] falta |
| 1645 | `LEXR-01234` | esposa | diccionario_general | - [ ] falta |
| 1646 | `LEXR-03715` | esposa del primo | diccionario_general | - [ ] falta |
| 1647 | `LEXR-00444` | esposo de la prima | diccionario_general | - [ ] falta |
| 1648 | `LEXR-03095` | espíritus de las quebradas | diccionario_general | - [ ] falta |
| 1649 | `LEXR-03877` | esquilar | diccionario_general | - [ ] falta |
| 1650 | `LEXR-03466` | esquina de la casa | diccionario_general | - [ ] falta |
| 1651 | `LEXR-00669` | esta generación, contemporáneos | diccionario_general | - [ ] falta |
| 1652 | `LEXR-00848` | estantillo de la casa | diccionario_general | - [ ] falta |
| 1653 | `LEXR-02738` | estar (parado) | diccionario_general | - [ ] falta |
| 1654 | `LEXR-03527` | estar (sentado, acostado, coljado), habitar, morar | diccionario_general | - [ ] falta |
| 1655 | `LEXR-01102` | estar alentado, estar bien | diccionario_general | - [ ] falta |
| 1656 | `LEXR-02212` | estar ausente | diccionario_general | - [ ] falta |
| 1657 | `LEXR-00639` | estar callado, guardar silencio | diccionario_general | - [ ] falta |
| 1658 | `LEXR-03550` | estar contento | diccionario_general | - [ ] falta |
| 1659 | `LEXR-02501` | estar desnivelado | diccionario_general | - [ ] falta |
| 1660 | `LEXR-03870` | estar desocupado | diccionario_general | - [ ] falta |
| 1661 | `LEXR-00893` | estar disgustado | diccionario_general | - [ ] falta |
| 1662 | `LEXR-00616` | estar embarazada, encinta | diccionario_general | - [ ] falta |
| 1663 | `LEXR-00711` | estar encarcelado, detenido | diccionario_general | - [ ] falta |
| 1664 | `LEXR-01703` | estar enfermo | diccionario_general | - [ ] falta |
| 1665 | `LEXR-01952` | estar hambriento | diccionario_general | - [ ] falta |
| 1666 | `LEXR-02297` | estar medio colgado | diccionario_general | - [ ] falta |
| 1667 | `LEXR-00648` | estar ocupado | diccionario_general | - [ ] falta |
| 1668 | `LEXR-00678` | estar panzón | diccionario_general | - [ ] falta |
| 1669 | `LEXR-02408` | estar parado, de pie | diccionario_general | - [ ] falta |
| 1670 | `LEXR-03782` | estar renuente, tener pereza, no tener ganas | diccionario_general | - [ ] falta |
| 1671 | `LEXR-01844` | estar suspendido | diccionario_general | - [ ] falta |
| 1672 | `LEXR-01706` | estar triste | diccionario_general | - [ ] falta |
| 1673 | `LEXR-00979` | este, esta, esto | diccionario_general | - [ ] falta |
| 1674 | `LEXR-02745` | estigma de maíz, pelo de maíz | diccionario_general | - [ ] falta |
| 1675 | `LEXR-00515` | estirarse | diccionario_general | - [ ] falta |
| 1676 | `LEXR-00676` | estornudar | diccionario_general | - [ ] falta |
| 1677 | `LEXR-03685` | estrangular | diccionario_general | - [ ] falta |
| 1678 | `LEXR-01051` | estregar | diccionario_general | - [ ] falta |
| 1679 | `LEXR-03273` | eucalipto (árbol) | diccionario_general | - [ ] falta |
| 1680 | `LEXR-02250` | evidentemente, es evidente | diccionario_general | - [ ] falta |
| 1681 | `LEXR-02106` | excremento, estiércol (de animal) | diccionario_general | - [ ] falta |
| 1682 | `LEXR-01963` | experimentar tristeza | diccionario_general | - [ ] falta |
| 1683 | `LEXR-02517` | explicar, hacer entender | diccionario_general | - [ ] falta |
| 1684 | `LEXR-02895` | extender los brazos | diccionario_general | - [ ] falta |
| 1685 | `LEXR-03059` | extraer muela | diccionario_general | - [ ] falta |
| 1686 | `LEXR-01460` | extranjero, forastero | diccionario_general | - [ ] falta |
| 1687 | `LEXR-03878` | extrañarse | diccionario_general | - [ ] falta |
| 1688 | `LEXR-00517` | fabricar vasijas de barro | diccionario_general | - [ ] falta |
| 1689 | `LEXR-01560` | fama | diccionario_general | - [ ] falta |
| 1690 | `LEXR-03738` | familia, los de la casa | diccionario_general | - [ ] falta |
| 1691 | `LEXR-02269` | famoso, personaje importante | diccionario_general | - [ ] falta |
| 1692 | `LEXR-02164` | favor de... | diccionario_general | - [ ] falta |
| 1693 | `LEXR-01916` | favorecer | diccionario_general | - [ ] falta |
| 1694 | `LEXR-01338` | felicitar | diccionario_general | - [ ] falta |
| 1695 | `LEXR-00863` | feo, malo | diccionario_general | - [ ] falta |
| 1696 | `LEXR-03056` | fermentarse | diccionario_general | - [ ] falta |
| 1697 | `LEXR-03493` | fibra de cabuya | diccionario_general | - [ ] falta |
| 1698 | `LEXR-02004` | filos por ambos lados | diccionario_general | - [ ] falta |
| 1699 | `LEXR-03869` | fingir | diccionario_general | - [ ] falta |
| 1700 | `LEXR-03829` | fique | diccionario_general | - [ ] falta |
| 1701 | `LEXR-01167` | flaco, delgado | diccionario_general | - [ ] falta |
| 1702 | `LEXR-03429` | flamear, despedir llamas | diccionario_general | - [ ] falta |
| 1703 | `LEXR-01195` | fleco de la ruana o anaco | diccionario_general | - [ ] falta |
| 1704 | `LEXR-03248` | fleco, borde de la ruana | diccionario_general | - [ ] falta |
| 1705 | `LEXR-03799` | flojo | diccionario_general | - [ ] falta |
| 1706 | `LEXR-02211` | flojo, poco apretado (tornillo, cuerda) | diccionario_general | - [ ] falta |
| 1707 | `LEXR-00596` | flor de maíz | diccionario_general | - [x] `diccionario_general/flor_de_maíz.png` |
| 1708 | `LEXR-01880` | florecer | diccionario_general | - [ ] falta |
| 1709 | `LEXR-02207` | flotar | diccionario_general | - [ ] falta |
| 1710 | `LEXR-03880` | fondo de la olla | diccionario_general | - [ ] falta |
| 1711 | `LEXR-00519` | formar chupo (tumor) | diccionario_general | - [ ] falta |
| 1712 | `LEXR-01036` | formar grano | diccionario_general | - [ ] falta |
| 1713 | `LEXR-01267` | formar granos | diccionario_general | - [ ] falta |
| 1714 | `LEXR-00405` | formar tumor o chupo | diccionario_general | - [ ] falta |
| 1715 | `LEXR-01305` | fortalecer | diccionario_general | - [ ] falta |
| 1716 | `LEXR-01368` | fortalecer, animar | diccionario_general | - [ ] falta |
| 1717 | `LEXR-03655` | fracturado | diccionario_general | - [ ] falta |
| 1718 | `LEXR-03586` | fracturar | diccionario_general | - [ ] falta |
| 1719 | `LEXR-01405` | fracturar (varias veces o en varias partes) | diccionario_general | - [ ] falta |
| 1720 | `LEXR-00684` | fracturar hueso | diccionario_general | - [ ] falta |
| 1721 | `LEXR-03414` | fracturar, quebrar | diccionario_general | - [ ] falta |
| 1722 | `LEXR-02443` | fracturar, quebrarse | diccionario_general | - [ ] falta |
| 1723 | `LEXR-01188` | frailejón | diccionario_general | - [ ] falta |
| 1724 | `LEXR-03035` | frailejón (planta) | diccionario_general | - [ ] falta |
| 1725 | `LEXR-01487` | frecuentemente, con frecuencia, a menudo | diccionario_general | - [ ] falta |
| 1726 | `LEXR-01859` | fregado | diccionario_general | - [ ] falta |
| 1727 | `LEXR-03171` | frincir las cejas | diccionario_general | - [ ] falta |
| 1728 | `LEXR-00441` | frotar, alisar | diccionario_general | - [ ] falta |
| 1729 | `LEXR-03303` | fríjol blanco | diccionario_general | - [ ] falta |
| 1730 | `LEXR-00745` | fríjol cacha | diccionario_general | - [ ] falta |
| 1731 | `LEXR-02722` | fríjol pintado | diccionario_general | - [ ] falta |
| 1732 | `LEXR-01263` | fríjol rojo | diccionario_general | - [ ] falta |
| 1733 | `LEXR-00603` | frío | diccionario_general | - [ ] falta |
| 1734 | `LEXR-01715` | fuerte | diccionario_general | - [ ] falta |
| 1735 | `LEXR-02862` | fácil | diccionario_general | - [ ] falta |
| 1736 | `LEXR-03054` | gallinazo | diccionario_general | - [ ] falta |
| 1737 | `LEXR-03107` | ganar, vencer, ganar dinero, sufrir, experimentar, padecer | diccionario_general | - [ ] falta |
| 1738 | `LEXR-02185` | garra, uña (de pájaro) | diccionario_general | - [ ] falta |
| 1739 | `LEXR-03419` | gatear | diccionario_general | - [ ] falta |
| 1740 | `LEXR-02049` | gato | diccionario_general | - [ ] falta |
| 1741 | `LEXR-03843` | gavilán | diccionario_general | - [ ] falta |
| 1742 | `LEXR-03326` | genir (repetidas veces) | diccionario_general | - [ ] falta |
| 1743 | `LEXR-03516` | germen de maíz | diccionario_general | - [ ] falta |
| 1744 | `LEXR-01578` | glotón | diccionario_general | - [ ] falta |
| 1745 | `LEXR-03317` | glotón, comilón | diccionario_general | - [ ] falta |
| 1746 | `LEXR-00900` | gobernador del Cauca | diccionario_general | - [ ] falta |
| 1747 | `LEXR-01330` | gobernador indígena del resguardo | diccionario_general | - [ ] falta |
| 1748 | `LEXR-01598` | golpear (repetidas veces), aglomerarse | diccionario_general | - [ ] falta |
| 1749 | `LEXR-02681` | golpear (varias veces) | diccionario_general | - [ ] falta |
| 1750 | `LEXR-00794` | golpear, chocar con, colindar con | diccionario_general | - [ ] falta |
| 1751 | `LEXR-02438` | golpear, tocar (la puerta) | diccionario_general | - [ ] falta |
| 1752 | `LEXR-02924` | gordo | diccionario_general | - [ ] falta |
| 1753 | `LEXR-00397` | gorgojearse | diccionario_general | - [ ] falta |
| 1754 | `LEXR-01165` | gotear | diccionario_general | - [ ] falta |
| 1755 | `LEXR-01765` | gozo | diccionario_general | - [ ] falta |
| 1756 | `LEXR-03265` | granadilla (fruta) | diccionario_general | - [ ] falta |
| 1757 | `LEXR-01410` | granadillo | diccionario_general | - [ ] falta |
| 1758 | `LEXR-02431` | grande (gente) | diccionario_general | - [ ] falta |
| 1759 | `LEXR-00564` | grande, alto | diccionario_general | - [ ] falta |
| 1760 | `LEXR-02729` | grande, importante | diccionario_general | - [ ] falta |
| 1761 | `LEXR-00876` | grando de maíz | diccionario_general | - [ ] falta |
| 1762 | `LEXR-00777` | grano | diccionario_general | - [ ] falta |
| 1763 | `LEXR-02242` | grato | diccionario_general | - [ ] falta |
| 1764 | `LEXR-00830` | grieta, rendija | diccionario_general | - [ ] falta |
| 1765 | `LEXR-00497` | grillo | diccionario_general | - [x] `diccionario_general/grillo.png` |
| 1766 | `LEXR-02338` | gris | diccionario_general | - [ ] falta |
| 1767 | `LEXR-02941` | gris, pardo | diccionario_general | - [ ] falta |
| 1768 | `LEXR-01015` | gritar | diccionario_general | - [ ] falta |
| 1769 | `LEXR-02816` | grueso | diccionario_general | - [ ] falta |
| 1770 | `LEXR-02753` | grueso y alto | diccionario_general | - [ ] falta |
| 1771 | `LEXR-03576` | guacamayo | diccionario_general | - [ ] falta |
| 1772 | `LEXR-03596` | guache (culebra) | diccionario_general | - [ ] falta |
| 1773 | `LEXR-02642` | guagua, paca (mamífero roedor) | diccionario_general | - [ ] falta |
| 1774 | `LEXR-02353` | guama | diccionario_general | - [ ] falta |
| 1775 | `LEXR-03007` | guamo | diccionario_general | - [ ] falta |
| 1776 | `LEXR-02318` | guantín (mamífero roedor) | diccionario_general | - [ ] falta |
| 1777 | `LEXR-01053` | guardar, cruzar los brazos | diccionario_general | - [ ] falta |
| 1778 | `LEXR-00386` | guasca de fique | diccionario_general | - [ ] falta |
| 1779 | `LEXR-03868` | guayaba (fruta) | diccionario_general | - [x] `diccionario_general/guayaba_(fruta).png` |
| 1780 | `LEXR-00844` | gusano | diccionario_general | - [ ] falta |
| 1781 | `LEXR-02592` | gusano venenoso | diccionario_general | - [ ] falta |
| 1782 | `LEXR-00811` | guía | diccionario_general | - [ ] falta |
| 1783 | `LEXR-03469` | haba | diccionario_general | - [ ] falta |
| 1784 | `LEXR-02697` | haber derrumbe | diccionario_general | - [ ] falta |
| 1785 | `LEXR-02148` | haber eclipse de luna | diccionario_general | - [ ] falta |
| 1786 | `LEXR-01616` | haber eclipse de sol | diccionario_general | - [ ] falta |
| 1787 | `LEXR-01860` | haber temblor, terremoto | diccionario_general | - [ ] falta |
| 1788 | `LEXR-01106` | habitante de Tierradentro | diccionario_general | - [ ] falta |
| 1789 | `LEXR-01618` | habitante del pueblo | diccionario_general | - [ ] falta |
| 1790 | `LEXR-03033` | habitante, morador | diccionario_general | - [ ] falta |
| 1791 | `LEXR-01361` | hablar contra otro | diccionario_general | - [ ] falta |
| 1792 | `LEXR-01821` | hablar en voz alta | diccionario_general | - [ ] falta |
| 1793 | `LEXR-02825` | hablar en voz baja | diccionario_general | - [ ] falta |
| 1794 | `LEXR-00787` | hablar mal | diccionario_general | - [ ] falta |
| 1795 | `LEXR-02402` | hace tiempo | diccionario_general | - [ ] falta |
| 1796 | `LEXR-01906` | hacer abrir | diccionario_general | - [ ] falta |
| 1797 | `LEXR-03695` | hacer abundar | diccionario_general | - [ ] falta |
| 1798 | `LEXR-01722` | hacer acercar, arrimar | diccionario_general | - [ ] falta |
| 1799 | `LEXR-00866` | hacer amarrar | diccionario_general | - [ ] falta |
| 1800 | `LEXR-02364` | hacer amontonar | diccionario_general | - [ ] falta |
| 1801 | `LEXR-02334` | hacer ampollas | diccionario_general | - [ ] falta |
| 1802 | `LEXR-03129` | hacer andar | diccionario_general | - [ ] falta |
| 1803 | `LEXR-00585` | hacer aparar | diccionario_general | - [ ] falta |
| 1804 | `LEXR-01447` | hacer arrastrar | diccionario_general | - [ ] falta |
| 1805 | `LEXR-00500` | hacer arrear | diccionario_general | - [ ] falta |
| 1806 | `LEXR-01712` | hacer arreglar | diccionario_general | - [ ] falta |
| 1807 | `LEXR-02603` | hacer arrodillar | diccionario_general | - [ ] falta |
| 1808 | `LEXR-02740` | hacer asar | diccionario_general | - [ ] falta |
| 1809 | `LEXR-00781` | hacer atajar, mandar atajar | diccionario_general | - [ ] falta |
| 1810 | `LEXR-02911` | hacer ayudar, permitir ayudar | diccionario_general | - [ ] falta |
| 1811 | `LEXR-03012` | hacer bailar | diccionario_general | - [x] `diccionario_general/hacer_bailar.png` |
| 1812 | `LEXR-01115` | hacer bajar (dese arriba) | diccionario_general | - [ ] falta |
| 1813 | `LEXR-02151` | hacer barbacoa | diccionario_general | - [ ] falta |
| 1814 | `LEXR-01092` | hacer barro | diccionario_general | - [ ] falta |
| 1815 | `LEXR-02425` | hacer basura o polvo | diccionario_general | - [ ] falta |
| 1816 | `LEXR-03706` | hacer bañar (a otro) | diccionario_general | - [ ] falta |
| 1817 | `LEXR-03705` | hacer beber | diccionario_general | - [ ] falta |
| 1818 | `LEXR-03165` | hacer bostezar | diccionario_general | - [ ] falta |
| 1819 | `LEXR-01279` | hacer brotar | diccionario_general | - [ ] falta |
| 1820 | `LEXR-02369` | hacer caer, dejar caer | diccionario_general | - [ ] falta |
| 1821 | `LEXR-02417` | hacer callar | diccionario_general | - [ ] falta |
| 1822 | `LEXR-01191` | hacer calor | diccionario_general | - [ ] falta |
| 1823 | `LEXR-01845` | hacer cambiar | diccionario_general | - [ ] falta |
| 1824 | `LEXR-00692` | hacer cantar | diccionario_general | - [ ] falta |
| 1825 | `LEXR-03227` | hacer cargar (ej. niño, en el bautismo) | diccionario_general | - [ ] falta |
| 1826 | `LEXR-00694` | hacer cargar, echar carga | diccionario_general | - [ ] falta |
| 1827 | `LEXR-00570` | hacer casa | diccionario_general | - [ ] falta |
| 1828 | `LEXR-02519` | hacer casarse | diccionario_general | - [ ] falta |
| 1829 | `LEXR-03310` | hacer chicha | diccionario_general | - [ ] falta |
| 1830 | `LEXR-00954` | hacer chupar, desinflamar | diccionario_general | - [ ] falta |
| 1831 | `LEXR-00859` | hacer clavar, mandar crucificar | diccionario_general | - [ ] falta |
| 1832 | `LEXR-02094` | hacer cocer | diccionario_general | - [ ] falta |
| 1833 | `LEXR-03730` | hacer coger, hacer prender | diccionario_general | - [ ] falta |
| 1834 | `LEXR-01198` | hacer confrontar | diccionario_general | - [ ] falta |
| 1835 | `LEXR-03110` | hacer correr | diccionario_general | - [ ] falta |
| 1836 | `LEXR-01586` | hacer cortar (palo) | diccionario_general | - [ ] falta |
| 1837 | `LEXR-03889` | hacer coser | diccionario_general | - [ ] falta |
| 1838 | `LEXR-00420` | hacer cosquillas | diccionario_general | - [ ] falta |
| 1839 | `LEXR-02910` | hacer creer | diccionario_general | - [ ] falta |
| 1840 | `LEXR-03173` | hacer cubrir | diccionario_general | - [ ] falta |
| 1841 | `LEXR-01778` | hacer cubrirse | diccionario_general | - [ ] falta |
| 1842 | `LEXR-02843` | hacer dar de tomar | diccionario_general | - [ ] falta |
| 1843 | `LEXR-00679` | hacer dar vuelta | diccionario_general | - [ ] falta |
| 1844 | `LEXR-02471` | hacer dañar | diccionario_general | - [ ] falta |
| 1845 | `LEXR-00906` | hacer daño a una persona, agredir | diccionario_general | - [ ] falta |
| 1846 | `LEXR-02693` | hacer dejar | diccionario_general | - [ ] falta |
| 1847 | `LEXR-02913` | hacer demorar, atrasar | diccionario_general | - [ ] falta |
| 1848 | `LEXR-03741` | hacer derretir | diccionario_general | - [ ] falta |
| 1849 | `LEXR-02418` | hacer descansar, aliviar, calmar | diccionario_general | - [ ] falta |
| 1850 | `LEXR-02947` | hacer econtrarse | diccionario_general | - [ ] falta |
| 1851 | `LEXR-03515` | hacer encarar | diccionario_general | - [ ] falta |
| 1852 | `LEXR-03221` | hacer endeudar | diccionario_general | - [ ] falta |
| 1853 | `LEXR-01587` | hacer engordar | diccionario_general | - [ ] falta |
| 1854 | `LEXR-02840` | hacer enojar, ofender | diccionario_general | - [ ] falta |
| 1855 | `LEXR-00682` | hacer entregar | diccionario_general | - [ ] falta |
| 1856 | `LEXR-02255` | hacer envolver | diccionario_general | - [ ] falta |
| 1857 | `LEXR-00402` | hacer eructar | diccionario_general | - [ ] falta |
| 1858 | `LEXR-00916` | hacer escapar, dejar escapar | diccionario_general | - [ ] falta |
| 1859 | `LEXR-03556` | hacer escribir | diccionario_general | - [ ] falta |
| 1860 | `LEXR-01514` | hacer escupir | diccionario_general | - [ ] falta |
| 1861 | `LEXR-00597` | hacer estallar, detonar | diccionario_general | - [ ] falta |
| 1862 | `LEXR-02251` | hacer estanque | diccionario_general | - [ ] falta |
| 1863 | `LEXR-03495` | hacer estornudar | diccionario_general | - [ ] falta |
| 1864 | `LEXR-03499` | hacer estrechar la mano (ej. en las bodas) | diccionario_general | - [ ] falta |
| 1865 | `LEXR-01785` | hacer extender los brazos | diccionario_general | - [ ] falta |
| 1866 | `LEXR-03191` | hacer extraer | diccionario_general | - [ ] falta |
| 1867 | `LEXR-03603` | hacer fiesta | diccionario_general | - [ ] falta |
| 1868 | `LEXR-03770` | hacer firmar | diccionario_general | - [ ] falta |
| 1869 | `LEXR-00498` | hacer firme, apuntalar | diccionario_general | - [ ] falta |
| 1870 | `LEXR-01743` | hacer florecer | diccionario_general | - [ ] falta |
| 1871 | `LEXR-00506` | hacer frío | diccionario_general | - [ ] falta |
| 1872 | `LEXR-02566` | hacer ganar | diccionario_general | - [ ] falta |
| 1873 | `LEXR-01511` | hacer gastar | diccionario_general | - [ ] falta |
| 1874 | `LEXR-01907` | hacer girar | diccionario_general | - [ ] falta |
| 1875 | `LEXR-03847` | hacer gotear | diccionario_general | - [ ] falta |
| 1876 | `LEXR-01787` | hacer gritar | diccionario_general | - [ ] falta |
| 1877 | `LEXR-02953` | hacer guardar | diccionario_general | - [ ] falta |
| 1878 | `LEXR-03681` | hacer invierno | diccionario_general | - [ ] falta |
| 1879 | `LEXR-03331` | hacer lavar las manos | diccionario_general | - [ ] falta |
| 1880 | `LEXR-03725` | hacer llegar | diccionario_general | - [ ] falta |
| 1881 | `LEXR-02465` | hacer lloar | diccionario_general | - [ ] falta |
| 1882 | `LEXR-01742` | hacer llover | diccionario_general | - [ ] falta |
| 1883 | `LEXR-03739` | hacer lo indebido | diccionario_general | - [ ] falta |
| 1884 | `LEXR-01277` | hacer masticar, hacer morder | diccionario_general | - [ ] falta |
| 1885 | `LEXR-00589` | hacer mazamorra | diccionario_general | - [ ] falta |
| 1886 | `LEXR-01552` | hacer medir, hacer contar, hacer probar | diccionario_general | - [ ] falta |
| 1887 | `LEXR-03598` | hacer menear | diccionario_general | - [ ] falta |
| 1888 | `LEXR-00720` | hacer mermar | diccionario_general | - [ ] falta |
| 1889 | `LEXR-00947` | hacer montar | diccionario_general | - [ ] falta |
| 1890 | `LEXR-02317` | hacer muecas | diccionario_general | - [ ] falta |
| 1891 | `LEXR-03597` | hacer obedecer | diccionario_general | - [ ] falta |
| 1892 | `LEXR-00770` | hacer olvidar | diccionario_general | - [ ] falta |
| 1893 | `LEXR-01515` | hacer pagar | diccionario_general | - [ ] falta |
| 1894 | `LEXR-01445` | hacer parar | diccionario_general | - [ ] falta |
| 1895 | `LEXR-02529` | hacer parar, hacer detenerse | diccionario_general | - [ ] falta |
| 1896 | `LEXR-03282` | hacer pasar por (ej. el río) | diccionario_general | - [ ] falta |
| 1897 | `LEXR-02200` | hacer pelear | diccionario_general | - [ ] falta |
| 1898 | `LEXR-03807` | hacer pensar | diccionario_general | - [ ] falta |
| 1899 | `LEXR-03254` | hacer pliegues | diccionario_general | - [ ] falta |
| 1900 | `LEXR-02466` | hacer poner (sombrero) | diccionario_general | - [ ] falta |
| 1901 | `LEXR-03707` | hacer ponr, mandar ponder | diccionario_general | - [ ] falta |
| 1902 | `LEXR-03087` | hacer que otro lo fortalece | diccionario_general | - [ ] falta |
| 1903 | `LEXR-01645` | hacer quemar | diccionario_general | - [ ] falta |
| 1904 | `LEXR-01201` | hacer quitar | diccionario_general | - [ ] falta |
| 1905 | `LEXR-00439` | hacer rayas, pintar | diccionario_general | - [ ] falta |
| 1906 | `LEXR-00391` | hacer recordar | diccionario_general | - [ ] falta |
| 1907 | `LEXR-02467` | hacer regalar | diccionario_general | - [ ] falta |
| 1908 | `LEXR-01971` | hacer regar | diccionario_general | - [ ] falta |
| 1909 | `LEXR-01233` | hacer rendir más, hacer que abunde | diccionario_general | - [ ] falta |
| 1910 | `LEXR-03771` | hacer rezar | diccionario_general | - [ ] falta |
| 1911 | `LEXR-02261` | hacer reír | diccionario_general | - [ ] falta |
| 1912 | `LEXR-00960` | hacer rodar | diccionario_general | - [ ] falta |
| 1913 | `LEXR-02231` | hacer ruido | diccionario_general | - [ ] falta |
| 1914 | `LEXR-01364` | hacer ruido, retumbar | diccionario_general | - [ ] falta |
| 1915 | `LEXR-02746` | hacer saludar | diccionario_general | - [ ] falta |
| 1916 | `LEXR-03014` | hacer sanar | diccionario_general | - [ ] falta |
| 1917 | `LEXR-01646` | hacer sentarse | diccionario_general | - [ ] falta |
| 1918 | `LEXR-02093` | hacer sentir incapaz | diccionario_general | - [ ] falta |
| 1919 | `LEXR-01371` | hacer servir, ocupar, utilizar, usar | diccionario_general | - [ ] falta |
| 1920 | `LEXR-02805` | hacer seña | diccionario_general | - [ ] falta |
| 1921 | `LEXR-00992` | hacer señas | diccionario_general | - [ ] falta |
| 1922 | `LEXR-02655` | hacer señas (con la mirada), guiñar | diccionario_general | - [ ] falta |
| 1923 | `LEXR-02533` | hacer sombra | diccionario_general | - [ ] falta |
| 1924 | `LEXR-02967` | hacer sombra, ocultarse | diccionario_general | - [ ] falta |
| 1925 | `LEXR-01366` | hacer sonar (maraca) | diccionario_general | - [ ] falta |
| 1926 | `LEXR-01512` | hacer subir | diccionario_general | - [ ] falta |
| 1927 | `LEXR-02522` | hacer tener, hacer concebir | diccionario_general | - [ ] falta |
| 1928 | `LEXR-03862` | hacer toser | diccionario_general | - [ ] falta |
| 1929 | `LEXR-01979` | hacer trabajar, obligar a trabajar | diccionario_general | - [ ] falta |
| 1930 | `LEXR-00587` | hacer tragar | diccionario_general | - [ ] falta |
| 1931 | `LEXR-01856` | hacer tropezar | diccionario_general | - [ ] falta |
| 1932 | `LEXR-03679` | hacer un rito (brujo) | diccionario_general | - [ ] falta |
| 1933 | `LEXR-02567` | hacer unir | diccionario_general | - [ ] falta |
| 1934 | `LEXR-03101` | hacer ver | diccionario_general | - [ ] falta |
| 1935 | `LEXR-03108` | hacer ver, hacer mirar | diccionario_general | - [ ] falta |
| 1936 | `LEXR-02442` | hacer verano, hacer sol | diccionario_general | - [ ] falta |
| 1937 | `LEXR-00586` | hacer vestir | diccionario_general | - [ ] falta |
| 1938 | `LEXR-01199` | hacer vivir | diccionario_general | - [ ] falta |
| 1939 | `LEXR-03470` | hacer vomitar | diccionario_general | - [ ] falta |
| 1940 | `LEXR-02085` | hacer, actuar, realizar | diccionario_general | - [ ] falta |
| 1941 | `LEXR-03065` | hacerse mataduras | diccionario_general | - [ ] falta |
| 1942 | `LEXR-01607` | hacerse pedazos | diccionario_general | - [ ] falta |
| 1943 | `LEXR-00812` | hacerse pedazos, despedazarse | diccionario_general | - [ ] falta |
| 1944 | `LEXR-02532` | hacerse responsable por otro | diccionario_general | - [ ] falta |
| 1945 | `LEXR-02617` | hacerse tarde, tardar | diccionario_general | - [ ] falta |
| 1946 | `LEXR-02159` | haciendo bien | diccionario_general | - [ ] falta |
| 1947 | `LEXR-02104` | haciendo mal | diccionario_general | - [ ] falta |
| 1948 | `LEXR-00568` | halar (repetidas veces) | diccionario_general | - [ ] falta |
| 1949 | `LEXR-01695` | halar, arrastrar | diccionario_general | - [ ] falta |
| 1950 | `LEXR-03079` | harina de maíz | diccionario_general | - [ ] falta |
| 1951 | `LEXR-03060` | harina de trigo | diccionario_general | - [ ] falta |
| 1952 | `LEXR-00850` | harina de yuca | diccionario_general | - [x] `diccionario_general/harina_de_yuca.png` |
| 1953 | `LEXR-01595` | hartarse | diccionario_general | - [ ] falta |
| 1954 | `LEXR-03632` | hartarse, saciarse | diccionario_general | - [ ] falta |
| 1955 | `LEXR-00481` | hasta | diccionario_general | - [ ] falta |
| 1956 | `LEXR-01518` | hechizar | diccionario_general | - [ ] falta |
| 1957 | `LEXR-02139` | hecho | diccionario_general | - [ ] falta |
| 1958 | `LEXR-02647` | hemorragia nasal | diccionario_general | - [ ] falta |
| 1959 | `LEXR-01241` | hendir, abrir hendedura | diccionario_general | - [ ] falta |
| 1960 | `LEXR-02525` | herido | diccionario_general | - [ ] falta |
| 1961 | `LEXR-03395` | herirse, lastimarse | diccionario_general | - [ ] falta |
| 1962 | `LEXR-01675` | hermano con hermana | diccionario_general | - [ ] falta |
| 1963 | `LEXR-00634` | hermano con hermano, o hermana con hermana | diccionario_general | - [ ] falta |
| 1964 | `LEXR-01667` | hermano, hermana (del mismo sexo) | diccionario_general | - [ ] falta |
| 1965 | `LEXR-02072` | herrero | diccionario_general | - [ ] falta |
| 1966 | `LEXR-00867` | hervido | diccionario_general | - [ ] falta |
| 1967 | `LEXR-03105` | hervir | diccionario_general | - [ ] falta |
| 1968 | `LEXR-01846` | hervir, dejar hervir | diccionario_general | - [ ] falta |
| 1969 | `LEXR-01101` | hiel | diccionario_general | - [ ] falta |
| 1970 | `LEXR-01403` | hierbabuena (planta) | diccionario_general | - [ ] falta |
| 1971 | `LEXR-02704` | hija mayor | diccionario_general | - [ ] falta |
| 1972 | `LEXR-01741` | hija menor | diccionario_general | - [ ] falta |
| 1973 | `LEXR-03118` | hijastra | diccionario_general | - [ ] falta |
| 1974 | `LEXR-00895` | hijastro | diccionario_general | - [ ] falta |
| 1975 | `LEXR-02061` | hilar | diccionario_general | - [ ] falta |
| 1976 | `LEXR-02105` | hilo | diccionario_general | - [ ] falta |
| 1977 | `LEXR-02796` | hincharse | diccionario_general | - [ ] falta |
| 1978 | `LEXR-02279` | hinchazón | diccionario_general | - [ ] falta |
| 1979 | `LEXR-02253` | hoja de arbusto | diccionario_general | - [ ] falta |
| 1980 | `LEXR-01155` | hoja de mejicano (da sabor a la mazamorra) | diccionario_general | - [ ] falta |
| 1981 | `LEXR-02259` | hormiga | diccionario_general | - [x] `diccionario_general/hormiga.png` |
| 1982 | `LEXR-01793` | hormiga grande (insecto) | diccionario_general | - [x] `diccionario_general/hormiga_grande_(insecto).png` |
| 1983 | `LEXR-01928` | hospedar | diccionario_general | - [ ] falta |
| 1984 | `LEXR-00940` | hoy, ahora, recién | diccionario_general | - [ ] falta |
| 1985 | `LEXR-00447` | hueco | diccionario_general | - [ ] falta |
| 1986 | `LEXR-03032` | hueso de la nuca | diccionario_general | - [ ] falta |
| 1987 | `LEXR-01702` | huevo crudo | diccionario_general | - [ ] falta |
| 1988 | `LEXR-01407` | humear | diccionario_general | - [ ] falta |
| 1989 | `LEXR-00928` | humedecerse | diccionario_general | - [ ] falta |
| 1990 | `LEXR-01867` | hundirse, zambullirse | diccionario_general | - [ ] falta |
| 1991 | `LEXR-00621` | huésped | diccionario_general | - [ ] falta |
| 1992 | `LEXR-00610` | húmedo | diccionario_general | - [ ] falta |
| 1993 | `LEXR-01825` | ida | diccionario_general | - [ ] falta |
| 1994 | `LEXR-02480` | igual | diccionario_general | - [ ] falta |
| 1995 | `LEXR-00948` | igualar (el peso), comparar | diccionario_general | - [ ] falta |
| 1996 | `LEXR-02610` | iluminación | diccionario_general | - [ ] falta |
| 1997 | `LEXR-01250` | imitar, remedar | diccionario_general | - [ ] falta |
| 1998 | `LEXR-01718` | impartir (luz, calor, frío) | diccionario_general | - [ ] falta |
| 1999 | `LEXR-03149` | inclinar la cabeza | diccionario_general | - [ ] falta |
| 2000 | `LEXR-01899` | incomodarse | diccionario_general | - [ ] falta |
| 2001 | `LEXR-01890` | indicar, señalar (con el dedo) | diccionario_general | - [ ] falta |
| 2002 | `LEXR-00670` | indigino, deficiente | diccionario_general | - [ ] falta |
| 2003 | `LEXR-03800` | indígena guambiano | diccionario_general | - [ ] falta |
| 2004 | `LEXR-01737` | infanticida | diccionario_general | - [ ] falta |
| 2005 | `LEXR-03006` | inferior | diccionario_general | - [ ] falta |
| 2006 | `LEXR-00553` | inflamarse | diccionario_general | - [ ] falta |
| 2007 | `LEXR-00414` | inmenso | diccionario_general | - [ ] falta |
| 2008 | `LEXR-03246` | inmortal | diccionario_general | - [ ] falta |
| 2009 | `LEXR-02832` | inocente | diccionario_general | - [ ] falta |
| 2010 | `LEXR-00918` | insertar | diccionario_general | - [ ] falta |
| 2011 | `LEXR-00809` | insinuar, hablar indirectamente de otro | diccionario_general | - [ ] falta |
| 2012 | `LEXR-03043` | inspector | diccionario_general | - [ ] falta |
| 2013 | `LEXR-03405` | instrumento para matar | diccionario_general | - [ ] falta |
| 2014 | `LEXR-03373` | insuficiente, incompleto, menos | diccionario_general | - [ ] falta |
| 2015 | `LEXR-03824` | insultar, ultrajar | diccionario_general | - [ ] falta |
| 2016 | `LEXR-02045` | inteligente | diccionario_general | - [ ] falta |
| 2017 | `LEXR-02964` | intervenir | diccionario_general | - [ ] falta |
| 2018 | `LEXR-00779` | intervenir (en una conversación) | diccionario_general | - [ ] falta |
| 2019 | `LEXR-00981` | invierno | diccionario_general | - [ ] falta |
| 2020 | `LEXR-01010` | invisible | diccionario_general | - [ ] falta |
| 2021 | `LEXR-01875` | invitar a varias personas | diccionario_general | - [ ] falta |
| 2022 | `LEXR-00887` | invitar, convidar | diccionario_general | - [ ] falta |
| 2023 | `LEXR-02995` | inútil, inservible | diccionario_general | - [ ] falta |
| 2024 | `LEXR-03593` | ir y venir (varias veces) | diccionario_general | - [ ] falta |
| 2025 | `LEXR-01468` | ir, aprovechando la oportunidad de acompañar a otro | diccionario_general | - [ ] falta |
| 2026 | `LEXR-00741` | ir, irse | diccionario_general | - [ ] falta |
| 2027 | `LEXR-03085` | jactarse, hablar con orgullo | diccionario_general | - [ ] falta |
| 2028 | `LEXR-01437` | jadear, respirar con dificultad | diccionario_general | - [ ] falta |
| 2029 | `LEXR-01315` | jardín | diccionario_general | - [ ] falta |
| 2030 | `LEXR-03172` | jigra con huecos grandes | diccionario_general | - [ ] falta |
| 2031 | `LEXR-03844` | jigra de colores | diccionario_general | - [ ] falta |
| 2032 | `LEXR-01996` | jigra tejida con agujas grandes | diccionario_general | - [ ] falta |
| 2033 | `LEXR-02293` | jinete, que monta a caballo | diccionario_general | - [ ] falta |
| 2034 | `LEXR-02272` | joven adulto | diccionario_general | - [ ] falta |
| 2035 | `LEXR-00930` | juguetear (repetidas veces) | diccionario_general | - [ ] falta |
| 2036 | `LEXR-00437` | juguetón | diccionario_general | - [ ] falta |
| 2037 | `LEXR-02866` | juntar, unir | diccionario_general | - [ ] falta |
| 2038 | `LEXR-00869` | jáquima | diccionario_general | - [ ] falta |
| 2039 | `LEXR-00588` | la abeja (insecto) | diccionario_general | - [x] `diccionario_general/la_abeja_(insecto).png` |
| 2040 | `LEXR-00816` | la abuela | diccionario_general | - [ ] falta |
| 2041 | `LEXR-01666` | la abuela, bisabuela | diccionario_general | - [ ] falta |
| 2042 | `LEXR-01021` | la acequia | diccionario_general | - [ ] falta |
| 2043 | `LEXR-00852` | la aguja | diccionario_general | - [ ] falta |
| 2044 | `LEXR-00897` | la ahijada | diccionario_general | - [ ] falta |
| 2045 | `LEXR-01747` | la almohada | diccionario_general | - [ ] falta |
| 2046 | `LEXR-01396` | la alpargata | diccionario_general | - [ ] falta |
| 2047 | `LEXR-01904` | la altasara | diccionario_general | - [ ] falta |
| 2048 | `LEXR-00837` | la araña (arácnido) | diccionario_general | - [x] `diccionario_general/la_araña_(arácnido).png` |
| 2049 | `LEXR-02178` | la ardilla (mamífero roedor) | diccionario_general | - [ ] falta |
| 2050 | `LEXR-00613` | la arena | diccionario_general | - [ ] falta |
| 2051 | `LEXR-03920` | la arepa | diccionario_general | - [x] `diccionario_general/la_arepa.png` |
| 2052 | `LEXR-03600` | la arruga | diccionario_general | - [ ] falta |
| 2053 | `LEXR-01995` | la avispa (insecto) | diccionario_general | - [ ] falta |
| 2054 | `LEXR-02389` | la ayuda | diccionario_general | - [ ] falta |
| 2055 | `LEXR-00383` | la barbacoa (cama hecha de palos) | diccionario_general | - [ ] falta |
| 2056 | `LEXR-01376` | la basura | diccionario_general | - [ ] falta |
| 2057 | `LEXR-02648` | la batata (planta, de tubérculos comestibles) | diccionario_general | - [ ] falta |
| 2058 | `LEXR-02735` | la bifurcacíon (del río) | diccionario_general | - [ ] falta |
| 2059 | `LEXR-03357` | la blusa de lana | diccionario_general | - [ ] falta |
| 2060 | `LEXR-03647` | la boda, día del casamiento | diccionario_general | - [ ] falta |
| 2061 | `LEXR-01033` | la boda, el casamiento (díade la ceremonia) | diccionario_general | - [ ] falta |
| 2062 | `LEXR-01625` | la borrachera | diccionario_general | - [ ] falta |
| 2063 | `LEXR-01083` | la broma, el chiste, la chanza | diccionario_general | - [ ] falta |
| 2064 | `LEXR-00965` | la brujería hechicería | diccionario_general | - [ ] falta |
| 2065 | `LEXR-02307` | la cabeza | diccionario_general | - [ ] falta |
| 2066 | `LEXR-01779` | la cabra, el chivo | diccionario_general | - [ ] falta |
| 2067 | `LEXR-03693` | la cabuya, el fique | diccionario_general | - [ ] falta |
| 2068 | `LEXR-02111` | la cadera | diccionario_general | - [ ] falta |
| 2069 | `LEXR-01441` | la caldera | diccionario_general | - [ ] falta |
| 2070 | `LEXR-02782` | la calle, el callejón | diccionario_general | - [ ] falta |
| 2071 | `LEXR-02101` | la cama | diccionario_general | - [ ] falta |
| 2072 | `LEXR-01782` | la camisa | diccionario_general | - [ ] falta |
| 2073 | `LEXR-02037` | la campana | diccionario_general | - [ ] falta |
| 2074 | `LEXR-02479` | la cana | diccionario_general | - [ ] falta |
| 2075 | `LEXR-02847` | la candela, el fuego | diccionario_general | - [x] `diccionario_general/la_candela,_el_fuego.png` |
| 2076 | `LEXR-00783` | la candelilla (insecto) | diccionario_general | - [ ] falta |
| 2077 | `LEXR-02368` | la candelilla, luciérnaga | diccionario_general | - [ ] falta |
| 2078 | `LEXR-01849` | la canilla | diccionario_general | - [ ] falta |
| 2079 | `LEXR-00681` | la canoa (artesa para la chicha) | diccionario_general | - [x] `diccionario_general/la_canoa_(artesa_para_la_chicha).png` |
| 2080 | `LEXR-03849` | la cara, el rostro | diccionario_general | - [ ] falta |
| 2081 | `LEXR-02468` | la carne | diccionario_general | - [ ] falta |
| 2082 | `LEXR-02497` | la carne espumosa | diccionario_general | - [ ] falta |
| 2083 | `LEXR-01103` | la casa | diccionario_general | - [ ] falta |
| 2084 | `LEXR-01609` | la casa de la minga | diccionario_general | - [ ] falta |
| 2085 | `LEXR-02371` | la casa donde se celebra la fiesta | diccionario_general | - [ ] falta |
| 2086 | `LEXR-00964` | la caspa | diccionario_general | - [ ] falta |
| 2087 | `LEXR-02983` | la catarata | diccionario_general | - [ ] falta |
| 2088 | `LEXR-01370` | la caña brava (planta) | diccionario_general | - [ ] falta |
| 2089 | `LEXR-01978` | la caña brava del páramo (planta) | diccionario_general | - [ ] falta |
| 2090 | `LEXR-01412` | la cebolla (planta, de raíz comestible) | diccionario_general | - [ ] falta |
| 2091 | `LEXR-01780` | la cecina | diccionario_general | - [ ] falta |
| 2092 | `LEXR-00956` | la ceniza, la pólvora | diccionario_general | - [ ] falta |
| 2093 | `LEXR-02861` | la cera (del oído), cerúmen | diccionario_general | - [ ] falta |
| 2094 | `LEXR-02661` | la cerbatana, bodoquera | diccionario_general | - [ ] falta |
| 2095 | `LEXR-01009` | la cerca, el cerco | diccionario_general | - [ ] falta |
| 2096 | `LEXR-01090` | la chamiza | diccionario_general | - [ ] falta |
| 2097 | `LEXR-02357` | la chinche del árbol | diccionario_general | - [ ] falta |
| 2098 | `LEXR-02044` | la chispa | diccionario_general | - [ ] falta |
| 2099 | `LEXR-01203` | la chonta (especie de palmera), la vara de chonta | diccionario_general | - [ ] falta |
| 2100 | `LEXR-02914` | la chucha, zarigüeya (mamífero) | diccionario_general | - [ ] falta |
| 2101 | `LEXR-03029` | la cicatriz, marca | diccionario_general | - [ ] falta |
| 2102 | `LEXR-02824` | la cidrayota (planta comestible) | diccionario_general | - [ ] falta |
| 2103 | `LEXR-02998` | la circuela silvestre (fruta) | diccionario_general | - [ ] falta |
| 2104 | `LEXR-03193` | la ciudad | diccionario_general | - [ ] falta |
| 2105 | `LEXR-00690` | la clavija (para torcer laso) | diccionario_general | - [ ] falta |
| 2106 | `LEXR-02834` | la clueca | diccionario_general | - [ ] falta |
| 2107 | `LEXR-01138` | la cobija | diccionario_general | - [ ] falta |
| 2108 | `LEXR-02931` | la cobija (tejido en telar) | diccionario_general | - [ ] falta |
| 2109 | `LEXR-01965` | la coca (planta) | diccionario_general | - [ ] falta |
| 2110 | `LEXR-01520` | la cocinera | diccionario_general | - [ ] falta |
| 2111 | `LEXR-01226` | la cola | diccionario_general | - [ ] falta |
| 2112 | `LEXR-01465` | la compañera (mujer que cohabita con un hombre sin casarse) | diccionario_general | - [ ] falta |
| 2113 | `LEXR-02343` | la concuñada | diccionario_general | - [ ] falta |
| 2114 | `LEXR-02773` | la coral (culebra) | diccionario_general | - [ ] falta |
| 2115 | `LEXR-02678` | la coronilla (de la cabeza) | diccionario_general | - [ ] falta |
| 2116 | `LEXR-03176` | la corriente del rió | diccionario_general | - [ ] falta |
| 2117 | `LEXR-03020` | la corteza de árbol | diccionario_general | - [ ] falta |
| 2118 | `LEXR-02337` | la costilla, el costado | diccionario_general | - [ ] falta |
| 2119 | `LEXR-01989` | la coyuntura, canuto de la caña | diccionario_general | - [ ] falta |
| 2120 | `LEXR-00936` | la cresta (de gallo) | diccionario_general | - [ ] falta |
| 2121 | `LEXR-02393` | la cucaracha (insecto) | diccionario_general | - [ ] falta |
| 2122 | `LEXR-02095` | la cuchara | diccionario_general | - [ ] falta |
| 2123 | `LEXR-01095` | la culebra | diccionario_general | - [x] `diccionario_general/la_culebra.png` |
| 2124 | `LEXR-03444` | la culpa, delito | diccionario_general | - [ ] falta |
| 2125 | `LEXR-01704` | la curuba (fruta) | diccionario_general | - [ ] falta |
| 2126 | `LEXR-01068` | la cuñada (entre mujeres) | diccionario_general | - [ ] falta |
| 2127 | `LEXR-03130` | la cárcel | diccionario_general | - [ ] falta |
| 2128 | `LEXR-03502` | la danta (mamífero) | diccionario_general | - [ ] falta |
| 2129 | `LEXR-00723` | la derecha | diccionario_general | - [ ] falta |
| 2130 | `LEXR-02460` | la desgracia | diccionario_general | - [ ] falta |
| 2131 | `LEXR-02409` | la deuda | diccionario_general | - [ ] falta |
| 2132 | `LEXR-02147` | la diarrea | diccionario_general | - [ ] falta |
| 2133 | `LEXR-02689` | la dolencia | diccionario_general | - [ ] falta |
| 2134 | `LEXR-03669` | la enfermedad, peste, epidemia | diccionario_general | - [ ] falta |
| 2135 | `LEXR-02780` | la enjalma | diccionario_general | - [ ] falta |
| 2136 | `LEXR-00929` | la entrada | diccionario_general | - [ ] falta |
| 2137 | `LEXR-02033` | la era, el surco, la hilera | diccionario_general | - [ ] falta |
| 2138 | `LEXR-03092` | la escalera | diccionario_general | - [ ] falta |
| 2139 | `LEXR-01356` | la escarcha | diccionario_general | - [ ] falta |
| 2140 | `LEXR-03351` | la escopeta | diccionario_general | - [ ] falta |
| 2141 | `LEXR-01255` | la espalda | diccionario_general | - [ ] falta |
| 2142 | `LEXR-03614` | la espiga | diccionario_general | - [ ] falta |
| 2143 | `LEXR-03125` | la espina, zarza | diccionario_general | - [ ] falta |
| 2144 | `LEXR-02872` | la espuma | diccionario_general | - [ ] falta |
| 2145 | `LEXR-03775` | la espuma del jabón | diccionario_general | - [ ] falta |
| 2146 | `LEXR-02621` | la estera | diccionario_general | - [ ] falta |
| 2147 | `LEXR-03004` | la estrella | diccionario_general | - [ ] falta |
| 2148 | `LEXR-01186` | la estrella fugaz | diccionario_general | - [ ] falta |
| 2149 | `LEXR-01556` | la faja, el chumbe | diccionario_general | - [ ] falta |
| 2150 | `LEXR-02256` | la fiebre | diccionario_general | - [ ] falta |
| 2151 | `LEXR-00701` | la fiesta | diccionario_general | - [ ] falta |
| 2152 | `LEXR-02157` | la flauta | diccionario_general | - [ ] falta |
| 2153 | `LEXR-00730` | la flauta (de carrizos verticales) | diccionario_general | - [ ] falta |
| 2154 | `LEXR-02226` | la flor | diccionario_general | - [ ] falta |
| 2155 | `LEXR-01700` | la fontanela | diccionario_general | - [ ] falta |
| 2156 | `LEXR-00902` | la fornicadora | diccionario_general | - [ ] falta |
| 2157 | `LEXR-01126` | la frente | diccionario_general | - [ ] falta |
| 2158 | `LEXR-02644` | la fruta | diccionario_general | - [ ] falta |
| 2159 | `LEXR-01905` | la gallina | diccionario_general | - [ ] falta |
| 2160 | `LEXR-01404` | la garganta | diccionario_general | - [ ] falta |
| 2161 | `LEXR-01884` | la garganta, cuello | diccionario_general | - [ ] falta |
| 2162 | `LEXR-02141` | la gargantilla, collar de cuentas | diccionario_general | - [ ] falta |
| 2163 | `LEXR-03856` | la gente de la minga (’invitados’) | diccionario_general | - [ ] falta |
| 2164 | `LEXR-02572` | la golondrina (ave) | diccionario_general | - [ ] falta |
| 2165 | `LEXR-02280` | la gotera | diccionario_general | - [ ] falta |
| 2166 | `LEXR-03355` | la guacharaca (ave) | diccionario_general | - [ ] falta |
| 2167 | `LEXR-02923` | la guadua (especie de bambú) | diccionario_general | - [ ] falta |
| 2168 | `LEXR-03388` | la guala (ave, como gallinazo) | diccionario_general | - [ ] falta |
| 2169 | `LEXR-01217` | la guaraca, honda | diccionario_general | - [ ] falta |
| 2170 | `LEXR-00661` | la guasca, cuerda, soga, piola | diccionario_general | - [ ] falta |
| 2171 | `LEXR-03311` | la guayaba (fruta) | diccionario_general | - [ ] falta |
| 2172 | `LEXR-02462` | la haba | diccionario_general | - [ ] falta |
| 2173 | `LEXR-02899` | la hamaca | diccionario_general | - [ ] falta |
| 2174 | `LEXR-03636` | la harina | diccionario_general | - [ ] falta |
| 2175 | `LEXR-03443` | la hebilla (del cinturón) | diccionario_general | - [ ] falta |
| 2176 | `LEXR-02152` | la hemorragia | diccionario_general | - [ ] falta |
| 2177 | `LEXR-01519` | la herida, lastimadura | diccionario_general | - [ ] falta |
| 2178 | `LEXR-01464` | la hermana (respecto al hombre) | diccionario_general | - [ ] falta |
| 2179 | `LEXR-01169` | la hidropesía | diccionario_general | - [ ] falta |
| 2180 | `LEXR-00419` | la hierba, maleza | diccionario_general | - [ ] falta |
| 2181 | `LEXR-02321` | la hija | diccionario_general | - [ ] falta |
| 2182 | `LEXR-01528` | la hoja | diccionario_general | - [ ] falta |
| 2183 | `LEXR-03622` | la hoja (de árbol o planta), el papel | diccionario_general | - [ ] falta |
| 2184 | `LEXR-01321` | la hoja de maíz | diccionario_general | - [ ] falta |
| 2185 | `LEXR-01516` | la hormiga (insecto) | diccionario_general | - [x] `diccionario_general/la_hormiga_(insecto).png` |
| 2186 | `LEXR-00687` | la horqueta | diccionario_general | - [ ] falta |
| 2187 | `LEXR-03170` | la horqueta para puerco | diccionario_general | - [ ] falta |
| 2188 | `LEXR-02137` | la hoz (herramienta) | diccionario_general | - [ ] falta |
| 2189 | `LEXR-02800` | la huerta | diccionario_general | - [ ] falta |
| 2190 | `LEXR-00737` | la huerta, hortaliza | diccionario_general | - [ ] falta |
| 2191 | `LEXR-03433` | la iglesia | diccionario_general | - [ ] falta |
| 2192 | `LEXR-01017` | la jigra, el morral, mochila | diccionario_general | - [ ] falta |
| 2193 | `LEXR-00594` | la jovencita, señorita | diccionario_general | - [ ] falta |
| 2194 | `LEXR-02012` | la lama, el musgo | diccionario_general | - [ ] falta |
| 2195 | `LEXR-02742` | la lana | diccionario_general | - [ ] falta |
| 2196 | `LEXR-01042` | la langosta (insecto) | diccionario_general | - [x] `diccionario_general/la_langosta_(insecto).png` |
| 2197 | `LEXR-00566` | la lanza | diccionario_general | - [ ] falta |
| 2198 | `LEXR-01644` | la larva | diccionario_general | - [ ] falta |
| 2199 | `LEXR-02473` | la lechuza, el búho (ave) | diccionario_general | - [ ] falta |
| 2200 | `LEXR-01912` | la lejía | diccionario_general | - [ ] falta |
| 2201 | `LEXR-02071` | la lengua | diccionario_general | - [ ] falta |
| 2202 | `LEXR-02102` | la leña | diccionario_general | - [ ] falta |
| 2203 | `LEXR-03677` | la limeta | diccionario_general | - [ ] falta |
| 2204 | `LEXR-01268` | la llaga, úlcera, ’granos’ | diccionario_general | - [ ] falta |
| 2205 | `LEXR-01531` | la llama | diccionario_general | - [ ] falta |
| 2206 | `LEXR-00691` | la llama (de fuego) | diccionario_general | - [x] `diccionario_general/la_llama_(de_fuego).png` |
| 2207 | `LEXR-02193` | la llave | diccionario_general | - [ ] falta |
| 2208 | `LEXR-01802` | la llovizna | diccionario_general | - [ ] falta |
| 2209 | `LEXR-00538` | la lombricera, el vermífugo | diccionario_general | - [ ] falta |
| 2210 | `LEXR-00921` | la lombriz intestinal | diccionario_general | - [ ] falta |
| 2211 | `LEXR-03696` | la luciérnaga (insecto) | diccionario_general | - [x] `diccionario_general/la_luciérnaga_(insecto).png` |
| 2212 | `LEXR-03403` | la luz, claridad | diccionario_general | - [ ] falta |
| 2213 | `LEXR-01079` | la lámpara | diccionario_general | - [ ] falta |
| 2214 | `LEXR-02705` | la madre | diccionario_general | - [ ] falta |
| 2215 | `LEXR-00807` | la madrina | diccionario_general | - [ ] falta |
| 2216 | `LEXR-02922` | la mamá | diccionario_general | - [ ] falta |
| 2217 | `LEXR-02048` | la manga, el potrero | diccionario_general | - [ ] falta |
| 2218 | `LEXR-03136` | la mano | diccionario_general | - [ ] falta |
| 2219 | `LEXR-01154` | la mano derecha | diccionario_general | - [ ] falta |
| 2220 | `LEXR-01324` | la maraca | diccionario_general | - [ ] falta |
| 2221 | `LEXR-02447` | la maraca, el alfandoque | diccionario_general | - [ ] falta |
| 2222 | `LEXR-01253` | la mariposa (insecto) | diccionario_general | - [x] `diccionario_general/la_mariposa_(insecto).png` |
| 2223 | `LEXR-02728` | la marteja, mono nocturno (mamífero) | diccionario_general | - [ ] falta |
| 2224 | `LEXR-02997` | la mata | diccionario_general | - [ ] falta |
| 2225 | `LEXR-02374` | la mata, el árbol | diccionario_general | - [ ] falta |
| 2226 | `LEXR-01911` | la mazamorra | diccionario_general | - [ ] falta |
| 2227 | `LEXR-02545` | la mecha, pavesa | diccionario_general | - [ ] falta |
| 2228 | `LEXR-01522` | la medianoche | diccionario_general | - [ ] falta |
| 2229 | `LEXR-02344` | la menstruación | diccionario_general | - [ ] falta |
| 2230 | `LEXR-02874` | la mentira | diccionario_general | - [ ] falta |
| 2231 | `LEXR-03096` | la miel de abeja | diccionario_general | - [x] `diccionario_general/la_miel_de_abeja.png` |
| 2232 | `LEXR-00427` | la miel, guerapo de caña sin fermentar | diccionario_general | - [ ] falta |
| 2233 | `LEXR-00913` | la mitad | diccionario_general | - [ ] falta |
| 2234 | `LEXR-03575` | la montura | diccionario_general | - [ ] falta |
| 2235 | `LEXR-01141` | la mosca (insecto) | diccionario_general | - [ ] falta |
| 2236 | `LEXR-00468` | la muchacha | diccionario_general | - [ ] falta |
| 2237 | `LEXR-00740` | la muela | diccionario_general | - [ ] falta |
| 2238 | `LEXR-02999` | la muela del juicio | diccionario_general | - [ ] falta |
| 2239 | `LEXR-01174` | la muerte, día de la muerte | diccionario_general | - [ ] falta |
| 2240 | `LEXR-03611` | la mugre, contaminación | diccionario_general | - [ ] falta |
| 2241 | `LEXR-02475` | la muñeca (parte del brazo) | diccionario_general | - [ ] falta |
| 2242 | `LEXR-02788` | la naranja (fruta) | diccionario_general | - [ ] falta |
| 2243 | `LEXR-03859` | la nariz | diccionario_general | - [ ] falta |
| 2244 | `LEXR-02390` | la nigua (insecto) | diccionario_general | - [ ] falta |
| 2245 | `LEXR-01286` | la noche | diccionario_general | - [ ] falta |
| 2246 | `LEXR-02383` | la novia, comprometida | diccionario_general | - [ ] falta |
| 2247 | `LEXR-01094` | la nube, neblina | diccionario_general | - [ ] falta |
| 2248 | `LEXR-03116` | la nuera | diccionario_general | - [ ] falta |
| 2249 | `LEXR-01879` | la nuez de la garganta | diccionario_general | - [ ] falta |
| 2250 | `LEXR-00516` | la olla | diccionario_general | - [x] `diccionario_general/la_olla.png` |
| 2251 | `LEXR-01384` | la orden, el mandato | diccionario_general | - [ ] falta |
| 2252 | `LEXR-03700` | la oreja | diccionario_general | - [ ] falta |
| 2253 | `LEXR-00543` | la orina | diccionario_general | - [ ] falta |
| 2254 | `LEXR-03353` | la ortiga | diccionario_general | - [ ] falta |
| 2255 | `LEXR-01474` | la oveja | diccionario_general | - [ ] falta |
| 2256 | `LEXR-03187` | la paja | diccionario_general | - [ ] falta |
| 2257 | `LEXR-00554` | la paloma (ave) | diccionario_general | - [ ] falta |
| 2258 | `LEXR-01725` | la panela | diccionario_general | - [ ] falta |
| 2259 | `LEXR-01242` | la pantorrilla | diccionario_general | - [ ] falta |
| 2260 | `LEXR-00388` | la papa | diccionario_general | - [x] `diccionario_general/la_papa.png` |
| 2261 | `LEXR-02169` | la papaya (fruta del papayo) | diccionario_general | - [x] `diccionario_general/la_papaya_(fruta_del_papayo).png` |
| 2262 | `LEXR-02932` | la pareja (de personas) | diccionario_general | - [ ] falta |
| 2263 | `LEXR-00831` | la partera | diccionario_general | - [ ] falta |
| 2264 | `LEXR-02428` | la parálisis | diccionario_general | - [ ] falta |
| 2265 | `LEXR-00786` | la perdiz (ave) | diccionario_general | - [ ] falta |
| 2266 | `LEXR-01982` | la pezuña del puerco | diccionario_general | - [ ] falta |
| 2267 | `LEXR-03259` | la peña | diccionario_general | - [ ] falta |
| 2268 | `LEXR-01132` | la piedra | diccionario_general | - [ ] falta |
| 2269 | `LEXR-01085` | la piedra de afilar | diccionario_general | - [ ] falta |
| 2270 | `LEXR-02031` | la piedra de moler | diccionario_general | - [ ] falta |
| 2271 | `LEXR-02963` | la piel | diccionario_general | - [ ] falta |
| 2272 | `LEXR-02055` | la pierna, la canilla | diccionario_general | - [ ] falta |
| 2273 | `LEXR-02298` | la piña (planta) | diccionario_general | - [x] `diccionario_general/la_piña_(planta).png` |
| 2274 | `LEXR-03166` | la planta del pie | diccionario_general | - [ ] falta |
| 2275 | `LEXR-01642` | la pluma (de gallina) | diccionario_general | - [ ] falta |
| 2276 | `LEXR-02433` | la posada | diccionario_general | - [ ] falta |
| 2277 | `LEXR-00747` | la puerta | diccionario_general | - [ ] falta |
| 2278 | `LEXR-00533` | la pulga (insecto) | diccionario_general | - [ ] falta |
| 2279 | `LEXR-03607` | la pulpa, la carne | diccionario_general | - [ ] falta |
| 2280 | `LEXR-01431` | la punta de la aguja | diccionario_general | - [ ] falta |
| 2281 | `LEXR-00931` | la punta, cumbre | diccionario_general | - [ ] falta |
| 2282 | `LEXR-02688` | la pólvora | diccionario_general | - [ ] falta |
| 2283 | `LEXR-03430` | la quijada | diccionario_general | - [ ] falta |
| 2284 | `LEXR-02631` | la rana (batracio) | diccionario_general | - [x] `diccionario_general/la_rana_(batracio).png` |
| 2285 | `LEXR-02835` | la rascadera, mafafa (planta) | diccionario_general | - [ ] falta |
| 2286 | `LEXR-01173` | la rata (mamífero roedor) | diccionario_general | - [ ] falta |
| 2287 | `LEXR-00842` | la raíz | diccionario_general | - [ ] falta |
| 2288 | `LEXR-03338` | la raíz (de árbol) | diccionario_general | - [ ] falta |
| 2289 | `LEXR-02829` | la red, malla | diccionario_general | - [ ] falta |
| 2290 | `LEXR-03485` | la risa | diccionario_general | - [ ] falta |
| 2291 | `LEXR-03816` | la roca | diccionario_general | - [ ] falta |
| 2292 | `LEXR-00976` | la rodilla | diccionario_general | - [ ] falta |
| 2293 | `LEXR-03011` | la roncha | diccionario_general | - [ ] falta |
| 2294 | `LEXR-02482` | la ropa de boda (de la novia) | diccionario_general | - [ ] falta |
| 2295 | `LEXR-01337` | la roza | diccionario_general | - [ ] falta |
| 2296 | `LEXR-02521` | la roza (de selva virgen) | diccionario_general | - [ ] falta |
| 2297 | `LEXR-03537` | la roza, el maizal | diccionario_general | - [ ] falta |
| 2298 | `LEXR-03228` | la roza, el sembrado | diccionario_general | - [ ] falta |
| 2299 | `LEXR-01583` | la ruana, el anaco | diccionario_general | - [ ] falta |
| 2300 | `LEXR-03743` | la rueca, puchicanga | diccionario_general | - [ ] falta |
| 2301 | `LEXR-01960` | la sabana | diccionario_general | - [ ] falta |
| 2302 | `LEXR-02539` | la sal | diccionario_general | - [ ] falta |
| 2303 | `LEXR-00851` | la sala | diccionario_general | - [ ] falta |
| 2304 | `LEXR-02568` | la salida, en la salida | diccionario_general | - [ ] falta |
| 2305 | `LEXR-00788` | la saliva, baba | diccionario_general | - [ ] falta |
| 2306 | `LEXR-02421` | la sarna | diccionario_general | - [ ] falta |
| 2307 | `LEXR-00938` | la sed | diccionario_general | - [ ] falta |
| 2308 | `LEXR-02029` | la selva | diccionario_general | - [ ] falta |
| 2309 | `LEXR-01551` | la semana | diccionario_general | - [ ] falta |
| 2310 | `LEXR-00800` | la semana pasada | diccionario_general | - [ ] falta |
| 2311 | `LEXR-01898` | la semano pasada | diccionario_general | - [ ] falta |
| 2312 | `LEXR-02311` | la semilla (de plantas), la semilla (raza de animales) | diccionario_general | - [ ] falta |
| 2313 | `LEXR-00532` | la semilla que vuelve a dar después de acosechado, sarapanga | diccionario_general | - [ ] falta |
| 2314 | `LEXR-01322` | la señora (de raza blanca) | diccionario_general | - [ ] falta |
| 2315 | `LEXR-01086` | la señorita (de raza blanca) | diccionario_general | - [ ] falta |
| 2316 | `LEXR-02477` | la soga, el lazo | diccionario_general | - [ ] falta |
| 2317 | `LEXR-00528` | la sombra | diccionario_general | - [ ] falta |
| 2318 | `LEXR-00820` | la sombra (de una persona) | diccionario_general | - [ ] falta |
| 2319 | `LEXR-02285` | la suegra | diccionario_general | - [ ] falta |
| 2320 | `LEXR-01968` | la tapa | diccionario_general | - [ ] falta |
| 2321 | `LEXR-01172` | la tarabita (cuerda pa cruzar el río) | diccionario_general | - [ ] falta |
| 2322 | `LEXR-00697` | la tarabita (para cruzar río) | diccionario_general | - [ ] falta |
| 2323 | `LEXR-02971` | la taza | diccionario_general | - [ ] falta |
| 2324 | `LEXR-01326` | la teja | diccionario_general | - [ ] falta |
| 2325 | `LEXR-01256` | la telaraña | diccionario_general | - [ ] falta |
| 2326 | `LEXR-02333` | la tierra, el terreno, suelo | diccionario_general | - [ ] falta |
| 2327 | `LEXR-01689` | la tijereta (ave) | diccionario_general | - [ ] falta |
| 2328 | `LEXR-02950` | la tinta morada (planta) | diccionario_general | - [ ] falta |
| 2329 | `LEXR-00699` | la tosferina (la tos ferina) | diccionario_general | - [ ] falta |
| 2330 | `LEXR-03637` | la trampa | diccionario_general | - [ ] falta |
| 2331 | `LEXR-01631` | la trampa (con soga) | diccionario_general | - [ ] falta |
| 2332 | `LEXR-00836` | la trenza de cabello o de cabuya | diccionario_general | - [ ] falta |
| 2333 | `LEXR-03359` | la tripa, el intestino | diccionario_general | - [ ] falta |
| 2334 | `LEXR-01504` | la tristeza, angustia | diccionario_general | - [ ] falta |
| 2335 | `LEXR-03380` | la tulpa | diccionario_general | - [ ] falta |
| 2336 | `LEXR-01685` | la tusa de maíz | diccionario_general | - [ ] falta |
| 2337 | `LEXR-02624` | la tía (hermana de la mamá) | diccionario_general | - [ ] falta |
| 2338 | `LEXR-02201` | la uva silvestre | diccionario_general | - [ ] falta |
| 2339 | `LEXR-03774` | la vaca | diccionario_general | - [ ] falta |
| 2340 | `LEXR-00857` | la vara (medida) | diccionario_general | - [ ] falta |
| 2341 | `LEXR-02500` | la vasija, calabacita (partida en mitad) | diccionario_general | - [ ] falta |
| 2342 | `LEXR-01772` | la vejez (refiriendo a un hombre) | diccionario_general | - [ ] falta |
| 2343 | `LEXR-02930` | la vejez (refiriendo a una mujer) | diccionario_general | - [ ] falta |
| 2344 | `LEXR-02446` | la vejiga | diccionario_general | - [ ] falta |
| 2345 | `LEXR-03081` | la vena | diccionario_general | - [ ] falta |
| 2346 | `LEXR-02795` | la vena yugular | diccionario_general | - [ ] falta |
| 2347 | `LEXR-02686` | la verruga | diccionario_general | - [ ] falta |
| 2348 | `LEXR-00706` | la vez, vuelta | diccionario_general | - [ ] falta |
| 2349 | `LEXR-03658` | la vida | diccionario_general | - [ ] falta |
| 2350 | `LEXR-00478` | la vida (futura) | diccionario_general | - [ ] falta |
| 2351 | `LEXR-02909` | la vida (pasada) | diccionario_general | - [ ] falta |
| 2352 | `LEXR-02122` | la viga | diccionario_general | - [x] `diccionario_general/la_viga.png` |
| 2353 | `LEXR-03915` | la viga transversal | diccionario_general | - [ ] falta |
| 2354 | `LEXR-00761` | la visiones | diccionario_general | - [ ] falta |
| 2355 | `LEXR-02814` | la viuda | diccionario_general | - [ ] falta |
| 2356 | `LEXR-01786` | la vulva | diccionario_general | - [ ] falta |
| 2357 | `LEXR-03127` | la yuca (planta, de raíz comestible) | diccionario_general | - [x] `diccionario_general/la_yuca_(planta,_de_raíz_comestible).png` |
| 2358 | `LEXR-01652` | la zanja | diccionario_general | - [ ] falta |
| 2359 | `LEXR-01724` | la zarza (planta) | diccionario_general | - [ ] falta |
| 2360 | `LEXR-01359` | la ánima, la alma del difunto | diccionario_general | - [ ] falta |
| 2361 | `LEXR-03306` | labio | diccionario_general | - [ ] falta |
| 2362 | `LEXR-02023` | ladrar (repetidas veces) | diccionario_general | - [ ] falta |
| 2363 | `LEXR-03399` | lama (planta parasítica) | diccionario_general | - [ ] falta |
| 2364 | `LEXR-03030` | lamer | diccionario_general | - [ ] falta |
| 2365 | `LEXR-01680` | lana de oveja | diccionario_general | - [ ] falta |
| 2366 | `LEXR-02781` | lana teñida | diccionario_general | - [ ] falta |
| 2367 | `LEXR-00590` | lanudo | diccionario_general | - [ ] falta |
| 2368 | `LEXR-01917` | largo | diccionario_general | - [ ] falta |
| 2369 | `LEXR-01751` | las tijeras | diccionario_general | - [ ] falta |
| 2370 | `LEXR-03240` | laurel de cera (árbol) | diccionario_general | - [ ] falta |
| 2371 | `LEXR-03341` | lavar (loza) | diccionario_general | - [ ] falta |
| 2372 | `LEXR-00901` | lavar la cara | diccionario_general | - [ ] falta |
| 2373 | `LEXR-01136` | lavar las manos | diccionario_general | - [ ] falta |
| 2374 | `LEXR-02319` | leche | diccionario_general | - [ ] falta |
| 2375 | `LEXR-02346` | legaña | diccionario_general | - [ ] falta |
| 2376 | `LEXR-02576` | lejos | diccionario_general | - [ ] falta |
| 2377 | `LEXR-00418` | lejos, largo, alto | diccionario_general | - [ ] falta |
| 2378 | `LEXR-01013` | lenguaje, habla, voz | diccionario_general | - [ ] falta |
| 2379 | `LEXR-00668` | levantar chismes | diccionario_general | - [ ] falta |
| 2380 | `LEXR-02583` | levantarse, madrguar | diccionario_general | - [ ] falta |
| 2381 | `LEXR-03119` | lezna (herramienta) | diccionario_general | - [ ] falta |
| 2382 | `LEXR-00935` | librarse | diccionario_general | - [ ] falta |
| 2383 | `LEXR-02511` | liendre | diccionario_general | - [ ] falta |
| 2384 | `LEXR-00765` | ligero | diccionario_general | - [ ] falta |
| 2385 | `LEXR-00555` | ligero, aprisa | diccionario_general | - [ ] falta |
| 2386 | `LEXR-01918` | limosna | diccionario_general | - [ ] falta |
| 2387 | `LEXR-02214` | limpiar | diccionario_general | - [ ] falta |
| 2388 | `LEXR-03437` | limpiar, mugre, quitar contaminación | diccionario_general | - [ ] falta |
| 2389 | `LEXR-01733` | limpiarse (a uno mismo) | diccionario_general | - [ ] falta |
| 2390 | `LEXR-02564` | limpio | diccionario_general | - [ ] falta |
| 2391 | `LEXR-02270` | lindero | diccionario_general | - [ ] falta |
| 2392 | `LEXR-00712` | liso | diccionario_general | - [ ] falta |
| 2393 | `LEXR-01966` | liviano | diccionario_general | - [ ] falta |
| 2394 | `LEXR-02658` | liviano, no pesado | diccionario_general | - [ ] falta |
| 2395 | `LEXR-02787` | llamado | diccionario_general | - [ ] falta |
| 2396 | `LEXR-03777` | llamar | diccionario_general | - [ ] falta |
| 2397 | `LEXR-01572` | llamarse | diccionario_general | - [ ] falta |
| 2398 | `LEXR-01352` | llanto | diccionario_general | - [ ] falta |
| 2399 | `LEXR-03713` | llegada (futura) | diccionario_general | - [ ] falta |
| 2400 | `LEXR-02050` | llegada (pasada) | diccionario_general | - [ ] falta |
| 2401 | `LEXR-01237` | llegar | diccionario_general | - [ ] falta |
| 2402 | `LEXR-00604` | llegar (visitar dos lugares en el mismo viaje) | diccionario_general | - [ ] falta |
| 2403 | `LEXR-02543` | llegar a ser | diccionario_general | - [ ] falta |
| 2404 | `LEXR-02561` | llegar de un viaje | diccionario_general | - [ ] falta |
| 2405 | `LEXR-03071` | llenar | diccionario_general | - [ ] falta |
| 2406 | `LEXR-02248` | llenar, rellenar | diccionario_general | - [ ] falta |
| 2407 | `LEXR-02683` | llenarse | diccionario_general | - [ ] falta |
| 2408 | `LEXR-02724` | lleno | diccionario_general | - [ ] falta |
| 2409 | `LEXR-03073` | llevar (varias personas o varias coas) | diccionario_general | - [ ] falta |
| 2410 | `LEXR-03410` | llevar alrededor de (ej. en procesión) | diccionario_general | - [ ] falta |
| 2411 | `LEXR-03821` | llevar consigo (a otra persona) | diccionario_general | - [ ] falta |
| 2412 | `LEXR-00898` | llevar debajo del brazo, apretar | diccionario_general | - [ ] falta |
| 2413 | `LEXR-01496` | llevar en la mano | diccionario_general | - [ ] falta |
| 2414 | `LEXR-00430` | llevar, guiar, encaminar | diccionario_general | - [ ] falta |
| 2415 | `LEXR-00884` | llorar (al mismo tiempo que hace otra cosa) | diccionario_general | - [ ] falta |
| 2416 | `LEXR-02057` | llorar (por ir con la mamá) | diccionario_general | - [ ] falta |
| 2417 | `LEXR-02397` | llorón | diccionario_general | - [ ] falta |
| 2418 | `LEXR-03409` | llover | diccionario_general | - [ ] falta |
| 2419 | `LEXR-01392` | llovizna | diccionario_general | - [ ] falta |
| 2420 | `LEXR-00742` | lloviznar | diccionario_general | - [ ] falta |
| 2421 | `LEXR-01801` | lo mismo como, igual que | diccionario_general | - [ ] falta |
| 2422 | `LEXR-02671` | lo que da sabor, condimento | diccionario_general | - [ ] falta |
| 2423 | `LEXR-02848` | loco | diccionario_general | - [ ] falta |
| 2424 | `LEXR-02534` | lograr | diccionario_general | - [ ] falta |
| 2425 | `LEXR-01851` | lograr avisar | diccionario_general | - [ ] falta |
| 2426 | `LEXR-01128` | lograr detener | diccionario_general | - [ ] falta |
| 2427 | `LEXR-00778` | lograr empujar | diccionario_general | - [ ] falta |
| 2428 | `LEXR-01127` | lograr entender | diccionario_general | - [ ] falta |
| 2429 | `LEXR-03224` | lograr escuchar | diccionario_general | - [ ] falta |
| 2430 | `LEXR-03335` | lograr hacer entender | diccionario_general | - [ ] falta |
| 2431 | `LEXR-03135` | lograr halar | diccionario_general | - [ ] falta |
| 2432 | `LEXR-01444` | lograr intervenir | diccionario_general | - [ ] falta |
| 2433 | `LEXR-03832` | lograr llevar | diccionario_general | - [ ] falta |
| 2434 | `LEXR-02808` | lograr mirar | diccionario_general | - [ ] falta |
| 2435 | `LEXR-02426` | los antepasados | diccionario_general | - [ ] falta |
| 2436 | `LEXR-03815` | los calzones | diccionario_general | - [ ] falta |
| 2437 | `LEXR-00879` | los de enfrente | diccionario_general | - [ ] falta |
| 2438 | `LEXR-03322` | los padres (padre y madre) | diccionario_general | - [ ] falta |
| 2439 | `LEXR-01061` | los pantalones (de liencillo) | diccionario_general | - [ ] falta |
| 2440 | `LEXR-02430` | los ramos | diccionario_general | - [ ] falta |
| 2441 | `LEXR-03531` | lucero | diccionario_general | - [ ] falta |
| 2442 | `LEXR-01720` | luciérnaga | diccionario_general | - [ ] falta |
| 2443 | `LEXR-00577` | lugar habitual, morada | diccionario_general | - [ ] falta |
| 2444 | `LEXR-03086` | lulo | diccionario_general | - [ ] falta |
| 2445 | `LEXR-02512` | luna nueva | diccionario_general | - [ ] falta |
| 2446 | `LEXR-03873` | luna, mes | diccionario_general | - [ ] falta |
| 2447 | `LEXR-00937` | lágrima | diccionario_general | - [ ] falta |
| 2448 | `LEXR-01641` | macana | diccionario_general | - [ ] falta |
| 2449 | `LEXR-03612` | macana, arma del telar | diccionario_general | - [ ] falta |
| 2450 | `LEXR-01665` | madre | diccionario_general | - [ ] falta |
| 2451 | `LEXR-00986` | madre con hijo u hija | diccionario_general | - [ ] falta |
| 2452 | `LEXR-01811` | madrina con ahijado o ahijada | diccionario_general | - [ ] falta |
| 2453 | `LEXR-02813` | madrino | diccionario_general | - [ ] falta |
| 2454 | `LEXR-01897` | madurarse | diccionario_general | - [ ] falta |
| 2455 | `LEXR-02518` | maestro, que enseña | diccionario_general | - [ ] falta |
| 2456 | `LEXR-01753` | mafafa | diccionario_general | - [ ] falta |
| 2457 | `LEXR-01615` | mafafa (planta comestible) | diccionario_general | - [ ] falta |
| 2458 | `LEXR-02984` | maldecir (deseando mal a otro), ultrajar | diccionario_general | - [ ] falta |
| 2459 | `LEXR-02388` | malgastar | diccionario_general | - [ ] falta |
| 2460 | `LEXR-02017` | malla de alambre | diccionario_general | - [ ] falta |
| 2461 | `LEXR-03476` | malo | diccionario_general | - [ ] falta |
| 2462 | `LEXR-03457` | maltratar | diccionario_general | - [ ] falta |
| 2463 | `LEXR-03854` | maltratar, atacar a un indefenso, agredir | diccionario_general | - [ ] falta |
| 2464 | `LEXR-02003` | maltrato | diccionario_general | - [ ] falta |
| 2465 | `LEXR-03132` | mamar | diccionario_general | - [ ] falta |
| 2466 | `LEXR-03848` | manco, manimocho | diccionario_general | - [ ] falta |
| 2467 | `LEXR-01054` | mandadero | diccionario_general | - [ ] falta |
| 2468 | `LEXR-00390` | mandar alimentar | diccionario_general | - [ ] falta |
| 2469 | `LEXR-03192` | mandar avisar | diccionario_general | - [ ] falta |
| 2470 | `LEXR-02696` | mandar comprar | diccionario_general | - [ ] falta |
| 2471 | `LEXR-03583` | mandar cortar (pelo, tabla) | diccionario_general | - [ ] falta |
| 2472 | `LEXR-03013` | mandar dar látigo | diccionario_general | - [ ] falta |
| 2473 | `LEXR-02652` | mandar encender | diccionario_general | - [ ] falta |
| 2474 | `LEXR-03796` | mandar guardar dieta | diccionario_general | - [ ] falta |
| 2475 | `LEXR-03772` | mandar hervir | diccionario_general | - [ ] falta |
| 2476 | `LEXR-00874` | mandar lavar | diccionario_general | - [ ] falta |
| 2477 | `LEXR-01114` | mandar peinar | diccionario_general | - [ ] falta |
| 2478 | `LEXR-03860` | mandar poner | diccionario_general | - [ ] falta |
| 2479 | `LEXR-02084` | mandar razón | diccionario_general | - [ ] falta |
| 2480 | `LEXR-01568` | mandar saludos | diccionario_general | - [ ] falta |
| 2481 | `LEXR-00486` | mandar soltar, hacer suspender (un trabajo) | diccionario_general | - [ ] falta |
| 2482 | `LEXR-03426` | mandar, enviar | diccionario_general | - [ ] falta |
| 2483 | `LEXR-01813` | mandar, matar | diccionario_general | - [ ] falta |
| 2484 | `LEXR-01972` | mandato, orden | diccionario_general | - [ ] falta |
| 2485 | `LEXR-02176` | manojo de trigo | diccionario_general | - [ ] falta |
| 2486 | `LEXR-01413` | manso | diccionario_general | - [ ] falta |
| 2487 | `LEXR-03180` | mantener, criar | diccionario_general | - [ ] falta |
| 2488 | `LEXR-02934` | maní | diccionario_general | - [ ] falta |
| 2489 | `LEXR-01814` | maní (planta) | diccionario_general | - [ ] falta |
| 2490 | `LEXR-02949` | marco del telar (palos verticales) | diccionario_general | - [ ] falta |
| 2491 | `LEXR-01841` | mascar coca | diccionario_general | - [ ] falta |
| 2492 | `LEXR-02385` | mascar, masticar | diccionario_general | - [ ] falta |
| 2493 | `LEXR-03327` | mata de aguacate | diccionario_general | - [ ] falta |
| 2494 | `LEXR-02415` | mata de cabuya | diccionario_general | - [ ] falta |
| 2495 | `LEXR-03757` | mata de caña brava | diccionario_general | - [ ] falta |
| 2496 | `LEXR-00801` | mata de durazno (árbol) | diccionario_general | - [ ] falta |
| 2497 | `LEXR-03718` | mata de hongo | diccionario_general | - [ ] falta |
| 2498 | `LEXR-01335` | mataganado (culebra) | diccionario_general | - [ ] falta |
| 2499 | `LEXR-00790` | matar | diccionario_general | - [ ] falta |
| 2500 | `LEXR-01067` | mayor (de edad) | diccionario_general | - [ ] falta |
| 2501 | `LEXR-02790` | mayor, el que manda | diccionario_general | - [ ] falta |
| 2502 | `LEXR-03514` | mayordomo | diccionario_general | - [ ] falta |
| 2503 | `LEXR-03908` | mayores | diccionario_general | - [ ] falta |
| 2504 | `LEXR-00520` | mazamorra con sal, sanco | diccionario_general | - [ ] falta |
| 2505 | `LEXR-00540` | mazamorra sin sal | diccionario_general | - [ ] falta |
| 2506 | `LEXR-03645` | maíz | diccionario_general | - [ ] falta |
| 2507 | `LEXR-01985` | maíz amarillo | diccionario_general | - [ ] falta |
| 2508 | `LEXR-00875` | maíz en grano | diccionario_general | - [ ] falta |
| 2509 | `LEXR-01134` | maíz negro | diccionario_general | - [ ] falta |
| 2510 | `LEXR-01372` | maíz pintado | diccionario_general | - [ ] falta |
| 2511 | `LEXR-02809` | maíz pirá | diccionario_general | - [ ] falta |
| 2512 | `LEXR-02263` | maíz sarazo | diccionario_general | - [ ] falta |
| 2513 | `LEXR-00829` | maíz tierno | diccionario_general | - [ ] falta |
| 2514 | `LEXR-02744` | mañana | diccionario_general | - [ ] falta |
| 2515 | `LEXR-00854` | mecer | diccionario_general | - [ ] falta |
| 2516 | `LEXR-03501` | medio, a medias, no enteramente | diccionario_general | - [ ] falta |
| 2517 | `LEXR-02060` | mejilla, cachete | diccionario_general | - [ ] falta |
| 2518 | `LEXR-02556` | mejor, antes bien | diccionario_general | - [ ] falta |
| 2519 | `LEXR-01589` | mejorarse (de una enfermedad) | diccionario_general | - [ ] falta |
| 2520 | `LEXR-01726` | mejorarse, componerse (el tiempo) | diccionario_general | - [ ] falta |
| 2521 | `LEXR-00491` | mejorarse, recuperarse, fortalecerse, arreciar (lluvia) | diccionario_general | - [ ] falta |
| 2522 | `LEXR-02126` | menear (repetidas veces) | diccionario_general | - [ ] falta |
| 2523 | `LEXR-03150` | menear, mover, agitar | diccionario_general | - [ ] falta |
| 2524 | `LEXR-00640` | menear, revolver | diccionario_general | - [ ] falta |
| 2525 | `LEXR-03005` | menitr | diccionario_general | - [ ] falta |
| 2526 | `LEXR-01023` | menitroso | diccionario_general | - [ ] falta |
| 2527 | `LEXR-03402` | menor, segundo | diccionario_general | - [ ] falta |
| 2528 | `LEXR-01788` | menospreciar | diccionario_general | - [ ] falta |
| 2529 | `LEXR-03287` | mentar, mencionar | diccionario_general | - [ ] falta |
| 2530 | `LEXR-02851` | menudo | diccionario_general | - [ ] falta |
| 2531 | `LEXR-00715` | mercado | diccionario_general | - [ ] falta |
| 2532 | `LEXR-03503` | mermar, disminuir, encogerse | diccionario_general | - [ ] falta |
| 2533 | `LEXR-02302` | mes para sembrar maíz | diccionario_general | - [ ] falta |
| 2534 | `LEXR-03916` | metamorfosear (ej. mariposa) | diccionario_general | - [x] `diccionario_general/metamorfosear_(ej._mariposa).png` |
| 2535 | `LEXR-01852` | meter (cosa gruesa) | diccionario_general | - [ ] falta |
| 2536 | `LEXR-01853` | meter (repetidas veces) | diccionario_general | - [ ] falta |
| 2537 | `LEXR-02559` | meter debajo de | diccionario_general | - [ ] falta |
| 2538 | `LEXR-01020` | meter en, echar en | diccionario_general | - [ ] falta |
| 2539 | `LEXR-02739` | mezclar | diccionario_general | - [ ] falta |
| 2540 | `LEXR-02252` | mezquino | diccionario_general | - [ ] falta |
| 2541 | `LEXR-03722` | mi (femenino) | diccionario_general | - [ ] falta |
| 2542 | `LEXR-02113` | mico | diccionario_general | - [ ] falta |
| 2543 | `LEXR-02806` | miel de abeja | diccionario_general | - [x] `diccionario_general/miel_de_abeja.png` |
| 2544 | `LEXR-00671` | miel de caña | diccionario_general | - [ ] falta |
| 2545 | `LEXR-03787` | miembros del cabildo, cabildantes | diccionario_general | - [ ] falta |
| 2546 | `LEXR-00381` | mientras, durante... | diccionario_general | - [ ] falta |
| 2547 | `LEXR-00970` | mirar (al mismo tiempo que hace otra cosa) | diccionario_general | - [ ] falta |
| 2548 | `LEXR-03835` | mirar (repetidas veces) | diccionario_general | - [ ] falta |
| 2549 | `LEXR-01484` | mirar a lo lejos | diccionario_general | - [ ] falta |
| 2550 | `LEXR-02206` | mirar adentro | diccionario_general | - [ ] falta |
| 2551 | `LEXR-00817` | mirar al otro lado | diccionario_general | - [ ] falta |
| 2552 | `LEXR-01672` | mirar arriba (repetidas veces) | diccionario_general | - [ ] falta |
| 2553 | `LEXR-00753` | mirar atrás, voltearse para mirar atrás | diccionario_general | - [ ] falta |
| 2554 | `LEXR-03154` | mirar hacia abajo (repetidas veces) | diccionario_general | - [ ] falta |
| 2555 | `LEXR-03507` | mitad | diccionario_general | - [ ] falta |
| 2556 | `LEXR-02197` | moco | diccionario_general | - [ ] falta |
| 2557 | `LEXR-00889` | mojado | diccionario_general | - [ ] falta |
| 2558 | `LEXR-00977` | mojar, regar | diccionario_general | - [ ] falta |
| 2559 | `LEXR-02769` | mojar, remojar | diccionario_general | - [ ] falta |
| 2560 | `LEXR-01448` | mojarse | diccionario_general | - [ ] falta |
| 2561 | `LEXR-01184` | moler | diccionario_general | - [ ] falta |
| 2562 | `LEXR-01387` | moler (cosa aquada) | diccionario_general | - [ ] falta |
| 2563 | `LEXR-02312` | moler (repetidas veces) | diccionario_general | - [ ] falta |
| 2564 | `LEXR-03473` | moler caña | diccionario_general | - [ ] falta |
| 2565 | `LEXR-02210` | moler finito, desmenuzar | diccionario_general | - [ ] falta |
| 2566 | `LEXR-00404` | molestar (hablando), estorbar | diccionario_general | - [ ] falta |
| 2567 | `LEXR-01593` | molestar (un ruido), hacer bulla | diccionario_general | - [ ] falta |
| 2568 | `LEXR-01789` | molestar, picar (pulga) | diccionario_general | - [ ] falta |
| 2569 | `LEXR-03584` | molestar, poner pereque | diccionario_general | - [ ] falta |
| 2570 | `LEXR-01620` | molleja | diccionario_general | - [ ] falta |
| 2571 | `LEXR-02726` | moneda fraccionaria | diccionario_general | - [ ] falta |
| 2572 | `LEXR-01629` | monedas fraccionarias | diccionario_general | - [ ] falta |
| 2573 | `LEXR-01427` | mono nocturno | diccionario_general | - [ ] falta |
| 2574 | `LEXR-01107` | montar | diccionario_general | - [ ] falta |
| 2575 | `LEXR-02505` | montaña | diccionario_general | - [ ] falta |
| 2576 | `LEXR-03489` | montaña derribada | diccionario_general | - [ ] falta |
| 2577 | `LEXR-03239` | montículo de tierra | diccionario_general | - [ ] falta |
| 2578 | `LEXR-01151` | montón, montículo | diccionario_general | - [ ] falta |
| 2579 | `LEXR-00575` | moquear | diccionario_general | - [ ] falta |
| 2580 | `LEXR-03639` | morado | diccionario_general | - [ ] falta |
| 2581 | `LEXR-02221` | morder (culebra) | diccionario_general | - [ ] falta |
| 2582 | `LEXR-00623` | morir en lugar de otro | diccionario_general | - [ ] falta |
| 2583 | `LEXR-03634` | mortal, destinado a morir | diccionario_general | - [ ] falta |
| 2584 | `LEXR-03675` | mosca | diccionario_general | - [x] `diccionario_general/mosca.png` |
| 2585 | `LEXR-01711` | mosquito (insecto) | diccionario_general | - [x] `diccionario_general/mosquito_(insecto).png` |
| 2586 | `LEXR-01157` | mostacilla (insecto) | diccionario_general | - [ ] falta |
| 2587 | `LEXR-01005` | mostrar | diccionario_general | - [ ] falta |
| 2588 | `LEXR-02295` | mostrar los dientes (de contento) | diccionario_general | - [ ] falta |
| 2589 | `LEXR-01145` | mostrenco, sin marca | diccionario_general | - [ ] falta |
| 2590 | `LEXR-02981` | motilón (árbol, con fruta comestible) | diccionario_general | - [ ] falta |
| 2591 | `LEXR-00855` | moverse | diccionario_general | - [ ] falta |
| 2592 | `LEXR-01189` | moverse (repetidas veces) | diccionario_general | - [ ] falta |
| 2593 | `LEXR-03793` | mucho, muy | diccionario_general | - [ ] falta |
| 2594 | `LEXR-03319` | mudar la piel | diccionario_general | - [ ] falta |
| 2595 | `LEXR-01228` | mudarse de casa, quitarse de, retirarse de | diccionario_general | - [ ] falta |
| 2596 | `LEXR-02771` | mudo | diccionario_general | - [ ] falta |
| 2597 | `LEXR-00991` | muela | diccionario_general | - [ ] falta |
| 2598 | `LEXR-02770` | muerte (futura) | diccionario_general | - [ ] falta |
| 2599 | `LEXR-00882` | muerto | diccionario_general | - [ ] falta |
| 2600 | `LEXR-01762` | mujer encinta, embarazada | diccionario_general | - [ ] falta |
| 2601 | `LEXR-03104` | murciélago | diccionario_general | - [x] `diccionario_general/murciélago.png` |
| 2602 | `LEXR-00660` | murmurar | diccionario_general | - [ ] falta |
| 2603 | `LEXR-02498` | murmurar (ruido del río) | diccionario_general | - [ ] falta |
| 2604 | `LEXR-01663` | muy (árbol, que carga pepa) | diccionario_general | - [ ] falta |
| 2605 | `LEXR-03304` | muy agradable | diccionario_general | - [ ] falta |
| 2606 | `LEXR-01691` | muy cerca | diccionario_general | - [ ] falta |
| 2607 | `LEXR-03902` | muy de mañana, temprano | diccionario_general | - [ ] falta |
| 2608 | `LEXR-03819` | muy sumamente (superlativo) | diccionario_general | - [ ] falta |
| 2609 | `LEXR-00477` | muy triste | diccionario_general | - [ ] falta |
| 2610 | `LEXR-02590` | muy tupido | diccionario_general | - [ ] falta |
| 2611 | `LEXR-00704` | más | diccionario_general | - [ ] falta |
| 2612 | `LEXR-00567` | más (comparativo) | diccionario_general | - [ ] falta |
| 2613 | `LEXR-01148` | más antes | diccionario_general | - [ ] falta |
| 2614 | `LEXR-01421` | más corto | diccionario_general | - [ ] falta |
| 2615 | `LEXR-02908` | más tarde | diccionario_general | - [ ] falta |
| 2616 | `LEXR-01418` | más, grave, peor | diccionario_general | - [ ] falta |
| 2617 | `LEXR-01262` | nacimiento, lugar de nacimiento | diccionario_general | - [ ] falta |
| 2618 | `LEXR-02708` | nadar | diccionario_general | - [x] `diccionario_general/nadar.png` |
| 2619 | `LEXR-00917` | nadia | diccionario_general | - [ ] falta |
| 2620 | `LEXR-03358` | nadie, ninguno | diccionario_general | - [ ] falta |
| 2621 | `LEXR-01736` | naranjal | diccionario_general | - [x] `diccionario_general/naranjal.png` |
| 2622 | `LEXR-01433` | narices, ventana de la nariz | diccionario_general | - [ ] falta |
| 2623 | `LEXR-03160` | nariz aguileña, narigudo | diccionario_general | - [ ] falta |
| 2624 | `LEXR-02145` | nariz chata | diccionario_general | - [ ] falta |
| 2625 | `LEXR-00762` | nariz filuda | diccionario_general | - [ ] falta |
| 2626 | `LEXR-01677` | necesidad | diccionario_general | - [ ] falta |
| 2627 | `LEXR-00815` | necesitar, faltar, hacer falta | diccionario_general | - [ ] falta |
| 2628 | `LEXR-01866` | necesitar, hacer falta | diccionario_general | - [ ] falta |
| 2629 | `LEXR-02194` | negar, no divulgar | diccionario_general | - [ ] falta |
| 2630 | `LEXR-00432` | negar, ocultar | diccionario_general | - [ ] falta |
| 2631 | `LEXR-01205` | negro, sucio | diccionario_general | - [ ] falta |
| 2632 | `LEXR-03909` | ni siquiera | diccionario_general | - [ ] falta |
| 2633 | `LEXR-03328` | ni un poco, ni siquiera | diccionario_general | - [ ] falta |
| 2634 | `LEXR-02898` | nido | diccionario_general | - [ ] falta |
| 2635 | `LEXR-03245` | nivelar, allanar | diccionario_general | - [ ] falta |
| 2636 | `LEXR-03465` | niña del ojo, pupila | diccionario_general | - [ ] falta |
| 2637 | `LEXR-01738` | niño | diccionario_general | - [ ] falta |
| 2638 | `LEXR-01728` | niño prematuro | diccionario_general | - [ ] falta |
| 2639 | `LEXR-01298` | no | diccionario_general | - [ ] falta |
| 2640 | `LEXR-00502` | no en vano | diccionario_general | - [ ] falta |
| 2641 | `LEXR-02905` | nombrado, con el nombre de | diccionario_general | - [ ] falta |
| 2642 | `LEXR-03225` | nosotros, nosotras | diccionario_general | - [ ] falta |
| 2643 | `LEXR-01355` | nube obscura (mal agüero) | diccionario_general | - [ ] falta |
| 2644 | `LEXR-00675` | nubes dispersas | diccionario_general | - [ ] falta |
| 2645 | `LEXR-02636` | nuca | diccionario_general | - [ ] falta |
| 2646 | `LEXR-01104` | nuche (insecto) | diccionario_general | - [ ] falta |
| 2647 | `LEXR-02852` | nueve | diccionario_general | - [ ] falta |
| 2648 | `LEXR-00655` | nuevo | diccionario_general | - [ ] falta |
| 2649 | `LEXR-01093` | nuez de la garganta | diccionario_general | - [ ] falta |
| 2650 | `LEXR-02510` | nunca | diccionario_general | - [ ] falta |
| 2651 | `LEXR-03163` | nunca, jamás | diccionario_general | - [ ] falta |
| 2652 | `LEXR-03529` | nutria | diccionario_general | - [ ] falta |
| 2653 | `LEXR-01835` | nutria (mamífero) | diccionario_general | - [ ] falta |
| 2654 | `LEXR-00891` | o...o | diccionario_general | - [ ] falta |
| 2655 | `LEXR-02542` | obediente | diccionario_general | - [ ] falta |
| 2656 | `LEXR-02976` | obligatoriamente | diccionario_general | - [ ] falta |
| 2657 | `LEXR-01304` | obscurecer | diccionario_general | - [ ] falta |
| 2658 | `LEXR-03345` | obscurecerse | diccionario_general | - [ ] falta |
| 2659 | `LEXR-01406` | obscuro | diccionario_general | - [ ] falta |
| 2660 | `LEXR-01235` | ocho | diccionario_general | - [ ] falta |
| 2661 | `LEXR-03882` | ocultar, disimular | diccionario_general | - [ ] falta |
| 2662 | `LEXR-01318` | ocultarse el sol | diccionario_general | - [ ] falta |
| 2663 | `LEXR-03567` | odedecer, hacer caso | diccionario_general | - [ ] falta |
| 2664 | `LEXR-03046` | ofrecer sal a un caballo | diccionario_general | - [ ] falta |
| 2665 | `LEXR-02009` | ofrendar, propiciar a los espíritus | diccionario_general | - [ ] falta |
| 2666 | `LEXR-03842` | oirse, sonar | diccionario_general | - [ ] falta |
| 2667 | `LEXR-03216` | ojo de aguja | diccionario_general | - [ ] falta |
| 2668 | `LEXR-03689` | ola (del río o mar) | diccionario_general | - [ ] falta |
| 2669 | `LEXR-01311` | oler | diccionario_general | - [ ] falta |
| 2670 | `LEXR-02316` | oler, coger rastro | diccionario_general | - [ ] falta |
| 2671 | `LEXR-00995` | olla de barro | diccionario_general | - [ ] falta |
| 2672 | `LEXR-03281` | olla para guarapo | diccionario_general | - [ ] falta |
| 2673 | `LEXR-01178` | olor fragante | diccionario_general | - [ ] falta |
| 2674 | `LEXR-01204` | oloroso, fétido | diccionario_general | - [ ] falta |
| 2675 | `LEXR-03506` | olvidar | diccionario_general | - [ ] falta |
| 2676 | `LEXR-02870` | olvidarse | diccionario_general | - [ ] falta |
| 2677 | `LEXR-02992` | olvido, olvidado | diccionario_general | - [ ] falta |
| 2678 | `LEXR-00735` | opacar, obscurecerse | diccionario_general | - [ ] falta |
| 2679 | `LEXR-00483` | orange | diccionario_general | - [ ] falta |
| 2680 | `LEXR-00708` | ordenar (repetidas veces) | diccionario_general | - [ ] falta |
| 2681 | `LEXR-03562` | ordenar, gobernar | diccionario_general | - [ ] falta |
| 2682 | `LEXR-02915` | orejudo | diccionario_general | - [ ] falta |
| 2683 | `LEXR-01220` | orgullo | diccionario_general | - [ ] falta |
| 2684 | `LEXR-03406` | orgullo (habla) | diccionario_general | - [ ] falta |
| 2685 | `LEXR-03138` | orgulloso | diccionario_general | - [ ] falta |
| 2686 | `LEXR-01227` | orilla de la olla | diccionario_general | - [ ] falta |
| 2687 | `LEXR-02290` | orilla del río | diccionario_general | - [ ] falta |
| 2688 | `LEXR-03389` | orinar | diccionario_general | - [ ] falta |
| 2689 | `LEXR-01274` | orinar en | diccionario_general | - [ ] falta |
| 2690 | `LEXR-01599` | orín | diccionario_general | - [ ] falta |
| 2691 | `LEXR-03642` | oso | diccionario_general | - [ ] falta |
| 2692 | `LEXR-03883` | otra vez | diccionario_general | - [ ] falta |
| 2693 | `LEXR-01492` | otro | diccionario_general | - [ ] falta |
| 2694 | `LEXR-01398` | oveja | diccionario_general | - [ ] falta |
| 2695 | `LEXR-03352` | oxidado | diccionario_general | - [ ] falta |
| 2696 | `LEXR-03604` | oxidado, corroído | diccionario_general | - [ ] falta |
| 2697 | `LEXR-03785` | oxidarse | diccionario_general | - [ ] falta |
| 2698 | `LEXR-01495` | oyente | diccionario_general | - [ ] falta |
| 2699 | `LEXR-01254` | pacunga (planta) | diccionario_general | - [ ] falta |
| 2700 | `LEXR-03308` | padecer | diccionario_general | - [ ] falta |
| 2701 | `LEXR-01426` | padecer una enfermdad | diccionario_general | - [ ] falta |
| 2702 | `LEXR-01415` | padre | diccionario_general | - [ ] falta |
| 2703 | `LEXR-02793` | padre o madre con el hijo | diccionario_general | - [ ] falta |
| 2704 | `LEXR-01399` | padre o madre con la hija | diccionario_general | - [ ] falta |
| 2705 | `LEXR-03028` | padrino con ahijado o ahijada | diccionario_general | - [ ] falta |
| 2706 | `LEXR-02366` | padrinos (de matrimonio) | diccionario_general | - [ ] falta |
| 2707 | `LEXR-02955` | pagado | diccionario_general | - [ ] falta |
| 2708 | `LEXR-02427` | pagar | diccionario_general | - [ ] falta |
| 2709 | `LEXR-01670` | pagar por otro | diccionario_general | - [ ] falta |
| 2710 | `LEXR-03450` | palma de la mano | diccionario_general | - [ ] falta |
| 2711 | `LEXR-02062` | palo de telar (sostiene el ñuwe) | diccionario_general | - [ ] falta |
| 2712 | `LEXR-02565` | palo horitzontal del telar | diccionario_general | - [ ] falta |
| 2713 | `LEXR-00508` | palo madera | diccionario_general | - [ ] falta |
| 2714 | `LEXR-02804` | palo vertical del telar | diccionario_general | - [ ] falta |
| 2715 | `LEXR-01003` | paloma | diccionario_general | - [ ] falta |
| 2716 | `LEXR-03144` | panderé (árbol) | diccionario_general | - [ ] falta |
| 2717 | `LEXR-03010` | panzón | diccionario_general | - [ ] falta |
| 2718 | `LEXR-02516` | papa menudita | diccionario_general | - [ ] falta |
| 2719 | `LEXR-02092` | papal | diccionario_general | - [ ] falta |
| 2720 | `LEXR-01074` | papaya | diccionario_general | - [ ] falta |
| 2721 | `LEXR-03455` | paralizarse, entumirse | diccionario_general | - [ ] falta |
| 2722 | `LEXR-00571` | pararse, ponerse de pie | diccionario_general | - [ ] falta |
| 2723 | `LEXR-00642` | parcialmente encogido (las piernas) | diccionario_general | - [ ] falta |
| 2724 | `LEXR-00593` | pardo | diccionario_general | - [ ] falta |
| 2725 | `LEXR-01478` | pariente (con respecto a otro pariente | diccionario_general | - [ ] falta |
| 2726 | `LEXR-01858` | parir, poner huevos (gallinas) | diccionario_general | - [ ] falta |
| 2727 | `LEXR-02286` | parpadear | diccionario_general | - [ ] falta |
| 2728 | `LEXR-02283` | partear, atender el parto | diccionario_general | - [ ] falta |
| 2729 | `LEXR-01308` | participar en la molienda | diccionario_general | - [ ] falta |
| 2730 | `LEXR-01795` | partidario | diccionario_general | - [ ] falta |
| 2731 | `LEXR-02758` | partir (en dos o más partes) | diccionario_general | - [ ] falta |
| 2732 | `LEXR-01676` | partir en dos, dividir | diccionario_general | - [ ] falta |
| 2733 | `LEXR-01309` | partir en varios pedazos, despedazar | diccionario_general | - [ ] falta |
| 2734 | `LEXR-00696` | pasado mañana | diccionario_general | - [ ] falta |
| 2735 | `LEXR-03917` | pasajero, que pasa pronto | diccionario_general | - [ ] falta |
| 2736 | `LEXR-02404` | pasajero, viajero | diccionario_general | - [ ] falta |
| 2737 | `LEXR-00797` | pasar | diccionario_general | - [ ] falta |
| 2738 | `LEXR-00827` | pasar (hacia abajo) | diccionario_general | - [ ] falta |
| 2739 | `LEXR-01076` | pasar (repetidas veces) | diccionario_general | - [ ] falta |
| 2740 | `LEXR-02608` | pasar a través (en plano) | diccionario_general | - [ ] falta |
| 2741 | `LEXR-03264` | pasar de un lado a otro, venir del otro lado | diccionario_general | - [ ] falta |
| 2742 | `LEXR-02435` | pasear | diccionario_general | - [ ] falta |
| 2743 | `LEXR-03486` | patear | diccionario_general | - [ ] falta |
| 2744 | `LEXR-02039` | patimocho | diccionario_general | - [ ] falta |
| 2745 | `LEXR-02700` | pavo del monte | diccionario_general | - [ ] falta |
| 2746 | `LEXR-00810` | pecar, caer en pecado | diccionario_general | - [ ] falta |
| 2747 | `LEXR-02858` | pecarí | diccionario_general | - [ ] falta |
| 2748 | `LEXR-03568` | pechanga, verbena (planta) | diccionario_general | - [ ] falta |
| 2749 | `LEXR-02325` | pedazo por pedazo | diccionario_general | - [ ] falta |
| 2750 | `LEXR-02125` | pedido | diccionario_general | - [ ] falta |
| 2751 | `LEXR-03440` | pedir | diccionario_general | - [ ] falta |
| 2752 | `LEXR-03034` | pedir fiado, dar fiado | diccionario_general | - [ ] falta |
| 2753 | `LEXR-03458` | pedir, preguntar | diccionario_general | - [ ] falta |
| 2754 | `LEXR-03857` | pegajoso | diccionario_general | - [ ] falta |
| 2755 | `LEXR-02725` | pegar (con la mano) | diccionario_general | - [ ] falta |
| 2756 | `LEXR-01281` | pegar con goma | diccionario_general | - [ ] falta |
| 2757 | `LEXR-00488` | peinilla | diccionario_general | - [ ] falta |
| 2758 | `LEXR-03366` | pelado, desnudo | diccionario_general | - [ ] falta |
| 2759 | `LEXR-02797` | pelar | diccionario_general | - [ ] falta |
| 2760 | `LEXR-01027` | pelar los dientes | diccionario_general | - [ ] falta |
| 2761 | `LEXR-01682` | peleador, pleitista | diccionario_general | - [ ] falta |
| 2762 | `LEXR-03907` | pelear | diccionario_general | - [ ] falta |
| 2763 | `LEXR-01812` | pelear (unos con otros) | diccionario_general | - [ ] falta |
| 2764 | `LEXR-01099` | pellizcar | diccionario_general | - [ ] falta |
| 2765 | `LEXR-00878` | pelo corto, pelón, motilón | diccionario_general | - [ ] falta |
| 2766 | `LEXR-01373` | pelusa de maíz | diccionario_general | - [ ] falta |
| 2767 | `LEXR-00583` | penca de cabuya | diccionario_general | - [ ] falta |
| 2768 | `LEXR-02124` | pender | diccionario_general | - [ ] falta |
| 2769 | `LEXR-02993` | pendiente | diccionario_general | - [ ] falta |
| 2770 | `LEXR-01909` | pendiente, inclinación del tejado | diccionario_general | - [ ] falta |
| 2771 | `LEXR-00868` | pene | diccionario_general | - [ ] falta |
| 2772 | `LEXR-01185` | pensamiento | diccionario_general | - [ ] falta |
| 2773 | `LEXR-02209` | pensar mal | diccionario_general | - [ ] falta |
| 2774 | `LEXR-03894` | pensar, creer, suponer | diccionario_general | - [ ] falta |
| 2775 | `LEXR-03676` | pequeño | diccionario_general | - [ ] falta |
| 2776 | `LEXR-01222` | perder | diccionario_general | - [ ] falta |
| 2777 | `LEXR-00909` | perder de vista | diccionario_general | - [ ] falta |
| 2778 | `LEXR-03299` | perder sabor | diccionario_general | - [ ] falta |
| 2779 | `LEXR-00601` | perdiz | diccionario_general | - [ ] falta |
| 2780 | `LEXR-03342` | perdonar | diccionario_general | - [ ] falta |
| 2781 | `LEXR-01313` | perdonarse | diccionario_general | - [ ] falta |
| 2782 | `LEXR-02078` | perezozo | diccionario_general | - [ ] falta |
| 2783 | `LEXR-02182` | perforar (varias cosas o en varias partes) | diccionario_general | - [ ] falta |
| 2784 | `LEXR-02203` | perico (ave) | diccionario_general | - [ ] falta |
| 2785 | `LEXR-00967` | perico plomo (aven nocturna, mal agüero) | diccionario_general | - [ ] falta |
| 2786 | `LEXR-00933` | periquillo | diccionario_general | - [ ] falta |
| 2787 | `LEXR-01389` | permanentamente | diccionario_general | - [ ] falta |
| 2788 | `LEXR-01152` | permitir amanecer | diccionario_general | - [ ] falta |
| 2789 | `LEXR-01200` | permitir asistir, mandar reunirse | diccionario_general | - [ ] falta |
| 2790 | `LEXR-01783` | permitir buscar, mandar buscar | diccionario_general | - [ ] falta |
| 2791 | `LEXR-02954` | permitir comer, dejar comer | diccionario_general | - [ ] falta |
| 2792 | `LEXR-03729` | permitir contestar | diccionario_general | - [ ] falta |
| 2793 | `LEXR-00484` | permitir destruir | diccionario_general | - [ ] falta |
| 2794 | `LEXR-03040` | permitir entrar y sentarse | diccionario_general | - [ ] falta |
| 2795 | `LEXR-01605` | permitir fermentar | diccionario_general | - [ ] falta |
| 2796 | `LEXR-03560` | permitir oír | diccionario_general | - [ ] falta |
| 2797 | `LEXR-02706` | permitir pasar el día | diccionario_general | - [ ] falta |
| 2798 | `LEXR-03223` | permitir tocar, partear | diccionario_general | - [ ] falta |
| 2799 | `LEXR-00951` | permitir vender | diccionario_general | - [ ] falta |
| 2800 | `LEXR-01062` | pero | diccionario_general | - [ ] falta |
| 2801 | `LEXR-02690` | perro | diccionario_general | - [ ] falta |
| 2802 | `LEXR-02081` | persona despreciado | diccionario_general | - [ ] falta |
| 2803 | `LEXR-01929` | persona que acompaña voluntariamente (al ir) | diccionario_general | - [ ] falta |
| 2804 | `LEXR-02116` | persona que acompaña voluntariamente (al venir) | diccionario_general | - [ ] falta |
| 2805 | `LEXR-01245` | persona que causa daño a otro | diccionario_general | - [ ] falta |
| 2806 | `LEXR-01957` | persona que da hospedaje, persona que pide hospedaje | diccionario_general | - [ ] falta |
| 2807 | `LEXR-00417` | persona que desea algo | diccionario_general | - [ ] falta |
| 2808 | `LEXR-03905` | persona que encarga algo | diccionario_general | - [ ] falta |
| 2809 | `LEXR-02876` | persona que está presente | diccionario_general | - [ ] falta |
| 2810 | `LEXR-02618` | persona que está, equivocada o desviada | diccionario_general | - [ ] falta |
| 2811 | `LEXR-01740` | persona que habla páez | diccionario_general | - [ ] falta |
| 2812 | `LEXR-02633` | persona que rie | diccionario_general | - [ ] falta |
| 2813 | `LEXR-01930` | persuadir | diccionario_general | - [ ] falta |
| 2814 | `LEXR-01064` | persuadir a otro quedarse, rogar se quede | diccionario_general | - [ ] falta |
| 2815 | `LEXR-03211` | persuadir, hablar con cariño | diccionario_general | - [ ] falta |
| 2816 | `LEXR-01047` | pesado | diccionario_general | - [ ] falta |
| 2817 | `LEXR-01951` | pescar | diccionario_general | - [x] `diccionario_general/pescar.png` |
| 2818 | `LEXR-03277` | pestaña, ceja | diccionario_general | - [ ] falta |
| 2819 | `LEXR-03093` | picadura | diccionario_general | - [ ] falta |
| 2820 | `LEXR-01179` | picante, amargo | diccionario_general | - [ ] falta |
| 2821 | `LEXR-01329` | picar, hacer pedazos, roer | diccionario_general | - [ ] falta |
| 2822 | `LEXR-01623` | pichón (ave) | diccionario_general | - [ ] falta |
| 2823 | `LEXR-03590` | Pijaos (tribu indígena) | diccionario_general | - [ ] falta |
| 2824 | `LEXR-02220` | pilado | diccionario_general | - [ ] falta |
| 2825 | `LEXR-03519` | pilar, cocer maíz para quitar la cáscara | diccionario_general | - [ ] falta |
| 2826 | `LEXR-03795` | pintado, teñido | diccionario_general | - [ ] falta |
| 2827 | `LEXR-03208` | pinto (blanco y negro) | diccionario_general | - [ ] falta |
| 2828 | `LEXR-02885` | pinto, moteado | diccionario_general | - [ ] falta |
| 2829 | `LEXR-03617` | pisar, pisotear | diccionario_general | - [ ] falta |
| 2830 | `LEXR-00466` | pisotear (repetidas veces) | diccionario_general | - [ ] falta |
| 2831 | `LEXR-01564` | pisotear, pisar | diccionario_general | - [ ] falta |
| 2832 | `LEXR-01976` | piña | diccionario_general | - [x] `diccionario_general/piña.png` |
| 2833 | `LEXR-00925` | planchudo | diccionario_general | - [ ] falta |
| 2834 | `LEXR-00819` | planta del pie, palma de la mano | diccionario_general | - [ ] falta |
| 2835 | `LEXR-03733` | plataforma en los sembrados | diccionario_general | - [ ] falta |
| 2836 | `LEXR-01612` | platanal | diccionario_general | - [ ] falta |
| 2837 | `LEXR-00858` | plato (de madera) | diccionario_general | - [ ] falta |
| 2838 | `LEXR-03481` | plegar | diccionario_general | - [ ] falta |
| 2839 | `LEXR-00726` | pleito | diccionario_general | - [ ] falta |
| 2840 | `LEXR-02593` | pluma (de pájaro) | diccionario_general | - [ ] falta |
| 2841 | `LEXR-03447` | pluma de gallina | diccionario_general | - [ ] falta |
| 2842 | `LEXR-01310` | plátano | diccionario_general | - [x] `diccionario_general/plátano.png` |
| 2843 | `LEXR-01809` | plátano maduro | diccionario_general | - [ ] falta |
| 2844 | `LEXR-01159` | pobre, desgraciado | diccionario_general | - [ ] falta |
| 2845 | `LEXR-03539` | pobre, pobrecito | diccionario_general | - [ ] falta |
| 2846 | `LEXR-03099` | poco | diccionario_general | - [ ] falta |
| 2847 | `LEXR-00927` | poco a poco, despacio | diccionario_general | - [ ] falta |
| 2848 | `LEXR-00998` | poco, poquito | diccionario_general | - [ ] falta |
| 2849 | `LEXR-02112` | pocos | diccionario_general | - [ ] falta |
| 2850 | `LEXR-00785` | poder | diccionario_general | - [ ] falta |
| 2851 | `LEXR-03280` | poder, completar, alcanzar, llegar el tiempo | diccionario_general | - [ ] falta |
| 2852 | `LEXR-02422` | poderoso | diccionario_general | - [ ] falta |
| 2853 | `LEXR-00574` | poderoso, capaz | diccionario_general | - [ ] falta |
| 2854 | `LEXR-00774` | podrido | diccionario_general | - [ ] falta |
| 2855 | `LEXR-01654` | podrir | diccionario_general | - [ ] falta |
| 2856 | `LEXR-01119` | podrirse | diccionario_general | - [ ] falta |
| 2857 | `LEXR-03708` | polvo de la casa | diccionario_general | - [ ] falta |
| 2858 | `LEXR-03735` | polvo de la tierra | diccionario_general | - [ ] falta |
| 2859 | `LEXR-01139` | ponedora (galiina que pone huevos), animal con cría | diccionario_general | - [ ] falta |
| 2860 | `LEXR-01248` | poner (repetidas veces cosas) | diccionario_general | - [ ] falta |
| 2861 | `LEXR-00751` | poner adelante, arrear | diccionario_general | - [ ] falta |
| 2862 | `LEXR-02757` | poner atravesado | diccionario_general | - [ ] falta |
| 2863 | `LEXR-02692` | poner encima de | diccionario_general | - [ ] falta |
| 2864 | `LEXR-02837` | poner encima de (cosa larga) | diccionario_general | - [ ] falta |
| 2865 | `LEXR-03103` | poner enjalma, (fig) engañar | diccionario_general | - [ ] falta |
| 2866 | `LEXR-00915` | poner inclinado | diccionario_general | - [ ] falta |
| 2867 | `LEXR-03237` | poner mano encima de | diccionario_general | - [ ] falta |
| 2868 | `LEXR-02801` | poner queja | diccionario_general | - [ ] falta |
| 2869 | `LEXR-03851` | poner sobre el hombro | diccionario_general | - [ ] falta |
| 2870 | `LEXR-01862` | poner sombrero | diccionario_general | - [ ] falta |
| 2871 | `LEXR-01325` | poner torcido, encorvar | diccionario_general | - [ ] falta |
| 2872 | `LEXR-00489` | poner vara a lo largo | diccionario_general | - [ ] falta |
| 2873 | `LEXR-02523` | poner, colocar | diccionario_general | - [ ] falta |
| 2874 | `LEXR-03750` | poner, colocar, edificar | diccionario_general | - [ ] falta |
| 2875 | `LEXR-01225` | ponerse amarillo | diccionario_general | - [ ] falta |
| 2876 | `LEXR-03023` | ponerse blando, ablandarse | diccionario_general | - [ ] falta |
| 2877 | `LEXR-00620` | ponerse caro | diccionario_general | - [ ] falta |
| 2878 | `LEXR-03865` | ponerse derecho, recto, empinarse | diccionario_general | - [ ] falta |
| 2879 | `LEXR-00919` | ponerse el sol | diccionario_general | - [ ] falta |
| 2880 | `LEXR-02236` | ponerse grave, empeorar | diccionario_general | - [ ] falta |
| 2881 | `LEXR-01535` | ponerse liso, resbaloso | diccionario_general | - [ ] falta |
| 2882 | `LEXR-01714` | ponerse obscuro | diccionario_general | - [ ] falta |
| 2883 | `LEXR-00782` | ponerse pesado | diccionario_general | - [ ] falta |
| 2884 | `LEXR-01590` | ponerse pálido | diccionario_general | - [ ] falta |
| 2885 | `LEXR-01939` | ponerse ronco | diccionario_general | - [ ] falta |
| 2886 | `LEXR-03233` | ponerse ruana | diccionario_general | - [ ] falta |
| 2887 | `LEXR-01882` | ponerse tupido | diccionario_general | - [ ] falta |
| 2888 | `LEXR-00581` | por | diccionario_general | - [ ] falta |
| 2889 | `LEXR-01776` | por acá | diccionario_general | - [ ] falta |
| 2890 | `LEXR-03451` | por allí | diccionario_general | - [ ] falta |
| 2891 | `LEXR-00503` | por allí (a través) | diccionario_general | - [ ] falta |
| 2892 | `LEXR-03316` | por consiguiente, así que | diccionario_general | - [ ] falta |
| 2893 | `LEXR-01209` | por esa misma razón | diccionario_general | - [ ] falta |
| 2894 | `LEXR-00718` | por eso | diccionario_general | - [ ] falta |
| 2895 | `LEXR-02656` | por eso, con el fin de que | diccionario_general | - [ ] falta |
| 2896 | `LEXR-02382` | por favor | diccionario_general | - [ ] falta |
| 2897 | `LEXR-00645` | por igual | diccionario_general | - [ ] falta |
| 2898 | `LEXR-02695` | por las calles | diccionario_general | - [ ] falta |
| 2899 | `LEXR-00627` | por sí mismo, uno mismo, propio | diccionario_general | - [ ] falta |
| 2900 | `LEXR-01861` | portarse mal | diccionario_general | - [ ] falta |
| 2901 | `LEXR-03090` | posada | diccionario_general | - [ ] falta |
| 2902 | `LEXR-01391` | postrero | diccionario_general | - [ ] falta |
| 2903 | `LEXR-02378` | potro, potranco | diccionario_general | - [ ] falta |
| 2904 | `LEXR-02812` | practicar brujería | diccionario_general | - [ ] falta |
| 2905 | `LEXR-03881` | preguntar, consultar a otro | diccionario_general | - [ ] falta |
| 2906 | `LEXR-01792` | prematuro | diccionario_general | - [ ] falta |
| 2907 | `LEXR-03558` | preocuparse | diccionario_general | - [ ] falta |
| 2908 | `LEXR-02205` | prestar ayuda | diccionario_general | - [ ] falta |
| 2909 | `LEXR-02760` | prestar, emprestar | diccionario_general | - [ ] falta |
| 2910 | `LEXR-00652` | preñada, enrazada (animales) | diccionario_general | - [ ] falta |
| 2911 | `LEXR-03747` | prima (respecto al primo) | diccionario_general | - [ ] falta |
| 2912 | `LEXR-02889` | primero, antes, anteriormente | diccionario_general | - [ ] falta |
| 2913 | `LEXR-03544` | primo (respecto a la prima) | diccionario_general | - [ ] falta |
| 2914 | `LEXR-02222` | primo con prima | diccionario_general | - [ ] falta |
| 2915 | `LEXR-01401` | primo con primo o prima con prima | diccionario_general | - [ ] falta |
| 2916 | `LEXR-02006` | primo, prima | diccionario_general | - [ ] falta |
| 2917 | `LEXR-02734` | probar (un alimento), sorber | diccionario_general | - [x] `diccionario_general/probar_(un_alimento),_sorber.png` |
| 2918 | `LEXR-03070` | probar (varias veces) | diccionario_general | - [ ] falta |
| 2919 | `LEXR-01669` | procurar, esforzarse, afanarse | diccionario_general | - [ ] falta |
| 2920 | `LEXR-03182` | producir | diccionario_general | - [ ] falta |
| 2921 | `LEXR-03651` | prole, cría | diccionario_general | - [x] `diccionario_general/prole,_cría.png` |
| 2922 | `LEXR-01973` | propiciar | diccionario_general | - [ ] falta |
| 2923 | `LEXR-00814` | propio de él | diccionario_general | - [ ] falta |
| 2924 | `LEXR-00406` | provocar, atacar, azuzar | diccionario_general | - [ ] falta |
| 2925 | `LEXR-01683` | puente arqueado | diccionario_general | - [x] `diccionario_general/puente_arqueado.png` |
| 2926 | `LEXR-03891` | puente de guadua | diccionario_general | - [x] `diccionario_general/puente_de_guadua.png` |
| 2927 | `LEXR-01758` | puente en forma de arco | diccionario_general | - [x] `diccionario_general/puente_en_forma_de_arco.png` |
| 2928 | `LEXR-01339` | puente techado | diccionario_general | - [x] `diccionario_general/puente_techado.png` |
| 2929 | `LEXR-02563` | pues | diccionario_general | - [ ] falta |
| 2930 | `LEXR-02763` | pulga | diccionario_general | - [x] `diccionario_general/pulga.png` |
| 2931 | `LEXR-03918` | puma, león | diccionario_general | - [x] `diccionario_general/puma,_león.png` |
| 2932 | `LEXR-00646` | punta de la lengua | diccionario_general | - [ ] falta |
| 2933 | `LEXR-03751` | purificarse | diccionario_general | - [ ] falta |
| 2934 | `LEXR-02748` | puñalarse | diccionario_general | - [ ] falta |
| 2935 | `LEXR-01336` | pájaro | diccionario_general | - [x] `diccionario_general/pájaro.png` |
| 2936 | `LEXR-03656` | pálido | diccionario_general | - [ ] falta |
| 2937 | `LEXR-02027` | párpado | diccionario_general | - [ ] falta |
| 2938 | `LEXR-01135` | que alumbra (por ejemplo, el sol) | diccionario_general | - [ ] falta |
| 2939 | `LEXR-02641` | que ataja | diccionario_general | - [ ] falta |
| 2940 | `LEXR-03543` | que avisa, que anuncia | diccionario_general | - [ ] falta |
| 2941 | `LEXR-01394` | que barre | diccionario_general | - [ ] falta |
| 2942 | `LEXR-01153` | que busca | diccionario_general | - [ ] falta |
| 2943 | `LEXR-00479` | que come, comensal | diccionario_general | - [ ] falta |
| 2944 | `LEXR-01872` | que contesta | diccionario_general | - [ ] falta |
| 2945 | `LEXR-01804` | que da paliza | diccionario_general | - [ ] falta |
| 2946 | `LEXR-00458` | que edifica | diccionario_general | - [ ] falta |
| 2947 | `LEXR-01258` | que entra | diccionario_general | - [ ] falta |
| 2948 | `LEXR-02020` | que ha nacido | diccionario_general | - [ ] falta |
| 2949 | `LEXR-01567` | que habla | diccionario_general | - [ ] falta |
| 2950 | `LEXR-03448` | que habla con desprecio | diccionario_general | - [ ] falta |
| 2951 | `LEXR-02260` | que hiere (a otro) | diccionario_general | - [ ] falta |
| 2952 | `LEXR-03036` | que insulta | diccionario_general | - [ ] falta |
| 2953 | `LEXR-00813` | que olvida | diccionario_general | - [ ] falta |
| 2954 | `LEXR-00821` | que pelea | diccionario_general | - [ ] falta |
| 2955 | `LEXR-00834` | que pide | diccionario_general | - [ ] falta |
| 2956 | `LEXR-02732` | que piensa, confía | diccionario_general | - [ ] falta |
| 2957 | `LEXR-01633` | que presenta queja, demanda | diccionario_general | - [ ] falta |
| 2958 | `LEXR-01472` | que regala | diccionario_general | - [ ] falta |
| 2959 | `LEXR-03608` | que sana | diccionario_general | - [ ] falta |
| 2960 | `LEXR-03698` | que tiene misericordia, que ama | diccionario_general | - [ ] falta |
| 2961 | `LEXR-01824` | que toma | diccionario_general | - [ ] falta |
| 2962 | `LEXR-02864` | que vende | diccionario_general | - [ ] falta |
| 2963 | `LEXR-01347` | que viene | diccionario_general | - [ ] falta |
| 2964 | `LEXR-02208` | que vive, ser viviendo | diccionario_general | - [ ] falta |
| 2965 | `LEXR-03754` | que,?qué? | diccionario_general | - [ ] falta |
| 2966 | `LEXR-00658` | quebrar (varias cosas) | diccionario_general | - [ ] falta |
| 2967 | `LEXR-03534` | quebrar (varios huesos) | diccionario_general | - [ ] falta |
| 2968 | `LEXR-03102` | quebrar, fracturar | diccionario_general | - [ ] falta |
| 2969 | `LEXR-03766` | quebrar, romper | diccionario_general | - [ ] falta |
| 2970 | `LEXR-00659` | quebrarse (varias cosas) | diccionario_general | - [ ] falta |
| 2971 | `LEXR-01764` | quedar complacido | diccionario_general | - [ ] falta |
| 2972 | `LEXR-01293` | quedar suspendido | diccionario_general | - [ ] falta |
| 2973 | `LEXR-01807` | quejarse (enfermo) | diccionario_general | - [ ] falta |
| 2974 | `LEXR-02865` | quejarse, gemir, pujar | diccionario_general | - [ ] falta |
| 2975 | `LEXR-00392` | quemar | diccionario_general | - [ ] falta |
| 2976 | `LEXR-00393` | quemar repetidas veces | diccionario_general | - [ ] falta |
| 2977 | `LEXR-03212` | querer, amar, gustar | diccionario_general | - [ ] falta |
| 2978 | `LEXR-01892` | querer, desear | diccionario_general | - [ ] falta |
| 2979 | `LEXR-01098` | querido | diccionario_general | - [ ] falta |
| 2980 | `LEXR-00843` | querido, apreciable | diccionario_general | - [ ] falta |
| 2981 | `LEXR-02960` | quiarse ruana | diccionario_general | - [ ] falta |
| 2982 | `LEXR-03256` | quiebramaíz | diccionario_general | - [ ] falta |
| 2983 | `LEXR-00727` | quien, ?quién? | diccionario_general | - [ ] falta |
| 2984 | `LEXR-03692` | quieto | diccionario_general | - [ ] falta |
| 2985 | `LEXR-03749` | quinto | diccionario_general | - [ ] falta |
| 2986 | `LEXR-01910` | quitar enjalma, (fig) desengañar | diccionario_general | - [ ] falta |
| 2987 | `LEXR-03912` | quitar sombrero | diccionario_general | - [ ] falta |
| 2988 | `LEXR-00626` | quitar varias cosas | diccionario_general | - [ ] falta |
| 2989 | `LEXR-01721` | quitar, despojar | diccionario_general | - [ ] falta |
| 2990 | `LEXR-02665` | quitar, despojar a otro | diccionario_general | - [ ] falta |
| 2991 | `LEXR-03293` | racimo de plátano | diccionario_general | - [ ] falta |
| 2992 | `LEXR-02711` | rajar, partir (con hacha) | diccionario_general | - [x] `diccionario_general/rajar,_partir_(con_hacha).png` |
| 2993 | `LEXR-01544` | rajarse (en varias partes) | diccionario_general | - [ ] falta |
| 2994 | `LEXR-02996` | rajarse, agrietarse | diccionario_general | - [ ] falta |
| 2995 | `LEXR-00656` | rajarse, partirse | diccionario_general | - [ ] falta |
| 2996 | `LEXR-00394` | ralo (tejido) | diccionario_general | - [ ] falta |
| 2997 | `LEXR-01187` | rama de arbusto | diccionario_general | - [ ] falta |
| 2998 | `LEXR-03453` | rama de árbol | diccionario_general | - [ ] falta |
| 2999 | `LEXR-03159` | rascar, dar raquiña, comezón | diccionario_general | - [ ] falta |
| 3000 | `LEXR-00643` | rasgar, romper (varias cosas) | diccionario_general | - [ ] falta |
| 3001 | `LEXR-02578` | rasguñar (repetidas veces) | diccionario_general | - [ ] falta |
| 3002 | `LEXR-00625` | rasguñar, arañar, coger con las uñas | diccionario_general | - [ ] falta |
| 3003 | `LEXR-02401` | raspar | diccionario_general | - [ ] falta |
| 3004 | `LEXR-00464` | rata | diccionario_general | - [ ] falta |
| 3005 | `LEXR-01261` | rata grande del monte (mamífero roedor) | diccionario_general | - [ ] falta |
| 3006 | `LEXR-00743` | ratón | diccionario_general | - [ ] falta |
| 3007 | `LEXR-01075` | raya | diccionario_general | - [ ] falta |
| 3008 | `LEXR-01527` | rayado | diccionario_general | - [ ] falta |
| 3009 | `LEXR-02826` | rayar, escribir con lápiz | diccionario_general | - [ ] falta |
| 3010 | `LEXR-00764` | rayo | diccionario_general | - [ ] falta |
| 3011 | `LEXR-03704` | raíz de cabuya | diccionario_general | - [ ] falta |
| 3012 | `LEXR-01000` | raíz de la lengua | diccionario_general | - [ ] falta |
| 3013 | `LEXR-01938` | raíz del diente | diccionario_general | - [ ] falta |
| 3014 | `LEXR-01999` | rebajar (precio) | diccionario_general | - [ ] falta |
| 3015 | `LEXR-00767` | rebosar | diccionario_general | - [ ] falta |
| 3016 | `LEXR-03513` | rechazar, burlar, despreciar | diccionario_general | - [ ] falta |
| 3017 | `LEXR-00756` | recibir fiado, endeudarse | diccionario_general | - [ ] falta |
| 3018 | `LEXR-01499` | reciente (ej. oficiales recientement elegidos) | diccionario_general | - [ ] falta |
| 3019 | `LEXR-00459` | reciente, hace poco | diccionario_general | - [ ] falta |
| 3020 | `LEXR-03278` | reclamar, protestar | diccionario_general | - [ ] falta |
| 3021 | `LEXR-00700` | reclinarse | diccionario_general | - [ ] falta |
| 3022 | `LEXR-01215` | recoger (granos) | diccionario_general | - [ ] falta |
| 3023 | `LEXR-02625` | recoger, cosechar | diccionario_general | - [ ] falta |
| 3024 | `LEXR-02195` | reconciliar | diccionario_general | - [ ] falta |
| 3025 | `LEXR-03069` | recordado | diccionario_general | - [ ] falta |
| 3026 | `LEXR-00674` | recordar | diccionario_general | - [ ] falta |
| 3027 | `LEXR-00856` | recostarse | diccionario_general | - [ ] falta |
| 3028 | `LEXR-01166` | recto, directo | diccionario_general | - [ ] falta |
| 3029 | `LEXR-03272` | red (para atrapar pájaros) | diccionario_general | - [ ] falta |
| 3030 | `LEXR-03199` | redondear | diccionario_general | - [ ] falta |
| 3031 | `LEXR-02110` | redondo | diccionario_general | - [ ] falta |
| 3032 | `LEXR-02968` | reemplazar, sustituir | diccionario_general | - [ ] falta |
| 3033 | `LEXR-02331` | reemplazo (en el cargo) | diccionario_general | - [ ] falta |
| 3034 | `LEXR-00591` | reflejar, centellear | diccionario_general | - [ ] falta |
| 3035 | `LEXR-02053` | regalado | diccionario_general | - [ ] falta |
| 3036 | `LEXR-02580` | regalar | diccionario_general | - [ ] falta |
| 3037 | `LEXR-03263` | regalar (varias veces or a varias personas) | diccionario_general | - [ ] falta |
| 3038 | `LEXR-03716` | regar (granos), esparcir, repartir | diccionario_general | - [ ] falta |
| 3039 | `LEXR-02348` | regar (líquido) | diccionario_general | - [ ] falta |
| 3040 | `LEXR-02629` | regar (repetidas veces) | diccionario_general | - [ ] falta |
| 3041 | `LEXR-03161` | regarse, desparramarse | diccionario_general | - [ ] falta |
| 3042 | `LEXR-01576` | regañar, censurar | diccionario_general | - [ ] falta |
| 3043 | `LEXR-01432` | regañar, reprender | diccionario_general | - [ ] falta |
| 3044 | `LEXR-01707` | regaño | diccionario_general | - [ ] falta |
| 3045 | `LEXR-02685` | regocijo, felicidad | diccionario_general | - [ ] falta |
| 3046 | `LEXR-02586` | regresar, volver | diccionario_general | - [ ] falta |
| 3047 | `LEXR-01608` | rehusar dar o gastar (repetidas veces) | diccionario_general | - [ ] falta |
| 3048 | `LEXR-02634` | reir | diccionario_general | - [x] `diccionario_general/reir.png` |
| 3049 | `LEXR-00828` | reir (repetidas veces) | diccionario_general | - [ ] falta |
| 3050 | `LEXR-03714` | reirse con los que se ríen | diccionario_general | - [ ] falta |
| 3051 | `LEXR-01540` | reirse de | diccionario_general | - [ ] falta |
| 3052 | `LEXR-01282` | relampaguear | diccionario_general | - [ ] falta |
| 3053 | `LEXR-00608` | relinchar | diccionario_general | - [ ] falta |
| 3054 | `LEXR-00522` | remendar | diccionario_general | - [ ] falta |
| 3055 | `LEXR-02868` | remover, suavizar | diccionario_general | - [ ] falta |
| 3056 | `LEXR-03822` | rencor, resentimiento | diccionario_general | - [ ] falta |
| 3057 | `LEXR-01545` | renovar | diccionario_general | - [ ] falta |
| 3058 | `LEXR-02684` | renuente, desinclinado | diccionario_general | - [ ] falta |
| 3059 | `LEXR-02719` | repartir | diccionario_general | - [ ] falta |
| 3060 | `LEXR-03667` | repartir (varias cosas entre varias personas) | diccionario_general | - [ ] falta |
| 3061 | `LEXR-03234` | repartir (varias cosas) | diccionario_general | - [ ] falta |
| 3062 | `LEXR-02454` | repartir, distribuir (varias cosas, o a varias personas) | diccionario_general | - [ ] falta |
| 3063 | `LEXR-02326` | repetidamente | diccionario_general | - [ ] falta |
| 3064 | `LEXR-03790` | repetir | diccionario_general | - [ ] falta |
| 3065 | `LEXR-03791` | repetir (varias veces) | diccionario_general | - [ ] falta |
| 3066 | `LEXR-00641` | resbalar | diccionario_general | - [ ] falta |
| 3067 | `LEXR-02396` | resbaloso | diccionario_general | - [ ] falta |
| 3068 | `LEXR-02090` | resfriarse | diccionario_general | - [ ] falta |
| 3069 | `LEXR-03218` | respiración | diccionario_general | - [ ] falta |
| 3070 | `LEXR-02413` | respirar, volver en sí | diccionario_general | - [ ] falta |
| 3071 | `LEXR-03329` | resplandecer | diccionario_general | - [ ] falta |
| 3072 | `LEXR-03279` | resplandor, fulgor | diccionario_general | - [ ] falta |
| 3073 | `LEXR-03468` | resucitar | diccionario_general | - [ ] falta |
| 3074 | `LEXR-02871` | retirarse, retroceder | diccionario_general | - [ ] falta |
| 3075 | `LEXR-02490` | retorcer | diccionario_general | - [ ] falta |
| 3076 | `LEXR-03097` | retorcer, menear la cabeza (en señal de disgusto) | diccionario_general | - [ ] falta |
| 3077 | `LEXR-03494` | retoñar, brotar | diccionario_general | - [ ] falta |
| 3078 | `LEXR-03381` | reumatismo articular (enfermedad de los huesos) | diccionario_general | - [ ] falta |
| 3079 | `LEXR-01818` | reunirse, congregarse | diccionario_general | - [ ] falta |
| 3080 | `LEXR-02216` | reunirse, juntarse | diccionario_general | - [ ] falta |
| 3081 | `LEXR-00525` | reunión | diccionario_general | - [ ] falta |
| 3082 | `LEXR-00861` | revelar, mostrar | diccionario_general | - [ ] falta |
| 3083 | `LEXR-03038` | revivir, resucitar | diccionario_general | - [ ] falta |
| 3084 | `LEXR-03732` | revolver, menear | diccionario_general | - [ ] falta |
| 3085 | `LEXR-03711` | rezar | diccionario_general | - [ ] falta |
| 3086 | `LEXR-03820` | rico | diccionario_general | - [ ] falta |
| 3087 | `LEXR-01632` | rincón de la casa | diccionario_general | - [ ] falta |
| 3088 | `LEXR-01244` | risueño | diccionario_general | - [ ] falta |
| 3089 | `LEXR-00818` | robado | diccionario_general | - [ ] falta |
| 3090 | `LEXR-01678` | robar | diccionario_general | - [ ] falta |
| 3091 | `LEXR-01937` | rociar | diccionario_general | - [ ] falta |
| 3092 | `LEXR-02436` | rodar, caer dando vueltas | diccionario_general | - [ ] falta |
| 3093 | `LEXR-02120` | rodar, revolcarse (varias veces) | diccionario_general | - [ ] falta |
| 3094 | `LEXR-01523` | rodear | diccionario_general | - [ ] falta |
| 3095 | `LEXR-03260` | rogar, suplicar | diccionario_general | - [ ] falta |
| 3096 | `LEXR-03846` | rojo claro | diccionario_general | - [ ] falta |
| 3097 | `LEXR-03510` | rollo | diccionario_general | - [ ] falta |
| 3098 | `LEXR-01820` | romper | diccionario_general | - [ ] falta |
| 3099 | `LEXR-03267` | romper, rasgar | diccionario_general | - [ ] falta |
| 3100 | `LEXR-02277` | romper, rasgar (una sola tira) | diccionario_general | - [ ] falta |
| 3101 | `LEXR-03268` | romperse (varias veces) | diccionario_general | - [ ] falta |
| 3102 | `LEXR-02180` | romperse, desgarrarse | diccionario_general | - [ ] falta |
| 3103 | `LEXR-02679` | roncar | diccionario_general | - [ ] falta |
| 3104 | `LEXR-00914` | ronco | diccionario_general | - [ ] falta |
| 3105 | `LEXR-02416` | rosado | diccionario_general | - [ ] falta |
| 3106 | `LEXR-03325` | roza de choclo | diccionario_general | - [ ] falta |
| 3107 | `LEXR-01566` | rozar | diccionario_general | - [ ] falta |
| 3108 | `LEXR-02822` | roñoso, áspero | diccionario_general | - [ ] falta |
| 3109 | `LEXR-01584` | ruana o anaco delgado | diccionario_general | - [ ] falta |
| 3110 | `LEXR-03555` | ruana o anaco grueso | diccionario_general | - [ ] falta |
| 3111 | `LEXR-00611` | rucio | diccionario_general | - [ ] falta |
| 3112 | `LEXR-00832` | ruido | diccionario_general | - [ ] falta |
| 3113 | `LEXR-03694` | rumbo a, hacia (recíproco) | diccionario_general | - [ ] falta |
| 3114 | `LEXR-00599` | rápidamenta | diccionario_general | - [ ] falta |
| 3115 | `LEXR-01131` | sabaleta | diccionario_general | - [ ] falta |
| 3116 | `LEXR-02694` | sacar (animales) | diccionario_general | - [ ] falta |
| 3117 | `LEXR-03408` | sacar (sin permiso, cosa ajena) | diccionario_general | - [ ] falta |
| 3118 | `LEXR-03205` | sacar líquido, servir comida | diccionario_general | - [ ] falta |
| 3119 | `LEXR-02275` | sacar muesca | diccionario_general | - [ ] falta |
| 3120 | `LEXR-03810` | sacristán | diccionario_general | - [ ] falta |
| 3121 | `LEXR-02063` | sacudir | diccionario_general | - [ ] falta |
| 3122 | `LEXR-01815` | sacudir (repetidas veces) | diccionario_general | - [ ] falta |
| 3123 | `LEXR-03201` | sacudirse | diccionario_general | - [ ] falta |
| 3124 | `LEXR-01302` | sal de Zipaquirá | diccionario_general | - [ ] falta |
| 3125 | `LEXR-03178` | salar, echar sal | diccionario_general | - [ ] falta |
| 3126 | `LEXR-03699` | salir el sol | diccionario_general | - [ ] falta |
| 3127 | `LEXR-03390` | salir mazorca | diccionario_general | - [ ] falta |
| 3128 | `LEXR-01895` | salir sobre | diccionario_general | - [ ] falta |
| 3129 | `LEXR-03126` | saludar (repetidas veces) | diccionario_general | - [ ] falta |
| 3130 | `LEXR-03083` | Salvar | diccionario_general | - [ ] falta |
| 3131 | `LEXR-03745` | salvia (planta medicinal) | diccionario_general | - [ ] falta |
| 3132 | `LEXR-01232` | sanar | diccionario_general | - [ ] falta |
| 3133 | `LEXR-03217` | sanarse | diccionario_general | - [ ] falta |
| 3134 | `LEXR-02687` | sangrar | diccionario_general | - [ ] falta |
| 3135 | `LEXR-01140` | sangre | diccionario_general | - [ ] falta |
| 3136 | `LEXR-02531` | savia | diccionario_general | - [ ] falta |
| 3137 | `LEXR-02229` | seca (infarto de una glándula) | diccionario_general | - [ ] falta |
| 3138 | `LEXR-02294` | secar | diccionario_general | - [ ] falta |
| 3139 | `LEXR-00559` | seco | diccionario_general | - [ ] falta |
| 3140 | `LEXR-01671` | secretamente, en secreto | diccionario_general | - [ ] falta |
| 3141 | `LEXR-02410` | sediento, que tiene sed | diccionario_general | - [ ] falta |
| 3142 | `LEXR-01288` | seguir | diccionario_general | - [ ] falta |
| 3143 | `LEXR-00971` | seguir rastro, oler | diccionario_general | - [ ] falta |
| 3144 | `LEXR-01887` | seguir, continuar haciendo algo | diccionario_general | - [ ] falta |
| 3145 | `LEXR-03717` | seis | diccionario_general | - [ ] falta |
| 3146 | `LEXR-02456` | sembrado | diccionario_general | - [ ] falta |
| 3147 | `LEXR-01482` | sembrado de maní | diccionario_general | - [ ] falta |
| 3148 | `LEXR-01423` | sembrador, que siembra | diccionario_general | - [ ] falta |
| 3149 | `LEXR-02720` | sembrar | diccionario_general | - [ ] falta |
| 3150 | `LEXR-01627` | sembrar (diversas semillas) | diccionario_general | - [ ] falta |
| 3151 | `LEXR-02672` | sentarse | diccionario_general | - [ ] falta |
| 3152 | `LEXR-01533` | sentir ’señas’, adivinar por sensaciones en el cuerpo | diccionario_general | - [ ] falta |
| 3153 | `LEXR-03652` | sentir (cuando otro la toca) | diccionario_general | - [ ] falta |
| 3154 | `LEXR-02245` | sentir calor, acalorarse | diccionario_general | - [ ] falta |
| 3155 | `LEXR-02246` | sentir cosquillas | diccionario_general | - [ ] falta |
| 3156 | `LEXR-01270` | sentir dolor | diccionario_general | - [ ] falta |
| 3157 | `LEXR-02458` | sentir frío | diccionario_general | - [ ] falta |
| 3158 | `LEXR-03238` | sentir pesar | diccionario_general | - [ ] falta |
| 3159 | `LEXR-02699` | sentir una sensacíon extraña | diccionario_general | - [ ] falta |
| 3160 | `LEXR-02080` | sentirse bien, estar alentado | diccionario_general | - [ ] falta |
| 3161 | `LEXR-03594` | sentirse incapaz | diccionario_general | - [ ] falta |
| 3162 | `LEXR-01333` | separar, repartir, dividir, apartar | diccionario_general | - [ ] falta |
| 3163 | `LEXR-03244` | separarse (varias cosas, o varias personas) | diccionario_general | - [ ] falta |
| 3164 | `LEXR-00461` | separarse, alejarse, apartarse | diccionario_general | - [ ] falta |
| 3165 | `LEXR-01240` | sepulcro, fosa pars entierro | diccionario_general | - [ ] falta |
| 3166 | `LEXR-02626` | sepultado | diccionario_general | - [ ] falta |
| 3167 | `LEXR-01346` | ser | diccionario_general | - [ ] falta |
| 3168 | `LEXR-00471` | ser agredido | diccionario_general | - [ ] falta |
| 3169 | `LEXR-00606` | ser amado, quererse recíprocamente | diccionario_general | - [ ] falta |
| 3170 | `LEXR-03024` | ser amigos, tener amistad | diccionario_general | - [ ] falta |
| 3171 | `LEXR-02244` | ser bautizado | diccionario_general | - [ ] falta |
| 3172 | `LEXR-01341` | ser burlado | diccionario_general | - [ ] falta |
| 3173 | `LEXR-03214` | ser castigado | diccionario_general | - [ ] falta |
| 3174 | `LEXR-03017` | ser condenado | diccionario_general | - [ ] falta |
| 3175 | `LEXR-02904` | ser dejado, quedarse involuntariamente | diccionario_general | - [ ] falta |
| 3176 | `LEXR-01893` | ser despreciado | diccionario_general | - [ ] falta |
| 3177 | `LEXR-01223` | ser esquivo, esquivar | diccionario_general | - [ ] falta |
| 3178 | `LEXR-02026` | ser lavado | diccionario_general | - [ ] falta |
| 3179 | `LEXR-02791` | ser madrina | diccionario_general | - [ ] falta |
| 3180 | `LEXR-00450` | ser mezquino | diccionario_general | - [ ] falta |
| 3181 | `LEXR-01571` | ser nombrado | diccionario_general | - [ ] falta |
| 3182 | `LEXR-02002` | ser olvidadizo | diccionario_general | - [ ] falta |
| 3183 | `LEXR-00693` | ser padrinos (de matrimonio) | diccionario_general | - [ ] falta |
| 3184 | `LEXR-00710` | ser quitado, dejarse quitar | diccionario_general | - [ ] falta |
| 3185 | `LEXR-02698` | ser salvo | diccionario_general | - [ ] falta |
| 3186 | `LEXR-02140` | ser sobrenatural | diccionario_general | - [ ] falta |
| 3187 | `LEXR-01771` | ser, llegar a ser | diccionario_general | - [ ] falta |
| 3188 | `LEXR-01265` | serranía | diccionario_general | - [ ] falta |
| 3189 | `LEXR-01144` | servible, usado (de segunda mano) | diccionario_general | - [ ] falta |
| 3190 | `LEXR-03613` | servir, ser útil | diccionario_general | - [ ] falta |
| 3191 | `LEXR-02224` | servirse (mutuamente) | diccionario_general | - [ ] falta |
| 3192 | `LEXR-02786` | severamente | diccionario_general | - [ ] falta |
| 3193 | `LEXR-03477` | severo, temible | diccionario_general | - [ ] falta |
| 3194 | `LEXR-01239` | siempre, realmente (con seguridad) | diccionario_general | - [ ] falta |
| 3195 | `LEXR-01881` | siete | diccionario_general | - [ ] falta |
| 3196 | `LEXR-01727` | silbar | diccionario_general | - [ ] falta |
| 3197 | `LEXR-02266` | silbar (repetidas veces) | diccionario_general | - [ ] falta |
| 3198 | `LEXR-00539` | simple, soso | diccionario_general | - [ ] falta |
| 3199 | `LEXR-02273` | sin embargo | diccionario_general | - [ ] falta |
| 3200 | `LEXR-01354` | sin miedo | diccionario_general | - [ ] falta |
| 3201 | `LEXR-03922` | sitio anterior de la casa | diccionario_general | - [ ] falta |
| 3202 | `LEXR-02827` | sobar, acarciciar (varias veces) | diccionario_general | - [ ] falta |
| 3203 | `LEXR-03062` | sobar, componer un hueso dislocado | diccionario_general | - [ ] falta |
| 3204 | `LEXR-01746` | sobra | diccionario_general | - [ ] falta |
| 3205 | `LEXR-02441` | sobra, sobrante | diccionario_general | - [ ] falta |
| 3206 | `LEXR-00734` | sobrar | diccionario_general | - [ ] falta |
| 3207 | `LEXR-00724` | sobrino o sobrina con el tío | diccionario_general | - [ ] falta |
| 3208 | `LEXR-03362` | sobrino o sobrina con tía | diccionario_general | - [ ] falta |
| 3209 | `LEXR-03592` | soledad | diccionario_general | - [ ] falta |
| 3210 | `LEXR-01932` | soledad (ave) | diccionario_general | - [ ] falta |
| 3211 | `LEXR-03435` | sollozar | diccionario_general | - [ ] falta |
| 3212 | `LEXR-03393` | soltar, desatar | diccionario_general | - [ ] falta |
| 3213 | `LEXR-01066` | soltera | diccionario_general | - [ ] falta |
| 3214 | `LEXR-02854` | soltero | diccionario_general | - [ ] falta |
| 3215 | `LEXR-02423` | sombrero de hoja de caña | diccionario_general | - [ ] falta |
| 3216 | `LEXR-03876` | sombrero de ramos | diccionario_general | - [ ] falta |
| 3217 | `LEXR-03270` | sonar | diccionario_general | - [ ] falta |
| 3218 | `LEXR-02227` | sonar (ruido de cascabel) | diccionario_general | - [ ] falta |
| 3219 | `LEXR-02632` | sonar, hacer ruido (maraca) | diccionario_general | - [ ] falta |
| 3220 | `LEXR-02716` | sonarse las narices | diccionario_general | - [ ] falta |
| 3221 | `LEXR-01775` | sonreir | diccionario_general | - [x] `diccionario_general/sonreir.png` |
| 3222 | `LEXR-01440` | sonrojarse | diccionario_general | - [ ] falta |
| 3223 | `LEXR-01181` | sonsacar | diccionario_general | - [ ] falta |
| 3224 | `LEXR-02493` | soplar | diccionario_general | - [ ] falta |
| 3225 | `LEXR-02276` | soplar (repetidas veces) | diccionario_general | - [ ] falta |
| 3226 | `LEXR-03420` | soplar la candela | diccionario_general | - [ ] falta |
| 3227 | `LEXR-03031` | sordo | diccionario_general | - [ ] falta |
| 3228 | `LEXR-01766` | sorpresivamente, súbitamente | diccionario_general | - [ ] falta |
| 3229 | `LEXR-00400` | soñar | diccionario_general | - [ ] falta |
| 3230 | `LEXR-01791` | su | diccionario_general | - [ ] falta |
| 3231 | `LEXR-00462` | su (de ellos, de ellas) | diccionario_general | - [ ] falta |
| 3232 | `LEXR-01257` | su (de él, de ella) | diccionario_general | - [ ] falta |
| 3233 | `LEXR-00792` | subir | diccionario_general | - [x] `diccionario_general/subir.png` |
| 3234 | `LEXR-01744` | subir (ej. ladrillos) | diccionario_general | - [ ] falta |
| 3235 | `LEXR-01488` | subir, ascender, trepar | diccionario_general | - [ ] falta |
| 3236 | `LEXR-03906` | suegro o suegra con el yerno | diccionario_general | - [ ] falta |
| 3237 | `LEXR-01006` | suelto | diccionario_general | - [ ] falta |
| 3238 | `LEXR-01377` | sueño | diccionario_general | - [ ] falta |
| 3239 | `LEXR-03578` | suficiente, complete | diccionario_general | - [ ] falta |
| 3240 | `LEXR-01034` | sufir castigo | diccionario_general | - [ ] falta |
| 3241 | `LEXR-03295` | sufrir | diccionario_general | - [ ] falta |
| 3242 | `LEXR-03425` | sufrir dolor | diccionario_general | - [ ] falta |
| 3243 | `LEXR-00934` | suicidarse | diccionario_general | - [ ] falta |
| 3244 | `LEXR-01622` | supurar | diccionario_general | - [ ] falta |
| 3245 | `LEXR-03162` | suspirar | diccionario_general | - [ ] falta |
| 3246 | `LEXR-01457` | suyo | diccionario_general | - [ ] falta |
| 3247 | `LEXR-02730` | tabaco (planta) | diccionario_general | - [ ] falta |
| 3248 | `LEXR-02131` | tabla | diccionario_general | - [ ] falta |
| 3249 | `LEXR-02451` | tamal de choclo | diccionario_general | - [ ] falta |
| 3250 | `LEXR-03348` | tamaño, dimensión de altura, anchura, profundidad | diccionario_general | - [ ] falta |
| 3251 | `LEXR-01494` | tambalear | diccionario_general | - [ ] falta |
| 3252 | `LEXR-02183` | tambalearse | diccionario_general | - [ ] falta |
| 3253 | `LEXR-02979` | también | diccionario_general | - [ ] falta |
| 3254 | `LEXR-01230` | tan, tanto (de este tamaño o cantidad) | diccionario_general | - [ ] falta |
| 3255 | `LEXR-03836` | tantos | diccionario_general | - [ ] falta |
| 3256 | `LEXR-02187` | taparse | diccionario_general | - [ ] falta |
| 3257 | `LEXR-03814` | taparse el rostro | diccionario_general | - [ ] falta |
| 3258 | `LEXR-03625` | tarro de guadua | diccionario_general | - [ ] falta |
| 3259 | `LEXR-02509` | tasajear (carne) | diccionario_general | - [ ] falta |
| 3260 | `LEXR-01697` | techo de la casa | diccionario_general | - [ ] falta |
| 3261 | `LEXR-02345` | tejedor, que teje | diccionario_general | - [ ] falta |
| 3262 | `LEXR-00561` | tejido | diccionario_general | - [ ] falta |
| 3263 | `LEXR-03875` | tejido trenzado | diccionario_general | - [ ] falta |
| 3264 | `LEXR-02894` | telar para tejer chumbe | diccionario_general | - [ ] falta |
| 3265 | `LEXR-02150` | telar para tejer ruana | diccionario_general | - [ ] falta |
| 3266 | `LEXR-01019` | temblar (de miedo, o del frío) | diccionario_general | - [ ] falta |
| 3267 | `LEXR-02969` | temblar (movimiento telúrico) | diccionario_general | - [ ] falta |
| 3268 | `LEXR-00673` | temer, tener miedo, asustarse | diccionario_general | - [ ] falta |
| 3269 | `LEXR-01436` | temible | diccionario_general | - [ ] falta |
| 3270 | `LEXR-03415` | templar | diccionario_general | - [ ] falta |
| 3271 | `LEXR-01941` | templar (varias cuerdas) | diccionario_general | - [ ] falta |
| 3272 | `LEXR-01839` | temprano | diccionario_general | - [ ] falta |
| 3273 | `LEXR-03487` | tender | diccionario_general | - [ ] falta |
| 3274 | `LEXR-00530` | tender, extender | diccionario_general | - [ ] falta |
| 3275 | `LEXR-01752` | tendido, sudadero | diccionario_general | - [ ] falta |
| 3276 | `LEXR-03257` | tendón de la mano | diccionario_general | - [ ] falta |
| 3277 | `LEXR-01039` | tendón de la pie | diccionario_general | - [ ] falta |
| 3278 | `LEXR-01182` | tener ’sensaciones’ en el cuerpo | diccionario_general | - [ ] falta |
| 3279 | `LEXR-01160` | tener celos (entre esposos) | diccionario_general | - [ ] falta |
| 3280 | `LEXR-00793` | tener celos, estar celoso | diccionario_general | - [ ] falta |
| 3281 | `LEXR-00513` | tener cuidado | diccionario_general | - [ ] falta |
| 3282 | `LEXR-01091` | tener dificultades | diccionario_general | - [ ] falta |
| 3283 | `LEXR-03213` | tener hambre | diccionario_general | - [ ] falta |
| 3284 | `LEXR-01987` | tener hipo | diccionario_general | - [ ] falta |
| 3285 | `LEXR-03697` | tener miedo | diccionario_general | - [ ] falta |
| 3286 | `LEXR-02643` | tener sed | diccionario_general | - [ ] falta |
| 3287 | `LEXR-03416` | tener sesaciones (sentir ’señas’) | diccionario_general | - [ ] falta |
| 3288 | `LEXR-00963` | tener sueño | diccionario_general | - [ ] falta |
| 3289 | `LEXR-03805` | tener vergüenza | diccionario_general | - [ ] falta |
| 3290 | `LEXR-01991` | tener, poseer, contener | diccionario_general | - [ ] falta |
| 3291 | `LEXR-02677` | tercero | diccionario_general | - [ ] falta |
| 3292 | `LEXR-00514` | terciado | diccionario_general | - [ ] falta |
| 3293 | `LEXR-01458` | terciar, llevar terciado | diccionario_general | - [ ] falta |
| 3294 | `LEXR-01276` | terminar (poner fin a un asunto o a una reunión) | diccionario_general | - [ ] falta |
| 3295 | `LEXR-01574` | terminar un asunto | diccionario_general | - [ ] falta |
| 3296 | `LEXR-02890` | terrible, horrible | diccionario_general | - [ ] falta |
| 3297 | `LEXR-03318` | terrón | diccionario_general | - [ ] falta |
| 3298 | `LEXR-03831` | teñir de negro | diccionario_general | - [ ] falta |
| 3299 | `LEXR-00748` | tibia | diccionario_general | - [ ] falta |
| 3300 | `LEXR-01919` | tiempos anteriores | diccionario_general | - [ ] falta |
| 3301 | `LEXR-02196` | tierno, recíen nacido | diccionario_general | - [ ] falta |
| 3302 | `LEXR-01190` | tierra caliente | diccionario_general | - [ ] falta |
| 3303 | `LEXR-03048` | tierra fría | diccionario_general | - [ ] falta |
| 3304 | `LEXR-03587` | tierra lejana | diccionario_general | - [ ] falta |
| 3305 | `LEXR-01829` | tieso | diccionario_general | - [ ] falta |
| 3306 | `LEXR-01561` | tigrillo | diccionario_general | - [ ] falta |
| 3307 | `LEXR-02288` | tijereta | diccionario_general | - [ ] falta |
| 3308 | `LEXR-00624` | timidez | diccionario_general | - [ ] falta |
| 3309 | `LEXR-00864` | tirante (pieza de la armadura del tejado) | diccionario_general | - [ ] falta |
| 3310 | `LEXR-03140` | tocar (con la mano), palpar | diccionario_general | - [ ] falta |
| 3311 | `LEXR-02504` | tocar (la puerta) | diccionario_general | - [ ] falta |
| 3312 | `LEXR-00707` | tocar (repetidas veces) | diccionario_general | - [ ] falta |
| 3313 | `LEXR-03526` | tocar (un instrumento musical) | diccionario_general | - [ ] falta |
| 3314 | `LEXR-01208` | tocar flauta | diccionario_general | - [ ] falta |
| 3315 | `LEXR-00499` | tocar repetidas veces con algo | diccionario_general | - [ ] falta |
| 3316 | `LEXR-02021` | tocar, echar mano | diccionario_general | - [ ] falta |
| 3317 | `LEXR-03364` | toda la noche | diccionario_general | - [ ] falta |
| 3318 | `LEXR-03606` | todavía | diccionario_general | - [ ] falta |
| 3319 | `LEXR-03284` | todavía obscuro (en la madrugada) | diccionario_general | - [ ] falta |
| 3320 | `LEXR-00799` | todo | diccionario_general | - [ ] falta |
| 3321 | `LEXR-01296` | todos | diccionario_general | - [ ] falta |
| 3322 | `LEXR-01613` | tomar preso, aprisionar | diccionario_general | - [ ] falta |
| 3323 | `LEXR-00695` | torcaz | diccionario_general | - [ ] falta |
| 3324 | `LEXR-01883` | torcaz (ave) | diccionario_general | - [ ] falta |
| 3325 | `LEXR-00665` | torcaz del monte (ave) | diccionario_general | - [ ] falta |
| 3326 | `LEXR-00453` | torcaz domesticado | diccionario_general | - [ ] falta |
| 3327 | `LEXR-00494` | torcaz pequeña (ave) | diccionario_general | - [ ] falta |
| 3328 | `LEXR-00473` | torcaz silvestre | diccionario_general | - [ ] falta |
| 3329 | `LEXR-02073` | torcer | diccionario_general | - [ ] falta |
| 3330 | `LEXR-00542` | torcer (hilo o guasca) | diccionario_general | - [ ] falta |
| 3331 | `LEXR-00550` | torcer, retorcer | diccionario_general | - [ ] falta |
| 3332 | `LEXR-02233` | torcerse, encorvarse | diccionario_general | - [ ] falta |
| 3333 | `LEXR-03242` | torcido | diccionario_general | - [ ] falta |
| 3334 | `LEXR-02819` | tormenta, tempestad | diccionario_general | - [ ] falta |
| 3335 | `LEXR-03591` | toser | diccionario_general | - [ ] falta |
| 3336 | `LEXR-01078` | toser (repetidas veces) | diccionario_general | - [ ] falta |
| 3337 | `LEXR-02114` | trabajar | diccionario_general | - [ ] falta |
| 3338 | `LEXR-03055` | traer | diccionario_general | - [ ] falta |
| 3339 | `LEXR-00894` | traer (a través) | diccionario_general | - [ ] falta |
| 3340 | `LEXR-03609` | traer (desde abajo) | diccionario_general | - [ ] falta |
| 3341 | `LEXR-03626` | traer (desde arriba), bajar (ej. a un enfermo) | diccionario_general | - [ ] falta |
| 3342 | `LEXR-01069` | traer (desde arriba, en plano) | diccionario_general | - [ ] falta |
| 3343 | `LEXR-00619` | traer (llegando a un lugar) | diccionario_general | - [ ] falta |
| 3344 | `LEXR-01539` | traer, cargar | diccionario_general | - [ ] falta |
| 3345 | `LEXR-03179` | traer, hacer llegar | diccionario_general | - [ ] falta |
| 3346 | `LEXR-03141` | tragar | diccionario_general | - [ ] falta |
| 3347 | `LEXR-01072` | trama, hilo horizontal del telar | diccionario_general | - [ ] falta |
| 3348 | `LEXR-02777` | tranca | diccionario_general | - [ ] falta |
| 3349 | `LEXR-03500` | transnochar | diccionario_general | - [ ] falta |
| 3350 | `LEXR-02181` | transparente, claro | diccionario_general | - [ ] falta |
| 3351 | `LEXR-02046` | trapiche movido por bestia | diccionario_general | - [ ] falta |
| 3352 | `LEXR-00526` | trasladar, transtear | diccionario_general | - [ ] falta |
| 3353 | `LEXR-02274` | trastear, mudarse | diccionario_general | - [ ] falta |
| 3354 | `LEXR-01732` | tratar con severidad | diccionario_general | - [ ] falta |
| 3355 | `LEXR-01927` | tratarse como parientes | diccionario_general | - [ ] falta |
| 3356 | `LEXR-00584` | trenza | diccionario_general | - [ ] falta |
| 3357 | `LEXR-00551` | trenzar | diccionario_general | - [ ] falta |
| 3358 | `LEXR-00546` | tres | diccionario_general | - [ ] falta |
| 3359 | `LEXR-01705` | triste | diccionario_general | - [ ] falta |
| 3360 | `LEXR-01784` | tronar | diccionario_general | - [ ] falta |
| 3361 | `LEXR-02597` | tropezar | diccionario_general | - [ ] falta |
| 3362 | `LEXR-03434` | tu (niña o pariente fememina) | diccionario_general | - [ ] falta |
| 3363 | `LEXR-03454` | tu, su, de usted | diccionario_general | - [ ] falta |
| 3364 | `LEXR-00703` | tu, su, de usted (masculino) | diccionario_general | - [ ] falta |
| 3365 | `LEXR-03401` | tusa de maíz | diccionario_general | - [ ] falta |
| 3366 | `LEXR-03522` | tusilla (planta) | diccionario_general | - [ ] falta |
| 3367 | `LEXR-01291` | tábano | diccionario_general | - [ ] falta |
| 3368 | `LEXR-00795` | tábano (insecto) | diccionario_general | - [ ] falta |
| 3369 | `LEXR-00440` | tía (hermana de la mamá) | diccionario_general | - [ ] falta |
| 3370 | `LEXR-01933` | tía con sobrino o sobrina | diccionario_general | - [ ] falta |
| 3371 | `LEXR-01469` | tímido, temeroso, miedoso | diccionario_general | - [ ] falta |
| 3372 | `LEXR-02785` | tú (niña o pariente femenina) | diccionario_general | - [ ] falta |
| 3373 | `LEXR-01915` | tú, usted (masculino) | diccionario_general | - [ ] falta |
| 3374 | `LEXR-00920` | ulluco | diccionario_general | - [ ] falta |
| 3375 | `LEXR-03518` | ultrajar | diccionario_general | - [ ] falta |
| 3376 | `LEXR-02118` | ultraje | diccionario_general | - [ ] falta |
| 3377 | `LEXR-03838` | un ratico | diccionario_general | - [ ] falta |
| 3378 | `LEXR-02489` | un rato | diccionario_general | - [ ] falta |
| 3379 | `LEXR-00547` | una brazada | diccionario_general | - [ ] falta |
| 3380 | `LEXR-03021` | una persona vestida | diccionario_general | - [ ] falta |
| 3381 | `LEXR-00501` | unidos | diccionario_general | - [ ] falta |
| 3382 | `LEXR-01498` | unir | diccionario_general | - [ ] falta |
| 3383 | `LEXR-02965` | unirse, juntarse con | diccionario_general | - [ ] falta |
| 3384 | `LEXR-01416` | uno | diccionario_general | - [ ] falta |
| 3385 | `LEXR-02235` | uno por uno | diccionario_general | - [ ] falta |
| 3386 | `LEXR-03247` | uno tras otro | diccionario_general | - [ ] falta |
| 3387 | `LEXR-02663` | unos cuantos | diccionario_general | - [ ] falta |
| 3388 | `LEXR-01059` | unos pocos, unos cuantos | diccionario_general | - [ ] falta |
| 3389 | `LEXR-03412` | urdir, preparar los hilos de la urdimbre | diccionario_general | - [ ] falta |
| 3390 | `LEXR-00982` | urdirmbre (hilos verticales del telar) | diccionario_general | - [ ] falta |
| 3391 | `LEXR-03512` | urraca | diccionario_general | - [ ] falta |
| 3392 | `LEXR-01007` | urraca (ave) | diccionario_general | - [ ] falta |
| 3393 | `LEXR-02437` | usado, viejo | diccionario_general | - [ ] falta |
| 3394 | `LEXR-02213` | usado, viejo, remendado | diccionario_general | - [ ] falta |
| 3395 | `LEXR-02375` | ustedes | diccionario_general | - [ ] falta |
| 3396 | `LEXR-03748` | uvillo | diccionario_general | - [ ] falta |
| 3397 | `LEXR-02040` | vaca | diccionario_general | - [ ] falta |
| 3398 | `LEXR-02750` | vaciar | diccionario_general | - [ ] falta |
| 3399 | `LEXR-02314` | vaciar (granos) | diccionario_general | - [ ] falta |
| 3400 | `LEXR-03456` | vaciar (líquido) | diccionario_general | - [ ] falta |
| 3401 | `LEXR-03532` | valiente | diccionario_general | - [ ] falta |
| 3402 | `LEXR-02605` | vara larga | diccionario_general | - [ ] falta |
| 3403 | `LEXR-02034` | varicela, viruela loca | diccionario_general | - [ ] falta |
| 3404 | `LEXR-02262` | varios, bastante | diccionario_general | - [ ] falta |
| 3405 | `LEXR-01970` | vela | diccionario_general | - [ ] falta |
| 3406 | `LEXR-00411` | vena | diccionario_general | - [ ] falta |
| 3407 | `LEXR-02973` | vena de la nuca | diccionario_general | - [ ] falta |
| 3408 | `LEXR-00773` | venado | diccionario_general | - [x] `diccionario_general/venado.png` |
| 3409 | `LEXR-00739` | vender | diccionario_general | - [ ] falta |
| 3410 | `LEXR-03764` | vendido | diccionario_general | - [ ] falta |
| 3411 | `LEXR-02907` | venida | diccionario_general | - [ ] falta |
| 3412 | `LEXR-01497` | venir | diccionario_general | - [ ] falta |
| 3413 | `LEXR-03746` | venir acompañado a otro voluntariamente | diccionario_general | - [ ] falta |
| 3414 | `LEXR-03794` | ventear | diccionario_general | - [ ] falta |
| 3415 | `LEXR-02645` | ver visiones | diccionario_general | - [ ] falta |
| 3416 | `LEXR-02352` | verdaderamente | diccionario_general | - [ ] falta |
| 3417 | `LEXR-00438` | verdugo | diccionario_general | - [ ] falta |
| 3418 | `LEXR-00615` | vereda | diccionario_general | - [ ] falta |
| 3419 | `LEXR-01323` | vereda de Mariposas | diccionario_general | - [x] `diccionario_general/vereda_de_mariposas.png` |
| 3420 | `LEXR-01673` | vergonzoso | diccionario_general | - [ ] falta |
| 3421 | `LEXR-00999` | vergüenza | diccionario_general | - [ ] falta |
| 3422 | `LEXR-02067` | verter | diccionario_general | - [ ] falta |
| 3423 | `LEXR-01481` | vertical | diccionario_general | - [ ] falta |
| 3424 | `LEXR-01581` | vestido | diccionario_general | - [ ] falta |
| 3425 | `LEXR-01278` | vestido sin costura | diccionario_general | - [ ] falta |
| 3426 | `LEXR-02363` | vestir (a otro) | diccionario_general | - [ ] falta |
| 3427 | `LEXR-01221` | vestirse (dícese de la mujer) | diccionario_general | - [ ] falta |
| 3428 | `LEXR-01828` | vez | diccionario_general | - [ ] falta |
| 3429 | `LEXR-02119` | viajarm andar de una parte a otra | diccionario_general | - [ ] falta |
| 3430 | `LEXR-02606` | viche, no maduro | diccionario_general | - [ ] falta |
| 3431 | `LEXR-02054` | vieja, anciana | diccionario_general | - [ ] falta |
| 3432 | `LEXR-03888` | viejo (referiendo a hombre, o a cosa) | diccionario_general | - [ ] falta |
| 3433 | `LEXR-02515` | viruela | diccionario_general | - [ ] falta |
| 3434 | `LEXR-03813` | visible | diccionario_general | - [ ] falta |
| 3435 | `LEXR-02240` | visitar | diccionario_general | - [ ] falta |
| 3436 | `LEXR-02189` | vistazo oblícuo | diccionario_general | - [ ] falta |
| 3437 | `LEXR-03827` | vivir | diccionario_general | - [ ] falta |
| 3438 | `LEXR-01505` | vivir, estar vivo | diccionario_general | - [ ] falta |
| 3439 | `LEXR-00507` | vivir, pasar el día | diccionario_general | - [ ] falta |
| 3440 | `LEXR-01434` | vivo, viviente | diccionario_general | - [ ] falta |
| 3441 | `LEXR-00713` | volar | diccionario_general | - [x] `diccionario_general/volar.png` |
| 3442 | `LEXR-03428` | volteado (boca arriba) | diccionario_general | - [ ] falta |
| 3443 | `LEXR-00738` | voltear | diccionario_general | - [ ] falta |
| 3444 | `LEXR-00421` | voltear para abajo | diccionario_general | - [ ] falta |
| 3445 | `LEXR-01420` | voltearse, volver | diccionario_general | - [ ] falta |
| 3446 | `LEXR-01563` | voluntariamente, de buena gana | diccionario_general | - [ ] falta |
| 3447 | `LEXR-01342` | volverse agua | diccionario_general | - [ ] falta |
| 3448 | `LEXR-03545` | volverse mezquino | diccionario_general | - [ ] falta |
| 3449 | `LEXR-01756` | volverse pardo | diccionario_general | - [ ] falta |
| 3450 | `LEXR-03157` | volverse perezozo | diccionario_general | - [ ] falta |
| 3451 | `LEXR-03753` | volverse sordo | diccionario_general | - [ ] falta |
| 3452 | `LEXR-00911` | vomitar | diccionario_general | - [ ] falta |
| 3453 | `LEXR-03720` | vía láctea | diccionario_general | - [ ] falta |
| 3454 | `LEXR-01260` | víbora venenosa (bothropo atrox) | diccionario_general | - [ ] falta |
| 3455 | `LEXR-00746` | y | diccionario_general | - [ ] falta |
| 3456 | `LEXR-00847` | yacuma blanca (planta medicinal) | diccionario_general | - [ ] falta |
| 3457 | `LEXR-02488` | yerbatero | diccionario_general | - [ ] falta |
| 3458 | `LEXR-01506` | yo (femenino) | diccionario_general | - [ ] falta |
| 3459 | `LEXR-03219` | yo, conmigo, mine | diccionario_general | - [ ] falta |
| 3460 | `LEXR-02873` | yuca viche | diccionario_general | - [ ] falta |
| 3461 | `LEXR-02486` | zafar, quitar | diccionario_general | - [ ] falta |
| 3462 | `LEXR-02669` | zafarse | diccionario_general | - [ ] falta |
| 3463 | `LEXR-02175` | zafarse y caer | diccionario_general | - [ ] falta |
| 3464 | `LEXR-01018` | zafarse, desengarzarse | diccionario_general | - [ ] falta |
| 3465 | `LEXR-03368` | zarco | diccionario_general | - [ ] falta |
| 3466 | `LEXR-02394` | zarco, azul-verde | diccionario_general | - [ ] falta |
| 3467 | `LEXR-00775` | zarigüeya, chucha | diccionario_general | - [ ] falta |
| 3468 | `LEXR-02237` | zarzamora (planta) | diccionario_general | - [ ] falta |
| 3469 | `LEXR-02594` | zorrillo, comadreja (mamífero) | diccionario_general | - [x] `diccionario_general/zorrillo,_comadreja_(mamífero).png` |
| 3470 | `LEXR-01164` | zorro | diccionario_general | - [ ] falta |
| 3471 | `LEXR-00556` | zumbar | diccionario_general | - [ ] falta |
| 3472 | `LEXR-03000` | zumo de la hoja de encenillo (medicinal) | diccionario_general | - [ ] falta |
| 3473 | `LEXR-01383` | zurdo | diccionario_general | - [ ] falta |
| 3474 | `LEXR-01921` | ¡Camine! | diccionario_general | - [ ] falta |
| 3475 | `LEXR-02165` | ¡Coma! | diccionario_general | - [ ] falta |
| 3476 | `LEXR-00805` | ¡Coséchelo! | diccionario_general | - [ ] falta |
| 3477 | `LEXR-01462` | ¡Diga! | diccionario_general | - [ ] falta |
| 3478 | `LEXR-01602` | ¡Dispare! | diccionario_general | - [ ] falta |
| 3479 | `LEXR-02381` | ¡Déle! | diccionario_general | - [ ] falta |
| 3480 | `LEXR-03588` | ¡Entre! | diccionario_general | - [ ] falta |
| 3481 | `LEXR-03491` | ¡Fuera! (ahuyentando gallinas) | diccionario_general | - [ ] falta |
| 3482 | `LEXR-03542` | ¡Llore! | diccionario_general | - [ ] falta |
| 3483 | `LEXR-00614` | ¡Muélalo! | diccionario_general | - [ ] falta |
| 3484 | `LEXR-02432` | ¡Pégale! | diccionario_general | - [ ] falta |
| 3485 | `LEXR-02536` | ¡Que esté! | diccionario_general | - [ ] falta |
| 3486 | `LEXR-01300` | ¡Quiébrelo! | diccionario_general | - [ ] falta |
| 3487 | `LEXR-01150` | ¡Siémbrelo! | diccionario_general | - [ ] falta |
| 3488 | `LEXR-02676` | ¡Toma! | diccionario_general | - [ ] falta |
| 3489 | `LEXR-01837` | ¡Uy! (expresión de asombro) | diccionario_general | - [ ] falta |
| 3490 | `LEXR-01796` | ¡Vaya! | diccionario_general | - [ ] falta |
| 3491 | `LEXR-02754` | ¿por qué?, ¿para qué? | diccionario_general | - [ ] falta |
| 3492 | `LEXR-01475` | ácido | diccionario_general | - [ ] falta |
| 3493 | `LEXR-01489` | él, ella, aquel, aquella, ese, esa | diccionario_general | - [ ] falta |
| 3494 | `LEXR-03174` | él, ella, aquél, aquélla | diccionario_general | - [ ] falta |
| 3495 | `LEXR-02115` | último | diccionario_general | - [ ] falta |
| 3496 | `LEXR-01924` | último, menor (ej. hijo, menor de todos) | diccionario_general | - [ ] falta |
| 3497 | `LEXR-00637` | útil | diccionario_general | - [ ] falta |
| 3498 | `LEX-00236` | Aguacate | frutas_verduras | - [x] `frutas_verduras/aguacate.png` |
| 3499 | `LEX-00217` | Ajo | frutas_verduras | - [x] `frutas_verduras/ajo.png` |
| 3500 | `LEX-00221` | Banano | frutas_verduras | - [x] `frutas_verduras/banano.png` |
| 3501 | `LEX-00228` | Chirimoya | frutas_verduras | - [x] `frutas_verduras/chirimoya.png` |
| 3502 | `LEX-00215` | Curuba | frutas_verduras | - [x] `frutas_verduras/curuba.png` |
| 3503 | `LEX-00222` | Durazno | frutas_verduras | - [x] `frutas_verduras/durazno.png` |
| 3504 | `LEX-00234` | Granadilla | frutas_verduras | - [x] `frutas_verduras/granadilla.png` |
| 3505 | `LEX-00216` | Guama | frutas_verduras | - [x] `frutas_verduras/guama.png` |
| 3506 | `LEX-00229` | Guanabana | frutas_verduras | - [x] `frutas_verduras/guanabana.png` |
| 3507 | `LEX-00232` | Guayaba | frutas_verduras | - [x] `frutas_verduras/guayaba.png` |
| 3508 | `LEX-00225` | Limon | frutas_verduras | - [x] `frutas_verduras/limon.png` |
| 3509 | `LEX-00230` | Lulo | frutas_verduras | - [x] `frutas_verduras/lulo.png` |
| 3510 | `LEX-00235` | Mandarina | frutas_verduras | - [x] `frutas_verduras/mandarina.png` |
| 3511 | `LEX-00218` | Mango | frutas_verduras | - [x] `frutas_verduras/mango.png` |
| 3512 | `LEX-00231` | Manzana | frutas_verduras | - [x] `frutas_verduras/manzana.png` |
| 3513 | `LEX-00237` | Maracuya | frutas_verduras | - [x] `frutas_verduras/maracuya.png` |
| 3514 | `LEX-00233` | Mora | frutas_verduras | - [x] `frutas_verduras/mora.png` |
| 3515 | `LEX-00224` | Naranja | frutas_verduras | - [x] `frutas_verduras/naranja.png` |
| 3516 | `LEX-00227` | Papaya | frutas_verduras | - [x] `frutas_verduras/papaya.png` |
| 3517 | `LEX-00219` | Pina | frutas_verduras | - [x] `frutas_verduras/pina.png` |
| 3518 | `LEX-00226` | Tomate | frutas_verduras | - [x] `frutas_verduras/tomate.png` |
| 3519 | `LEX-00214` | Uva silvestre | frutas_verduras | - [x] `frutas_verduras/uva_silvestre.png` |
| 3520 | `LEX-00220` | Uvas | frutas_verduras | - [x] `frutas_verduras/uvas.png` |
| 3521 | `LEX-00223` | Zapote | frutas_verduras | - [x] `frutas_verduras/zapote.png` |
| 3522 | `LEX-00291` | Ahoyador | herramientas | - [x] `herramientas/ahoyador.png` |
| 3523 | `LEX-00285` | Alicate | herramientas | - [x] `herramientas/alicate.png` |
| 3524 | `LEX-00284` | Azadon | herramientas | - [x] `herramientas/azadon.png` |
| 3525 | `LEX-00282` | Barra | herramientas | - [x] `herramientas/barra.png` |
| 3526 | `LEX-00286` | Barreton | herramientas | - [x] `herramientas/barreton.png` |
| 3527 | `LEX-00287` | Carretilla | herramientas | - [x] `herramientas/carretilla.png` |
| 3528 | `LEX-00290` | Deshojador | herramientas | - [x] `herramientas/deshojador.png` |
| 3529 | `LEX-00292` | Flauta | herramientas | - [x] `herramientas/flauta.png` |
| 3530 | `LEX-00295` | Guitarra | herramientas | - [x] `herramientas/guitarra.png` |
| 3531 | `LEX-00281` | Hacha | herramientas | - [x] `herramientas/hacha.png` |
| 3532 | `LEX-00289` | Machete | herramientas | - [x] `herramientas/machete.png` |
| 3533 | `LEX-00297` | Manguera | herramientas | - [x] `herramientas/manguera.png` |
| 3534 | `LEX-00296` | Martillo | herramientas | - [x] `herramientas/martillo.png` |
| 3535 | `LEX-00288` | Motosierra | herramientas | - [x] `herramientas/motosierra.png` |
| 3536 | `LEX-00283` | Pica | herramientas | - [x] `herramientas/pica.png` |
| 3537 | `LEX-00294` | Tambor | herramientas | - [x] `herramientas/tambor.png` |
| 3538 | `LEX-00293` | Zampona | herramientas | - [x] `herramientas/zampona.png` |
| 3539 | `LEX-00347` | Cama | muebles_inmuebles | - [x] `muebles_inmuebles/cama.png` |
| 3540 | `LEX-00358` | Casa | muebles_inmuebles | - [x] `muebles_inmuebles/casa.png` |
| 3541 | `LEX-00359` | Choza | muebles_inmuebles | - [x] `muebles_inmuebles/choza.png` |
| 3542 | `LEX-00349` | Cocina | muebles_inmuebles | - [x] `muebles_inmuebles/cocina.png` |
| 3543 | `LEX-00356` | Dinero | muebles_inmuebles | - [x] `muebles_inmuebles/dinero.png` |
| 3544 | `LEX-00354` | Huerta | muebles_inmuebles | - [x] `muebles_inmuebles/huerta.png` |
| 3545 | `LEX-00346` | Lavadero de ropa | muebles_inmuebles | - [x] `muebles_inmuebles/lavadero_de_ropa.png` |
| 3546 | `LEX-00351` | Mesa | muebles_inmuebles | - [x] `muebles_inmuebles/mesa.png` |
| 3547 | `LEX-00357` | Puente | muebles_inmuebles | - [x] `muebles_inmuebles/puente.png` |
| 3548 | `LEX-00355` | Puerta | muebles_inmuebles | - [x] `muebles_inmuebles/puerta.png` |
| 3549 | `LEX-00348` | Ropero | muebles_inmuebles | - [x] `muebles_inmuebles/ropero.png` |
| 3550 | `LEX-00350` | Sala | muebles_inmuebles | - [x] `muebles_inmuebles/sala.png` |
| 3551 | `LEX-00352` | Silla | muebles_inmuebles | - [x] `muebles_inmuebles/silla.png` |
| 3552 | `LEX-00353` | Trapiche | muebles_inmuebles | - [x] `muebles_inmuebles/trapiche.png` |
| 3553 | `LEX-00360` | Ventana | muebles_inmuebles | - [x] `muebles_inmuebles/ventana.png` |
| 3554 | `LEX-00380` | abel | nombres_propios | - [x] `nombres_propios/abel.png` |
| 3555 | `LEX-00374` | cecilia | nombres_propios | - [x] `nombres_propios/cecilia.png` |
| 3556 | `LEX-00377` | domingo | nombres_propios | - [x] `nombres_propios/domingo.png` |
| 3557 | `LEX-00369` | enrique | nombres_propios | - [x] `nombres_propios/enrique.png` |
| 3558 | `LEX-00368` | enriqueta | nombres_propios | - [x] `nombres_propios/enriqueta.png` |
| 3559 | `LEX-00375` | francisca | nombres_propios | - [x] `nombres_propios/francisca.png` |
| 3560 | `LEX-00367` | francisco | nombres_propios | - [x] `nombres_propios/francisco.png` |
| 3561 | `LEX-00373` | isabela | nombres_propios | - [x] `nombres_propios/isabela.png` |
| 3562 | `LEX-00366` | jesus | nombres_propios | - [x] `nombres_propios/jesus.png` |
| 3563 | `LEX-00364` | jose | nombres_propios | - [x] `nombres_propios/jose.png` |
| 3564 | `LEX-00365` | josefa | nombres_propios | - [x] `nombres_propios/josefa.png` |
| 3565 | `LEX-00362` | juan | nombres_propios | - [x] `nombres_propios/juan.png` |
| 3566 | `LEX-00363` | juana | nombres_propios | - [x] `nombres_propios/juana.png` |
| 3567 | `LEX-00361` | juliana | nombres_propios | - [x] `nombres_propios/juliana.png` |
| 3568 | `LEX-00371` | manuel | nombres_propios | - [x] `nombres_propios/manuel.png` |
| 3569 | `LEX-00370` | maria | nombres_propios | - [x] `nombres_propios/maria.png` |
| 3570 | `LEX-00378` | martin | nombres_propios | - [x] `nombres_propios/martin.png` |
| 3571 | `LEX-00379` | martina | nombres_propios | - [x] `nombres_propios/martina.png` |
| 3572 | `LEX-00376` | otilia | nombres_propios | - [x] `nombres_propios/otilia.png` |
| 3573 | `LEX-00372` | pedro | nombres_propios | - [x] `nombres_propios/pedro.png` |
| 3574 | `LEX-00015` | Catorce | numeros | - [x] `numeros/catorce.png` |
| 3575 | `LEX-00001` | Cero | numeros | - [x] `numeros/cero.png` |
| 3576 | `LEX-00029` | Cien | numeros | - [x] `numeros/cien.png` |
| 3577 | `LEX-00056` | Cien mil | numeros | - [x] `numeros/cien_mil.png` |
| 3578 | `LEX-00006` | Cinco | numeros | - [x] `numeros/cinco.png` |
| 3579 | `LEX-00042` | Cinco mil | numeros | - [x] `numeros/cinco_mil.png` |
| 3580 | `LEX-00024` | Cincuenta | numeros | - [x] `numeros/cincuenta.png` |
| 3581 | `LEX-00051` | Cincuenta mil | numeros | - [x] `numeros/cincuenta_mil.png` |
| 3582 | `LEX-00023` | Cuarenta | numeros | - [x] `numeros/cuarenta.png` |
| 3583 | `LEX-00050` | Cuarenta mil | numeros | - [x] `numeros/cuarenta_mil.png` |
| 3584 | `LEX-00005` | Cuatro | numeros | - [x] `numeros/cuatro.png` |
| 3585 | `LEX-00041` | Cuatro mil | numeros | - [x] `numeros/cuatro_mil.png` |
| 3586 | `LEX-00032` | Cuatrocientos | numeros | - [x] `numeros/cuatrocientos.png` |
| 3587 | `LEX-00020` | Diecinueve | numeros | - [x] `numeros/diecinueve.png` |
| 3588 | `LEX-00019` | Dieciocho | numeros | - [x] `numeros/dieciocho.png` |
| 3589 | `LEX-00017` | Dieciseis | numeros | - [x] `numeros/dieciseis.png` |
| 3590 | `LEX-00018` | Diecisiete | numeros | - [x] `numeros/diecisiete.png` |
| 3591 | `LEX-00011` | Diez | numeros | - [x] `numeros/diez.png` |
| 3592 | `LEX-00047` | Diez mil | numeros | - [x] `numeros/diez_mil.png` |
| 3593 | `LEX-00013` | Doce | numeros | - [x] `numeros/doce.png` |
| 3594 | `LEX-00003` | Dos | numeros | - [x] `numeros/dos.png` |
| 3595 | `LEX-00039` | Dos mil | numeros | - [x] `numeros/dos_mil.png` |
| 3596 | `LEX-00058` | Dos millones | numeros | - [x] `numeros/dos_millones.png` |
| 3597 | `LEX-00030` | Doscientos | numeros | - [x] `numeros/doscientos.png` |
| 3598 | `LEX-00038` | Mil | numeros | - [x] `numeros/mil.png` |
| 3599 | `LEX-00037` | Novecientos | numeros | - [x] `numeros/novecientos.png` |
| 3600 | `LEX-00028` | Noventa | numeros | - [x] `numeros/noventa.png` |
| 3601 | `LEX-00055` | Noventa mil | numeros | - [x] `numeros/noventa_mil.png` |
| 3602 | `LEX-00010` | Nueve | numeros | - [x] `numeros/nueve.png` |
| 3603 | `LEX-00046` | Nueve mil | numeros | - [x] `numeros/nueve_mil.png` |
| 3604 | `LEX-00027` | Ochenta | numeros | - [x] `numeros/ochenta.png` |
| 3605 | `LEX-00054` | Ochenta mil | numeros | - [x] `numeros/ochenta_mil.png` |
| 3606 | `LEX-00009` | Ocho | numeros | - [x] `numeros/ocho.png` |
| 3607 | `LEX-00045` | Ocho mil | numeros | - [x] `numeros/ocho_mil.png` |
| 3608 | `LEX-00036` | Ochocientos | numeros | - [x] `numeros/ochocientos.png` |
| 3609 | `LEX-00012` | Once | numeros | - [x] `numeros/once.png` |
| 3610 | `LEX-00016` | Quince | numeros | - [x] `numeros/quince.png` |
| 3611 | `LEX-00033` | Quinientos | numeros | - [x] `numeros/quinientos.png` |
| 3612 | `LEX-00007` | Seis | numeros | - [x] `numeros/seis.png` |
| 3613 | `LEX-00043` | Seis mil | numeros | - [x] `numeros/seis_mil.png` |
| 3614 | `LEX-00034` | Seiscientos | numeros | - [x] `numeros/seiscientos.png` |
| 3615 | `LEX-00025` | Sesenta | numeros | - [x] `numeros/sesenta.png` |
| 3616 | `LEX-00052` | Sesenta mil | numeros | - [x] `numeros/sesenta_mil.png` |
| 3617 | `LEX-00035` | Setecientos | numeros | - [x] `numeros/setecientos.png` |
| 3618 | `LEX-00026` | Setenta | numeros | - [x] `numeros/setenta.png` |
| 3619 | `LEX-00053` | Setenta mil | numeros | - [x] `numeros/setenta_mil.png` |
| 3620 | `LEX-00008` | Siete | numeros | - [x] `numeros/siete.png` |
| 3621 | `LEX-00044` | Siete mil | numeros | - [x] `numeros/siete_mil.png` |
| 3622 | `LEX-00014` | Trece | numeros | - [x] `numeros/trece.png` |
| 3623 | `LEX-00022` | Treinta | numeros | - [x] `numeros/treinta.png` |
| 3624 | `LEX-00049` | Treinta mil | numeros | - [x] `numeros/treinta_mil.png` |
| 3625 | `LEX-00004` | Tres | numeros | - [x] `numeros/tres.png` |
| 3626 | `LEX-00040` | Tres mil | numeros | - [x] `numeros/tres_mil.png` |
| 3627 | `LEX-00031` | Trescientos | numeros | - [x] `numeros/trescientos.png` |
| 3628 | `LEX-00057` | Un millon | numeros | - [x] `numeros/un_millon.png` |
| 3629 | `LEX-00002` | Uno | numeros | - [x] `numeros/uno.png` |
| 3630 | `LEX-00021` | Veinte | numeros | - [x] `numeros/veinte.png` |
| 3631 | `LEX-00048` | Veinte mil | numeros | - [x] `numeros/veinte_mil.png` |
| 3632 | `LEX-00182` | Abuela | parentescos | - [x] `parentescos/abuela.png` |
| 3633 | `LEX-00185` | Abuelo | parentescos | - [x] `parentescos/abuelo.png` |
| 3634 | `LEX-00181` | Ahijado | parentescos | - [x] `parentescos/ahijado.png` |
| 3635 | `LEX-00184` | Anciana | parentescos | - [x] `parentescos/anciana.png` |
| 3636 | `LEX-00178` | Cunado | parentescos | - [x] `parentescos/cunado.png` |
| 3637 | `LEX-00180` | Esposa | parentescos | - [x] `parentescos/esposa.png` |
| 3638 | `LEX-00177` | Hermana | parentescos | - [x] `parentescos/hermana.png` |
| 3639 | `LEX-00188` | Hermano | parentescos | - [x] `parentescos/hermano.png` |
| 3640 | `LEX-00183` | Hija | parentescos | - [x] `parentescos/hija.png` |
| 3641 | `LEX-00179` | Hijo | parentescos | - [x] `parentescos/hijo.png` |
| 3642 | `LEX-00187` | Mama | parentescos | - [x] `parentescos/mama.png` |
| 3643 | `LEX-00189` | Nieto o nieta | parentescos | - [x] `parentescos/nieto_o_nieta.png` |
| 3644 | `LEX-00186` | Papa | parentescos | - [x] `parentescos/papa.png` |
| 3645 | `LEX-00252` | Alegria | plantas_medicinales | - [x] `plantas_medicinales/alegria.png` |
| 3646 | `LEX-00250` | Aloe vera | plantas_medicinales | - [x] `plantas_medicinales/aloe_vera.png` |
| 3647 | `LEX-00240` | Barbasco | plantas_medicinales | - [x] `plantas_medicinales/barbasco.png` |
| 3648 | `LEX-00239` | Botoncillo | plantas_medicinales | - [x] `plantas_medicinales/botoncillo.png` |
| 3649 | `LEX-00257` | Chilca | plantas_medicinales | - [x] `plantas_medicinales/chilca.png` |
| 3650 | `LEX-00253` | Coca | plantas_medicinales | - [x] `plantas_medicinales/coca.png` |
| 3651 | `LEX-00244` | Escoba | plantas_medicinales | - [x] `plantas_medicinales/escoba.png` |
| 3652 | `LEX-00249` | Lengua de vaca | plantas_medicinales | - [x] `plantas_medicinales/lengua_de_vaca.png` |
| 3653 | `LEX-00254` | Ortiga | plantas_medicinales | - [x] `plantas_medicinales/ortiga.png` |
| 3654 | `LEX-00255` | Ortiga roja | plantas_medicinales | - [x] `plantas_medicinales/ortiga_roja.png` |
| 3655 | `LEX-00248` | Paico | plantas_medicinales | - [x] `plantas_medicinales/paico.png` |
| 3656 | `LEX-00238` | Poleo | plantas_medicinales | - [x] `plantas_medicinales/poleo.png` |
| 3657 | `LEX-00242` | Ruda | plantas_medicinales | - [x] `plantas_medicinales/ruda.png` |
| 3658 | `LEX-00247` | Tabaco | plantas_medicinales | - [x] `plantas_medicinales/tabaco.png` |
| 3659 | `LEX-00243` | Tomillo | plantas_medicinales | - [x] `plantas_medicinales/tomillo.png` |
| 3660 | `LEX-00251` | Verbena | plantas_medicinales | - [x] `plantas_medicinales/verbena.png` |
| 3661 | `LEX-00245` | Yerba chivo | plantas_medicinales | - [x] `plantas_medicinales/yerba_chivo.png` |
| 3662 | `LEX-00246` | Yerba golpe | plantas_medicinales | - [x] `plantas_medicinales/yerba_golpe.png` |
| 3663 | `LEX-00241` | Yerba mora | plantas_medicinales | - [x] `plantas_medicinales/yerba_mora.png` |
| 3664 | `LEX-00256` | Yerbabuena | plantas_medicinales | - [x] `plantas_medicinales/yerbabuena.png` |
| 3665 | `LEX-00113` | Saludo basico | saludos | - [x] `saludos/saludo_basico.png` |
| 3666 | `LEX-00315` | Algodon | utiles_hogar | - [x] `utiles_hogar/algodon.png` |
| 3667 | `LEX-00314` | Bano o inodoro | utiles_hogar | - [x] `utiles_hogar/bano_o_inodoro.png` |
| 3668 | `LEX-00298` | Cernidor | utiles_hogar | - [x] `utiles_hogar/cernidor.png` |
| 3669 | `LEX-00312` | Cuchara | utiles_hogar | - [x] `utiles_hogar/cuchara.png` |
| 3670 | `LEX-00305` | Cucharona | utiles_hogar | - [x] `utiles_hogar/cucharona.png` |
| 3671 | `LEX-00304` | Cuchillo | utiles_hogar | - [x] `utiles_hogar/cuchillo.png` |
| 3672 | `LEX-00310` | Ducha | utiles_hogar | - [x] `utiles_hogar/ducha.png` |
| 3673 | `LEX-00311` | Espejo | utiles_hogar | - [x] `utiles_hogar/espejo.png` |
| 3674 | `LEX-00302` | Estufa | utiles_hogar | - [x] `utiles_hogar/estufa.png` |
| 3675 | `LEX-00306` | Fogon | utiles_hogar | - [x] `utiles_hogar/fogon.png` |
| 3676 | `LEX-00299` | Humo | utiles_hogar | - [x] `utiles_hogar/humo.png` |
| 3677 | `LEX-00307` | Jabon | utiles_hogar | - [x] `utiles_hogar/jabon.png` |
| 3678 | `LEX-00309` | Olla | utiles_hogar | - [x] `utiles_hogar/olla.png` |
| 3679 | `LEX-00308` | Olleta | utiles_hogar | - [x] `utiles_hogar/olleta.png` |
| 3680 | `LEX-00313` | Peine | utiles_hogar | - [x] `utiles_hogar/peine.png` |
| 3681 | `LEX-00301` | Plato | utiles_hogar | - [x] `utiles_hogar/plato.png` |
| 3682 | `LEX-00300` | Trampa | utiles_hogar | - [x] `utiles_hogar/trampa.png` |
| 3683 | `LEX-00303` | Vaso | utiles_hogar | - [x] `utiles_hogar/vaso.png` |
| 3684 | `LEX-00080` | Abrir o extender los brazos | vocabulario_general | - [x] `vocabulario_general/abrir_o_extender_los_brazos.png` |
| 3685 | `LEX-00110` | Agarrar | vocabulario_general | - [x] `vocabulario_general/agarrar.png` |
| 3686 | `LEX-00106` | Amarrar | vocabulario_general | - [x] `vocabulario_general/amarrar.png` |
| 3687 | `LEX-00100` | Ancho | vocabulario_general | - [x] `vocabulario_general/ancho.png` |
| 3688 | `LEX-00095` | Ayudar o colaborar | vocabulario_general | - [x] `vocabulario_general/ayudar_o_colaborar.png` |
| 3689 | `LEX-00090` | Bailar o danzar | vocabulario_general | - [x] `vocabulario_general/bailar_o_danzar.png` |
| 3690 | `LEX-00094` | Barrer | vocabulario_general | - [x] `vocabulario_general/barrer.png` |
| 3691 | `LEX-00082` | Barro | vocabulario_general | - [x] `vocabulario_general/barro.png` |
| 3692 | `LEX-00112` | Bonito o hermosa | vocabulario_general | - [x] `vocabulario_general/bonito_o_hermosa.png` |
| 3693 | `LEX-00089` | Borrar o limpiar | vocabulario_general | - [x] `vocabulario_general/borrar_o_limpiar.png` |
| 3694 | `LEX-00077` | Caliente | vocabulario_general | - [x] `vocabulario_general/caliente.png` |
| 3695 | `LEX-00111` | Camino | vocabulario_general | - [x] `vocabulario_general/camino.png` |
| 3696 | `LEX-00105` | Cargar | vocabulario_general | - [x] `vocabulario_general/cargar.png` |
| 3697 | `LEX-00079` | Cerrar | vocabulario_general | - [x] `vocabulario_general/cerrar.png` |
| 3698 | `LEX-00076` | Colgar | vocabulario_general | - [x] `vocabulario_general/colgar.png` |
| 3699 | `LEX-00107` | Correr o trotar | vocabulario_general | - [x] `vocabulario_general/correr_o_trotar.png` |
| 3700 | `LEX-00096` | Cortar | vocabulario_general | - [x] `vocabulario_general/cortar.png` |
| 3701 | `LEX-00103` | Cuidar o vigilar | vocabulario_general | - [x] `vocabulario_general/cuidar_o_vigilar.png` |
| 3702 | `LEX-00109` | Dar o entregar | vocabulario_general | - [x] `vocabulario_general/dar_o_entregar.png` |
| 3703 | `LEX-00097` | Dibujando | vocabulario_general | - [x] `vocabulario_general/dibujando.png` |
| 3704 | `LEX-00084` | Divertido o alegre | vocabulario_general | - [x] `vocabulario_general/divertido_o_alegre.png` |
| 3705 | `LEX-00087` | Escribir | vocabulario_general | - [x] `vocabulario_general/escribir.png` |
| 3706 | `LEX-00081` | Espina o chuzo | vocabulario_general | - [x] `vocabulario_general/espina_o_chuzo.png` |
| 3707 | `LEX-00099` | Flaco | vocabulario_general | - [x] `vocabulario_general/flaco.png` |
| 3708 | `LEX-00083` | Fuerza | vocabulario_general | - [x] `vocabulario_general/fuerza.png` |
| 3709 | `LEX-00088` | Hueco | vocabulario_general | - [x] `vocabulario_general/hueco.png` |
| 3710 | `LEX-00102` | Lamer | vocabulario_general | - [x] `vocabulario_general/lamer.png` |
| 3711 | `LEX-00104` | Lavar o enjabonar | vocabulario_general | - [x] `vocabulario_general/lavar_o_enjabonar.png` |
| 3712 | `LEX-00085` | Mojado | vocabulario_general | - [x] `vocabulario_general/mojado.png` |
| 3713 | `LEX-00108` | Nacer o reventar huevos | vocabulario_general | - [x] `vocabulario_general/nacer_o_reventar_huevos.png` |
| 3714 | `LEX-00091` | Noche | vocabulario_general | - [x] `vocabulario_general/noche.png` |
| 3715 | `LEX-00092` | Por favor | vocabulario_general | - [x] `vocabulario_general/por_favor.png` |
| 3716 | `LEX-00101` | Redondo o circulo | vocabulario_general | - [x] `vocabulario_general/redondo_o_circulo.png` |
| 3717 | `LEX-00086` | Sucio | vocabulario_general | - [x] `vocabulario_general/sucio.png` |
| 3718 | `LEX-00098` | Sueño | vocabulario_general | - [x] `vocabulario_general/sueño.png` |
| 3719 | `LEX-00078` | Tapar o cubrir | vocabulario_general | - [x] `vocabulario_general/tapar_o_cubrir.png` |
| 3720 | `LEX-00093` | Trabajo colectivo por un mismo objetivo | vocabulario_general | - [x] `vocabulario_general/trabajo_colectivo_por_un_mismo_objetivo.png` |

## Todas las entradas (orden por id)

Las **3922** filas siguientes son todas las filas lexicas del CSV; comparten imagen cuando coinciden **espanol + categoria** con un par de la tabla superior (3720 claves de imagen).

| id | nasa_yuwe | espanol | categoria |
|----|-----------|---------|-----------|
| `LEX-00001` | Mea | Cero | numeros |
| `LEX-00002` | Teeçx | Uno | numeros |
| `LEX-00003` | E'z | Dos | numeros |
| `LEX-00004` | Tekh | Tres | numeros |
| `LEX-00005` | Pahz | Cuatro | numeros |
| `LEX-00006` | Tahç | Cinco | numeros |
| `LEX-00007` | Setx | Seis | numeros |
| `LEX-00008` | Sa't | Siete | numeros |
| `LEX-00009` | Tawn | Ocho | numeros |
| `LEX-00010` | Kheb | Nueve | numeros |
| `LEX-00011` | Kseba | Diez | numeros |
| `LEX-00012` | Kse teeçx | Once | numeros |
| `LEX-00013` | Kse e'z | Doce | numeros |
| `LEX-00014` | Kse tekh | Trece | numeros |
| `LEX-00015` | Kse pahz | Catorce | numeros |
| `LEX-00016` | Kse tahç | Quince | numeros |
| `LEX-00017` | Kse setx | Dieciseis | numeros |
| `LEX-00018` | Kse sa't | Diecisiete | numeros |
| `LEX-00019` | Kse tawn | Dieciocho | numeros |
| `LEX-00020` | Kse kheb | Diecinueve | numeros |
| `LEX-00021` | Eba | Veinte | numeros |
| `LEX-00022` | Teba | Treinta | numeros |
| `LEX-00023` | Paba | Cuarenta | numeros |
| `LEX-00024` | Taba | Cincuenta | numeros |
| `LEX-00025` | Seba | Sesenta | numeros |
| `LEX-00026` | Saba | Setenta | numeros |
| `LEX-00027` | Tawnba | Ochenta | numeros |
| `LEX-00028` | Kheba | Noventa | numeros |
| `LEX-00029` | Eçxkan | Cien | numeros |
| `LEX-00030` | Ekan | Doscientos | numeros |
| `LEX-00031` | Tekan | Trescientos | numeros |
| `LEX-00032` | Pakan | Cuatrocientos | numeros |
| `LEX-00033` | Takan | Quinientos | numeros |
| `LEX-00034` | Sekan | Seiscientos | numeros |
| `LEX-00035` | Sakan | Setecientos | numeros |
| `LEX-00036` | Tawnkan | Ochocientos | numeros |
| `LEX-00037` | Khekan | Novecientos | numeros |
| `LEX-00038` | Pkab | Mil | numeros |
| `LEX-00039` | Epkab | Dos mil | numeros |
| `LEX-00040` | Tepkab | Tres mil | numeros |
| `LEX-00041` | Papkab | Cuatro mil | numeros |
| `LEX-00042` | Tapkab | Cinco mil | numeros |
| `LEX-00043` | Sepkab | Seis mil | numeros |
| `LEX-00044` | Sapkab | Siete mil | numeros |
| `LEX-00045` | Tawnpkab | Ocho mil | numeros |
| `LEX-00046` | Khepkab | Nueve mil | numeros |
| `LEX-00047` | Kseba pkab | Diez mil | numeros |
| `LEX-00048` | Eba pkab | Veinte mil | numeros |
| `LEX-00049` | Teba pkab | Treinta mil | numeros |
| `LEX-00050` | Paba pkab | Cuarenta mil | numeros |
| `LEX-00051` | Taba pkab | Cincuenta mil | numeros |
| `LEX-00052` | Seba pkab | Sesenta mil | numeros |
| `LEX-00053` | Saba pkab | Setenta mil | numeros |
| `LEX-00054` | Tawnba pkab | Ochenta mil | numeros |
| `LEX-00055` | Kheba pkab | Noventa mil | numeros |
| `LEX-00056` | Eçxkan pkab | Cien mil | numeros |
| `LEX-00057` | Pizx | Un millon | numeros |
| `LEX-00058` | E'z pizx | Dos millones | numeros |
| `LEX-00059` | Behbeh lem | Anaranjado | colores |
| `LEX-00060` | Çeenx | Verde | colores |
| `LEX-00061` | Çemçem | Azul | colores |
| `LEX-00062` | Beh | Rojo | colores |
| `LEX-00063` | Behbeh | Rojo encendido | colores |
| `LEX-00064` | Çxihme | Blanco | colores |
| `LEX-00065` | Khüçxh | Negro | colores |
| `LEX-00066` | Khuuç | Gris | colores |
| `LEX-00067` | Tçxkiy | Amarillo | colores |
| `LEX-00068` | cuchi | cerdo | animales |
| `LEX-00069` | cuchi | puerco | animales |
| `LEX-00070` | cuchi ĩts | hocico del puerco | animales |
| `LEX-00071` | cuchi tel | horqueta para puerco | animales |
| `LEX-00072` | cuchi vyllill | pezuña del puerco | animales |
| `LEX-00073` | quiwe cuchi | pecari | animales |
| `LEX-00074` | yu’cj cuchi | saino | animales |
| `LEX-00075` | yu’cj cuchi | aguti o guatuza | animales |
| `LEX-00076` | A'y | Colgar | vocabulario_general |
| `LEX-00077` | Açxa | Caliente | vocabulario_general |
| `LEX-00078` | Afxihb | Tapar o cubrir | vocabulario_general |
| `LEX-00079` | Aph | Cerrar | vocabulario_general |
| `LEX-00080` | Çha’ya | Abrir o extender los brazos | vocabulario_general |
| `LEX-00081` | Çhüçh | Espina o chuzo | vocabulario_general |
| `LEX-00082` | Çiç | Barro | vocabulario_general |
| `LEX-00083` | Çxhaçxha | Fuerza | vocabulario_general |
| `LEX-00084` | Çxhakwe | Divertido o alegre | vocabulario_general |
| `LEX-00085` | Çxupx | Mojado | vocabulario_general |
| `LEX-00086` | Çxus | Sucio | vocabulario_general |
| `LEX-00087` | Fxi’j | Escribir | vocabulario_general |
| `LEX-00088` | Kafx | Hueco | vocabulario_general |
| `LEX-00089` | Khukh | Borrar o limpiar | vocabulario_general |
| `LEX-00090` | Ku’jxa | Bailar o danzar | vocabulario_general |
| `LEX-00091` | Kus | Noche | vocabulario_general |
| `LEX-00092` | Meen | Por favor | vocabulario_general |
| `LEX-00093` | Minga | Trabajo colectivo por un mismo objetivo | vocabulario_general |
| `LEX-00094` | Pad | Barrer | vocabulario_general |
| `LEX-00095` | Puçx | Ayudar o colaborar | vocabulario_general |
| `LEX-00096` | Speth | Cortar | vocabulario_general |
| `LEX-00097` | Suçn | Dibujando | vocabulario_general |
| `LEX-00098` | Sxa'w | Sueño | vocabulario_general |
| `LEX-00099` | Talx | Flaco | vocabulario_general |
| `LEX-00100` | Tape | Ancho | vocabulario_general |
| `LEX-00101` | Taz | Redondo o circulo | vocabulario_general |
| `LEX-00102` | Teçx | Lamer | vocabulario_general |
| `LEX-00103` | Thegu | Cuidar o vigilar | vocabulario_general |
| `LEX-00104` | Theth | Lavar o enjabonar | vocabulario_general |
| `LEX-00105` | Tu's | Cargar | vocabulario_general |
| `LEX-00106` | Tud | Amarrar | vocabulario_general |
| `LEX-00107` | Üph | Correr o trotar | vocabulario_general |
| `LEX-00108` | Upx | Nacer o reventar huevos | vocabulario_general |
| `LEX-00109` | Üs | Dar o entregar | vocabulario_general |
| `LEX-00110` | Uwe | Agarrar | vocabulario_general |
| `LEX-00111` | Zi’j | Camino | vocabulario_general |
| `LEX-00112` | Zxiçxkwe | Bonito o hermosa | vocabulario_general |
| `LEX-00113` | Ma’g pe’t | Saludo basico | saludos |
| `LEX-00114` | Ma’w pe’t | Saludo basico | saludos |
| `LEX-00115` | Ma'g fxi'z | Saludo basico | saludos |
| `LEX-00116` | Ma'w fxi'z | Saludo basico | saludos |
| `LEX-00117` | Ma'g ikuus | Saludo basico | saludos |
| `LEX-00118` | Ma'w ikuus | Saludo basico | saludos |
| `LEX-00119` | Puutx yunhaw | Saludo basico | saludos |
| `LEX-00120` | Anza | Carpintero | animales |
| `LEX-00121` | Çuh | Gorrion | animales |
| `LEX-00122` | Çuz | Rana | animales |
| `LEX-00123` | Fxizx | Guacharaca | animales |
| `LEX-00124` | Ïç waç | Pato | animales |
| `LEX-00125` | Kaça | Cusumbo | animales |
| `LEX-00126` | Kalpaç | Garrapata | animales |
| `LEX-00127` | Kawa | Mariquita | animales |
| `LEX-00128` | Klaweçx | Lagartija | animales |
| `LEX-00129` | Lazx | Borugo | animales |
| `LEX-00130` | Meewëjx | Gallinazo | animales |
| `LEX-00131` | Mezuw | Avispa | animales |
| `LEX-00132` | Sa'te | Cucaracha | animales |
| `LEX-00133` | Sap | Sapo | animales |
| `LEX-00134` | Sikhwet | Libelula | animales |
| `LEX-00135` | Supil | Cienpies | animales |
| `LEX-00136` | Sxape | Babosa | animales |
| `LEX-00137` | Tüç | Chamon | animales |
| `LEX-00138` | Us miç | Alacran | animales |
| `LEX-00139` | Wäka | Cangrejo | animales |
| `LEX-00140` | Wënxinx | Comadreja | animales |
| `LEX-00141` | Yawee | Chicharra | animales |
| `LEX-00142` | Alum | Lobo | animales |
| `LEX-00143` | Äph | Zancudo | animales |
| `LEX-00144` | Atalx | Gallina | animales |
| `LEX-00145` | Atalx pihç | Gallo | animales |
| `LEX-00146` | Çiklxi | Tigre | animales |
| `LEX-00147` | Çxavx | Venado | animales |
| `LEX-00148` | Çxuçxa | Zarigueya | animales |
| `LEX-00149` | E'ç | Colibri | animales |
| `LEX-00150` | Ës | Piojo | animales |
| `LEX-00151` | Fxi'l | Codorniz | animales |
| `LEX-00152` | Fxiçh | Cuy | animales |
| `LEX-00153` | Jiba | Caballo | animales |
| `LEX-00154` | Kähpx | Conejo | animales |
| `LEX-00155` | Kapla | Cabra | animales |
| `LEX-00156` | Kdul | Condor | animales |
| `LEX-00157` | Kihçe | Murcielago | animales |
| `LEX-00158` | Klaa u'y | Vaca | animales |
| `LEX-00159` | Kupe | Buho | animales |
| `LEX-00160` | Lxuun | Leon | animales |
| `LEX-00161` | Miku | Mono | animales |
| `LEX-00162` | Misx | Gato | animales |
| `LEX-00163` | Nxu'px | Guatin | animales |
| `LEX-00164` | Pä'pa | Pulga | animales |
| `LEX-00165` | Pisxaa | Oveja | animales |
| `LEX-00166` | Sxa'wë | Lombriz | animales |
| `LEX-00167` | Sxita | Armadillo | animales |
| `LEX-00168` | Sxuma | Ardilla | animales |
| `LEX-00169` | Tub | Paloma | animales |
| `LEX-00170` | Tupa | Arana | animales |
| `LEX-00171` | Uh | Aguila | animales |
| `LEX-00172` | Ukh | Gusano | animales |
| `LEX-00173` | Uhze | Raton | animales |
| `LEX-00174` | Ul | Serpiente | animales |
| `LEX-00175` | Welx | Loro | animales |
| `LEX-00176` | Wez | Pez | animales |
| `LEX-00177` | Be'sx | Hermana | parentescos |
| `LEX-00178` | Çu’m | Cunado | parentescos |
| `LEX-00179` | Dçxikh | Hijo | parentescos |
| `LEX-00180` | Dxyuu | Esposa | parentescos |
| `LEX-00181` | Khaalu | Ahijado | parentescos |
| `LEX-00182` | Lula | Abuela | parentescos |
| `LEX-00183` | Nyiis | Hija | parentescos |
| `LEX-00184` | Peezx | Anciana | parentescos |
| `LEX-00185` | Talul | Abuelo | parentescos |
| `LEX-00186` | Tata | Papa | parentescos |
| `LEX-00187` | Uma | Mama | parentescos |
| `LEX-00188` | Ziiy | Hermano | parentescos |
| `LEX-00189` | Zun | Nieto o nieta | parentescos |
| `LEX-00190` | Babh | Hombro | cuerpo_humano |
| `LEX-00191` | Çikh | Cuello | cuerpo_humano |
| `LEX-00192` | Çukh | Cabeza | cuerpo_humano |
| `LEX-00193` | Çxida | Pie | cuerpo_humano |
| `LEX-00194` | Çxu'çx | Seno | cuerpo_humano |
| `LEX-00195` | Çxul | Pene | cuerpo_humano |
| `LEX-00196` | Ïçh | Nariz | cuerpo_humano |
| `LEX-00197` | Ikhwëth | Rodilla | cuerpo_humano |
| `LEX-00198` | Ji'be | Pierna | cuerpo_humano |
| `LEX-00199` | Kuse | Mano | cuerpo_humano |
| `LEX-00200` | Ku'ta | Brazo | cuerpo_humano |
| `LEX-00201` | Pëçh | Garganta | cuerpo_humano |
| `LEX-00202` | Pe'pe | Cerebro | cuerpo_humano |
| `LEX-00203` | Sxab | Ombligo | cuerpo_humano |
| `LEX-00204` | Thamee | Vagina | cuerpo_humano |
| `LEX-00205` | Thune | Lengua | cuerpo_humano |
| `LEX-00206` | Thü'wë | Oreja | cuerpo_humano |
| `LEX-00207` | Tuç | Barriga | cuerpo_humano |
| `LEX-00208` | Txi'th | Diente | cuerpo_humano |
| `LEX-00209` | Üus | Corazon | cuerpo_humano |
| `LEX-00210` | Yafx | Ojo | cuerpo_humano |
| `LEX-00211` | Yuwe | Boca | cuerpo_humano |
| `LEX-00212` | Zi't | Hueso | cuerpo_humano |
| `LEX-00213` | Zkhas | Cabello | cuerpo_humano |
| `LEX-00214` | Tlxi'ja | Uva silvestre | frutas_verduras |
| `LEX-00215` | Nxawnuu | Curuba | frutas_verduras |
| `LEX-00216` | Afx | Guama | frutas_verduras |
| `LEX-00217` | Akhus | Ajo | frutas_verduras |
| `LEX-00218` | Beçe | Mango | frutas_verduras |
| `LEX-00219` | Çxahu | Pina | frutas_verduras |
| `LEX-00220` | Fel | Uvas | frutas_verduras |
| `LEX-00221` | Knenxu iç | Banano | frutas_verduras |
| `LEX-00222` | Lasxnu | Durazno | frutas_verduras |
| `LEX-00223` | Lemnxun | Zapote | frutas_verduras |
| `LEX-00224` | Lxima | Naranja | frutas_verduras |
| `LEX-00225` | Lxima txhib | Limon | frutas_verduras |
| `LEX-00226` | Matku | Tomate | frutas_verduras |
| `LEX-00227` | Meem wala | Papaya | frutas_verduras |
| `LEX-00228` | Mulx | Chirimoya | frutas_verduras |
| `LEX-00229` | Mulx çuç | Guanabana | frutas_verduras |
| `LEX-00230` | Mutkwe | Lulo | frutas_verduras |
| `LEX-00231` | Nxun wahwa | Manzana | frutas_verduras |
| `LEX-00232` | Pçxid | Guayaba | frutas_verduras |
| `LEX-00233` | Snxuun | Mora | frutas_verduras |
| `LEX-00234` | Sxlal | Granadilla | frutas_verduras |
| `LEX-00235` | Sxulxkwe | Mandarina | frutas_verduras |
| `LEX-00236` | Uhçe | Aguacate | frutas_verduras |
| `LEX-00237` | Yawnu | Maracuya | frutas_verduras |
| `LEX-00238` | Bakhis | Poleo | plantas_medicinales |
| `LEX-00239` | Bu’çx | Botoncillo | plantas_medicinales |
| `LEX-00240` | Çba'w | Barbasco | plantas_medicinales |
| `LEX-00241` | Eçx äwä ziç | Yerba mora | plantas_medicinales |
| `LEX-00242` | Luuta | Ruda | plantas_medicinales |
| `LEX-00243` | Neklu | Tomillo | plantas_medicinales |
| `LEX-00244` | Pçxaga | Escoba | plantas_medicinales |
| `LEX-00245` | Pisxaa jxuth | Yerba chivo | plantas_medicinales |
| `LEX-00246` | Pisxaa thune | Yerba golpe | plantas_medicinales |
| `LEX-00247` | Wëhnx | Tabaco | plantas_medicinales |
| `LEX-00248` | Paiku | Paico | plantas_medicinales |
| `LEX-00249` | Klathune | Lengua de vaca | plantas_medicinales |
| `LEX-00250` | Bahç na’na | Aloe vera | plantas_medicinales |
| `LEX-00251` | Belwëna | Verbena | plantas_medicinales |
| `LEX-00252` | Çxayu’ç | Alegria | plantas_medicinales |
| `LEX-00253` | Ësx | Coca | plantas_medicinales |
| `LEX-00254` | Khäas | Ortiga | plantas_medicinales |
| `LEX-00255` | Khäas beh | Ortiga roja | plantas_medicinales |
| `LEX-00256` | Pataathxä’ | Yerbabuena | plantas_medicinales |
| `LEX-00257` | Taph | Chilca | plantas_medicinales |
| `LEX-00258` | Alpes | Arveja | alimentos |
| `LEX-00259` | Ape | Zapallo | alimentos |
| `LEX-00260` | Ä's | Arracacha | alimentos |
| `LEX-00261` | Beka | Chicha | alimentos |
| `LEX-00262` | Çuth | Choclo | alimentos |
| `LEX-00263` | Çxiçx | Carne | alimentos |
| `LEX-00264` | Ee phewusa | Remolacha | alimentos |
| `LEX-00265` | Ka'ka | Papa | alimentos |
| `LEX-00266` | Kbiiçx | Caigua | alimentos |
| `LEX-00267` | Khasx | Sopa | alimentos |
| `LEX-00268` | Klayuta | Cidra | alimentos |
| `LEX-00269` | Kulxis | Coles | alimentos |
| `LEX-00270` | Kusxa | Sancocho | alimentos |
| `LEX-00271` | Kutxh | Maiz | alimentos |
| `LEX-00272` | Me'su | Cilantro | alimentos |
| `LEX-00273` | Muçi | Mote | alimentos |
| `LEX-00274` | Nxa | Yuca | alimentos |
| `LEX-00275` | Plad | Platano | alimentos |
| `LEX-00276` | Spulxa | Cebolla | alimentos |
| `LEX-00277` | Sxwil | Ollucos | alimentos |
| `LEX-00278` | Txit | Mani | alimentos |
| `LEX-00279` | Us | Frijol | alimentos |
| `LEX-00280` | Uswal | Chachafruto | alimentos |
| `LEX-00281` | Am | Hacha | herramientas |
| `LEX-00282` | Çaam a'bat | Barra | herramientas |
| `LEX-00283` | Çaam çxa'bwïkh | Pica | herramientas |
| `LEX-00284` | Çaam pçxuuk | Azadon | herramientas |
| `LEX-00285` | Çaam spethsa | Alicate | herramientas |
| `LEX-00286` | Çaam su’yakh | Barreton | herramientas |
| `LEX-00287` | Çaam txiwe pubwa' | Carretilla | herramientas |
| `LEX-00288` | Çaam zihkh twakwa' | Motosierra | herramientas |
| `LEX-00289` | Çxilx wala | Machete | herramientas |
| `LEX-00290` | Eç spethwa' | Deshojador | herramientas |
| `LEX-00291` | Kafxi'jsa | Ahoyador | herramientas |
| `LEX-00292` | Kuvx | Flauta | herramientas |
| `LEX-00293` | Kuvx musx | Zampona | herramientas |
| `LEX-00294` | Kweth | Tambor | herramientas |
| `LEX-00295` | Tala | Guitarra | herramientas |
| `LEX-00296` | Uka çaam | Martillo | herramientas |
| `LEX-00297` | Yu' wëzxwa' | Manguera | herramientas |
| `LEX-00298` | Äçthe | Cernidor | utiles_hogar |
| `LEX-00299` | Ah | Humo | utiles_hogar |
| `LEX-00300` | Akh | Trampa | utiles_hogar |
| `LEX-00301` | Biçx | Plato | utiles_hogar |
| `LEX-00302` | Çaam miç ahwa | Estufa | utiles_hogar |
| `LEX-00303` | Çxa'y | Vaso | utiles_hogar |
| `LEX-00304` | Çxilx | Cuchillo | utiles_hogar |
| `LEX-00305` | Ejwa | Cucharona | utiles_hogar |
| `LEX-00306` | Ipx kat | Fogon | utiles_hogar |
| `LEX-00307` | Kpuun | Jabon | utiles_hogar |
| `LEX-00308` | Lxeta | Olleta | utiles_hogar |
| `LEX-00309` | Miç | Olla | utiles_hogar |
| `LEX-00310` | Pewnxi | Ducha | utiles_hogar |
| `LEX-00311` | Thegnxi | Espejo | utiles_hogar |
| `LEX-00312` | Tuçxa'y | Cuchara | utiles_hogar |
| `LEX-00313` | Txid | Peine | utiles_hogar |
| `LEX-00314` | Üçxhwa | Bano o inodoro | utiles_hogar |
| `LEX-00315` | Wawa | Algodon | utiles_hogar |
| `LEX-00316` | Açxha | Arbol caucho | ambientales |
| `LEX-00317` | Buçe | Yarumo | ambientales |
| `LEX-00318` | Çhï'te | Arrayan | ambientales |
| `LEX-00319` | Çü'ph | Chusque | ambientales |
| `LEX-00320` | Çxped | Chonta | ambientales |
| `LEX-00321` | Kwetufx | Arbol de cera | ambientales |
| `LEX-00322` | Pizx | Roble | ambientales |
| `LEX-00323` | Çaam | Metal o hierro | ambientales |
| `LEX-00324` | Çhïçh | Paja | ambientales |
| `LEX-00325` | Çxä'px | Rama | ambientales |
| `LEX-00326` | Ëekhthe'j | Trueno | ambientales |
| `LEX-00327` | Ejx | Derrumbe | ambientales |
| `LEX-00328` | Ipx | Fuego | ambientales |
| `LEX-00329` | Kweth | Piedra | ambientales |
| `LEX-00330` | Kxthüus | Arcoiris | ambientales |
| `LEX-00331` | Muse | Arena | ambientales |
| `LEX-00332` | Nus | Lluvia | ambientales |
| `LEX-00333` | Nxaz | Nevado | ambientales |
| `LEX-00334` | Täph | Nube | ambientales |
| `LEX-00335` | Tasx | Planta | ambientales |
| `LEX-00336` | Thä' | Cerro | ambientales |
| `LEX-00337` | Txite | Flor | ambientales |
| `LEX-00338` | Txiwe | Tierra organica | ambientales |
| `LEX-00339` | Wejxa | Viento | ambientales |
| `LEX-00340` | Yu' | Agua | ambientales |
| `LEX-00341` | A' | Estrella | astros |
| `LEX-00342` | A'te | Luna | astros |
| `LEX-00343` | Ëewë | Cometa | astros |
| `LEX-00344` | Sek | Sol | astros |
| `LEX-00345` | Uma Txiwe | Planeta Tierra | astros |
| `LEX-00346` | Aç thetnxi | Lavadero de ropa | muebles_inmuebles |
| `LEX-00347` | Atüu | Cama | muebles_inmuebles |
| `LEX-00348` | Belx sxawwa' | Ropero | muebles_inmuebles |
| `LEX-00349` | Kçina | Cocina | muebles_inmuebles |
| `LEX-00350` | Nxuhne | Sala | muebles_inmuebles |
| `LEX-00351` | Paatap | Mesa | muebles_inmuebles |
| `LEX-00352` | Pagu | Silla | muebles_inmuebles |
| `LEX-00353` | Tel | Trapiche | muebles_inmuebles |
| `LEX-00354` | Tul | Huerta | muebles_inmuebles |
| `LEX-00355` | Vxiç | Puerta | muebles_inmuebles |
| `LEX-00356` | Vxyuu | Dinero | muebles_inmuebles |
| `LEX-00357` | Weh | Puente | muebles_inmuebles |
| `LEX-00358` | Yat | Casa | muebles_inmuebles |
| `LEX-00359` | Yat wa' | Choza | muebles_inmuebles |
| `LEX-00360` | Yat yafx | Ventana | muebles_inmuebles |
| `LEX-00361` | Khlxana | Juliana | nombres_propios |
| `LEX-00362` | Khwen | Juan | nombres_propios |
| `LEX-00363` | Khwena | Juana | nombres_propios |
| `LEX-00364` | Ksee | Jose | nombres_propios |
| `LEX-00365` | Ksepa | Josefa | nombres_propios |
| `LEX-00366` | Ksus | Jesus | nombres_propios |
| `LEX-00367` | Lasku | Francisco | nombres_propios |
| `LEX-00368` | Lxika | Enriqueta | nombres_propios |
| `LEX-00369` | Lxiki | Enrique | nombres_propios |
| `LEX-00370` | Mlxilx | Maria | nombres_propios |
| `LEX-00371` | Nwel | Manuel | nombres_propios |
| `LEX-00372` | Peklu | Pedro | nombres_propios |
| `LEX-00373` | Saphela | Isabela | nombres_propios |
| `LEX-00374` | Sila | Cecilia | nombres_propios |
| `LEX-00375` | Siska | Francisca | nombres_propios |
| `LEX-00376` | Til | Otilia | nombres_propios |
| `LEX-00377` | Tmigu | Domingo | nombres_propios |
| `LEX-00378` | Txin | Martin | nombres_propios |
| `LEX-00379` | Txina | Martina | nombres_propios |
| `LEX-00380` | Wel | Abel | nombres_propios |
| `LEXR-00381` | -pcachja’ | mientras, durante... | diccionario_general |
| `LEXR-00382` | a’ch | el carrete de barro para asentar olla | diccionario_general |
| `LEXR-00383` | atũ | la barbacoa (cama hecha de palos) | diccionario_general |
| `LEXR-00384` | aw-, awu- | echar (líquido) | diccionario_general |
| `LEXR-00385` | bagachva, bagachteva | cuandoquiera, siempre | diccionario_general |
| `LEXR-00386` | bats wes | guasca de fique | diccionario_general |
| `LEXR-00387` | beca ñusha | chicha dulce de maíz | diccionario_general |
| `LEXR-00388` | ca’ga | la papa | diccionario_general |
| `LEXR-00389` | caapi’qui’j-, caapiqui’ji- | dejar acompañar, permitir acompañar | diccionario_general |
| `LEXR-00390` | caapuutsu’j-, caapuutsu’ju- | mandar alimentar | diccionario_general |
| `LEXR-00391` | caayaqui’j-, caayaqui’ji- | hacer recordar | diccionario_general |
| `LEXR-00392` | camb-, cambu- | quemar | diccionario_general |
| `LEXR-00393` | cambuumbu-(cambu´mbu-) | quemar repetidas veces | diccionario_general |
| `LEXR-00394` | cash | ralo (tejido) | diccionario_general |
| `LEXR-00395` | cdeeje’j-, cdeeje’je- | 1. adormecer, causar sueño 2. acostar | diccionario_general |
| `LEXR-00396` | chang | el escoplo (herramienta) | diccionario_general |
| `LEXR-00397` | chica-, chicáa- | gorgojearse | diccionario_general |
| `LEXR-00398` | chictu’j | (especie de árbol) | diccionario_general |
| `LEXR-00399` | cjalu | el ahijado | diccionario_general |
| `LEXR-00400` | csha’w-, csha’wu- | soñar | diccionario_general |
| `LEXR-00401` | csuusu’j-, csuusu’ju- | 1. hacer sonar (un instrumento) 2. crujir los dientes 3. alborotar | diccionario_general |
| `LEXR-00402` | ctu’fi’j-, ctu’fi’ji- | hacer eructar | diccionario_general |
| `LEXR-00403` | cu’j-, cu’ju- | bailar | diccionario_general |
| `LEXR-00404` | cuch we’we- | molestar (hablando), estorbar | diccionario_general |
| `LEXR-00405` | cuw-, cuwúu- | formar tumor o chupo | diccionario_general |
| `LEXR-00406` | cvis-, cvisu- | provocar, atacar, azuzar | diccionario_general |
| `LEXR-00407` | cytem-, cytemúu- | apretar | diccionario_general |
| `LEXR-00408` | cytũus chijme | arco de noche | diccionario_general |
| `LEXR-00409` | cyuupjni | el corral | diccionario_general |
| `LEXR-00410` | denzh | dormilón | diccionario_general |
| `LEXR-00411` | ee watse | vena | diccionario_general |
| `LEXR-00412` | fytũu pitscue | (especie de planta medicinal) | diccionario_general |
| `LEXR-00413` | fĩchja- | apagar | diccionario_general |
| `LEXR-00414` | iiméj wala | inmenso | diccionario_general |
| `LEXR-00415` | iipuii yuu- | enemistarse, hacerse enemigos | diccionario_general |
| `LEXR-00416` | jyca | allí | diccionario_general |
| `LEXR-00417` | jytjãassa | persona que desea algo | diccionario_general |
| `LEXR-00418` | jyu’j | lejos, largo, alto | diccionario_general |
| `LEXR-00419` | jyutj (jyũtj) | la hierba, maleza | diccionario_general |
| `LEXR-00420` | lech-, lechíi- | hacer cosquillas | diccionario_general |
| `LEXR-00421` | leepja’- | voltear para abajo | diccionario_general |
| `LEXR-00422` | ma’wẽn | cuando, ¿cuándo?, ¿a qué horas? | diccionario_general |
| `LEXR-00423` | masu | el mazo | diccionario_general |
| `LEXR-00424` | me’sucue | el culantro (planta) | diccionario_general |
| `LEXR-00425` | meshish | el hongo (planta) | diccionario_general |
| `LEXR-00426` | micu | el mono, mico (mamífero) | diccionario_general |
| `LEXR-00427` | mil | la miel, guerapo de caña sin fermentar | diccionario_general |
| `LEXR-00428` | mtee (mdee T) | donde, adonde, ¿dónde? ¿adónde? | diccionario_general |
| `LEXR-00429` | nuucy-, nuuqui- | 1. pegarse a 2. asociarse con | diccionario_general |
| `LEXR-00430` | nuyi’j- | llevar, guiar, encaminar | diccionario_general |
| `LEXR-00431` | nuyjyu’ja- | alargar | diccionario_general |
| `LEXR-00432` | paana-, paanáa- | negar, ocultar | diccionario_general |
| `LEXR-00433` | paapeeygãj-, paapeeygãja- | compartir el sufrimiento de otro | diccionario_general |
| `LEXR-00434` | paayũs-, paayũsu- | compartir tristeza de otro | diccionario_general |
| `LEXR-00435` | pachpach | con las uñas, garras | diccionario_general |
| `LEXR-00436` | pal | el cura, sacerdote | diccionario_general |
| `LEXR-00437` | paypwesa | juguetón | diccionario_general |
| `LEXR-00438` | pcyuusa | verdugo | diccionario_general |
| `LEXR-00439` | peendu’j-, peendu’ju- | hacer rayas, pintar | diccionario_general |
| `LEXR-00440` | peeyũcue | tía (hermana de la mamá) | diccionario_general |
| `LEXR-00441` | plavi’j-, plavi’ji- | frotar, alisar | diccionario_general |
| `LEXR-00442` | pteenz | angosto, estecho | diccionario_general |
| `LEXR-00443` | pu’quis-, pu’quisu- | alzar | diccionario_general |
| `LEXR-00444` | pucacje ntsu’m | esposo de la prima | diccionario_general |
| `LEXR-00445` | pumba’jni | cámara lateral para entierro | diccionario_general |
| `LEXR-00446` | puuty ya’ptjãawe- | agredirse (mutuamente) | diccionario_general |
| `LEXR-00447` | quiwe pwa’ | hueco | diccionario_general |
| `LEXR-00448` | quiwe yase | apellido | diccionario_general |
| `LEXR-00449` | sec cãjatste | al salir el sol | diccionario_general |
| `LEXR-00450` | sendy-, sendyi- | ser mezquino | diccionario_general |
| `LEXR-00451` | shquitya-, shquityáa- | añadir, pegar con goma | diccionario_general |
| `LEXR-00452` | spẽ’tje’tj-, spẽ’tje’tje- | corar (varias cosas) | diccionario_general |
| `LEXR-00453` | taqui’ni tumb | torcaz domesticado | diccionario_general |
| `LEXR-00454` | tsam upj | cerca de alambre | diccionario_general |
| `LEXR-00455` | tsunz | el sapo pequeño | diccionario_general |
| `LEXR-00456` | tutu’tu- | canturrear | diccionario_general |
| `LEXR-00457` | tuutje’j-, tuutje’je- | divulgar | diccionario_general |
| `LEXR-00458` | tyaasa | que edifica | diccionario_general |
| `LEXR-00459` | tyachmée | reciente, hace poco | diccionario_general |
| `LEXR-00460` | tyity amb- | embarrar | diccionario_general |
| `LEXR-00461` | tyute-, tyutẽe- | separarse, alejarse, apartarse | diccionario_general |
| `LEXR-00462` | tyãawe’sh (cyãawe’sh) | su (de ellos, de ellas) | diccionario_general |
| `LEXR-00463` | undende- | cosechar | diccionario_general |
| `LEXR-00464` | unza wala | rata | diccionario_general |
| `LEXR-00465` | viina’ | callado | diccionario_general |
| `LEXR-00466` | waacji’cji’j- | pisotear (repetidas veces) | diccionario_general |
| `LEXR-00467` | wagas yuwe | el idioma castellano, español | diccionario_general |
| `LEXR-00468` | wasacuẽ (wesacuẽ) | la muchacha | diccionario_general |
| `LEXR-00469` | wete-, wetée- | caer | diccionario_general |
| `LEXR-00470` | ya’cpajcy-, ya’cpaqui- | dejarse alcanzar | diccionario_general |
| `LEXR-00471` | ya’ptjãawe- | ser agredido | diccionario_general |
| `LEXR-00472` | yu’cj nasa | el guerrillero | diccionario_general |
| `LEXR-00473` | yu’cj tumb | torcaz silvestre | diccionario_general |
| `LEXR-00474` | yẽepyãj-, yẽepyãja- | demorar (hasta mediodía) | diccionario_general |
| `LEXR-00475` | zuna’j-, zuna’ja- | apretar | diccionario_general |
| `LEXR-00476` | ñucue | el tío (hermano del papá) | diccionario_general |
| `LEXR-00477` | ñusñus | muy triste | diccionario_general |
| `LEXR-00478` | ĩtyĩ fi’nzewa’j | la vida (futura) | diccionario_general |
| `LEXR-00479` | ũ’sa | que come, comensal | diccionario_general |
| `LEXR-00480` | ẽsh | coca | diccionario_general |
| `LEXR-00481` | -pcach | hasta | diccionario_general |
| `LEXR-00482` | bajch-, bachi- | calentarse | diccionario_general |
| `LEXR-00483` | bejbej | orange | diccionario_general |
| `LEXR-00484` | caaiviitu’j-, caaiviitu’ju- | permitir destruir | diccionario_general |
| `LEXR-00485` | caame | avío (comida para el camino) | diccionario_general |
| `LEXR-00486` | caatywete’j-, caatywete’je- | mandar soltar, hacer suspender (un trabajo) | diccionario_general |
| `LEXR-00487` | cbaji’j-, cbaji’ji- | calentar | diccionario_general |
| `LEXR-00488` | cchill wala (chill wala) | peinilla | diccionario_general |
| `LEXR-00489` | cfindúu- | poner vara a lo largo | diccionario_general |
| `LEXR-00490` | chavy-, chavi- | dar un paso | diccionario_general |
| `LEXR-00491` | chjãchja- | mejorarse, recuperarse, fortalecerse, arreciar (lluvia) | diccionario_general |
| `LEXR-00492` | chu’nzhu | el cordón, látigo | diccionario_general |
| `LEXR-00493` | chuuma’ma- | enmohecerse | diccionario_general |
| `LEXR-00494` | chĩ’ch | torcaz pequeña (ave) | diccionario_general |
| `LEXR-00495` | cja’tyinde- | desprender | diccionario_general |
| `LEXR-00496` | cjas ujnde- | desplumar | diccionario_general |
| `LEXR-00497` | cjã’sh le’ch | grillo | diccionario_general |
| `LEXR-00498` | cpu’quitje’j-, cpu’quitjej’e- | hacer firme, apuntalar | diccionario_general |
| `LEXR-00499` | cuutsje’je’j-, cuutsje’je’je- | tocar repetidas veces con algo | diccionario_general |
| `LEXR-00500` | cyaatsqui’pu’j-, cyaatsqui’pu’ju- | hacer arrear | diccionario_general |
| `LEXR-00501` | cyterraj | unidos | diccionario_general |
| `LEXR-00502` | cyulmée | no en vano | diccionario_general |
| `LEXR-00503` | cyuy | por allí (a través) | diccionario_general |
| `LEXR-00504` | daaquí | Andaquí (indígena de la tribu Andaquí) | diccionario_general |
| `LEXR-00505` | een, eena’ | atento | diccionario_general |
| `LEXR-00506` | etse yuu | hacer frío | diccionario_general |
| `LEXR-00507` | fi’nze- | vivir, pasar el día | diccionario_general |
| `LEXR-00508` | fytũu | palo madera | diccionario_general |
| `LEXR-00509` | isni | el vestido (de mujer) | diccionario_general |
| `LEXR-00510` | ji’pjsa yuu- | enriquecerse, ser rico | diccionario_general |
| `LEXR-00511` | jimba cuse vyllill | casco (del caballo) | diccionario_general |
| `LEXR-00512` | jimba ji’mbe | anca | diccionario_general |
| `LEXR-00513` | jypa’yajcy-jypa’yaqui | tener cuidado | diccionario_general |
| `LEXR-00514` | jypunzani | terciado | diccionario_general |
| `LEXR-00515` | jyzuunz-, jyzuunzu- | estirarse | diccionario_general |
| `LEXR-00516` | mityj | la olla | diccionario_general |
| `LEXR-00517` | mityj um- | fabricar vasijas de barro | diccionario_general |
| `LEXR-00518` | much-, muchi- | acortar, caerse el pelo | diccionario_general |
| `LEXR-00519` | mutsu- | formar chupo (tumor) | diccionario_general |
| `LEXR-00520` | nenga cjash | mazamorra con sal, sanco | diccionario_general |
| `LEXR-00521` | nwe’sh | el pariente (de la misma raza) | diccionario_general |
| `LEXR-00522` | pa’cj-, pa’cje- (pã’cj- T) | remendar | diccionario_general |
| `LEXR-00523` | paaũ’ne- | compartir el llanto de otro | diccionario_general |
| `LEXR-00524` | pangu | banca (para sentarse) | diccionario_general |
| `LEXR-00525` | pcjaacjeni | reunión | diccionario_general |
| `LEXR-00526` | peefynicy-, peefyniqui- | trasladar, transtear | diccionario_general |
| `LEXR-00527` | pjeu’j-, pjeu’ju- | arreglar | diccionario_general |
| `LEXR-00528` | pshũu | la sombra | diccionario_general |
| `LEXR-00529` | ptyi’nsa | cuñada con cuñada | diccionario_general |
| `LEXR-00530` | pume-, pumée- | tender, extender | diccionario_general |
| `LEXR-00531` | puuty pdyi’p | cara a cara | diccionario_general |
| `LEXR-00532` | pã’cj | la semilla que vuelve a dar después de acosechado, sarapanga | diccionario_general |
| `LEXR-00533` | pã’pã | la pulga (insecto) | diccionario_general |
| `LEXR-00534` | pẽty shiwa | el coto, bocio | diccionario_general |
| `LEXR-00535` | scuela luuch | alumno de la escuela | diccionario_general |
| `LEXR-00536` | shbu | el uvillo (fruta silvestre comestible) | diccionario_general |
| `LEXR-00537` | shã’we yaj | bejuco | diccionario_general |
| `LEXR-00538` | shã’we yu’tse | la lombricera, el vermífugo | diccionario_general |
| `LEXR-00539` | shũu | simple, soso | diccionario_general |
| `LEXR-00540` | shũucjash | mazamorra sin sal | diccionario_general |
| `LEXR-00541` | spaatu | el zapato | diccionario_general |
| `LEXR-00542` | spund-, spundúu- | torcer (hilo o guasca) | diccionario_general |
| `LEXR-00543` | su’s | la orina | diccionario_general |
| `LEXR-00544` | tandy-. tandyíi- | dar vuelta, girar | diccionario_general |
| `LEXR-00545` | tata | el padre, papá | diccionario_general |
| `LEXR-00546` | tecj | tres | diccionario_general |
| `LEXR-00547` | tee cu’ta | una brazada | diccionario_general |
| `LEXR-00548` | tsep-, tsepúu- | aplastar | diccionario_general |
| `LEXR-00549` | tsundefy | el martingalvis (árbol) | diccionario_general |
| `LEXR-00550` | tswend-, tswendúu- | torcer, retorcer | diccionario_general |
| `LEXR-00551` | tsũ’ta’j-, tsũ’ta’ja- | trenzar | diccionario_general |
| `LEXR-00552` | tsũvy | el dormilón (ave nocturna) | diccionario_general |
| `LEXR-00553` | tu’cu- | inflamarse | diccionario_general |
| `LEXR-00554` | tumb chujme | la paloma (ave) | diccionario_general |
| `LEXR-00555` | tund | ligero, aprisa | diccionario_general |
| `LEXR-00556` | twĩi- | zumbar | diccionario_general |
| `LEXR-00557` | tyca | ahí | diccionario_general |
| `LEXR-00558` | tyãawe’sh (cyãawe’sh) | ellos, ellas, aquellos, aquellas | diccionario_general |
| `LEXR-00559` | ujndy | seco | diccionario_general |
| `LEXR-00560` | ultũpy | el ciempiés | diccionario_general |
| `LEXR-00561` | umnisa | tejido | diccionario_general |
| `LEXR-00562` | vyu | el dinero, la plata, moneda | diccionario_general |
| `LEXR-00563` | wa’ta’j-, wa’ta’ja- | ensillar | diccionario_general |
| `LEXR-00564` | wala | grande, alto | diccionario_general |
| `LEXR-00565` | we’pe | el páramo (terreno desierto, elevado y sin vegetación) | diccionario_general |
| `LEXR-00566` | we’tj | la lanza | diccionario_general |
| `LEXR-00567` | wejy | más (comparativo) | diccionario_general |
| `LEXR-00568` | wenzhi’nzhi- | halar (repetidas veces) | diccionario_general |
| `LEXR-00569` | ya’ndu- | enredarse | diccionario_general |
| `LEXR-00570` | yaatu’j-, yaatu’ju- | hacer casa | diccionario_general |
| `LEXR-00571` | yuju- | pararse, ponerse de pie | diccionario_general |
| `LEXR-00572` | yunda | el pajonal | diccionario_general |
| `LEXR-00573` | yũuna- | ayunar | diccionario_general |
| `LEXR-00574` | ãjsa | poderoso, capaz | diccionario_general |
| `LEXR-00575` | ñutyji- | moquear | diccionario_general |
| `LEXR-00576` | ũchja- | apagarse | diccionario_general |
| `LEXR-00577` | ũsni, ũswa’j | lugar habitual, morada | diccionario_general |
| `LEXR-00578` | ẽsẽe- | aligerar | diccionario_general |
| `LEXR-00579` | -dyiji- | casi | diccionario_general |
| `LEXR-00580` | -pcachte | en vez... | diccionario_general |
| `LEXR-00581` | -su | por | diccionario_general |
| `LEXR-00582` | a’tsja- | cernir, cerner, colar | diccionario_general |
| `LEXR-00583` | bats ets | penca de cabuya | diccionario_general |
| `LEXR-00584` | ca’jem (ca’jyam) | trenza | diccionario_general |
| `LEXR-00585` | caapaatje’j-, caapaatje’je- | hacer aparar | diccionario_general |
| `LEXR-00586` | caatje’j-, caatje’je- | hacer vestir | diccionario_general |
| `LEXR-00587` | caycjẽj-, caycjẽ´jẽ- | hacer tragar | diccionario_general |
| `LEXR-00588` | chji’ndy | la abeja (insecto) | diccionario_general |
| `LEXR-00589` | cjashi’j-, cjashi’ji- | hacer mazamorra | diccionario_general |
| `LEXR-00590` | cjastjẽ’j | lanudo | diccionario_general |
| `LEXR-00591` | cjicji’cji’j | reflejar, centellear | diccionario_general |
| `LEXR-00592` | cjĩij ej | el cañaduzal | diccionario_general |
| `LEXR-00593` | cjũchcjũchdyi’ | pardo | diccionario_general |
| `LEXR-00594` | cna’sa | la jovencita, señorita | diccionario_general |
| `LEXR-00595` | cupe | búho | diccionario_general |
| `LEXR-00596` | cutyj viits | flor de maíz | diccionario_general |
| `LEXR-00597` | cãapa’j-, cãapa’ja- | hacer estallar, detonar | diccionario_general |
| `LEXR-00598` | dej-, deje-, dee- | dormir, acostarse | diccionario_general |
| `LEXR-00599` | dundte, dundtey | rápidamenta | diccionario_general |
| `LEXR-00600` | e’tscuẽ | colibrí, esmeralda | diccionario_general |
| `LEXR-00601` | fi’l | perdiz | diccionario_general |
| `LEXR-00602` | fi’nze- | atardecer | diccionario_general |
| `LEXR-00603` | finze | frío | diccionario_general |
| `LEXR-00604` | iipa’j- | llegar (visitar dos lugares en el mismo viaje) | diccionario_general |
| `LEXR-00605` | iisa | cada | diccionario_general |
| `LEXR-00606` | iiwejndy-, iiweendyi- | ser amado, quererse recíprocamente | diccionario_general |
| `LEXR-00607` | isa- | ensayar, probar, tratar de | diccionario_general |
| `LEXR-00608` | jimba pembée- | relinchar | diccionario_general |
| `LEXR-00609` | jycja’cunde- | descargarse, librarse de | diccionario_general |
| `LEXR-00610` | le’le | húmedo | diccionario_general |
| `LEXR-00611` | lusiu | rucio | diccionario_general |
| `LEXR-00612` | mteeva | dondequiera | diccionario_general |
| `LEXR-00613` | muse | la arena | diccionario_general |
| `LEXR-00614` | mẽ’cjwe | ¡Muélalo! | diccionario_general |
| `LEXR-00615` | nasa dyi’j | vereda | diccionario_general |
| `LEXR-00616` | nasa ji’pj- | estar embarazada, encinta | diccionario_general |
| `LEXR-00617` | neeúu- | echar fuera, ahuyentar | diccionario_general |
| `LEXR-00618` | ntsu’m | el cuñado (entre hombres) | diccionario_general |
| `LEXR-00619` | nuycũj-, nuycũju- | traer (llegando a un lugar) | diccionario_general |
| `LEXR-00620` | pa’ga yuu- | ponerse caro | diccionario_general |
| `LEXR-00621` | paandeesa | huésped | diccionario_general |
| `LEXR-00622` | paanducj-, paanducje- | entregar voluntariamente | diccionario_general |
| `LEXR-00623` | paauu- | morir en lugar de otro | diccionario_general |
| `LEXR-00624` | paaũcjweete | timidez | diccionario_general |
| `LEXR-00625` | pach-, pachíi- | rasguñar, arañar, coger con las uñas | diccionario_general |
| `LEXR-00626` | pandende- | quitar varias cosas | diccionario_general |
| `LEXR-00627` | peecy | por sí mismo, uno mismo, propio | diccionario_general |
| `LEXR-00628` | pel-, pelu- | enrollar | diccionario_general |
| `LEXR-00629` | pembe-, pembée- | 1. gemir, gritar (de dolor) 2. mugir (vaca); 3. chillar; 4. relinchar (caballo), 5. cacarear (gallina), 6. maullar (gato) | diccionario_general |
| `LEXR-00630` | pi’qui | el compañero, la compañera | diccionario_general |
| `LEXR-00631` | pjay | chistoso | diccionario_general |
| `LEXR-00632` | pquipja | boca abajo | diccionario_general |
| `LEXR-00633` | puuty ya’pu’ch-, puuty ya’pu’chji- | ayudarse (mutuamente) | diccionario_general |
| `LEXR-00634` | pyacj | hermano con hermano, o hermana con hermana | diccionario_general |
| `LEXR-00635` | sec cjẽeni | el poniente, oeste, occidente | diccionario_general |
| `LEXR-00636` | sec cãani | el oriente, este | diccionario_general |
| `LEXR-00637` | seelpisa | útil | diccionario_general |
| `LEXR-00638` | shuma | ardilla | diccionario_general |
| `LEXR-00639` | shuuna’ u’p- | estar callado, guardar silencio | diccionario_general |
| `LEXR-00640` | shwende-, shwendúu- | menear, revolver | diccionario_general |
| `LEXR-00641` | sla’tyi- | resbalar | diccionario_general |
| `LEXR-00642` | spat-spate | parcialmente encogido (las piernas) | diccionario_general |
| `LEXR-00643` | stendende- | rasgar, romper (varias cosas) | diccionario_general |
| `LEXR-00644` | sũupi’j-, sũupi’ji- | 1. desyerbar, limpiar maleza; 2. desnudar, desvestir | diccionario_general |
| `LEXR-00645` | teechsa na’wẽrraj | por igual | diccionario_general |
| `LEXR-00646` | tjune vits | punta de la lengua | diccionario_general |
| `LEXR-00647` | tjẽysa | dificultad | diccionario_general |
| `LEXR-00648` | tjẽyte ũs- | estar ocupado | diccionario_general |
| `LEXR-00649` | tsall-, tsalli- | aclarar, volverse claro (líquido) | diccionario_general |
| `LEXR-00650` | tutje- | crear fama | diccionario_general |
| `LEXR-00651` | tutu- | embotarse | diccionario_general |
| `LEXR-00652` | tuya | preñada, enrazada (animales) | diccionario_general |
| `LEXR-00653` | tyacjji- | demorar (poco tiempo) | diccionario_general |
| `LEXR-00654` | tyjityjni | escogido | diccionario_general |
| `LEXR-00655` | u’se | nuevo | diccionario_general |
| `LEXR-00656` | ujcha-, ucha- | rajarse, partirse | diccionario_general |
| `LEXR-00657` | ul | bobo, tímido | diccionario_general |
| `LEXR-00658` | undund- | quebrar (varias cosas) | diccionario_general |
| `LEXR-00659` | upeepe- | quebrarse (varias cosas) | diccionario_general |
| `LEXR-00660` | we’wewe- | murmurar | diccionario_general |
| `LEXR-00661` | wes | la guasca, cuerda, soga, piola | diccionario_general |
| `LEXR-00662` | wãatãj-, wãatãja-, wãatãa- | botar, tirar | diccionario_general |
| `LEXR-00663` | wãca | el cangrejo (crustáceo) | diccionario_general |
| `LEXR-00664` | ya’yuu- | acontecer, suceder | diccionario_general |
| `LEXR-00665` | yu’cj tumb | torcaz del monte (ave) | diccionario_general |
| `LEXR-00666` | yu’cãchã | el caudal, corriente del rió | diccionario_general |
| `LEXR-00667` | yu’tse | el remedio, medicina | diccionario_general |
| `LEXR-00668` | yuwe quiis- | levantar chismes | diccionario_general |
| `LEXR-00669` | ãchgawe’sh | esta generación, contemporáneos | diccionario_general |
| `LEXR-00670` | ãjmeesa, ãjmeecuẽsa | indigino, deficiente | diccionario_general |
| `LEXR-00671` | ñusha mil | miel de caña | diccionario_general |
| `LEXR-00672` | ũuchi- | disminuir | diccionario_general |
| `LEXR-00673` | ũucj-, ũucju- | temer, tener miedo, asustarse | diccionario_general |
| `LEXR-00674` | ũusutje- | recordar | diccionario_general |
| `LEXR-00675` | ẽe piishá | nubes dispersas | diccionario_general |
| `LEXR-00676` | a’tyji’j-, a’tyji’ji- | estornudar | diccionario_general |
| `LEXR-00677` | atseyajcy- | despreciar | diccionario_general |
| `LEXR-00678` | buc-, bucu- | estar panzón | diccionario_general |
| `LEXR-00679` | caata’ngu’j-, caata’ngu’ju-(cta’ngu’j-) | hacer dar vuelta | diccionario_general |
| `LEXR-00680` | cacanaajũ | acá arriba | diccionario_general |
| `LEXR-00681` | canuwé | la canoa (artesa para la chicha) | diccionario_general |
| `LEXR-00682` | cduucje’j-, cduucje’je- | hacer entregar | diccionario_general |
| `LEXR-00683` | chalún | chicharrón | diccionario_general |
| `LEXR-00684` | chcate- | fracturar hueso | diccionario_general |
| `LEXR-00685` | chica | el gorgojo (insecto) | diccionario_general |
| `LEXR-00686` | chjamb | el caserío, pueblo, poblado | diccionario_general |
| `LEXR-00687` | chjã’py | la horqueta | diccionario_general |
| `LEXR-00688` | chu’ch tyujnde- | destetar | diccionario_general |
| `LEXR-00689` | cja’tyite- | desprenderse | diccionario_general |
| `LEXR-00690` | claapjica | la clavija (para torcer laso) | diccionario_general |
| `LEXR-00691` | cleech | la llama (de fuego) | diccionario_general |
| `LEXR-00692` | cmeemu’j-, cmeemu’ju- | hacer cantar | diccionario_general |
| `LEXR-00693` | cpu’nze’j-, cpu’nze’je | ser padrinos (de matrimonio) | diccionario_general |
| `LEXR-00694` | ctũ’se’j-, ctũ’se’je- | hacer cargar, echar carga | diccionario_general |
| `LEXR-00695` | cujtyil | torcaz | diccionario_general |
| `LEXR-00696` | cuscuscjẽ | pasado mañana | diccionario_general |
| `LEXR-00697` | dund yaj | la tarabita (para cruzar río) | diccionario_general |
| `LEXR-00698` | dyus ĩtyĩmeesa | el ídolo | diccionario_general |
| `LEXR-00699` | e’shwee | la tosferina (la tos ferina) | diccionario_general |
| `LEXR-00700` | eenze- | reclinarse | diccionario_general |
| `LEXR-00701` | fiesta | la fiesta | diccionario_general |
| `LEXR-00702` | finzh wala | el pavo de monte (ave) | diccionario_general |
| `LEXR-00703` | indy (iindy, ingy) | tu, su, de usted (masculino) | diccionario_general |
| `LEXR-00704` | jwee | más | diccionario_general |
| `LEXR-00705` | jweelu- | asomar | diccionario_general |
| `LEXR-00706` | jwend | la vez, vuelta | diccionario_general |
| `LEXR-00707` | jya’ndyi’ndyi- | tocar (repetidas veces) | diccionario_general |
| `LEXR-00708` | jycaaja’ja- | ordenar (repetidas veces) | diccionario_general |
| `LEXR-00709` | jycaasa | el gobernante, mandatario | diccionario_general |
| `LEXR-00710` | jycuusa’j-, jycuusa’ja- | ser quitado, dejarse quitar | diccionario_general |
| `LEXR-00711` | jytujnd-, jytundu- | estar encarcelado, detenido | diccionario_general |
| `LEXR-00712` | jyu’nde (jyũ’nda) | liso | diccionario_general |
| `LEXR-00713` | jyuja-, jyujáa- (T) | volar | diccionario_general |
| `LEXR-00714` | jyũcj-, jyũcje- | amarrar nudo | diccionario_general |
| `LEXR-00715` | mercau | mercado | diccionario_general |
| `LEXR-00716` | mityj umsá | el alfarero | diccionario_general |
| `LEXR-00717` | mityjáj- | cocinar | diccionario_general |
| `LEXR-00718` | naa pa’ga | por eso | diccionario_general |
| `LEXR-00719` | nuylajcy- nuylaqui- | aflojar | diccionario_general |
| `LEXR-00720` | nuyũuchi- | hacer mermar | diccionario_general |
| `LEXR-00721` | nwe’we- | defender, amparar, salvar | diccionario_general |
| `LEXR-00722` | paañusu- | compartir la tristeza de otro | diccionario_general |
| `LEXR-00723` | patsu | la derecha | diccionario_general |
| `LEXR-00724` | pcaaca | sobrino o sobrina con el tío | diccionario_general |
| `LEXR-00725` | pcaw-, pcawu- | derramar (líquido) | diccionario_general |
| `LEXR-00726` | puiini | pleito | diccionario_general |
| `LEXR-00727` | quim | quien, ?quién? | diccionario_general |
| `LEXR-00728` | quitje- | 1. inclinar la cabeza; 2. quedar humillado | diccionario_general |
| `LEXR-00729` | quĩj-, quĩja-, quĩi- | bajar | diccionario_general |
| `LEXR-00730` | sende cuvy | la flauta (de carrizos verticales) | diccionario_general |
| `LEXR-00731` | shlaapún | eslabón (hierro para afilar o para sacar fuego del pedernal) | diccionario_general |
| `LEXR-00732` | shũu yu’tscavy | (planta medicinal) | diccionario_general |
| `LEXR-00733` | susu | de abajo | diccionario_general |
| `LEXR-00734` | tjaacue- | sobrar | diccionario_general |
| `LEXR-00735` | tu’vi- | opacar, obscurecerse | diccionario_general |
| `LEXR-00736` | tucha’cy | cuchara | diccionario_general |
| `LEXR-00737` | tul | la huerta, hortaliza | diccionario_general |
| `LEXR-00738` | tupj-, tupji- | voltear | diccionario_general |
| `LEXR-00739` | tywey-, tyweyúu- (cywey-) | vender | diccionario_general |
| `LEXR-00740` | tũtsa | la muela | diccionario_general |
| `LEXR-00741` | u’j-, u’jue- | ir, irse | diccionario_general |
| `LEXR-00742` | umbu’mbu- | lloviznar | diccionario_general |
| `LEXR-00743` | unza le’ch | ratón | diccionario_general |
| `LEXR-00744` | us | el fríjol | diccionario_general |
| `LEXR-00745` | us tapla, us tsep | fríjol cacha | diccionario_general |
| `LEXR-00746` | vite’ | y | diccionario_general |
| `LEXR-00747` | vity | la puerta | diccionario_general |
| `LEXR-00748` | wajwa | tibia | diccionario_general |
| `LEXR-00749` | yajcy-, yaaqui-, yaacy- | 1. pensar, acordarse; 2. confiar en; 3. dudar, vacilar; 4. sentirse triste, pensativo | diccionario_general |
| `LEXR-00750` | yase yu’ | agua bendita | diccionario_general |
| `LEXR-00751` | yatsqui’p-, yatsqui’pu- | poner adelante, arrear | diccionario_general |
| `LEXR-00752` | yu’cj ech | animal salvaje | diccionario_general |
| `LEXR-00753` | yu’tjeng-, yu’tjengu- | mirar atrás, voltearse para mirar atrás | diccionario_general |
| `LEXR-00754` | yuj | cierto, ciertamente | diccionario_general |
| `LEXR-00755` | yul pẽjy- | cobrar una deuda | diccionario_general |
| `LEXR-00756` | yulu-, yulúu- | recibir fiado, endeudarse | diccionario_general |
| `LEXR-00757` | yusuusu- | dar de beber (varias veces) | diccionario_general |
| `LEXR-00758` | ãapj-ãapjúu- | asaltar, agredir | diccionario_general |
| `LEXR-00759` | ñun-, ñunu- (yũn-) | dar fruto, cargar | diccionario_general |
| `LEXR-00760` | ñusha tel | el trapiche de mano | diccionario_general |
| `LEXR-00761` | ĩcjwe’sh | la visiones | diccionario_general |
| `LEXR-00762` | ĩts taty | nariz filuda | diccionario_general |
| `LEXR-00763` | ũ’nisa | comestible | diccionario_general |
| `LEXR-00764` | ẽegatjẽ’j | rayo | diccionario_general |
| `LEXR-00765` | acha acha | ligero | diccionario_general |
| `LEXR-00766` | amb-, ambu- | ehcar (granos) | diccionario_general |
| `LEXR-00767` | amby-, ambíi | rebosar | diccionario_general |
| `LEXR-00768` | anza | el pájaro carpintero | diccionario_general |
| `LEXR-00769` | caaiwecha’j-, caaiwecha’ja | contentar | diccionario_general |
| `LEXR-00770` | caapechcanu’j-, caapechcanu’ju- | hacer olvidar | diccionario_general |
| `LEXR-00771` | cacue (cuacue T) | el cuerpo | diccionario_general |
| `LEXR-00772` | cha’cy-, cha’qui- | enfadarse | diccionario_general |
| `LEXR-00773` | chavy | venado | diccionario_general |
| `LEXR-00774` | chimby | podrido | diccionario_general |
| `LEXR-00775` | chucha | zarigüeya, chucha | diccionario_general |
| `LEXR-00776` | cjacj-, cjacje- | asar | diccionario_general |
| `LEXR-00777` | cjavy | grano | diccionario_general |
| `LEXR-00778` | cpaachãtyj-, cpaachãtyji- | lograr empujar | diccionario_general |
| `LEXR-00779` | cpaawe’we | intervenir (en una conversación) | diccionario_general |
| `LEXR-00780` | cuw | el tumor, absceso | diccionario_general |
| `LEXR-00781` | cyuupu’j-, cyuupu’ju- | hacer atajar, mandar atajar | diccionario_general |
| `LEXR-00782` | duj-, dujáa- | ponerse pesado | diccionario_general |
| `LEXR-00783` | ech cupjy | la candelilla (insecto) | diccionario_general |
| `LEXR-00784` | ejnz | el verano | diccionario_general |
| `LEXR-00785` | ewuu | poder | diccionario_general |
| `LEXR-00786` | fi’l | la perdiz (ave) | diccionario_general |
| `LEXR-00787` | fiy we’we- | hablar mal | diccionario_general |
| `LEXR-00788` | fyne’sh | la saliva, baba | diccionario_general |
| `LEXR-00789` | fynũ | el sitio | diccionario_general |
| `LEXR-00790` | icj-, icje- | matar | diccionario_general |
| `LEXR-00791` | iicjẽe- | bajar | diccionario_general |
| `LEXR-00792` | iictejca- | subir | diccionario_general |
| `LEXR-00793` | iipyãj-,iipyãja-, iipyãa- | tener celos, estar celoso | diccionario_general |
| `LEXR-00794` | ijca-, iica- | golpear, chocar con, colindar con | diccionario_general |
| `LEXR-00795` | jimba apj | tábano (insecto) | diccionario_general |
| `LEXR-00796` | jiyunimeesa | desconocido | diccionario_general |
| `LEXR-00797` | jycjẽw-, jycjẽúu- | pasar | diccionario_general |
| `LEXR-00798` | jypeetyatya- | aplaudir (dar repetidas palmadas) | diccionario_general |
| `LEXR-00799` | jyuca, jyucáy | todo | diccionario_general |
| `LEXR-00800` | jũ’na qui’su | la semana pasada | diccionario_general |
| `LEXR-00801` | lashnu tash | mata de durazno (árbol) | diccionario_general |
| `LEXR-00802` | letani | colgado | diccionario_general |
| `LEXR-00803` | luus | el arroz | diccionario_general |
| `LEXR-00804` | mellisu | el mellizo | diccionario_general |
| `LEXR-00805` | mende | ¡Coséchelo! | diccionario_general |
| `LEXR-00806` | mutcue | el lulo (planta) | diccionario_general |
| `LEXR-00807` | neenjĩ’j | la madrina | diccionario_general |
| `LEXR-00808` | ntsun | el nieto, la nieta | diccionario_general |
| `LEXR-00809` | pa’jy we’we- | insinuar, hablar indirectamente de otro | diccionario_general |
| `LEXR-00810` | pcalte wete- | pecar, caer en pecado | diccionario_general |
| `LEXR-00811` | pe’jna u’jsa | guía | diccionario_general |
| `LEXR-00812` | pe’ltete- | hacerse pedazos, despedazarse | diccionario_general |
| `LEXR-00813` | pechcanusa | que olvida | diccionario_general |
| `LEXR-00814` | peecy jĩi | propio de él | diccionario_general |
| `LEXR-00815` | pejtya-, pejíi- | necesitar, faltar, hacer falta | diccionario_general |
| `LEXR-00816` | penzhi | la abuela | diccionario_general |
| `LEXR-00817` | pesay-, pesayu- | mirar al otro lado | diccionario_general |
| `LEXR-00818` | peswení | robado | diccionario_general |
| `LEXR-00819` | pjapj | planta del pie, palma de la mano | diccionario_general |
| `LEXR-00820` | pnaasa | la sombra (de una persona) | diccionario_general |
| `LEXR-00821` | puiisá | que pelea | diccionario_general |
| `LEXR-00822` | punza cafy | el sobaco, axila | diccionario_general |
| `LEXR-00823` | pus | agrio, fermentado | diccionario_general |
| `LEXR-00824` | pyãjtewe’sh | el hermano de en medio | diccionario_general |
| `LEXR-00825` | pũ’we- | comer demasiado | diccionario_general |
| `LEXR-00826` | sba’cue | (planta silvestre, que se usa para jabón) | diccionario_general |
| `LEXR-00827` | scjẽw-, scjẽúu- | pasar (hacia abajo) | diccionario_general |
| `LEXR-00828` | shica’ca- | reir (repetidas veces) | diccionario_general |
| `LEXR-00829` | shimb | maíz tierno | diccionario_general |
| `LEXR-00830` | shish | grieta, rendija | diccionario_general |
| `LEXR-00831` | spaacysa | la partera | diccionario_general |
| `LEXR-00832` | susni | ruido | diccionario_general |
| `LEXR-00833` | teega wee | enfermedad contagiosa | diccionario_general |
| `LEXR-00834` | tjãassa | que pide | diccionario_general |
| `LEXR-00835` | tsam | el metal, hierro | diccionario_general |
| `LEXR-00836` | tsũ’ta | la trenza de cabello o de cabuya | diccionario_general |
| `LEXR-00837` | tupa | la araña (arácnido) | diccionario_general |
| `LEXR-00838` | ucapajcy-, ucapaqui- | empujar (con violencia) | diccionario_general |
| `LEXR-00839` | ul pẽjy-, ul pẽyi- | cobrar una deuda | diccionario_general |
| `LEXR-00840` | utsje’tsje- | tocar (repetidas veces) | diccionario_general |
| `LEXR-00841` | vyandu- | blandir (bastón) | diccionario_general |
| `LEXR-00842` | watse (wetse) | la raíz | diccionario_general |
| `LEXR-00843` | wendynisa | querido, apreciable | diccionario_general |
| `LEXR-00844` | wes | gusano | diccionario_general |
| `LEXR-00845` | ya’jypumba- | engañarse | diccionario_general |
| `LEXR-00846` | yaandúu- | enrollarse, enredarse | diccionario_general |
| `LEXR-00847` | yacum | yacuma blanca (planta medicinal) | diccionario_general |
| `LEXR-00848` | yat chinda | estantillo de la casa | diccionario_general |
| `LEXR-00849` | ãtsã’a- | enfermarse, sufrir dolores de parto | diccionario_general |
| `LEXR-00850` | ña ũ’we | harina de yuca | diccionario_general |
| `LEXR-00851` | ñujne | la sala | diccionario_general |
| `LEXR-00852` | ñunz (yujnz) | la aguja | diccionario_general |
| `LEXR-00853` | ñusha puutssa | el que mete la caña en el otro lado del trapiche | diccionario_general |
| `LEXR-00854` | ũuw-, ũuwu- | mecer | diccionario_general |
| `LEXR-00855` | ẽsẽ-, ẽsẽje- | moverse | diccionario_general |
| `LEXR-00856` | anzee- | recostarse | diccionario_general |
| `LEXR-00857` | bara | la vara (medida) | diccionario_general |
| `LEXR-00858` | bich | plato (de madera) | diccionario_general |
| `LEXR-00859` | caafyutsu’j-, caafyutsu’ju- | hacer clavar, mandar crucificar | diccionario_general |
| `LEXR-00860` | caaiipe’je’j-, caaiipe’je’je | dejar bajo custodia de otro | diccionario_general |
| `LEXR-00861` | caavya´j-, caavya’ja- | revelar, mostrar | diccionario_general |
| `LEXR-00862` | caju, cajuy | de arriba para abajo | diccionario_general |
| `LEXR-00863` | canzh | feo, malo | diccionario_general |
| `LEXR-00864` | catj | tirante (pieza de la armadura del tejado) | diccionario_general |
| `LEXR-00865` | catu´j-, catu´ju- | dejar mojar | diccionario_general |
| `LEXR-00866` | caytundu’j-, caytundu’ju- | hacer amarrar | diccionario_general |
| `LEXR-00867` | cbajy | hervido | diccionario_general |
| `LEXR-00868` | chull | pene | diccionario_general |
| `LEXR-00869` | cjaquima | jáquima | diccionario_general |
| `LEXR-00870` | cjẽendyi’j | el esófago | diccionario_general |
| `LEXR-00871` | cla | el res, el ganado (animal doméstico) | diccionario_general |
| `LEXR-00872` | cmbamba | el mentón, cumbamba (voz Quechua) | diccionario_general |
| `LEXR-00873` | cpunga’j wee | colerín | diccionario_general |
| `LEXR-00874` | ctjeetje’j-, ctjeetje’je- | mandar lavar | diccionario_general |
| `LEXR-00875` | cutyj cjavy | maíz en grano | diccionario_general |
| `LEXR-00876` | cutyj ñuñ | grando de maíz | diccionario_general |
| `LEXR-00877` | cyuupj-, cyuupjáa- | encerrar, encarcelar | diccionario_general |
| `LEXR-00878` | dycjas much | pelo corto, pelón, motilón | diccionario_general |
| `LEXR-00879` | dyi’ puwe’sh | los de enfrente | diccionario_general |
| `LEXR-00880` | ewuní | el poder | diccionario_general |
| `LEXR-00881` | fychacha upj | cerca de lechero | diccionario_general |
| `LEXR-00882` | icjni | muerto | diccionario_general |
| `LEXR-00883` | iindyi’pu- | confrontar | diccionario_general |
| `LEXR-00884` | iiũ’ne- | llorar (al mismo tiempo que hace otra cosa) | diccionario_general |
| `LEXR-00885` | ipywe’sh | el rayo (que quema) | diccionario_general |
| `LEXR-00886` | jueves | el jueves | diccionario_general |
| `LEXR-00887` | jypi’cy-, jypi’qui- | invitar, convidar | diccionario_general |
| `LEXR-00888` | jyũ’nzh, jyũ’nzhcuẽ | en forma de bola | diccionario_general |
| `LEXR-00889` | le’leni | mojado | diccionario_general |
| `LEXR-00890` | lisasá | el rezandero | diccionario_general |
| `LEXR-00891` | ma’c yuu...ma’c yuu | o...o | diccionario_general |
| `LEXR-00892` | maava | cualquiera, quienquiera | diccionario_general |
| `LEXR-00893` | mutsu- | estar disgustado | diccionario_general |
| `LEXR-00894` | muypesa- | traer (a través) | diccionario_general |
| `LEXR-00895` | nchi’c npaasa | hijastro | diccionario_general |
| `LEXR-00896` | nchi’c nuuchsa | el hijo menor | diccionario_general |
| `LEXR-00897` | neeniisa | la ahijada | diccionario_general |
| `LEXR-00898` | paatenz-, paatenzúu (ptenz-) | llevar debajo del brazo, apretar | diccionario_general |
| `LEXR-00899` | paletun (pleetun T) | barretón | diccionario_general |
| `LEXR-00900` | Payaate ne’jue’sh | gobernador del Cauca | diccionario_general |
| `LEXR-00901` | pchjĩ’ch-, pchjĩ’chi | lavar la cara | diccionario_general |
| `LEXR-00902` | pdeeu’y | la fornicadora | diccionario_general |
| `LEXR-00903` | peetje- | 1. dar sabor, condimentar; 2. penetrar (ej. humo) | diccionario_general |
| `LEXR-00904` | petyaatya- | dar bofetadas | diccionario_general |
| `LEXR-00905` | pta’shi’sh-, pta’shi’shi- | avisar (repetidas veces o a varias personas) | diccionario_general |
| `LEXR-00906` | ptjãawe- | hacer daño a una persona, agredir | diccionario_general |
| `LEXR-00907` | ptyijnde-, ptyinde- | 1. cruzarse en el camino, entrecruzarse; 2. quitar tiempo, interrupir | diccionario_general |
| `LEXR-00908` | pu’inene- | brillar | diccionario_general |
| `LEXR-00909` | pu’vitu- | perder de vista | diccionario_general |
| `LEXR-00910` | puca- | al lado de | diccionario_general |
| `LEXR-00911` | punga-, pungáa- | vomitar | diccionario_general |
| `LEXR-00912` | putsu | de lado, al soslayo | diccionario_general |
| `LEXR-00913` | puuvyãjn | la mitad | diccionario_general |
| `LEXR-00914` | pẽty apjani | ronco | diccionario_general |
| `LEXR-00915` | queenze’j-, queenze’je- | poner inclinado | diccionario_general |
| `LEXR-00916` | quiiyu’j-, quiiyu’ju- | hacer escapar, dejar escapar | diccionario_general |
| `LEXR-00917` | quim yujva | nadia | diccionario_general |
| `LEXR-00918` | se’w- | insertar | diccionario_general |
| `LEXR-00919` | sec cjẽj- | ponerse el sol | diccionario_general |
| `LEXR-00920` | shwi’la | ulluco | diccionario_general |
| `LEXR-00921` | shã’we | la lombriz intestinal | diccionario_general |
| `LEXR-00922` | shũpy | choclo cocido | diccionario_general |
| `LEXR-00923` | sumba- | alcanzar | diccionario_general |
| `LEXR-00924` | teelu’j-, teelu’ju- | 1. poner en la cepo 2. poner horqueta (al puerco) | diccionario_general |
| `LEXR-00925` | tsep | planchudo | diccionario_general |
| `LEXR-00926` | tsjĩtsj um- | empajar | diccionario_general |
| `LEXR-00927` | tujndtujnd | poco a poco, despacio | diccionario_general |
| `LEXR-00928` | tupjáa- | humedecerse | diccionario_general |
| `LEXR-00929` | u’cani | la entrada | diccionario_general |
| `LEXR-00930` | visu’s- | juguetear (repetidas veces) | diccionario_general |
| `LEXR-00931` | vits | la punta, cumbre | diccionario_general |
| `LEXR-00932` | wat | caripaspada, de mejillas rosadas | diccionario_general |
| `LEXR-00933` | well le’chcue, wellcue | periquillo | diccionario_general |
| `LEXR-00934` | ya’icj-, ya’icje- | suicidarse | diccionario_general |
| `LEXR-00935` | ya’nwe’we- | librarse | diccionario_general |
| `LEXR-00936` | yacue | la cresta (de gallo) | diccionario_general |
| `LEXR-00937` | yafy yu’ | lágrima | diccionario_general |
| `LEXR-00938` | yũ’wẽeni | la sed | diccionario_general |
| `LEXR-00939` | zeecu’j-, zeecu’ju- | afilar | diccionario_general |
| `LEXR-00940` | ãchj | hoy, ahora, recién | diccionario_general |
| `LEXR-00941` | ũs-, ũsu- | 1. dar, conceder; 2. saludar, dar la mano | diccionario_general |
| `LEXR-00942` | ajaj | con sabor de humo | diccionario_general |
| `LEXR-00943` | avy-, avi- | escupir | diccionario_general |
| `LEXR-00944` | awu’w | echar (líquido en varias ollas) | diccionario_general |
| `LEXR-00945` | bats ej | cabuyal, roza de cabuya | diccionario_general |
| `LEXR-00946` | bats yafy | cogollo de fique | diccionario_general |
| `LEXR-00947` | ca’ga’j-, ca’ja’ja- | hacer montar | diccionario_general |
| `LEXR-00948` | caaja’nda’j-, caaja’nda’ja- | igualar (el peso), comparar | diccionario_general |
| `LEXR-00949` | caanze’j-, caanze’je-(queenze’j-) | poner inclinado | diccionario_general |
| `LEXR-00950` | caapuutwe’we’j-, caapuutywe’we’je- | conciliar | diccionario_general |
| `LEXR-00951` | caatyweyu’j-, caatyweyu’ju- | permitir vender | diccionario_general |
| `LEXR-00952` | cachni | el asiento | diccionario_general |
| `LEXR-00953` | case´j-, caseje-(cãsej-) | 1. salir 2. nacer 3. resultar | diccionario_general |
| `LEXR-00954` | cchaanzha’j-, cchaanzha’ja- | hacer chupar, desinflamar | diccionario_general |
| `LEXR-00955` | chu’ch tyutee- | destetar | diccionario_general |
| `LEXR-00956` | cjuuts | la ceniza, la pólvora | diccionario_general |
| `LEXR-00957` | clapichi | el trapiche | diccionario_general |
| `LEXR-00958` | cnaysá | el jornalero | diccionario_general |
| `LEXR-00959` | corea | el cinturón, la correa | diccionario_general |
| `LEXR-00960` | cpeelu’j-, cpeelu’ju- | hacer rodar | diccionario_general |
| `LEXR-00961` | cuch-, cuchíi- | aburrirse | diccionario_general |
| `LEXR-00962` | cuetand | el mambe | diccionario_general |
| `LEXR-00963` | deewẽe- | tener sueño | diccionario_general |
| `LEXR-00964` | dyicy | la caspa | diccionario_general |
| `LEXR-00965` | dyijy yuuni | la brujería hechicería | diccionario_general |
| `LEXR-00966` | e’shavy | el oso (mamífero) | diccionario_general |
| `LEXR-00967` | echtel | perico plomo (aven nocturna, mal agüero) | diccionario_general |
| `LEXR-00968` | fii | aparte, separado | diccionario_general |
| `LEXR-00969` | iiquĩj- | bajar | diccionario_general |
| `LEXR-00970` | iitjeng- | mirar (al mismo tiempo que hace otra cosa) | diccionario_general |
| `LEXR-00971` | imu’s-imu’su- | seguir rastro, oler | diccionario_general |
| `LEXR-00972` | jemb | el chorrizo | diccionario_general |
| `LEXR-00973` | julnu | el horno | diccionario_general |
| `LEXR-00974` | jycaase-, jycaasée- | descansar | diccionario_general |
| `LEXR-00975` | jyputa’ta- | coger rastro (repetidas veces) | diccionario_general |
| `LEXR-00976` | jyũcuet | la rodilla | diccionario_general |
| `LEXR-00977` | le’le- | mojar, regar | diccionario_general |
| `LEXR-00978` | luuch le’chcue | criatura, bebé | diccionario_general |
| `LEXR-00979` | naa | este, esta, esto | diccionario_general |
| `LEXR-00980` | ne’sh, ne’shtjẽ’j | el primogénito (primer hijo) | diccionario_general |
| `LEXR-00981` | nus en | invierno | diccionario_general |
| `LEXR-00982` | pcambnisa | urdirmbre (hilos verticales del telar) | diccionario_general |
| `LEXR-00983` | peevya’j-, peevya’ja- (T) | enseñar | diccionario_general |
| `LEXR-00984` | pemba-, pembáa- | acabar | diccionario_general |
| `LEXR-00985` | piya-, piyáa- | aprender | diccionario_general |
| `LEXR-00986` | pnjĩ’j | madre con hijo u hija | diccionario_general |
| `LEXR-00987` | pu’nze’j-, pu’nze’je- | 1. dar sombra 2. servir como padrinos en las bodas | diccionario_general |
| `LEXR-00988` | pu’uwe- | coger (algo que viene del rumbo opuesto), apañar | diccionario_general |
| `LEXR-00989` | punza | el rincón, la esquina | diccionario_general |
| `LEXR-00990` | qui’spyãj | el miércoles | diccionario_general |
| `LEXR-00991` | qui’tj wala | muela | diccionario_general |
| `LEXR-00992` | quimbe’je’j-, quimbe’je’je- | hacer señas | diccionario_general |
| `LEXR-00993` | quitje’tje- | cabecear | diccionario_general |
| `LEXR-00994` | quitjeetj-, quitjeetje- | clavar varias estacas | diccionario_general |
| `LEXR-00995` | quiwe mityj | olla de barro | diccionario_general |
| `LEXR-00996` | sec cjẽjetste | al ponerse el sol | diccionario_general |
| `LEXR-00997` | sũpy-, sũpíi- | desnudarse, desvestirse | diccionario_general |
| `LEXR-00998` | teechcue | poco, poquito | diccionario_general |
| `LEXR-00999` | tjame ũus | vergüenza | diccionario_general |
| `LEXR-01000` | tjune watse | raíz de la lengua | diccionario_general |
| `LEXR-01001` | tsut | el choclo, mazorca de maíz tierno | diccionario_general |
| `LEXR-01002` | tulu’j-, tulu’ju- | cercar la hortaliza | diccionario_general |
| `LEXR-01003` | tumb | paloma | diccionario_general |
| `LEXR-01004` | tuts-, tutsúu- | aparar agua | diccionario_general |
| `LEXR-01005` | tywes-, tywesu- (cywes-) | mostrar | diccionario_general |
| `LEXR-01006` | tyweteni | suelto | diccionario_general |
| `LEXR-01007` | ulchic | urraca (ave) | diccionario_general |
| `LEXR-01008` | upagacy-, upagaqui- | empujar (repetidas veces) | diccionario_general |
| `LEXR-01009` | upj | la cerca, el cerco | diccionario_general |
| `LEXR-01010` | vyaasamée | invisible | diccionario_general |
| `LEXR-01011` | vyllill | 1. uña (de persona); 2. dedo (medida, anchura de un dedo); 3. garra (de ave); 4. casco (de caballo); 5. pezuña (de animal) | diccionario_general |
| `LEXR-01012` | wajty-, watyi- | cansarse | diccionario_general |
| `LEXR-01013` | we’weni | lenguaje, habla, voz | diccionario_general |
| `LEXR-01014` | weech yajcy- | despreciar | diccionario_general |
| `LEXR-01015` | wey-, weyíi- | gritar | diccionario_general |
| `LEXR-01016` | wuwúu- | correr | diccionario_general |
| `LEXR-01017` | ya’ja | la jigra, el morral, mochila | diccionario_general |
| `LEXR-01018` | yaatsjunde- | zafarse, desengarzarse | diccionario_general |
| `LEXR-01019` | yaya-, yayáa- | temblar (de miedo, o del frío) | diccionario_general |
| `LEXR-01020` | yu’achj-, yu’acje- | meter en, echar en | diccionario_general |
| `LEXR-01021` | yu’waca | la acequia | diccionario_general |
| `LEXR-01022` | yulsá (yulusá) | deudor | diccionario_general |
| `LEXR-01023` | ĩshiisa | menitroso | diccionario_general |
| `LEXR-01024` | ũchji’ndy-, ũchi’ndyi- (ushi’ndy-) | ser mezquino | diccionario_general |
| `LEXR-01025` | acha | caliente | diccionario_general |
| `LEXR-01026` | and-, andúu- | envolver, enrollar | diccionario_general |
| `LEXR-01027` | anzh-, anzhi- | pelar los dientes | diccionario_general |
| `LEXR-01028` | at-, atúu- | coger, llevar en la mano | diccionario_general |
| `LEXR-01029` | caachu | cuerno, cacho | diccionario_general |
| `LEXR-01030` | caanasa’j-, caanasa’ja- | colocar espantapájaros (en los sembrados) | diccionario_general |
| `LEXR-01031` | cacue cjas | el pelo del cuerpo | diccionario_general |
| `LEXR-01032` | cajcatẽ´j | el suegro | diccionario_general |
| `LEXR-01033` | camba en | la boda, el casamiento (díade la ceremonia) | diccionario_general |
| `LEXR-01034` | castigo cnay- | sufir castigo | diccionario_general |
| `LEXR-01035` | cdeeje’jmée- | desvelar, no dejar dormir | diccionario_general |
| `LEXR-01036` | cha’cute- | formar grano | diccionario_general |
| `LEXR-01037` | chavi’vi- | dar varios pasos | diccionario_general |
| `LEXR-01038` | chijme | blanco | diccionario_general |
| `LEXR-01039` | chinda watse | tendón de la pie | diccionario_general |
| `LEXR-01040` | chucha cu’jni | baile de la chucha | diccionario_general |
| `LEXR-01041` | cjuẽs | el juez (oficial del cabildo) | diccionario_general |
| `LEXR-01042` | cjã’sh wala | la langosta (insecto) | diccionario_general |
| `LEXR-01043` | cjũchcjũch tsẽy | azul subido | diccionario_general |
| `LEXR-01044` | cnzeevy-, cnzeevi- | chamuscar | diccionario_general |
| `LEXR-01045` | creĩ- | creer | diccionario_general |
| `LEXR-01046` | cyeele’j-, cyeele’je- | hacer cosquillas | diccionario_general |
| `LEXR-01047` | duj | pesado | diccionario_general |
| `LEXR-01048` | fytũu ũ’sa cjã’cjã | el comején | diccionario_general |
| `LEXR-01049` | iimi’- | casarse (dícese de la mujer) | diccionario_general |
| `LEXR-01050` | iitejca- | subir | diccionario_general |
| `LEXR-01051` | ja’ll-, ja’lli- | estregar | diccionario_general |
| `LEXR-01052` | jimba chinda vyllill | casco (del caballo) | diccionario_general |
| `LEXR-01053` | jyaw-, jyawúu- | guardar, cruzar los brazos | diccionario_general |
| `LEXR-01054` | jycaanisa | mandadero | diccionario_general |
| `LEXR-01055` | jypejcue- | cortarse | diccionario_general |
| `LEXR-01056` | jytandyi- | dar vuelta alrededor de | diccionario_general |
| `LEXR-01057` | jĩni | dicho | diccionario_general |
| `LEXR-01058` | luñis | el lunes | diccionario_general |
| `LEXR-01059` | manzcuẽe | unos pocos, unos cuantos | diccionario_general |
| `LEXR-01060` | me’cy | el hígado | diccionario_general |
| `LEXR-01061` | much | los pantalones (de liencillo) | diccionario_general |
| `LEXR-01062` | nava | pero | diccionario_general |
| `LEXR-01063` | nchi’c ntjẽjsa | el hijo mayor | diccionario_general |
| `LEXR-01064` | neevisha- | persuadir a otro quedarse, rogar se quede | diccionario_general |
| `LEXR-01065` | neeyũu- (neeñuu-) | 1. quedarse 2. ser salvo 3. ser condenado | diccionario_general |
| `LEXR-01066` | nmi’ ji’pjmeesa | soltera | diccionario_general |
| `LEXR-01067` | ntjẽj, ntẽ’jsa | mayor (de edad) | diccionario_general |
| `LEXR-01068` | ntyi’nsa (ntyi’nas J) | la cuñada (entre mujeres) | diccionario_general |
| `LEXR-01069` | nuysẽj-, nuysẽje- | traer (desde arriba, en plano) | diccionario_general |
| `LEXR-01070` | pa’j | hasta | diccionario_general |
| `LEXR-01071` | paawe’we- | encargar | diccionario_general |
| `LEXR-01072` | pacjẽ | trama, hilo horizontal del telar | diccionario_general |
| `LEXR-01073` | patyu | el patio | diccionario_general |
| `LEXR-01074` | payáa | papaya | diccionario_general |
| `LEXR-01075` | pend | raya | diccionario_general |
| `LEXR-01076` | pesaja’ja- | pasar (repetidas veces) | diccionario_general |
| `LEXR-01077` | pjulaĩi- | remendar | diccionario_general |
| `LEXR-01078` | pjãjã’jã- | toser (repetidas veces) | diccionario_general |
| `LEXR-01079` | pqui’tanisa | la lámpara | diccionario_general |
| `LEXR-01080` | ptamúu- | casarse, formar pareja | diccionario_general |
| `LEXR-01081` | pu’tjeng-, pu’tjengu- | encontrarse con otro (que viene del rumbo opuesto | diccionario_general |
| `LEXR-01082` | setlu | el cedro (árbol) | diccionario_general |
| `LEXR-01083` | shaacue | la broma, el chiste, la chanza | diccionario_general |
| `LEXR-01084` | shã’py | 1. vástago, renuevo de árbol o planta; 2. vástago, persona descendiente de otra | diccionario_general |
| `LEXR-01085` | shũucuet | la piedra de afilar | diccionario_general |
| `LEXR-01086` | siyula cna’sa | la señorita (de raza blanca) | diccionario_general |
| `LEXR-01087` | spãpa-, spãpáa- | esponjarse, hincharse | diccionario_general |
| `LEXR-01088` | suerte caaj- | echar suertes | diccionario_general |
| `LEXR-01089` | ta’nda | cucarrón | diccionario_general |
| `LEXR-01090` | tjuse | la chamiza | diccionario_general |
| `LEXR-01091` | tjẽyte ñuste fi’nze- | tener dificultades | diccionario_general |
| `LEXR-01092` | tyiityi’j- | hacer barro | diccionario_general |
| `LEXR-01093` | tyjicj lul | nuez de la garganta | diccionario_general |
| `LEXR-01094` | tãapj | la nube, neblina | diccionario_general |
| `LEXR-01095` | ul | la culebra | diccionario_general |
| `LEXR-01096` | uuni cja’ty | cadáver | diccionario_general |
| `LEXR-01097` | vis-, visu- | 1. desyerbar, limpiar maleza; 2. juguetear | diccionario_general |
| `LEXR-01098` | wendyni | querido | diccionario_general |
| `LEXR-01099` | wãatsja- | pellizcar | diccionario_general |
| `LEXR-01100` | wãatãtãj- | 1. botar (repetidas veces); 2. apedrear | diccionario_general |
| `LEXR-01101` | wãjy | hiel | diccionario_general |
| `LEXR-01102` | wẽt fi’nze- | estar alentado, estar bien | diccionario_general |
| `LEXR-01103` | yat | la casa | diccionario_general |
| `LEXR-01104` | ãpwes | nuche (insecto) | diccionario_general |
| `LEXR-01105` | ñusha cja’ty | bagazo | diccionario_general |
| `LEXR-01106` | ũyuwe’sh | habitante de Tierradentro | diccionario_general |
| `LEXR-01107` | a’j-, a’ja- | montar | diccionario_general |
| `LEXR-01108` | andni | enrollado | diccionario_general |
| `LEXR-01109` | atall luuch | el pollo | diccionario_general |
| `LEXR-01110` | atsjunde- | decolgar, desengarzar | diccionario_general |
| `LEXR-01111` | atyj cupy | anaco abierto | diccionario_general |
| `LEXR-01112` | baji’j-, baji’ji- | calentar (a otro) | diccionario_general |
| `LEXR-01113` | caapiya’jni | enseñanza | diccionario_general |
| `LEXR-01114` | caaquindu’j-, caaquindu’ju- | mandar peinar | diccionario_general |
| `LEXR-01115` | caaquĩiji’j-, caaquĩiji’ji- | hacer bajar (dese arriba) | diccionario_general |
| `LEXR-01116` | caytjacue´j-, caytjacue’je- | dejar pasar más tiempo | diccionario_general |
| `LEXR-01117` | chalsa | cosa gruesa | diccionario_general |
| `LEXR-01118` | chiime´j-, chiime’je- | blanquear | diccionario_general |
| `LEXR-01119` | chiiwa’wa- | podrirse | diccionario_general |
| `LEXR-01120` | chu’nzhu- | arrugarse | diccionario_general |
| `LEXR-01121` | chucuende- | arrancar | diccionario_general |
| `LEXR-01122` | chucuete- | arrancarse | diccionario_general |
| `LEXR-01123` | cielu | el cielo | diccionario_general |
| `LEXR-01124` | cja’tya’j-, cja’tya’ja- | dar rejo, castigar | diccionario_general |
| `LEXR-01125` | cjicjy-, cjicjíi- | aclarar el día | diccionario_general |
| `LEXR-01126` | cnene | la frente | diccionario_general |
| `LEXR-01127` | cpaacyjiyu- | lograr entender | diccionario_general |
| `LEXR-01128` | cpaanewe- | lograr detener | diccionario_general |
| `LEXR-01129` | ctejca-, cteega- | cruzar, pasar al otro lado | diccionario_general |
| `LEXR-01130` | cuchi | cerdo, marrano, puerco | diccionario_general |
| `LEXR-01131` | cue quiwe wendy | sabaleta | diccionario_general |
| `LEXR-01132` | cuet | la piedra | diccionario_general |
| `LEXR-01133` | cuetpũts | chulco (plana medicinal) | diccionario_general |
| `LEXR-01134` | cutyj cjũch | maíz negro | diccionario_general |
| `LEXR-01135` | cweetjsa | que alumbra (por ejemplo, el sol) | diccionario_general |
| `LEXR-01136` | cwẽechja-, cwẽechjáa- | lavar las manos | diccionario_general |
| `LEXR-01137` | cytũus | el arco iris | diccionario_general |
| `LEXR-01138` | deepa’chni | la cobija | diccionario_general |
| `LEXR-01139` | duusá | ponedora (galiina que pone huevos), animal con cría | diccionario_general |
| `LEXR-01140` | ee | sangre | diccionario_general |
| `LEXR-01141` | fynej | la mosca (insecto) | diccionario_general |
| `LEXR-01142` | fyutstende- | desclavar (un clavo), desbotonar | diccionario_general |
| `LEXR-01143` | iicjẽw- | pasar | diccionario_general |
| `LEXR-01144` | iijyũnisa | servible, usado (de segunda mano) | diccionario_general |
| `LEXR-01145` | iisawa’jnimée | mostrenco, sin marca | diccionario_general |
| `LEXR-01146` | iiwajtse-, iiwatse- | enraizar | diccionario_general |
| `LEXR-01147` | ji’mbe | el muslo | diccionario_general |
| `LEXR-01148` | jwee ũ’nacje | más antes | diccionario_general |
| `LEXR-01149` | jycjẽendyi’j | el esófago | diccionario_general |
| `LEXR-01150` | meej | ¡Siémbrelo! | diccionario_general |
| `LEXR-01151` | muts | montón, montículo | diccionario_general |
| `LEXR-01152` | nuype’te- | permitir amanecer | diccionario_general |
| `LEXR-01153` | pacuesá | que busca | diccionario_general |
| `LEXR-01154` | patsu cuse | la mano derecha | diccionario_general |
| `LEXR-01155` | peets tyjã’ | hoja de mejicano (da sabor a la mazamorra) | diccionario_general |
| `LEXR-01156` | penda-, pendáa- | 1. enterrar, sepular; 2. hundirse | diccionario_general |
| `LEXR-01157` | puca | mostacilla (insecto) | diccionario_general |
| `LEXR-01158` | putssu | a la orilla de | diccionario_general |
| `LEXR-01159` | puuple | pobre, desgraciado | diccionario_general |
| `LEXR-01160` | pyãj-, pyãja- | tener celos (entre esposos) | diccionario_general |
| `LEXR-01161` | pẽw-, pẽwúu- | bañarse | diccionario_general |
| `LEXR-01162` | shape | caracol | diccionario_general |
| `LEXR-01163` | sulu | el zorro (mamífero) | diccionario_general |
| `LEXR-01164` | sulu | zorro | diccionario_general |
| `LEXR-01165` | sund-, sundúu- (tsund-) | gotear | diccionario_general |
| `LEXR-01166` | sut | recto, directo | diccionario_general |
| `LEXR-01167` | tall | flaco, delgado | diccionario_general |
| `LEXR-01168` | tjũ’we cafy | el oído | diccionario_general |
| `LEXR-01169` | tsu’vy wee | la hidropesía | diccionario_general |
| `LEXR-01170` | tuca | el calabazo, la vasija rústica, totuma | diccionario_general |
| `LEXR-01171` | tulu | el toro | diccionario_general |
| `LEXR-01172` | tund yaj | la tarabita (cuerda pa cruzar el río) | diccionario_general |
| `LEXR-01173` | unza wala | la rata (mamífero roedor) | diccionario_general |
| `LEXR-01174` | uu en | la muerte, día de la muerte | diccionario_general |
| `LEXR-01175` | wawa | el algodón | diccionario_general |
| `LEXR-01176` | wendy ucje | atarraya | diccionario_general |
| `LEXR-01177` | wẽsẽ’j-, wẽsẽ’je- | escuchar, oir | diccionario_general |
| `LEXR-01178` | wẽt putasá | olor fragante | diccionario_general |
| `LEXR-01179` | yaj | picante, amargo | diccionario_general |
| `LEXR-01180` | yaj chijme | (especie de bejuco) | diccionario_general |
| `LEXR-01181` | yu’tya- | sonsacar | diccionario_general |
| `LEXR-01182` | ñeese- | tener ’sensaciones’ en el cuerpo | diccionario_general |
| `LEXR-01183` | ĩquĩ | crudo | diccionario_general |
| `LEXR-01184` | ũ’cj-, ũ’cju- | moler | diccionario_general |
| `LEXR-01185` | ũus yaacyni | pensamiento | diccionario_general |
| `LEXR-01186` | ẽewee | la estrella fugaz | diccionario_general |
| `LEXR-01187` | ẽjyã cu’ta | rama de arbusto | diccionario_general |
| `LEXR-01188` | ẽs ets, we’pe ẽs | frailejón | diccionario_general |
| `LEXR-01189` | ẽsẽ’sẽ- | moverse (repetidas veces) | diccionario_general |
| `LEXR-01190` | acha quiwe | tierra caliente | diccionario_general |
| `LEXR-01191` | acha yuu- | hacer calor | diccionario_general |
| `LEXR-01192` | apjni | cerrado | diccionario_general |
| `LEXR-01193` | arendãy- | arrendar (terreno) | diccionario_general |
| `LEXR-01194` | atsejy | asco, cosa desagrable | diccionario_general |
| `LEXR-01195` | atyj wẽsẽ | fleco de la ruana o anaco | diccionario_general |
| `LEXR-01196` | bats tsjũtsj | espina de cabuya | diccionario_general |
| `LEXR-01197` | blal | el umbral | diccionario_general |
| `LEXR-01198` | caacndyi’pu’j-, caacndyi’pu’ju- | hacer confrontar | diccionario_general |
| `LEXR-01199` | caafi’nze’j-, caafi’nze’je-(cfi’nze’j-) | hacer vivir | diccionario_general |
| `LEXR-01200` | caapcjaacje’j-, caapcjaacje’je- | permitir asistir, mandar reunirse | diccionario_general |
| `LEXR-01201` | caaquiisu’j-, caaquiisu’ju- | hacer quitar | diccionario_general |
| `LEXR-01202` | cafe | el café | diccionario_general |
| `LEXR-01203` | chunda | la chonta (especie de palmera), la vara de chonta | diccionario_general |
| `LEXR-01204` | cjãp | oloroso, fétido | diccionario_general |
| `LEXR-01205` | cjũch | negro, sucio | diccionario_general |
| `LEXR-01206` | cjẽj-, cjẽjẽ-, cjẽe- | bajar, descender, caber, ponserse el sol | diccionario_general |
| `LEXR-01207` | cu’ch | arenoso | diccionario_general |
| `LEXR-01208` | cuvy-, cuvíi- | tocar flauta | diccionario_general |
| `LEXR-01209` | cyajíi | por esa misma razón | diccionario_general |
| `LEXR-01210` | cãj-, cãjã- | empezar | diccionario_general |
| `LEXR-01211` | cãjpy | conejo | diccionario_general |
| `LEXR-01212` | enzh | aguado | diccionario_general |
| `LEXR-01213` | fi’fy | bajo (estatura) | diccionario_general |
| `LEXR-01214` | fita- | encogerse (tela) | diccionario_general |
| `LEXR-01215` | fiw-, fiwúu- | recoger (granos) | diccionario_general |
| `LEXR-01216` | fiy | distinto, diferente, extraño | diccionario_general |
| `LEXR-01217` | i’sut | la guaraca, honda | diccionario_general |
| `LEXR-01218` | iinamu-(iiyamu-) | adueñarse | diccionario_general |
| `LEXR-01219` | iisawa’jni | con señal, marca | diccionario_general |
| `LEXR-01220` | iiwejch yaacyni | orgullo | diccionario_general |
| `LEXR-01221` | is- | vestirse (dícese de la mujer) | diccionario_general |
| `LEXR-01222` | iviit-, iviitu- | perder | diccionario_general |
| `LEXR-01223` | jamby-, jambíi- | ser esquivo, esquivar | diccionario_general |
| `LEXR-01224` | jypumba-, jyumbáa- | equivocarse, desviarse, dejarse engeñar | diccionario_general |
| `LEXR-01225` | lemúu- | ponerse amarillo | diccionario_general |
| `LEXR-01226` | menz | la cola | diccionario_general |
| `LEXR-01227` | mityj tjũ’wẽ | orilla de la olla | diccionario_general |
| `LEXR-01228` | muvijty-, muvityíi- | mudarse de casa, quitarse de, retirarse de | diccionario_general |
| `LEXR-01229` | mẽewẽjy | el gallinazo, galembo (ave) | diccionario_general |
| `LEXR-01230` | nacue | tan, tanto (de este tamaño o cantidad) | diccionario_general |
| `LEXR-01231` | npach-, npaachíi- | coger sin permiso | diccionario_general |
| `LEXR-01232` | nuycatyji- | sanar | diccionario_general |
| `LEXR-01233` | nuypejna-, nuypena- | hacer rendir más, hacer que abunde | diccionario_general |
| `LEXR-01234` | nyuu | esposa | diccionario_general |
| `LEXR-01235` | ocho | ocho | diccionario_general |
| `LEXR-01236` | pa’csha’w- | soñar | diccionario_general |
| `LEXR-01237` | pa’j-, pa’ja- | llegar | diccionario_general |
| `LEXR-01238` | papa wala | el abuelo, bisabuelo | diccionario_general |
| `LEXR-01239` | pejca | siempre, realmente (con seguridad) | diccionario_general |
| `LEXR-01240` | pendani cafy | sepulcro, fosa pars entierro | diccionario_general |
| `LEXR-01241` | petsete- (petsate-) | hendir, abrir hendedura | diccionario_general |
| `LEXR-01242` | pil tuty | la pantorrilla | diccionario_general |
| `LEXR-01243` | pjate- | abrirse, rajarse | diccionario_general |
| `LEXR-01244` | pshica | risueño | diccionario_general |
| `LEXR-01245` | ptjãawesa | persona que causa daño a otro | diccionario_general |
| `LEXR-01246` | pucacje nyacj | el primo, la prima (del mismo sexo) | diccionario_general |
| `LEXR-01247` | puuquiwe- | empezar, emprender (un trabajo) | diccionario_general |
| `LEXR-01248` | qui’pu’p-, qui’pu’pu- | poner (repetidas veces cosas) | diccionario_general |
| `LEXR-01249` | quitscjẽ | abajo en la quebrada | diccionario_general |
| `LEXR-01250` | shi’nd-, shi’ndu- | imitar, remedar | diccionario_general |
| `LEXR-01251` | shquiicy | amarillo | diccionario_general |
| `LEXR-01252` | sinzha- | cinchar, asegurar la silla con cincha | diccionario_general |
| `LEXR-01253` | smejme (tsmejme) | la mariposa (insecto) | diccionario_general |
| `LEXR-01254` | tcu’nz | pacunga (planta) | diccionario_general |
| `LEXR-01255` | tsinz | la espalda | diccionario_general |
| `LEXR-01256` | tupa pwejy | la telaraña | diccionario_general |
| `LEXR-01257` | tyajy (cyajy) | su (de él, de ella) | diccionario_general |
| `LEXR-01258` | u’casa | que entra | diccionario_general |
| `LEXR-01259` | ufy-, ufi- | chiflar | diccionario_general |
| `LEXR-01260` | ul equis | víbora venenosa (bothropo atrox) | diccionario_general |
| `LEXR-01261` | ulu’j | rata grande del monte (mamífero roedor) | diccionario_general |
| `LEXR-01262` | upyni | nacimiento, lugar de nacimiento | diccionario_general |
| `LEXR-01263` | us bej | fríjol rojo | diccionario_general |
| `LEXR-01264` | vite jĩi | ajeno | diccionario_general |
| `LEXR-01265` | vitssu | serranía | diccionario_general |
| `LEXR-01266` | wa’ta’jni | ensillado | diccionario_general |
| `LEXR-01267` | wã’ji- | formar granos | diccionario_general |
| `LEXR-01268` | wã’jy | la llaga, úlcera, ’granos’ | diccionario_general |
| `LEXR-01269` | wẽt-, wẽtúu- | sanar | diccionario_general |
| `LEXR-01270` | yaaca-, yaacáa | sentir dolor | diccionario_general |
| `LEXR-01271` | yaawee | el paludismo | diccionario_general |
| `LEXR-01272` | yu’tse’j-, yu’tse’je- | curar, dar remedio, medicinar | diccionario_general |
| `LEXR-01273` | -ca, (-ga) | en, de | diccionario_general |
| `LEXR-01274` | avysu’s-, avysu’su- | orinar en | diccionario_general |
| `LEXR-01275` | bats upj | cerca de cabuya | diccionario_general |
| `LEXR-01276` | caaptsu’ju’j-, caaptsu’ju’ju- | terminar (poner fin a un asunto o a una reunión) | diccionario_general |
| `LEXR-01277` | caawa’qui’j-, caawa’qui’ji- | hacer masticar, hacer morder | diccionario_general |
| `LEXR-01278` | catstendenimeesa | vestido sin costura | diccionario_general |
| `LEXR-01279` | cbuucha’j-, cbuucha’ja- | hacer brotar | diccionario_general |
| `LEXR-01280` | cndul | cóndor | diccionario_general |
| `LEXR-01281` | cne’ta’j-, cne’ta’ja- | pegar con goma | diccionario_general |
| `LEXR-01282` | cpi’sh cwejne- | relampaguear | diccionario_general |
| `LEXR-01283` | cuene | brillar | diccionario_general |
| `LEXR-01284` | cuetmuse | la arena | diccionario_general |
| `LEXR-01285` | cuetumba ũshi- | caer granizo, granizar | diccionario_general |
| `LEXR-01286` | cus | la noche | diccionario_general |
| `LEXR-01287` | deepang- | demostrar sueño, transnochar | diccionario_general |
| `LEXR-01288` | e’ste u’j-, e’ste yuj- | seguir | diccionario_general |
| `LEXR-01289` | fyutsute- | desclavar, desprenderse, zafarse | diccionario_general |
| `LEXR-01290` | iiwejch-, iiweechi- | enorgullecerse | diccionario_general |
| `LEXR-01291` | jimba apj | tábano | diccionario_general |
| `LEXR-01292` | jyta’ñisa | adivino, persona que siente sensaciones | diccionario_general |
| `LEXR-01293` | jytjẽeyũu- | quedar suspendido | diccionario_general |
| `LEXR-01294` | jytuwúu- | acortarse | diccionario_general |
| `LEXR-01295` | jyu’ja- | 1. crecer (largo); 2. prolongarse, alargarse | diccionario_general |
| `LEXR-01296` | jyucaysa, jyucasay | todos | diccionario_general |
| `LEXR-01297` | luuchíi | desde la niñez | diccionario_general |
| `LEXR-01298` | mee- | no | diccionario_general |
| `LEXR-01299` | meeme | el higuillo (árbol) | diccionario_general |
| `LEXR-01300` | mend | ¡Quiébrelo! | diccionario_general |
| `LEXR-01301` | neeney | el padrino | diccionario_general |
| `LEXR-01302` | nenga reinu | sal de Zipaquirá | diccionario_general |
| `LEXR-01303` | npeevyshijca-, npeevyshica- (npeeshijca-) | burlar | diccionario_general |
| `LEXR-01304` | nuychji’ndy-, nuychji’ndyi | obscurecer | diccionario_general |
| `LEXR-01305` | nuychjãchja- | fortalecer | diccionario_general |
| `LEXR-01306` | nuytape- | ensanchar | diccionario_general |
| `LEXR-01307` | paawe’weni | encargo | diccionario_general |
| `LEXR-01308` | paaũ’cj-, paaũ’cju- | participar en la molienda | diccionario_general |
| `LEXR-01309` | pe’ltende- | partir en varios pedazos, despedazar | diccionario_general |
| `LEXR-01310` | pland | plátano | diccionario_general |
| `LEXR-01311` | puta-, putáa- | oler | diccionario_general |
| `LEXR-01312` | puutsuts-, puutsutsu- | 1. repartir comida (entre varias personas) 2. meter caña (en la trapiche) | diccionario_general |
| `LEXR-01313` | puuty ya’peltunaĩ- | perdonarse | diccionario_general |
| `LEXR-01314` | pũ’tyj-, pũ’tyji- | empezar | diccionario_general |
| `LEXR-01315` | quite ej | jardín | diccionario_general |
| `LEXR-01316` | quiwe tujnd | el polvo (del camino) | diccionario_general |
| `LEXR-01317` | scand-, scandúu- | envolver | diccionario_general |
| `LEXR-01318` | sec paatsu- | ocultarse el sol | diccionario_general |
| `LEXR-01319` | shaacue yasa | el apodo | diccionario_general |
| `LEXR-01320` | shaacãj | calambre | diccionario_general |
| `LEXR-01321` | shimb ets | la hoja de maíz | diccionario_general |
| `LEXR-01322` | siyula | la señora (de raza blanca) | diccionario_general |
| `LEXR-01323` | smeme quits | vereda de Mariposas | diccionario_general |
| `LEXR-01324` | snacja | la maraca | diccionario_general |
| `LEXR-01325` | ta’tsu’ju- | poner torcido, encorvar | diccionario_general |
| `LEXR-01326` | tecja | la teja | diccionario_general |
| `LEXR-01327` | teecjẽe | boca abajo | diccionario_general |
| `LEXR-01328` | tsjende upj | cerca de palos verticales | diccionario_general |
| `LEXR-01329` | tut-, tutúu- | picar, hacer pedazos, roer | diccionario_general |
| `LEXR-01330` | tutjensa (T) | gobernador indígena del resguardo | diccionario_general |
| `LEXR-01331` | twẽeji- | conversar, charlar | diccionario_general |
| `LEXR-01332` | tyity pusu | el pozo de barro (para hacer teja) | diccionario_general |
| `LEXR-01333` | tyujnde-, tyunde- | separar, repartir, dividir, apartar | diccionario_general |
| `LEXR-01334` | tũupi’j-, tũupi’ji- | 1. desyerbar; 2. desvestir | diccionario_general |
| `LEXR-01335` | ul ñavytuć | mataganado (culebra) | diccionario_general |
| `LEXR-01336` | vijcha | pájaro | diccionario_general |
| `LEXR-01337` | wats | la roza | diccionario_general |
| `LEXR-01338` | wecha pu’ch- | felicitar | diccionario_general |
| `LEXR-01339` | wej yat | puente techado | diccionario_general |
| `LEXR-01340` | weysá | comprador, que compra | diccionario_general |
| `LEXR-01341` | ya’iweech- | ser burlado | diccionario_general |
| `LEXR-01342` | yu’a- | volverse agua | diccionario_general |
| `LEXR-01343` | yu’mityj | el cántaro | diccionario_general |
| `LEXR-01344` | yujnz | la aguja | diccionario_general |
| `LEXR-01345` | yul pẽysa | cobrador | diccionario_general |
| `LEXR-01346` | yuu- | ser | diccionario_general |
| `LEXR-01347` | yuusá | que viene | diccionario_general |
| `LEXR-01348` | zunz, zunzcuẽ | 1. delgado; 2.tono muy agudo (música) | diccionario_general |
| `LEXR-01349` | ñaja- (yãja-) | chuzar, punzar | diccionario_general |
| `LEXR-01350` | ñusha | dulce (sabor) | diccionario_general |
| `LEXR-01351` | ũ’ jyaw yat | el troje, granero | diccionario_general |
| `LEXR-01352` | ũ’ne pety cjacj | llanto | diccionario_general |
| `LEXR-01353` | ũpjũupj-, ũpjũupju- | 1. saltar (repetidas veces); 2. palpitar, latir | diccionario_general |
| `LEXR-01354` | ũucjmée | sin miedo | diccionario_general |
| `LEXR-01355` | ẽe cjũch | nube obscura (mal agüero) | diccionario_general |
| `LEXR-01356` | ẽe cytã’ | la escarcha | diccionario_general |
| `LEXR-01357` | a’mbande- | 1. derrumbar 2. arar, sacar paladas | diccionario_general |
| `LEXR-01358` | ajwned- | dar latigo | diccionario_general |
| `LEXR-01359` | animus | la ánima, la alma del difunto | diccionario_general |
| `LEXR-01360` | atsa’ | y | diccionario_general |
| `LEXR-01361` | atsewe’we | hablar contra otro | diccionario_general |
| `LEXR-01362` | beca sec, cuty beca | chicha de maíz | diccionario_general |
| `LEXR-01363` | bu’ch, bu’chi- | empezar a hervir, burbjear | diccionario_general |
| `LEXR-01364` | bu’mbu- | hacer ruido, retumbar | diccionario_general |
| `LEXR-01365` | caacjẽu’j-, caacjẽuju- | dejar pasar (para arriba) | diccionario_general |
| `LEXR-01366` | caasyũyũj-, caasyũyũju- | hacer sonar (maraca) | diccionario_general |
| `LEXR-01367` | catsundenimeesa | anaco tubular | diccionario_general |
| `LEXR-01368` | cchjãachja’j-, cchjãachja’ja- | fortalecer, animar | diccionario_general |
| `LEXR-01369` | cja’cjunde- | descolgar, quitar | diccionario_general |
| `LEXR-01370` | cjĩj | la caña brava (planta) | diccionario_general |
| `LEXR-01371` | cseelpi’j-. cseelpi’ji- | hacer servir, ocupar, utilizar, usar | diccionario_general |
| `LEXR-01372` | cutyj bite | maíz pintado | diccionario_general |
| `LEXR-01373` | cutyj cjas | pelusa de maíz | diccionario_general |
| `LEXR-01374` | cutyj dyi’tj | caña de maíz | diccionario_general |
| `LEXR-01375` | cweetj-, cweetje- | alumbrar, iluminar | diccionario_general |
| `LEXR-01376` | cytã’ | la basura | diccionario_general |
| `LEXR-01377` | deewẽeni | sueño | diccionario_general |
| `LEXR-01378` | e’ts, e’tscuẽ | esmeralda, colibrí (ave) | diccionario_general |
| `LEXR-01379` | ewcha | !Hola! (saludando a un hombre) | diccionario_general |
| `LEXR-01380` | fitscu’ng | el nudillo (planta) | diccionario_general |
| `LEXR-01381` | iiũ’- | comer | diccionario_general |
| `LEXR-01382` | ipyñiñ | colorado, rojizo | diccionario_general |
| `LEXR-01383` | jembu cuseju | zurdo | diccionario_general |
| `LEXR-01384` | jycaani | la orden, el mandato | diccionario_general |
| `LEXR-01385` | jycja’ctende- | descolgarse, librarse de, desechar una acusación | diccionario_general |
| `LEXR-01386` | leng-, lengu- | cojear | diccionario_general |
| `LEXR-01387` | lu’l-, lu’lu- | moler (cosa aquada) | diccionario_general |
| `LEXR-01388` | ma’wẽnva | cuandoquiera, cualquier hora | diccionario_general |
| `LEXR-01389` | nes | permanentamente | diccionario_general |
| `LEXR-01390` | ney | el padre | diccionario_general |
| `LEXR-01391` | nmejtewe’sh | postrero | diccionario_general |
| `LEXR-01392` | nus muse | llovizna | diccionario_general |
| `LEXR-01393` | palsin | barsino | diccionario_general |
| `LEXR-01394` | pandsa | que barre | diccionario_general |
| `LEXR-01395` | pas-, pasu- | 1. contestar 2. comprometerse | diccionario_general |
| `LEXR-01396` | pelgatyi | la alpargata | diccionario_general |
| `LEXR-01397` | peña | barranco | diccionario_general |
| `LEXR-01398` | piishá | oveja | diccionario_general |
| `LEXR-01399` | pniisa | padre o madre con la hija | diccionario_general |
| `LEXR-01400` | pquivy-, pquiivi- | derretirse | diccionario_general |
| `LEXR-01401` | pucacje pyacj | primo con primo o prima con prima | diccionario_general |
| `LEXR-01402` | punga wee | colerín | diccionario_general |
| `LEXR-01403` | putatyjã’ | hierbabuena (planta) | diccionario_general |
| `LEXR-01404` | pẽtyj | la garganta | diccionario_general |
| `LEXR-01405` | shcandende- | fracturar (varias veces o en varias partes) | diccionario_general |
| `LEXR-01406` | shi’ndy (chji’ndy) | obscuro | diccionario_general |
| `LEXR-01407` | shi’ta- | humear | diccionario_general |
| `LEXR-01408` | shinde’nde- | erizar (varias veces) | diccionario_general |
| `LEXR-01409` | shita-, shitáa- | bramar | diccionario_general |
| `LEXR-01410` | shlalá | granadillo | diccionario_general |
| `LEXR-01411` | spajndspajnde | algo templado (freno) | diccionario_general |
| `LEXR-01412` | spulla | la cebolla (planta, de raíz comestible) | diccionario_general |
| `LEXR-01413` | styãa | manso | diccionario_general |
| `LEXR-01414` | taqui’nisa | animal domesticado | diccionario_general |
| `LEXR-01415` | tata | padre | diccionario_general |
| `LEXR-01416` | teech | uno | diccionario_general |
| `LEXR-01417` | teepjute- | dar volteretas | diccionario_general |
| `LEXR-01418` | tjaacue | más, grave, peor | diccionario_general |
| `LEXR-01419` | tupa | araña | diccionario_general |
| `LEXR-01420` | tupji- | voltearse, volver | diccionario_general |
| `LEXR-01421` | tuwtuw | más corto | diccionario_general |
| `LEXR-01422` | um-, umúu- | 1. tejer (jigra, ruana); 2. techar, empajar una casa | diccionario_general |
| `LEXR-01423` | uujsa | sembrador, que siembra | diccionario_general |
| `LEXR-01424` | wa’ | el rancho, cobertizo | diccionario_general |
| `LEXR-01425` | wat-, watúu- | dorarse | diccionario_general |
| `LEXR-01426` | wee cnay- | padecer una enfermdad | diccionario_general |
| `LEXR-01427` | wenze | mono nocturno | diccionario_general |
| `LEXR-01428` | yu’cj cuchi | agutí, guatuza, tuza (mamífero) | diccionario_general |
| `LEXR-01429` | yu’pusu | el pozo | diccionario_general |
| `LEXR-01430` | yus-, yusu- | dar de beber | diccionario_general |
| `LEXR-01431` | ñunz vits | la punta de la aguja | diccionario_general |
| `LEXR-01432` | ĩcy-, ĩqui- | regañar, reprender | diccionario_general |
| `LEXR-01433` | ĩts puty | narices, ventana de la nariz | diccionario_general |
| `LEXR-01434` | ĩtyĩ | vivo, viviente | diccionario_general |
| `LEXR-01435` | ũ’-, ũwe- | 1. comer; 2. mascar coca, mambear; 3. picar | diccionario_general |
| `LEXR-01436` | ũujũucjsa | temible | diccionario_general |
| `LEXR-01437` | ũuse’se- | jadear, respirar con dificultad | diccionario_general |
| `LEXR-01438` | alcu, alcucuẽ | el perro | diccionario_general |
| `LEXR-01439` | ambu’j-, ambu’ju- | alzar era | diccionario_general |
| `LEXR-01440` | beecãj-, beecãja- | sonrojarse | diccionario_general |
| `LEXR-01441` | calderu | la caldera | diccionario_general |
| `LEXR-01442` | chita- | colgar | diccionario_general |
| `LEXR-01443` | claapatu | el garabato | diccionario_general |
| `LEXR-01444` | cpaanwe’we- | lograr intervenir | diccionario_general |
| `LEXR-01445` | ctiishi’j-, ctiishi’ji- | hacer parar | diccionario_general |
| `LEXR-01446` | cwa’lu’j-, cwa’lu’ju- | causar pereza, desanimar | diccionario_general |
| `LEXR-01447` | cweenzhi’j-, cweenzhi’ji- | hacer arrastrar | diccionario_general |
| `LEXR-01448` | cã’tu’j-, cã’tu’ju- | mojarse | diccionario_general |
| `LEXR-01449` | cãja’j-, cãja’ja- | completar | diccionario_general |
| `LEXR-01450` | duu yat | el nido | diccionario_general |
| `LEXR-01451` | e’nz | dos | diccionario_general |
| `LEXR-01452` | ejwa | el cucharón (de madera) | diccionario_general |
| `LEXR-01453` | fiinze’j-, fiinze’je- | enfriar, refrescar | diccionario_general |
| `LEXR-01454` | fina-(fiina-) | ahorrar (comida o dinero) | diccionario_general |
| `LEXR-01455` | fitsj | el cuí, conejillo de indias (mamífero) | diccionario_general |
| `LEXR-01456` | fytũu pagayú | el carpintero (ave) | diccionario_general |
| `LEXR-01457` | i’cue’sh | suyo | diccionario_general |
| `LEXR-01458` | jypujnza-, jypuunza- | terciar, llevar terciado | diccionario_general |
| `LEXR-01459` | jytandyi | alrededor | diccionario_general |
| `LEXR-01460` | jyu’juwe’sh | extranjero, forastero | diccionario_general |
| `LEXR-01461` | jyumbani | error, equivocación | diccionario_general |
| `LEXR-01462` | mee | ¡Diga! | diccionario_general |
| `LEXR-01463` | neeyũu- | 1. prometer 2. enterarse | diccionario_general |
| `LEXR-01464` | npe’sh | la hermana (respecto al hombre) | diccionario_general |
| `LEXR-01465` | npi’qui | la compañera (mujer que cohabita con un hombre sin casarse) | diccionario_general |
| `LEXR-01466` | npiitstjẽj, npiitstjẽ’jsa | el jefe | diccionario_general |
| `LEXR-01467` | nus pa’jni ĩcj | el diluvio | diccionario_general |
| `LEXR-01468` | paau’j-, paau’jue- | ir, aprovechando la oportunidad de acompañar a otro | diccionario_general |
| `LEXR-01469` | paaũucjsa | tímido, temeroso, miedoso | diccionario_general |
| `LEXR-01470` | pecue’cue- | dar paliza (repetidas veces) | diccionario_general |
| `LEXR-01471` | peejyũcue- | arrodillarse | diccionario_general |
| `LEXR-01472` | peessa | que regala | diccionario_general |
| `LEXR-01473` | pi’cy-, pi’qui- | invitar, convidar | diccionario_general |
| `LEXR-01474` | piisháa | la oveja | diccionario_general |
| `LEXR-01475` | pllaana’ | ácido | diccionario_general |
| `LEXR-01476` | pucate | al lado de | diccionario_general |
| `LEXR-01477` | pwa’ | el corredor (de la casa), sitio cubierto | diccionario_general |
| `LEXR-01478` | pwe’sh | pariente (con respecto a otro pariente | diccionario_general |
| `LEXR-01479` | pwel | cubios | diccionario_general |
| `LEXR-01480` | pẽtyj-, pẽtyj- | derribar, tumbar | diccionario_general |
| `LEXR-01481` | quiitj | vertical | diccionario_general |
| `LEXR-01482` | quitj ej | sembrado de maní | diccionario_general |
| `LEXR-01483` | shimb dyi’tj | el tallo de maíz | diccionario_general |
| `LEXR-01484` | spay-, spayúu- | mirar a lo lejos | diccionario_general |
| `LEXR-01485` | spiina’sa | brea | diccionario_general |
| `LEXR-01486` | swejnde-, swende- | agujerear, taladrar, perforar | diccionario_general |
| `LEXR-01487` | tajta | frecuentemente, con frecuencia, a menudo | diccionario_general |
| `LEXR-01488` | tejca-, teeca- | subir, ascender, trepar | diccionario_general |
| `LEXR-01489` | tyãa (cyãa) | él, ella, aquel, aquella, ese, esa | diccionario_general |
| `LEXR-01490` | tũusá | el borracho | diccionario_general |
| `LEXR-01491` | vicysa | cazador | diccionario_general |
| `LEXR-01492` | vite | otro | diccionario_general |
| `LEXR-01493` | wacaaga- | cortar (en muchos pedazos) | diccionario_general |
| `LEXR-01494` | wãca’ca- | tambalear | diccionario_general |
| `LEXR-01495` | wẽsẽ’jsa | oyente | diccionario_general |
| `LEXR-01496` | yaat- | llevar en la mano | diccionario_general |
| `LEXR-01497` | yuj-, yuwée-, yuu- | venir | diccionario_general |
| `LEXR-01498` | yuutya- | unir | diccionario_general |
| `LEXR-01499` | ãchwe’sh | reciente (ej. oficiales recientement elegidos) | diccionario_general |
| `LEXR-01500` | ãsh-, ãshi- | echar granos, apuntar | diccionario_general |
| `LEXR-01501` | ãwã pijts | el ají picante (planta, usada como condimento) | diccionario_general |
| `LEXR-01502` | ñauñú | curuba | diccionario_general |
| `LEXR-01503` | ñiñ acj- | echar grano, cargar | diccionario_general |
| `LEXR-01504` | ñussa | la tristeza, angustia | diccionario_general |
| `LEXR-01505` | ĩtyĩ fi’nze | vivir, estar vivo | diccionario_general |
| `LEXR-01506` | ũ’cue (ũ’c J) | yo (femenino) | diccionario_general |
| `LEXR-01507` | ũ’na cus | al año pasado | diccionario_general |
| `LEXR-01508` | ẽepshũ | la sombra | diccionario_general |
| `LEXR-01509` | a’pja’pja- | aletear | diccionario_general |
| `LEXR-01510` | acach-, acachji- | caer encima de | diccionario_general |
| `LEXR-01511` | caagastaĩ’j-, caagastaĩ’jji- | hacer gastar | diccionario_general |
| `LEXR-01512` | caateca-j-, caateca’ja- | hacer subir | diccionario_general |
| `LEXR-01513` | caatenzu’j-, caatenzu’ju- | cargar debajo del brazo | diccionario_general |
| `LEXR-01514` | caavi’j-, caavi’ji- | hacer escupir | diccionario_general |
| `LEXR-01515` | cdeewe’j-, cdeewe’je- | hacer pagar | diccionario_general |
| `LEXR-01516` | cjã’cjã | la hormiga (insecto) | diccionario_general |
| `LEXR-01517` | cjũuchji’j-, cjũuchji’ji- | ensuciar, tiznar | diccionario_general |
| `LEXR-01518` | cne’s- | hechizar | diccionario_general |
| `LEXR-01519` | cpã | la herida, lastimadura | diccionario_general |
| `LEXR-01520` | csinela | la cocinera | diccionario_general |
| `LEXR-01521` | cuse mush | el dedo | diccionario_general |
| `LEXR-01522` | cuspyãj | la medianoche | diccionario_general |
| `LEXR-01523` | cyaandu- | rodear | diccionario_general |
| `LEXR-01524` | cyũ’wẽ’j-, cyũ’wẽ’je- | dar sed, causar sed | diccionario_general |
| `LEXR-01525` | cãtsa | coatí, cusumbe | diccionario_general |
| `LEXR-01526` | ele | cosquillas | diccionario_general |
| `LEXR-01527` | fi’j | rayado | diccionario_general |
| `LEXR-01528` | fytũu ets | la hoja | diccionario_general |
| `LEXR-01529` | iipuiisa | el enemigo | diccionario_general |
| `LEXR-01530` | indy yacj | contigo, con usted | diccionario_general |
| `LEXR-01531` | ipy cleechi | la llama | diccionario_general |
| `LEXR-01532` | je’ng | el paladar | diccionario_general |
| `LEXR-01533` | jyta’ñi- | sentir ’señas’, adivinar por sensaciones en el cuerpo | diccionario_general |
| `LEXR-01534` | jũ’na añu | el año pasado | diccionario_general |
| `LEXR-01535` | lavy-, lavi- | ponerse liso, resbaloso | diccionario_general |
| `LEXR-01536` | mtee mteeva | en todas partes | diccionario_general |
| `LEXR-01537` | mushca (T) | blanco (persona de raza blanca) | diccionario_general |
| `LEXR-01538` | ne’jue’sh | el gobernador (del resguardo) | diccionario_general |
| `LEXR-01539` | nicy-, niqui- | traer, cargar | diccionario_general |
| `LEXR-01540` | nshijca-, nshica- | reirse de | diccionario_general |
| `LEXR-01541` | ntsu’wa | el cuñado, la cuñada (entre los dos sexos) | diccionario_general |
| `LEXR-01542` | pajnde-, pande- | 1. zafar, quitar 2. desenfrenar | diccionario_general |
| `LEXR-01543` | pastu | el pasto | diccionario_general |
| `LEXR-01544` | pjatete- | rajarse (en varias partes) | diccionario_general |
| `LEXR-01545` | pju’se’j-, pju’se’je- | renovar | diccionario_general |
| `LEXR-01546` | pqui’ta- (fyqui’ta-) | encender, alumbrar | diccionario_general |
| `LEXR-01547` | ptyute-, ptyutée- | dividirse, separarse, bifurcarse | diccionario_general |
| `LEXR-01548` | pu’quisu’s-, pu’quisu’su- | alzar (repetidas veces) | diccionario_general |
| `LEXR-01549` | pyũuscue- | dar rabia | diccionario_general |
| `LEXR-01550` | pẽysa | que pide | diccionario_general |
| `LEXR-01551` | qui’su | la semana | diccionario_general |
| `LEXR-01552` | quiisa’j-, quiisa’ja- | hacer medir, hacer contar, hacer probar | diccionario_general |
| `LEXR-01553` | quiwendawa | centella (planta) | diccionario_general |
| `LEXR-01554` | scuutyj ej | el trigal | diccionario_general |
| `LEXR-01555` | shumatyjã’ | (planta, que da sabor a la comida) | diccionario_general |
| `LEXR-01556` | taw | la faja, el chumbe | diccionario_general |
| `LEXR-01557` | tjengmée nvijt- | abandonar | diccionario_general |
| `LEXR-01558` | tjãasni | deseo, voluntad | diccionario_general |
| `LEXR-01559` | tujnd | el polvo | diccionario_general |
| `LEXR-01560` | tuutje’jni | fama | diccionario_general |
| `LEXR-01561` | tyiclli | tigrillo | diccionario_general |
| `LEXR-01562` | vit-, vitu- | 1. hacer; 2. designar; 3. redimir | diccionario_general |
| `LEXR-01563` | wa’lmée | voluntariamente, de buena gana | diccionario_general |
| `LEXR-01564` | waacji’cj-, waacji’cji- | pisotear, pisar | diccionario_general |
| `LEXR-01565` | wantaĩ- | aguantar | diccionario_general |
| `LEXR-01566` | wats-, watsu- | rozar | diccionario_general |
| `LEXR-01567` | we’wesa | que habla | diccionario_general |
| `LEXR-01568` | wecha caaj- | mandar saludos | diccionario_general |
| `LEXR-01569` | wuw-, wuwu- | escarbar | diccionario_general |
| `LEXR-01570` | wãcã | cangrejo | diccionario_general |
| `LEXR-01571` | ya’cysus-, ya’cysusu- | ser nombrado | diccionario_general |
| `LEXR-01572` | ya’wecha- | llamarse | diccionario_general |
| `LEXR-01573` | yaja- | amargar, ponerse amargo | diccionario_general |
| `LEXR-01574` | yuwe ptsuu- | terminar un asunto | diccionario_general |
| `LEXR-01575` | ãtsã’ | enfermo | diccionario_general |
| `LEXR-01576` | ĩcywe’we- | regañar, censurar | diccionario_general |
| `LEXR-01577` | ĩish-, ĩishi- | envejecerse (hombre o cosa) | diccionario_general |
| `LEXR-01578` | ũ’shic | glotón | diccionario_general |
| `LEXR-01579` | -ju | con | diccionario_general |
| `LEXR-01580` | andtende- | desenvolver | diccionario_general |
| `LEXR-01581` | atjni | vestido | diccionario_general |
| `LEXR-01582` | atscue- | desplomarse, tambalear | diccionario_general |
| `LEXR-01583` | atyj | la ruana, el anaco | diccionario_general |
| `LEXR-01584` | atyj pets | ruana o anaco delgado | diccionario_general |
| `LEXR-01585` | byuu bee altal | altar dorado | diccionario_general |
| `LEXR-01586` | caatwaca’j-, caatwaca’ja- | hacer cortar (palo) | diccionario_general |
| `LEXR-01587` | caañiishi’j-, caañiishi’ji-(cniishi’j-) | hacer engordar | diccionario_general |
| `LEXR-01588` | capla | cabra | diccionario_general |
| `LEXR-01589` | catyji- | mejorarse (de una enfermedad) | diccionario_general |
| `LEXR-01590` | chijme yuu- | ponerse pálido | diccionario_general |
| `LEXR-01591` | claatyi | el carate (especie de sarna) | diccionario_general |
| `LEXR-01592` | csemba | diez | diccionario_general |
| `LEXR-01593` | cuch sus-, cuch susu- | molestar (un ruido), hacer bulla | diccionario_general |
| `LEXR-01594` | cuse njĩ’j | el pulgar | diccionario_general |
| `LEXR-01595` | cuuta’j-, cuuta’ja- | hartarse | diccionario_general |
| `LEXR-01596` | cuutsje’j-, cuutsje’je- | dejar tocar, permitir tocar | diccionario_general |
| `LEXR-01597` | fitse- | espesarse, ponerse espeso | diccionario_general |
| `LEXR-01598` | iica’ca- | golpear (repetidas veces), aglomerarse | diccionario_general |
| `LEXR-01599` | inz | orín | diccionario_general |
| `LEXR-01600` | jyumbamée | acertadamente, sin equivocarse | diccionario_general |
| `LEXR-01601` | mushclé | el huarango (árbol) | diccionario_general |
| `LEXR-01602` | mẽpa | ¡Dispare! | diccionario_general |
| `LEXR-01603` | nmi’ | el esposo, marido | diccionario_general |
| `LEXR-01604` | nuycase- | aliviar | diccionario_general |
| `LEXR-01605` | nuypusu- | permitir fermentar | diccionario_general |
| `LEXR-01606` | nyafytewe’sh | el primero, los primeros | diccionario_general |
| `LEXR-01607` | pe’late- | hacerse pedazos | diccionario_general |
| `LEXR-01608` | peevisha’j-, peevisha’ja- | rehusar dar o gastar (repetidas veces) | diccionario_general |
| `LEXR-01609` | pi’cy yat | la casa de la minga | diccionario_general |
| `LEXR-01610` | piisháa tjengsa | el pastor de ovejas | diccionario_general |
| `LEXR-01611` | pitscuẽ | el muchaco | diccionario_general |
| `LEXR-01612` | pland ej | platanal | diccionario_general |
| `LEXR-01613` | preesu’ji-, preesu’ju- | tomar preso, aprisionar | diccionario_general |
| `LEXR-01614` | puuty uy-, puuty uyúu- | encontrarse con otro | diccionario_general |
| `LEXR-01615` | pwel | mafafa (planta comestible) | diccionario_general |
| `LEXR-01616` | sec shi’ndy- | haber eclipse de sol | diccionario_general |
| `LEXR-01617` | shamb | el ombligo | diccionario_general |
| `LEXR-01618` | shambsá | habitante del pueblo | diccionario_general |
| `LEXR-01619` | shuuna’ nvijt- | callar, hacer callar | diccionario_general |
| `LEXR-01620` | shũcy | molleja | diccionario_general |
| `LEXR-01621` | tuca ĩts | calabazo (en forma embudo) | diccionario_general |
| `LEXR-01622` | tucja-, tucjáa- | supurar | diccionario_general |
| `LEXR-01623` | tumb luuch | pichón (ave) | diccionario_general |
| `LEXR-01624` | tuw | corto | diccionario_general |
| `LEXR-01625` | tũu | la borrachera | diccionario_general |
| `LEXR-01626` | ucje’j-, ucje’je- | culpar, juzgar | diccionario_general |
| `LEXR-01627` | uja’ja- | sembrar (diversas semillas) | diccionario_general |
| `LEXR-01628` | vite quiwejuwe’sh | el extranjero, forastero | diccionario_general |
| `LEXR-01629` | vyuu mush | monedas fraccionarias | diccionario_general |
| `LEXR-01630` | wãyãy, wẽyĩy | comadreja | diccionario_general |
| `LEXR-01631` | yajcy | la trampa (con soga) | diccionario_general |
| `LEXR-01632` | yat punza | rincón de la casa | diccionario_general |
| `LEXR-01633` | yuwe ũssa | que presenta queja, demanda | diccionario_general |
| `LEXR-01634` | ziyaj-, ziyaji- | chirriar | diccionario_general |
| `LEXR-01635` | ñusha beca | el guarapo, chicha de caña de azúcar | diccionario_general |
| `LEXR-01636` | ñusha jypa’gasa | el que recibe cañaen el trapiche | diccionario_general |
| `LEXR-01637` | ũtj | batata | diccionario_general |
| `LEXR-01638` | ũytas, ũytjasu- | esperar | diccionario_general |
| `LEXR-01639` | ẽeũy | de un lado a otro | diccionario_general |
| `LEXR-01640` | a’mbate- | desarraigarse | diccionario_general |
| `LEXR-01641` | acy | macana | diccionario_general |
| `LEXR-01642` | atall cjas | la pluma (de gallina) | diccionario_general |
| `LEXR-01643` | atresesa | el enemigo | diccionario_general |
| `LEXR-01644` | buts | la larva | diccionario_general |
| `LEXR-01645` | caacambu’j’, caacambu’ju- | hacer quemar | diccionario_general |
| `LEXR-01646` | caachji’j-, caachi’ji- | hacer sentarse | diccionario_general |
| `LEXR-01647` | caanuqui’j-, caanuqui’ji- | pegar con goma | diccionario_general |
| `LEXR-01648` | caapeswe’j-, caapeswe’je- | dejar robar | diccionario_general |
| `LEXR-01649` | canzh yuusa | adúltero/a | diccionario_general |
| `LEXR-01650` | cats-, catsu- | coser, costurar | diccionario_general |
| `LEXR-01651` | catstende’ | descoser (varias costuras) | diccionario_general |
| `LEXR-01652` | chamba | la zanja | diccionario_general |
| `LEXR-01653` | chavy tjacue fytũ | cerote (árbol) | diccionario_general |
| `LEXR-01654` | chimby-, chimbíi- | podrir | diccionario_general |
| `LEXR-01655` | cjã’-, cjã’a- | abrigarse | diccionario_general |
| `LEXR-01656` | cjũchji | ennegrecer, ponerse negro | diccionario_general |
| `LEXR-01657` | cujya | el caldo, la sopa | diccionario_general |
| `LEXR-01658` | e’swe’sh | descendiente | diccionario_general |
| `LEXR-01659` | ewchacue | !Hola! (saludando a una mujer o a varias personas) | diccionario_general |
| `LEXR-01660` | ewmeete nyijt- | condenar | diccionario_general |
| `LEXR-01661` | fytũu chica | comején | diccionario_general |
| `LEXR-01662` | isani | balanza, romana | diccionario_general |
| `LEXR-01663` | jande | muy (árbol, que carga pepa) | diccionario_general |
| `LEXR-01664` | laavi’j-, laavi’ji- | alisar | diccionario_general |
| `LEXR-01665` | mama | madre | diccionario_general |
| `LEXR-01666` | mama wala | la abuela, bisabuela | diccionario_general |
| `LEXR-01667` | nyacj | hermano, hermana (del mismo sexo) | diccionario_general |
| `LEXR-01668` | nũ’we- | comer lo ajeno | diccionario_general |
| `LEXR-01669` | pa’pchu- | procurar, esforzarse, afanarse | diccionario_general |
| `LEXR-01670` | paandewe- | pagar por otro | diccionario_general |
| `LEXR-01671` | paatste | secretamente, en secreto | diccionario_general |
| `LEXR-01672` | pagayu’yu- | mirar arriba (repetidas veces) | diccionario_general |
| `LEXR-01673` | paytjame’ | vergonzoso | diccionario_general |
| `LEXR-01674` | pcal | el pecado | diccionario_general |
| `LEXR-01675` | pdyiy | hermano con hermana | diccionario_general |
| `LEXR-01676` | pe’lande- | partir en dos, dividir | diccionario_general |
| `LEXR-01677` | peejini | necesidad | diccionario_general |
| `LEXR-01678` | peswe-, peswée- | robar | diccionario_general |
| `LEXR-01679` | petsetesa | astilla | diccionario_general |
| `LEXR-01680` | piishá cjas | lana de oveja | diccionario_general |
| `LEXR-01681` | pu’chji’ch-, pu’chji’chji- | ayudar (por turno) | diccionario_general |
| `LEXR-01682` | puii-jypaacuesa | peleador, pleitista | diccionario_general |
| `LEXR-01683` | taty wej | puente arqueado | diccionario_general |
| `LEXR-01684` | tsejctsejc | color claro | diccionario_general |
| `LEXR-01685` | tymi | la tusa de maíz | diccionario_general |
| `LEXR-01686` | ucue quiwe | el valle | diccionario_general |
| `LEXR-01687` | ul jycuet bej | el gusano, larva | diccionario_general |
| `LEXR-01688` | unzafy (J) | dibujo que usan para el chumbe | diccionario_general |
| `LEXR-01689` | uschi’ | la tijereta (ave) | diccionario_general |
| `LEXR-01690` | usmity | el alacrán (arácnido venenoso) | diccionario_general |
| `LEXR-01691` | utyutya | muy cerca | diccionario_general |
| `LEXR-01692` | uuni | muerto | diccionario_general |
| `LEXR-01693` | vxihçxa | pájaro | diccionario_general |
| `LEXR-01694` | waca- | 1. cosechar, segar, cortar; 2. esquilar | diccionario_general |
| `LEXR-01695` | wenzh-, wezhíi- | halar, arrastrar | diccionario_general |
| `LEXR-01696` | yap | envoltura | diccionario_general |
| `LEXR-01697` | yat cajcue (yat cuejcue) | techo de la casa | diccionario_general |
| `LEXR-01698` | yu’ finze | agua fría | diccionario_general |
| `LEXR-01699` | yu’ĩts | el ojo de agua, manatial | diccionario_general |
| `LEXR-01700` | yutyi | la fontanela | diccionario_general |
| `LEXR-01701` | zec | el filo | diccionario_general |
| `LEXR-01702` | zits ĩquĩ | huevo crudo | diccionario_general |
| `LEXR-01703` | ãtsã’na ũs- | estar enfermo | diccionario_general |
| `LEXR-01704` | ñauñú | la curuba (fruta) | diccionario_general |
| `LEXR-01705` | ñus (yũs) | triste | diccionario_general |
| `LEXR-01706` | ñusna ũs- | estar triste | diccionario_general |
| `LEXR-01707` | ĩcywe’weni | regaño | diccionario_general |
| `LEXR-01708` | ũuspa’- | asfixiarse | diccionario_general |
| `LEXR-01709` | atall ech | el tigrillo | diccionario_general |
| `LEXR-01710` | biu’ | avispado, vivo | diccionario_general |
| `LEXR-01711` | bus | mosquito (insecto) | diccionario_general |
| `LEXR-01712` | caapjeu’j-, caapjeu’ju- | hacer arreglar | diccionario_general |
| `LEXR-01713` | canzh yuuni | adulterio, inmoralidad | diccionario_general |
| `LEXR-01714` | chji’ndy-, chji’ndyi- | ponerse obscuro | diccionario_general |
| `LEXR-01715` | chjãchja | fuerte | diccionario_general |
| `LEXR-01716` | chwa’ ets | ala de sombrero | diccionario_general |
| `LEXR-01717` | cpeena’j-, cpeena’ja- | dejar pegar, permitir pegar | diccionario_general |
| `LEXR-01718` | cu’w-, cu’wu- | impartir (luz, calor, frío) | diccionario_general |
| `LEXR-01719` | cueneene- | relampaguear | diccionario_general |
| `LEXR-01720` | cupjy | luciérnaga | diccionario_general |
| `LEXR-01721` | cusa’j-, cusa’ja- | quitar, despojar | diccionario_general |
| `LEXR-01722` | cuutya’j-, cuutya’ja- | hacer acercar, arrimar | diccionario_general |
| `LEXR-01723` | cwẽeje’j-, cwẽeje’je- | causar hambre | diccionario_general |
| `LEXR-01724` | cwẽndyimbu | la zarza (planta) | diccionario_general |
| `LEXR-01725` | dulse | la panela | diccionario_general |
| `LEXR-01726` | ewuu- | mejorarse, componerse (el tiempo) | diccionario_general |
| `LEXR-01727` | fyu’fy-, fyu’fi- | silbar | diccionario_general |
| `LEXR-01728` | iitey casesa | niño prematuro | diccionario_general |
| `LEXR-01729` | iiuytjãs- | esperar | diccionario_general |
| `LEXR-01730` | iiyuu- | casarse (dícese del hombre) | diccionario_general |
| `LEXR-01731` | jimba chinda pẽty | cuartilla | diccionario_general |
| `LEXR-01732` | juuna’ yuu | tratar con severidad | diccionario_general |
| `LEXR-01733` | jycjũucj-, jycjũucju- | limpiarse (a uno mismo) | diccionario_general |
| `LEXR-01734` | jype’jnisa | entenado, a | diccionario_general |
| `LEXR-01735` | lawéch | el lagartijo | diccionario_general |
| `LEXR-01736` | llima ej | naranjal | diccionario_general |
| `LEXR-01737` | luuch icjsa | infanticida | diccionario_general |
| `LEXR-01738` | luuçx | niño | diccionario_general |
| `LEXR-01739` | mushi’j-, muushi’ji- | 1. despedazar 2. dar cambio (dinero) | diccionario_general |
| `LEXR-01740` | nasa yuwe we’wessa | persona que habla páez | diccionario_general |
| `LEXR-01741` | niisa nuuchsa | hija menor | diccionario_general |
| `LEXR-01742` | nus jyamby- | hacer llover | diccionario_general |
| `LEXR-01743` | nuyquite, nuyquitée- | hacer florecer | diccionario_general |
| `LEXR-01744` | nuytejca- | subir (ej. ladrillos) | diccionario_general |
| `LEXR-01745` | paatsu-, paatsúu- | desaparecer, ocultarse | diccionario_general |
| `LEXR-01746` | pe’ya | sobra | diccionario_general |
| `LEXR-01747` | peecydyiqui (peendyiqui) | la almohada | diccionario_general |
| `LEXR-01748` | pembasá | destructivo | diccionario_general |
| `LEXR-01749` | penzhíi- | envejercerse (mujer) | diccionario_general |
| `LEXR-01750` | preesu | el preso | diccionario_general |
| `LEXR-01751` | pteenzú | las tijeras | diccionario_general |
| `LEXR-01752` | pusni | tendido, sudadero | diccionario_general |
| `LEXR-01753` | pwel, ã’sh | mafafa | diccionario_general |
| `LEXR-01754` | qui’na- | chorrear | diccionario_general |
| `LEXR-01755` | scupeta | escopeta | diccionario_general |
| `LEXR-01756` | shumáa- | volverse pardo | diccionario_general |
| `LEXR-01757` | tacycue (J) | el sol | diccionario_general |
| `LEXR-01758` | taty wej | puente en forma de arco | diccionario_general |
| `LEXR-01759` | tsute | el encenillo (árbol, usado para leña) | diccionario_general |
| `LEXR-01760` | tuca vica | calabazo (en forma de gancho) | diccionario_general |
| `LEXR-01761` | tut | el puño | diccionario_general |
| `LEXR-01762` | tutyjte nasa ji’pjsa | mujer encinta, embarazada | diccionario_general |
| `LEXR-01763` | ujndy-, undyi- | 1. secarse; 2. agotarse | diccionario_general |
| `LEXR-01764` | wechana neeyũu- | quedar complacido | diccionario_general |
| `LEXR-01765` | wechani | gozo | diccionario_general |
| `LEXR-01766` | yaacynimeete | sorpresivamente, súbitamente | diccionario_general |
| `LEXR-01767` | yandy (ñandy T) | el nevado | diccionario_general |
| `LEXR-01768` | yase (yese) | el nombre | diccionario_general |
| `LEXR-01769` | yat namu | dueño de la casa | diccionario_general |
| `LEXR-01770` | yu’cypej-, yu’cypeje-, yu’cypee- | aconjesar | diccionario_general |
| `LEXR-01771` | yuu- | ser, llegar a ser | diccionario_general |
| `LEXR-01772` | ĩishweete | la vejez (refiriendo a un hombre) | diccionario_general |
| `LEXR-01773` | ũ’cjue’w | algo, bien | diccionario_general |
| `LEXR-01774` | -cjẽ | abajo | diccionario_general |
| `LEXR-01775` | anzu- | sonreir | diccionario_general |
| `LEXR-01776` | ayga | por acá | diccionario_general |
| `LEXR-01777` | buta wee | el sarampión | diccionario_general |
| `LEXR-01778` | caapã’chi’j-, caapã’chi’ji-(cpã’chi’j-) | hacer cubrirse | diccionario_general |
| `LEXR-01779` | capla, caplcuẽ | la cabra, el chivo | diccionario_general |
| `LEXR-01780` | chich ujndy | la cecina | diccionario_general |
| `LEXR-01781` | cjas pjapj | 1. la madeja de lana escarmenada 2. la pluma | diccionario_general |
| `LEXR-01782` | cmiisa | la camisa | diccionario_general |
| `LEXR-01783` | cpaacue’j-, cpaacue’je- | permitir buscar, mandar buscar | diccionario_general |
| `LEXR-01784` | cpi’sh we’we- | tronar | diccionario_general |
| `LEXR-01785` | ctsja’jya’j-, ctsja’jya’ja- | hacer extender los brazos | diccionario_general |
| `LEXR-01786` | cush | la vulva | diccionario_general |
| `LEXR-01787` | cweeyi’j-, cweeyi’ji- | hacer gritar | diccionario_general |
| `LEXR-01788` | dyi’wẽjẽ- | menospreciar | diccionario_general |
| `LEXR-01789` | fylele- | molestar, picar (pulga) | diccionario_general |
| `LEXR-01790` | fyneecu’c- | enjuagar | diccionario_general |
| `LEXR-01791` | i’cue’sh | su | diccionario_general |
| `LEXR-01792` | iitee, iitey | prematuro | diccionario_general |
| `LEXR-01793` | inz | hormiga grande (insecto) | diccionario_general |
| `LEXR-01794` | ipy ñiñ | el ascua, carbón encendido | diccionario_general |
| `LEXR-01795` | ju’ngusa | partidario | diccionario_general |
| `LEXR-01796` | me’j, me’jwe | ¡Vaya! | diccionario_general |
| `LEXR-01797` | na’wẽ, na’wẽy | 1. así 2. como, parecido | diccionario_general |
| `LEXR-01798` | naa quiwete | en esta tierra, en este mundo | diccionario_general |
| `LEXR-01799` | nasa pwe’sh | entre los de la misma tribu páez | diccionario_general |
| `LEXR-01800` | niish, niishi | el abuelo | diccionario_general |
| `LEXR-01801` | npaa | lo mismo como, igual que | diccionario_general |
| `LEXR-01802` | nus chu’ch | la llovizna | diccionario_general |
| `LEXR-01803` | paaũ’we-, (pũ’we-) | compartir la comida de otro | diccionario_general |
| `LEXR-01804` | pecuesa | que da paliza | diccionario_general |
| `LEXR-01805` | peetjé | el mejicano (calabaza) | diccionario_general |
| `LEXR-01806` | peeygãani | al amor, la misericordia | diccionario_general |
| `LEXR-01807` | pembe’mbe- | quejarse (enfermo) | diccionario_general |
| `LEXR-01808` | pinzh | el roble (árbol) | diccionario_general |
| `LEXR-01809` | pland ĩits | plátano maduro | diccionario_general |
| `LEXR-01810` | plenu | el frendo | diccionario_general |
| `LEXR-01811` | pneejĩ’j | madrina con ahijado o ahijada | diccionario_general |
| `LEXR-01812` | puuty puii- | pelear (unos con otros) | diccionario_general |
| `LEXR-01813` | quiicje’j-, quiicje’je- | mandar, matar | diccionario_general |
| `LEXR-01814` | quitj | maní (planta) | diccionario_general |
| `LEXR-01815` | sacueecue- | sacudir (repetidas veces) | diccionario_general |
| `LEXR-01816` | scuba | escoba | diccionario_general |
| `LEXR-01817` | sepu | el sebo | diccionario_general |
| `LEXR-01818` | shambúu- | reunirse, congregarse | diccionario_general |
| `LEXR-01819` | shũsh-, shũshúu- | 1. frotar, fregar, ungir, untar; 2. afilar (machete, hacha); 3. restregar trigo (con un mazo) | diccionario_general |
| `LEXR-01820` | sunde’nde- | romper | diccionario_general |
| `LEXR-01821` | sus we’we- | hablar en voz alta | diccionario_general |
| `LEXR-01822` | tata lul | el abuelo | diccionario_general |
| `LEXR-01823` | tjetj-, tjetjée- | apisonar | diccionario_general |
| `LEXR-01824` | tundysá | que toma | diccionario_general |
| `LEXR-01825` | u’jni | ida | diccionario_general |
| `LEXR-01826` | u’pni | el lugar de habitación, morada | diccionario_general |
| `LEXR-01827` | uj | el águila (ave) | diccionario_general |
| `LEXR-01828` | us | vez | diccionario_general |
| `LEXR-01829` | we’ll | tieso | diccionario_general |
| `LEXR-01830` | wãatãanisa | abadonado, cosa desechada | diccionario_general |
| `LEXR-01831` | wẽt, wẽtcuẽ | agradable, sabroso, saludable, bien (de salud) | diccionario_general |
| `LEXR-01832` | ya’ja wes | cargadera (de la jigra) | diccionario_general |
| `LEXR-01833` | yafy dyi’c | lágrima | diccionario_general |
| `LEXR-01835` | yu’nutre | nutria (mamífero) | diccionario_general |
| `LEXR-01836` | yucnenga | el rabo (de gallina) | diccionario_general |
| `LEXR-01837` | ¡uuju! | ¡Uy! (expresión de asombro) | diccionario_general |
| `LEXR-01838` | ẽejũjy | de arriba para abajo | diccionario_general |
| `LEXR-01839` | ẽeíi | temprano | diccionario_general |
| `LEXR-01840` | ẽs | el piojo (insecto) | diccionario_general |
| `LEXR-01841` | ẽsh pe’tse- | mascar coca | diccionario_general |
| `LEXR-01842` | aj | el humo | diccionario_general |
| `LEXR-01843` | ashnu | asno | diccionario_general |
| `LEXR-01844` | belen u’p- | estar suspendido | diccionario_general |
| `LEXR-01845` | caayu’ptje’j-, caayu’ptje’je- | hacer cambiar | diccionario_general |
| `LEXR-01846` | cambi´j-, cambi´ji- | hervir, dejar hervir | diccionario_general |
| `LEXR-01847` | capjute- | enderezarse | diccionario_general |
| `LEXR-01848` | chinda ca’ca | el tobillo, la espinilla | diccionario_general |
| `LEXR-01849` | chinda pil | la canilla | diccionario_general |
| `LEXR-01850` | cjũcj-, cjũcju- | borrar, limpiar (fregando) | diccionario_general |
| `LEXR-01851` | cpaapta’sh-, cpaapta’shi- | lograr avisar | diccionario_general |
| `LEXR-01852` | cupjat- | meter (cosa gruesa) | diccionario_general |
| `LEXR-01853` | cuptje’tje- | meter (repetidas veces) | diccionario_general |
| `LEXR-01854` | cute- | el lado opuesto | diccionario_general |
| `LEXR-01855` | cuẽ | el muchacho | diccionario_general |
| `LEXR-01856` | cyu’chafi’j-, cyu’chafi’ji- | hacer tropezar | diccionario_general |
| `LEXR-01857` | dund (tund) | aprisa, rápido, pronto | diccionario_general |
| `LEXR-01858` | duu- | parir, poner huevos (gallinas) | diccionario_general |
| `LEXR-01859` | echech | fregado | diccionario_general |
| `LEXR-01860` | ejnd u’j- | haber temblor, terremoto | diccionario_general |
| `LEXR-01861` | fiy yũu- | portarse mal | diccionario_general |
| `LEXR-01862` | fĩicj-, fĩicje- | poner sombrero | diccionario_general |
| `LEXR-01863` | ipy cjũch | candelilla (insecto) | diccionario_general |
| `LEXR-01864` | ju’ng | al lado do | diccionario_general |
| `LEXR-01865` | jycuutyi’j-, jycuutyi’ji-(jycuutyi’j-T) | desenfundar (machete), dar a luz | diccionario_general |
| `LEXR-01866` | jypejy-, jypeejy- | necesitar, hacer falta | diccionario_general |
| `LEXR-01867` | jypenda-, jypeendáa- | hundirse, zambullirse | diccionario_general |
| `LEXR-01868` | lupe | blando | diccionario_general |
| `LEXR-01869` | meerra, meerrava | o...o | diccionario_general |
| `LEXR-01870` | mityj yuc | asentadero de la olla | diccionario_general |
| `LEXR-01871` | newe- (neewe-) | detener, retener | diccionario_general |
| `LEXR-01872` | passa | que contesta | diccionario_general |
| `LEXR-01873` | pe’te- | amanecer (la persona) | diccionario_general |
| `LEXR-01874` | pets | delgado | diccionario_general |
| `LEXR-01875` | pi’qui’cy-, pi’qui’qui- | invitar a varias personas | diccionario_general |
| `LEXR-01876` | piicje | el matón | diccionario_general |
| `LEXR-01877` | pjande- | abrir | diccionario_general |
| `LEXR-01878` | pta’nzu’j-, pta’nzu’ju- | contaminar | diccionario_general |
| `LEXR-01879` | pẽty luwa | la nuez de la garganta | diccionario_general |
| `LEXR-01880` | quite-, quitée- | florecer | diccionario_general |
| `LEXR-01881` | siete | siete | diccionario_general |
| `LEXR-01882` | tjutj- tjutjúu- | ponerse tupido | diccionario_general |
| `LEXR-01883` | tumb | torcaz (ave) | diccionario_general |
| `LEXR-01884` | tyjicj | la garganta, cuello | diccionario_general |
| `LEXR-01885` | tyjityij-, tyjityiji- | escoger | diccionario_general |
| `LEXR-01886` | tyã’wẽ, tyã’wẽy (cyã’wẽ) | así, asimismo | diccionario_general |
| `LEXR-01887` | u’j-, u’jue- | seguir, continuar haciendo algo | diccionario_general |
| `LEXR-01888` | ucje- | espinarse, chuzar | diccionario_general |
| `LEXR-01889` | ucue | el plano, la llanura, el llano | diccionario_general |
| `LEXR-01890` | vijya-, viya- | indicar, señalar (con el dedo) | diccionario_general |
| `LEXR-01891` | waláa- | crecer | diccionario_general |
| `LEXR-01892` | wẽjẽ-, wẽe- | querer, desear | diccionario_general |
| `LEXR-01893` | yaatse- | ser despreciado | diccionario_general |
| `LEXR-01894` | yafy dyi’tj | cuenca del ojo | diccionario_general |
| `LEXR-01895` | ãpy-, ãpi | salir sobre | diccionario_general |
| `LEXR-01896` | ñusha ej | cañaduzal | diccionario_general |
| `LEXR-01897` | ĩits-, ĩitsúu- | madurarse | diccionario_general |
| `LEXR-01898` | ũ’na qui’su | la semano pasada | diccionario_general |
| `LEXR-01899` | ũuscha yajcy- | incomodarse | diccionario_general |
| `LEXR-01900` | -tjas | como si fuera | diccionario_general |
| `LEXR-01901` | aandas | andas (para llevar cadáveres) | diccionario_general |
| `LEXR-01902` | aj uweni- | ahumado | diccionario_general |
| `LEXR-01903` | almun | el almud | diccionario_general |
| `LEXR-01904` | anayún | la altasara | diccionario_general |
| `LEXR-01905` | atall | la gallina | diccionario_general |
| `LEXR-01906` | caapjande’j-, caapjande’je-(cpjandej-) | hacer abrir | diccionario_general |
| `LEXR-01907` | caatandyi’j-, caatyandyi’ji-(ctaandyi’j-) | hacer girar | diccionario_general |
| `LEXR-01908` | cajca | el tío (hermano de la mamá) | diccionario_general |
| `LEXR-01909` | catja´ | pendiente, inclinación del tejado | diccionario_general |
| `LEXR-01910` | cjalma spajcy- | quitar enjalma, (fig) desengañar | diccionario_general |
| `LEXR-01911` | cjash | la mazamorra | diccionario_general |
| `LEXR-01912` | cjuuts yu’ | la lejía | diccionario_general |
| `LEXR-01913` | dyiiga, dyiisu, dyiite | adentro | diccionario_general |
| `LEXR-01914` | fi’pju’chsa | escribano, escribiente | diccionario_general |
| `LEXR-01915` | indy (ingy) | tú, usted (masculino) | diccionario_general |
| `LEXR-01916` | ju’ngu yuu- | favorecer | diccionario_general |
| `LEXR-01917` | jyu’jyu’j | largo | diccionario_general |
| `LEXR-01918` | lmushnu | limosna | diccionario_general |
| `LEXR-01919` | maantey | tiempos anteriores | diccionario_general |
| `LEXR-01920` | meechica | el cucarachero (ave) | diccionario_general |
| `LEXR-01921` | mejca, mejcawe | ¡Camine! | diccionario_general |
| `LEXR-01922` | namu | el dueño, la dueña | diccionario_general |
| `LEXR-01923` | ndyi’sh | el hermano (respecto a la mujer) | diccionario_general |
| `LEXR-01924` | nmejwe’sh | último, menor (ej. hijo, menor de todos) | diccionario_general |
| `LEXR-01925` | nuasil (nuasel) | alguacil | diccionario_general |
| `LEXR-01926` | nus pa’ja en | el invierno, tiempo de invierno | diccionario_general |
| `LEXR-01927` | nwe’sh we’we- | tratarse como parientes | diccionario_general |
| `LEXR-01928` | paandej-, paandeje- | hospedar | diccionario_general |
| `LEXR-01929` | paau’jsa | persona que acompaña voluntariamente (al ir) | diccionario_general |
| `LEXR-01930` | peevisha- | persuadir | diccionario_general |
| `LEXR-01931` | pel | el carrizo | diccionario_general |
| `LEXR-01932` | pleecu’c | soledad (ave) | diccionario_general |
| `LEXR-01933` | pnjĩ’yacue | tía con sobrino o sobrina | diccionario_general |
| `LEXR-01934` | pta’sh-, pta’shi- | avisar, anunciar, informar, señalar | diccionario_general |
| `LEXR-01935` | ptjuc-, ptjucu- | apretar | diccionario_general |
| `LEXR-01936` | pumba’j-, pumba’ja- | cavar cámara lateral para enterrar | diccionario_general |
| `LEXR-01937` | pẽ’tsjutsj-, pẽ’tsjutsju- | rociar | diccionario_general |
| `LEXR-01938` | qui’tj watse | raíz del diente | diccionario_general |
| `LEXR-01939` | se’se- | ponerse ronco | diccionario_general |
| `LEXR-01940` | smala | el zamarro | diccionario_general |
| `LEXR-01941` | spandende- | templar (varias cuerdas) | diccionario_general |
| `LEXR-01942` | sẽ’j | barbasco (planta venenosa) | diccionario_general |
| `LEXR-01943` | tsinz zec | columna vertebral | diccionario_general |
| `LEXR-01944` | tsẽytsẽy chijme | azul claro | diccionario_general |
| `LEXR-01945` | ucj | el gusano | diccionario_general |
| `LEXR-01946` | ujca-, uca- | 1. golpear; 2. derribar, tumbar; 3. trillar | diccionario_general |
| `LEXR-01947` | uwe cu’jya’ (T) | baile de la boda | diccionario_general |
| `LEXR-01948` | vijcy- viqui- | 1. cazar animales; 2. ladrar | diccionario_general |
| `LEXR-01949` | vitu’tu- | corcovear | diccionario_general |
| `LEXR-01950` | wa’tsju’j-, wa’tsju’ju- | aplastar (repetidas veces), hacer arepa | diccionario_general |
| `LEXR-01951` | wendy uwe- | pescar | diccionario_general |
| `LEXR-01952` | wẽepang-, wẽepangúu- | estar hambriento | diccionario_general |
| `LEXR-01953` | yapundeni | desenvuelto | diccionario_general |
| `LEXR-01954` | yash | borrachero (árbol venenosa y narcótico) | diccionario_general |
| `LEXR-01955` | yat dyi’pte | en frente de la casa | diccionario_general |
| `LEXR-01956` | yat menz | alero | diccionario_general |
| `LEXR-01957` | yat pqui’sa | persona que da hospedaje, persona que pide hospedaje | diccionario_general |
| `LEXR-01958` | yu’pcjacje (yu’peecjacje) | confluencia de dos ríos o quebradas | diccionario_general |
| `LEXR-01959` | yu’puits | el zanjón de agua | diccionario_general |
| `LEXR-01960` | yunda ucue | la sabana | diccionario_general |
| `LEXR-01961` | ãa- | abiertamente, patente | diccionario_general |
| `LEXR-01962` | ñandy (yãndy) | el nevado (ej. Nevado de Huila) | diccionario_general |
| `LEXR-01963` | ñus cnay- | experimentar tristeza | diccionario_general |
| `LEXR-01964` | ũyu (ũjyu’ng) | al otro lado de la cordillera (ej. Tierradentro) | diccionario_general |
| `LEXR-01965` | ẽsh | la coca (planta) | diccionario_general |
| `LEXR-01966` | ẽsẽ’ | liviano | diccionario_general |
| `LEXR-01967` | aj | el lugar | diccionario_general |
| `LEXR-01968` | apjáa | la tapa | diccionario_general |
| `LEXR-01969` | bagach | cuando | diccionario_general |
| `LEXR-01970` | bela | vela | diccionario_general |
| `LEXR-01971` | caacpũushi’j-, caacpũushi’ji- | hacer regar | diccionario_general |
| `LEXR-01972` | caajni | mandato, orden | diccionario_general |
| `LEXR-01973` | caapeewecha’j-, caapeewecha’ja- | propiciar | diccionario_general |
| `LEXR-01974` | canzh we´we- | decir malas palabras | diccionario_general |
| `LEXR-01975` | caycjẽuj-, caycjẽu´ju- | deja pasar (al través) | diccionario_general |
| `LEXR-01976` | chajú | piña | diccionario_general |
| `LEXR-01977` | chjãchjamée | débil | diccionario_general |
| `LEXR-01978` | cjĩtsha | la caña brava del páramo (planta) | diccionario_general |
| `LEXR-01979` | cmaajĩ’j-,cmaajĩ’ji | hacer trabajar, obligar a trabajar | diccionario_general |
| `LEXR-01980` | cpi’sh | el trueno, rayo, relámpago | diccionario_general |
| `LEXR-01981` | cpun | el jabón | diccionario_general |
| `LEXR-01982` | cuchi vyllill | la pezuña del puerco | diccionario_general |
| `LEXR-01983` | cumby | 1. la comadreja (mamífero) 2. ser sobrenatural (mohán o moján) | diccionario_general |
| `LEXR-01984` | cus-, cusu- | anochecer | diccionario_general |
| `LEXR-01985` | cutyj bej | maíz amarillo | diccionario_general |
| `LEXR-01986` | cutyj fycach | capa de maíz | diccionario_general |
| `LEXR-01987` | e’shi-, e’shi’ji- | tener hipo | diccionario_general |
| `LEXR-01988` | ech pijts | el viudo | diccionario_general |
| `LEXR-01989` | findy | la coyuntura, canuto de la caña | diccionario_general |
| `LEXR-01990` | ja’ndawe’sh | de la misma edad | diccionario_general |
| `LEXR-01991` | ji’pj-, ji’pju- | tener, poseer, contener | diccionario_general |
| `LEXR-01992` | jysa’j-, jysa’ja- | bajar, desmontar | diccionario_general |
| `LEXR-01993` | lemlem | amarillo claro | diccionario_general |
| `LEXR-01994` | maasu | manso | diccionario_general |
| `LEXR-01995` | menzucue | la avispa (insecto) | diccionario_general |
| `LEXR-01996` | molta ya’ja | jigra tejida con agujas grandes | diccionario_general |
| `LEXR-01997` | nduj | el yerno | diccionario_general |
| `LEXR-01998` | ntundy-, ntundyi- | beber (lo ajeno) | diccionario_general |
| `LEXR-01999` | nuycjẽj-, nuycjẽje- | rebajar (precio) | diccionario_general |
| `LEXR-02000` | nuywe’we- | calumniar, criticar | diccionario_general |
| `LEXR-02001` | nyãja- | chuzar (aprovechando ausencia del dueño) | diccionario_general |
| `LEXR-02002` | paapechcanu- | ser olvidadizo | diccionario_general |
| `LEXR-02003` | pcyuuni | maltrato | diccionario_general |
| `LEXR-02004` | peepaj zec | filos por ambos lados | diccionario_general |
| `LEXR-02005` | pety cuet | el pedernal (para prender candela) | diccionario_general |
| `LEXR-02006` | primu | primo, prima | diccionario_general |
| `LEXR-02007` | ptsu’m | cuñado con cuñado | diccionario_general |
| `LEXR-02008` | ptsuu- | acabarse, darse por terminado | diccionario_general |
| `LEXR-02009` | pujnde-, punde- | ofrendar, propiciar a los espíritus | diccionario_general |
| `LEXR-02010` | qui’tj | el diente | diccionario_general |
| `LEXR-02011` | scandundu- | envolver (repetidas veces) | diccionario_general |
| `LEXR-02012` | sha’cy | la lama, el musgo | diccionario_general |
| `LEXR-02013` | shpiipí | el bimbo, pisco, pavo común (ave) | diccionario_general |
| `LEXR-02014` | speeju | el espejo | diccionario_general |
| `LEXR-02015` | tata wala | el abuelo | diccionario_general |
| `LEXR-02016` | tsalli’ll | el gavilán (ave) | diccionario_general |
| `LEXR-02017` | tsam ucje | malla de alambre | diccionario_general |
| `LEXR-02018` | tsjĩtsj yat | choza, con techo de paja | diccionario_general |
| `LEXR-02019` | tund-, tundu- | amarrar, atara | diccionario_general |
| `LEXR-02020` | upysa | que ha nacido | diccionario_general |
| `LEXR-02021` | utsje-, utsjée- | tocar, echar mano | diccionario_general |
| `LEXR-02022` | uwu- | derramarse, desbordarse | diccionario_general |
| `LEXR-02023` | viquiiqui- | ladrar (repetidas veces) | diccionario_general |
| `LEXR-02024` | wagás yuwe | el castellano, español (idioma) | diccionario_general |
| `LEXR-02025` | wã’jy wee | enfermedad de granos | diccionario_general |
| `LEXR-02026` | ya’pcji’cj- | ser lavado | diccionario_general |
| `LEXR-02027` | yafy cja’ty | párpado | diccionario_general |
| `LEXR-02028` | yat tjũ’we | cada saliente del vértice de techo | diccionario_general |
| `LEXR-02029` | yu’cj wala | la selva | diccionario_general |
| `LEXR-02030` | yu’wala | el río | diccionario_general |
| `LEXR-02031` | ũ’cj cuet | la piedra de moler | diccionario_general |
| `LEXR-02032` | aca pa’j- | doler | diccionario_general |
| `LEXR-02033` | amb | la era, el surco, la hilera | diccionario_general |
| `LEXR-02034` | buts wee, buts wee wajwa | varicela, viruela loca | diccionario_general |
| `LEXR-02035` | caapiya’j-, caapiya’ja- | enseñar | diccionario_general |
| `LEXR-02036` | caawãshi’j-, caawãshi’ji- | asustar a otra persona | diccionario_general |
| `LEXR-02037` | cambana | la campana | diccionario_general |
| `LEXR-02038` | cchill (chill) | el cuchillo | diccionario_general |
| `LEXR-02039` | chinda much | patimocho | diccionario_general |
| `LEXR-02040` | cla | vaca | diccionario_general |
| `LEXR-02041` | cpaajya’ndy-, cpaajya’ndyi- | alcanzar a tocar, lograr tocar | diccionario_general |
| `LEXR-02042` | fytũu ẽsh | (especie de madera, que usan para labrar cucharas) | diccionario_general |
| `LEXR-02043` | fyuts-, fyutsu- | clavar, acuñar (teja, maíz), abrochar, abotonar | diccionario_general |
| `LEXR-02044` | ipy pchĩ’ | la chispa | diccionario_general |
| `LEXR-02045` | jiisa | inteligente | diccionario_general |
| `LEXR-02046` | jimba tlaapichi | trapiche movido por bestia | diccionario_general |
| `LEXR-02047` | lash-, lashi- | aflojarse | diccionario_general |
| `LEXR-02048` | manga | la manga, el potrero | diccionario_general |
| `LEXR-02049` | mish | gato | diccionario_general |
| `LEXR-02050` | pa’jni | llegada (pasada) | diccionario_general |
| `LEXR-02051` | paatje-, paatjée- | aparar | diccionario_general |
| `LEXR-02052` | pchatj-, pchatje- | 1. poner atravesado (palo) 2. cruzar las piernas | diccionario_general |
| `LEXR-02053` | peesni | regalado | diccionario_general |
| `LEXR-02054` | penzh, penzhcuẽ | vieja, anciana | diccionario_general |
| `LEXR-02055` | pil | la pierna, la canilla | diccionario_general |
| `LEXR-02056` | piun | el peón, jornalero | diccionario_general |
| `LEXR-02057` | pshindy-, pshindyíi- | llorar (por ir con la mamá) | diccionario_general |
| `LEXR-02058` | pteenzúu- (peetenzu-) | apretarse | diccionario_general |
| `LEXR-02059` | ptsun | abuelo o abuela con nieto o nieta | diccionario_general |
| `LEXR-02060` | pucacuet | mejilla, cachete | diccionario_general |
| `LEXR-02061` | pund-, pundúu- | hilar | diccionario_general |
| `LEXR-02062` | sacue | palo de telar (sostiene el ñuwe) | diccionario_general |
| `LEXR-02063` | sajcu-, sacue- | sacudir | diccionario_general |
| `LEXR-02064` | shull | aguado | diccionario_general |
| `LEXR-02065` | shũ’tene- | desgarrar (varias tiras) | diccionario_general |
| `LEXR-02066` | spajcy-, spaaqui-, spaacy- | 1. bajar algo (de arriba para abajo); 2. desensillar | diccionario_general |
| `LEXR-02067` | squijw-, squiwu- | verter | diccionario_general |
| `LEXR-02068` | taacue yaj | (especie de bejuco) | diccionario_general |
| `LEXR-02069` | tayti | el plátano (de tierrra templada) | diccionario_general |
| `LEXR-02070` | tjacue | arriba | diccionario_general |
| `LEXR-02071` | tjune | la lengua | diccionario_general |
| `LEXR-02072` | tsam tutsa | herrero | diccionario_general |
| `LEXR-02073` | tspund-, tspundúu- | torcer | diccionario_general |
| `LEXR-02074` | tundu-, tundúu- | apresurarse, tener tiempo | diccionario_general |
| `LEXR-02075` | ujw-, ujwu- | escarbar, arar | diccionario_general |
| `LEXR-02076` | upy-, upyji- | 1. nacer; 2. reventar (pollito) | diccionario_general |
| `LEXR-02077` | vichacue | el pájaro | diccionario_general |
| `LEXR-02078` | watycue | perezozo | diccionario_general |
| `LEXR-02079` | wendy ñujnz | anzuelo | diccionario_general |
| `LEXR-02080` | wẽt ũs-, wẽt u’p- | sentirse bien, estar alentado | diccionario_general |
| `LEXR-02081` | yaatsesa | persona despreciado | diccionario_general |
| `LEXR-02082` | yafy | el ojo | diccionario_general |
| `LEXR-02083` | yafy wee | enfermedad de los ojos | diccionario_general |
| `LEXR-02084` | yuwe caaj- | mandar razón | diccionario_general |
| `LEXR-02085` | yũu- | hacer, actuar, realizar | diccionario_general |
| `LEXR-02086` | ãjmée yũu- | cometer falta, incumplir, ser indigno | diccionario_general |
| `LEXR-02087` | ñiñ | el grano, la pepita | diccionario_general |
| `LEXR-02088` | ñuspa’ | agradable, apetecible | diccionario_general |
| `LEXR-02089` | ũchi’ch- | defecar (repetidas veces) | diccionario_general |
| `LEXR-02090` | acj pa’j-, acj pa’ja- | resfriarse | diccionario_general |
| `LEXR-02091` | atate lem | amarillento | diccionario_general |
| `LEXR-02092` | ca’ga ej | papal | diccionario_general |
| `LEXR-02093` | caashingu’j-, caashingu’ju- | hacer sentir incapaz | diccionario_general |
| `LEXR-02094` | caaĩitse’j-, caaĩtse’je- | hacer cocer | diccionario_general |
| `LEXR-02095` | cha’cy | la cuchara | diccionario_general |
| `LEXR-02096` | chinda findy | coyuntura del pie | diccionario_general |
| `LEXR-02097` | cjimb-, cjimbu- | desatar | diccionario_general |
| `LEXR-02098` | cu’ta dyi’tj | el húmero, hueso del brazo | diccionario_general |
| `LEXR-02099` | cwẽetes | el cohete | diccionario_general |
| `LEXR-02100` | cãwũhw-, cãwũwu- | sacudir | diccionario_general |
| `LEXR-02101` | deeni, deeni atũ (deeñi, deeñi atũ) | la cama | diccionario_general |
| `LEXR-02102` | e’cy | la leña | diccionario_general |
| `LEXR-02103` | ew | bien, bueno | diccionario_general |
| `LEXR-02104` | ewmée yũuna | haciendo mal | diccionario_general |
| `LEXR-02105` | ilu | hilo | diccionario_general |
| `LEXR-02106` | ime | excremento, estiércol (de animal) | diccionario_general |
| `LEXR-02107` | is atuj | anaco | diccionario_general |
| `LEXR-02108` | isa- | contar, medir, pesar | diccionario_general |
| `LEXR-02109` | jweete ntsun | biznieto, biznieta | diccionario_general |
| `LEXR-02110` | jyand | redondo | diccionario_general |
| `LEXR-02111` | jytund yaj | la cadera | diccionario_general |
| `LEXR-02112` | manzmanz | pocos | diccionario_general |
| `LEXR-02113` | micu | mico | diccionario_general |
| `LEXR-02114` | mjĩi- | trabajar | diccionario_general |
| `LEXR-02115` | nmej | último | diccionario_general |
| `LEXR-02116` | paayuusa | persona que acompaña voluntariamente (al venir) | diccionario_general |
| `LEXR-02117` | pacue-, pacuée- | buscar | diccionario_general |
| `LEXR-02118` | pcyuuwe’weni | ultraje | diccionario_general |
| `LEXR-02119` | pecu’j-, pecu’ju- | viajarm andar de una parte a otra | diccionario_general |
| `LEXR-02120` | peluulu- | rodar, revolcarse (varias veces) | diccionario_general |
| `LEXR-02121` | pepy | 1. grueso, robusto; 2. nota muy baja (música) | diccionario_general |
| `LEXR-02122` | picas | la viga | diccionario_general |
| `LEXR-02123` | pu’ch-, pu’chji- | compartir, colaborar | diccionario_general |
| `LEXR-02124` | pẽ’tje- | pender | diccionario_general |
| `LEXR-02125` | pẽyni | pedido | diccionario_general |
| `LEXR-02126` | shwendu’ndu- | menear (repetidas veces) | diccionario_general |
| `LEXR-02127` | slun (sluty T) | el zurrón (botija de piel para guarapo) | diccionario_general |
| `LEXR-02128` | taafiy | el ánima (del difunto) | diccionario_general |
| `LEXR-02129` | taape’j, taape’je- | ensanchar | diccionario_general |
| `LEXR-02130` | tajcy | animal doméstico | diccionario_general |
| `LEXR-02131` | tapla | tabla | diccionario_general |
| `LEXR-02132` | tenz-, tenzúu- (ptenz-) | apretar | diccionario_general |
| `LEXR-02133` | tsund-, tsundúu- | gotear | diccionario_general |
| `LEXR-02134` | turúc | el toromonte (ave) | diccionario_general |
| `LEXR-02135` | twaaca’ca- | cortar (en varios pedazos) | diccionario_general |
| `LEXR-02136` | umbu- | 1. derrumbarse; 2. mudar pluma | diccionario_general |
| `LEXR-02137` | usa | la hoz (herramienta) | diccionario_general |
| `LEXR-02138` | utya | cerca | diccionario_general |
| `LEXR-02139` | vitni | hecho | diccionario_general |
| `LEXR-02140` | vitywe’sh | ser sobrenatural | diccionario_general |
| `LEXR-02141` | wã’chja | la gargantilla, collar de cuentas | diccionario_general |
| `LEXR-02142` | yajcy-, yaaqui-, yaacy- | despertar | diccionario_general |
| `LEXR-02143` | zits cja’ty | cáscara de huevo | diccionario_general |
| `LEXR-02144` | ĩ’née | en vano, sin motivo, de nada | diccionario_general |
| `LEXR-02145` | ĩts tutj | nariz chata | diccionario_general |
| `LEXR-02146` | ũ’ | comida, alimento | diccionario_general |
| `LEXR-02147` | ũchi’ch wee | la diarrea | diccionario_general |
| `LEXR-02148` | a’te uu- | haber eclipse de luna | diccionario_general |
| `LEXR-02149` | aacha’j-, aacha’ja- | calentar | diccionario_general |
| `LEXR-02150` | atyj tel | telar para tejer ruana | diccionario_general |
| `LEXR-02151` | atũju’j- | hacer barbacoa | diccionario_general |
| `LEXR-02152` | cacue yu’ | la hemorragia | diccionario_general |
| `LEXR-02153` | cash | el canasto, cesto | diccionario_general |
| `LEXR-02154` | ca´ndu- | asociarse con | diccionario_general |
| `LEXR-02155` | chinda pẽtyj | el empeine | diccionario_general |
| `LEXR-02156` | cjãambu | bordón, bastón | diccionario_general |
| `LEXR-02157` | cuvy | la flauta | diccionario_general |
| `LEXR-02158` | cweejya’j-cweejya’ja- | aventar | diccionario_general |
| `LEXR-02159` | ew yũuna | haciendo bien | diccionario_general |
| `LEXR-02160` | fi’jni | escrito | diccionario_general |
| `LEXR-02161` | ju’ngtjẽ’jwe’sh | antepasados | diccionario_general |
| `LEXR-02162` | jypa’yajcynimée | descuido | diccionario_general |
| `LEXR-02163` | jytyunde- | compartir | diccionario_general |
| `LEXR-02164` | meen | favor de... | diccionario_general |
| `LEXR-02165` | mẽ’, mẽ’we | ¡Coma! | diccionario_general |
| `LEXR-02166` | nchi’c | el hijo | diccionario_general |
| `LEXR-02167` | neecaj-, neecaja- | encargar | diccionario_general |
| `LEXR-02168` | nuytuw-, nuytuwúu- | acortar (ej. estribos) | diccionario_general |
| `LEXR-02169` | payaa | la papaya (fruta del papayo) | diccionario_general |
| `LEXR-02170` | pisun | el pisón | diccionario_general |
| `LEXR-02171` | pãpa- | dar paliza | diccionario_general |
| `LEXR-02172` | que’shi’j-, que’shi’ji- | dar hipo | diccionario_general |
| `LEXR-02173` | quishcue | el perrito, cachorro | diccionario_general |
| `LEXR-02174` | quiwe yase | apelldio | diccionario_general |
| `LEXR-02175` | saapajcy-, saapaqui- | zafarse y caer | diccionario_general |
| `LEXR-02176` | scuutyj tund | manojo de trigo | diccionario_general |
| `LEXR-02177` | shi’ndy | la abeja (insecto) | diccionario_general |
| `LEXR-02178` | shuma | la ardilla (mamífero roedor) | diccionario_general |
| `LEXR-02179` | shĩ’j | el león, puma (mamífero) | diccionario_general |
| `LEXR-02180` | shũ’wete- | romperse, desgarrarse | diccionario_general |
| `LEXR-02181` | sneene | transparente, claro | diccionario_general |
| `LEXR-02182` | swendende- | perforar (varias cosas o en varias partes) | diccionario_general |
| `LEXR-02183` | tjuja’ja- | tambalearse | diccionario_general |
| `LEXR-02184` | tutyj dyiite | el vientre | diccionario_general |
| `LEXR-02185` | vichacue vyllill | garra, uña (de pájaro) | diccionario_general |
| `LEXR-02186` | wechana | contento | diccionario_general |
| `LEXR-02187` | ya’pa’ch- (ya’pã’ch-) | taparse | diccionario_general |
| `LEXR-02188` | yaacyni | pensamiento | diccionario_general |
| `LEXR-02189` | yafy menzu | vistazo oblícuo | diccionario_general |
| `LEXR-02190` | yajta- | sacudir | diccionario_general |
| `LEXR-02191` | yats- | 1. adelante; 2. primero | diccionario_general |
| `LEXR-02192` | ye’ch | el retoño | diccionario_general |
| `LEXR-02193` | yevi | la llave | diccionario_general |
| `LEXR-02194` | yuwe apj- | negar, no divulgar | diccionario_general |
| `LEXR-02195` | yuwewúu | reconciliar | diccionario_general |
| `LEXR-02196` | ãpã, ãpãcuẽ | tierno, recíen nacido | diccionario_general |
| `LEXR-02197` | ñuty | moco | diccionario_general |
| `LEXR-02198` | ẽe- | arriba | diccionario_general |
| `LEXR-02199` | apj | el zancudo | diccionario_general |
| `LEXR-02200` | caapuí’j-, caapuíji- | hacer pelear | diccionario_general |
| `LEXR-02201` | camañún | la uva silvestre | diccionario_general |
| `LEXR-02202` | catyja´ | activo | diccionario_general |
| `LEXR-02203` | chĩ’ | perico (ave) | diccionario_general |
| `LEXR-02204` | ctandyii | alrededor | diccionario_general |
| `LEXR-02205` | cuse peequi’j- | prestar ayuda | diccionario_general |
| `LEXR-02206` | cuy-, cuyúu- | mirar adentro | diccionario_general |
| `LEXR-02207` | enda- | flotar | diccionario_general |
| `LEXR-02208` | fi’nzesa | que vive, ser viviendo | diccionario_general |
| `LEXR-02209` | fiy yajcy- | pensar mal | diccionario_general |
| `LEXR-02210` | iiweesu-, iiweesúu- | moler finito, desmenuzar | diccionario_general |
| `LEXR-02211` | lacy | flojo, poco apretado (tornillo, cuerda) | diccionario_general |
| `LEXR-02212` | mee- | estar ausente | diccionario_general |
| `LEXR-02213` | mell | usado, viejo, remendado | diccionario_general |
| `LEXR-02214` | nuyaatée- | limpiar | diccionario_general |
| `LEXR-02215` | pajnztewe’sh | cuarto | diccionario_general |
| `LEXR-02216` | pcjaacje- | reunirse, juntarse | diccionario_general |
| `LEXR-02217` | pichga | anguilla (ave) | diccionario_general |
| `LEXR-02218` | piisháa cyuupjni | el corral de ovejas | diccionario_general |
| `LEXR-02219` | piscu | el pisco, pavo (ave) | diccionario_general |
| `LEXR-02220` | playni | pilado | diccionario_general |
| `LEXR-02221` | pqui’se (T) | morder (culebra) | diccionario_general |
| `LEXR-02222` | pucacje pdyi’sh | primo con prima | diccionario_general |
| `LEXR-02223` | puuty pyũuscue- | enfadarse, enojarse (mutuamente) | diccionario_general |
| `LEXR-02224` | puuty ya’selpii- | servirse (mutuamente) | diccionario_general |
| `LEXR-02225` | quind | el peine | diccionario_general |
| `LEXR-02226` | quite | la flor | diccionario_general |
| `LEXR-02227` | sda’nda- | sonar (ruido de cascabel) | diccionario_general |
| `LEXR-02228` | selpisá | el siervo, que sirve | diccionario_general |
| `LEXR-02229` | sha’lul | seca (infarto de una glándula) | diccionario_general |
| `LEXR-02230` | shunde- | 1. escarmenar lana, cardar; 2. cosechar maíz | diccionario_general |
| `LEXR-02231` | sus-, susu- | hacer ruido | diccionario_general |
| `LEXR-02232` | sũtj-, sũje- | esconder | diccionario_general |
| `LEXR-02233` | ta’tsu- | torcerse, encorvarse | diccionario_general |
| `LEXR-02234` | tapesa | ancho, anchura | diccionario_general |
| `LEXR-02235` | teech teech | uno por uno | diccionario_general |
| `LEXR-02236` | tjacue-, tjacuée | ponerse grave, empeorar | diccionario_general |
| `LEXR-02237` | tsiun | zarzamora (planta) | diccionario_general |
| `LEXR-02238` | tyjã’ | el col, repollo (planta comestible) | diccionario_general |
| `LEXR-02239` | uutjash | el sembrado | diccionario_general |
| `LEXR-02240` | visitaĩ- | visitar | diccionario_general |
| `LEXR-02241` | vyuu bej | el oro (metal) | diccionario_general |
| `LEXR-02242` | wecha | grato | diccionario_general |
| `LEXR-02243` | wechwecha caayaqui’j- | alegrar | diccionario_general |
| `LEXR-02244` | ya’bautisaĩ- | ser bautizado | diccionario_general |
| `LEXR-02245` | yaacha-, yaacháa- | sentir calor, acalorarse | diccionario_general |
| `LEXR-02246` | yeele-, yeelée- | sentir cosquillas | diccionario_general |
| `LEXR-02247` | yu’le’ch | el riachuelo | diccionario_general |
| `LEXR-02248` | yuta-, yutáa- | llenar, rellenar | diccionario_general |
| `LEXR-02249` | yuwe pu’ch- | abogar, intervenir en un asunto | diccionario_general |
| `LEXR-02250` | ãadyija’ | evidentemente, es evidente | diccionario_general |
| `LEXR-02251` | ĩicja’j-, ĩicja’ja- | hacer estanque | diccionario_general |
| `LEXR-02252` | ũchji’ndy | mezquino | diccionario_general |
| `LEXR-02253` | ẽjyã ets | hoja de arbusto | diccionario_general |
| `LEXR-02254` | amwe’sh | el rayo | diccionario_general |
| `LEXR-02255` | caayapu’j-, caayapu’ju- | hacer envolver | diccionario_general |
| `LEXR-02256` | cacuesec | la fiebre | diccionario_general |
| `LEXR-02257` | calze tsjũtsj | especie de planta | diccionario_general |
| `LEXR-02258` | cjas wãjyandy | el ovillo | diccionario_general |
| `LEXR-02259` | cjã’cjã | hormiga | diccionario_general |
| `LEXR-02260` | cpãvitsa | que hiere (a otro) | diccionario_general |
| `LEXR-02261` | cshiica’j-, cshiica’ja- | hacer reír | diccionario_general |
| `LEXR-02262` | cuj (cũj) | varios, bastante | diccionario_general |
| `LEXR-02263` | cutyj tupj | maíz sarazo | diccionario_general |
| `LEXR-02264` | cyul | en vano, inútilmente | diccionario_general |
| `LEXR-02265` | fiyajts-, fiyats- | adelantarse | diccionario_general |
| `LEXR-02266` | fyu’fyu’ju- | silbar (repetidas veces) | diccionario_general |
| `LEXR-02267` | iicjalu | ahijado | diccionario_general |
| `LEXR-02268` | iisa’j-, iisa’ja- | bajar, desmontar (de una bestia) | diccionario_general |
| `LEXR-02269` | jytujtjesa | famoso, personaje importante | diccionario_general |
| `LEXR-02270` | llinderu | lindero | diccionario_general |
| `LEXR-02271` | llinu | castellano (idioma) | diccionario_general |
| `LEXR-02272` | majcysa | joven adulto | diccionario_general |
| `LEXR-02273` | naasá | sin embargo | diccionario_general |
| `LEXR-02274` | npeefynicy-, npeeefyniqui- | trastear, mudarse | diccionario_general |
| `LEXR-02275` | petyi’j-, petyi’ji- | sacar muesca | diccionario_general |
| `LEXR-02276` | putja’tj-, putja’tja- | soplar (repetidas veces) | diccionario_general |
| `LEXR-02277` | shũ’wende- | romper, rasgar (una sola tira) | diccionario_general |
| `LEXR-02278` | tjũ’we ya’qui | arete | diccionario_general |
| `LEXR-02279` | tsu’vy | hinchazón | diccionario_general |
| `LEXR-02280` | tsund | la gotera | diccionario_general |
| `LEXR-02281` | tucj | el pus | diccionario_general |
| `LEXR-02282` | tundundu- | amarrar (varias veces) | diccionario_general |
| `LEXR-02283` | tutyj jya’ndy- | partear, atender el parto | diccionario_general |
| `LEXR-02284` | tyiclli | el tigrillo (mamífero) | diccionario_general |
| `LEXR-02285` | u’ytjẽ’j | la suegra | diccionario_general |
| `LEXR-02286` | upja’pja- | parpadear | diccionario_general |
| `LEXR-02287` | us tandy | corazón de buey | diccionario_general |
| `LEXR-02288` | uschi’ | tijereta | diccionario_general |
| `LEXR-02289` | wallinde (wellinda) | el aguardiente | diccionario_general |
| `LEXR-02290` | yu’puts | orilla del río | diccionario_general |
| `LEXR-02291` | yuwe pjeu’j- | arreglar un asunto | diccionario_general |
| `LEXR-02292` | ã’pjy-, ã’pji- | echarse (gallina), empollar | diccionario_general |
| `LEXR-02293` | a’jsa | jinete, que monta a caballo | diccionario_general |
| `LEXR-02294` | andy-, andyi- | secar | diccionario_general |
| `LEXR-02295` | anzu’nzu- | mostrar los dientes (de contento) | diccionario_general |
| `LEXR-02296` | atj-, atje- | atrancar | diccionario_general |
| `LEXR-02297` | becuena u’p- | estar medio colgado | diccionario_general |
| `LEXR-02298` | chajú | la piña (planta) | diccionario_general |
| `LEXR-02299` | chich tujnd | carna pulpa | diccionario_general |
| `LEXR-02300` | cuchi | el puerco, cerdo, marrano | diccionario_general |
| `LEXR-02301` | cujmée | pocos | diccionario_general |
| `LEXR-02302` | cutyj uja a’te | mes para sembrar maíz | diccionario_general |
| `LEXR-02303` | cwẽese’j | barbasco (planta venenosa) | diccionario_general |
| `LEXR-02304` | cytey yuu- | cumplir, llevar a cabo | diccionario_general |
| `LEXR-02305` | cytãtujnd | el polvo | diccionario_general |
| `LEXR-02306` | daachajca | curíbano (planta) | diccionario_general |
| `LEXR-02307` | dyictjé | la cabeza | diccionario_general |
| `LEXR-02308` | dyijy, dyijy yuusá | el brujo, hechicero | diccionario_general |
| `LEXR-02309` | e’nzíi | ambos | diccionario_general |
| `LEXR-02310` | fillunde- | descoyuntarse | diccionario_general |
| `LEXR-02311` | fiw | la semilla (de plantas), la semilla (raza de animales) | diccionario_general |
| `LEXR-02312` | iiweesu’s- | moler (repetidas veces) | diccionario_general |
| `LEXR-02313` | iiẽepyãj-, iiẽepyãja- | demorar | diccionario_general |
| `LEXR-02314` | jyamb-, jyambu- | vaciar (granos) | diccionario_general |
| `LEXR-02315` | jypeesa’j | a través de, a lo largo de | diccionario_general |
| `LEXR-02316` | jyputa-, jyputáa- | oler, coger rastro | diccionario_general |
| `LEXR-02317` | jyũ’nzh-, jyũ’nzhi- | hacer muecas | diccionario_general |
| `LEXR-02318` | lanzh | guantín (mamífero roedor) | diccionario_general |
| `LEXR-02319` | lechi | leche | diccionario_general |
| `LEXR-02320` | mdyii | adentro | diccionario_general |
| `LEXR-02321` | niisa | la hija | diccionario_general |
| `LEXR-02322` | nish dej- | entumirse | diccionario_general |
| `LEXR-02323` | pa’ga | caro | diccionario_general |
| `LEXR-02324` | pa’ga, pa’gate | por | diccionario_general |
| `LEXR-02325` | pe’lpe’la | pedazo por pedazo | diccionario_general |
| `LEXR-02326` | peena | repetidamente | diccionario_general |
| `LEXR-02327` | pescal | el fiscal (oficial) | diccionario_general |
| `LEXR-02328` | pica (T) | el pico (herramienta) | diccionario_general |
| `LEXR-02329` | piisani | dibujo | diccionario_general |
| `LEXR-02330` | pjiw-, pjiwúu- | encontrar (algo que otro ha perdido) | diccionario_general |
| `LEXR-02331` | pu’yacjsa | reemplazo (en el cargo) | diccionario_general |
| `LEXR-02332` | quele’j-, quele’je- | hacer cosquillas | diccionario_general |
| `LEXR-02333` | quiwe | la tierra, el terreno, suelo | diccionario_general |
| `LEXR-02334` | shcambish-, shcambishíi- | hacer ampollas | diccionario_general |
| `LEXR-02335` | shpite’te- | desgarjarse, desprenderse | diccionario_general |
| `LEXR-02336` | sultyjica | anillo, sortija | diccionario_general |
| `LEXR-02337` | tamby | la costilla, el costado | diccionario_general |
| `LEXR-02338` | tsẽytsẽy tujme | gris | diccionario_general |
| `LEXR-02339` | tucú | torcaz (ave) | diccionario_general |
| `LEXR-02340` | tut | embotado | diccionario_general |
| `LEXR-02341` | tyjityjnisa | algo que ha sido escogido | diccionario_general |
| `LEXR-02342` | tũts | chamón (ave dañina) | diccionario_general |
| `LEXR-02343` | u’y pyacj | la concuñada | diccionario_general |
| `LEXR-02344` | u’y wee | la menstruación | diccionario_general |
| `LEXR-02345` | umsá | tejedor, que teje | diccionario_general |
| `LEXR-02346` | yafy chic | legaña | diccionario_general |
| `LEXR-02347` | yeets-, yeetsu- | echar hojas | diccionario_general |
| `LEXR-02348` | yu’ caa- | regar (líquido) | diccionario_general |
| `LEXR-02349` | yuc chich tujnd | carne de la cadera | diccionario_general |
| `LEXR-02350` | yuwe | 1. la boca; 2. el idioma; 3. el saludo; 4. asunto, noticia, razón | diccionario_general |
| `LEXR-02351` | yuwe pta’shsa | el mensajero | diccionario_general |
| `LEXR-02352` | ĩshiimée | verdaderamente | diccionario_general |
| `LEXR-02353` | afy | guama | diccionario_general |
| `LEXR-02354` | atate tsẽy | azul celeste | diccionario_general |
| `LEXR-02355` | baj, baji- | calentarse | diccionario_general |
| `LEXR-02356` | bu’ch | 1. la espuma 2. planta medicinal | diccionario_general |
| `LEXR-02357` | buu | la chinche del árbol | diccionario_general |
| `LEXR-02358` | caachinda’j-, caachinda’ja- | echar los cimientos (al edificar una casa) | diccionario_general |
| `LEXR-02359` | caapa’cjshi’j-, caapa’cjshi’ji- | asustar a otra persona | diccionario_general |
| `LEXR-02360` | catsni | costura | diccionario_general |
| `LEXR-02361` | chijmchijme | blancuzco | diccionario_general |
| `LEXR-02362` | cjas waga’te | el huso (palo para hilar) | diccionario_general |
| `LEXR-02363` | cjyũ’ju’j-, cjyũ’ju’ju- | vestir (a otro) | diccionario_general |
| `LEXR-02364` | cmuutsu’j-, cmuutsu’ju- | hacer amontonar | diccionario_general |
| `LEXR-02365` | cpi’sh quĩj- | caer rayo | diccionario_general |
| `LEXR-02366` | cpu’nzesawe’sh | padrinos (de matrimonio) | diccionario_general |
| `LEXR-02367` | cpunga’j wẽeni | ansia, náusea | diccionario_general |
| `LEXR-02368` | cupjy | la candelilla, luciérnaga | diccionario_general |
| `LEXR-02369` | cweete’j-, cweete’je- | hacer caer, dejar caer | diccionario_general |
| `LEXR-02370` | cũ’p-, cũ’pu- | enlazar | diccionario_general |
| `LEXR-02371` | fiesta yat | la casa donde se celebra la fiesta | diccionario_general |
| `LEXR-02372` | fiy yuu- | cambiar de aspecto | diccionario_general |
| `LEXR-02373` | fychacha | el lechero (árbol) | diccionario_general |
| `LEXR-02374` | fytũu tash | la mata, el árbol | diccionario_general |
| `LEXR-02375` | i’cue’sh | ustedes | diccionario_general |
| `LEXR-02376` | iicjala | ahijada | diccionario_general |
| `LEXR-02377` | ji’pjuni | bienes, posesiones | diccionario_general |
| `LEXR-02378` | jimba luuch | potro, potranco | diccionario_general |
| `LEXR-02379` | jypeejini | necesidad | diccionario_general |
| `LEXR-02380` | lem | amarillo | diccionario_general |
| `LEXR-02381` | mẽs, mẽswe | ¡Déle! | diccionario_general |
| `LEXR-02382` | nuu | por favor | diccionario_general |
| `LEXR-02383` | nyu yuuwa’jsa | la novia, comprometida | diccionario_general |
| `LEXR-02384` | pa’ch-, pa’chi- (pã’ch-) | cobijarse, taparse | diccionario_general |
| `LEXR-02385` | pe’tse- | mascar, masticar | diccionario_general |
| `LEXR-02386` | pechujcue-, pechuucue- | dar látigo | diccionario_general |
| `LEXR-02387` | pi’cy yat cu’jni | baile en una minga | diccionario_general |
| `LEXR-02388` | psuw-, psuwúu- | malgastar | diccionario_general |
| `LEXR-02389` | pu’chni | la ayuda | diccionario_general |
| `LEXR-02390` | quima | la nigua (insecto) | diccionario_general |
| `LEXR-02391` | quitj-, quitje- | clavar, poner estaca | diccionario_general |
| `LEXR-02392` | sa’ | y | diccionario_general |
| `LEXR-02393` | sa’te | la cucaracha (insecto) | diccionario_general |
| `LEXR-02394` | saatill | zarco, azul-verde | diccionario_general |
| `LEXR-02395` | scuutyj dyi’tj ej | el rastrojo | diccionario_general |
| `LEXR-02396` | sha’tyj (T) | resbaloso | diccionario_general |
| `LEXR-02397` | shindy | llorón | diccionario_general |
| `LEXR-02398` | shũ’tete- | desgarrarse (en varias partes) | diccionario_general |
| `LEXR-02399` | sus | duro (sonido) | diccionario_general |
| `LEXR-02400` | taacy wendy | el renacuajo, cría de la rana | diccionario_general |
| `LEXR-02401` | tupinde- | raspar | diccionario_general |
| `LEXR-02402` | tyach (cyach) | hace tiempo | diccionario_general |
| `LEXR-02403` | u’ca- | entrar | diccionario_general |
| `LEXR-02404` | u’jsa, u’jwa’jsa | pasajero, viajero | diccionario_general |
| `LEXR-02405` | viits-, viitsu- | echar espigas (maíz), salir la espiga | diccionario_general |
| `LEXR-02406` | vit-sa | el que hace | diccionario_general |
| `LEXR-02407` | wendy uwesá | el pescador | diccionario_general |
| `LEXR-02408` | yujurra ũs- | estar parado, de pie | diccionario_general |
| `LEXR-02409` | yul (yuul) | la deuda | diccionario_general |
| `LEXR-02410` | yũ’wẽesa | sediento, que tiene sed | diccionario_general |
| `LEXR-02411` | ĩishi | abuelo | diccionario_general |
| `LEXR-02412` | ũ’nacje | anteayer, antier | diccionario_general |
| `LEXR-02413` | ũuse-, ũusée- | respirar, volver en sí | diccionario_general |
| `LEXR-02414` | atyj tel | el telar | diccionario_general |
| `LEXR-02415` | bats tash | mata de cabuya | diccionario_general |
| `LEXR-02416` | bejbej chijme | rosado | diccionario_general |
| `LEXR-02417` | caashuuna’j-, caashuuna’ja- | hacer callar | diccionario_general |
| `LEXR-02418` | caycase´j-, caycase´je- | hacer descansar, aliviar, calmar | diccionario_general |
| `LEXR-02419` | caytjame’j-, caytjame’je- | avergonzar, causar pena | diccionario_general |
| `LEXR-02420` | chama’j-, chamba’ja- | cavar zanja | diccionario_general |
| `LEXR-02421` | chandy, chandy wee | la sarna | diccionario_general |
| `LEXR-02422` | chjãchjasa | poderoso | diccionario_general |
| `LEXR-02423` | cjĩij chwa’ | sombrero de hoja de caña | diccionario_general |
| `LEXR-02424` | cuse caaj- | echar mano a | diccionario_general |
| `LEXR-02425` | cytã’ja’j-, cytã’ja’ja- | hacer basura o polvo | diccionario_general |
| `LEXR-02426` | cyãaniwe’sh, cyãaniteywe’sh | los antepasados | diccionario_general |
| `LEXR-02427` | dewe-, dewée- | pagar | diccionario_general |
| `LEXR-02428` | jyanduwee | la parálisis | diccionario_general |
| `LEXR-02429` | jytuundsa | el preso | diccionario_general |
| `LEXR-02430` | lamus | los ramos | diccionario_general |
| `LEXR-02431` | majcy | grande (gente) | diccionario_general |
| `LEXR-02432` | meca, mecawe | ¡Pégale! | diccionario_general |
| `LEXR-02433` | pa’j yat | la posada | diccionario_general |
| `LEXR-02434` | paanu- | desconocer | diccionario_general |
| `LEXR-02435` | pasiáa- | pasear | diccionario_general |
| `LEXR-02436` | pelu- | rodar, caer dando vueltas | diccionario_general |
| `LEXR-02437` | pete | usado, viejo | diccionario_general |
| `LEXR-02438` | pu’tata- | golpear, tocar (la puerta) | diccionario_general |
| `LEXR-02439` | puutejca- | aventajar | diccionario_general |
| `LEXR-02440` | pã’ | dizque | diccionario_general |
| `LEXR-02441` | quijya, quijyasá | sobra, sobrante | diccionario_general |
| `LEXR-02442` | secúu- | hacer verano, hacer sol | diccionario_general |
| `LEXR-02443` | shcate- | fracturar, quebrarse | diccionario_general |
| `LEXR-02444` | shna’na | baba | diccionario_general |
| `LEXR-02445` | shũuwa’c | (planta medicinal) | diccionario_general |
| `LEXR-02446` | suucal | la vejiga | diccionario_general |
| `LEXR-02447` | sñuñu (syũyu) | la maraca, el alfandoque | diccionario_general |
| `LEXR-02448` | tamb pitscue, tamb u’y | arbusto, usan la hoja para lastimaduras | diccionario_general |
| `LEXR-02449` | tandy | redondo | diccionario_general |
| `LEXR-02450` | tsucj (tsũcj T) | la cabeza | diccionario_general |
| `LEXR-02451` | tsut pullu | tamal de choclo | diccionario_general |
| `LEXR-02452` | tuca cha’cy | calabazo (para sevir chicha) | diccionario_general |
| `LEXR-02453` | tuñ | encorvado | diccionario_general |
| `LEXR-02454` | tyundende- | repartir, distribuir (varias cosas, o a varias personas) | diccionario_general |
| `LEXR-02455` | uu- | 1. estar enfermo; 2. morir, fallecer | diccionario_general |
| `LEXR-02456` | uujni | sembrado | diccionario_general |
| `LEXR-02457` | uunsá | difunto, a | diccionario_general |
| `LEXR-02458` | yeetse-, yeetsée- | sentir frío | diccionario_general |
| `LEXR-02459` | zunzu- | adelgazarse | diccionario_general |
| `LEXR-02460` | ñusu en | la desgracia | diccionario_general |
| `LEXR-02461` | afy-afi- | aclarar, ponerse claro | diccionario_general |
| `LEXR-02462` | apas | la haba | diccionario_general |
| `LEXR-02463` | boda bu’ju | baile de la boda | diccionario_general |
| `LEXR-02464` | ca’jem-, ca’jemu- | trenzar | diccionario_general |
| `LEXR-02465` | ca’ne’j-, ca’en’je- | hacer lloar | diccionario_general |
| `LEXR-02466` | caafĩcje’j-, caafĩcje’je- | hacer poner (sombrero) | diccionario_general |
| `LEXR-02467` | caapeesu’j-, caapeesu’ju- | hacer regalar | diccionario_general |
| `LEXR-02468` | chich | la carne | diccionario_general |
| `LEXR-02469` | chu’ch | el pecho, la teta | diccionario_general |
| `LEXR-02470` | chucha cu’jni | baile de la chucha (un año después de edificar una casa) | diccionario_general |
| `LEXR-02471` | csuuwu’j-, csuuwu’ju- | hacer dañar | diccionario_general |
| `LEXR-02472` | cu’s-, cu’su- | 1. moler, exprimir 2. ordeñar vaca | diccionario_general |
| `LEXR-02473` | cupe | la lechuza, el búho (ave) | diccionario_general |
| `LEXR-02474` | cuse pil | el antebrazo | diccionario_general |
| `LEXR-02475` | cuse pẽtyj | la muñeca (parte del brazo) | diccionario_general |
| `LEXR-02476` | cyã’wẽ, cyã’wẽy (tyã’wẽ, tyã’wẽy) | así, asimismo | diccionario_general |
| `LEXR-02477` | cũ’p cja’tya | la soga, el lazo | diccionario_general |
| `LEXR-02478` | dyi’tjemby | caspi (árbol) | diccionario_general |
| `LEXR-02479` | fime | la cana | diccionario_general |
| `LEXR-02480` | fiymée | igual | diccionario_general |
| `LEXR-02481` | fytũu wes | el comején (insecto) | diccionario_general |
| `LEXR-02482` | iimi’wa’j atyj | la ropa de boda (de la novia) | diccionario_general |
| `LEXR-02483` | ij fi’nze- | convivir, cohabitar | diccionario_general |
| `LEXR-02484` | infiernu | el infierno | diccionario_general |
| `LEXR-02485` | jimba dyi’j | camino de herradura | diccionario_general |
| `LEXR-02486` | jypajnde-, jypaajnde | zafar, quitar | diccionario_general |
| `LEXR-02487` | jytjaacue | más | diccionario_general |
| `LEXR-02488` | jyutj vissa | yerbatero | diccionario_general |
| `LEXR-02489` | le’chcuẽ | un rato | diccionario_general |
| `LEXR-02490` | me’m-, me’mu- | retorcer | diccionario_general |
| `LEXR-02491` | muutsu’j-, muutsu’ju- | amontonar | diccionario_general |
| `LEXR-02492` | pe’te- | amanecer (el día) | diccionario_general |
| `LEXR-02493` | putj-, putjáa- | soplar | diccionario_general |
| `LEXR-02494` | putsputs | a un lado de | diccionario_general |
| `LEXR-02495` | quish-, quishi- | consolarse | diccionario_general |
| `LEXR-02496` | shaacuesa | bromeador, chistoso | diccionario_general |
| `LEXR-02497` | shba’mb | la carne espumosa | diccionario_general |
| `LEXR-02498` | shwawa- | murmurar (ruido del río) | diccionario_general |
| `LEXR-02499` | sápatu | el sábado | diccionario_general |
| `LEXR-02500` | tjee | la vasija, calabacita (partida en mitad) | diccionario_general |
| `LEXR-02501` | tjuja- | estar desnivelado | diccionario_general |
| `LEXR-02502` | tjẽ’j yu’tsesa | el curandero | diccionario_general |
| `LEXR-02503` | tsut-, tsutu- | darse, producirse (plantas) | diccionario_general |
| `LEXR-02504` | tu’ca- | tocar (la puerta) | diccionario_general |
| `LEXR-02505` | vits wala | montaña | diccionario_general |
| `LEXR-02506` | wa’tsju- | aplastar | diccionario_general |
| `LEXR-02507` | wendy cja’ty | escama (de pescado) | diccionario_general |
| `LEXR-02508` | ya’spẽ’tj-, ya’spẽtje- | cortarse (a sí mismo) | diccionario_general |
| `LEXR-02509` | yuja’j-, yuja’ja- | tasajear (carne) | diccionario_general |
| `LEXR-02510` | ũca | nunca | diccionario_general |
| `LEXR-02511` | ẽs zits | liendre | diccionario_general |
| `LEXR-02512` | a’te tjẽj | luna nueva | diccionario_general |
| `LEXR-02513` | apj-, apjáa- | cerrar, tapar, cubrir | diccionario_general |
| `LEXR-02514` | ate-, atée- | aclarar, despejarse | diccionario_general |
| `LEXR-02515` | buts wee wala | viruela | diccionario_general |
| `LEXR-02516` | ca’ga mush | papa menudita | diccionario_general |
| `LEXR-02517` | caajiyu’j-, caajiyu’ju-(cjiyu’j-) | explicar, hacer entender | diccionario_general |
| `LEXR-02518` | caapiya’jsa | maestro, que enseña | diccionario_general |
| `LEXR-02519` | caaptamu’j-, caaptamu’ju- | hacer casarse | diccionario_general |
| `LEXR-02520` | case-, casée- | aliviarse (de un dolor) | diccionario_general |
| `LEXR-02521` | chimby ej | la roza (de selva virgen) | diccionario_general |
| `LEXR-02522` | cji’pju’j-, cji’pju’ju | hacer tener, hacer concebir | diccionario_general |
| `LEXR-02523` | cjicj-, cjicje- | poner, colocar | diccionario_general |
| `LEXR-02524` | cpajcy-, cpaaqui-, cpaacy- | alcanzar (en el camino) | diccionario_general |
| `LEXR-02525` | cpãvitni | herido | diccionario_general |
| `LEXR-02526` | cuma-, cumáa- | sentir frío | diccionario_general |
| `LEXR-02527` | cupjy-, cupji- | descascarar | diccionario_general |
| `LEXR-02528` | cutyj mull | maíz amarillo | diccionario_general |
| `LEXR-02529` | cyuuju’j-, cyuuju’ju- | hacer parar, hacer detenerse | diccionario_general |
| `LEXR-02530` | ech iiyamunisa | endemoniado | diccionario_general |
| `LEXR-02531` | fytũu yu’ | savia | diccionario_general |
| `LEXR-02532` | iipa’j-, iipe’je- | hacerse responsable por otro | diccionario_general |
| `LEXR-02533` | iipshũ’j-, iipshũ’ju- | hacer sombra | diccionario_general |
| `LEXR-02534` | jyã’j-, jyãja- | lograr | diccionario_general |
| `LEXR-02535` | lashnu | el durazno (fruta) | diccionario_general |
| `LEXR-02536` | me’p, me’pwe | ¡Que esté! | diccionario_general |
| `LEXR-02537` | mish | 1. el gato (mamífero); 2. el espíritu guardián (vitywe’sh) | diccionario_general |
| `LEXR-02538` | mjĩi | el trabajo, empleo | diccionario_general |
| `LEXR-02539` | nenga | la sal | diccionario_general |
| `LEXR-02540` | niipeetje-, niipeetjeje- | 1. contagiar, contaminar 2. perjudicar | diccionario_general |
| `LEXR-02541` | nuywejy-, nuyweji- | endurecer | diccionario_general |
| `LEXR-02542` | nwẽese’jsa | obediente | diccionario_general |
| `LEXR-02543` | pa’j-, pa’ja- | llegar a ser | diccionario_general |
| `LEXR-02544` | paaya’ducj-, paaya’ducje- | entregarse voluntariamente | diccionario_general |
| `LEXR-02545` | pchĩ’ | la mecha, pavesa | diccionario_general |
| `LEXR-02546` | pu’chwa’jsa | el ayudante, que ayudará | diccionario_general |
| `LEXR-02547` | puuty ũuscha- | enojarse (mutuamente) | diccionario_general |
| `LEXR-02548` | shuuna’ vit- | hacer callar | diccionario_general |
| `LEXR-02549` | shũ’sh | crespo | diccionario_general |
| `LEXR-02550` | syu’tje- | resbalar | diccionario_general |
| `LEXR-02551` | taachin yuu- | disfrazarse (pintar la cara) | diccionario_general |
| `LEXR-02552` | tu’fy-, tu’fi- | eructar | diccionario_general |
| `LEXR-02553` | tupil | el ciempiés (miriápodo) | diccionario_general |
| `LEXR-02554` | ujtse | el aguacate (fruto) | diccionario_general |
| `LEXR-02555` | uusá pendaní cafy | el sepulcro, cementario | diccionario_general |
| `LEXR-02556` | wejyva | mejor, antes bien | diccionario_general |
| `LEXR-02557` | weyní | comprado, compra | diccionario_general |
| `LEXR-02558` | yaseni | bautizo | diccionario_general |
| `LEXR-02559` | yu’ãsh-, yu’ãshi- | meter debajo de | diccionario_general |
| `LEXR-02560` | yuc | 1. la nalga, asentaderas; 2. fondo | diccionario_general |
| `LEXR-02561` | ĩcj-ĩcje- | llegar de un viaje | diccionario_general |
| `LEXR-02562` | ũ’shic | el gusano | diccionario_general |
| `LEXR-02563` | -vacy (-va’cy) | pues | diccionario_general |
| `LEXR-02564` | ate | limpio | diccionario_general |
| `LEXR-02565` | atyj tel cuse | palo horitzontal del telar | diccionario_general |
| `LEXR-02566` | caacnayu’j-, caacnayu’ju- | hacer ganar | diccionario_general |
| `LEXR-02567` | caaviitse’j-, caaviitse’je- | hacer unir | diccionario_general |
| `LEXR-02568` | case´jete | la salida, en la salida | diccionario_general |
| `LEXR-02569` | chunga | el trompo (juguete) | diccionario_general |
| `LEXR-02570` | cpiitan | el capitán | diccionario_general |
| `LEXR-02571` | cu’nd-, cu’ndu- | 1. untar 2. curtir (cuero) 3. desfibrar cabuya | diccionario_general |
| `LEXR-02572` | dyus vichacue | la golondrina (ave) | diccionario_general |
| `LEXR-02573` | fycaach–, fycaachi- | deshojar (maíz) | diccionario_general |
| `LEXR-02574` | iiwe- | dejarse coger | diccionario_general |
| `LEXR-02575` | jimba cjũch | danta | diccionario_general |
| `LEXR-02576` | jyu’j dyi’j | lejos | diccionario_general |
| `LEXR-02577` | manz | cuanto, ¿cuánto? | diccionario_general |
| `LEXR-02578` | pachi’ch- | rasguñar (repetidas veces) | diccionario_general |
| `LEXR-02579` | pchiime’j-, pcjiime’je- | blanquear | diccionario_general |
| `LEXR-02580` | pees-, peesu- | regalar | diccionario_general |
| `LEXR-02581` | pi’cyna u’j- | acompañar | diccionario_general |
| `LEXR-02582` | puuple yuu- | empobrecerse | diccionario_general |
| `LEXR-02583` | quiite-, quiitée- | levantarse, madrguar | diccionario_general |
| `LEXR-02584` | sap | el sapo (batracio) | diccionario_general |
| `LEXR-02585` | shacue | el abono | diccionario_general |
| `LEXR-02586` | shavy-, shavíi- (chjavy-) | regresar, volver | diccionario_general |
| `LEXR-02587` | shic | el cardo (planta) | diccionario_general |
| `LEXR-02588` | sũpy | desnudo, pelado | diccionario_general |
| `LEXR-02589` | ta’nda | el cucarrón, escarabajo (insecto) | diccionario_general |
| `LEXR-02590` | tjutj tjujt | muy tupido | diccionario_general |
| `LEXR-02591` | ujnza | el ratón (mamífero roedor) | diccionario_general |
| `LEXR-02592` | uschic | gusano venenoso | diccionario_general |
| `LEXR-02593` | vichacue cjas | pluma (de pájaro) | diccionario_general |
| `LEXR-02594` | wãyãy (wẽyĩy) | zorrillo, comadreja (mamífero) | diccionario_general |
| `LEXR-02595` | wẽjẽ | el hambre, escasez | diccionario_general |
| `LEXR-02596` | ya’jiyu- | entenderse | diccionario_general |
| `LEXR-02597` | yu’chavy-, yu’chavi- | tropezar | diccionario_general |
| `LEXR-02598` | yuc dyi’tj | cadera | diccionario_general |
| `LEXR-02599` | ashnu | el asno (mamífero) | diccionario_general |
| `LEXR-02600` | atseni | despreciado, odiado | diccionario_general |
| `LEXR-02601` | aysu | por acá | diccionario_general |
| `LEXR-02602` | bish-, bishi- | ampollarse | diccionario_general |
| `LEXR-02603` | caapẽjyucue’j-, caapẽjyucue’je- | hacer arrodillar | diccionario_general |
| `LEXR-02604` | caashwendu’j-, caashwendu’ju- | devolver | diccionario_general |
| `LEXR-02605` | cfind | vara larga | diccionario_general |
| `LEXR-02606` | chacha | viche, no maduro | diccionario_general |
| `LEXR-02607` | cjũchcjũch bej | castaño | diccionario_general |
| `LEXR-02608` | cjẽw-, cjẽúu- | pasar a través (en plano) | diccionario_general |
| `LEXR-02609` | cmaasu’j-, cmaasu’ju- | amansar | diccionario_general |
| `LEXR-02610` | cweetjnisa | iluminación | diccionario_general |
| `LEXR-02611` | cwẽ’ndyi- | arrugarse | diccionario_general |
| `LEXR-02612` | e’nze’nz | de dos en dos | diccionario_general |
| `LEXR-02613` | e’su | después (posterioridad de tiempo) | diccionario_general |
| `LEXR-02614` | ecajuwe’sh | el extranjero | diccionario_general |
| `LEXR-02615` | ejejme | corriente del río tendido | diccionario_general |
| `LEXR-02616` | fycach | el amero (envoltura de maíz) | diccionario_general |
| `LEXR-02617` | jycuusu- | hacerse tarde, tardar | diccionario_general |
| `LEXR-02618` | jyumbasa | persona que está, equivocada o desviada | diccionario_general |
| `LEXR-02619` | maa | cual, cualquier, alguno | diccionario_general |
| `LEXR-02620` | manzcuẽ | cuanto | diccionario_general |
| `LEXR-02621` | mastela (T) | la estera | diccionario_general |
| `LEXR-02622` | mem | el canto, la canción | diccionario_general |
| `LEXR-02623` | ney npaasa | el padrastro | diccionario_general |
| `LEXR-02624` | njĩ’yacue, njĩ’yũcue | la tía (hermana de la mamá) | diccionario_general |
| `LEXR-02625` | pcãash-, pcjacje- | recoger, cosechar | diccionario_general |
| `LEXR-02626` | pendaní | sepultado | diccionario_general |
| `LEXR-02627` | pesatj | al través, horizontal | diccionario_general |
| `LEXR-02628` | pucacjẽ | cerca a | diccionario_general |
| `LEXR-02629` | pumbuumbu- | regar (repetidas veces) | diccionario_general |
| `LEXR-02630` | qui’sen | el domingo | diccionario_general |
| `LEXR-02631` | sap le’chue | la rana (batracio) | diccionario_general |
| `LEXR-02632` | shajshaj- | sonar, hacer ruido (maraca) | diccionario_general |
| `LEXR-02633` | shicasa | persona que rie | diccionario_general |
| `LEXR-02634` | shijca-, shica- | reir | diccionario_general |
| `LEXR-02635` | shũ’sh-, shũshu- | arrugar | diccionario_general |
| `LEXR-02636` | tyjicj shbimby | nuca | diccionario_general |
| `LEXR-02637` | waga’te dyi’tj | el malacate | diccionario_general |
| `LEXR-02638` | wats-, watsu- | ensartar | diccionario_general |
| `LEXR-02639` | weech we’we- | burlar | diccionario_general |
| `LEXR-02640` | weeswee | de mal genio, bravo | diccionario_general |
| `LEXR-02641` | yupsá | que ataja | diccionario_general |
| `LEXR-02642` | ñu’py wala | guagua, paca (mamífero roedor) | diccionario_general |
| `LEXR-02643` | ñu’wẽ- (yũ’wẽ-) | tener sed | diccionario_general |
| `LEXR-02644` | ñun (yũn) | la fruta | diccionario_general |
| `LEXR-02645` | ĩ’cj-, ĩ’cje- | ver visiones | diccionario_general |
| `LEXR-02646` | ĩitse’jni | cocido | diccionario_general |
| `LEXR-02647` | ĩts yachni | hemorragia nasal | diccionario_general |
| `LEXR-02648` | ũtj | la batata (planta, de tubérculos comestibles) | diccionario_general |
| `LEXR-02649` | a’tsjanisa | cernidor, cernedor, cedazo, susunga | diccionario_general |
| `LEXR-02650` | aca | el dolor | diccionario_general |
| `LEXR-02651` | bejbej tujme | castaño | diccionario_general |
| `LEXR-02652` | caaqui’ta’j-, caaqui’ta’ja- | mandar encender | diccionario_general |
| `LEXR-02653` | cpeembe’j-, cpeembe’je- | hacer gritar | diccionario_general |
| `LEXR-02654` | csha’w | el sueño | diccionario_general |
| `LEXR-02655` | csẽ’sẽ- | hacer señas (con la mirada), guiñar | diccionario_general |
| `LEXR-02656` | cyaj | por eso, con el fin de que | diccionario_general |
| `LEXR-02657` | cãtsa | el cusumbe, coatí (mamífero) | diccionario_general |
| `LEXR-02658` | deujmée | liviano, no pesado | diccionario_general |
| `LEXR-02659` | ducj-, ducje- | entregar, pagar deuda | diccionario_general |
| `LEXR-02660` | finzh cjũch | el pavo de monte (ave) | diccionario_general |
| `LEXR-02661` | fytũupatj | la cerbatana, bodoquera | diccionario_general |
| `LEXR-02662` | ipy tyjic | el tizón | diccionario_general |
| `LEXR-02663` | nanz, nanzcuẽ | unos cuantos | diccionario_general |
| `LEXR-02664` | nasa icjsa | el homicida, asesino | diccionario_general |
| `LEXR-02665` | ncuusa’j-, ncuusa’ja- | quitar, despojar a otro | diccionario_general |
| `LEXR-02666` | nus pĩi- | escampar | diccionario_general |
| `LEXR-02667` | pa’gamée | barato | diccionario_general |
| `LEXR-02668` | pasni | contestación | diccionario_general |
| `LEXR-02669` | pate-, patée- | zafarse | diccionario_general |
| `LEXR-02670` | payu pjeelu | bayo cariblanco | diccionario_general |
| `LEXR-02671` | peetjenisa | lo que da sabor, condimento | diccionario_general |
| `LEXR-02672` | pish’-, pishi- (C) | sentarse | diccionario_general |
| `LEXR-02673` | pu’chsa | el ayudante, que ayuda | diccionario_general |
| `LEXR-02674` | sec | el sol | diccionario_general |
| `LEXR-02675` | shaacue’j-, shaacue’je- | abonar | diccionario_general |
| `LEXR-02676` | shuj | ¡Toma! | diccionario_general |
| `LEXR-02677` | tecjtewe’sh | tercero | diccionario_general |
| `LEXR-02678` | tjã’mbush | la coronilla (de la cabeza) | diccionario_general |
| `LEXR-02679` | tjã’tj-, tjã’tja- | roncar | diccionario_general |
| `LEXR-02680` | tutyj (tuts T) | el estómago, la barriga | diccionario_general |
| `LEXR-02681` | uca’ca- | golpear (varias veces) | diccionario_general |
| `LEXR-02682` | ul watycue | (culebra no venenosa) | diccionario_general |
| `LEXR-02683` | uta-, utáa- | llenarse | diccionario_general |
| `LEXR-02684` | wa’lsa | renuente, desinclinado | diccionario_general |
| `LEXR-02685` | wecha en | regocijo, felicidad | diccionario_general |
| `LEXR-02686` | wenze | la verruga | diccionario_general |
| `LEXR-02687` | yaach-, yaachji- | sangrar | diccionario_general |
| `LEXR-02688` | ũpacjuuts | la pólvora | diccionario_general |
| `LEXR-02689` | acasa | la dolencia | diccionario_general |
| `LEXR-02690` | alcu | perro | diccionario_general |
| `LEXR-02691` | ambu’mbu- | echar (varias veces o varias cosas | diccionario_general |
| `LEXR-02692` | aqui’p-, aqui’pu | poner encima de | diccionario_general |
| `LEXR-02693` | caanviitu’j-, caanviitu’ju- | hacer dejar | diccionario_general |
| `LEXR-02694` | cashish- | sacar (animales) | diccionario_general |
| `LEXR-02695` | clliicjunsu | por las calles | diccionario_general |
| `LEXR-02696` | cweeyu’j-, cweeyu’ju- | mandar comprar | diccionario_general |
| `LEXR-02697` | ejy u’j- | haber derrumbe | diccionario_general |
| `LEXR-02698` | ewte neeyũu- | ser salvo | diccionario_general |
| `LEXR-02699` | fiityu’yu- | sentir una sensacíon extraña | diccionario_general |
| `LEXR-02700` | finzh | pavo del monte | diccionario_general |
| `LEXR-02701` | ipy chjã’chja | carbón, brasa | diccionario_general |
| `LEXR-02702` | jimba | el caballo | diccionario_general |
| `LEXR-02703` | msuuva | dondequiera | diccionario_general |
| `LEXR-02704` | niisa ntjẽjsa | hija mayor | diccionario_general |
| `LEXR-02705` | njĩ’j | la madre | diccionario_general |
| `LEXR-02706` | nuyfi’nze- | permitir pasar el día | diccionario_general |
| `LEXR-02707` | peetsu’j-, peetsu’ju- | 1. adelgazar; 2. rematar, acabar un trabajo | diccionario_general |
| `LEXR-02708` | pejnd-, pendu- | nadar | diccionario_general |
| `LEXR-02709` | pesu | el peso (moneda) | diccionario_general |
| `LEXR-02710` | peswée | el ladrón | diccionario_general |
| `LEXR-02711` | pets-, petsjúu- (pẽts-) | rajar, partir (con hacha) | diccionario_general |
| `LEXR-02712` | pinzú | el aliso (árbol) | diccionario_general |
| `LEXR-02713` | pu’ch-, pu’chji- | ayudar, apoyar | diccionario_general |
| `LEXR-02714` | pucasu | a orillas de | diccionario_general |
| `LEXR-02715` | pãatyjĩ’cj-, pãatyjĩ’cje- | acusar, presentar queja contra otra persona | diccionario_general |
| `LEXR-02716` | pĩitsj-, pĩitsjúu- | sonarse las narices | diccionario_general |
| `LEXR-02717` | sec en | el verano | diccionario_general |
| `LEXR-02718` | tsjende- | atar palos verticales | diccionario_general |
| `LEXR-02719` | tyu’tende- | repartir | diccionario_general |
| `LEXR-02720` | uj-, uja- | sembrar | diccionario_general |
| `LEXR-02721` | ul bite | coral (víbora) | diccionario_general |
| `LEXR-02722` | us bite | fríjol pintado | diccionario_general |
| `LEXR-02723` | usmity | alacrán | diccionario_general |
| `LEXR-02724` | uta | lleno | diccionario_general |
| `LEXR-02725` | uyi-, uyíi- | pegar (con la mano) | diccionario_general |
| `LEXR-02726` | vyuu mush | moneda fraccionaria | diccionario_general |
| `LEXR-02727` | wecha-, wecháa- | 1. estar agradecido, agradecer; 2. saludar, despedir, besar | diccionario_general |
| `LEXR-02728` | wenze | la marteja, mono nocturno (mamífero) | diccionario_general |
| `LEXR-02729` | wálasa | grande, importante | diccionario_general |
| `LEXR-02730` | wãjy (wẽjy) | tabaco (planta) | diccionario_general |
| `LEXR-02731` | ya’cach- | 1. caer encima de; 2. ser vencido | diccionario_general |
| `LEXR-02732` | yaacysa | que piensa, confía | diccionario_general |
| `LEXR-02733` | yaatul | el fuete | diccionario_general |
| `LEXR-02734` | yajpe-, yape- | probar (un alimento), sorber | diccionario_general |
| `LEXR-02735` | yu’shãpy | la bifurcacíon (del río) | diccionario_general |
| `LEXR-02736` | ã’s | arracacha | diccionario_general |
| `LEXR-02737` | ãtsja- | deshojar | diccionario_general |
| `LEXR-02738` | ũs-, ũsu- | estar (parado) | diccionario_general |
| `LEXR-02739` | ca’nd-, ca’ndu- | mezclar | diccionario_general |
| `LEXR-02740` | caacjacje’j-, caacjacje’je- | hacer asar | diccionario_general |
| `LEXR-02741` | chinda tã’sh | el calcañar, el talón | diccionario_general |
| `LEXR-02742` | cjas | la lana | diccionario_general |
| `LEXR-02743` | cjumbe-, cjumbée- | arrancar, desarraigar | diccionario_general |
| `LEXR-02744` | cuscay (cuscus) | mañana | diccionario_general |
| `LEXR-02745` | cutyj dycjas | estigma de maíz, pelo de maíz | diccionario_general |
| `LEXR-02746` | cweecha’j-, cweecha’ja- | hacer saludar | diccionario_general |
| `LEXR-02747` | ejnd | el temblor (de tierra) | diccionario_general |
| `LEXR-02748` | iiyã’yãaja- | puñalarse | diccionario_general |
| `LEXR-02749` | ipy aj | el humo | diccionario_general |
| `LEXR-02750` | jyãsh-, jyãshi- | vaciar | diccionario_general |
| `LEXR-02751` | le’chcuesa | el niño, la niña | diccionario_general |
| `LEXR-02752` | maajy | cualquiera | diccionario_general |
| `LEXR-02753` | majcymajcy | grueso y alto | diccionario_general |
| `LEXR-02754` | mjĩte, mjĩya | ¿por qué?, ¿para qué? | diccionario_general |
| `LEXR-02755` | mutyi | el mote | diccionario_general |
| `LEXR-02756` | mẽs, mẽswe | ¡Que esté! | diccionario_general |
| `LEXR-02757` | paand-, paandúu- | poner atravesado | diccionario_general |
| `LEXR-02758` | petsjuutsju- | partir (en dos o más partes) | diccionario_general |
| `LEXR-02759` | pjeelu | careto, cariblanco | diccionario_general |
| `LEXR-02760` | pqui’j-, pqui’ja- | prestar, emprestar | diccionario_general |
| `LEXR-02761` | pullu | el tamal, el bollo (envuelto de maíz) | diccionario_general |
| `LEXR-02762` | puuty we’weni | conversación, plática, charla | diccionario_general |
| `LEXR-02763` | pã’pã | pulga | diccionario_general |
| `LEXR-02764` | qui’tj vits | diente delantero | diccionario_general |
| `LEXR-02765` | shita | el armadillo (mamífero) | diccionario_general |
| `LEXR-02766` | shpindende- | desgajar (varias veces o varias ramas) | diccionario_general |
| `LEXR-02767` | tjuw | el enrizo, puerco espín (mamífero) | diccionario_general |
| `LEXR-02768` | tsunde tash | ciruelo (árbol) | diccionario_general |
| `LEXR-02769` | tuupja’j-, tuupja’ja- | mojar, remojar | diccionario_general |
| `LEXR-02770` | uuwa’j | muerte (futura) | diccionario_general |
| `LEXR-02771` | we’weya’ ãjasamée | mudo | diccionario_general |
| `LEXR-02772` | ãtsã’sa | el enfermo, el paciente | diccionario_general |
| `LEXR-02773` | ñavytuć | la coral (culebra) | diccionario_general |
| `LEXR-02774` | ĩchjíi- | enflaquecerse, delilitarse | diccionario_general |
| `LEXR-02775` | ũusutjeni | conciencia | diccionario_general |
| `LEXR-02776` | acháa- | calentarse | diccionario_general |
| `LEXR-02777` | atjni | tranca | diccionario_general |
| `LEXR-02778` | ayjyu | de aquí | diccionario_general |
| `LEXR-02779` | caamba’j-, caamba’ja- | casar, legalizar matrimonio | diccionario_general |
| `LEXR-02780` | cjalma | la enjalma | diccionario_general |
| `LEXR-02781` | cjas bite | lana teñida | diccionario_general |
| `LEXR-02782` | clliicjun | la calle, el callejón | diccionario_general |
| `LEXR-02783` | cwẽeta tujcaya’ | a tocar tambor | diccionario_general |
| `LEXR-02784` | i’cue yacj | contigo, con usted | diccionario_general |
| `LEXR-02785` | ijcha | tú (niña o pariente femenina) | diccionario_general |
| `LEXR-02786` | juuna’ | severamente | diccionario_general |
| `LEXR-02787` | jĩnisa | llamado | diccionario_general |
| `LEXR-02788` | llima | la naranja (fruta) | diccionario_general |
| `LEXR-02789` | ma’wẽ | como, ¿cómo? | diccionario_general |
| `LEXR-02790` | neej | mayor, el que manda | diccionario_general |
| `LEXR-02791` | neenjĩ’j yuju- | ser madrina | diccionario_general |
| `LEXR-02792` | pang-, pangúu- | descoyuntar, dislocar | diccionario_general |
| `LEXR-02793` | pchi’c | padre o madre con el hijo | diccionario_general |
| `LEXR-02794` | peevya’jsa (T) | el maestro, que enseña | diccionario_general |
| `LEXR-02795` | pẽty watse | la vena yugular | diccionario_general |
| `LEXR-02796` | tsu’vy, tsu’vi- (tsũ’vy-) | hincharse | diccionario_general |
| `LEXR-02797` | tupy-, tupi- (tũpy-) | pelar | diccionario_general |
| `LEXR-02798` | tyjẽ’en | el viernes | diccionario_general |
| `LEXR-02799` | wa’cj | el musgo | diccionario_general |
| `LEXR-02800` | walta | la huerta | diccionario_general |
| `LEXR-02801` | yuwe cjicj- | poner queja | diccionario_general |
| `LEXR-02802` | ñu’py le’ch | agutí | diccionario_general |
| `LEXR-02803` | ñuwe | el palo del telar (lanzadera) | diccionario_general |
| `LEXR-02804` | atyj tel chinda | palo vertical del telar | diccionario_general |
| `LEXR-02805` | bajy we’we- | hacer seña | diccionario_general |
| `LEXR-02806` | chji’ndy mil | miel de abeja | diccionario_general |
| `LEXR-02807` | cja’ty | 1. el cuero, la piel 2. la cáscara, corteza de árbol | diccionario_general |
| `LEXR-02808` | cpaatjeng-, cpaatjengu- | lograr mirar | diccionario_general |
| `LEXR-02809` | cutyj mush | maíz pirá | diccionario_general |
| `LEXR-02810` | cyajũ’ | entonces | diccionario_general |
| `LEXR-02811` | cyãawe’sh (tyãawe’sh) | esos, esas | diccionario_general |
| `LEXR-02812` | dyijy, yuu- | practicar brujería | diccionario_general |
| `LEXR-02813` | dyus mama | madrino | diccionario_general |
| `LEXR-02814` | ech u’y | la viuda | diccionario_general |
| `LEXR-02815` | jwendu’ndu- | dar látigo (repetidas veces) | diccionario_general |
| `LEXR-02816` | lepy | grueso | diccionario_general |
| `LEXR-02817` | nasa yuwe | el idioma páez | diccionario_general |
| `LEXR-02818` | nus wala | aguacero | diccionario_general |
| `LEXR-02819` | nus wejya dyi’j | tormenta, tempestad | diccionario_general |
| `LEXR-02820` | pdyi’p | ambos lados, de lado a lado (opuesto) | diccionario_general |
| `LEXR-02821` | quiwe yuwe | asunto de terrenos | diccionario_general |
| `LEXR-02822` | shicshic | roñoso, áspero | diccionario_general |
| `LEXR-02823` | shinde-, shindée- | erizar | diccionario_general |
| `LEXR-02824` | shwa’ | la cidrayota (planta comestible) | diccionario_general |
| `LEXR-02825` | susmée we’we- | hablar en voz baja | diccionario_general |
| `LEXR-02826` | suty-, sutyíi- (sũty-) | rayar, escribir con lápiz | diccionario_general |
| `LEXR-02827` | sũcja’cja- | sobar, acarciciar (varias veces) | diccionario_general |
| `LEXR-02828` | tee jwend | de una vez, directamente | diccionario_general |
| `LEXR-02829` | ucje | la red, malla | diccionario_general |
| `LEXR-02830` | ufiifi- | chiflar (repetidas veces) | diccionario_general |
| `LEXR-02831` | wãwã | el abejorro, abejón (insecto) | diccionario_general |
| `LEXR-02832` | yuuwemeesa | inocente | diccionario_general |
| `LEXR-02833` | yuuwesa | culpable | diccionario_general |
| `LEXR-02834` | ã’pysa | la clueca | diccionario_general |
| `LEXR-02835` | ã’sh | la rascadera, mafafa (planta) | diccionario_general |
| `LEXR-02836` | ũpj-, ũpjúu- | encogerse | diccionario_general |
| `LEXR-02837` | acjicj-, acjicje- | poner encima de (cosa larga) | diccionario_general |
| `LEXR-02838` | amu | el señor, patrón | diccionario_general |
| `LEXR-02839` | ayte | aquí | diccionario_general |
| `LEXR-02840` | caaũuscha’j-, caaũuscha’ja- | hacer enojar, ofender | diccionario_general |
| `LEXR-02841` | cneetul (T) | el corredor (de la casa) | diccionario_general |
| `LEXR-02842` | culu-, culúu’ | acogollar, echar cogollo | diccionario_general |
| `LEXR-02843` | cyuusu’j-, cyuusu’ju- | hacer dar de tomar | diccionario_general |
| `LEXR-02844` | cũj-, cũju-, cũu- | subir | diccionario_general |
| `LEXR-02845` | fitsj | cuí, conejillo de indias | diccionario_general |
| `LEXR-02846` | iilajcy-, iilaaqui- | aflojar | diccionario_general |
| `LEXR-02847` | ipy | la candela, el fuego | diccionario_general |
| `LEXR-02848` | luucu | loco | diccionario_general |
| `LEXR-02849` | me’cyshũ | el pulmón | diccionario_general |
| `LEXR-02850` | mllinu | el molino | diccionario_general |
| `LEXR-02851` | mush | menudo | diccionario_general |
| `LEXR-02852` | nueve | nueve | diccionario_general |
| `LEXR-02853` | nyafíi, nyafiitey | al principio | diccionario_general |
| `LEXR-02854` | nyu ji’pjmeesa | soltero | diccionario_general |
| `LEXR-02855` | patj | el cañuto | diccionario_general |
| `LEXR-02856` | pcamb-, pcambu- | regar (líquido) | diccionario_general |
| `LEXR-02857` | pu’jycjẽw-, pu’jycjẽúu- | econtrarse con otro que viene de rumbo opuesto y seguir adelante | diccionario_general |
| `LEXR-02858` | quiwe cuchi | pecarí | diccionario_general |
| `LEXR-02859` | scuutyj (scuucyj T) | el trigo | diccionario_general |
| `LEXR-02860` | tacj-, tacje- | emperzar, comenzar | diccionario_general |
| `LEXR-02861` | tjũ’we chica | la cera (del oído), cerúmen | diccionario_general |
| `LEXR-02862` | tjẽymée | fácil | diccionario_general |
| `LEXR-02863` | tyuj | el gorrion | diccionario_general |
| `LEXR-02864` | tyweysá | que vende | diccionario_general |
| `LEXR-02865` | tũchj-, tũchjíi- | quejarse, gemir, pujar | diccionario_general |
| `LEXR-02866` | utya- | juntar, unir | diccionario_general |
| `LEXR-02867` | vyandu’ndu- | 1. blandir (repetidas veces); 2. recoger con cuchara) | diccionario_general |
| `LEXR-02868` | waawa’j-, waawa’ja- | remover, suavizar | diccionario_general |
| `LEXR-02869` | we’lli- | entiesar, ponerse tieso | diccionario_general |
| `LEXR-02870` | ya’pechcanu- | olvidarse | diccionario_general |
| `LEXR-02871` | ya’sca’j-, ya’sca’ja- | retirarse, retroceder | diccionario_general |
| `LEXR-02872` | yu’bu’ch | la espuma | diccionario_general |
| `LEXR-02873` | ña chachay | yuca viche | diccionario_general |
| `LEXR-02874` | ĩshiini | la mentira | diccionario_general |
| `LEXR-02875` | ũ’tsjsa | el carpintero | diccionario_general |
| `LEXR-02876` | ũssa | persona que está presente | diccionario_general |
| `LEXR-02877` | a’qui’cy-, a’qui’qui- | colgar (varias cosas) | diccionario_general |
| `LEXR-02878` | a’te luuch | luna nueva | diccionario_general |
| `LEXR-02879` | a’te shi’ndy- | haber eclipse de luna | diccionario_general |
| `LEXR-02880` | cach-, cachjí- | 1. sentarse 2. posar (ave) 3. aterrizar (avión) | diccionario_general |
| `LEXR-02881` | calzec | especie de árbol | diccionario_general |
| `LEXR-02882` | cjã’sh | el grillo (insecto) | diccionario_general |
| `LEXR-02883` | cu’le’j-, cu’le’je- | 1. enderezar, alinear 2. rectificar | diccionario_general |
| `LEXR-02884` | cviitu’j-, cviitu’ju- | 1. mandar hacer 2. hacer celebrar misa | diccionario_general |
| `LEXR-02885` | fi’cue | pinto, moteado | diccionario_general |
| `LEXR-02886` | jamby | arisco, esquivo | diccionario_general |
| `LEXR-02887` | jiyuni | conocimiento | diccionario_general |
| `LEXR-02888` | nuytjẽ’j-, nuytjẽ’je- | criar hijos | diccionario_general |
| `LEXR-02889` | nyafy | primero, antes, anteriormente | diccionario_general |
| `LEXR-02890` | seena’ | terrible, horrible | diccionario_general |
| `LEXR-02891` | shaacue we’we- | bromear, chancear | diccionario_general |
| `LEXR-02892` | slluj | el chiguaco (ave) | diccionario_general |
| `LEXR-02893` | spate- | encogerse | diccionario_general |
| `LEXR-02894` | taw tel | telar para tejer chumbe | diccionario_general |
| `LEXR-02895` | tsja’ya- | extender los brazos | diccionario_general |
| `LEXR-02896` | tundy-, tundyíi- (tungy-) | beber, tomar | diccionario_general |
| `LEXR-02897` | us | el riñón | diccionario_general |
| `LEXR-02898` | vichacue yat | nido | diccionario_general |
| `LEXR-02899` | wej | la hamaca | diccionario_general |
| `LEXR-02900` | wendy | el pescado, pez | diccionario_general |
| `LEXR-02901` | wãwã | abeja, abejón | diccionario_general |
| `LEXR-02902` | ya’gaña- | dejarse engañar | diccionario_general |
| `LEXR-02903` | ya’jwend- | dar látigo | diccionario_general |
| `LEXR-02904` | ya’neeyũu- | ser dejado, quedarse involuntariamente | diccionario_general |
| `LEXR-02905` | yaasesa | nombrado, con el nombre de | diccionario_general |
| `LEXR-02906` | yusu’s- | dar de beber (a varias personas, o varias veces) | diccionario_general |
| `LEXR-02907` | yuuní, yuuwa’j | venida | diccionario_general |
| `LEXR-02908` | ãchãch | más tarde | diccionario_general |
| `LEXR-02909` | ĩtyĩ fi’nzeni | la vida (pasada) | diccionario_general |
| `LEXR-02910` | caacreĩ’j-, caacreĩ’ji- | hacer creer | diccionario_general |
| `LEXR-02911` | caapu’chji’j-, caapu’chji’ji-(cpu’chji’j-) | hacer ayudar, permitir ayudar | diccionario_general |
| `LEXR-02912` | caypumba´j-, caypumba´ja- | 1. hacer equivocar, hacer desviar 2. engañar | diccionario_general |
| `LEXR-02913` | caytẽeyu´j-, caytẽeyu´ju- | hacer demorar, atrasar | diccionario_general |
| `LEXR-02914` | chucha | la chucha, zarigüeya (mamífero) | diccionario_general |
| `LEXR-02915` | chũpy | orejudo | diccionario_general |
| `LEXR-02916` | cpuuse’j-, cpuuse’je- | dejar fermentar | diccionario_general |
| `LEXR-02917` | cu’le | derecho, recto | diccionario_general |
| `LEXR-02918` | custal | el costal | diccionario_general |
| `LEXR-02919` | efy | el colmillo | diccionario_general |
| `LEXR-02920` | fiy vit- | confundir, perturbar | diccionario_general |
| `LEXR-02921` | jypey-, jypeyi- | apuntar (un arma) | diccionario_general |
| `LEXR-02922` | mama | la mamá | diccionario_general |
| `LEXR-02923` | mujm | la guadua (especie de bambú) | diccionario_general |
| `LEXR-02924` | nish | gordo | diccionario_general |
| `LEXR-02925` | pajy-, pajíi- | ahuyentar pájaros | diccionario_general |
| `LEXR-02926` | pand-, pandu- | barrer | diccionario_general |
| `LEXR-02927` | pdyi’sh | hermano con hermana | diccionario_general |
| `LEXR-02928` | pe’la | el pedazo | diccionario_general |
| `LEXR-02929` | peeawu- | echar agua (ej. en el bautismo) | diccionario_general |
| `LEXR-02930` | penzhweete | la vejez (refiriendo a una mujer) | diccionario_general |
| `LEXR-02931` | plliisatu (pllist T) | la cobija (tejido en telar) | diccionario_general |
| `LEXR-02932` | ptam | la pareja (de personas) | diccionario_general |
| `LEXR-02933` | puuty we’we- | 1. conversar, platicar, charlar 2. orar | diccionario_general |
| `LEXR-02934` | quĩtj | maní | diccionario_general |
| `LEXR-02935` | shamb wes | el cordón umbilical | diccionario_general |
| `LEXR-02936` | shuuna’ | callado | diccionario_general |
| `LEXR-02937` | shwa’ | cidrayota | diccionario_general |
| `LEXR-02938` | tama | el tamo | diccionario_general |
| `LEXR-02939` | tpand-, tpandúu- | arrollar, arremangar | diccionario_general |
| `LEXR-02940` | tpengu’ngu- | doblar, encorvar (repetidas veces) | diccionario_general |
| `LEXR-02941` | tujme | gris, pardo | diccionario_general |
| `LEXR-02942` | uy-, uyúu- | 1. ver, encontrar; 2. conseguir, hallar | diccionario_general |
| `LEXR-02943` | waccha | el huérfano, guacho | diccionario_general |
| `LEXR-02944` | way-, wayíi- | abrir la boca | diccionario_general |
| `LEXR-02945` | yu’pets | el vado | diccionario_general |
| `LEXR-02946` | ũjt-, ũtu- | mojarse | diccionario_general |
| `LEXR-02947` | caapuutyuyu’j-, caapuutyuyu’ju- | hacer econtrarse | diccionario_general |
| `LEXR-02948` | caayu’spẽtje’j-, caayu’spẽ’tje’je-(cyu’spẽ’tje’j-) | hacer tropezar | diccionario_general |
| `LEXR-02949` | catjwe´sh | marco del telar (palos verticales) | diccionario_general |
| `LEXR-02950` | cndu | la tinta morada (planta) | diccionario_general |
| `LEXR-02951` | cu’ta | 1. el hombro, brazo 2. la brazada (medida | diccionario_general |
| `LEXR-02952` | cuse nuuchcue | el meñique | diccionario_general |
| `LEXR-02953` | cyu’acje’j-, cyu’acje’je- | hacer guardar | diccionario_general |
| `LEXR-02954` | cã’wẽ’j-, cã’wẽjẽ- | permitir comer, dejar comer | diccionario_general |
| `LEXR-02955` | deweni | pagado | diccionario_general |
| `LEXR-02956` | dyii- | adentro | diccionario_general |
| `LEXR-02957` | fillute- | descoyuntar | diccionario_general |
| `LEXR-02958` | finze yuu- | enfriarse | diccionario_general |
| `LEXR-02959` | fytũu vica | el bordón | diccionario_general |
| `LEXR-02960` | jycatsunde- | quiarse ruana | diccionario_general |
| `LEXR-02961` | much | corto | diccionario_general |
| `LEXR-02962` | namicu | el amigo | diccionario_general |
| `LEXR-02963` | nish cja’ty (T) | la piel | diccionario_general |
| `LEXR-02964` | paanwe’we- | intervenir | diccionario_general |
| `LEXR-02965` | peecjacje- | unirse, juntarse con | diccionario_general |
| `LEXR-02966` | pejna-, pena- | abundar, rendir | diccionario_general |
| `LEXR-02967` | pshũu- | hacer sombra, ocultarse | diccionario_general |
| `LEXR-02968` | pu’yacj-, pu’yacje- | reemplazar, sustituir | diccionario_general |
| `LEXR-02969` | quiwe ẽsẽ-, quiwe u’j- | temblar (movimiento telúrico) | diccionario_general |
| `LEXR-02970` | shita | armadillo | diccionario_general |
| `LEXR-02971` | tasa | la taza | diccionario_general |
| `LEXR-02972` | tjẽy | difícil | diccionario_general |
| `LEXR-02973` | tyjicj watse | vena de la nuca | diccionario_general |
| `LEXR-02974` | well | el loro (ave) | diccionario_general |
| `LEXR-02975` | wẽt-sa | cosa agradable | diccionario_general |
| `LEXR-02976` | ãandyijimée | obligatoriamente | diccionario_general |
| `LEXR-02977` | ñunda alcu (T) | el zorro (mamífero) | diccionario_general |
| `LEXR-02978` | ẽjyã | el arbusto | diccionario_general |
| `LEXR-02979` | -va | también | diccionario_general |
| `LEXR-02980` | bush | el andamio | diccionario_general |
| `LEXR-02981` | capijnz | motilón (árbol, con fruta comestible) | diccionario_general |
| `LEXR-02982` | chulfity | dorotea (ave) | diccionario_general |
| `LEXR-02983` | cjise | la catarata | diccionario_general |
| `LEXR-02984` | cysew-, cyseúu | maldecir (deseando mal a otro), ultrajar | diccionario_general |
| `LEXR-02985` | fĩtyj-, fĩtyji- | despertar (a otro) | diccionario_general |
| `LEXR-02986` | icjsa | el homicida | diccionario_general |
| `LEXR-02987` | iw | el pene | diccionario_general |
| `LEXR-02988` | jimba dycjas | crin | diccionario_general |
| `LEXR-02989` | leng | cojo | diccionario_general |
| `LEXR-02990` | mjĩi en | días hábiles | diccionario_general |
| `LEXR-02991` | ne’ca- | entrar brevemente | diccionario_general |
| `LEXR-02992` | pechanuni | olvido, olvidado | diccionario_general |
| `LEXR-02993` | pẽ’tjesa | pendiente | diccionario_general |
| `LEXR-02994` | quiis-, quiisu- | 1. alzar, levantar, quitar; 2. edificar casa | diccionario_general |
| `LEXR-02995` | seelpimeesa | inútil, inservible | diccionario_general |
| `LEXR-02996` | shish-, shishíi- | rajarse, agrietarse | diccionario_general |
| `LEXR-02997` | tash | la mata | diccionario_general |
| `LEXR-02998` | tsunde | la circuela silvestre (fruta) | diccionario_general |
| `LEXR-02999` | tsute wala | la muela del juicio | diccionario_general |
| `LEXR-03000` | tsute yu’ | zumo de la hoja de encenillo (medicinal) | diccionario_general |
| `LEXR-03001` | ulñiñ | el curíbano (planta medicinal) | diccionario_general |
| `LEXR-03002` | uswa’l | chachafruto (árbol) | diccionario_general |
| `LEXR-03003` | wẽt ũsni, wẽt ũswa’j | bienestar, felicidad | diccionario_general |
| `LEXR-03004` | ã’ | la estrella | diccionario_general |
| `LEXR-03005` | ĩshíi-ĩshiija- | menitr | diccionario_general |
| `LEXR-03006` | achamée | inferior | diccionario_general |
| `LEXR-03007` | afy | guamo | diccionario_general |
| `LEXR-03008` | atall pits | el gallo | diccionario_general |
| `LEXR-03009` | ayu, ayuy | por acá | diccionario_general |
| `LEXR-03010` | buc | panzón | diccionario_general |
| `LEXR-03011` | buta | la roncha | diccionario_general |
| `LEXR-03012` | caacu’ju’j-, caacu’ju’ju- | hacer bailar | diccionario_general |
| `LEXR-03013` | caapechucue’j-, caapechucue’ju- | mandar dar látigo | diccionario_general |
| `LEXR-03014` | caywẽtu’j-, caywẽtu’ju- | hacer sanar | diccionario_general |
| `LEXR-03015` | chavyuu- | dar ataque | diccionario_general |
| `LEXR-03016` | cu’jsa | bailador | diccionario_general |
| `LEXR-03017` | ewmeete neeyũu- | ser condenado | diccionario_general |
| `LEXR-03018` | finfina- | ahorrar (varias cosas) | diccionario_general |
| `LEXR-03019` | fytũu chica | el comején (insecto) | diccionario_general |
| `LEXR-03020` | fytũu cja’ty | la corteza de árbol | diccionario_general |
| `LEXR-03021` | jyaatjsa | una persona vestida | diccionario_general |
| `LEXR-03022` | jẽp | (yerba que enloquece) | diccionario_general |
| `LEXR-03023` | lupe- | ponerse blando, ablandarse | diccionario_general |
| `LEXR-03024` | namicu yuu- | ser amigos, tener amistad | diccionario_general |
| `LEXR-03025` | niipeetjeesa | contagioso | diccionario_general |
| `LEXR-03026` | niishi- | engordarse | diccionario_general |
| `LEXR-03027` | pjay we’we- | bromear, chancear | diccionario_general |
| `LEXR-03028` | pneeney | padrino con ahijado o ahijada | diccionario_general |
| `LEXR-03029` | sñal (syal) | la cicatriz, marca | diccionario_general |
| `LEXR-03030` | tech-, techíi- | lamer | diccionario_general |
| `LEXR-03031` | tjũ’we puuple | sordo | diccionario_general |
| `LEXR-03032` | tyjicj dyi’yj | hueso de la nuca | diccionario_general |
| `LEXR-03033` | u’psa | habitante, morador | diccionario_general |
| `LEXR-03034` | ulu’j-, ulu’ju- | pedir fiado, dar fiado | diccionario_general |
| `LEXR-03035` | we’pe ẽs | frailejón (planta) | diccionario_general |
| `LEXR-03036` | wẽeshusá | que insulta | diccionario_general |
| `LEXR-03037` | yu’ acha | agua hirviendo | diccionario_general |
| `LEXR-03038` | ĩtyĩ yuu- | revivir, resucitar | diccionario_general |
| `LEXR-03039` | apj le’ch | el mosquito | diccionario_general |
| `LEXR-03040` | cayachiji´j-, caycachji´ji- | permitir entrar y sentarse | diccionario_general |
| `LEXR-03041` | cchiiwa’j-, cchiiwa’ja- | empachar | diccionario_general |
| `LEXR-03042` | chinda vyllill | el dedo del pie | diccionario_general |
| `LEXR-03043` | cleecytul (T) | inspector | diccionario_general |
| `LEXR-03044` | cluuvi’j-, cluuvi’ji- | amontonar | diccionario_general |
| `LEXR-03045` | cujya- | cocinar yerba | diccionario_general |
| `LEXR-03046` | cytu’cy-, cytu’qui- | ofrecer sal a un caballo | diccionario_general |
| `LEXR-03047` | dyi’tj sũpy | el esqueleto | diccionario_general |
| `LEXR-03048` | finze quiwe | tierra fría | diccionario_general |
| `LEXR-03049` | fytũ pagayú | carpintero | diccionario_general |
| `LEXR-03050` | fyu cu’ta (jyu cu’ta) | el ala | diccionario_general |
| `LEXR-03051` | jycuet | la cabeza | diccionario_general |
| `LEXR-03052` | jyu’jmeecue | breve | diccionario_general |
| `LEXR-03053` | macjue | cuanto (distancia), ¿cuánto? | diccionario_general |
| `LEXR-03054` | mẽewẽjy | gallinazo | diccionario_general |
| `LEXR-03055` | neejyũj- | traer | diccionario_general |
| `LEXR-03056` | pus-, pusúu- | fermentarse | diccionario_general |
| `LEXR-03057` | puts- | al borde de | diccionario_general |
| `LEXR-03058` | qui’s-, qui’su- | 1. guardar dieta; 2. guardar día de fiesta | diccionario_general |
| `LEXR-03059` | qui’tj cutyi’j- | extraer muela | diccionario_general |
| `LEXR-03060` | scuutyj ũ’we | harina de trigo | diccionario_general |
| `LEXR-03061` | styãj-, styãja-, styãa- | amañarse, acostumbrarse | diccionario_general |
| `LEXR-03062` | sũcj-, sũcjáa- | sobar, componer un hueso dislocado | diccionario_general |
| `LEXR-03063` | ta’ts yuu- | encorvarse | diccionario_general |
| `LEXR-03064` | taty | el arco, de forma arqueda | diccionario_general |
| `LEXR-03065` | tupite- | hacerse mataduras | diccionario_general |
| `LEXR-03066` | twajca-, twaaca- | cortar, trozar | diccionario_general |
| `LEXR-03067` | tũ’s-, tũsu-, (tu’s-) | cargar | diccionario_general |
| `LEXR-03068` | vyaa- | aparecer, estar presente | diccionario_general |
| `LEXR-03069` | yaacynisa | recordado | diccionario_general |
| `LEXR-03070` | yapeepe- | probar (varias veces) | diccionario_general |
| `LEXR-03071` | yuuta, yuutáa- | llenar | diccionario_general |
| `LEXR-03072` | yuwe ũchja- | darse por terminado (un pleito) | diccionario_general |
| `LEXR-03073` | atu’t- | llevar (varias personas o varias coas) | diccionario_general |
| `LEXR-03074` | añu | el año | diccionario_general |
| `LEXR-03075` | caaclala’j-, caaclala’ja- | dejar hervir | diccionario_general |
| `LEXR-03076` | cja’tya | el rejo | diccionario_general |
| `LEXR-03077` | ctã’ñi’j-, ctã’ñi’ji- | causar sentir ’señas’ | diccionario_general |
| `LEXR-03078` | cutyi’j-, cutyi’ji- | 1. sacar 2. traducir | diccionario_general |
| `LEXR-03079` | cutyj ũ’we | harina de maíz | diccionario_general |
| `LEXR-03080` | cñusu’j-, cñusu’ju-(cyũusu’j-) | entristecer, hacer sufrir | diccionario_general |
| `LEXR-03081` | ee watse | la vena | diccionario_general |
| `LEXR-03082` | etse | frío | diccionario_general |
| `LEXR-03083` | ewte nvijt- | Salvar | diccionario_general |
| `LEXR-03084` | fychacha upj | cerco de lechero | diccionario_general |
| `LEXR-03085` | iiwejch we’we- | jactarse, hablar con orgullo | diccionario_general |
| `LEXR-03086` | mutcue | lulo | diccionario_general |
| `LEXR-03087` | nuycchijãachja’j-, nuycchjãachja’ja- | hacer que otro lo fortalece | diccionario_general |
| `LEXR-03088` | nuyi’nsa | el líder (de un conjunto de músicos) | diccionario_general |
| `LEXR-03089` | nuyutya- | acercar, arrimar | diccionario_general |
| `LEXR-03090` | paandee yat | posada | diccionario_general |
| `LEXR-03091` | peecjicj- | alumbrar a otro | diccionario_general |
| `LEXR-03092` | petyi’jni | la escalera | diccionario_general |
| `LEXR-03093` | pinzh | picadura | diccionario_general |
| `LEXR-03094` | puuts-, puutsu- | alimentar, dar de comer | diccionario_general |
| `LEXR-03095` | quitssuwe’sh | espíritus de las quebradas | diccionario_general |
| `LEXR-03096` | shi’ndy mil | la miel de abeja | diccionario_general |
| `LEXR-03097` | tswendu’ndu- | retorcer, menear la cabeza (en señal de disgusto) | diccionario_general |
| `LEXR-03098` | tupil | ciempiés | diccionario_general |
| `LEXR-03099` | wej, wejcuẽ | poco | diccionario_general |
| `LEXR-03100` | wẽeshuní | ultraje | diccionario_general |
| `LEXR-03101` | caauyu’j-, caauyu’ju- | hacer ver | diccionario_general |
| `LEXR-03102` | chcajnde-, chcande- | quebrar, fracturar | diccionario_general |
| `LEXR-03103` | cjalma tyaj- | poner enjalma, (fig) engañar | diccionario_general |
| `LEXR-03104` | cjĩtse | murciélago | diccionario_general |
| `LEXR-03105` | clala- | hervir | diccionario_general |
| `LEXR-03106` | cmbeesáa- | confesar (al cura) | diccionario_general |
| `LEXR-03107` | cnay-, cnayúu- | ganar, vencer, ganar dinero, sufrir, experimentar, padecer | diccionario_general |
| `LEXR-03108` | ctjeengu’j-, ctjeengu’ju- | hacer ver, hacer mirar | diccionario_general |
| `LEXR-03109` | cu’ju | el baile | diccionario_general |
| `LEXR-03110` | cwuuwu’j-, cwuuwu’ju- | hacer correr | diccionario_general |
| `LEXR-03111` | cytandy-, cytandyíi- | rodear | diccionario_general |
| `LEXR-03112` | dyictjé sũpy | calvo | diccionario_general |
| `LEXR-03113` | jwendtunde- | desenredar | diccionario_general |
| `LEXR-03114` | jytjaacue-, jytjaacuée- | empeorar, aumentar más y más | diccionario_general |
| `LEXR-03115` | jytjuuc-, jytjuucu- | ahorcarse | diccionario_general |
| `LEXR-03116` | ncuẽmiyu | la nuera | diccionario_general |
| `LEXR-03117` | neepenzh | la abuela | diccionario_general |
| `LEXR-03118` | niisa npaasa | hijastra | diccionario_general |
| `LEXR-03119` | pundúu | lezna (herramienta) | diccionario_general |
| `LEXR-03120` | pyãj- | en medio de | diccionario_general |
| `LEXR-03121` | scuutyj spiiga | espiga de trigo | diccionario_general |
| `LEXR-03122` | shateete- | despedazarse (en varias partes) | diccionario_general |
| `LEXR-03123` | tjuw | erizo, puerco espín | diccionario_general |
| `LEXR-03124` | tsjende upj | cerca hecha de palos verticales | diccionario_general |
| `LEXR-03125` | tsjũtsj | la espina, zarza | diccionario_general |
| `LEXR-03126` | wecha’cha- | saludar (repetidas veces) | diccionario_general |
| `LEXR-03127` | ña (yã) | la yuca (planta, de raíz comestible) | diccionario_general |
| `LEXR-03128` | -dyij- | ciertamente | diccionario_general |
| `LEXR-03129` | caau’j-, caau’ju- | hacer andar | diccionario_general |
| `LEXR-03130` | carcel | la cárcel | diccionario_general |
| `LEXR-03131` | caywẽchpa’ja’j-, caywẽchpa’ja’ja- | darle un ataque | diccionario_general |
| `LEXR-03132` | chu’ch-, chu’chu | mamar | diccionario_general |
| `LEXR-03133` | cja’ctende- | descolgar (varias cosas), quitar | diccionario_general |
| `LEXR-03134` | cneeyú | el guineo (especie de plátano pequeño) | diccionario_general |
| `LEXR-03135` | cpaawenzh-, cpaawenzhi- | lograr halar | diccionario_general |
| `LEXR-03136` | cuse | la mano | diccionario_general |
| `LEXR-03137` | ewsa | bueno, fino | diccionario_general |
| `LEXR-03138` | iiwejch | orgulloso | diccionario_general |
| `LEXR-03139` | ju’ngu | a favor de | diccionario_general |
| `LEXR-03140` | jya’ndy-, jya’ndyi- | tocar (con la mano), palpar | diccionario_general |
| `LEXR-03141` | jycjẽe- | tragar | diccionario_general |
| `LEXR-03142` | menzucue | avispa | diccionario_general |
| `LEXR-03143` | niimal | el animal | diccionario_general |
| `LEXR-03144` | paandlé | panderé (árbol) | diccionario_general |
| `LEXR-03145` | pi’pi | el junco (arbusto) | diccionario_general |
| `LEXR-03146` | pshi’nd-, pshi’ndu- (T) | burlar, hacer burla | diccionario_general |
| `LEXR-03147` | putste | al borde de | diccionario_general |
| `LEXR-03148` | puuty ya’pcyuu- | agredirse (mutuamente) | diccionario_general |
| `LEXR-03149` | quĩitsju- | inclinar la cabeza | diccionario_general |
| `LEXR-03150` | quẽese’j-, quẽese’je- | menear, mover, agitar | diccionario_general |
| `LEXR-03151` | shal | el teñidero (árbol, que se usa para teñir de negro) | diccionario_general |
| `LEXR-03152` | shimb ej | la roza | diccionario_general |
| `LEXR-03153` | slenu (sleena) | el sereno | diccionario_general |
| `LEXR-03154` | squiiyu’yu- | mirar hacia abajo (repetidas veces) | diccionario_general |
| `LEXR-03155` | upajcy-, upaqui- | empujar | diccionario_general |
| `LEXR-03156` | wata | espeso (miel, goma, etc.) | diccionario_general |
| `LEXR-03157` | watycue yuu- | volverse perezozo | diccionario_general |
| `LEXR-03158` | yajcy- | atrapar, coger con trampa | diccionario_general |
| `LEXR-03159` | yuuse’j-, yuuse’je- | rascar, dar raquiña, comezón | diccionario_general |
| `LEXR-03160` | ĩts zec | nariz aguileña, narigudo | diccionario_general |
| `LEXR-03161` | ũshi- | regarse, desparramarse | diccionario_general |
| `LEXR-03162` | ũusdyi’-, ũusdyi’i- | suspirar | diccionario_general |
| `LEXR-03163` | bagach yujva | nunca, jamás | diccionario_general |
| `LEXR-03164` | bendesĩ | bendecir | diccionario_general |
| `LEXR-03165` | cdeewayi’j-, cdeewayi’ji- | hacer bostezar | diccionario_general |
| `LEXR-03166` | chind pjapj | la planta del pie | diccionario_general |
| `LEXR-03167` | chãty-, chãtyi-(chaty-) | empujar | diccionario_general |
| `LEXR-03168` | chũjwa (chũjwe) | agudo, puntiagudo | diccionario_general |
| `LEXR-03169` | cteenz-, cteenzúu- | apretar | diccionario_general |
| `LEXR-03170` | cuchi tel | la horqueta para puerco | diccionario_general |
| `LEXR-03171` | cue’nzu-(cue’nzhu-) | frincir las cejas | diccionario_general |
| `LEXR-03172` | cumby ya’ja | jigra con huecos grandes | diccionario_general |
| `LEXR-03173` | cya’patje’j-, cya’patje’je- | hacer cubrir | diccionario_general |
| `LEXR-03174` | cyãa (tyãa) | él, ella, aquél, aquélla | diccionario_general |
| `LEXR-03175` | dyus | Dios | diccionario_general |
| `LEXR-03176` | ejme | la corriente del rió | diccionario_general |
| `LEXR-03177` | jweenzh | el agüinche | diccionario_general |
| `LEXR-03178` | nenga’j- | salar, echar sal | diccionario_general |
| `LEXR-03179` | nuypa’j-, nuypa’ja- | traer, hacer llegar | diccionario_general |
| `LEXR-03180` | nuype’j-, nuype’je- | mantener, criar | diccionario_general |
| `LEXR-03181` | pajnz | cuatro | diccionario_general |
| `LEXR-03182` | pquĩiji- | producir | diccionario_general |
| `LEXR-03183` | scatyĩ’j-, scatuĩja- | atizar la candela | diccionario_general |
| `LEXR-03184` | sec uu- | haber eclipse de sol | diccionario_general |
| `LEXR-03185` | shquiicy yuu- | ponerse amarillo | diccionario_general |
| `LEXR-03186` | tamby | el bulto | diccionario_general |
| `LEXR-03187` | tsjĩtsj | la paja | diccionario_general |
| `LEXR-03188` | yat cluu | cumbrera de la casa, caballete | diccionario_general |
| `LEXR-03189` | yu’amb-, yu’ambu- | echar en | diccionario_general |
| `LEXR-03190` | ajtse-, atse- | despreciar, odiar | diccionario_general |
| `LEXR-03191` | caacutyi’j-, caacutyi’ji- | hacer extraer | diccionario_general |
| `LEXR-03192` | caapta’shi’j-, cappta’shi’ji- | mandar avisar | diccionario_general |
| `LEXR-03193` | chjamb wala | la ciudad | diccionario_general |
| `LEXR-03194` | cweeji’j-, cweeji’ji- | 1. endurecer 2. cuajar (leche) | diccionario_general |
| `LEXR-03195` | cwẽ’yã | el helecho | diccionario_general |
| `LEXR-03196` | e’s | atrás, detrás | diccionario_general |
| `LEXR-03197` | ja’nda | igual | diccionario_general |
| `LEXR-03198` | jimba | caballo | diccionario_general |
| `LEXR-03199` | jyandu’j-, jyandu’ju- | redondear | diccionario_general |
| `LEXR-03200` | jypẽew-, jypẽewu- | bañarse (con remedio) | diccionario_general |
| `LEXR-03201` | jysaacuecue- | sacudirse | diccionario_general |
| `LEXR-03202` | jytu’cj-, jytu’cje- | atragantarse | diccionario_general |
| `LEXR-03203` | ncaaca | el tío (hermano de la mamá) | diccionario_general |
| `LEXR-03204` | nvijt-, nviitu- | 1. dejar 2. designar 3. derrotar | diccionario_general |
| `LEXR-03205` | pa’cy-, pa’qui- | sacar líquido, servir comida | diccionario_general |
| `LEXR-03206` | pecu’j | alrededor | diccionario_general |
| `LEXR-03207` | peetjengu- | espiar | diccionario_general |
| `LEXR-03208` | shlalá | pinto (blanco y negro) | diccionario_general |
| `LEXR-03209` | tundte (dundte) | de presto, un momento | diccionario_general |
| `LEXR-03210` | tyity | el barro, lodo | diccionario_general |
| `LEXR-03211` | tywe’we- | persuadir, hablar con cariño | diccionario_general |
| `LEXR-03212` | wendy-, wendyi- | querer, amar, gustar | diccionario_general |
| `LEXR-03213` | wẽjẽ-, wẽe- | tener hambre | diccionario_general |
| `LEXR-03214` | ya’castigaĩ- | ser castigado | diccionario_general |
| `LEXR-03215` | yu’cypeeni | el consejo | diccionario_general |
| `LEXR-03216` | yunz cafy | ojo de aguja | diccionario_general |
| `LEXR-03217` | ĩiwẽet-ĩiwẽetúu- | sanarse | diccionario_general |
| `LEXR-03218` | ũuseni | respiración | diccionario_general |
| `LEXR-03219` | andy | yo, conmigo, mine | diccionario_general |
| `LEXR-03220` | apj-, apju- | escarbar | diccionario_general |
| `LEXR-03221` | caayulu’j-, caayulu’ju-(cyulu’j-) | hacer endeudar | diccionario_general |
| `LEXR-03222` | cjumbete- | desarraigarse | diccionario_general |
| `LEXR-03223` | cjya’ndyi’j-, cjya’ndyi’ji- | permitir tocar, partear | diccionario_general |
| `LEXR-03224` | cpaawẽsẽ’j-, cpaawẽsẽ’je | lograr escuchar | diccionario_general |
| `LEXR-03225` | cue’sh | nosotros, nosotras | diccionario_general |
| `LEXR-03226` | cviisu’j-, cviisu’ju- | 1. hacer desyerbar 2. hacer entretenerse | diccionario_general |
| `LEXR-03227` | cyaacje’j-, cyaacje’je- | hacer cargar (ej. niño, en el bautismo) | diccionario_general |
| `LEXR-03228` | ej | la roza, el sembrado | diccionario_general |
| `LEXR-03229` | fitse | espeso | diccionario_general |
| `LEXR-03230` | iindeewe- | defenderse | diccionario_general |
| `LEXR-03231` | iindeeweni | callo | diccionario_general |
| `LEXR-03232` | iiwejch yajcy- | enorgullecerse, sentirse orgulloso | diccionario_general |
| `LEXR-03233` | jycajts-, jycatsu- | ponerse ruana | diccionario_general |
| `LEXR-03234` | jytyundende- | repartir (varias cosas) | diccionario_general |
| `LEXR-03235` | jyũu- | 1. traer, llevar; 2. vestirse | diccionario_general |
| `LEXR-03236` | ndyiy | el hermano (respecto a la mujer) | diccionario_general |
| `LEXR-03237` | peequinze-, peequinzée- | poner mano encima de | diccionario_general |
| `LEXR-03238` | pytjaa yajcy- | sentir pesar | diccionario_general |
| `LEXR-03239` | quiwe muts | montículo de tierra | diccionario_general |
| `LEXR-03240` | sela | laurel de cera (árbol) | diccionario_general |
| `LEXR-03241` | sus-, susúu- | chorrear, escurrir | diccionario_general |
| `LEXR-03242` | ta’ts, ta’tscue | torcido | diccionario_general |
| `LEXR-03243` | tutyj letya | el abdomen | diccionario_general |
| `LEXR-03244` | tyute’te- | separarse (varias cosas, o varias personas) | diccionario_general |
| `LEXR-03245` | uucue’j-, uucue’je- | nivelar, allanar | diccionario_general |
| `LEXR-03246` | uuwa’jmeesa | inmortal | diccionario_general |
| `LEXR-03247` | vitvite | uno tras otro | diccionario_general |
| `LEXR-03248` | wẽsẽ | fleco, borde de la ruana | diccionario_general |
| `LEXR-03249` | ñusha beca | chicga de caña, guarapo | diccionario_general |
| `LEXR-03250` | ĩcj | el charco, lago | diccionario_general |
| `LEXR-03251` | ũuscha-, ũuscháa- | enojarse | diccionario_general |
| `LEXR-03252` | aan | a ver | diccionario_general |
| `LEXR-03253` | ay- | acá, aquí | diccionario_general |
| `LEXR-03254` | cseembu’j-, cseembu’ju- | hacer pliegues | diccionario_general |
| `LEXR-03255` | cunzha | cuchara (hecha de calabaza) | diccionario_general |
| `LEXR-03256` | cupytende- | quiebramaíz | diccionario_general |
| `LEXR-03257` | cuse watse | tendón de la mano | diccionario_general |
| `LEXR-03258` | ech | animal salvaje, fiera, el demonio | diccionario_general |
| `LEXR-03259` | ejy | la peña | diccionario_general |
| `LEXR-03260` | fytjaa we’we- | rogar, suplicar | diccionario_general |
| `LEXR-03261` | menz shã’py | el cangrejo, alacrán (arácnido) | diccionario_general |
| `LEXR-03262` | nus wajwa | llovizna | diccionario_general |
| `LEXR-03263` | peesu’s-, peesu’su- | regalar (varias veces or a varias personas) | diccionario_general |
| `LEXR-03264` | pesaj-, pesaja- | pasar de un lado a otro, venir del otro lado | diccionario_general |
| `LEXR-03265` | shlalá | granadilla (fruta) | diccionario_general |
| `LEXR-03266` | spjamb-, spjaambu- | despajar | diccionario_general |
| `LEXR-03267` | sunde- | romper, rasgar | diccionario_general |
| `LEXR-03268` | sute’te- | romperse (varias veces) | diccionario_general |
| `LEXR-03269` | swee- | dañarse | diccionario_general |
| `LEXR-03270` | tsñiñi- | sonar | diccionario_general |
| `LEXR-03271` | tu’j | el poporo | diccionario_general |
| `LEXR-03272` | tumb ucje | red (para atrapar pájaros) | diccionario_general |
| `LEXR-03273` | ucalitu | eucalipto (árbol) | diccionario_general |
| `LEXR-03274` | vyuu ets | billete | diccionario_general |
| `LEXR-03275` | vyuutyjã’ | chulco (planta medicinal) | diccionario_general |
| `LEXR-03276` | wa’wa- | podrirse | diccionario_general |
| `LEXR-03277` | yafy cjas | pestaña, ceja | diccionario_general |
| `LEXR-03278` | yuwe ũs- | reclamar, protestar | diccionario_general |
| `LEXR-03279` | zmeena’ | resplandor, fulgor | diccionario_general |
| `LEXR-03280` | ãj-, ãja- | poder, completar, alcanzar, llegar el tiempo | diccionario_general |
| `LEXR-03281` | beca mityj | olla para guarapo | diccionario_general |
| `LEXR-03282` | caauycjeũ’j-, caauycjeũ’ju- | hacer pasar por (ej. el río) | diccionario_general |
| `LEXR-03283` | chijme | el blanco (de raza blanca) | diccionario_general |
| `LEXR-03284` | chji’ndytey | todavía obscuro (en la madrugada) | diccionario_general |
| `LEXR-03285` | cmbale | el compadre | diccionario_general |
| `LEXR-03286` | cwe’we’j-, cwe’we’je- | dejar hablar, permitir hablar | diccionario_general |
| `LEXR-03287` | cysus-, syusu- | mentar, mencionar | diccionario_general |
| `LEXR-03288` | dyiicjẽy | de antemano | diccionario_general |
| `LEXR-03289` | llun (T) | el león (mamífero) | diccionario_general |
| `LEXR-03290` | maanteywe’sh | antepasados | diccionario_general |
| `LEXR-03291` | ncaacatjẽj | el suegro | diccionario_general |
| `LEXR-03292` | piinaa | el pepino | diccionario_general |
| `LEXR-03293` | pland pjapj | racimo de plátano | diccionario_general |
| `LEXR-03294` | pta’shni | aviso, anuncio | diccionario_general |
| `LEXR-03295` | pytjaa yuu- | sufrir | diccionario_general |
| `LEXR-03296` | quityji- | gotear | diccionario_general |
| `LEXR-03297` | quityáa- | 1. agacharse; 2. prender candela | diccionario_general |
| `LEXR-03298` | shquiicy | el chicao (ave amarillo) | diccionario_general |
| `LEXR-03299` | shũucãj- | perder sabor | diccionario_general |
| `LEXR-03300` | spẽ’tj-, spẽ’tje- | cortar | diccionario_general |
| `LEXR-03301` | tsuvy-, tsuvíi- | columpiar | diccionario_general |
| `LEXR-03302` | tuwúu- | acortar, mermar | diccionario_general |
| `LEXR-03303` | us chijme | fríjol blanco | diccionario_general |
| `LEXR-03304` | wẽtwẽt | muy agradable | diccionario_general |
| `LEXR-03305` | yu’ cbajy | agua hervida | diccionario_general |
| `LEXR-03306` | yuwe cja’ty | labio | diccionario_general |
| `LEXR-03307` | ze’nze | (planta) | diccionario_general |
| `LEXR-03308` | ñus cnay- | padecer | diccionario_general |
| `LEXR-03309` | aca yuu- | doler | diccionario_general |
| `LEXR-03310` | beca’j-, beca’ja- | hacer chicha | diccionario_general |
| `LEXR-03311` | cpiinda | la guayaba (fruta) | diccionario_general |
| `LEXR-03312` | cuentu’j-, cuentu’ju- | contar, relatar | diccionario_general |
| `LEXR-03313` | cuẽtya-, cuẽtyáa- | abollar | diccionario_general |
| `LEXR-03314` | dyi’tj | el hueso | diccionario_general |
| `LEXR-03315` | ipy ca’t | el lado del fogón | diccionario_general |
| `LEXR-03316` | na’ | por consiguiente, así que | diccionario_general |
| `LEXR-03317` | pũ’we | glotón, comilón | diccionario_general |
| `LEXR-03318` | quiwe cuet | terrón | diccionario_general |
| `LEXR-03319` | scuupy- | mudar la piel | diccionario_general |
| `LEXR-03320` | shã’py-, shã’pi- | 1. echar ramas; 2. tener vástago | diccionario_general |
| `LEXR-03321` | stende- | 1. rasgar, romper; 2. changuar, separar hebras (de cabuya o bejuco) | diccionario_general |
| `LEXR-03322` | tatawe’sh | los padres (padre y madre) | diccionario_general |
| `LEXR-03323` | tcafy | el desfiladero | diccionario_general |
| `LEXR-03324` | tjã’j | el cerro | diccionario_general |
| `LEXR-03325` | tsut ej | roza de choclo | diccionario_general |
| `LEXR-03326` | tũchji’chji- | genir (repetidas veces) | diccionario_general |
| `LEXR-03327` | utse tash | mata de aguacate | diccionario_general |
| `LEXR-03328` | wej yujva | ni un poco, ni siquiera | diccionario_general |
| `LEXR-03329` | zuntete- | resplandecer | diccionario_general |
| `LEXR-03330` | atyáj-, atyája- | 1. poner, colocar encima de 2. averiguar, investigar | diccionario_general |
| `LEXR-03331` | caacwecha’j-, caacwecha’ja- | hacer lavar las manos | diccionario_general |
| `LEXR-03332` | cafy | el hueco, hoyo, agujero, cueva | diccionario_general |
| `LEXR-03333` | chuwatyj | el carángano (insecto) | diccionario_general |
| `LEXR-03334` | claa luuch | el ternero | diccionario_general |
| `LEXR-03335` | cpaacycjiyu’j-, cpaacycjiyu’ju- | lograr hacer entender | diccionario_general |
| `LEXR-03336` | dyi’j | el camino | diccionario_general |
| `LEXR-03337` | echtjẽ’j | el diablo | diccionario_general |
| `LEXR-03338` | fytũu watse | la raíz (de árbol) | diccionario_general |
| `LEXR-03339` | iimujcue- | cerrar la boca | diccionario_general |
| `LEXR-03340` | nasa nwe’sh | de la misma tribu páez | diccionario_general |
| `LEXR-03341` | pcji’cj-, pcji’cji- | lavar (loza) | diccionario_general |
| `LEXR-03342` | peltunaĩ- | perdonar | diccionario_general |
| `LEXR-03343` | quĩj yuupa’ga | ?por qué? | diccionario_general |
| `LEXR-03344` | shamb | el pueblo, caserío | diccionario_general |
| `LEXR-03345` | shi’ndy-, shi’ndyi- (chji’ndy-) | obscurecerse | diccionario_general |
| `LEXR-03346` | tlaapichi | el trapiche | diccionario_general |
| `LEXR-03347` | tyachwe’sh | cosa usada, no nueva | diccionario_general |
| `LEXR-03348` | tyacjue, tyacjuey | tamaño, dimensión de altura, anchura, profundidad | diccionario_general |
| `LEXR-03349` | wejya’jya- | correr brisa | diccionario_general |
| `LEXR-03350` | ya’cy-, ya’qui- | colgarse, ahorcarse | diccionario_general |
| `LEXR-03351` | ũpatel | la escopeta | diccionario_general |
| `LEXR-03352` | baytu’cni | oxidado | diccionario_general |
| `LEXR-03353` | cjãas | la ortiga | diccionario_general |
| `LEXR-03354` | csha’wte | en sueños | diccionario_general |
| `LEXR-03355` | finzh | la guacharaca (ave) | diccionario_general |
| `LEXR-03356` | jytundnisa | cinturón | diccionario_general |
| `LEXR-03357` | jyuuts atyj | la blusa de lana | diccionario_general |
| `LEXR-03358` | maa yujva | nadie, ninguno | diccionario_general |
| `LEXR-03359` | meetu’j | la tripa, el intestino | diccionario_general |
| `LEXR-03360` | mjĩisa | el trabajador | diccionario_general |
| `LEXR-03361` | nenga yu’ | caldo | diccionario_general |
| `LEXR-03362` | ptsuuts | sobrino o sobrina con tía | diccionario_general |
| `LEXR-03363` | quijyáa- | sobrar | diccionario_general |
| `LEXR-03364` | tee cus uta | toda la noche | diccionario_general |
| `LEXR-03365` | tjũ’we chũpy | orejudo | diccionario_general |
| `LEXR-03366` | tũpy | pelado, desnudo | diccionario_general |
| `LEXR-03367` | waga’te fytũu | el palo del huso | diccionario_general |
| `LEXR-03368` | yafy tsẽy | zarco | diccionario_general |
| `LEXR-03369` | yaptende- | desenvolver | diccionario_general |
| `LEXR-03370` | yu’ | 1. el agua; 2. líquido | diccionario_general |
| `LEXR-03371` | yũunani | el ayuno | diccionario_general |
| `LEXR-03372` | ángeles cu’jni | baile de un niño muerto | diccionario_general |
| `LEXR-03373` | ãjmée | insuficiente, incompleto, menos | diccionario_general |
| `LEXR-03374` | ẽsh ej | campo de coca | diccionario_general |
| `LEXR-03375` | aca ũs- | causar dolor o enfermedad | diccionario_general |
| `LEXR-03376` | chji’ndy | obscuro | diccionario_general |
| `LEXR-03377` | chuctende- | arrancar espigas | diccionario_general |
| `LEXR-03378` | cleechi’j-, cleechi’ji- | hacer cosquillas | diccionario_general |
| `LEXR-03379` | cpuunu’j-, cpuunu’ju- | castrar, capar | diccionario_general |
| `LEXR-03380` | ipy cuet | la tulpa | diccionario_general |
| `LEXR-03381` | lel | reumatismo articular (enfermedad de los huesos) | diccionario_general |
| `LEXR-03382` | ma’wẽva | comoquiera | diccionario_general |
| `LEXR-03383` | paautyáa- | acercarse voluntariamente | diccionario_general |
| `LEXR-03384` | pecue- | dar paliza | diccionario_general |
| `LEXR-03385` | peescatyjĩ’j-, peescatyjĩ’ja- | atizar (la lumbre) | diccionario_general |
| `LEXR-03386` | pits pyacj | el concuñado | diccionario_general |
| `LEXR-03387` | ptsu’wa | cuñado con cuñada | diccionario_general |
| `LEXR-03388` | sapete | la guala (ave, como gallinazo) | diccionario_general |
| `LEXR-03389` | su’s-, su’su- | orinar | diccionario_general |
| `LEXR-03390` | sñula- (syuula-) | salir mazorca | diccionario_general |
| `LEXR-03391` | tpejng-, tpengu- | doblar | diccionario_general |
| `LEXR-03392` | tujnd-, tujndu- | calmarse, cesar | diccionario_general |
| `LEXR-03393` | tywete-, tyewetée- | soltar, desatar | diccionario_general |
| `LEXR-03394` | ujnde-, unde- | 1. cosechar, cortar café, fríjol; 2. desplumar | diccionario_general |
| `LEXR-03395` | ya’cpã’yuu- | herirse, lastimarse | diccionario_general |
| `LEXR-03396` | zi’nzi- | zumbar | diccionario_general |
| `LEXR-03397` | am | el hacha | diccionario_general |
| `LEXR-03398` | bej-m, beje- | arder | diccionario_general |
| `LEXR-03399` | cha’cy | lama (planta parasítica) | diccionario_general |
| `LEXR-03400` | cjash yu’ | chicha de maíz | diccionario_general |
| `LEXR-03401` | cutyj tymi | tusa de maíz | diccionario_general |
| `LEXR-03402` | e’stewe’sh | menor, segundo | diccionario_general |
| `LEXR-03403` | een, eena’ | la luz, claridad | diccionario_general |
| `LEXR-03404` | i’cue’sh | con ustedes | diccionario_general |
| `LEXR-03405` | icjni | instrumento para matar | diccionario_general |
| `LEXR-03406` | iiwejch we’weni | orgullo (habla) | diccionario_general |
| `LEXR-03407` | jycuet dyi’tj | cráneo | diccionario_general |
| `LEXR-03408` | ncuutyi’j-, ncuutyi’ji- | sacar (sin permiso, cosa ajena) | diccionario_general |
| `LEXR-03409` | nus pa’j- | llover | diccionario_general |
| `LEXR-03410` | nuytandyi- | llevar alrededor de (ej. en procesión) | diccionario_general |
| `LEXR-03411` | payu | bayo | diccionario_general |
| `LEXR-03412` | pcamb-, pcambu- | urdir, preparar los hilos de la urdimbre | diccionario_general |
| `LEXR-03413` | pitstjẽ’j | el hombre (adulto) | diccionario_general |
| `LEXR-03414` | shcajnde-, shcande- | fracturar, quebrar | diccionario_general |
| `LEXR-03415` | spajnde-, spande- | templar | diccionario_general |
| `LEXR-03416` | ta’ñi- | tener sesaciones (sentir ’señas’) | diccionario_general |
| `LEXR-03417` | tyjĩ’te | el arrayán (árbol) | diccionario_general |
| `LEXR-03418` | wa’wa | podrido | diccionario_general |
| `LEXR-03419` | wẽy-, wẽyíi- | gatear | diccionario_general |
| `LEXR-03420` | yutj-, yutjáa- | soplar la candela | diccionario_general |
| `LEXR-03421` | yuwe cjas | bigote, barba | diccionario_general |
| `LEXR-03422` | ĩitse’j-, ĩitse’je- | cocer | diccionario_general |
| `LEXR-03423` | ũuschaani | el enojo, la ira | diccionario_general |
| `LEXR-03424` | a’teweete | en tiempo de luna | diccionario_general |
| `LEXR-03425` | aca cnay- | sufrir dolor | diccionario_general |
| `LEXR-03426` | caaj-, caja- | mandar, enviar | diccionario_general |
| `LEXR-03427` | cafi´j-, cafi´ji- | cavar, abrir hoyo, ahuecar | diccionario_general |
| `LEXR-03428` | cjẽete | volteado (boca arriba) | diccionario_general |
| `LEXR-03429` | cleechi’ch-, cleechi’chi- | flamear, despedir llamas | diccionario_general |
| `LEXR-03430` | cmbamba dyi’tj | la quijada | diccionario_general |
| `LEXR-03431` | cshi’ta’j-, cshi’ta’ja- | echar humo, evaporar, quemar incienso | diccionario_general |
| `LEXR-03432` | cuvyasa, cuvytewe’sh | el flautista | diccionario_general |
| `LEXR-03433` | dyuus yat | la iglesia | diccionario_general |
| `LEXR-03434` | icha | tu (niña o pariente fememina) | diccionario_general |
| `LEXR-03435` | jetu’t-, jetu’tu- | sollozar | diccionario_general |
| `LEXR-03436` | ji’j | el linaje, la raza, el descendiente | diccionario_general |
| `LEXR-03437` | jychanzha-, jychanzháa- | limpiar, mugre, quitar contaminación | diccionario_general |
| `LEXR-03438` | jysũutj-, jysũutje- (fysũutje- T) | esconderse | diccionario_general |
| `LEXR-03439` | neewe’we- | encomendar | diccionario_general |
| `LEXR-03440` | pẽjy-, pẽyi- | pedir | diccionario_general |
| `LEXR-03441` | shũulape (shũulepja) | (planta medicinal) | diccionario_general |
| `LEXR-03442` | taqui’sa | el creador | diccionario_general |
| `LEXR-03443` | villa | la hebilla (del cinturón) | diccionario_general |
| `LEXR-03444` | yuuwe | la culpa, delito | diccionario_general |
| `LEXR-03445` | yãja- (ñaja-) | chuzar, punzar | diccionario_general |
| `LEXR-03446` | a’cyni | colgado | diccionario_general |
| `LEXR-03447` | atall cjas | pluma de gallina | diccionario_general |
| `LEXR-03448` | atsewe’wesa | que habla con desprecio | diccionario_general |
| `LEXR-03449` | cshavy- | en medio de, entre | diccionario_general |
| `LEXR-03450` | cuse pjapj | palma de la mano | diccionario_general |
| `LEXR-03451` | cysu | por allí | diccionario_general |
| `LEXR-03452` | en | el día, tiempo | diccionario_general |
| `LEXR-03453` | fytũu cu’ta | rama de árbol | diccionario_general |
| `LEXR-03454` | i’cue | tu, su, de usted | diccionario_general |
| `LEXR-03455` | jyandu-, jyandúu- | paralizarse, entumirse | diccionario_general |
| `LEXR-03456` | jyaw-, jyawu- | vaciar (líquido) | diccionario_general |
| `LEXR-03457` | pcyuu- | maltratar | diccionario_general |
| `LEXR-03458` | pe’w-, pe’wu- | pedir, preguntar | diccionario_general |
| `LEXR-03459` | pyajtse-, pyaatse- | dar asco, desagradar | diccionario_general |
| `LEXR-03460` | scuutyj cweejya’jya’ | aventar trigo | diccionario_general |
| `LEXR-03461` | stela | la estera | diccionario_general |
| `LEXR-03462` | tsinz dyi’tj | espina dorsal | diccionario_general |
| `LEXR-03463` | tuñi- | encorvarse, inclinarse | diccionario_general |
| `LEXR-03464` | yacjtjẽ’j | el hermano, la hermana (del mismo sexo) | diccionario_general |
| `LEXR-03465` | yafy dyuus | niña del ojo, pupila | diccionario_general |
| `LEXR-03466` | yat punza eca | esquina de la casa | diccionario_general |
| `LEXR-03467` | yesenisa | bautizado | diccionario_general |
| `LEXR-03468` | ĩtyĩ vit- | resucitar | diccionario_general |
| `LEXR-03469` | apas | haba | diccionario_general |
| `LEXR-03470` | caacpunga’j-, caacpunga’ja- | hacer vomitar | diccionario_general |
| `LEXR-03471` | caaimi’a’j-caaimi’aja-(cmi’a’j-) | dar a la hija en casamiento, permitir a la hija casarse | diccionario_general |
| `LEXR-03472` | cjimbtende- | desbaratar (varias cosas) | diccionario_general |
| `LEXR-03473` | cu’nd-, cu’ndu- | moler caña | diccionario_general |
| `LEXR-03474` | cyãawe’sh (tyãawe’sh) | ellos, ellas | diccionario_general |
| `LEXR-03475` | dyi’p | en frente de, delante de, ante | diccionario_general |
| `LEXR-03476` | ewmée | malo | diccionario_general |
| `LEXR-03477` | juuna’sa | severo, temible | diccionario_general |
| `LEXR-03478` | nuyle’ch-, nuyle’chi- | achicar, comprimir, reducir de tamaño | diccionario_general |
| `LEXR-03479` | paatjeng-, paatjengu- | cuidar de, vigilar (en ausencia del dueño) | diccionario_general |
| `LEXR-03480` | pasu’s- | contestar (repetidas veces) | diccionario_general |
| `LEXR-03481` | sembu’j-, sembu’ju- | plegar | diccionario_general |
| `LEXR-03482` | sende’nde- | enfilarse (según cierto orden) | diccionario_general |
| `LEXR-03483` | shande- | desgranar, cosechar | diccionario_general |
| `LEXR-03484` | shcayatú | ampolla | diccionario_general |
| `LEXR-03485` | shicani | la risa | diccionario_general |
| `LEXR-03486` | swẽtj-, swẽtje- | patear | diccionario_general |
| `LEXR-03487` | tende- | tender | diccionario_general |
| `LEXR-03488` | tsjende cuvy | la flauta (de carrizos verticales) | diccionario_general |
| `LEXR-03489` | ucani | montaña derribada | diccionario_general |
| `LEXR-03490` | yã’py-, yã’pji- | cobijarse con otra persona | diccionario_general |
| `LEXR-03491` | ¡uvy uvy! | ¡Fuera! (ahuyentando gallinas) | diccionario_general |
| `LEXR-03492` | ape | el zapallo rayado | diccionario_general |
| `LEXR-03493` | bats yaj | fibra de cabuya | diccionario_general |
| `LEXR-03494` | buch-, bucha- | retoñar, brotar | diccionario_general |
| `LEXR-03495` | ca’tyji’j-, ca’tyji’ji- | hacer estornudar | diccionario_general |
| `LEXR-03496` | canzh yuu- | cometer adulterio | diccionario_general |
| `LEXR-03497` | cjyu’ja’j-, cjyu’ja’ja- | dejar crecer el pelo | diccionario_general |
| `LEXR-03498` | cu’ju qui’p- | celebrar en baile | diccionario_general |
| `LEXR-03499` | cũupjũj-, cũupjũju- | hacer estrechar la mano (ej. en las bodas) | diccionario_general |
| `LEXR-03500` | dejmée pe’te- | transnochar | diccionario_general |
| `LEXR-03501` | dyi’- | medio, a medias, no enteramente | diccionario_general |
| `LEXR-03502` | jimba cjũch | la danta (mamífero) | diccionario_general |
| `LEXR-03503` | le’chi- | mermar, disminuir, encogerse | diccionario_general |
| `LEXR-03504` | muuse’j-, muuse’je- | desmenuzar, hacer polvo de | diccionario_general |
| `LEXR-03505` | pcalsa | el pecador | diccionario_general |
| `LEXR-03506` | pecu’tjwe’sh | olvidar | diccionario_general |
| `LEXR-03507` | pyãj, pyãjn | mitad | diccionario_general |
| `LEXR-03508` | scuela | escuela | diccionario_general |
| `LEXR-03509` | sẽj-, sẽje-, sẽe- | bajar, descender | diccionario_general |
| `LEXR-03510` | tpand | rollo | diccionario_general |
| `LEXR-03511` | tyi’fy | el búho, la lechuza (ave) | diccionario_general |
| `LEXR-03512` | ulchic | urraca | diccionario_general |
| `LEXR-03513` | weech-, weechi- | rechazar, burlar, despreciar | diccionario_general |
| `LEXR-03514` | yultumu | mayordomo | diccionario_general |
| `LEXR-03515` | caapdyi’pu’j-, caapdyi’pju’ju- | hacer encarar | diccionario_general |
| `LEXR-03516` | cutyj ũus | germen de maíz | diccionario_general |
| `LEXR-03517` | letya | el abdomen | diccionario_general |
| `LEXR-03518` | pcyuuwe’we- | ultrajar | diccionario_general |
| `LEXR-03519` | plaaĩ-, plaaĩi- | pilar, cocer maíz para quitar la cáscara | diccionario_general |
| `LEXR-03520` | puuty ya’cviisha’j-, puuty ya’cviisha’ja- | consolarse (mutuamente) | diccionario_general |
| `LEXR-03521` | qui’p-, qui’pu- | 1. poner, inyectar; 2. nombrar en un puesto | diccionario_general |
| `LEXR-03522` | shande | tusilla (planta) | diccionario_general |
| `LEXR-03523` | shũuwe’tj | escancel (planta medicinal) | diccionario_general |
| `LEXR-03524` | sã’jĩ- | 1. alimentar; 2. hacer un flavor | diccionario_general |
| `LEXR-03525` | tishi- | pararse, ponerse de pie | diccionario_general |
| `LEXR-03526` | tujca-, tuca- | tocar (un instrumento musical) | diccionario_general |
| `LEXR-03527` | u’p-, u’pu- | estar (sentado, acostado, coljado), habitar, morar | diccionario_general |
| `LEXR-03528` | uusá jycuet dyi’tj | calavera | diccionario_general |
| `LEXR-03529` | yu’alcu | nutria | diccionario_general |
| `LEXR-03530` | zits chijme | claro de huevo | diccionario_general |
| `LEXR-03531` | ã’ wala | lucero | diccionario_general |
| `LEXR-03532` | ũus chjãchjãsa | valiente | diccionario_general |
| `LEXR-03533` | avytjetj-, avytjetje- | escupir en | diccionario_general |
| `LEXR-03534` | chcandende- | quebrar (varios huesos) | diccionario_general |
| `LEXR-03535` | cjã’ng | la hormiga (insecto) | diccionario_general |
| `LEXR-03536` | cjĩjtse (cjitsa T) | el murcielago (mamífero) | diccionario_general |
| `LEXR-03537` | cutyj ej | la roza, el maizal | diccionario_general |
| `LEXR-03538` | cyãa (tyãa) | ese, esa | diccionario_general |
| `LEXR-03539` | fytjaa, fytjaacuẽ | pobre, pobrecito | diccionario_general |
| `LEXR-03540` | jytjãas-, jytjãasu- | desear | diccionario_general |
| `LEXR-03541` | jũ’na | ayer | diccionario_general |
| `LEXR-03542` | mẽ’ne, mẽ’newe | ¡Llore! | diccionario_general |
| `LEXR-03543` | pta’shsa | que avisa, que anuncia | diccionario_general |
| `LEXR-03544` | pucacje ndyiy | primo (respecto a la prima) | diccionario_general |
| `LEXR-03545` | sendy yuu- | volverse mezquino | diccionario_general |
| `LEXR-03546` | talli- | enflaquecerse | diccionario_general |
| `LEXR-03547` | tjẽeyũu- | durar | diccionario_general |
| `LEXR-03548` | tsam wes | alambre | diccionario_general |
| `LEXR-03549` | uycjẽw, uycjẽúu- | atravesar, cruzar, pasar al otro lado | diccionario_general |
| `LEXR-03550` | wechana ũs-, wechana u’p- | estar contento | diccionario_general |
| `LEXR-03551` | yu’cuet | el hielo | diccionario_general |
| `LEXR-03552` | ajtsajtse | desprecio | diccionario_general |
| `LEXR-03553` | anz-, anzúu- | cubrir, tapar (con cobija) | diccionario_general |
| `LEXR-03554` | atsju- | 1. trabar, eredar 2. acornear | diccionario_general |
| `LEXR-03555` | atyj chal | ruana o anaco grueso | diccionario_general |
| `LEXR-03556` | cfi’ja’j-, cfi’ja’ja- | hacer escribir | diccionario_general |
| `LEXR-03557` | chinda | el pie, la pierna (de persona), la pata (de animal) | diccionario_general |
| `LEXR-03558` | cuch yajcy- | preocuparse | diccionario_general |
| `LEXR-03559` | cul | cogollo | diccionario_general |
| `LEXR-03560` | cwẽese’j-, cwẽese’je- | permitir oír | diccionario_general |
| `LEXR-03561` | cã’pji’j-, cãpj’ji- | echar una clueca | diccionario_general |
| `LEXR-03562` | jycaa-jycaja- | ordenar, gobernar | diccionario_general |
| `LEXR-03563` | jyũcjwende- | desatar nudo | diccionario_general |
| `LEXR-03564` | luucu yuu- | enloquecerse | diccionario_general |
| `LEXR-03565` | mcaa (mgaa T) | de donde, ¿de dónde? | diccionario_general |
| `LEXR-03566` | neesu- | contagiarse | diccionario_general |
| `LEXR-03567` | nwẽese’j-, nwẽese’je- | odedecer, hacer caso | diccionario_general |
| `LEXR-03568` | pchanga | pechanga, verbena (planta) | diccionario_general |
| `LEXR-03569` | pdeepits | el fornicador | diccionario_general |
| `LEXR-03570` | peendu’jni | rayado | diccionario_general |
| `LEXR-03571` | quimbe’j-, quimbe’je- | hacer seña | diccionario_general |
| `LEXR-03572` | shpite- (shapite) | desgajarse, desprenderse | diccionario_general |
| `LEXR-03573` | tjẽ’j we’we- | hechizar | diccionario_general |
| `LEXR-03574` | tjẽ’jsa | adulto, mayor de edad | diccionario_general |
| `LEXR-03575` | wa’ta | la montura | diccionario_general |
| `LEXR-03576` | well wala | guacamayo | diccionario_general |
| `LEXR-03577` | yajtse- | disgustarse | diccionario_general |
| `LEXR-03578` | ãj | suficiente, complete | diccionario_general |
| `LEXR-03579` | ĩcj wala | el mar | diccionario_general |
| `LEXR-03580` | ũ’tsj-, ũ’tsju- | 1. cepillar, labrar madera; 2. rebanar | diccionario_general |
| `LEXR-03581` | ũtj | el muchilero (ave) | diccionario_general |
| `LEXR-03582` | atsjute- | zafarse, desengarzarse | diccionario_general |
| `LEXR-03583` | caaspẽtje’j’, caaspẽtje’je- | mandar cortar (pelo, tabla) | diccionario_general |
| `LEXR-03584` | cuch vit-, cuch vitu- | molestar, poner pereque | diccionario_general |
| `LEXR-03585` | cuetand tu’j | el poporo | diccionario_general |
| `LEXR-03586` | jypaang- | fracturar | diccionario_general |
| `LEXR-03587` | jyu’j quiwe | tierra lejana | diccionario_general |
| `LEXR-03588` | me’ca, me’cawe | ¡Entre! | diccionario_general |
| `LEXR-03589` | msuu | donde, ¿de dónde? (para abajo), ¿por dónde? | diccionario_general |
| `LEXR-03590` | pi’pyshavy | Pijaos (tribu indígena) | diccionario_general |
| `LEXR-03591` | pjãjã- | toser | diccionario_general |
| `LEXR-03592` | pleecu’c | soledad | diccionario_general |
| `LEXR-03593` | shawendu’ndu- | ir y venir (varias veces) | diccionario_general |
| `LEXR-03594` | shiing-, shiingúu- | sentirse incapaz | diccionario_general |
| `LEXR-03595` | tse’-, tse’e- | robar | diccionario_general |
| `LEXR-03596` | ul tsẽy | guache (culebra) | diccionario_general |
| `LEXR-03597` | caanwẽese’j-, caanwẽese’je-(cnwẽese’j-) | hacer obedecer | diccionario_general |
| `LEXR-03598` | caawũwu’j-, caawũwu’ju- | hacer menear | diccionario_general |
| `LEXR-03599` | cjaavi’j-, cjaavi’ji- | desgranar | diccionario_general |
| `LEXR-03600` | cue’nz | la arruga | diccionario_general |
| `LEXR-03601` | cuse ũus | el dedo cordial o de en medio | diccionario_general |
| `LEXR-03602` | fi’jnisa | escritura | diccionario_general |
| `LEXR-03603` | fiesta’ja- | hacer fiesta | diccionario_general |
| `LEXR-03604` | inzũ’ni | oxidado, corroído | diccionario_general |
| `LEXR-03605` | jwet-, jwetáa- | encogerse | diccionario_general |
| `LEXR-03606` | nee | todavía | diccionario_general |
| `LEXR-03607` | nish | la pulpa, la carne | diccionario_general |
| `LEXR-03608` | nuycatyjisa | que sana | diccionario_general |
| `LEXR-03609` | nuycãj-, nuycãja- | traer (desde abajo) | diccionario_general |
| `LEXR-03610` | pshũ’ju- | causar sombra | diccionario_general |
| `LEXR-03611` | pta’nz | la mugre, contaminación | diccionario_general |
| `LEXR-03612` | quita | macana, arma del telar | diccionario_general |
| `LEXR-03613` | selpíi- | servir, ser útil | diccionario_general |
| `LEXR-03614` | spiiga | la espiga | diccionario_general |
| `LEXR-03615` | yu’tsesa (yu’tsesatjẽ’j T) | el curandero | diccionario_general |
| `LEXR-03616` | ñu’py le’chcue | agutí, guatín (mamífero roedor) | diccionario_general |
| `LEXR-03617` | a’cji’j-, a’cji’ji- | pisar, pisotear | diccionario_general |
| `LEXR-03618` | catsunde- | descoser (una costura) | diccionario_general |
| `LEXR-03619` | cutyj | el maíz | diccionario_general |
| `LEXR-03620` | cutyj dyi’tj ej | el maizal (depués de cosechar) | diccionario_general |
| `LEXR-03621` | cãj-, cãjã- | subir | diccionario_general |
| `LEXR-03622` | ets | la hoja (de árbol o planta), el papel | diccionario_general |
| `LEXR-03623` | fi’fy-, fi’fi- | silbar | diccionario_general |
| `LEXR-03624` | lucjlucj jĩ- | cloquear | diccionario_general |
| `LEXR-03625` | mum tuca | tarro de guadua | diccionario_general |
| `LEXR-03626` | nuyquĩj-, nuyquĩji- | traer (desde arriba), bajar (ej. a un enfermo) | diccionario_general |
| `LEXR-03627` | nuyzuna’- | apretar | diccionario_general |
| `LEXR-03628` | pel upj | cerca de carrizo | diccionario_general |
| `LEXR-03629` | puii we’we- | argumentar | diccionario_general |
| `LEXR-03630` | shape | el caracol | diccionario_general |
| `LEXR-03631` | ta’ngu- | dar vuelta | diccionario_general |
| `LEXR-03632` | tyic-, tyicu- | hartarse, saciarse | diccionario_general |
| `LEXR-03633` | ujne | el hongo (planta) | diccionario_general |
| `LEXR-03634` | uuwa’jsa | mortal, destinado a morir | diccionario_general |
| `LEXR-03635` | ya’jytund- | ceñirse | diccionario_general |
| `LEXR-03636` | ũ’we | la harina | diccionario_general |
| `LEXR-03637` | acj | la trampa | diccionario_general |
| `LEXR-03638` | chavytũu | el higuerón, canela de páramo (árbol) | diccionario_general |
| `LEXR-03639` | cjũch bejbej | morado | diccionario_general |
| `LEXR-03640` | cuse chavy | el músculo | diccionario_general |
| `LEXR-03641` | cãjpy | conejo (mamífero) | diccionario_general |
| `LEXR-03642` | e’shavy | oso | diccionario_general |
| `LEXR-03643` | iimi’ya’ passa | comprometida (la novia) | diccionario_general |
| `LEXR-03644` | jũ’na cuscjẽ | antenoche | diccionario_general |
| `LEXR-03645` | kutxh | maíz | diccionario_general |
| `LEXR-03646` | mielcules | el miércoles | diccionario_general |
| `LEXR-03647` | patmu en | la boda, día del casamiento | diccionario_general |
| `LEXR-03648` | puuty ijca-, puuty iica- | chocar con | diccionario_general |
| `LEXR-03649` | shpijnde-, shpinde- (shapijnde-) | desgajar | diccionario_general |
| `LEXR-03650` | soldau | el soldado | diccionario_general |
| `LEXR-03651` | ya’luch | prole, cría | diccionario_general |
| `LEXR-03652` | ye’tsje- | sentir (cuando otro la toca) | diccionario_general |
| `LEXR-03653` | yu’ptjej-, yu’ptjeje- | 1. Intercambiar; 2. transformar | diccionario_general |
| `LEXR-03654` | cacue cja’ty | el cadáver | diccionario_general |
| `LEXR-03655` | chcateni | fracturado | diccionario_general |
| `LEXR-03656` | chijme yuuni | pálido | diccionario_general |
| `LEXR-03657` | cytũus bej | arco del día | diccionario_general |
| `LEXR-03658` | fi’nzeni | la vida | diccionario_general |
| `LEXR-03659` | iiwajca-, iiwaaca- | cortarse (el pelo) | diccionario_general |
| `LEXR-03660` | jwendu-, jwendúu- | amarrar varias vueltas | diccionario_general |
| `LEXR-03661` | mama lula | la abuela, bisabuela | diccionario_general |
| `LEXR-03662` | puuty ya’peeygãj-, puuty ya’peeygãja- | amarse (mutuamente) | diccionario_general |
| `LEXR-03663` | pytjaa, pytjaacuẽ | pobre, pobrecito | diccionario_general |
| `LEXR-03664` | pũpy-, pũpíi- | juntar, unir | diccionario_general |
| `LEXR-03665` | quitya’tya- | agacharse (repetidas veces) | diccionario_general |
| `LEXR-03666` | tmbi’ch | alchucha (planta comestible) | diccionario_general |
| `LEXR-03667` | tyu’ndende- | repartir (varias cosas entre varias personas) | diccionario_general |
| `LEXR-03668` | wa’cy-, wa’qui- | 1. moder (perro, culebra); 2. picar | diccionario_general |
| `LEXR-03669` | wee | la enfermedad, peste, epidemia | diccionario_general |
| `LEXR-03670` | yaase- | llamarse | diccionario_general |
| `LEXR-03671` | yuwe wã’jy | afta | diccionario_general |
| `LEXR-03672` | ẽepyãj | el mediodía | diccionario_general |
| `LEXR-03673` | chinda tuty | la pantorrilla | diccionario_general |
| `LEXR-03674` | cuchi ĩts | el hocico del puerco | diccionario_general |
| `LEXR-03675` | fĩsh, fynej | mosca | diccionario_general |
| `LEXR-03676` | le’ch, le’chcuẽ | pequeño | diccionario_general |
| `LEXR-03677` | limeeta | la limeta | diccionario_general |
| `LEXR-03678` | llimún | el limón (fruta) | diccionario_general |
| `LEXR-03679` | mestláa- | hacer un rito (brujo) | diccionario_general |
| `LEXR-03680` | nus quĩj- | llover | diccionario_general |
| `LEXR-03681` | nusu-, nusúu- | hacer invierno | diccionario_general |
| `LEXR-03682` | pilwe’sh | el curandero, hechicero | diccionario_general |
| `LEXR-03683` | quiite-, quiitée- | empezar | diccionario_general |
| `LEXR-03684` | shita | avispa (insecto) | diccionario_general |
| `LEXR-03685` | tjuc-, tjucu- | estrangular | diccionario_general |
| `LEXR-03686` | tsẽy | azul, verde | diccionario_general |
| `LEXR-03687` | ya’patj-, ya’patjée- | cubrirse (ej. con un pañolón) | diccionario_general |
| `LEXR-03688` | yatsgawe’sh | 1. los antepasados; 2. oficiales salientes | diccionario_general |
| `LEXR-03689` | yu’ tũchjasa | ola (del río o mar) | diccionario_general |
| `LEXR-03690` | ñus pu’ch- | condolerse, compartir la flicción de otro | diccionario_general |
| `LEXR-03691` | ũucj yajcy- | atemorizarse | diccionario_general |
| `LEXR-03692` | ẽsẽmée | quieto | diccionario_general |
| `LEXR-03693` | bajts | la cabuya, el fique | diccionario_general |
| `LEXR-03694` | ca’t, ca’tu, ca’tsuy | rumbo a, hacia (recíproco) | diccionario_general |
| `LEXR-03695` | caapena’j-, caapena’ja | hacer abundar | diccionario_general |
| `LEXR-03696` | echtsẽy | la luciérnaga (insecto) | diccionario_general |
| `LEXR-03697` | iiũucj- | tener miedo | diccionario_general |
| `LEXR-03698` | peeygãasa | que tiene misericordia, que ama | diccionario_general |
| `LEXR-03699` | sec cãj- | salir el sol | diccionario_general |
| `LEXR-03700` | tjũwe (tjũwa T) | la oreja | diccionario_general |
| `LEXR-03701` | tjẽ’j-, tjẽ’je- | 1. madurar; 2. envejecerse | diccionario_general |
| `LEXR-03702` | upj-, upjáa- | 1. cercar; 2. cerrar los ojos | diccionario_general |
| `LEXR-03703` | yat pwa’ | corredor | diccionario_general |
| `LEXR-03704` | bats watse | raíz de cabuya | diccionario_general |
| `LEXR-03705` | caatundyi’j-, caatundyi’ji | hacer beber | diccionario_general |
| `LEXR-03706` | cpẽeu’j-, cpẽeu’ju- | hacer bañar (a otro) | diccionario_general |
| `LEXR-03707` | ctyaaja’j-, ctyaaja’ja- | hacer ponr, mandar ponder | diccionario_general |
| `LEXR-03708` | cytã’ tujnd | polvo de la casa | diccionario_general |
| `LEXR-03709` | dycjas | el pelo, cabello | diccionario_general |
| `LEXR-03710` | jytund-, jytundu- | ceñirse, amarrar (con correa o chumbe) | diccionario_general |
| `LEXR-03711` | lisa-, lisáa- | rezar | diccionario_general |
| `LEXR-03712` | pa’ga yuu- | sufrir | diccionario_general |
| `LEXR-03713` | pa’jwa’j | llegada (futura) | diccionario_general |
| `LEXR-03714` | paashijca-, paashica- | reirse con los que se ríen | diccionario_general |
| `LEXR-03715` | pucacje ntsu’wa | esposa del primo | diccionario_general |
| `LEXR-03716` | pũsh-, pũshi- | regar (granos), esparcir, repartir | diccionario_general |
| `LEXR-03717` | teesacy | seis | diccionario_general |
| `LEXR-03718` | une tash | mata de hongo | diccionario_general |
| `LEXR-03719` | zuuna’ | apretado | diccionario_general |
| `LEXR-03720` | ã’ mush | vía láctea | diccionario_general |
| `LEXR-03721` | ãwã | el ají (planta, usada como condimento) | diccionario_general |
| `LEXR-03722` | ũ’cue | mi (femenino) | diccionario_general |
| `LEXR-03723` | acjus | el ajo | diccionario_general |
| `LEXR-03724` | aj cshi’ta’j- | ahumar | diccionario_general |
| `LEXR-03725` | caapa’ja’j-, caapa’ja’ja-(cpa’ja’j-) | hacer llegar | diccionario_general |
| `LEXR-03726` | catashi´jni | encabado | diccionario_general |
| `LEXR-03727` | chanzh-, chanzháa- | 1. chupar 2. absorbar 3. fumar (tobaco) | diccionario_general |
| `LEXR-03728` | cpaandewe- | pagar por otro | diccionario_general |
| `LEXR-03729` | cpaasu’j-, cpaasu’ju- | permitir contestar | diccionario_general |
| `LEXR-03730` | cuwe’j-, cuwe’je- | hacer coger, hacer prender | diccionario_general |
| `LEXR-03731` | cwaatyi’j-, cwaatyi’ji- | cansar, fatigar | diccionario_general |
| `LEXR-03732` | davy-, davíi- | revolver, menear | diccionario_general |
| `LEXR-03733` | ej atũ | plataforma en los sembrados | diccionario_general |
| `LEXR-03734` | i’cue’sh pwe’sh | entre ustedes, unos con otros | diccionario_general |
| `LEXR-03735` | quiwe tujnd | polvo de la tierra | diccionario_general |
| `LEXR-03736` | squijw tuca | el calabazo (para líquidos) | diccionario_general |
| `LEXR-03737` | ya’afijmb-, ya’afimbu- | esparcir | diccionario_general |
| `LEXR-03738` | yaattewe’sh | familia, los de la casa | diccionario_general |
| `LEXR-03739` | achamée yũu- | hacer lo indebido | diccionario_general |
| `LEXR-03740` | atall we’wetste | al canto de gallo | diccionario_general |
| `LEXR-03741` | caapquivi’j-, caapquivi’ji- | hacer derretir | diccionario_general |
| `LEXR-03742` | cchu’chu’j-, cchu’chu’ju- | amamantar | diccionario_general |
| `LEXR-03743` | cjaswat | la rueca, puchicanga | diccionario_general |
| `LEXR-03744` | cpate- | deshincharse | diccionario_general |
| `LEXR-03745` | jyutcjamb | salvia (planta medicinal) | diccionario_general |
| `LEXR-03746` | paayuu- | venir acompañado a otro voluntariamente | diccionario_general |
| `LEXR-03747` | pucacje npe’sh | prima (respecto al primo) | diccionario_general |
| `LEXR-03748` | shbu | uvillo | diccionario_general |
| `LEXR-03749` | tajtstewe’sh | quinto | diccionario_general |
| `LEXR-03750` | tyaj-, tyaja-, tyaa- | poner, colocar, edificar | diccionario_general |
| `LEXR-03751` | yaate-, yaatée | purificarse | diccionario_general |
| `LEXR-03752` | ĩitse’jsa | la cocinera | diccionario_general |
| `LEXR-03753` | much yuu- | volverse sordo | diccionario_general |
| `LEXR-03754` | quĩj | que,?qué? | diccionario_general |
| `LEXR-03755` | yu’cja- | crecer (el monte) | diccionario_general |
| `LEXR-03756` | cjaasu’j-, cjaasu’ju- | cardar lana | diccionario_general |
| `LEXR-03757` | cjĩij tash | mata de caña brava | diccionario_general |
| `LEXR-03758` | cuñ-, cuñi- | 1. despulpar 2. castrar (animales) | diccionario_general |
| `LEXR-03759` | nasa | 1. indígena páez 2. gente, persona | diccionario_general |
| `LEXR-03760` | peeygãawa’j | amor, misericordia | diccionario_general |
| `LEXR-03761` | puuty yaatse- | despreciarse (mutuamente) | diccionario_general |
| `LEXR-03762` | tjẽ’j, tjẽ’cjue | 1. adulto, maduro, título de respeto a mayores; 2. jecho, en sazón (fruta, etc.) | diccionario_general |
| `LEXR-03763` | tujme | en seco (tierra firme) | diccionario_general |
| `LEXR-03764` | tyweyní | vendido | diccionario_general |
| `LEXR-03765` | tã’sh | el calcañar, talón | diccionario_general |
| `LEXR-03766` | ujnd-, undu- | quebrar, romper | diccionario_general |
| `LEXR-03767` | ñusha’j-, ñusha’ja- | endulzar | diccionario_general |
| `LEXR-03768` | ũpjsá | asaltador | diccionario_general |
| `LEXR-03769` | a’cy-, a’qui- | colgar | diccionario_general |
| `LEXR-03770` | caafirmaĩ’j-, caafirmaĩ’ji- | hacer firmar | diccionario_general |
| `LEXR-03771` | caalisa’j-, caalisa’ja- | hacer rezar | diccionario_general |
| `LEXR-03772` | caambi’j-, caambi’ji- | mandar hervir | diccionario_general |
| `LEXR-03773` | caastaja’j-, caastyaja’ja- | amansar, domesticar | diccionario_general |
| `LEXR-03774` | claa u’y | la vaca | diccionario_general |
| `LEXR-03775` | cpun bu’ch | la espuma del jabón | diccionario_general |
| `LEXR-03776` | luuch, luuchcuẽ | el niño, la niña | diccionario_general |
| `LEXR-03777` | pa’ya- | llamar | diccionario_general |
| `LEXR-03778` | pujmb-, pumbu- | botar (al viento), regar, arrojar | diccionario_general |
| `LEXR-03780` | u’ju- | andar, caminar | diccionario_general |
| `LEXR-03781` | u’sha | la señora (de raza blanca) | diccionario_general |
| `LEXR-03782` | wa’l-, wa’lu- | estar renuente, tener pereza, no tener ganas | diccionario_general |
| `LEXR-03783` | yuwe pta’sh- | avisar, traer un mensaje | diccionario_general |
| `LEXR-03784` | ãnwẽse | avispa (insecto) | diccionario_general |
| `LEXR-03785` | baytu’c-, baytu’cu- | oxidarse | diccionario_general |
| `LEXR-03786` | caambutsj-, caambutsje- | ahogarse | diccionario_general |
| `LEXR-03787` | cabilduwe’sh | miembros del cabildo, cabildantes | diccionario_general |
| `LEXR-03788` | chaquijnde-, chaquinde- | despegar, quitar coas pegada | diccionario_general |
| `LEXR-03789` | jaw | el carrizo (sirve para flauta) | diccionario_general |
| `LEXR-03790` | peena- | repetir | diccionario_general |
| `LEXR-03791` | peenana- | repetir (varias veces) | diccionario_general |
| `LEXR-03792` | twaatsec | cafeto (árbol) | diccionario_general |
| `LEXR-03793` | wala | mucho, muy | diccionario_general |
| `LEXR-03794` | wejya-, wejyáa- | ventear | diccionario_general |
| `LEXR-03795` | bite | pintado, teñido | diccionario_general |
| `LEXR-03796` | caaqui’su’j-, caaqui’su’ju- | mandar guardar dieta | diccionario_general |
| `LEXR-03797` | cjç’ng yat | el hormiguero | diccionario_general |
| `LEXR-03798` | jype’j-, jype’je- | mantener, criar | diccionario_general |
| `LEXR-03799` | lash | flojo | diccionario_general |
| `LEXR-03800` | muuwe’sh | indígena guambiano | diccionario_general |
| `LEXR-03801` | nasa spaacysa | la partera | diccionario_general |
| `LEXR-03802` | punga | el vómito | diccionario_general |
| `LEXR-03803` | quimva | cualquiera, quienquiera | diccionario_general |
| `LEXR-03804` | taúl | el ataúd | diccionario_general |
| `LEXR-03805` | tjame- | tener vergüenza | diccionario_general |
| `LEXR-03806` | tjãas-, tjãasu- | pedir | diccionario_general |
| `LEXR-03807` | caaũusutje’j-, caaũusutje’je- | hacer pensar | diccionario_general |
| `LEXR-03808` | cuse wetse | tendón de la mano | diccionario_general |
| `LEXR-03809` | mestlu | el brujo, hechicero | diccionario_general |
| `LEXR-03810` | sangistan | sacristán | diccionario_general |
| `LEXR-03811` | sllimum | carrizo de guadua | diccionario_general |
| `LEXR-03812` | tjutj | bien tejido (jigra, canasta, ruana) | diccionario_general |
| `LEXR-03813` | vyaasa | visible | diccionario_general |
| `LEXR-03814` | yaapj-, yaapjáa | taparse el rostro | diccionario_general |
| `LEXR-03815` | calsun | los calzones | diccionario_general |
| `LEXR-03816` | cuet wala | la roca | diccionario_general |
| `LEXR-03817` | cuse ũs- | dar la mano, saludar | diccionario_general |
| `LEXR-03818` | iiash-, iilashi- | aflojar, dar campo | diccionario_general |
| `LEXR-03819` | iiméj | muy sumamente (superlativo) | diccionario_general |
| `LEXR-03820` | ji’pjsa | rico | diccionario_general |
| `LEXR-03821` | pe’j-, pe’je- | llevar consigo (a otra persona) | diccionario_general |
| `LEXR-03822` | pyũuscue yaacyni | rencor, resentimiento | diccionario_general |
| `LEXR-03823` | quisu | el queso | diccionario_general |
| `LEXR-03824` | wẽeshúu- | insultar, ultrajar | diccionario_general |
| `LEXR-03825` | yuwe wecha- | mandar saludos | diccionario_general |
| `LEXR-03826` | ãwã penzh | el ají pimentón (planta, usada como condimento) | diccionario_general |
| `LEXR-03827` | ĩtyĩ fi’nze | vivir | diccionario_general |
| `LEXR-03828` | a’tya- | 1. abrirse 2. montar a horcajadas | diccionario_general |
| `LEXR-03829` | bajts | fique | diccionario_general |
| `LEXR-03830` | biite’j-, biite’je | embijarse | diccionario_general |
| `LEXR-03831` | cjũchacj-, cjũchacje- | teñir de negro | diccionario_general |
| `LEXR-03832` | cpaanicy-, cpaaniqui- | lograr llevar | diccionario_general |
| `LEXR-03833` | cu’ch-, cu’chi- | desmoronar | diccionario_general |
| `LEXR-03834` | cuetumba | el granizo | diccionario_general |
| `LEXR-03835` | cuyu’yu- | mirar (repetidas veces) | diccionario_general |
| `LEXR-03836` | cyãanz | tantos | diccionario_general |
| `LEXR-03837` | Dyusa’s yaacysa | creyente, que confía en Dios | diccionario_general |
| `LEXR-03838` | le’chle’ch | un ratico | diccionario_general |
| `LEXR-03839` | nasa we’wesa | persona que habla páez | diccionario_general |
| `LEXR-03840` | neenchi’c | el ahijado | diccionario_general |
| `LEXR-03841` | papa lul | el abuelo, bisabuelo | diccionario_general |
| `LEXR-03842` | ptjũuse- | oirse, sonar | diccionario_general |
| `LEXR-03843` | tsalli’ll | gavilán | diccionario_general |
| `LEXR-03844` | ya’ja bite | jigra de colores | diccionario_general |
| `LEXR-03845` | atyj tul | el anaco (de lana) | diccionario_general |
| `LEXR-03846` | bej atate | rojo claro | diccionario_general |
| `LEXR-03847` | caaquityi’j-, caaquityi’ji- | hacer gotear | diccionario_general |
| `LEXR-03848` | cuse much | manco, manimocho | diccionario_general |
| `LEXR-03849` | dyi’p | la cara, el rostro | diccionario_general |
| `LEXR-03850` | eca | afuera | diccionario_general |
| `LEXR-03851` | jypeecypacy-, jypeecypaqui- | poner sobre el hombro | diccionario_general |
| `LEXR-03852` | jypujts-, jypuuts- | enganchar, abrochar | diccionario_general |
| `LEXR-03853` | luasil | el alguacil | diccionario_general |
| `LEXR-03854` | nui- | maltratar, atacar a un indefenso, agredir | diccionario_general |
| `LEXR-03855` | patste | a la derecha | diccionario_general |
| `LEXR-03856` | pi’cy nasa | la gente de la minga (’invitados’) | diccionario_general |
| `LEXR-03857` | spiina’ | pegajoso | diccionario_general |
| `LEXR-03858` | yu’y-, yu’yu- | chupar caña | diccionario_general |
| `LEXR-03859` | ĩts | la nariz | diccionario_general |
| `LEXR-03860` | caaqui’pu’j-, caaqui’pu’ju- | mandar poner | diccionario_general |
| `LEXR-03861` | caascjẽu’j-, caascjẽu’ju- | 1. dejar pasar (para abajo) 2. celebrar fiesta | diccionario_general |
| `LEXR-03862` | cpjãaja’j-, cpjãaja’ja- | hacer toser | diccionario_general |
| `LEXR-03863` | cuet yuu | congelarse | diccionario_general |
| `LEXR-03864` | cyũusu’j-, cyũusu’ju- | entristecer, causar tristeza | diccionario_general |
| `LEXR-03865` | le’ya’- | ponerse derecho, recto, empinarse | diccionario_general |
| `LEXR-03866` | majũ | desde, de donde | diccionario_general |
| `LEXR-03867` | men | el último hijo, a | diccionario_general |
| `LEXR-03868` | pquiinda | guayaba (fruta) | diccionario_general |
| `LEXR-03869` | sẽ’j-, sẽ’je- | fingir | diccionario_general |
| `LEXR-03870` | tjẽytemée ũs- | estar desocupado | diccionario_general |
| `LEXR-03871` | tũu- | emborracharse | diccionario_general |
| `LEXR-03872` | zits | el huevo | diccionario_general |
| `LEXR-03873` | a’te | luna, mes | diccionario_general |
| `LEXR-03874` | beca pus | chicha fermentada | diccionario_general |
| `LEXR-03875` | calli | tejido trenzado | diccionario_general |
| `LEXR-03876` | chũpy chwa’ | sombrero de ramos | diccionario_general |
| `LEXR-03877` | cjas waca- | esquilar | diccionario_general |
| `LEXR-03878` | fiicãj-, fiicãja-, fiicãa- | extrañarse | diccionario_general |
| `LEXR-03879` | menzu- | 1. agarrar por la cola; 2. (fig) fingir ser partidario de | diccionario_general |
| `LEXR-03880` | mityj yuc | fondo de la olla | diccionario_general |
| `LEXR-03881` | paapẽjy-, paapẽyĩ- | preguntar, consultar a otro | diccionario_general |
| `LEXR-03882` | peenda-, peendáa- | ocultar, disimular | diccionario_general |
| `LEXR-03883` | qui’quin (qui’) | otra vez | diccionario_general |
| `LEXR-03884` | vyllill-, vyllillíi- | escarbar (con uña) | diccionario_general |
| `LEXR-03885` | ya’tyaj-, ya’tyaja- | cargar sobre sí mismo | diccionario_general |
| `LEXR-03886` | yeletjẽ’j | cosquilloso | diccionario_general |
| `LEXR-03887` | ĩ’pjy-, ĩ’pji- | cargar a cuestas | diccionario_general |
| `LEXR-03888` | ĩish | viejo (referiendo a hombre, o a cosa) | diccionario_general |
| `LEXR-03889` | caatsu’j-, caatsu’ju- | hacer coser | diccionario_general |
| `LEXR-03890` | lepja | colgante | diccionario_general |
| `LEXR-03891` | mum wej | puente de guadua | diccionario_general |
| `LEXR-03892` | peecytuty | echado boca abajp, postrado | diccionario_general |
| `LEXR-03893` | shaacãj u’j- | dar calambre | diccionario_general |
| `LEXR-03894` | sũj-, sũjũ-, sũu- | pensar, creer, suponer | diccionario_general |
| `LEXR-03895` | tlu (T) | el plátano (planta) | diccionario_general |
| `LEXR-03896` | vite qui’sute | en la otra semana | diccionario_general |
| `LEXR-03897` | wãwã mil, shi’ndy mil | miel de abeja | diccionario_general |
| `LEXR-03898` | yase- | 1. poner nombre; 2. bautizar | diccionario_general |
| `LEXR-03899` | yu’cypeesa | el consejero, que aconseja | diccionario_general |
| `LEXR-03900` | ẽsh ũ’we- | mascar coca | diccionario_general |
| `LEXR-03901` | cmbamb | el hombro | diccionario_general |
| `LEXR-03902` | cusíi | muy de mañana, temprano | diccionario_general |
| `LEXR-03903` | cviisha’j-, cviisha’ja- | consolar | diccionario_general |
| `LEXR-03904` | dyijca | activo, hábil | diccionario_general |
| `LEXR-03905` | paawe’wesa | persona que encarga algo | diccionario_general |
| `LEXR-03906` | pduj | suegro o suegra con el yerno | diccionario_general |
| `LEXR-03907` | puii- | pelear | diccionario_general |
| `LEXR-03908` | tjẽ’jwe’sh | mayores | diccionario_general |
| `LEXR-03909` | yujva | ni siquiera | diccionario_general |
| `LEXR-03910` | ña ej | el yucal | diccionario_general |
| `LEXR-03911` | ũch-, ũchi- | defecar, cagar (animales) | diccionario_general |
| `LEXR-03912` | fĩicunde- | quitar sombrero | diccionario_general |
| `LEXR-03913` | iipta’sh- | avisar (al mismo tiempo que hace otra cosa) | diccionario_general |
| `LEXR-03914` | iipyãani | celos | diccionario_general |
| `LEXR-03915` | pand | la viga transversal | diccionario_general |
| `LEXR-03916` | peecupy- | metamorfosear (ej. mariposa) | diccionario_general |
| `LEXR-03917` | scjẽwsa, scjẽwwa’jsa | pasajero, que pasa pronto | diccionario_general |
| `LEXR-03918` | shĩ’j | puma, león | diccionario_general |
| `LEXR-03919` | tupj | húmedo | diccionario_general |
| `LEXR-03920` | wa’ts | la arepa | diccionario_general |
| `LEXR-03921` | wata- | esperarse, ponerse espeso | diccionario_general |
| `LEXR-03922` | yat fynũ | sitio anterior de la casa | diccionario_general |
| `LEXR-03923` | yuwe ucje’j- | echar la culpa, juzgar | diccionario_general |
| `LEXR-03924` | zyaya-, zyayáa- | chasquear, rechinar | diccionario_general |

---

## Regenerar esta lista

Si actualizas `corpus_bilingue_v5.csv`, vuelve a exportar filtrando `record_type = lexico` y las columnas `id`, `nasa_yuwe`, `espanol`, `categoria`. El diccionario de la app usa ese mismo CSV vía `YuweAI/web/server.py` (`CorpusEngine`).
