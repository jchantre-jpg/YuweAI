# Imagenes lexico: nombres de archivo sugeridos

Este documento lista **cada entrada de lexico** del corpus `corpus_bilingue_v5.csv` con el **nombre de archivo** recomendado para que puedas descargar o dibujar la imagen y asociarla de forma estable (sin depender de Wikimedia Commons).

## Convencion

- Carpeta raiz sugerida: `corpus/imagenes/` (variable de entorno `AVI_LEXICO_IMAGES_DIR` en el servidor; Git LFS si pesan mucho).
- Subcarpeta **una por categoria** del CSV (mismo texto que la columna `categoria`).
- Archivo: **`{espanol_norm}`** en minusculas, espacios como `_`, sin caracteres prohibidos en Windows, extension **`.jpg`** o **`.webp`** (elige una y usala en todo el proyecto).
- La columna **Archivo sugerido** usa `espanol_norm` del corpus; si en tu Excel el lema difiere, prioriza `espanol_norm` para que coincida con el indice del sistema.
- Columna **ID**: identificador unico del CSV por si necesitas distinguir homonimos (no suele haber en la misma categoria).
- Para **regenerar** esta lista tras editar el CSV: `python scripts/gen_imagenes_lexico_md.py` (desde la carpeta `YuweAI`).
- El backend sirve primero archivos locales y luego Commons: rutas `/media/lexico/...` y convencion descrita en `corpus/imagenes/README.md`.
- Descarga automatica (Commons): `python scripts/download_lexico_images.py --max 30` (desde `YuweAI`).

## Resumen por categoria

| Categoria | Entradas (unicas por `espanol_norm`) |
|-----------|----------------------------------------|
| `alimentos` | 23 |
| `ambientales` | 25 |
| `animales` | 65 |
| `astros` | 5 |
| `colores` | 9 |
| `cuerpo_humano` | 24 |
| `diccionario_general` | 3346 |
| `frutas_verduras` | 24 |
| `herramientas` | 17 |
| `muebles_inmuebles` | 15 |
| `nombres_propios` | 20 |
| `numeros` | 58 |
| `parentescos` | 13 |
| `plantas_medicinales` | 20 |
| `saludos` | 1 |
| `utiles_hogar` | 18 |
| `vocabulario_general` | 37 |

---

## `alimentos` (23 archivos)

| Archivo sugerido | espanol (etiqueta) | nasa_yuwe | id |
|-------------------|---------------------|-----------|----|
| `alimentos/arracacha.jpg` | Arracacha | Ä's | `LEX-00260` |
| `alimentos/arveja.jpg` | Arveja | Alpes | `LEX-00258` |
| `alimentos/caigua.jpg` | Caigua | Kbiiçx | `LEX-00266` |
| `alimentos/carne.jpg` | Carne | Çxiçx | `LEX-00263` |
| `alimentos/cebolla.jpg` | Cebolla | Spulxa | `LEX-00276` |
| `alimentos/chachafruto.jpg` | Chachafruto | Uswal | `LEX-00280` |
| `alimentos/chicha.jpg` | Chicha | Beka | `LEX-00261` |
| `alimentos/choclo.jpg` | Choclo | Çuth | `LEX-00262` |
| `alimentos/cidra.jpg` | Cidra | Klayuta | `LEX-00268` |
| `alimentos/cilantro.jpg` | Cilantro | Me'su | `LEX-00272` |
| `alimentos/coles.jpg` | Coles | Kulxis | `LEX-00269` |
| `alimentos/frijol.jpg` | Frijol | Us | `LEX-00279` |
| `alimentos/maiz.jpg` | Maiz | Kutxh | `LEX-00271` |
| `alimentos/mani.jpg` | Mani | Txit | `LEX-00278` |
| `alimentos/mote.jpg` | Mote | Muçi | `LEX-00273` |
| `alimentos/ollucos.jpg` | Ollucos | Sxwil | `LEX-00277` |
| `alimentos/papa.jpg` | Papa | Ka'ka | `LEX-00265` |
| `alimentos/platano.jpg` | Platano | Plad | `LEX-00275` |
| `alimentos/remolacha.jpg` | Remolacha | Ee phewusa | `LEX-00264` |
| `alimentos/sancocho.jpg` | Sancocho | Kusxa | `LEX-00270` |
| `alimentos/sopa.jpg` | Sopa | Khasx | `LEX-00267` |
| `alimentos/yuca.jpg` | Yuca | Nxa | `LEX-00274` |
| `alimentos/zapallo.jpg` | Zapallo | Ape | `LEX-00259` |
## `ambientales` (25 archivos)

| Archivo sugerido | espanol (etiqueta) | nasa_yuwe | id |
|-------------------|---------------------|-----------|----|
| `ambientales/agua.jpg` | Agua | Yu' | `LEX-00340` |
| `ambientales/arbol_caucho.jpg` | Arbol caucho | Açxha | `LEX-00316` |
| `ambientales/arbol_de_cera.jpg` | Arbol de cera | Kwetufx | `LEX-00321` |
| `ambientales/arcoiris.jpg` | Arcoiris | Kxthüus | `LEX-00330` |
| `ambientales/arena.jpg` | Arena | Muse | `LEX-00331` |
| `ambientales/arrayan.jpg` | Arrayan | Çhï'te | `LEX-00318` |
| `ambientales/cerro.jpg` | Cerro | Thä' | `LEX-00336` |
| `ambientales/chonta.jpg` | Chonta | Çxped | `LEX-00320` |
| `ambientales/chusque.jpg` | Chusque | Çü'ph | `LEX-00319` |
| `ambientales/derrumbe.jpg` | Derrumbe | Ejx | `LEX-00327` |
| `ambientales/flor.jpg` | Flor | Txite | `LEX-00337` |
| `ambientales/fuego.jpg` | Fuego | Ipx | `LEX-00328` |
| `ambientales/lluvia.jpg` | Lluvia | Nus | `LEX-00332` |
| `ambientales/metal_o_hierro.jpg` | Metal o hierro | Çaam | `LEX-00323` |
| `ambientales/nevado.jpg` | Nevado | Nxaz | `LEX-00333` |
| `ambientales/nube.jpg` | Nube | Täph | `LEX-00334` |
| `ambientales/paja.jpg` | Paja | Çhïçh | `LEX-00324` |
| `ambientales/piedra.jpg` | Piedra | Kweth | `LEX-00329` |
| `ambientales/planta.jpg` | Planta | Tasx | `LEX-00335` |
| `ambientales/rama.jpg` | Rama | Çxä'px | `LEX-00325` |
| `ambientales/roble.jpg` | Roble | Pizx | `LEX-00322` |
| `ambientales/tierra_organica.jpg` | Tierra organica | Txiwe | `LEX-00338` |
| `ambientales/trueno.jpg` | Trueno | Ëekhthe'j | `LEX-00326` |
| `ambientales/viento.jpg` | Viento | Wejxa | `LEX-00339` |
| `ambientales/yarumo.jpg` | Yarumo | Buçe | `LEX-00317` |
## `animales` (65 archivos)

| Archivo sugerido | espanol (etiqueta) | nasa_yuwe | id |
|-------------------|---------------------|-----------|----|
| `animales/aguila.jpg` | Aguila | Uh | `LEX-00171` |
| `animales/aguti_o_guatuza.jpg` | aguti o guatuza | yu’cj cuchi | `LEX-00075` |
| `animales/alacran.jpg` | Alacran | Us miç | `LEX-00138` |
| `animales/arana.jpg` | Arana | Tupa | `LEX-00170` |
| `animales/ardilla.jpg` | Ardilla | Sxuma | `LEX-00168` |
| `animales/armadillo.jpg` | Armadillo | Sxita | `LEX-00167` |
| `animales/avispa.jpg` | Avispa | Mezuw | `LEX-00131` |
| `animales/babosa.jpg` | Babosa | Sxape | `LEX-00136` |
| `animales/borugo.jpg` | Borugo | Lazx | `LEX-00129` |
| `animales/buho.jpg` | Buho | Kupe | `LEX-00159` |
| `animales/caballo.jpg` | Caballo | Jiba | `LEX-00153` |
| `animales/cabra.jpg` | Cabra | Kapla | `LEX-00155` |
| `animales/cangrejo.jpg` | Cangrejo | Wäka | `LEX-00139` |
| `animales/carpintero.jpg` | Carpintero | Anza | `LEX-00120` |
| `animales/cerdo.jpg` | cerdo | cuchi | `LEX-00068` |
| `animales/chamon.jpg` | Chamon | Tüç | `LEX-00137` |
| `animales/chicharra.jpg` | Chicharra | Yawee | `LEX-00141` |
| `animales/cienpies.jpg` | Cienpies | Supil | `LEX-00135` |
| `animales/codorniz.jpg` | Codorniz | Fxi'l | `LEX-00151` |
| `animales/colibri.jpg` | Colibri | E'ç | `LEX-00149` |
| `animales/comadreja.jpg` | Comadreja | Wënxinx | `LEX-00140` |
| `animales/condor.jpg` | Condor | Kdul | `LEX-00156` |
| `animales/conejo.jpg` | Conejo | Kähpx | `LEX-00154` |
| `animales/cucaracha.jpg` | Cucaracha | Sa'te | `LEX-00132` |
| `animales/cusumbo.jpg` | Cusumbo | Kaça | `LEX-00125` |
| `animales/cuy.jpg` | Cuy | Fxiçh | `LEX-00152` |
| `animales/gallina.jpg` | Gallina | Atalx | `LEX-00144` |
| `animales/gallinazo.jpg` | Gallinazo | Meewëjx | `LEX-00130` |
| `animales/gallo.jpg` | Gallo | Atalx pihç | `LEX-00145` |
| `animales/garrapata.jpg` | Garrapata | Kalpaç | `LEX-00126` |
| `animales/gato.jpg` | Gato | Misx | `LEX-00162` |
| `animales/gorrion.jpg` | Gorrion | Çuh | `LEX-00121` |
| `animales/guacharaca.jpg` | Guacharaca | Fxizx | `LEX-00123` |
| `animales/guatin.jpg` | Guatin | Nxu'px | `LEX-00163` |
| `animales/gusano.jpg` | Gusano | Ukh | `LEX-00172` |
| `animales/hocico_del_puerco.jpg` | hocico del puerco | cuchi ĩts | `LEX-00070` |
| `animales/horqueta_para_puerco.jpg` | horqueta para puerco | cuchi tel | `LEX-00071` |
| `animales/lagartija.jpg` | Lagartija | Klaweçx | `LEX-00128` |
| `animales/leon.jpg` | Leon | Lxuun | `LEX-00160` |
| `animales/libelula.jpg` | Libelula | Sikhwet | `LEX-00134` |
| `animales/lobo.jpg` | Lobo | Alum | `LEX-00142` |
| `animales/lombriz.jpg` | Lombriz | Sxa'wë | `LEX-00166` |
| `animales/loro.jpg` | Loro | Welx | `LEX-00175` |
| `animales/mariquita.jpg` | Mariquita | Kawa | `LEX-00127` |
| `animales/mono.jpg` | Mono | Miku | `LEX-00161` |
| `animales/murcielago.jpg` | Murcielago | Kihçe | `LEX-00157` |
| `animales/oveja.jpg` | Oveja | Pisxaa | `LEX-00165` |
| `animales/paloma.jpg` | Paloma | Tub | `LEX-00169` |
| `animales/pato.jpg` | Pato | Ïç waç | `LEX-00124` |
| `animales/pecari.jpg` | pecari | quiwe cuchi | `LEX-00073` |
| `animales/pez.jpg` | Pez | Wez | `LEX-00176` |
| `animales/pezuña_del_puerco.jpg` | pezuña del puerco | cuchi vyllill | `LEX-00072` |
| `animales/piojo.jpg` | Piojo | Ës | `LEX-00150` |
| `animales/puerco.jpg` | puerco | cuchi | `LEX-00069` |
| `animales/pulga.jpg` | Pulga | Pä'pa | `LEX-00164` |
| `animales/rana.jpg` | Rana | Çuz | `LEX-00122` |
| `animales/raton.jpg` | Raton | Uhze | `LEX-00173` |
| `animales/saino.jpg` | saino | yu’cj cuchi | `LEX-00074` |
| `animales/sapo.jpg` | Sapo | Sap | `LEX-00133` |
| `animales/serpiente.jpg` | Serpiente | Ul | `LEX-00174` |
| `animales/tigre.jpg` | Tigre | Çiklxi | `LEX-00146` |
| `animales/vaca.jpg` | Vaca | Klaa u'y | `LEX-00158` |
| `animales/venado.jpg` | Venado | Çxavx | `LEX-00147` |
| `animales/zancudo.jpg` | Zancudo | Äph | `LEX-00143` |
| `animales/zarigueya.jpg` | Zarigueya | Çxuçxa | `LEX-00148` |
## `astros` (5 archivos)

| Archivo sugerido | espanol (etiqueta) | nasa_yuwe | id |
|-------------------|---------------------|-----------|----|
| `astros/cometa.jpg` | Cometa | Ëewë | `LEX-00343` |
| `astros/estrella.jpg` | Estrella | A' | `LEX-00341` |
| `astros/luna.jpg` | Luna | A'te | `LEX-00342` |
| `astros/planeta_tierra.jpg` | Planeta Tierra | Uma Txiwe | `LEX-00345` |
| `astros/sol.jpg` | Sol | Sek | `LEX-00344` |
## `colores` (9 archivos)

| Archivo sugerido | espanol (etiqueta) | nasa_yuwe | id |
|-------------------|---------------------|-----------|----|
| `colores/amarillo.jpg` | Amarillo | Tçxkiy | `LEX-00067` |
| `colores/anaranjado.jpg` | Anaranjado | Behbeh lem | `LEX-00059` |
| `colores/azul.jpg` | Azul | Çemçem | `LEX-00061` |
| `colores/blanco.jpg` | Blanco | Çxihme | `LEX-00064` |
| `colores/gris.jpg` | Gris | Khuuç | `LEX-00066` |
| `colores/negro.jpg` | Negro | Khüçxh | `LEX-00065` |
| `colores/rojo.jpg` | Rojo | Beh | `LEX-00062` |
| `colores/rojo_encendido.jpg` | Rojo encendido | Behbeh | `LEX-00063` |
| `colores/verde.jpg` | Verde | Çeenx | `LEX-00060` |
## `cuerpo_humano` (24 archivos)

| Archivo sugerido | espanol (etiqueta) | nasa_yuwe | id |
|-------------------|---------------------|-----------|----|
| `cuerpo_humano/barriga.jpg` | Barriga | Tuç | `LEX-00207` |
| `cuerpo_humano/boca.jpg` | Boca | Yuwe | `LEX-00211` |
| `cuerpo_humano/brazo.jpg` | Brazo | Ku'ta | `LEX-00200` |
| `cuerpo_humano/cabello.jpg` | Cabello | Zkhas | `LEX-00213` |
| `cuerpo_humano/cabeza.jpg` | Cabeza | Çukh | `LEX-00192` |
| `cuerpo_humano/cerebro.jpg` | Cerebro | Pe'pe | `LEX-00202` |
| `cuerpo_humano/corazon.jpg` | Corazon | Üus | `LEX-00209` |
| `cuerpo_humano/cuello.jpg` | Cuello | Çikh | `LEX-00191` |
| `cuerpo_humano/diente.jpg` | Diente | Txi'th | `LEX-00208` |
| `cuerpo_humano/garganta.jpg` | Garganta | Pëçh | `LEX-00201` |
| `cuerpo_humano/hombro.jpg` | Hombro | Babh | `LEX-00190` |
| `cuerpo_humano/hueso.jpg` | Hueso | Zi't | `LEX-00212` |
| `cuerpo_humano/lengua.jpg` | Lengua | Thune | `LEX-00205` |
| `cuerpo_humano/mano.jpg` | Mano | Kuse | `LEX-00199` |
| `cuerpo_humano/nariz.jpg` | Nariz | Ïçh | `LEX-00196` |
| `cuerpo_humano/ojo.jpg` | Ojo | Yafx | `LEX-00210` |
| `cuerpo_humano/ombligo.jpg` | Ombligo | Sxab | `LEX-00203` |
| `cuerpo_humano/oreja.jpg` | Oreja | Thü'wë | `LEX-00206` |
| `cuerpo_humano/pene.jpg` | Pene | Çxul | `LEX-00195` |
| `cuerpo_humano/pie.jpg` | Pie | Çxida | `LEX-00193` |
| `cuerpo_humano/pierna.jpg` | Pierna | Ji'be | `LEX-00198` |
| `cuerpo_humano/rodilla.jpg` | Rodilla | Ikhwëth | `LEX-00197` |
| `cuerpo_humano/seno.jpg` | Seno | Çxu'çx | `LEX-00194` |
| `cuerpo_humano/vagina.jpg` | Vagina | Thamee | `LEX-00204` |
## `diccionario_general` (3346 archivos)

| Archivo sugerido | espanol (etiqueta) | nasa_yuwe | id |
|-------------------|---------------------|-----------|----|
| `diccionario_general/!_hola!_(saludando_a_un_hombre).jpg` | !Hola! (saludando a un hombre) | ewcha | `LEXR-01379` |
| `diccionario_general/!_hola!_(saludando_a_una_mujer_o_a_varias_personas).jpg` | !Hola! (saludando a una mujer o a varias personas) | ewchacue | `LEXR-01659` |
| `diccionario_general/(culebra_no_venenosa).jpg` | (culebra no venenosa) | ul watycue | `LEXR-02682` |
| `diccionario_general/(especie_de_bejuco).jpg` | (especie de bejuco) | yaj chijme | `LEXR-01180` |
| `diccionario_general/(especie_de_madera,_que_usan_para_labrar_cucharas).jpg` | (especie de madera, que usan para labrar cucharas) | fytũu ẽsh | `LEXR-02042` |
| `diccionario_general/(especie_de_planta_medicinal).jpg` | (especie de planta medicinal) | fytũu pitscue | `LEXR-00412` |
| `diccionario_general/(especie_de_árbol).jpg` | (especie de árbol) | chictu’j | `LEXR-00398` |
| `diccionario_general/(planta_medicinal).jpg` | (planta medicinal) | shũu yu’tscavy | `LEXR-00732` |
| `diccionario_general/(planta_silvestre,_que_se_usa_para_jabón).jpg` | (planta silvestre, que se usa para jabón) | sba’cue | `LEXR-00826` |
| `diccionario_general/(planta).jpg` | (planta) | ze’nze | `LEXR-03307` |
| `diccionario_general/(planta,_que_da_sabor_a_la_comida).jpg` | (planta, que da sabor a la comida) | shumatyjã’ | `LEXR-01555` |
| `diccionario_general/(yerba_que_enloquece).jpg` | (yerba que enloquece) | jẽp | `LEXR-03022` |
| `diccionario_general/1._abrirse_2._montar_a_horcajadas.jpg` | 1. abrirse 2. montar a horcajadas | a’tya- | `LEXR-03828` |
| `diccionario_general/1._adelante;_2._primero.jpg` | 1. adelante; 2. primero | yats- | `LEXR-02191` |
| `diccionario_general/1._adelgazar;_2._rematar,_acabar_un_trabajo.jpg` | 1. adelgazar; 2. rematar, acabar un trabajo | peetsu’j-, peetsu’ju- | `LEXR-02707` |
| `diccionario_general/1._adormecer,_causar_sueño_2._acostar.jpg` | 1. adormecer, causar sueño 2. acostar | cdeeje’j-, cdeeje’je- | `LEXR-00395` |
| `diccionario_general/1._adulto,_maduro,_título_de_respeto_a_mayores;_2._jecho,_en_sazón_(fruta,_etc._).jpg` | 1. adulto, maduro, título de respeto a mayores; 2. jecho, en sazón (fruta, etc.) | tjẽ’j, tjẽ’cjue | `LEXR-03762` |
| `diccionario_general/1._agacharse;_2._prender_candela.jpg` | 1. agacharse; 2. prender candela | quityáa- | `LEXR-03297` |
| `diccionario_general/1._agarrar_por_la_cola;_2._(fig)_fingir_ser_partidario_de.jpg` | 1. agarrar por la cola; 2. (fig) fingir ser partidario de | menzu- | `LEXR-03879` |
| `diccionario_general/1._alimentar;_2._hacer_un_flavor.jpg` | 1. alimentar; 2. hacer un flavor | sã’jĩ- | `LEXR-03524` |
| `diccionario_general/1._alzar,_levantar,_quitar;_2._edificar_casa.jpg` | 1. alzar, levantar, quitar; 2. edificar casa | quiis-, quiisu- | `LEXR-02994` |
| `diccionario_general/1._así_2._como,_parecido.jpg` | 1. así 2. como, parecido | na’wẽ, na’wẽy | `LEXR-01797` |
| `diccionario_general/1._bajar_algo_(de_arriba_para_abajo);_2._desensillar.jpg` | 1. bajar algo (de arriba para abajo); 2. desensillar | spajcy-, spaaqui-, spaacy- | `LEXR-02066` |
| `diccionario_general/1._blandir_(repetidas_veces);_2._recoger_con_cuchara).jpg` | 1. blandir (repetidas veces); 2. recoger con cuchara) | vyandu’ndu- | `LEXR-02867` |
| `diccionario_general/1._botar_(repetidas_veces);_2._apedrear.jpg` | 1. botar (repetidas veces); 2. apedrear | wãatãtãj- | `LEXR-01100` |
| `diccionario_general/1._caer_encima_de;_2._ser_vencido.jpg` | 1. caer encima de; 2. ser vencido | ya’cach- | `LEXR-02731` |
| `diccionario_general/1._cazar_animales;_2._ladrar.jpg` | 1. cazar animales; 2. ladrar | vijcy- viqui- | `LEXR-01948` |
| `diccionario_general/1._cepillar,_labrar_madera;_2._rebanar.jpg` | 1. cepillar, labrar madera; 2. rebanar | ũ’tsj-, ũ’tsju- | `LEXR-03580` |
| `diccionario_general/1._cercar;_2._cerrar_los_ojos.jpg` | 1. cercar; 2. cerrar los ojos | upj-, upjáa- | `LEXR-03702` |
| `diccionario_general/1._chupar_2._absorbar_3._fumar_(tobaco).jpg` | 1. chupar 2. absorbar 3. fumar (tobaco) | chanzh-, chanzháa- | `LEXR-03727` |
| `diccionario_general/1._comer;_2._mascar_coca,_mambear;_3._picar.jpg` | 1. comer; 2. mascar coca, mambear; 3. picar | ũ’-, ũwe- | `LEXR-01435` |
| `diccionario_general/1._contagiar,_contaminar_2._perjudicar.jpg` | 1. contagiar, contaminar 2. perjudicar | niipeetje-, niipeetjeje- | `LEXR-02540` |
| `diccionario_general/1._contestar_2._comprometerse.jpg` | 1. contestar 2. comprometerse | pas-, pasu- | `LEXR-01395` |
| `diccionario_general/1._conversar,_platicar,_charlar_2._orar.jpg` | 1. conversar, platicar, charlar 2. orar | puuty we’we- | `LEXR-02933` |
| `diccionario_general/1._cosechar,_cortar_café,_fríjol;_2._desplumar.jpg` | 1. cosechar, cortar café, fríjol; 2. desplumar | ujnde-, unde- | `LEXR-03394` |
| `diccionario_general/1._cosechar,_segar,_cortar;_2._esquilar.jpg` | 1. cosechar, segar, cortar; 2. esquilar | waca- | `LEXR-01694` |
| `diccionario_general/1._crecer_(largo);_2._prolongarse,_alargarse.jpg` | 1. crecer (largo); 2. prolongarse, alargarse | jyu’ja- | `LEXR-01295` |
| `diccionario_general/1._cruzarse_en_el_camino,_entrecruzarse;_2._quitar_tiempo,_interrupir.jpg` | 1. cruzarse en el camino, entrecruzarse; 2. quitar tiempo, interrupir | ptyijnde-, ptyinde- | `LEXR-00907` |
| `diccionario_general/1._dar_sabor,_condimentar;_2._penetrar_(ej._humo).jpg` | 1. dar sabor, condimentar; 2. penetrar (ej. humo) | peetje- | `LEXR-00903` |
| `diccionario_general/1._dar_sombra_2._servir_como_padrinos_en_las_bodas.jpg` | 1. dar sombra 2. servir como padrinos en las bodas | pu’nze’j-, pu’nze’je- | `LEXR-00987` |
| `diccionario_general/1._dar,_conceder;_2._saludar,_dar_la_mano.jpg` | 1. dar, conceder; 2. saludar, dar la mano | ũs-, ũsu- | `LEXR-00941` |
| `diccionario_general/1._dejar_2._designar_3._derrotar.jpg` | 1. dejar 2. designar 3. derrotar | nvijt-, nviitu- | `LEXR-03204` |
| `diccionario_general/1._dejar_pasar_(para_abajo)_2._celebrar_fiesta.jpg` | 1. dejar pasar (para abajo) 2. celebrar fiesta | caascjẽu’j-, caascjẽu’ju- | `LEXR-03861` |
| `diccionario_general/1._delgado;_2._tono_muy_agudo_(música).jpg` | 1. delgado; 2.tono muy agudo (música) | zunz, zunzcuẽ | `LEXR-01348` |
| `diccionario_general/1._derrumbar_2._arar,_sacar_paladas.jpg` | 1. derrumbar 2. arar, sacar paladas | a’mbande- | `LEXR-01357` |
| `diccionario_general/1._derrumbarse;_2._mudar_pluma.jpg` | 1. derrumbarse; 2. mudar pluma | umbu- | `LEXR-02136` |
| `diccionario_general/1._despedazar_2._dar_cambio_(dinero).jpg` | 1. despedazar 2. dar cambio (dinero) | mushi’j-, muushi’ji- | `LEXR-01739` |
| `diccionario_general/1._despulpar_2._castrar_(animales).jpg` | 1. despulpar 2. castrar (animales) | cuñ-, cuñi- | `LEXR-03758` |
| `diccionario_general/1._desyerbar,_limpiar_maleza;_2._desnudar,_desvestir.jpg` | 1. desyerbar, limpiar maleza; 2. desnudar, desvestir | sũupi’j-, sũupi’ji- | `LEXR-00644` |
| `diccionario_general/1._desyerbar,_limpiar_maleza;_2._juguetear.jpg` | 1. desyerbar, limpiar maleza; 2. juguetear | vis-, visu- | `LEXR-01097` |
| `diccionario_general/1._desyerbar;_2._desvestir.jpg` | 1. desyerbar; 2. desvestir | tũupi’j-, tũupi’ji- | `LEXR-01334` |
| `diccionario_general/1._echar_ramas;_2._tener_vástago.jpg` | 1. echar ramas; 2. tener vástago | shã’py-, shã’pi- | `LEXR-03320` |
| `diccionario_general/1._el_agua;_2._líquido.jpg` | 1. el agua; 2. líquido | yu’ | `LEXR-03370` |
| `diccionario_general/1._el_cuero,_la_piel_2._la_cáscara,_corteza_de_árbol.jpg` | 1. el cuero, la piel 2. la cáscara, corteza de árbol | cja’ty | `LEXR-02807` |
| `diccionario_general/1._el_gato_(mamífero);_2._el_espíritu_guardián_(vitywe'sh).jpg` | 1. el gato (mamífero); 2. el espíritu guardián (vitywe’sh) | mish | `LEXR-02537` |
| `diccionario_general/1._el_hombro,_brazo_2._la_brazada_(medida.jpg` | 1. el hombro, brazo 2. la brazada (medida | cu’ta | `LEXR-02951` |
| `diccionario_general/1._enderezar,_alinear_2._rectificar.jpg` | 1. enderezar, alinear 2. rectificar | cu’le’j-, cu’le’je- | `LEXR-02883` |
| `diccionario_general/1._endurecer_2._cuajar_(leche).jpg` | 1. endurecer 2. cuajar (leche) | cweeji’j-, cweeji’ji- | `LEXR-03194` |
| `diccionario_general/1._enterrar,_sepular;_2._hundirse.jpg` | 1. enterrar, sepular; 2. hundirse | penda-, pendáa- | `LEXR-01156` |
| `diccionario_general/1._escarmenar_lana,_cardar;_2._cosechar_maíz.jpg` | 1. escarmenar lana, cardar; 2. cosechar maíz | shunde- | `LEXR-02230` |
| `diccionario_general/1._estar_agradecido,_agradecer;_2._saludar,_despedir,_besar.jpg` | 1. estar agradecido, agradecer; 2. saludar, despedir, besar | wecha-, wecháa- | `LEXR-02727` |
| `diccionario_general/1._estar_enfermo;_2._morir,_fallecer.jpg` | 1. estar enfermo; 2. morir, fallecer | uu- | `LEXR-02455` |
| `diccionario_general/1._frotar,_fregar,_ungir,_untar;_2._afilar_(machete,_hacha);_3._restregar_trigo_(con_un_mazo).jpg` | 1. frotar, fregar, ungir, untar; 2. afilar (machete, hacha); 3. restregar trigo (con un mazo) | shũsh-, shũshúu- | `LEXR-01819` |
| `diccionario_general/1._gemir,_gritar_(de_dolor)_2._mugir_(vaca);_3._chillar;_4._relinchar_(caballo),_5._cacarear_(gallina),_6._maullar_(gato).jpg` | 1. gemir, gritar (de dolor) 2. mugir (vaca); 3. chillar; 4. relinchar (caballo), 5. cacarear (gallina), 6. maullar (gato) | pembe-, pembée- | `LEXR-00629` |
| `diccionario_general/1._golpear;_2._derribar,_tumbar;_3._trillar.jpg` | 1. golpear; 2. derribar, tumbar; 3. trillar | ujca-, uca- | `LEXR-01946` |
| `diccionario_general/1._grueso,_robusto;_2._nota_muy_baja_(música).jpg` | 1. grueso, robusto; 2. nota muy baja (música) | pepy | `LEXR-02121` |
| `diccionario_general/1._guardar_dieta;_2._guardar_día_de_fiesta.jpg` | 1. guardar dieta; 2. guardar día de fiesta | qui’s-, qui’su- | `LEXR-03058` |
| `diccionario_general/1._hacer_desyerbar_2._hacer_entretenerse.jpg` | 1. hacer desyerbar 2. hacer entretenerse | cviisu’j-, cviisu’ju- | `LEXR-03226` |
| `diccionario_general/1._hacer_equivocar,_hacer_desviar_2._engañar.jpg` | 1. hacer equivocar, hacer desviar 2. engañar | caypumba´j-, caypumba´ja- | `LEXR-02912` |
| `diccionario_general/1._hacer_sonar_(un_instrumento)_2._crujir_los_dientes_3._alborotar.jpg` | 1. hacer sonar (un instrumento) 2. crujir los dientes 3. alborotar | csuusu’j-, csuusu’ju- | `LEXR-00401` |
| `diccionario_general/1._hacer;_2._designar;_3._redimir.jpg` | 1. hacer; 2. designar; 3. redimir | vit-, vitu- | `LEXR-01562` |
| `diccionario_general/1._inclinar_la_cabeza;_2._quedar_humillado.jpg` | 1. inclinar la cabeza; 2. quedar humillado | quitje- | `LEXR-00728` |
| `diccionario_general/1._indígena_páez_2._gente,_persona.jpg` | 1. indígena páez 2. gente, persona | nasa | `LEXR-03759` |
| `diccionario_general/1._intercambiar;_2._transformar.jpg` | 1. Intercambiar; 2. transformar | yu’ptjej-, yu’ptjeje- | `LEXR-03653` |
| `diccionario_general/1._la_boca;_2._el_idioma;_3._el_saludo;_4._asunto,_noticia,_razón.jpg` | 1. la boca; 2. el idioma; 3. el saludo; 4. asunto, noticia, razón | yuwe | `LEXR-02350` |
| `diccionario_general/1._la_comadreja_(mamífero)_2._ser_sobrenatural_(mohán_o_moján).jpg` | 1. la comadreja (mamífero) 2. ser sobrenatural (mohán o moján) | cumby | `LEXR-01983` |
| `diccionario_general/1._la_espuma_2._planta_medicinal.jpg` | 1. la espuma 2. planta medicinal | bu’ch | `LEXR-02356` |
| `diccionario_general/1._la_madeja_de_lana_escarmenada_2._la_pluma.jpg` | 1. la madeja de lana escarmenada 2. la pluma | cjas pjapj | `LEXR-01781` |
| `diccionario_general/1._la_nalga,_asentaderas;_2._fondo.jpg` | 1. la nalga, asentaderas; 2. fondo | yuc | `LEXR-02560` |
| `diccionario_general/1._los_antepasados;_2._oficiales_salientes.jpg` | 1. los antepasados; 2. oficiales salientes | yatsgawe’sh | `LEXR-03688` |
| `diccionario_general/1._madurar;_2._envejecerse.jpg` | 1. madurar; 2. envejecerse | tjẽ’j-, tjẽ’je- | `LEXR-03701` |
| `diccionario_general/1._mandar_hacer_2._hacer_celebrar_misa.jpg` | 1. mandar hacer 2. hacer celebrar misa | cviitu’j-, cviitu’ju- | `LEXR-02884` |
| `diccionario_general/1._moder_(perro,_culebra);_2._picar.jpg` | 1. moder (perro, culebra); 2. picar | wa’cy-, wa’qui- | `LEXR-03668` |
| `diccionario_general/1._moler,_exprimir_2._ordeñar_vaca.jpg` | 1. moler, exprimir 2. ordeñar vaca | cu’s-, cu’su- | `LEXR-02472` |
| `diccionario_general/1._nacer;_2._reventar_(pollito).jpg` | 1. nacer; 2. reventar (pollito) | upy-, upyji- | `LEXR-02076` |
| `diccionario_general/1._pegarse_a_2._asociarse_con.jpg` | 1. pegarse a 2. asociarse con | nuucy-, nuuqui- | `LEXR-00429` |
| `diccionario_general/1._pensar,_acordarse;_2._confiar_en;_3._dudar,_vacilar;_4._sentirse_triste,_pensativo.jpg` | 1. pensar, acordarse; 2. confiar en; 3. dudar, vacilar; 4. sentirse triste, pensativo | yajcy-, yaaqui-, yaacy- | `LEXR-00749` |
| `diccionario_general/1._poner_atravesado_(palo)_2._cruzar_las_piernas.jpg` | 1. poner atravesado (palo) 2. cruzar las piernas | pchatj-, pchatje- | `LEXR-02052` |
| `diccionario_general/1._poner_en_la_cepo_2._poner_horqueta_(al_puerco).jpg` | 1. poner en la cepo 2. poner horqueta (al puerco) | teelu’j-, teelu’ju- | `LEXR-00924` |
| `diccionario_general/1._poner_nombre;_2._bautizar.jpg` | 1. poner nombre; 2. bautizar | yase- | `LEXR-03898` |
| `diccionario_general/1._poner,_colocar_encima_de_2._averiguar,_investigar.jpg` | 1. poner, colocar encima de 2. averiguar, investigar | atyáj-, atyája- | `LEXR-03330` |
| `diccionario_general/1._poner,_inyectar;_2._nombrar_en_un_puesto.jpg` | 1. poner, inyectar; 2. nombrar en un puesto | qui’p-, qui’pu- | `LEXR-03521` |
| `diccionario_general/1._prometer_2._enterarse.jpg` | 1. prometer 2. enterarse | neeyũu- | `LEXR-01463` |
| `diccionario_general/1._quedarse_2._ser_salvo_3._ser_condenado.jpg` | 1. quedarse 2. ser salvo 3. ser condenado | neeyũu- (neeñuu-) | `LEXR-01065` |
| `diccionario_general/1._rasgar,_romper;_2._changuar,_separar_hebras_(de_cabuya_o_bejuco).jpg` | 1. rasgar, romper; 2. changuar, separar hebras (de cabuya o bejuco) | stende- | `LEXR-03321` |
| `diccionario_general/1._repartir_comida_(entre_varias_personas)_2._meter_caña_(en_la_trapiche).jpg` | 1. repartir comida (entre varias personas) 2. meter caña (en la trapiche) | puutsuts-, puutsutsu- | `LEXR-01312` |
| `diccionario_general/1._sacar_2._traducir.jpg` | 1. sacar 2. traducir | cutyi’j-, cutyi’ji- | `LEXR-03078` |
| `diccionario_general/1._salir_2._nacer_3._resultar.jpg` | 1. salir 2. nacer 3. resultar | case´j-, caseje-(cãsej-) | `LEXR-00953` |
| `diccionario_general/1._saltar_(repetidas_veces);_2._palpitar,_latir.jpg` | 1. saltar (repetidas veces); 2. palpitar, latir | ũpjũupj-, ũpjũupju- | `LEXR-01353` |
| `diccionario_general/1._secarse;_2._agotarse.jpg` | 1. secarse; 2. agotarse | ujndy-, undyi- | `LEXR-01763` |
| `diccionario_general/1._sentarse_2._posar_(ave)_3._aterrizar_(avión).jpg` | 1. sentarse 2. posar (ave) 3. aterrizar (avión) | cach-, cachjí- | `LEXR-02880` |
| `diccionario_general/1._tejer_(jigra,_ruana);_2._techar,_empajar_una_casa.jpg` | 1. tejer (jigra, ruana); 2. techar, empajar una casa | um-, umúu- | `LEXR-01422` |
| `diccionario_general/1._trabar,_eredar_2._acornear.jpg` | 1. trabar, eredar 2. acornear | atsju- | `LEXR-03554` |
| `diccionario_general/1._traer,_llevar;_2._vestirse.jpg` | 1. traer, llevar; 2. vestirse | jyũu- | `LEXR-03235` |
| `diccionario_general/1._untar_2._curtir_(cuero)_3._desfibrar_cabuya.jpg` | 1. untar 2. curtir (cuero) 3. desfibrar cabuya | cu’nd-, cu’ndu- | `LEXR-02571` |
| `diccionario_general/1._uña_(de_persona);_2._dedo_(medida,_anchura_de_un_dedo);_3._garra_(de_ave);_4._casco_(de_caballo);_5._pezuña_(de_animal).jpg` | 1. uña (de persona); 2. dedo (medida, anchura de un dedo); 3. garra (de ave); 4. casco (de caballo); 5. pezuña (de animal) | vyllill | `LEXR-01011` |
| `diccionario_general/1._ver,_encontrar;_2._conseguir,_hallar.jpg` | 1. ver, encontrar; 2. conseguir, hallar | uy-, uyúu- | `LEXR-02942` |
| `diccionario_general/1._vástago,_renuevo_de_árbol_o_planta;_2._vástago,_persona_descendiente_de_otra.jpg` | 1. vástago, renuevo de árbol o planta; 2. vástago, persona descendiente de otra | shã’py | `LEXR-01084` |
| `diccionario_general/1._zafar,_quitar_2._desenfrenar.jpg` | 1. zafar, quitar 2. desenfrenar | pajnde-, pande- | `LEXR-01542` |
| `diccionario_general/por_qué.jpg` | ?por qué? | quĩj yuupa’ga | `LEXR-03343` |
| `diccionario_general/a_favor_de.jpg` | a favor de | ju’ngu | `LEXR-03139` |
| `diccionario_general/a_la_derecha.jpg` | a la derecha | patste | `LEXR-03855` |
| `diccionario_general/a_la_orilla_de.jpg` | a la orilla de | putssu | `LEXR-01158` |
| `diccionario_general/a_orillas_de.jpg` | a orillas de | pucasu | `LEXR-02714` |
| `diccionario_general/a_tocar_tambor.jpg` | a tocar tambor | cwẽeta tujcaya’ | `LEXR-02783` |
| `diccionario_general/a_través_de,_a_lo_largo_de.jpg` | a través de, a lo largo de | jypeesa’j | `LEXR-02315` |
| `diccionario_general/a_un_lado_de.jpg` | a un lado de | putsputs | `LEXR-02494` |
| `diccionario_general/a_ver.jpg` | a ver | aan | `LEXR-03252` |
| `diccionario_general/abadonado,_cosa_desechada.jpg` | abadonado, cosa desechada | wãatãanisa | `LEXR-01830` |
| `diccionario_general/abajo.jpg` | abajo | -cjẽ | `LEXR-01774` |
| `diccionario_general/abajo_en_la_quebrada.jpg` | abajo en la quebrada | quitscjẽ | `LEXR-01249` |
| `diccionario_general/abandonar.jpg` | abandonar | tjengmée nvijt- | `LEXR-01557` |
| `diccionario_general/abeja,_abejón.jpg` | abeja, abejón | wãwã | `LEXR-02901` |
| `diccionario_general/abiertamente,_patente.jpg` | abiertamente, patente | ãa- | `LEXR-01961` |
| `diccionario_general/abogar,_intervenir_en_un_asunto.jpg` | abogar, intervenir en un asunto | yuwe pu’ch- | `LEXR-02249` |
| `diccionario_general/abollar.jpg` | abollar | cuẽtya-, cuẽtyáa- | `LEXR-03313` |
| `diccionario_general/abonar.jpg` | abonar | shaacue’j-, shaacue’je- | `LEXR-02675` |
| `diccionario_general/abrigarse.jpg` | abrigarse | cjã’-, cjã’a- | `LEXR-01655` |
| `diccionario_general/abrir.jpg` | abrir | pjande- | `LEXR-01877` |
| `diccionario_general/abrir_la_boca.jpg` | abrir la boca | way-, wayíi- | `LEXR-02944` |
| `diccionario_general/abrirse,_rajarse.jpg` | abrirse, rajarse | pjate- | `LEXR-01243` |
| `diccionario_general/abuelo.jpg` | abuelo | ĩishi | `LEXR-02411` |
| `diccionario_general/abuelo_o_abuela_con_nieto_o_nieta.jpg` | abuelo o abuela con nieto o nieta | ptsun | `LEXR-02059` |
| `diccionario_general/abundar,_rendir.jpg` | abundar, rendir | pejna-, pena- | `LEXR-02966` |
| `diccionario_general/aburrirse.jpg` | aburrirse | cuch-, cuchíi- | `LEXR-00961` |
| `diccionario_general/acabar.jpg` | acabar | pemba-, pembáa- | `LEXR-00984` |
| `diccionario_general/acabarse,_darse_por_terminado.jpg` | acabarse, darse por terminado | ptsuu- | `LEXR-02008` |
| `diccionario_general/acercar,_arrimar.jpg` | acercar, arrimar | nuyutya- | `LEXR-03089` |
| `diccionario_general/acercarse_voluntariamente.jpg` | acercarse voluntariamente | paautyáa- | `LEXR-03383` |
| `diccionario_general/acertadamente,_sin_equivocarse.jpg` | acertadamente, sin equivocarse | jyumbamée | `LEXR-01600` |
| `diccionario_general/achicar,_comprimir,_reducir_de_tamaño.jpg` | achicar, comprimir, reducir de tamaño | nuyle’ch-, nuyle’chi- | `LEXR-03478` |
| `diccionario_general/aclarar_el_día.jpg` | aclarar el día | cjicjy-, cjicjíi- | `LEXR-01125` |
| `diccionario_general/aclarar,_despejarse.jpg` | aclarar, despejarse | ate-, atée- | `LEXR-02514` |
| `diccionario_general/aclarar,_ponerse_claro.jpg` | aclarar, ponerse claro | afy-afi- | `LEXR-02461` |
| `diccionario_general/aclarar,_volverse_claro_(líquido).jpg` | aclarar, volverse claro (líquido) | tsall-, tsalli- | `LEXR-00649` |
| `diccionario_general/acogollar,_echar_cogollo.jpg` | acogollar, echar cogollo | culu-, culúu’ | `LEXR-02842` |
| `diccionario_general/acompañar.jpg` | acompañar | pi’cyna u’j- | `LEXR-02581` |
| `diccionario_general/aconjesar.jpg` | aconjesar | yu’cypej-, yu’cypeje-, yu’cypee- | `LEXR-01770` |
| `diccionario_general/acontecer,_suceder.jpg` | acontecer, suceder | ya’yuu- | `LEXR-00664` |
| `diccionario_general/acortar_(ej._estribos).jpg` | acortar (ej. estribos) | nuytuw-, nuytuwúu- | `LEXR-02168` |
| `diccionario_general/acortar,_caerse_el_pelo.jpg` | acortar, caerse el pelo | much-, muchi- | `LEXR-00518` |
| `diccionario_general/acortar,_mermar.jpg` | acortar, mermar | tuwúu- | `LEXR-03302` |
| `diccionario_general/acortarse.jpg` | acortarse | jytuwúu- | `LEXR-01294` |
| `diccionario_general/activo.jpg` | activo | catyja´ | `LEXR-02202` |
| `diccionario_general/activo,_hábil.jpg` | activo, hábil | dyijca | `LEXR-03904` |
| `diccionario_general/acusar,_presentar_queja_contra_otra_persona.jpg` | acusar, presentar queja contra otra persona | pãatyjĩ’cj-, pãatyjĩ’cje- | `LEXR-02715` |
| `diccionario_general/acá_arriba.jpg` | acá arriba | cacanaajũ | `LEXR-00680` |
| `diccionario_general/acá,_aquí.jpg` | acá, aquí | ay- | `LEXR-03253` |
| `diccionario_general/adelantarse.jpg` | adelantarse | fiyajts-, fiyats- | `LEXR-02265` |
| `diccionario_general/adelgazarse.jpg` | adelgazarse | zunzu- | `LEXR-02459` |
| `diccionario_general/adentro.jpg` | adentro | dyiiga, dyiisu, dyiite | `LEXR-01913` |
| `diccionario_general/adivino,_persona_que_siente_sensaciones.jpg` | adivino, persona que siente sensaciones | jyta’ñisa | `LEXR-01292` |
| `diccionario_general/adueñarse.jpg` | adueñarse | iinamu-(iiyamu-) | `LEXR-01218` |
| `diccionario_general/adulterio,_inmoralidad.jpg` | adulterio, inmoralidad | canzh yuuni | `LEXR-01713` |
| `diccionario_general/adulto,_mayor_de_edad.jpg` | adulto, mayor de edad | tjẽ’jsa | `LEXR-03574` |
| `diccionario_general/adúltero_a.jpg` | adúltero/a | canzh yuusa | `LEXR-01649` |
| `diccionario_general/afilar.jpg` | afilar | zeecu’j-, zeecu’ju- | `LEXR-00939` |
| `diccionario_general/aflojar.jpg` | aflojar | nuylajcy- nuylaqui- | `LEXR-00719` |
| `diccionario_general/aflojar,_dar_campo.jpg` | aflojar, dar campo | iiash-, iilashi- | `LEXR-03818` |
| `diccionario_general/aflojarse.jpg` | aflojarse | lash-, lashi- | `LEXR-02047` |
| `diccionario_general/afta.jpg` | afta | yuwe wã’jy | `LEXR-03671` |
| `diccionario_general/afuera.jpg` | afuera | eca | `LEXR-03850` |
| `diccionario_general/agacharse_(repetidas_veces).jpg` | agacharse (repetidas veces) | quitya’tya- | `LEXR-03665` |
| `diccionario_general/agradable,_apetecible.jpg` | agradable, apetecible | ñuspa’ | `LEXR-02088` |
| `diccionario_general/agradable,_sabroso,_saludable,_bien_(de_salud).jpg` | agradable, sabroso, saludable, bien (de salud) | wẽt, wẽtcuẽ | `LEXR-01831` |
| `diccionario_general/agredirse_(mutuamente).jpg` | agredirse (mutuamente) | puuty ya’ptjãawe- | `LEXR-00446` |
| `diccionario_general/agrio,_fermentado.jpg` | agrio, fermentado | pus | `LEXR-00823` |
| `diccionario_general/agua_bendita.jpg` | agua bendita | yase yu’ | `LEXR-00750` |
| `diccionario_general/agua_fría.jpg` | agua fría | yu’ finze | `LEXR-01698` |
| `diccionario_general/agua_hervida.jpg` | agua hervida | yu’ cbajy | `LEXR-03305` |
| `diccionario_general/agua_hirviendo.jpg` | agua hirviendo | yu’ acha | `LEXR-03037` |
| `diccionario_general/aguacero.jpg` | aguacero | nus wala | `LEXR-02818` |
| `diccionario_general/aguado.jpg` | aguado | enzh | `LEXR-01212` |
| `diccionario_general/aguantar.jpg` | aguantar | wantaĩ- | `LEXR-01565` |
| `diccionario_general/agudo,_puntiagudo.jpg` | agudo, puntiagudo | chũjwa (chũjwe) | `LEXR-03168` |
| `diccionario_general/agujerear,_taladrar,_perforar.jpg` | agujerear, taladrar, perforar | swejnde-, swende- | `LEXR-01486` |
| `diccionario_general/agutí.jpg` | agutí | ñu’py le’ch | `LEXR-02802` |
| `diccionario_general/agutí,_guatuza,_tuza_(mamífero).jpg` | agutí, guatuza, tuza (mamífero) | yu’cj cuchi | `LEXR-01428` |
| `diccionario_general/agutí,_guatín_(mamífero_roedor).jpg` | agutí, guatín (mamífero roedor) | ñu’py le’chcue | `LEXR-03616` |
| `diccionario_general/ahijada.jpg` | ahijada | iicjala | `LEXR-02376` |
| `diccionario_general/ahijado.jpg` | ahijado | iicjalu | `LEXR-02267` |
| `diccionario_general/ahogarse.jpg` | ahogarse | caambutsj-, caambutsje- | `LEXR-03786` |
| `diccionario_general/ahorcarse.jpg` | ahorcarse | jytjuuc-, jytjuucu- | `LEXR-03115` |
| `diccionario_general/ahorrar_(comida_o_dinero).jpg` | ahorrar (comida o dinero) | fina-(fiina-) | `LEXR-01454` |
| `diccionario_general/ahorrar_(varias_cosas).jpg` | ahorrar (varias cosas) | finfina- | `LEXR-03018` |
| `diccionario_general/ahumado.jpg` | ahumado | aj uweni- | `LEXR-01902` |
| `diccionario_general/ahumar.jpg` | ahumar | aj cshi’ta’j- | `LEXR-03724` |
| `diccionario_general/ahuyentar_pájaros.jpg` | ahuyentar pájaros | pajy-, pajíi- | `LEXR-02925` |
| `diccionario_general/ahí.jpg` | ahí | tyca | `LEXR-00557` |
| `diccionario_general/ajeno.jpg` | ajeno | vite jĩi | `LEXR-01264` |
| `diccionario_general/al_amor,_la_misericordia.jpg` | al amor, la misericordia | peeygãani | `LEXR-01806` |
| `diccionario_general/al_año_pasado.jpg` | al año pasado | ũ’na cus | `LEXR-01507` |
| `diccionario_general/al_borde_de.jpg` | al borde de | puts- | `LEXR-03057` |
| `diccionario_general/al_canto_de_gallo.jpg` | al canto de gallo | atall we’wetste | `LEXR-03740` |
| `diccionario_general/al_lado_de.jpg` | al lado de | puca- | `LEXR-00910` |
| `diccionario_general/al_lado_do.jpg` | al lado do | ju’ng | `LEXR-01864` |
| `diccionario_general/al_otro_lado_de_la_cordillera_(ej._tierradentro).jpg` | al otro lado de la cordillera (ej. Tierradentro) | ũyu (ũjyu’ng) | `LEXR-01964` |
| `diccionario_general/al_ponerse_el_sol.jpg` | al ponerse el sol | sec cjẽjetste | `LEXR-00996` |
| `diccionario_general/al_principio.jpg` | al principio | nyafíi, nyafiitey | `LEXR-02853` |
| `diccionario_general/al_salir_el_sol.jpg` | al salir el sol | sec cãjatste | `LEXR-00449` |
| `diccionario_general/al_través,_horizontal.jpg` | al través, horizontal | pesatj | `LEXR-02627` |
| `diccionario_general/ala_de_sombrero.jpg` | ala de sombrero | chwa’ ets | `LEXR-01716` |
| `diccionario_general/alacrán.jpg` | alacrán | usmity | `LEXR-02723` |
| `diccionario_general/alambre.jpg` | alambre | tsam wes | `LEXR-03548` |
| `diccionario_general/alargar.jpg` | alargar | nuyjyu’ja- | `LEXR-00431` |
| `diccionario_general/alcanzar.jpg` | alcanzar | sumba- | `LEXR-00923` |
| `diccionario_general/alcanzar_(en_el_camino).jpg` | alcanzar (en el camino) | cpajcy-, cpaaqui-, cpaacy- | `LEXR-02524` |
| `diccionario_general/alcanzar_a_tocar,_lograr_tocar.jpg` | alcanzar a tocar, lograr tocar | cpaajya’ndy-, cpaajya’ndyi- | `LEXR-02041` |
| `diccionario_general/alchucha_(planta_comestible).jpg` | alchucha (planta comestible) | tmbi’ch | `LEXR-03666` |
| `diccionario_general/alegrar.jpg` | alegrar | wechwecha caayaqui’j- | `LEXR-02243` |
| `diccionario_general/alero.jpg` | alero | yat menz | `LEXR-01956` |
| `diccionario_general/aletear.jpg` | aletear | a’pja’pja- | `LEXR-01509` |
| `diccionario_general/algo_que_ha_sido_escogido.jpg` | algo que ha sido escogido | tyjityjnisa | `LEXR-02341` |
| `diccionario_general/algo_templado_(freno).jpg` | algo templado (freno) | spajndspajnde | `LEXR-01411` |
| `diccionario_general/algo,_bien.jpg` | algo, bien | ũ’cjue’w | `LEXR-01773` |
| `diccionario_general/alguacil.jpg` | alguacil | nuasil (nuasel) | `LEXR-01925` |
| `diccionario_general/aligerar.jpg` | aligerar | ẽsẽe- | `LEXR-00578` |
| `diccionario_general/alimentar,_dar_de_comer.jpg` | alimentar, dar de comer | puuts-, puutsu- | `LEXR-03094` |
| `diccionario_general/alisar.jpg` | alisar | laavi’j-, laavi’ji- | `LEXR-01664` |
| `diccionario_general/aliviar.jpg` | aliviar | nuycase- | `LEXR-01604` |
| `diccionario_general/aliviarse_(de_un_dolor).jpg` | aliviarse (de un dolor) | case-, casée- | `LEXR-02520` |
| `diccionario_general/allí.jpg` | allí | jyca | `LEXR-00416` |
| `diccionario_general/alrededor.jpg` | alrededor | jytandyi | `LEXR-01459` |
| `diccionario_general/altar_dorado.jpg` | altar dorado | byuu bee altal | `LEXR-01585` |
| `diccionario_general/alumbrar_a_otro.jpg` | alumbrar a otro | peecjicj- | `LEXR-03091` |
| `diccionario_general/alumbrar,_iluminar.jpg` | alumbrar, iluminar | cweetj-, cweetje- | `LEXR-01375` |
| `diccionario_general/alumno_de_la_escuela.jpg` | alumno de la escuela | scuela luuch | `LEXR-00535` |
| `diccionario_general/alzar.jpg` | alzar | pu’quis-, pu’quisu- | `LEXR-00443` |
| `diccionario_general/alzar_(repetidas_veces).jpg` | alzar (repetidas veces) | pu’quisu’s-, pu’quisu’su- | `LEXR-01548` |
| `diccionario_general/alzar_era.jpg` | alzar era | ambu’j-, ambu’ju- | `LEXR-01439` |
| `diccionario_general/amamantar.jpg` | amamantar | cchu’chu’j-, cchu’chu’ju- | `LEXR-03742` |
| `diccionario_general/amanecer_(el_día).jpg` | amanecer (el día) | pe’te- | `LEXR-02492` |
| `diccionario_general/amanecer_(la_persona).jpg` | amanecer (la persona) | pe’te- | `LEXR-01873` |
| `diccionario_general/amansar.jpg` | amansar | cmaasu’j-, cmaasu’ju- | `LEXR-02609` |
| `diccionario_general/amansar,_domesticar.jpg` | amansar, domesticar | caastaja’j-, caastyaja’ja- | `LEXR-03773` |
| `diccionario_general/amargar,_ponerse_amargo.jpg` | amargar, ponerse amargo | yaja- | `LEXR-01573` |
| `diccionario_general/amarillento.jpg` | amarillento | atate lem | `LEXR-02091` |
| `diccionario_general/amarillo.jpg` | amarillo | shquiicy | `LEXR-01251` |
| `diccionario_general/amarillo_claro.jpg` | amarillo claro | lemlem | `LEXR-01993` |
| `diccionario_general/amarrar_(varias_veces).jpg` | amarrar (varias veces) | tundundu- | `LEXR-02282` |
| `diccionario_general/amarrar_nudo.jpg` | amarrar nudo | jyũcj-, jyũcje- | `LEXR-00714` |
| `diccionario_general/amarrar_varias_vueltas.jpg` | amarrar varias vueltas | jwendu-, jwendúu- | `LEXR-03660` |
| `diccionario_general/amarrar,_atara.jpg` | amarrar, atara | tund-, tundu- | `LEXR-02019` |
| `diccionario_general/amarse_(mutuamente).jpg` | amarse (mutuamente) | puuty ya’peeygãj-, puuty ya’peeygãja- | `LEXR-03662` |
| `diccionario_general/amañarse,_acostumbrarse.jpg` | amañarse, acostumbrarse | styãj-, styãja-, styãa- | `LEXR-03061` |
| `diccionario_general/ambos.jpg` | ambos | e’nzíi | `LEXR-02309` |
| `diccionario_general/ambos_lados,_de_lado_a_lado_(opuesto).jpg` | ambos lados, de lado a lado (opuesto) | pdyi’p | `LEXR-02820` |
| `diccionario_general/amontonar.jpg` | amontonar | muutsu’j-, muutsu’ju- | `LEXR-02491` |
| `diccionario_general/amor,_misericordia.jpg` | amor, misericordia | peeygãawa’j | `LEXR-03760` |
| `diccionario_general/ampolla.jpg` | ampolla | shcayatú | `LEXR-03484` |
| `diccionario_general/ampollarse.jpg` | ampollarse | bish-, bishi- | `LEXR-02602` |
| `diccionario_general/anaco.jpg` | anaco | is atuj | `LEXR-02107` |
| `diccionario_general/anaco_abierto.jpg` | anaco abierto | atyj cupy | `LEXR-01111` |
| `diccionario_general/anaco_tubular.jpg` | anaco tubular | catsundenimeesa | `LEXR-01367` |
| `diccionario_general/anca.jpg` | anca | jimba ji’mbe | `LEXR-00512` |
| `diccionario_general/ancho,_anchura.jpg` | ancho, anchura | tapesa | `LEXR-02234` |
| `diccionario_general/andaquí_(indígena_de_la_tribu_andaquí).jpg` | Andaquí (indígena de la tribu Andaquí) | daaquí | `LEXR-00504` |
| `diccionario_general/andar,_caminar.jpg` | andar, caminar | u’ju- | `LEXR-03780` |
| `diccionario_general/andas_(para_llevar_cadáveres).jpg` | andas (para llevar cadáveres) | aandas | `LEXR-01901` |
| `diccionario_general/angosto,_estecho.jpg` | angosto, estecho | pteenz | `LEXR-00442` |
| `diccionario_general/anguilla_(ave).jpg` | anguilla (ave) | pichga | `LEXR-02217` |
| `diccionario_general/anillo,_sortija.jpg` | anillo, sortija | sultyjica | `LEXR-02336` |
| `diccionario_general/animal_domesticado.jpg` | animal domesticado | taqui’nisa | `LEXR-01414` |
| `diccionario_general/animal_doméstico.jpg` | animal doméstico | tajcy | `LEXR-02130` |
| `diccionario_general/animal_salvaje.jpg` | animal salvaje | yu’cj ech | `LEXR-00752` |
| `diccionario_general/animal_salvaje,_fiera,_el_demonio.jpg` | animal salvaje, fiera, el demonio | ech | `LEXR-03258` |
| `diccionario_general/anochecer.jpg` | anochecer | cus-, cusu- | `LEXR-01984` |
| `diccionario_general/ansia,_náusea.jpg` | ansia, náusea | cpunga’j wẽeni | `LEXR-02367` |
| `diccionario_general/anteayer,_antier.jpg` | anteayer, antier | ũ’nacje | `LEXR-02412` |
| `diccionario_general/antenoche.jpg` | antenoche | jũ’na cuscjẽ | `LEXR-03644` |
| `diccionario_general/antepasados.jpg` | antepasados | ju’ngtjẽ’jwe’sh | `LEXR-02161` |
| `diccionario_general/anzuelo.jpg` | anzuelo | wendy ñujnz | `LEXR-02079` |
| `diccionario_general/apagar.jpg` | apagar | fĩchja- | `LEXR-00413` |
| `diccionario_general/apagarse.jpg` | apagarse | ũchja- | `LEXR-00576` |
| `diccionario_general/aparar.jpg` | aparar | paatje-, paatjée- | `LEXR-02051` |
| `diccionario_general/aparar_agua.jpg` | aparar agua | tuts-, tutsúu- | `LEXR-01004` |
| `diccionario_general/aparecer,_estar_presente.jpg` | aparecer, estar presente | vyaa- | `LEXR-03068` |
| `diccionario_general/aparte,_separado.jpg` | aparte, separado | fii | `LEXR-00968` |
| `diccionario_general/apelldio.jpg` | apelldio | quiwe yase | `LEXR-02174` |
| `diccionario_general/apellido.jpg` | apellido | quiwe yase | `LEXR-00448` |
| `diccionario_general/apisonar.jpg` | apisonar | tjetj-, tjetjée- | `LEXR-01823` |
| `diccionario_general/aplastar.jpg` | aplastar | tsep-, tsepúu- | `LEXR-00548` |
| `diccionario_general/aplastar_(repetidas_veces),_hacer_arepa.jpg` | aplastar (repetidas veces), hacer arepa | wa’tsju’j-, wa’tsju’ju- | `LEXR-01950` |
| `diccionario_general/aplaudir_(dar_repetidas_palmadas).jpg` | aplaudir (dar repetidas palmadas) | jypeetyatya- | `LEXR-00798` |
| `diccionario_general/aprender.jpg` | aprender | piya-, piyáa- | `LEXR-00985` |
| `diccionario_general/apresurarse,_tener_tiempo.jpg` | apresurarse, tener tiempo | tundu-, tundúu- | `LEXR-02074` |
| `diccionario_general/apretado.jpg` | apretado | zuuna’ | `LEXR-03719` |
| `diccionario_general/apretar.jpg` | apretar | cytem-, cytemúu- | `LEXR-00407` |
| `diccionario_general/apretarse.jpg` | apretarse | pteenzúu- (peetenzu-) | `LEXR-02058` |
| `diccionario_general/aprisa,_rápido,_pronto.jpg` | aprisa, rápido, pronto | dund (tund) | `LEXR-01857` |
| `diccionario_general/apuntar_(un_arma).jpg` | apuntar (un arma) | jypey-, jypeyi- | `LEXR-02921` |
| `diccionario_general/aquí.jpg` | aquí | ayte | `LEXR-02839` |
| `diccionario_general/araña.jpg` | araña | tupa | `LEXR-01419` |
| `diccionario_general/arbusto,_usan_la_hoja_para_lastimaduras.jpg` | arbusto, usan la hoja para lastimaduras | tamb pitscue, tamb u’y | `LEXR-02448` |
| `diccionario_general/arco_de_noche.jpg` | arco de noche | cytũus chijme | `LEXR-00408` |
| `diccionario_general/arco_del_día.jpg` | arco del día | cytũus bej | `LEXR-03657` |
| `diccionario_general/arder.jpg` | arder | bej-m, beje- | `LEXR-03398` |
| `diccionario_general/ardilla.jpg` | ardilla | shuma | `LEXR-00638` |
| `diccionario_general/arenoso.jpg` | arenoso | cu’ch | `LEXR-01207` |
| `diccionario_general/arete.jpg` | arete | tjũ’we ya’qui | `LEXR-02278` |
| `diccionario_general/argumentar.jpg` | argumentar | puii we’we- | `LEXR-03629` |
| `diccionario_general/arisco,_esquivo.jpg` | arisco, esquivo | jamby | `LEXR-02886` |
| `diccionario_general/armadillo.jpg` | armadillo | shita | `LEXR-02970` |
| `diccionario_general/arracacha.jpg` | arracacha | ã’s | `LEXR-02736` |
| `diccionario_general/arrancar.jpg` | arrancar | chucuende- | `LEXR-01121` |
| `diccionario_general/arrancar_espigas.jpg` | arrancar espigas | chuctende- | `LEXR-03377` |
| `diccionario_general/arrancar,_desarraigar.jpg` | arrancar, desarraigar | cjumbe-, cjumbée- | `LEXR-02743` |
| `diccionario_general/arrancarse.jpg` | arrancarse | chucuete- | `LEXR-01122` |
| `diccionario_general/arreglar.jpg` | arreglar | pjeu’j-, pjeu’ju- | `LEXR-00527` |
| `diccionario_general/arreglar_un_asunto.jpg` | arreglar un asunto | yuwe pjeu’j- | `LEXR-02291` |
| `diccionario_general/arrendar_(terreno).jpg` | arrendar (terreno) | arendãy- | `LEXR-01193` |
| `diccionario_general/arriba.jpg` | arriba | tjacue | `LEXR-02070` |
| `diccionario_general/arrodillarse.jpg` | arrodillarse | peejyũcue- | `LEXR-01471` |
| `diccionario_general/arrollar,_arremangar.jpg` | arrollar, arremangar | tpand-, tpandúu- | `LEXR-02939` |
| `diccionario_general/arrugar.jpg` | arrugar | shũ’sh-, shũshu- | `LEXR-02635` |
| `diccionario_general/arrugarse.jpg` | arrugarse | chu’nzhu- | `LEXR-01120` |
| `diccionario_general/asaltador.jpg` | asaltador | ũpjsá | `LEXR-03768` |
| `diccionario_general/asaltar,_agredir.jpg` | asaltar, agredir | ãapj-ãapjúu- | `LEXR-00758` |
| `diccionario_general/asar.jpg` | asar | cjacj-, cjacje- | `LEXR-00776` |
| `diccionario_general/asco,_cosa_desagrable.jpg` | asco, cosa desagrable | atsejy | `LEXR-01194` |
| `diccionario_general/asentadero_de_la_olla.jpg` | asentadero de la olla | mityj yuc | `LEXR-01870` |
| `diccionario_general/asfixiarse.jpg` | asfixiarse | ũuspa’- | `LEXR-01708` |
| `diccionario_general/asno.jpg` | asno | ashnu | `LEXR-01843` |
| `diccionario_general/asociarse_con.jpg` | asociarse con | ca´ndu- | `LEXR-02154` |
| `diccionario_general/asomar.jpg` | asomar | jweelu- | `LEXR-00705` |
| `diccionario_general/astilla.jpg` | astilla | petsetesa | `LEXR-01679` |
| `diccionario_general/asunto_de_terrenos.jpg` | asunto de terrenos | quiwe yuwe | `LEXR-02821` |
| `diccionario_general/asustar_a_otra_persona.jpg` | asustar a otra persona | caawãshi’j-, caawãshi’ji- | `LEXR-02036` |
| `diccionario_general/así,_asimismo.jpg` | así, asimismo | tyã’wẽ, tyã’wẽy (cyã’wẽ) | `LEXR-01886` |
| `diccionario_general/atar_palos_verticales.jpg` | atar palos verticales | tsjende- | `LEXR-02718` |
| `diccionario_general/atardecer.jpg` | atardecer | fi’nze- | `LEXR-00602` |
| `diccionario_general/atarraya.jpg` | atarraya | wendy ucje | `LEXR-01176` |
| `diccionario_general/atemorizarse.jpg` | atemorizarse | ũucj yajcy- | `LEXR-03691` |
| `diccionario_general/atento.jpg` | atento | een, eena’ | `LEXR-00505` |
| `diccionario_general/atizar_(la_lumbre).jpg` | atizar (la lumbre) | peescatyjĩ’j-, peescatyjĩ’ja- | `LEXR-03385` |
| `diccionario_general/atizar_la_candela.jpg` | atizar la candela | scatyĩ’j-, scatuĩja- | `LEXR-03183` |
| `diccionario_general/atragantarse.jpg` | atragantarse | jytu’cj-, jytu’cje- | `LEXR-03202` |
| `diccionario_general/atrancar.jpg` | atrancar | atj-, atje- | `LEXR-02296` |
| `diccionario_general/atrapar,_coger_con_trampa.jpg` | atrapar, coger con trampa | yajcy- | `LEXR-03158` |
| `diccionario_general/atravesar,_cruzar,_pasar_al_otro_lado.jpg` | atravesar, cruzar, pasar al otro lado | uycjẽw, uycjẽúu- | `LEXR-03549` |
| `diccionario_general/atrás,_detrás.jpg` | atrás, detrás | e’s | `LEXR-03196` |
| `diccionario_general/aventajar.jpg` | aventajar | puutejca- | `LEXR-02439` |
| `diccionario_general/aventar.jpg` | aventar | cweejya’j-cweejya’ja- | `LEXR-02158` |
| `diccionario_general/aventar_trigo.jpg` | aventar trigo | scuutyj cweejya’jya’ | `LEXR-03460` |
| `diccionario_general/avergonzar,_causar_pena.jpg` | avergonzar, causar pena | caytjame’j-, caytjame’je- | `LEXR-02419` |
| `diccionario_general/avisar_(al_mismo_tiempo_que_hace_otra_cosa).jpg` | avisar (al mismo tiempo que hace otra cosa) | iipta’sh- | `LEXR-03913` |
| `diccionario_general/avisar_(repetidas_veces_o_a_varias_personas).jpg` | avisar (repetidas veces o a varias personas) | pta’shi’sh-, pta’shi’shi- | `LEXR-00905` |
| `diccionario_general/avisar,_anunciar,_informar,_señalar.jpg` | avisar, anunciar, informar, señalar | pta’sh-, pta’shi- | `LEXR-01934` |
| `diccionario_general/avisar,_traer_un_mensaje.jpg` | avisar, traer un mensaje | yuwe pta’sh- | `LEXR-03783` |
| `diccionario_general/aviso,_anuncio.jpg` | aviso, anuncio | pta’shni | `LEXR-03294` |
| `diccionario_general/avispa.jpg` | avispa | menzucue | `LEXR-03142` |
| `diccionario_general/avispa_(insecto).jpg` | avispa (insecto) | shita | `LEXR-03684` |
| `diccionario_general/avispado,_vivo.jpg` | avispado, vivo | biu’ | `LEXR-01710` |
| `diccionario_general/avío_(comida_para_el_camino).jpg` | avío (comida para el camino) | caame | `LEXR-00485` |
| `diccionario_general/ayer.jpg` | ayer | jũ’na | `LEXR-03541` |
| `diccionario_general/ayudar_(por_turno).jpg` | ayudar (por turno) | pu’chji’ch-, pu’chji’chji- | `LEXR-01681` |
| `diccionario_general/ayudar,_apoyar.jpg` | ayudar, apoyar | pu’ch-, pu’chji- | `LEXR-02713` |
| `diccionario_general/ayudarse_(mutuamente).jpg` | ayudarse (mutuamente) | puuty ya’pu’ch-, puuty ya’pu’chji- | `LEXR-00633` |
| `diccionario_general/ayunar.jpg` | ayunar | yũuna- | `LEXR-00573` |
| `diccionario_general/azul_celeste.jpg` | azul celeste | atate tsẽy | `LEXR-02354` |
| `diccionario_general/azul_claro.jpg` | azul claro | tsẽytsẽy chijme | `LEXR-01944` |
| `diccionario_general/azul_subido.jpg` | azul subido | cjũchcjũch tsẽy | `LEXR-01043` |
| `diccionario_general/azul,_verde.jpg` | azul, verde | tsẽy | `LEXR-03686` |
| `diccionario_general/añadir,_pegar_con_goma.jpg` | añadir, pegar con goma | shquitya-, shquityáa- | `LEXR-00451` |
| `diccionario_general/baba.jpg` | baba | shna’na | `LEXR-02444` |
| `diccionario_general/bagazo.jpg` | bagazo | ñusha cja’ty | `LEXR-01105` |
| `diccionario_general/bailador.jpg` | bailador | cu’jsa | `LEXR-03016` |
| `diccionario_general/bailar.jpg` | bailar | cu’j-, cu’ju- | `LEXR-00403` |
| `diccionario_general/baile_de_la_boda.jpg` | baile de la boda | uwe cu’jya’ (T) | `LEXR-01947` |
| `diccionario_general/baile_de_la_chucha.jpg` | baile de la chucha | chucha cu’jni | `LEXR-01040` |
| `diccionario_general/baile_de_la_chucha_(un_año_después_de_edificar_una_casa).jpg` | baile de la chucha (un año después de edificar una casa) | chucha cu’jni | `LEXR-02470` |
| `diccionario_general/baile_de_un_niño_muerto.jpg` | baile de un niño muerto | ángeles cu’jni | `LEXR-03372` |
| `diccionario_general/baile_en_una_minga.jpg` | baile en una minga | pi’cy yat cu’jni | `LEXR-02387` |
| `diccionario_general/bajar.jpg` | bajar | quĩj-, quĩja-, quĩi- | `LEXR-00729` |
| `diccionario_general/bajar,_descender.jpg` | bajar, descender | sẽj-, sẽje-, sẽe- | `LEXR-03509` |
| `diccionario_general/bajar,_descender,_caber,_ponserse_el_sol.jpg` | bajar, descender, caber, ponserse el sol | cjẽj-, cjẽjẽ-, cjẽe- | `LEXR-01206` |
| `diccionario_general/bajar,_desmontar.jpg` | bajar, desmontar | jysa’j-, jysa’ja- | `LEXR-01992` |
| `diccionario_general/bajar,_desmontar_(de_una_bestia).jpg` | bajar, desmontar (de una bestia) | iisa’j-, iisa’ja- | `LEXR-02268` |
| `diccionario_general/bajo_(estatura).jpg` | bajo (estatura) | fi’fy | `LEXR-01213` |
| `diccionario_general/balanza,_romana.jpg` | balanza, romana | isani | `LEXR-01662` |
| `diccionario_general/banca_(para_sentarse).jpg` | banca (para sentarse) | pangu | `LEXR-00524` |
| `diccionario_general/barato.jpg` | barato | pa’gamée | `LEXR-02667` |
| `diccionario_general/barbasco_(planta_venenosa).jpg` | barbasco (planta venenosa) | sẽ’j | `LEXR-01942` |
| `diccionario_general/barranco.jpg` | barranco | peña | `LEXR-01397` |
| `diccionario_general/barrer.jpg` | barrer | pand-, pandu- | `LEXR-02926` |
| `diccionario_general/barretón.jpg` | barretón | paletun (pleetun T) | `LEXR-00899` |
| `diccionario_general/barsino.jpg` | barsino | palsin | `LEXR-01393` |
| `diccionario_general/batata.jpg` | batata | ũtj | `LEXR-01637` |
| `diccionario_general/bautizado.jpg` | bautizado | yesenisa | `LEXR-03467` |
| `diccionario_general/bautizo.jpg` | bautizo | yaseni | `LEXR-02558` |
| `diccionario_general/bayo.jpg` | bayo | payu | `LEXR-03411` |
| `diccionario_general/bayo_cariblanco.jpg` | bayo cariblanco | payu pjeelu | `LEXR-02670` |
| `diccionario_general/bañarse.jpg` | bañarse | pẽw-, pẽwúu- | `LEXR-01161` |
| `diccionario_general/bañarse_(con_remedio).jpg` | bañarse (con remedio) | jypẽew-, jypẽewu- | `LEXR-03200` |
| `diccionario_general/beber_(lo_ajeno).jpg` | beber (lo ajeno) | ntundy-, ntundyi- | `LEXR-01998` |
| `diccionario_general/beber,_tomar.jpg` | beber, tomar | tundy-, tundyíi- (tungy-) | `LEXR-02896` |
| `diccionario_general/bejuco.jpg` | bejuco | shã’we yaj | `LEXR-00537` |
| `diccionario_general/bendecir.jpg` | bendecir | bendesĩ | `LEXR-03164` |
| `diccionario_general/bien_tejido_(jigra,_canasta,_ruana).jpg` | bien tejido (jigra, canasta, ruana) | tjutj | `LEXR-03812` |
| `diccionario_general/bien,_bueno.jpg` | bien, bueno | ew | `LEXR-02103` |
| `diccionario_general/bienes,_posesiones.jpg` | bienes, posesiones | ji’pjuni | `LEXR-02377` |
| `diccionario_general/bienestar,_felicidad.jpg` | bienestar, felicidad | wẽt ũsni, wẽt ũswa’j | `LEXR-03003` |
| `diccionario_general/bigote,_barba.jpg` | bigote, barba | yuwe cjas | `LEXR-03421` |
| `diccionario_general/billete.jpg` | billete | vyuu ets | `LEXR-03274` |
| `diccionario_general/biznieto,_biznieta.jpg` | biznieto, biznieta | jweete ntsun | `LEXR-02109` |
| `diccionario_general/blanco.jpg` | blanco | chijme | `LEXR-01038` |
| `diccionario_general/blanco_(persona_de_raza_blanca).jpg` | blanco (persona de raza blanca) | mushca (T) | `LEXR-01537` |
| `diccionario_general/blancuzco.jpg` | blancuzco | chijmchijme | `LEXR-02361` |
| `diccionario_general/blandir_(bastón).jpg` | blandir (bastón) | vyandu- | `LEXR-00841` |
| `diccionario_general/blando.jpg` | blando | lupe | `LEXR-01868` |
| `diccionario_general/blanquear.jpg` | blanquear | chiime´j-, chiime’je- | `LEXR-01118` |
| `diccionario_general/bobo,_tímido.jpg` | bobo, tímido | ul | `LEXR-00657` |
| `diccionario_general/boca_abajo.jpg` | boca abajo | pquipja | `LEXR-00632` |
| `diccionario_general/bordón,_bastón.jpg` | bordón, bastón | cjãambu | `LEXR-02156` |
| `diccionario_general/borrachero_(árbol_venenosa_y_narcótico).jpg` | borrachero (árbol venenosa y narcótico) | yash | `LEXR-01954` |
| `diccionario_general/borrar,_limpiar_(fregando).jpg` | borrar, limpiar (fregando) | cjũcj-, cjũcju- | `LEXR-01850` |
| `diccionario_general/botar_(al_viento),_regar,_arrojar.jpg` | botar (al viento), regar, arrojar | pujmb-, pumbu- | `LEXR-03778` |
| `diccionario_general/botar,_tirar.jpg` | botar, tirar | wãatãj-, wãatãja-, wãatãa- | `LEXR-00662` |
| `diccionario_general/bramar.jpg` | bramar | shita-, shitáa- | `LEXR-01409` |
| `diccionario_general/brea.jpg` | brea | spiina’sa | `LEXR-01485` |
| `diccionario_general/breve.jpg` | breve | jyu’jmeecue | `LEXR-03052` |
| `diccionario_general/brillar.jpg` | brillar | pu’inene- | `LEXR-00908` |
| `diccionario_general/bromeador,_chistoso.jpg` | bromeador, chistoso | shaacuesa | `LEXR-02496` |
| `diccionario_general/bromear,_chancear.jpg` | bromear, chancear | shaacue we’we- | `LEXR-02891` |
| `diccionario_general/bueno,_fino.jpg` | bueno, fino | ewsa | `LEXR-03137` |
| `diccionario_general/burlar.jpg` | burlar | npeevyshijca-, npeevyshica- (npeeshijca-) | `LEXR-01303` |
| `diccionario_general/burlar,_hacer_burla.jpg` | burlar, hacer burla | pshi’nd-, pshi’ndu- (T) | `LEXR-03146` |
| `diccionario_general/buscar.jpg` | buscar | pacue-, pacuée- | `LEXR-02117` |
| `diccionario_general/búho.jpg` | búho | cupe | `LEXR-00595` |
| `diccionario_general/caballo.jpg` | caballo | jimba | `LEXR-03198` |
| `diccionario_general/cabecear.jpg` | cabecear | quitje’tje- | `LEXR-00993` |
| `diccionario_general/cabra.jpg` | cabra | capla | `LEXR-01588` |
| `diccionario_general/cabuyal,_roza_de_cabuya.jpg` | cabuyal, roza de cabuya | bats ej | `LEXR-00945` |
| `diccionario_general/cada.jpg` | cada | iisa | `LEXR-00605` |
| `diccionario_general/cada_saliente_del_vértice_de_techo.jpg` | cada saliente del vértice de techo | yat tjũ’we | `LEXR-02028` |
| `diccionario_general/cadera.jpg` | cadera | yuc dyi’tj | `LEXR-02598` |
| `diccionario_general/cadáver.jpg` | cadáver | uuni cja’ty | `LEXR-01096` |
| `diccionario_general/caer.jpg` | caer | wete-, wetée- | `LEXR-00469` |
| `diccionario_general/caer_encima_de.jpg` | caer encima de | acach-, acachji- | `LEXR-01510` |
| `diccionario_general/caer_granizo,_granizar.jpg` | caer granizo, granizar | cuetumba ũshi- | `LEXR-01285` |
| `diccionario_general/caer_rayo.jpg` | caer rayo | cpi’sh quĩj- | `LEXR-02365` |
| `diccionario_general/cafeto_(árbol).jpg` | cafeto (árbol) | twaatsec | `LEXR-03792` |
| `diccionario_general/calabazo_(en_forma_de_gancho).jpg` | calabazo (en forma de gancho) | tuca vica | `LEXR-01760` |
| `diccionario_general/calabazo_(en_forma_embudo).jpg` | calabazo (en forma embudo) | tuca ĩts | `LEXR-01621` |
| `diccionario_general/calabazo_(para_sevir_chicha).jpg` | calabazo (para sevir chicha) | tuca cha’cy | `LEXR-02452` |
| `diccionario_general/calambre.jpg` | calambre | shaacãj | `LEXR-01320` |
| `diccionario_general/calavera.jpg` | calavera | uusá jycuet dyi’tj | `LEXR-03528` |
| `diccionario_general/caldo.jpg` | caldo | nenga yu’ | `LEXR-03361` |
| `diccionario_general/calentar.jpg` | calentar | cbaji’j-, cbaji’ji- | `LEXR-00487` |
| `diccionario_general/calentar_(a_otro).jpg` | calentar (a otro) | baji’j-, baji’ji- | `LEXR-01112` |
| `diccionario_general/calentarse.jpg` | calentarse | bajch-, bachi- | `LEXR-00482` |
| `diccionario_general/caliente.jpg` | caliente | acha | `LEXR-01025` |
| `diccionario_general/callado.jpg` | callado | viina’ | `LEXR-00465` |
| `diccionario_general/callar,_hacer_callar.jpg` | callar, hacer callar | shuuna’ nvijt- | `LEXR-01619` |
| `diccionario_general/callo.jpg` | callo | iindeeweni | `LEXR-03231` |
| `diccionario_general/calmarse,_cesar.jpg` | calmarse, cesar | tujnd-, tujndu- | `LEXR-03392` |
| `diccionario_general/calumniar,_criticar.jpg` | calumniar, criticar | nuywe’we- | `LEXR-02000` |
| `diccionario_general/calvo.jpg` | calvo | dyictjé sũpy | `LEXR-03112` |
| `diccionario_general/cambiar_de_aspecto.jpg` | cambiar de aspecto | fiy yuu- | `LEXR-02372` |
| `diccionario_general/camino_de_herradura.jpg` | camino de herradura | jimba dyi’j | `LEXR-02485` |
| `diccionario_general/campo_de_coca.jpg` | campo de coca | ẽsh ej | `LEXR-03374` |
| `diccionario_general/candelilla_(insecto).jpg` | candelilla (insecto) | ipy cjũch | `LEXR-01863` |
| `diccionario_general/cangrejo.jpg` | cangrejo | wãcã | `LEXR-01570` |
| `diccionario_general/cansar,_fatigar.jpg` | cansar, fatigar | cwaatyi’j-, cwaatyi’ji- | `LEXR-03731` |
| `diccionario_general/cansarse.jpg` | cansarse | wajty-, watyi- | `LEXR-01012` |
| `diccionario_general/canturrear.jpg` | canturrear | tutu’tu- | `LEXR-00456` |
| `diccionario_general/capa_de_maíz.jpg` | capa de maíz | cutyj fycach | `LEXR-01986` |
| `diccionario_general/cara_a_cara.jpg` | cara a cara | puuty pdyi’p | `LEXR-00531` |
| `diccionario_general/caracol.jpg` | caracol | shape | `LEXR-01162` |
| `diccionario_general/carbón,_brasa.jpg` | carbón, brasa | ipy chjã’chja | `LEXR-02701` |
| `diccionario_general/cardar_lana.jpg` | cardar lana | cjaasu’j-, cjaasu’ju- | `LEXR-03756` |
| `diccionario_general/careto,_cariblanco.jpg` | careto, cariblanco | pjeelu | `LEXR-02759` |
| `diccionario_general/cargadera_(de_la_jigra).jpg` | cargadera (de la jigra) | ya’ja wes | `LEXR-01832` |
| `diccionario_general/cargar.jpg` | cargar | tũ’s-, tũsu-, (tu’s-) | `LEXR-03067` |
| `diccionario_general/cargar_a_cuestas.jpg` | cargar a cuestas | ĩ’pjy-, ĩ’pji- | `LEXR-03887` |
| `diccionario_general/cargar_debajo_del_brazo.jpg` | cargar debajo del brazo | caatenzu’j-, caatenzu’ju- | `LEXR-01513` |
| `diccionario_general/cargar_sobre_sí_mismo.jpg` | cargar sobre sí mismo | ya’tyaj-, ya’tyaja- | `LEXR-03885` |
| `diccionario_general/caripaspada,_de_mejillas_rosadas.jpg` | caripaspada, de mejillas rosadas | wat | `LEXR-00932` |
| `diccionario_general/carna_pulpa.jpg` | carna pulpa | chich tujnd | `LEXR-02299` |
| `diccionario_general/carne_de_la_cadera.jpg` | carne de la cadera | yuc chich tujnd | `LEXR-02349` |
| `diccionario_general/caro.jpg` | caro | pa’ga | `LEXR-02323` |
| `diccionario_general/carpintero.jpg` | carpintero | fytũ pagayú | `LEXR-03049` |
| `diccionario_general/carrizo_de_guadua.jpg` | carrizo de guadua | sllimum | `LEXR-03811` |
| `diccionario_general/casar,_legalizar_matrimonio.jpg` | casar, legalizar matrimonio | caamba’j-, caamba’ja- | `LEXR-02779` |
| `diccionario_general/casarse_(dícese_de_la_mujer).jpg` | casarse (dícese de la mujer) | iimi’- | `LEXR-01049` |
| `diccionario_general/casarse_(dícese_del_hombre).jpg` | casarse (dícese del hombre) | iiyuu- | `LEXR-01730` |
| `diccionario_general/casarse,_formar_pareja.jpg` | casarse, formar pareja | ptamúu- | `LEXR-01080` |
| `diccionario_general/casco_(del_caballo).jpg` | casco (del caballo) | jimba cuse vyllill | `LEXR-00511` |
| `diccionario_general/casi.jpg` | casi | -dyiji- | `LEXR-00579` |
| `diccionario_general/caspi_(árbol).jpg` | caspi (árbol) | dyi’tjemby | `LEXR-02478` |
| `diccionario_general/castaño.jpg` | castaño | cjũchcjũch bej | `LEXR-02607` |
| `diccionario_general/castellano_(idioma).jpg` | castellano (idioma) | llinu | `LEXR-02271` |
| `diccionario_general/castrar,_capar.jpg` | castrar, capar | cpuunu’j-, cpuunu’ju- | `LEXR-03379` |
| `diccionario_general/causar_dolor_o_enfermedad.jpg` | causar dolor o enfermedad | aca ũs- | `LEXR-03375` |
| `diccionario_general/causar_hambre.jpg` | causar hambre | cwẽeje’j-, cwẽeje’je- | `LEXR-01723` |
| `diccionario_general/causar_pereza,_desanimar.jpg` | causar pereza, desanimar | cwa’lu’j-, cwa’lu’ju- | `LEXR-01446` |
| `diccionario_general/causar_sentir_'señas'.jpg` | causar sentir ’señas’ | ctã’ñi’j-, ctã’ñi’ji- | `LEXR-03077` |
| `diccionario_general/causar_sombra.jpg` | causar sombra | pshũ’ju- | `LEXR-03610` |
| `diccionario_general/cavar_cámara_lateral_para_enterrar.jpg` | cavar cámara lateral para enterrar | pumba’j-, pumba’ja- | `LEXR-01936` |
| `diccionario_general/cavar_zanja.jpg` | cavar zanja | chama’j-, chamba’ja- | `LEXR-02420` |
| `diccionario_general/cavar,_abrir_hoyo,_ahuecar.jpg` | cavar, abrir hoyo, ahuecar | cafi´j-, cafi´ji- | `LEXR-03427` |
| `diccionario_general/cazador.jpg` | cazador | vicysa | `LEXR-01491` |
| `diccionario_general/caña_de_maíz.jpg` | caña de maíz | cutyj dyi’tj | `LEXR-01374` |
| `diccionario_general/cañaduzal.jpg` | cañaduzal | ñusha ej | `LEXR-01896` |
| `diccionario_general/celebrar_en_baile.jpg` | celebrar en baile | cu’ju qui’p- | `LEXR-03498` |
| `diccionario_general/celos.jpg` | celos | iipyãani | `LEXR-03914` |
| `diccionario_general/centella_(planta).jpg` | centella (planta) | quiwendawa | `LEXR-01553` |
| `diccionario_general/cerca.jpg` | cerca | utya | `LEXR-02138` |
| `diccionario_general/cerca_a.jpg` | cerca a | pucacjẽ | `LEXR-02628` |
| `diccionario_general/cerca_de_alambre.jpg` | cerca de alambre | tsam upj | `LEXR-00454` |
| `diccionario_general/cerca_de_cabuya.jpg` | cerca de cabuya | bats upj | `LEXR-01275` |
| `diccionario_general/cerca_de_carrizo.jpg` | cerca de carrizo | pel upj | `LEXR-03628` |
| `diccionario_general/cerca_de_lechero.jpg` | cerca de lechero | fychacha upj | `LEXR-00881` |
| `diccionario_general/cerca_de_palos_verticales.jpg` | cerca de palos verticales | tsjende upj | `LEXR-01328` |
| `diccionario_general/cerca_hecha_de_palos_verticales.jpg` | cerca hecha de palos verticales | tsjende upj | `LEXR-03124` |
| `diccionario_general/cercar_la_hortaliza.jpg` | cercar la hortaliza | tulu’j-, tulu’ju- | `LEXR-01002` |
| `diccionario_general/cerco_de_lechero.jpg` | cerco de lechero | fychacha upj | `LEXR-03084` |
| `diccionario_general/cerdo,_marrano,_puerco.jpg` | cerdo, marrano, puerco | cuchi | `LEXR-01130` |
| `diccionario_general/cernidor,_cernedor,_cedazo,_susunga.jpg` | cernidor, cernedor, cedazo, susunga | a’tsjanisa | `LEXR-02649` |
| `diccionario_general/cernir,_cerner,_colar.jpg` | cernir, cerner, colar | a’tsja- | `LEXR-00582` |
| `diccionario_general/cerote_(árbol).jpg` | cerote (árbol) | chavy tjacue fytũ | `LEXR-01653` |
| `diccionario_general/cerrado.jpg` | cerrado | apjni | `LEXR-01192` |
| `diccionario_general/cerrar_la_boca.jpg` | cerrar la boca | iimujcue- | `LEXR-03339` |
| `diccionario_general/cerrar,_tapar,_cubrir.jpg` | cerrar, tapar, cubrir | apj-, apjáa- | `LEXR-02513` |
| `diccionario_general/ceñirse.jpg` | ceñirse | ya’jytund- | `LEXR-03635` |
| `diccionario_general/ceñirse,_amarrar_(con_correa_o_chumbe).jpg` | ceñirse, amarrar (con correa o chumbe) | jytund-, jytundu- | `LEXR-03710` |
| `diccionario_general/chachafruto_(árbol).jpg` | chachafruto (árbol) | uswa’l | `LEXR-03002` |
| `diccionario_general/chamuscar.jpg` | chamuscar | cnzeevy-, cnzeevi- | `LEXR-01044` |
| `diccionario_general/chamón_(ave_dañina).jpg` | chamón (ave dañina) | tũts | `LEXR-02342` |
| `diccionario_general/chasquear,_rechinar.jpg` | chasquear, rechinar | zyaya-, zyayáa- | `LEXR-03924` |
| `diccionario_general/chicga_de_caña,_guarapo.jpg` | chicga de caña, guarapo | ñusha beca | `LEXR-03249` |
| `diccionario_general/chicha_de_maíz.jpg` | chicha de maíz | beca sec, cuty beca | `LEXR-01362` |
| `diccionario_general/chicha_dulce_de_maíz.jpg` | chicha dulce de maíz | beca ñusha | `LEXR-00387` |
| `diccionario_general/chicha_fermentada.jpg` | chicha fermentada | beca pus | `LEXR-03874` |
| `diccionario_general/chicharrón.jpg` | chicharrón | chalún | `LEXR-00683` |
| `diccionario_general/chiflar.jpg` | chiflar | ufy-, ufi- | `LEXR-01259` |
| `diccionario_general/chiflar_(repetidas_veces).jpg` | chiflar (repetidas veces) | ufiifi- | `LEXR-02830` |
| `diccionario_general/chirriar.jpg` | chirriar | ziyaj-, ziyaji- | `LEXR-01634` |
| `diccionario_general/chistoso.jpg` | chistoso | pjay | `LEXR-00631` |
| `diccionario_general/chocar_con.jpg` | chocar con | puuty ijca-, puuty iica- | `LEXR-03648` |
| `diccionario_general/choclo_cocido.jpg` | choclo cocido | shũpy | `LEXR-00922` |
| `diccionario_general/chorrear.jpg` | chorrear | qui’na- | `LEXR-01754` |
| `diccionario_general/chorrear,_escurrir.jpg` | chorrear, escurrir | sus-, susúu- | `LEXR-03241` |
| `diccionario_general/choza,_con_techo_de_paja.jpg` | choza, con techo de paja | tsjĩtsj yat | `LEXR-02018` |
| `diccionario_general/chulco_(plana_medicinal).jpg` | chulco (plana medicinal) | cuetpũts | `LEXR-01133` |
| `diccionario_general/chulco_(planta_medicinal).jpg` | chulco (planta medicinal) | vyuutyjã’ | `LEXR-03275` |
| `diccionario_general/chupar_caña.jpg` | chupar caña | yu’y-, yu’yu- | `LEXR-03858` |
| `diccionario_general/chuzar_(aprovechando_ausencia_del_dueño).jpg` | chuzar (aprovechando ausencia del dueño) | nyãja- | `LEXR-02001` |
| `diccionario_general/chuzar,_punzar.jpg` | chuzar, punzar | ñaja- (yãja-) | `LEXR-01349` |
| `diccionario_general/cidrayota.jpg` | cidrayota | shwa’ | `LEXR-02937` |
| `diccionario_general/ciempiés.jpg` | ciempiés | tupil | `LEXR-03098` |
| `diccionario_general/ciertamente.jpg` | ciertamente | -dyij- | `LEXR-03128` |
| `diccionario_general/cierto,_ciertamente.jpg` | cierto, ciertamente | yuj | `LEXR-00754` |
| `diccionario_general/cinchar,_asegurar_la_silla_con_cincha.jpg` | cinchar, asegurar la silla con cincha | sinzha- | `LEXR-01252` |
| `diccionario_general/cinturón.jpg` | cinturón | jytundnisa | `LEXR-03356` |
| `diccionario_general/ciruelo_(árbol).jpg` | ciruelo (árbol) | tsunde tash | `LEXR-02768` |
| `diccionario_general/claro_de_huevo.jpg` | claro de huevo | zits chijme | `LEXR-03530` |
| `diccionario_general/clavar_varias_estacas.jpg` | clavar varias estacas | quitjeetj-, quitjeetje- | `LEXR-00994` |
| `diccionario_general/clavar,_acuñar_(teja,_maíz),_abrochar,_abotonar.jpg` | clavar, acuñar (teja, maíz), abrochar, abotonar | fyuts-, fyutsu- | `LEXR-02043` |
| `diccionario_general/clavar,_poner_estaca.jpg` | clavar, poner estaca | quitj-, quitje- | `LEXR-02391` |
| `diccionario_general/cloquear.jpg` | cloquear | lucjlucj jĩ- | `LEXR-03624` |
| `diccionario_general/coatí,_cusumbe.jpg` | coatí, cusumbe | cãtsa | `LEXR-01525` |
| `diccionario_general/cobijarse_con_otra_persona.jpg` | cobijarse con otra persona | yã’py-, yã’pji- | `LEXR-03490` |
| `diccionario_general/cobijarse,_taparse.jpg` | cobijarse, taparse | pa’ch-, pa’chi- (pã’ch-) | `LEXR-02384` |
| `diccionario_general/cobrador.jpg` | cobrador | yul pẽysa | `LEXR-01345` |
| `diccionario_general/cobrar_una_deuda.jpg` | cobrar una deuda | yul pẽjy- | `LEXR-00755` |
| `diccionario_general/coca.jpg` | coca | ẽsh | `LEXR-00480` |
| `diccionario_general/cocer.jpg` | cocer | ĩitse’j-, ĩitse’je- | `LEXR-03422` |
| `diccionario_general/cocido.jpg` | cocido | ĩitse’jni | `LEXR-02646` |
| `diccionario_general/cocinar.jpg` | cocinar | mityjáj- | `LEXR-00717` |
| `diccionario_general/cocinar_yerba.jpg` | cocinar yerba | cujya- | `LEXR-03045` |
| `diccionario_general/coger_(algo_que_viene_del_rumbo_opuesto),_apañar.jpg` | coger (algo que viene del rumbo opuesto), apañar | pu’uwe- | `LEXR-00988` |
| `diccionario_general/coger_rastro_(repetidas_veces).jpg` | coger rastro (repetidas veces) | jyputa’ta- | `LEXR-00975` |
| `diccionario_general/coger_sin_permiso.jpg` | coger sin permiso | npach-, npaachíi- | `LEXR-01231` |
| `diccionario_general/coger,_llevar_en_la_mano.jpg` | coger, llevar en la mano | at-, atúu- | `LEXR-01028` |
| `diccionario_general/cogollo.jpg` | cogollo | cul | `LEXR-03559` |
| `diccionario_general/cogollo_de_fique.jpg` | cogollo de fique | bats yafy | `LEXR-00946` |
| `diccionario_general/cojear.jpg` | cojear | leng-, lengu- | `LEXR-01386` |
| `diccionario_general/cojo.jpg` | cojo | leng | `LEXR-02989` |
| `diccionario_general/colerín.jpg` | colerín | cpunga’j wee | `LEXR-00873` |
| `diccionario_general/colgado.jpg` | colgado | letani | `LEXR-00802` |
| `diccionario_general/colgante.jpg` | colgante | lepja | `LEXR-03890` |
| `diccionario_general/colgar.jpg` | colgar | chita- | `LEXR-01442` |
| `diccionario_general/colgar_(varias_cosas).jpg` | colgar (varias cosas) | a’qui’cy-, a’qui’qui- | `LEXR-02877` |
| `diccionario_general/colgarse,_ahorcarse.jpg` | colgarse, ahorcarse | ya’cy-, ya’qui- | `LEXR-03350` |
| `diccionario_general/colibrí,_esmeralda.jpg` | colibrí, esmeralda | e’tscuẽ | `LEXR-00600` |
| `diccionario_general/colocar_espantapájaros_(en_los_sembrados).jpg` | colocar espantapájaros (en los sembrados) | caanasa’j-, caanasa’ja- | `LEXR-01030` |
| `diccionario_general/color_claro.jpg` | color claro | tsejctsejc | `LEXR-01684` |
| `diccionario_general/colorado,_rojizo.jpg` | colorado, rojizo | ipyñiñ | `LEXR-01382` |
| `diccionario_general/columna_vertebral.jpg` | columna vertebral | tsinz zec | `LEXR-01943` |
| `diccionario_general/columpiar.jpg` | columpiar | tsuvy-, tsuvíi- | `LEXR-03301` |
| `diccionario_general/comadreja.jpg` | comadreja | wãyãy, wẽyĩy | `LEXR-01630` |
| `diccionario_general/comején.jpg` | comején | fytũu chica | `LEXR-01661` |
| `diccionario_general/comer.jpg` | comer | iiũ’- | `LEXR-01381` |
| `diccionario_general/comer_demasiado.jpg` | comer demasiado | pũ’we- | `LEXR-00825` |
| `diccionario_general/comer_lo_ajeno.jpg` | comer lo ajeno | nũ’we- | `LEXR-01668` |
| `diccionario_general/comestible.jpg` | comestible | ũ’nisa | `LEXR-00763` |
| `diccionario_general/cometer_adulterio.jpg` | cometer adulterio | canzh yuu- | `LEXR-03496` |
| `diccionario_general/cometer_falta,_incumplir,_ser_indigno.jpg` | cometer falta, incumplir, ser indigno | ãjmée yũu- | `LEXR-02086` |
| `diccionario_general/comida,_alimento.jpg` | comida, alimento | ũ’ | `LEXR-02146` |
| `diccionario_general/como_si_fuera.jpg` | como si fuera | -tjas | `LEXR-01900` |
| `diccionario_general/como,_¿cómo.jpg` | como, ¿cómo? | ma’wẽ | `LEXR-02789` |
| `diccionario_general/comoquiera.jpg` | comoquiera | ma’wẽva | `LEXR-03382` |
| `diccionario_general/compartir.jpg` | compartir | jytyunde- | `LEXR-02163` |
| `diccionario_general/compartir_el_llanto_de_otro.jpg` | compartir el llanto de otro | paaũ’ne- | `LEXR-00523` |
| `diccionario_general/compartir_el_sufrimiento_de_otro.jpg` | compartir el sufrimiento de otro | paapeeygãj-, paapeeygãja- | `LEXR-00433` |
| `diccionario_general/compartir_la_comida_de_otro.jpg` | compartir la comida de otro | paaũ’we-, (pũ’we-) | `LEXR-01803` |
| `diccionario_general/compartir_la_tristeza_de_otro.jpg` | compartir la tristeza de otro | paañusu- | `LEXR-00722` |
| `diccionario_general/compartir_tristeza_de_otro.jpg` | compartir tristeza de otro | paayũs-, paayũsu- | `LEXR-00434` |
| `diccionario_general/compartir,_colaborar.jpg` | compartir, colaborar | pu’ch-, pu’chji- | `LEXR-02123` |
| `diccionario_general/completar.jpg` | completar | cãja’j-, cãja’ja- | `LEXR-01449` |
| `diccionario_general/comprado,_compra.jpg` | comprado, compra | weyní | `LEXR-02557` |
| `diccionario_general/comprador,_que_compra.jpg` | comprador, que compra | weysá | `LEXR-01340` |
| `diccionario_general/comprometida_(la_novia).jpg` | comprometida (la novia) | iimi’ya’ passa | `LEXR-03643` |
| `diccionario_general/con.jpg` | con | -ju | `LEXR-01579` |
| `diccionario_general/con_las_uñas,_garras.jpg` | con las uñas, garras | pachpach | `LEXR-00435` |
| `diccionario_general/con_sabor_de_humo.jpg` | con sabor de humo | ajaj | `LEXR-00942` |
| `diccionario_general/con_señal,_marca.jpg` | con señal, marca | iisawa’jni | `LEXR-01219` |
| `diccionario_general/con_ustedes.jpg` | con ustedes | i’cue’sh | `LEXR-03404` |
| `diccionario_general/conciencia.jpg` | conciencia | ũusutjeni | `LEXR-02775` |
| `diccionario_general/conciliar.jpg` | conciliar | caapuutwe’we’j-, caapuutywe’we’je- | `LEXR-00950` |
| `diccionario_general/condenar.jpg` | condenar | ewmeete nyijt- | `LEXR-01660` |
| `diccionario_general/condolerse,_compartir_la_flicción_de_otro.jpg` | condolerse, compartir la flicción de otro | ñus pu’ch- | `LEXR-03690` |
| `diccionario_general/conejo.jpg` | conejo | cãjpy | `LEXR-01211` |
| `diccionario_general/conejo_(mamífero).jpg` | conejo (mamífero) | cãjpy | `LEXR-03641` |
| `diccionario_general/confesar_(al_cura).jpg` | confesar (al cura) | cmbeesáa- | `LEXR-03106` |
| `diccionario_general/confluencia_de_dos_ríos_o_quebradas.jpg` | confluencia de dos ríos o quebradas | yu’pcjacje (yu’peecjacje) | `LEXR-01958` |
| `diccionario_general/confrontar.jpg` | confrontar | iindyi’pu- | `LEXR-00883` |
| `diccionario_general/confundir,_perturbar.jpg` | confundir, perturbar | fiy vit- | `LEXR-02920` |
| `diccionario_general/congelarse.jpg` | congelarse | cuet yuu | `LEXR-03863` |
| `diccionario_general/conocimiento.jpg` | conocimiento | jiyuni | `LEXR-02887` |
| `diccionario_general/consolar.jpg` | consolar | cviisha’j-, cviisha’ja- | `LEXR-03903` |
| `diccionario_general/consolarse.jpg` | consolarse | quish-, quishi- | `LEXR-02495` |
| `diccionario_general/consolarse_(mutuamente).jpg` | consolarse (mutuamente) | puuty ya’cviisha’j-, puuty ya’cviisha’ja- | `LEXR-03520` |
| `diccionario_general/contagiarse.jpg` | contagiarse | neesu- | `LEXR-03566` |
| `diccionario_general/contagioso.jpg` | contagioso | niipeetjeesa | `LEXR-03025` |
| `diccionario_general/contaminar.jpg` | contaminar | pta’nzu’j-, pta’nzu’ju- | `LEXR-01878` |
| `diccionario_general/contar,_medir,_pesar.jpg` | contar, medir, pesar | isa- | `LEXR-02108` |
| `diccionario_general/contar,_relatar.jpg` | contar, relatar | cuentu’j-, cuentu’ju- | `LEXR-03312` |
| `diccionario_general/contentar.jpg` | contentar | caaiwecha’j-, caaiwecha’ja | `LEXR-00769` |
| `diccionario_general/contento.jpg` | contento | wechana | `LEXR-02186` |
| `diccionario_general/contestación.jpg` | contestación | pasni | `LEXR-02668` |
| `diccionario_general/contestar_(repetidas_veces).jpg` | contestar (repetidas veces) | pasu’s- | `LEXR-03480` |
| `diccionario_general/contigo,_con_usted.jpg` | contigo, con usted | indy yacj | `LEXR-01530` |
| `diccionario_general/conversación,_plática,_charla.jpg` | conversación, plática, charla | puuty we’weni | `LEXR-02762` |
| `diccionario_general/conversar,_charlar.jpg` | conversar, charlar | twẽeji- | `LEXR-01331` |
| `diccionario_general/convivir,_cohabitar.jpg` | convivir, cohabitar | ij fi’nze- | `LEXR-02483` |
| `diccionario_general/coral_(víbora).jpg` | coral (víbora) | ul bite | `LEXR-02721` |
| `diccionario_general/corar_(varias_cosas).jpg` | corar (varias cosas) | spẽ’tje’tj-, spẽ’tje’tje- | `LEXR-00452` |
| `diccionario_general/corazón_de_buey.jpg` | corazón de buey | us tandy | `LEXR-02287` |
| `diccionario_general/corcovear.jpg` | corcovear | vitu’tu- | `LEXR-01949` |
| `diccionario_general/corredor.jpg` | corredor | yat pwa’ | `LEXR-03703` |
| `diccionario_general/correr.jpg` | correr | wuwúu- | `LEXR-01016` |
| `diccionario_general/correr_brisa.jpg` | correr brisa | wejya’jya- | `LEXR-03349` |
| `diccionario_general/corriente_del_río_tendido.jpg` | corriente del río tendido | ejejme | `LEXR-02615` |
| `diccionario_general/cortar.jpg` | cortar | spẽ’tj-, spẽ’tje- | `LEXR-03300` |
| `diccionario_general/cortar_(en_muchos_pedazos).jpg` | cortar (en muchos pedazos) | wacaaga- | `LEXR-01493` |
| `diccionario_general/cortar_(en_varios_pedazos).jpg` | cortar (en varios pedazos) | twaaca’ca- | `LEXR-02135` |
| `diccionario_general/cortar,_trozar.jpg` | cortar, trozar | twajca-, twaaca- | `LEXR-03066` |
| `diccionario_general/cortarse.jpg` | cortarse | jypejcue- | `LEXR-01055` |
| `diccionario_general/cortarse_(a_sí_mismo).jpg` | cortarse (a sí mismo) | ya’spẽ’tj-, ya’spẽtje- | `LEXR-02508` |
| `diccionario_general/cortarse_(el_pelo).jpg` | cortarse (el pelo) | iiwajca-, iiwaaca- | `LEXR-03659` |
| `diccionario_general/corto.jpg` | corto | tuw | `LEXR-01624` |
| `diccionario_general/cosa_agradable.jpg` | cosa agradable | wẽt-sa | `LEXR-02975` |
| `diccionario_general/cosa_gruesa.jpg` | cosa gruesa | chalsa | `LEXR-01117` |
| `diccionario_general/cosa_usada,_no_nueva.jpg` | cosa usada, no nueva | tyachwe’sh | `LEXR-03347` |
| `diccionario_general/cosechar.jpg` | cosechar | undende- | `LEXR-00463` |
| `diccionario_general/coser,_costurar.jpg` | coser, costurar | cats-, catsu- | `LEXR-01650` |
| `diccionario_general/cosquillas.jpg` | cosquillas | ele | `LEXR-01526` |
| `diccionario_general/cosquilloso.jpg` | cosquilloso | yeletjẽ’j | `LEXR-03886` |
| `diccionario_general/costura.jpg` | costura | catsni | `LEXR-02360` |
| `diccionario_general/coyuntura_del_pie.jpg` | coyuntura del pie | chinda findy | `LEXR-02096` |
| `diccionario_general/crear_fama.jpg` | crear fama | tutje- | `LEXR-00650` |
| `diccionario_general/crecer.jpg` | crecer | waláa- | `LEXR-01891` |
| `diccionario_general/crecer_(el_monte).jpg` | crecer (el monte) | yu’cja- | `LEXR-03755` |
| `diccionario_general/creer.jpg` | creer | creĩ- | `LEXR-01045` |
| `diccionario_general/crespo.jpg` | crespo | shũ’sh | `LEXR-02549` |
| `diccionario_general/creyente,_que_confía_en_dios.jpg` | creyente, que confía en Dios | Dyusa’s yaacysa | `LEXR-03837` |
| `diccionario_general/criar_hijos.jpg` | criar hijos | nuytjẽ’j-, nuytjẽ’je- | `LEXR-02888` |
| `diccionario_general/criatura,_bebé.jpg` | criatura, bebé | luuch le’chcue | `LEXR-00978` |
| `diccionario_general/crin.jpg` | crin | jimba dycjas | `LEXR-02988` |
| `diccionario_general/crudo.jpg` | crudo | ĩquĩ | `LEXR-01183` |
| `diccionario_general/cruzar,_pasar_al_otro_lado.jpg` | cruzar, pasar al otro lado | ctejca-, cteega- | `LEXR-01129` |
| `diccionario_general/cráneo.jpg` | cráneo | jycuet dyi’tj | `LEXR-03407` |
| `diccionario_general/cual,_cualquier,_alguno.jpg` | cual, cualquier, alguno | maa | `LEXR-02619` |
| `diccionario_general/cualquiera.jpg` | cualquiera | maajy | `LEXR-02752` |
| `diccionario_general/cualquiera,_quienquiera.jpg` | cualquiera, quienquiera | maava | `LEXR-00892` |
| `diccionario_general/cuando.jpg` | cuando | bagach | `LEXR-01969` |
| `diccionario_general/cuando,_¿cuándo_,_¿a_qué_horas.jpg` | cuando, ¿cuándo?, ¿a qué horas? | ma’wẽn | `LEXR-00422` |
| `diccionario_general/cuandoquiera,_cualquier_hora.jpg` | cuandoquiera, cualquier hora | ma’wẽnva | `LEXR-01388` |
| `diccionario_general/cuandoquiera,_siempre.jpg` | cuandoquiera, siempre | bagachva, bagachteva | `LEXR-00385` |
| `diccionario_general/cuanto.jpg` | cuanto | manzcuẽ | `LEXR-02620` |
| `diccionario_general/cuanto_(distancia),_¿cuánto.jpg` | cuanto (distancia), ¿cuánto? | macjue | `LEXR-03053` |
| `diccionario_general/cuanto,_¿cuánto.jpg` | cuanto, ¿cuánto? | manz | `LEXR-02577` |
| `diccionario_general/cuartilla.jpg` | cuartilla | jimba chinda pẽty | `LEXR-01731` |
| `diccionario_general/cuarto.jpg` | cuarto | pajnztewe’sh | `LEXR-02215` |
| `diccionario_general/cuatro.jpg` | cuatro | pajnz | `LEXR-03181` |
| `diccionario_general/cubios.jpg` | cubios | pwel | `LEXR-01479` |
| `diccionario_general/cubrir,_tapar_(con_cobija).jpg` | cubrir, tapar (con cobija) | anz-, anzúu- | `LEXR-03553` |
| `diccionario_general/cubrirse_(ej._con_un_pañolón).jpg` | cubrirse (ej. con un pañolón) | ya’patj-, ya’patjée- | `LEXR-03687` |
| `diccionario_general/cucarrón.jpg` | cucarrón | ta’nda | `LEXR-01089` |
| `diccionario_general/cuchara.jpg` | cuchara | tucha’cy | `LEXR-00736` |
| `diccionario_general/cuchara_(hecha_de_calabaza).jpg` | cuchara (hecha de calabaza) | cunzha | `LEXR-03255` |
| `diccionario_general/cuenca_del_ojo.jpg` | cuenca del ojo | yafy dyi’tj | `LEXR-01894` |
| `diccionario_general/cuerno,_cacho.jpg` | cuerno, cacho | caachu | `LEXR-01029` |
| `diccionario_general/cuidar_de,_vigilar_(en_ausencia_del_dueño).jpg` | cuidar de, vigilar (en ausencia del dueño) | paatjeng-, paatjengu- | `LEXR-03479` |
| `diccionario_general/culpable.jpg` | culpable | yuuwesa | `LEXR-02833` |
| `diccionario_general/culpar,_juzgar.jpg` | culpar, juzgar | ucje’j-, ucje’je- | `LEXR-01626` |
| `diccionario_general/cumbrera_de_la_casa,_caballete.jpg` | cumbrera de la casa, caballete | yat cluu | `LEXR-03188` |
| `diccionario_general/cumplir,_llevar_a_cabo.jpg` | cumplir, llevar a cabo | cytey yuu- | `LEXR-02304` |
| `diccionario_general/curar,_dar_remedio,_medicinar.jpg` | curar, dar remedio, medicinar | yu’tse’j-, yu’tse’je- | `LEXR-01272` |
| `diccionario_general/curuba.jpg` | curuba | ñauñú | `LEXR-01502` |
| `diccionario_general/curíbano_(planta).jpg` | curíbano (planta) | daachajca | `LEXR-02306` |
| `diccionario_general/cuí,_conejillo_de_indias.jpg` | cuí, conejillo de indias | fitsj | `LEXR-02845` |
| `diccionario_general/cuñada_con_cuñada.jpg` | cuñada con cuñada | ptyi’nsa | `LEXR-00529` |
| `diccionario_general/cuñado_con_cuñada.jpg` | cuñado con cuñada | ptsu’wa | `LEXR-03387` |
| `diccionario_general/cuñado_con_cuñado.jpg` | cuñado con cuñado | ptsu’m | `LEXR-02007` |
| `diccionario_general/cámara_lateral_para_entierro.jpg` | cámara lateral para entierro | pumba’jni | `LEXR-00445` |
| `diccionario_general/cáscara_de_huevo.jpg` | cáscara de huevo | zits cja’ty | `LEXR-02143` |
| `diccionario_general/cóndor.jpg` | cóndor | cndul | `LEXR-01280` |
| `diccionario_general/danta.jpg` | danta | jimba cjũch | `LEXR-02575` |
| `diccionario_general/dar_a_la_hija_en_casamiento,_permitir_a_la_hija_casarse.jpg` | dar a la hija en casamiento, permitir a la hija casarse | caaimi’a’j-caaimi’aja-(cmi’a’j-) | `LEXR-03471` |
| `diccionario_general/dar_asco,_desagradar.jpg` | dar asco, desagradar | pyajtse-, pyaatse- | `LEXR-03459` |
| `diccionario_general/dar_ataque.jpg` | dar ataque | chavyuu- | `LEXR-03015` |
| `diccionario_general/dar_bofetadas.jpg` | dar bofetadas | petyaatya- | `LEXR-00904` |
| `diccionario_general/dar_calambre.jpg` | dar calambre | shaacãj u’j- | `LEXR-03893` |
| `diccionario_general/dar_de_beber.jpg` | dar de beber | yus-, yusu- | `LEXR-01430` |
| `diccionario_general/dar_de_beber_(a_varias_personas,_o_varias_veces).jpg` | dar de beber (a varias personas, o varias veces) | yusu’s- | `LEXR-02906` |
| `diccionario_general/dar_de_beber_(varias_veces).jpg` | dar de beber (varias veces) | yusuusu- | `LEXR-00757` |
| `diccionario_general/dar_fruto,_cargar.jpg` | dar fruto, cargar | ñun-, ñunu- (yũn-) | `LEXR-00759` |
| `diccionario_general/dar_hipo.jpg` | dar hipo | que’shi’j-, que’shi’ji- | `LEXR-02172` |
| `diccionario_general/dar_la_mano,_saludar.jpg` | dar la mano, saludar | cuse ũs- | `LEXR-03817` |
| `diccionario_general/dar_latigo.jpg` | dar latigo | ajwned- | `LEXR-01358` |
| `diccionario_general/dar_látigo.jpg` | dar látigo | pechujcue-, pechuucue- | `LEXR-02386` |
| `diccionario_general/dar_látigo_(repetidas_veces).jpg` | dar látigo (repetidas veces) | jwendu’ndu- | `LEXR-02815` |
| `diccionario_general/dar_paliza.jpg` | dar paliza | pãpa- | `LEXR-02171` |
| `diccionario_general/dar_paliza_(repetidas_veces).jpg` | dar paliza (repetidas veces) | pecue’cue- | `LEXR-01470` |
| `diccionario_general/dar_rabia.jpg` | dar rabia | pyũuscue- | `LEXR-01549` |
| `diccionario_general/dar_rejo,_castigar.jpg` | dar rejo, castigar | cja’tya’j-, cja’tya’ja- | `LEXR-01124` |
| `diccionario_general/dar_sed,_causar_sed.jpg` | dar sed, causar sed | cyũ’wẽ’j-, cyũ’wẽ’je- | `LEXR-01524` |
| `diccionario_general/dar_un_paso.jpg` | dar un paso | chavy-, chavi- | `LEXR-00490` |
| `diccionario_general/dar_varios_pasos.jpg` | dar varios pasos | chavi’vi- | `LEXR-01037` |
| `diccionario_general/dar_volteretas.jpg` | dar volteretas | teepjute- | `LEXR-01417` |
| `diccionario_general/dar_vuelta.jpg` | dar vuelta | ta’ngu- | `LEXR-03631` |
| `diccionario_general/dar_vuelta_alrededor_de.jpg` | dar vuelta alrededor de | jytandyi- | `LEXR-01056` |
| `diccionario_general/dar_vuelta,_girar.jpg` | dar vuelta, girar | tandy-. tandyíi- | `LEXR-00544` |
| `diccionario_general/darle_un_ataque.jpg` | darle un ataque | caywẽchpa’ja’j-, caywẽchpa’ja’ja- | `LEXR-03131` |
| `diccionario_general/darse_por_terminado_(un_pleito).jpg` | darse por terminado (un pleito) | yuwe ũchja- | `LEXR-03072` |
| `diccionario_general/darse,_producirse_(plantas).jpg` | darse, producirse (plantas) | tsut-, tsutu- | `LEXR-02503` |
| `diccionario_general/dañarse.jpg` | dañarse | swee- | `LEXR-03269` |
| `diccionario_general/de_abajo.jpg` | de abajo | susu | `LEXR-00733` |
| `diccionario_general/de_antemano.jpg` | de antemano | dyiicjẽy | `LEXR-03288` |
| `diccionario_general/de_aquí.jpg` | de aquí | ayjyu | `LEXR-02778` |
| `diccionario_general/de_arriba_para_abajo.jpg` | de arriba para abajo | caju, cajuy | `LEXR-00862` |
| `diccionario_general/de_donde,_¿de_dónde.jpg` | de donde, ¿de dónde? | mcaa (mgaa T) | `LEXR-03565` |
| `diccionario_general/de_dos_en_dos.jpg` | de dos en dos | e’nze’nz | `LEXR-02612` |
| `diccionario_general/de_la_misma_edad.jpg` | de la misma edad | ja’ndawe’sh | `LEXR-01990` |
| `diccionario_general/de_la_misma_tribu_páez.jpg` | de la misma tribu páez | nasa nwe’sh | `LEXR-03340` |
| `diccionario_general/de_lado,_al_soslayo.jpg` | de lado, al soslayo | putsu | `LEXR-00912` |
| `diccionario_general/de_mal_genio,_bravo.jpg` | de mal genio, bravo | weeswee | `LEXR-02640` |
| `diccionario_general/de_presto,_un_momento.jpg` | de presto, un momento | tundte (dundte) | `LEXR-03209` |
| `diccionario_general/de_un_lado_a_otro.jpg` | de un lado a otro | ẽeũy | `LEXR-01639` |
| `diccionario_general/de_una_vez,_directamente.jpg` | de una vez, directamente | tee jwend | `LEXR-02828` |
| `diccionario_general/decir_malas_palabras.jpg` | decir malas palabras | canzh we´we- | `LEXR-01974` |
| `diccionario_general/decolgar,_desengarzar.jpg` | decolgar, desengarzar | atsjunde- | `LEXR-01110` |
| `diccionario_general/defecar_(repetidas_veces).jpg` | defecar (repetidas veces) | ũchi’ch- | `LEXR-02089` |
| `diccionario_general/defecar,_cagar_(animales).jpg` | defecar, cagar (animales) | ũch-, ũchi- | `LEXR-03911` |
| `diccionario_general/defender,_amparar,_salvar.jpg` | defender, amparar, salvar | nwe’we- | `LEXR-00721` |
| `diccionario_general/defenderse.jpg` | defenderse | iindeewe- | `LEXR-03230` |
| `diccionario_general/deja_pasar_(al_través).jpg` | deja pasar (al través) | caycjẽuj-, caycjẽu´ju- | `LEXR-01975` |
| `diccionario_general/dejar_acompañar,_permitir_acompañar.jpg` | dejar acompañar, permitir acompañar | caapi’qui’j-, caapiqui’ji- | `LEXR-00389` |
| `diccionario_general/dejar_bajo_custodia_de_otro.jpg` | dejar bajo custodia de otro | caaiipe’je’j-, caaiipe’je’je | `LEXR-00860` |
| `diccionario_general/dejar_crecer_el_pelo.jpg` | dejar crecer el pelo | cjyu’ja’j-, cjyu’ja’ja- | `LEXR-03497` |
| `diccionario_general/dejar_fermentar.jpg` | dejar fermentar | cpuuse’j-, cpuuse’je- | `LEXR-02916` |
| `diccionario_general/dejar_hablar,_permitir_hablar.jpg` | dejar hablar, permitir hablar | cwe’we’j-, cwe’we’je- | `LEXR-03286` |
| `diccionario_general/dejar_hervir.jpg` | dejar hervir | caaclala’j-, caaclala’ja- | `LEXR-03075` |
| `diccionario_general/dejar_mojar.jpg` | dejar mojar | catu´j-, catu´ju- | `LEXR-00865` |
| `diccionario_general/dejar_pasar_(para_arriba).jpg` | dejar pasar (para arriba) | caacjẽu’j-, caacjẽuju- | `LEXR-01365` |
| `diccionario_general/dejar_pasar_más_tiempo.jpg` | dejar pasar más tiempo | caytjacue´j-, caytjacue’je- | `LEXR-01116` |
| `diccionario_general/dejar_pegar,_permitir_pegar.jpg` | dejar pegar, permitir pegar | cpeena’j-, cpeena’ja- | `LEXR-01717` |
| `diccionario_general/dejar_robar.jpg` | dejar robar | caapeswe’j-, caapeswe’je- | `LEXR-01648` |
| `diccionario_general/dejar_tocar,_permitir_tocar.jpg` | dejar tocar, permitir tocar | cuutsje’j-, cuutsje’je- | `LEXR-01596` |
| `diccionario_general/dejarse_alcanzar.jpg` | dejarse alcanzar | ya’cpajcy-, ya’cpaqui- | `LEXR-00470` |
| `diccionario_general/dejarse_coger.jpg` | dejarse coger | iiwe- | `LEXR-02574` |
| `diccionario_general/dejarse_engañar.jpg` | dejarse engañar | ya’gaña- | `LEXR-02902` |
| `diccionario_general/delgado.jpg` | delgado | pets | `LEXR-01874` |
| `diccionario_general/demorar.jpg` | demorar | iiẽepyãj-, iiẽepyãja- | `LEXR-02313` |
| `diccionario_general/demorar_(hasta_mediodía).jpg` | demorar (hasta mediodía) | yẽepyãj-, yẽepyãja- | `LEXR-00474` |
| `diccionario_general/demorar_(poco_tiempo).jpg` | demorar (poco tiempo) | tyacjji- | `LEXR-00653` |
| `diccionario_general/demostrar_sueño,_transnochar.jpg` | demostrar sueño, transnochar | deepang- | `LEXR-01287` |
| `diccionario_general/derecho,_recto.jpg` | derecho, recto | cu’le | `LEXR-02917` |
| `diccionario_general/derramar_(líquido).jpg` | derramar (líquido) | pcaw-, pcawu- | `LEXR-00725` |
| `diccionario_general/derramarse,_desbordarse.jpg` | derramarse, desbordarse | uwu- | `LEXR-02022` |
| `diccionario_general/derretirse.jpg` | derretirse | pquivy-, pquiivi- | `LEXR-01400` |
| `diccionario_general/derribar,_tumbar.jpg` | derribar, tumbar | pẽtyj-, pẽtyj- | `LEXR-01480` |
| `diccionario_general/desaparecer,_ocultarse.jpg` | desaparecer, ocultarse | paatsu-, paatsúu- | `LEXR-01745` |
| `diccionario_general/desarraigarse.jpg` | desarraigarse | a’mbate- | `LEXR-01640` |
| `diccionario_general/desatar.jpg` | desatar | cjimb-, cjimbu- | `LEXR-02097` |
| `diccionario_general/desatar_nudo.jpg` | desatar nudo | jyũcjwende- | `LEXR-03563` |
| `diccionario_general/desbaratar_(varias_cosas).jpg` | desbaratar (varias cosas) | cjimbtende- | `LEXR-03472` |
| `diccionario_general/descansar.jpg` | descansar | jycaase-, jycaasée- | `LEXR-00974` |
| `diccionario_general/descargarse,_librarse_de.jpg` | descargarse, librarse de | jycja’cunde- | `LEXR-00609` |
| `diccionario_general/descascarar.jpg` | descascarar | cupjy-, cupji- | `LEXR-02527` |
| `diccionario_general/descendiente.jpg` | descendiente | e’swe’sh | `LEXR-01658` |
| `diccionario_general/desclavar_(un_clavo),_desbotonar.jpg` | desclavar (un clavo), desbotonar | fyutstende- | `LEXR-01142` |
| `diccionario_general/desclavar,_desprenderse,_zafarse.jpg` | desclavar, desprenderse, zafarse | fyutsute- | `LEXR-01289` |
| `diccionario_general/descolgar_(varias_cosas),_quitar.jpg` | descolgar (varias cosas), quitar | cja’ctende- | `LEXR-03133` |
| `diccionario_general/descolgar,_quitar.jpg` | descolgar, quitar | cja’cjunde- | `LEXR-01369` |
| `diccionario_general/descolgarse,_librarse_de,_desechar_una_acusación.jpg` | descolgarse, librarse de, desechar una acusación | jycja’ctende- | `LEXR-01385` |
| `diccionario_general/desconocer.jpg` | desconocer | paanu- | `LEXR-02434` |
| `diccionario_general/desconocido.jpg` | desconocido | jiyunimeesa | `LEXR-00796` |
| `diccionario_general/descoser_(una_costura).jpg` | descoser (una costura) | catsunde- | `LEXR-03618` |
| `diccionario_general/descoser_(varias_costuras).jpg` | descoser (varias costuras) | catstende’ | `LEXR-01651` |
| `diccionario_general/descoyuntar.jpg` | descoyuntar | fillute- | `LEXR-02957` |
| `diccionario_general/descoyuntar,_dislocar.jpg` | descoyuntar, dislocar | pang-, pangúu- | `LEXR-02792` |
| `diccionario_general/descoyuntarse.jpg` | descoyuntarse | fillunde- | `LEXR-02310` |
| `diccionario_general/descuido.jpg` | descuido | jypa’yajcynimée | `LEXR-02162` |
| `diccionario_general/desde_la_niñez.jpg` | desde la niñez | luuchíi | `LEXR-01297` |
| `diccionario_general/desde,_de_donde.jpg` | desde, de donde | majũ | `LEXR-03866` |
| `diccionario_general/desear.jpg` | desear | jytjãas-, jytjãasu- | `LEXR-03540` |
| `diccionario_general/desenfundar_(machete),_dar_a_luz.jpg` | desenfundar (machete), dar a luz | jycuutyi’j-, jycuutyi’ji-(jycuutyi’j-T) | `LEXR-01865` |
| `diccionario_general/desenredar.jpg` | desenredar | jwendtunde- | `LEXR-03113` |
| `diccionario_general/desenvolver.jpg` | desenvolver | andtende- | `LEXR-01580` |
| `diccionario_general/desenvuelto.jpg` | desenvuelto | yapundeni | `LEXR-01953` |
| `diccionario_general/deseo,_voluntad.jpg` | deseo, voluntad | tjãasni | `LEXR-01558` |
| `diccionario_general/desgajar.jpg` | desgajar | shpijnde-, shpinde- (shapijnde-) | `LEXR-03649` |
| `diccionario_general/desgajar_(varias_veces_o_varias_ramas).jpg` | desgajar (varias veces o varias ramas) | shpindende- | `LEXR-02766` |
| `diccionario_general/desgajarse,_desprenderse.jpg` | desgajarse, desprenderse | shpite- (shapite) | `LEXR-03572` |
| `diccionario_general/desgarjarse,_desprenderse.jpg` | desgarjarse, desprenderse | shpite’te- | `LEXR-02335` |
| `diccionario_general/desgarrar_(varias_tiras).jpg` | desgarrar (varias tiras) | shũ’tene- | `LEXR-02065` |
| `diccionario_general/desgarrarse_(en_varias_partes).jpg` | desgarrarse (en varias partes) | shũ’tete- | `LEXR-02398` |
| `diccionario_general/desgranar.jpg` | desgranar | cjaavi’j-, cjaavi’ji- | `LEXR-03599` |
| `diccionario_general/desgranar,_cosechar.jpg` | desgranar, cosechar | shande- | `LEXR-03483` |
| `diccionario_general/deshincharse.jpg` | deshincharse | cpate- | `LEXR-03744` |
| `diccionario_general/deshojar.jpg` | deshojar | ãtsja- | `LEXR-02737` |
| `diccionario_general/deshojar_(maíz).jpg` | deshojar (maíz) | fycaach–, fycaachi- | `LEXR-02573` |
| `diccionario_general/desmenuzar,_hacer_polvo_de.jpg` | desmenuzar, hacer polvo de | muuse’j-, muuse’je- | `LEXR-03504` |
| `diccionario_general/desmoronar.jpg` | desmoronar | cu’ch-, cu’chi- | `LEXR-03833` |
| `diccionario_general/desnudarse,_desvestirse.jpg` | desnudarse, desvestirse | sũpy-, sũpíi- | `LEXR-00997` |
| `diccionario_general/desnudo,_pelado.jpg` | desnudo, pelado | sũpy | `LEXR-02588` |
| `diccionario_general/despajar.jpg` | despajar | spjamb-, spjaambu- | `LEXR-03266` |
| `diccionario_general/despedazarse_(en_varias_partes).jpg` | despedazarse (en varias partes) | shateete- | `LEXR-03122` |
| `diccionario_general/despegar,_quitar_coas_pegada.jpg` | despegar, quitar coas pegada | chaquijnde-, chaquinde- | `LEXR-03788` |
| `diccionario_general/despertar.jpg` | despertar | yajcy-, yaaqui-, yaacy- | `LEXR-02142` |
| `diccionario_general/despertar_(a_otro).jpg` | despertar (a otro) | fĩtyj-, fĩtyji- | `LEXR-02985` |
| `diccionario_general/desplomarse,_tambalear.jpg` | desplomarse, tambalear | atscue- | `LEXR-01582` |
| `diccionario_general/desplumar.jpg` | desplumar | cjas ujnde- | `LEXR-00496` |
| `diccionario_general/despreciado,_odiado.jpg` | despreciado, odiado | atseni | `LEXR-02600` |
| `diccionario_general/despreciar.jpg` | despreciar | atseyajcy- | `LEXR-00677` |
| `diccionario_general/despreciar,_odiar.jpg` | despreciar, odiar | ajtse-, atse- | `LEXR-03190` |
| `diccionario_general/despreciarse_(mutuamente).jpg` | despreciarse (mutuamente) | puuty yaatse- | `LEXR-03761` |
| `diccionario_general/desprecio.jpg` | desprecio | ajtsajtse | `LEXR-03552` |
| `diccionario_general/desprender.jpg` | desprender | cja’tyinde- | `LEXR-00495` |
| `diccionario_general/desprenderse.jpg` | desprenderse | cja’tyite- | `LEXR-00689` |
| `diccionario_general/después_(posterioridad_de_tiempo).jpg` | después (posterioridad de tiempo) | e’su | `LEXR-02613` |
| `diccionario_general/destetar.jpg` | destetar | chu’ch tyujnde- | `LEXR-00688` |
| `diccionario_general/destructivo.jpg` | destructivo | pembasá | `LEXR-01748` |
| `diccionario_general/desvelar,_no_dejar_dormir.jpg` | desvelar, no dejar dormir | cdeeje’jmée- | `LEXR-01035` |
| `diccionario_general/detener,_retener.jpg` | detener, retener | newe- (neewe-) | `LEXR-01871` |
| `diccionario_general/deudor.jpg` | deudor | yulsá (yulusá) | `LEXR-01022` |
| `diccionario_general/devolver.jpg` | devolver | caashwendu’j-, caashwendu’ju- | `LEXR-02604` |
| `diccionario_general/dibujo.jpg` | dibujo | piisani | `LEXR-02329` |
| `diccionario_general/dibujo_que_usan_para_el_chumbe.jpg` | dibujo que usan para el chumbe | unzafy (J) | `LEXR-01688` |
| `diccionario_general/dicho.jpg` | dicho | jĩni | `LEXR-01057` |
| `diccionario_general/diente_delantero.jpg` | diente delantero | qui’tj vits | `LEXR-02764` |
| `diccionario_general/diez.jpg` | diez | csemba | `LEXR-01592` |
| `diccionario_general/dificultad.jpg` | dificultad | tjẽysa | `LEXR-00647` |
| `diccionario_general/difunto,_a.jpg` | difunto, a | uunsá | `LEXR-02457` |
| `diccionario_general/difícil.jpg` | difícil | tjẽy | `LEXR-02972` |
| `diccionario_general/dios.jpg` | Dios | dyus | `LEXR-03175` |
| `diccionario_general/disfrazarse_(pintar_la_cara).jpg` | disfrazarse (pintar la cara) | taachin yuu- | `LEXR-02551` |
| `diccionario_general/disgustarse.jpg` | disgustarse | yajtse- | `LEXR-03577` |
| `diccionario_general/disminuir.jpg` | disminuir | ũuchi- | `LEXR-00672` |
| `diccionario_general/distinto,_diferente,_extraño.jpg` | distinto, diferente, extraño | fiy | `LEXR-01216` |
| `diccionario_general/dividirse,_separarse,_bifurcarse.jpg` | dividirse, separarse, bifurcarse | ptyute-, ptyutée- | `LEXR-01547` |
| `diccionario_general/divulgar.jpg` | divulgar | tuutje’j-, tuutje’je- | `LEXR-00457` |
| `diccionario_general/dizque.jpg` | dizque | pã’ | `LEXR-02440` |
| `diccionario_general/doblar.jpg` | doblar | tpejng-, tpengu- | `LEXR-03391` |
| `diccionario_general/doblar,_encorvar_(repetidas_veces).jpg` | doblar, encorvar (repetidas veces) | tpengu’ngu- | `LEXR-02940` |
| `diccionario_general/doler.jpg` | doler | aca pa’j- | `LEXR-02032` |
| `diccionario_general/donde,_adonde,_¿dónde_¿adónde.jpg` | donde, adonde, ¿dónde? ¿adónde? | mtee (mdee T) | `LEXR-00428` |
| `diccionario_general/donde,_¿de_dónde_(para_abajo),_¿por_dónde.jpg` | donde, ¿de dónde? (para abajo), ¿por dónde? | msuu | `LEXR-03589` |
| `diccionario_general/dondequiera.jpg` | dondequiera | mteeva | `LEXR-00612` |
| `diccionario_general/dorarse.jpg` | dorarse | wat-, watúu- | `LEXR-01425` |
| `diccionario_general/dormilón.jpg` | dormilón | denzh | `LEXR-00410` |
| `diccionario_general/dormir,_acostarse.jpg` | dormir, acostarse | dej-, deje-, dee- | `LEXR-00598` |
| `diccionario_general/dorotea_(ave).jpg` | dorotea (ave) | chulfity | `LEXR-02982` |
| `diccionario_general/dos.jpg` | dos | e’nz | `LEXR-01451` |
| `diccionario_general/dueño_de_la_casa.jpg` | dueño de la casa | yat namu | `LEXR-01769` |
| `diccionario_general/dulce_(sabor).jpg` | dulce (sabor) | ñusha | `LEXR-01350` |
| `diccionario_general/durar.jpg` | durar | tjẽeyũu- | `LEXR-03547` |
| `diccionario_general/duro_(sonido).jpg` | duro (sonido) | sus | `LEXR-02399` |
| `diccionario_general/débil.jpg` | débil | chjãchjamée | `LEXR-01977` |
| `diccionario_general/días_hábiles.jpg` | días hábiles | mjĩi en | `LEXR-02990` |
| `diccionario_general/echado_boca_abajp,_postrado.jpg` | echado boca abajp, postrado | peecytuty | `LEXR-03892` |
| `diccionario_general/echar_(líquido_en_varias_ollas).jpg` | echar (líquido en varias ollas) | awu’w | `LEXR-00944` |
| `diccionario_general/echar_(líquido).jpg` | echar (líquido) | aw-, awu- | `LEXR-00384` |
| `diccionario_general/echar_(varias_veces_o_varias_cosas.jpg` | echar (varias veces o varias cosas | ambu’mbu- | `LEXR-02691` |
| `diccionario_general/echar_agua_(ej._en_el_bautismo).jpg` | echar agua (ej. en el bautismo) | peeawu- | `LEXR-02929` |
| `diccionario_general/echar_en.jpg` | echar en | yu’amb-, yu’ambu- | `LEXR-03189` |
| `diccionario_general/echar_espigas_(maíz),_salir_la_espiga.jpg` | echar espigas (maíz), salir la espiga | viits-, viitsu- | `LEXR-02405` |
| `diccionario_general/echar_fuera,_ahuyentar.jpg` | echar fuera, ahuyentar | neeúu- | `LEXR-00617` |
| `diccionario_general/echar_grano,_cargar.jpg` | echar grano, cargar | ñiñ acj- | `LEXR-01503` |
| `diccionario_general/echar_granos,_apuntar.jpg` | echar granos, apuntar | ãsh-, ãshi- | `LEXR-01500` |
| `diccionario_general/echar_hojas.jpg` | echar hojas | yeets-, yeetsu- | `LEXR-02347` |
| `diccionario_general/echar_humo,_evaporar,_quemar_incienso.jpg` | echar humo, evaporar, quemar incienso | cshi’ta’j-, cshi’ta’ja- | `LEXR-03431` |
| `diccionario_general/echar_la_culpa,_juzgar.jpg` | echar la culpa, juzgar | yuwe ucje’j- | `LEXR-03923` |
| `diccionario_general/echar_los_cimientos_(al_edificar_una_casa).jpg` | echar los cimientos (al edificar una casa) | caachinda’j-, caachinda’ja- | `LEXR-02358` |
| `diccionario_general/echar_mano_a.jpg` | echar mano a | cuse caaj- | `LEXR-02424` |
| `diccionario_general/echar_suertes.jpg` | echar suertes | suerte caaj- | `LEXR-01088` |
| `diccionario_general/echar_una_clueca.jpg` | echar una clueca | cã’pji’j-, cãpj’ji- | `LEXR-03561` |
| `diccionario_general/echarse_(gallina),_empollar.jpg` | echarse (gallina), empollar | ã’pjy-, ã’pji- | `LEXR-02292` |
| `diccionario_general/econtrarse_con_otro_que_viene_de_rumbo_opuesto_y_seguir_adelante.jpg` | econtrarse con otro que viene de rumbo opuesto y seguir adelante | pu’jycjẽw-, pu’jycjẽúu- | `LEXR-02857` |
| `diccionario_general/ehcar_(granos).jpg` | ehcar (granos) | amb-, ambu- | `LEXR-00766` |
| `diccionario_general/el_abdomen.jpg` | el abdomen | tutyj letya | `LEXR-03243` |
| `diccionario_general/el_abejorro,_abejón_(insecto).jpg` | el abejorro, abejón (insecto) | wãwã | `LEXR-02831` |
| `diccionario_general/el_abono.jpg` | el abono | shacue | `LEXR-02585` |
| `diccionario_general/el_abuelo.jpg` | el abuelo | niish, niishi | `LEXR-01800` |
| `diccionario_general/el_abuelo,_bisabuelo.jpg` | el abuelo, bisabuelo | papa wala | `LEXR-01238` |
| `diccionario_general/el_aguacate_(fruto).jpg` | el aguacate (fruto) | ujtse | `LEXR-02554` |
| `diccionario_general/el_aguardiente.jpg` | el aguardiente | wallinde (wellinda) | `LEXR-02289` |
| `diccionario_general/el_agüinche.jpg` | el agüinche | jweenzh | `LEXR-03177` |
| `diccionario_general/el_ahijado.jpg` | el ahijado | cjalu | `LEXR-00399` |
| `diccionario_general/el_ajo.jpg` | el ajo | acjus | `LEXR-03723` |
| `diccionario_general/el_ají_(planta,_usada_como_condimento).jpg` | el ají (planta, usada como condimento) | ãwã | `LEXR-03721` |
| `diccionario_general/el_ají_picante_(planta,_usada_como_condimento).jpg` | el ají picante (planta, usada como condimento) | ãwã pijts | `LEXR-01501` |
| `diccionario_general/el_ají_pimentón_(planta,_usada_como_condimento).jpg` | el ají pimentón (planta, usada como condimento) | ãwã penzh | `LEXR-03826` |
| `diccionario_general/el_ala.jpg` | el ala | fyu cu’ta (jyu cu’ta) | `LEXR-03050` |
| `diccionario_general/el_alacrán_(arácnido_venenoso).jpg` | el alacrán (arácnido venenoso) | usmity | `LEXR-01690` |
| `diccionario_general/el_alfarero.jpg` | el alfarero | mityj umsá | `LEXR-00716` |
| `diccionario_general/el_algodón.jpg` | el algodón | wawa | `LEXR-01175` |
| `diccionario_general/el_alguacil.jpg` | el alguacil | luasil | `LEXR-03853` |
| `diccionario_general/el_aliso_(árbol).jpg` | el aliso (árbol) | pinzú | `LEXR-02712` |
| `diccionario_general/el_almud.jpg` | el almud | almun | `LEXR-01903` |
| `diccionario_general/el_amero_(envoltura_de_maíz).jpg` | el amero (envoltura de maíz) | fycach | `LEXR-02616` |
| `diccionario_general/el_amigo.jpg` | el amigo | namicu | `LEXR-02962` |
| `diccionario_general/el_anaco_(de_lana).jpg` | el anaco (de lana) | atyj tul | `LEXR-03845` |
| `diccionario_general/el_andamio.jpg` | el andamio | bush | `LEXR-02980` |
| `diccionario_general/el_animal.jpg` | el animal | niimal | `LEXR-03143` |
| `diccionario_general/el_antebrazo.jpg` | el antebrazo | cuse pil | `LEXR-02474` |
| `diccionario_general/el_apodo.jpg` | el apodo | shaacue yasa | `LEXR-01319` |
| `diccionario_general/el_arbusto.jpg` | el arbusto | ẽjyã | `LEXR-02978` |
| `diccionario_general/el_arco_iris.jpg` | el arco iris | cytũus | `LEXR-01137` |
| `diccionario_general/el_arco,_de_forma_arqueda.jpg` | el arco, de forma arqueda | taty | `LEXR-03064` |
| `diccionario_general/el_armadillo_(mamífero).jpg` | el armadillo (mamífero) | shita | `LEXR-02765` |
| `diccionario_general/el_arrayán_(árbol).jpg` | el arrayán (árbol) | tyjĩ’te | `LEXR-03417` |
| `diccionario_general/el_arroz.jpg` | el arroz | luus | `LEXR-00803` |
| `diccionario_general/el_ascua,_carbón_encendido.jpg` | el ascua, carbón encendido | ipy ñiñ | `LEXR-01794` |
| `diccionario_general/el_asiento.jpg` | el asiento | cachni | `LEXR-00952` |
| `diccionario_general/el_asno_(mamífero).jpg` | el asno (mamífero) | ashnu | `LEXR-02599` |
| `diccionario_general/el_ataúd.jpg` | el ataúd | taúl | `LEXR-03804` |
| `diccionario_general/el_ayudante,_que_ayuda.jpg` | el ayudante, que ayuda | pu’chsa | `LEXR-02673` |
| `diccionario_general/el_ayudante,_que_ayudará.jpg` | el ayudante, que ayudará | pu’chwa’jsa | `LEXR-02546` |
| `diccionario_general/el_ayuno.jpg` | el ayuno | yũunani | `LEXR-03371` |
| `diccionario_general/el_año.jpg` | el año | añu | `LEXR-03074` |
| `diccionario_general/el_año_pasado.jpg` | el año pasado | jũ’na añu | `LEXR-01534` |
| `diccionario_general/el_baile.jpg` | el baile | cu’ju | `LEXR-03109` |
| `diccionario_general/el_barro,_lodo.jpg` | el barro, lodo | tyity | `LEXR-03210` |
| `diccionario_general/el_bimbo,_pisco,_pavo_común_(ave).jpg` | el bimbo, pisco, pavo común (ave) | shpiipí | `LEXR-02013` |
| `diccionario_general/el_blanco_(de_raza_blanca).jpg` | el blanco (de raza blanca) | chijme | `LEXR-03283` |
| `diccionario_general/el_bordón.jpg` | el bordón | fytũu vica | `LEXR-02959` |
| `diccionario_general/el_borracho.jpg` | el borracho | tũusá | `LEXR-01490` |
| `diccionario_general/el_brujo,_hechicero.jpg` | el brujo, hechicero | dyijy, dyijy yuusá | `LEXR-02308` |
| `diccionario_general/el_bulto.jpg` | el bulto | tamby | `LEXR-03186` |
| `diccionario_general/el_búho,_la_lechuza_(ave).jpg` | el búho, la lechuza (ave) | tyi’fy | `LEXR-03511` |
| `diccionario_general/el_caballo.jpg` | el caballo | jimba | `LEXR-02702` |
| `diccionario_general/el_cadáver.jpg` | el cadáver | cacue cja’ty | `LEXR-03654` |
| `diccionario_general/el_café.jpg` | el café | cafe | `LEXR-01202` |
| `diccionario_general/el_calabazo_(para_líquidos).jpg` | el calabazo (para líquidos) | squijw tuca | `LEXR-03736` |
| `diccionario_general/el_calabazo,_la_vasija_rústica,_totuma.jpg` | el calabazo, la vasija rústica, totuma | tuca | `LEXR-01170` |
| `diccionario_general/el_calcañar,_el_talón.jpg` | el calcañar, el talón | chinda tã’sh | `LEXR-02741` |
| `diccionario_general/el_calcañar,_talón.jpg` | el calcañar, talón | tã’sh | `LEXR-03765` |
| `diccionario_general/el_caldo,_la_sopa.jpg` | el caldo, la sopa | cujya | `LEXR-01657` |
| `diccionario_general/el_camino.jpg` | el camino | dyi’j | `LEXR-03336` |
| `diccionario_general/el_canasto,_cesto.jpg` | el canasto, cesto | cash | `LEXR-02153` |
| `diccionario_general/el_cangrejo_(crustáceo).jpg` | el cangrejo (crustáceo) | wãca | `LEXR-00663` |
| `diccionario_general/el_cangrejo,_alacrán_(arácnido).jpg` | el cangrejo, alacrán (arácnido) | menz shã’py | `LEXR-03261` |
| `diccionario_general/el_canto,_la_canción.jpg` | el canto, la canción | mem | `LEXR-02622` |
| `diccionario_general/el_capitán.jpg` | el capitán | cpiitan | `LEXR-02570` |
| `diccionario_general/el_caracol.jpg` | el caracol | shape | `LEXR-03630` |
| `diccionario_general/el_carate_(especie_de_sarna).jpg` | el carate (especie de sarna) | claatyi | `LEXR-01591` |
| `diccionario_general/el_cardo_(planta).jpg` | el cardo (planta) | shic | `LEXR-02587` |
| `diccionario_general/el_carpintero.jpg` | el carpintero | ũ’tsjsa | `LEXR-02875` |
| `diccionario_general/el_carpintero_(ave).jpg` | el carpintero (ave) | fytũu pagayú | `LEXR-01456` |
| `diccionario_general/el_carrete_de_barro_para_asentar_olla.jpg` | el carrete de barro para asentar olla | a’ch | `LEXR-00382` |
| `diccionario_general/el_carrizo.jpg` | el carrizo | pel | `LEXR-01931` |
| `diccionario_general/el_carrizo_(sirve_para_flauta).jpg` | el carrizo (sirve para flauta) | jaw | `LEXR-03789` |
| `diccionario_general/el_carángano_(insecto).jpg` | el carángano (insecto) | chuwatyj | `LEXR-03333` |
| `diccionario_general/el_caserío,_pueblo,_poblado.jpg` | el caserío, pueblo, poblado | chjamb | `LEXR-00686` |
| `diccionario_general/el_castellano,_español_(idioma).jpg` | el castellano, español (idioma) | wagás yuwe | `LEXR-02024` |
| `diccionario_general/el_caudal,_corriente_del_rió.jpg` | el caudal, corriente del rió | yu’cãchã | `LEXR-00666` |
| `diccionario_general/el_cañaduzal.jpg` | el cañaduzal | cjĩij ej | `LEXR-00592` |
| `diccionario_general/el_cañuto.jpg` | el cañuto | patj | `LEXR-02855` |
| `diccionario_general/el_cedro_(árbol).jpg` | el cedro (árbol) | setlu | `LEXR-01082` |
| `diccionario_general/el_cerro.jpg` | el cerro | tjã’j | `LEXR-03324` |
| `diccionario_general/el_charco,_lago.jpg` | el charco, lago | ĩcj | `LEXR-03250` |
| `diccionario_general/el_chicao_(ave_amarillo).jpg` | el chicao (ave amarillo) | shquiicy | `LEXR-03298` |
| `diccionario_general/el_chiguaco_(ave).jpg` | el chiguaco (ave) | slluj | `LEXR-02892` |
| `diccionario_general/el_choclo,_mazorca_de_maíz_tierno.jpg` | el choclo, mazorca de maíz tierno | tsut | `LEXR-01001` |
| `diccionario_general/el_chorrizo.jpg` | el chorrizo | jemb | `LEXR-00972` |
| `diccionario_general/el_cielo.jpg` | el cielo | cielu | `LEXR-01123` |
| `diccionario_general/el_ciempiés.jpg` | el ciempiés | ultũpy | `LEXR-00560` |
| `diccionario_general/el_ciempiés_(miriápodo).jpg` | el ciempiés (miriápodo) | tupil | `LEXR-02553` |
| `diccionario_general/el_cinturón,_la_correa.jpg` | el cinturón, la correa | corea | `LEXR-00959` |
| `diccionario_general/el_cohete.jpg` | el cohete | cwẽetes | `LEXR-02099` |
| `diccionario_general/el_col,_repollo_(planta_comestible).jpg` | el col, repollo (planta comestible) | tyjã’ | `LEXR-02238` |
| `diccionario_general/el_colmillo.jpg` | el colmillo | efy | `LEXR-02919` |
| `diccionario_general/el_comején.jpg` | el comején | fytũu ũ’sa cjã’cjã | `LEXR-01048` |
| `diccionario_general/el_comején_(insecto).jpg` | el comején (insecto) | fytũu wes | `LEXR-02481` |
| `diccionario_general/el_compadre.jpg` | el compadre | cmbale | `LEXR-03285` |
| `diccionario_general/el_compañero,_la_compañera.jpg` | el compañero, la compañera | pi’qui | `LEXR-00630` |
| `diccionario_general/el_concuñado.jpg` | el concuñado | pits pyacj | `LEXR-03386` |
| `diccionario_general/el_consejero,_que_aconseja.jpg` | el consejero, que aconseja | yu’cypeesa | `LEXR-03899` |
| `diccionario_general/el_consejo.jpg` | el consejo | yu’cypeeni | `LEXR-03215` |
| `diccionario_general/el_cordón_umbilical.jpg` | el cordón umbilical | shamb wes | `LEXR-02935` |
| `diccionario_general/el_cordón,_látigo.jpg` | el cordón, látigo | chu’nzhu | `LEXR-00492` |
| `diccionario_general/el_corral.jpg` | el corral | cyuupjni | `LEXR-00409` |
| `diccionario_general/el_corral_de_ovejas.jpg` | el corral de ovejas | piisháa cyuupjni | `LEXR-02218` |
| `diccionario_general/el_corredor_(de_la_casa).jpg` | el corredor (de la casa) | cneetul (T) | `LEXR-02841` |
| `diccionario_general/el_corredor_(de_la_casa),_sitio_cubierto.jpg` | el corredor (de la casa), sitio cubierto | pwa’ | `LEXR-01477` |
| `diccionario_general/el_costal.jpg` | el costal | custal | `LEXR-02918` |
| `diccionario_general/el_coto,_bocio.jpg` | el coto, bocio | pẽty shiwa | `LEXR-00534` |
| `diccionario_general/el_creador.jpg` | el creador | taqui’sa | `LEXR-03442` |
| `diccionario_general/el_cucarachero_(ave).jpg` | el cucarachero (ave) | meechica | `LEXR-01920` |
| `diccionario_general/el_cucarrón,_escarabajo_(insecto).jpg` | el cucarrón, escarabajo (insecto) | ta’nda | `LEXR-02589` |
| `diccionario_general/el_cucharón_(de_madera).jpg` | el cucharón (de madera) | ejwa | `LEXR-01452` |
| `diccionario_general/el_cuchillo.jpg` | el cuchillo | cchill (chill) | `LEXR-02038` |
| `diccionario_general/el_cuerpo.jpg` | el cuerpo | cacue (cuacue T) | `LEXR-00771` |
| `diccionario_general/el_culantro_(planta).jpg` | el culantro (planta) | me’sucue | `LEXR-00424` |
| `diccionario_general/el_cura,_sacerdote.jpg` | el cura, sacerdote | pal | `LEXR-00436` |
| `diccionario_general/el_curandero.jpg` | el curandero | tjẽ’j yu’tsesa | `LEXR-02502` |
| `diccionario_general/el_curandero,_hechicero.jpg` | el curandero, hechicero | pilwe’sh | `LEXR-03682` |
| `diccionario_general/el_curíbano_(planta_medicinal).jpg` | el curíbano (planta medicinal) | ulñiñ | `LEXR-03001` |
| `diccionario_general/el_cusumbe,_coatí_(mamífero).jpg` | el cusumbe, coatí (mamífero) | cãtsa | `LEXR-02657` |
| `diccionario_general/el_cuí,_conejillo_de_indias_(mamífero).jpg` | el cuí, conejillo de indias (mamífero) | fitsj | `LEXR-01455` |
| `diccionario_general/el_cuñado_(entre_hombres).jpg` | el cuñado (entre hombres) | ntsu’m | `LEXR-00618` |
| `diccionario_general/el_cuñado,_la_cuñada_(entre_los_dos_sexos).jpg` | el cuñado, la cuñada (entre los dos sexos) | ntsu’wa | `LEXR-01541` |
| `diccionario_general/el_cántaro.jpg` | el cántaro | yu’mityj | `LEXR-01343` |
| `diccionario_general/el_dedo.jpg` | el dedo | cuse mush | `LEXR-01521` |
| `diccionario_general/el_dedo_cordial_o_de_en_medio.jpg` | el dedo cordial o de en medio | cuse ũus | `LEXR-03601` |
| `diccionario_general/el_dedo_del_pie.jpg` | el dedo del pie | chinda vyllill | `LEXR-03042` |
| `diccionario_general/el_desfiladero.jpg` | el desfiladero | tcafy | `LEXR-03323` |
| `diccionario_general/el_diablo.jpg` | el diablo | echtjẽ’j | `LEXR-03337` |
| `diccionario_general/el_diente.jpg` | el diente | qui’tj | `LEXR-02010` |
| `diccionario_general/el_diluvio.jpg` | el diluvio | nus pa’jni ĩcj | `LEXR-01467` |
| `diccionario_general/el_dinero,_la_plata,_moneda.jpg` | el dinero, la plata, moneda | vyu | `LEXR-00562` |
| `diccionario_general/el_dolor.jpg` | el dolor | aca | `LEXR-02650` |
| `diccionario_general/el_domingo.jpg` | el domingo | qui’sen | `LEXR-02630` |
| `diccionario_general/el_dormilón_(ave_nocturna).jpg` | el dormilón (ave nocturna) | tsũvy | `LEXR-00552` |
| `diccionario_general/el_dueño,_la_dueña.jpg` | el dueño, la dueña | namu | `LEXR-01922` |
| `diccionario_general/el_durazno_(fruta).jpg` | el durazno (fruta) | lashnu | `LEXR-02535` |
| `diccionario_general/el_día,_tiempo.jpg` | el día, tiempo | en | `LEXR-03452` |
| `diccionario_general/el_empeine.jpg` | el empeine | chinda pẽtyj | `LEXR-02155` |
| `diccionario_general/el_encenillo_(árbol,_usado_para_leña).jpg` | el encenillo (árbol, usado para leña) | tsute | `LEXR-01759` |
| `diccionario_general/el_enemigo.jpg` | el enemigo | iipuiisa | `LEXR-01529` |
| `diccionario_general/el_enfermo,_el_paciente.jpg` | el enfermo, el paciente | ãtsã’sa | `LEXR-02772` |
| `diccionario_general/el_enojo,_la_ira.jpg` | el enojo, la ira | ũuschaani | `LEXR-03423` |
| `diccionario_general/el_enrizo,_puerco_espín_(mamífero).jpg` | el enrizo, puerco espín (mamífero) | tjuw | `LEXR-02767` |
| `diccionario_general/el_escoplo_(herramienta).jpg` | el escoplo (herramienta) | chang | `LEXR-00396` |
| `diccionario_general/el_espejo.jpg` | el espejo | speeju | `LEXR-02014` |
| `diccionario_general/el_esposo,_marido.jpg` | el esposo, marido | nmi’ | `LEXR-01603` |
| `diccionario_general/el_esqueleto.jpg` | el esqueleto | dyi’tj sũpy | `LEXR-03047` |
| `diccionario_general/el_estómago,_la_barriga.jpg` | el estómago, la barriga | tutyj (tuts T) | `LEXR-02680` |
| `diccionario_general/el_esófago.jpg` | el esófago | cjẽendyi’j | `LEXR-00870` |
| `diccionario_general/el_extranjero.jpg` | el extranjero | ecajuwe’sh | `LEXR-02614` |
| `diccionario_general/el_extranjero,_forastero.jpg` | el extranjero, forastero | vite quiwejuwe’sh | `LEXR-01628` |
| `diccionario_general/el_filo.jpg` | el filo | zec | `LEXR-01701` |
| `diccionario_general/el_fiscal_(oficial).jpg` | el fiscal (oficial) | pescal | `LEXR-02327` |
| `diccionario_general/el_flautista.jpg` | el flautista | cuvyasa, cuvytewe’sh | `LEXR-03432` |
| `diccionario_general/el_fornicador.jpg` | el fornicador | pdeepits | `LEXR-03569` |
| `diccionario_general/el_frendo.jpg` | el frendo | plenu | `LEXR-01810` |
| `diccionario_general/el_fríjol.jpg` | el fríjol | us | `LEXR-00744` |
| `diccionario_general/el_fuete.jpg` | el fuete | yaatul | `LEXR-02733` |
| `diccionario_general/el_gallinazo,_galembo_(ave).jpg` | el gallinazo, galembo (ave) | mẽewẽjy | `LEXR-01229` |
| `diccionario_general/el_gallo.jpg` | el gallo | atall pits | `LEXR-03008` |
| `diccionario_general/el_garabato.jpg` | el garabato | claapatu | `LEXR-01443` |
| `diccionario_general/el_gavilán_(ave).jpg` | el gavilán (ave) | tsalli’ll | `LEXR-02016` |
| `diccionario_general/el_gobernador_(del_resguardo).jpg` | el gobernador (del resguardo) | ne’jue’sh | `LEXR-01538` |
| `diccionario_general/el_gobernante,_mandatario.jpg` | el gobernante, mandatario | jycaasa | `LEXR-00709` |
| `diccionario_general/el_gorgojo_(insecto).jpg` | el gorgojo (insecto) | chica | `LEXR-00685` |
| `diccionario_general/el_gorrion.jpg` | el gorrion | tyuj | `LEXR-02863` |
| `diccionario_general/el_granizo.jpg` | el granizo | cuetumba | `LEXR-03834` |
| `diccionario_general/el_grano,_la_pepita.jpg` | el grano, la pepita | ñiñ | `LEXR-02087` |
| `diccionario_general/el_grillo_(insecto).jpg` | el grillo (insecto) | cjã’sh | `LEXR-02882` |
| `diccionario_general/el_guarapo,_chicha_de_caña_de_azúcar.jpg` | el guarapo, chicha de caña de azúcar | ñusha beca | `LEXR-01635` |
| `diccionario_general/el_guerrillero.jpg` | el guerrillero | yu’cj nasa | `LEXR-00472` |
| `diccionario_general/el_guineo_(especie_de_plátano_pequeño).jpg` | el guineo (especie de plátano pequeño) | cneeyú | `LEXR-03134` |
| `diccionario_general/el_gusano.jpg` | el gusano | ucj | `LEXR-01945` |
| `diccionario_general/el_gusano,_larva.jpg` | el gusano, larva | ul jycuet bej | `LEXR-01687` |
| `diccionario_general/el_hacha.jpg` | el hacha | am | `LEXR-03397` |
| `diccionario_general/el_hambre,_escasez.jpg` | el hambre, escasez | wẽjẽ | `LEXR-02595` |
| `diccionario_general/el_helecho.jpg` | el helecho | cwẽ’yã | `LEXR-03195` |
| `diccionario_general/el_hermano_(respecto_a_la_mujer).jpg` | el hermano (respecto a la mujer) | ndyi’sh | `LEXR-01923` |
| `diccionario_general/el_hermano_de_en_medio.jpg` | el hermano de en medio | pyãjtewe’sh | `LEXR-00824` |
| `diccionario_general/el_hermano,_la_hermana_(del_mismo_sexo).jpg` | el hermano, la hermana (del mismo sexo) | yacjtjẽ’j | `LEXR-03464` |
| `diccionario_general/el_hielo.jpg` | el hielo | yu’cuet | `LEXR-03551` |
| `diccionario_general/el_higuerón,_canela_de_páramo_(árbol).jpg` | el higuerón, canela de páramo (árbol) | chavytũu | `LEXR-03638` |
| `diccionario_general/el_higuillo_(árbol).jpg` | el higuillo (árbol) | meeme | `LEXR-01299` |
| `diccionario_general/el_hijo.jpg` | el hijo | nchi’c | `LEXR-02166` |
| `diccionario_general/el_hijo_mayor.jpg` | el hijo mayor | nchi’c ntjẽjsa | `LEXR-01063` |
| `diccionario_general/el_hijo_menor.jpg` | el hijo menor | nchi’c nuuchsa | `LEXR-00896` |
| `diccionario_general/el_hocico_del_puerco.jpg` | el hocico del puerco | cuchi ĩts | `LEXR-03674` |
| `diccionario_general/el_hombre_(adulto).jpg` | el hombre (adulto) | pitstjẽ’j | `LEXR-03413` |
| `diccionario_general/el_hombro.jpg` | el hombro | cmbamb | `LEXR-03901` |
| `diccionario_general/el_homicida.jpg` | el homicida | icjsa | `LEXR-02986` |
| `diccionario_general/el_homicida,_asesino.jpg` | el homicida, asesino | nasa icjsa | `LEXR-02664` |
| `diccionario_general/el_hongo_(planta).jpg` | el hongo (planta) | meshish | `LEXR-00425` |
| `diccionario_general/el_hormiguero.jpg` | el hormiguero | cjç’ng yat | `LEXR-03797` |
| `diccionario_general/el_horno.jpg` | el horno | julnu | `LEXR-00973` |
| `diccionario_general/el_huarango_(árbol).jpg` | el huarango (árbol) | mushclé | `LEXR-01601` |
| `diccionario_general/el_hueco,_hoyo,_agujero,_cueva.jpg` | el hueco, hoyo, agujero, cueva | cafy | `LEXR-03332` |
| `diccionario_general/el_hueso.jpg` | el hueso | dyi’tj | `LEXR-03314` |
| `diccionario_general/el_huevo.jpg` | el huevo | zits | `LEXR-03872` |
| `diccionario_general/el_humo.jpg` | el humo | aj | `LEXR-01842` |
| `diccionario_general/el_huso_(palo_para_hilar).jpg` | el huso (palo para hilar) | cjas waga’te | `LEXR-02362` |
| `diccionario_general/el_huérfano,_guacho.jpg` | el huérfano, guacho | waccha | `LEXR-02943` |
| `diccionario_general/el_hígado.jpg` | el hígado | me’cy | `LEXR-01060` |
| `diccionario_general/el_húmero,_hueso_del_brazo.jpg` | el húmero, hueso del brazo | cu’ta dyi’tj | `LEXR-02098` |
| `diccionario_general/el_idioma_castellano,_español.jpg` | el idioma castellano, español | wagas yuwe | `LEXR-00467` |
| `diccionario_general/el_idioma_páez.jpg` | el idioma páez | nasa yuwe | `LEXR-02817` |
| `diccionario_general/el_infierno.jpg` | el infierno | infiernu | `LEXR-02484` |
| `diccionario_general/el_invierno,_tiempo_de_invierno.jpg` | el invierno, tiempo de invierno | nus pa’ja en | `LEXR-01926` |
| `diccionario_general/el_jabón.jpg` | el jabón | cpun | `LEXR-01981` |
| `diccionario_general/el_jefe.jpg` | el jefe | npiitstjẽj, npiitstjẽ’jsa | `LEXR-01466` |
| `diccionario_general/el_jornalero.jpg` | el jornalero | cnaysá | `LEXR-00958` |
| `diccionario_general/el_jueves.jpg` | el jueves | jueves | `LEXR-00886` |
| `diccionario_general/el_juez_(oficial_del_cabildo).jpg` | el juez (oficial del cabildo) | cjuẽs | `LEXR-01041` |
| `diccionario_general/el_junco_(arbusto).jpg` | el junco (arbusto) | pi’pi | `LEXR-03145` |
| `diccionario_general/el_lado_del_fogón.jpg` | el lado del fogón | ipy ca’t | `LEXR-03315` |
| `diccionario_general/el_lado_opuesto.jpg` | el lado opuesto | cute- | `LEXR-01854` |
| `diccionario_general/el_ladrón.jpg` | el ladrón | peswée | `LEXR-02710` |
| `diccionario_general/el_lagartijo.jpg` | el lagartijo | lawéch | `LEXR-01735` |
| `diccionario_general/el_lechero_(árbol).jpg` | el lechero (árbol) | fychacha | `LEXR-02373` |
| `diccionario_general/el_león_(mamífero).jpg` | el león (mamífero) | llun (T) | `LEXR-03289` |
| `diccionario_general/el_león,_puma_(mamífero).jpg` | el león, puma (mamífero) | shĩ’j | `LEXR-02179` |
| `diccionario_general/el_limón_(fruta).jpg` | el limón (fruta) | llimún | `LEXR-03678` |
| `diccionario_general/el_linaje,_la_raza,_el_descendiente.jpg` | el linaje, la raza, el descendiente | ji’j | `LEXR-03436` |
| `diccionario_general/el_loro_(ave).jpg` | el loro (ave) | well | `LEXR-02974` |
| `diccionario_general/el_lugar.jpg` | el lugar | aj | `LEXR-01967` |
| `diccionario_general/el_lugar_de_habitación,_morada.jpg` | el lugar de habitación, morada | u’pni | `LEXR-01826` |
| `diccionario_general/el_lulo_(planta).jpg` | el lulo (planta) | mutcue | `LEXR-00806` |
| `diccionario_general/el_lunes.jpg` | el lunes | luñis | `LEXR-01058` |
| `diccionario_general/el_líder_(de_un_conjunto_de_músicos).jpg` | el líder (de un conjunto de músicos) | nuyi’nsa | `LEXR-03088` |
| `diccionario_general/el_maestro,_que_enseña.jpg` | el maestro, que enseña | peevya’jsa (T) | `LEXR-02794` |
| `diccionario_general/el_maizal_(depués_de_cosechar).jpg` | el maizal (depués de cosechar) | cutyj dyi’tj ej | `LEXR-03620` |
| `diccionario_general/el_malacate.jpg` | el malacate | waga’te dyi’tj | `LEXR-02637` |
| `diccionario_general/el_mambe.jpg` | el mambe | cuetand | `LEXR-00962` |
| `diccionario_general/el_mar.jpg` | el mar | ĩcj wala | `LEXR-03579` |
| `diccionario_general/el_martingalvis_(árbol).jpg` | el martingalvis (árbol) | tsundefy | `LEXR-00549` |
| `diccionario_general/el_matón.jpg` | el matón | piicje | `LEXR-01876` |
| `diccionario_general/el_mazo.jpg` | el mazo | masu | `LEXR-00423` |
| `diccionario_general/el_maíz.jpg` | el maíz | cutyj | `LEXR-03619` |
| `diccionario_general/el_mediodía.jpg` | el mediodía | ẽepyãj | `LEXR-03672` |
| `diccionario_general/el_mejicano_(calabaza).jpg` | el mejicano (calabaza) | peetjé | `LEXR-01805` |
| `diccionario_general/el_mellizo.jpg` | el mellizo | mellisu | `LEXR-00804` |
| `diccionario_general/el_mensajero.jpg` | el mensajero | yuwe pta’shsa | `LEXR-02351` |
| `diccionario_general/el_mentón,_cumbamba_(voz_quechua).jpg` | el mentón, cumbamba (voz Quechua) | cmbamba | `LEXR-00872` |
| `diccionario_general/el_metal,_hierro.jpg` | el metal, hierro | tsam | `LEXR-00835` |
| `diccionario_general/el_meñique.jpg` | el meñique | cuse nuuchcue | `LEXR-02952` |
| `diccionario_general/el_miércoles.jpg` | el miércoles | qui’spyãj | `LEXR-00990` |
| `diccionario_general/el_molino.jpg` | el molino | mllinu | `LEXR-02850` |
| `diccionario_general/el_mono,_mico_(mamífero).jpg` | el mono, mico (mamífero) | micu | `LEXR-00426` |
| `diccionario_general/el_mosquito.jpg` | el mosquito | apj le’ch | `LEXR-03039` |
| `diccionario_general/el_mote.jpg` | el mote | mutyi | `LEXR-02755` |
| `diccionario_general/el_muchacho.jpg` | el muchacho | cuẽ | `LEXR-01855` |
| `diccionario_general/el_muchaco.jpg` | el muchaco | pitscuẽ | `LEXR-01611` |
| `diccionario_general/el_muchilero_(ave).jpg` | el muchilero (ave) | ũtj | `LEXR-03581` |
| `diccionario_general/el_murcielago_(mamífero).jpg` | el murcielago (mamífero) | cjĩjtse (cjitsa T) | `LEXR-03536` |
| `diccionario_general/el_musgo.jpg` | el musgo | wa’cj | `LEXR-02799` |
| `diccionario_general/el_muslo.jpg` | el muslo | ji’mbe | `LEXR-01147` |
| `diccionario_general/el_músculo.jpg` | el músculo | cuse chavy | `LEXR-03640` |
| `diccionario_general/el_nevado.jpg` | el nevado | yandy (ñandy T) | `LEXR-01767` |
| `diccionario_general/el_nevado_(ej._nevado_de_huila).jpg` | el nevado (ej. Nevado de Huila) | ñandy (yãndy) | `LEXR-01962` |
| `diccionario_general/el_nido.jpg` | el nido | duu yat | `LEXR-01450` |
| `diccionario_general/el_nieto,_la_nieta.jpg` | el nieto, la nieta | ntsun | `LEXR-00808` |
| `diccionario_general/el_niño,_la_niña.jpg` | el niño, la niña | le’chcuesa | `LEXR-02751` |
| `diccionario_general/el_nombre.jpg` | el nombre | yase (yese) | `LEXR-01768` |
| `diccionario_general/el_nudillo_(planta).jpg` | el nudillo (planta) | fitscu’ng | `LEXR-01380` |
| `diccionario_general/el_ojo.jpg` | el ojo | yafy | `LEXR-02082` |
| `diccionario_general/el_ojo_de_agua,_manatial.jpg` | el ojo de agua, manatial | yu’ĩts | `LEXR-01699` |
| `diccionario_general/el_ombligo.jpg` | el ombligo | shamb | `LEXR-01617` |
| `diccionario_general/el_oriente,_este.jpg` | el oriente, este | sec cãani | `LEXR-00636` |
| `diccionario_general/el_oro_(metal).jpg` | el oro (metal) | vyuu bej | `LEXR-02241` |
| `diccionario_general/el_oso_(mamífero).jpg` | el oso (mamífero) | e’shavy | `LEXR-00966` |
| `diccionario_general/el_ovillo.jpg` | el ovillo | cjas wãjyandy | `LEXR-02258` |
| `diccionario_general/el_oído.jpg` | el oído | tjũ’we cafy | `LEXR-01168` |
| `diccionario_general/el_padrastro.jpg` | el padrastro | ney npaasa | `LEXR-02623` |
| `diccionario_general/el_padre.jpg` | el padre | ney | `LEXR-01390` |
| `diccionario_general/el_padre,_papá.jpg` | el padre, papá | tata | `LEXR-00545` |
| `diccionario_general/el_padrino.jpg` | el padrino | neeney | `LEXR-01301` |
| `diccionario_general/el_pajonal.jpg` | el pajonal | yunda | `LEXR-00572` |
| `diccionario_general/el_paladar.jpg` | el paladar | je’ng | `LEXR-01532` |
| `diccionario_general/el_palo_del_huso.jpg` | el palo del huso | waga’te fytũu | `LEXR-03367` |
| `diccionario_general/el_palo_del_telar_(lanzadera).jpg` | el palo del telar (lanzadera) | ñuwe | `LEXR-02803` |
| `diccionario_general/el_paludismo.jpg` | el paludismo | yaawee | `LEXR-01271` |
| `diccionario_general/el_pariente_(de_la_misma_raza).jpg` | el pariente (de la misma raza) | nwe’sh | `LEXR-00521` |
| `diccionario_general/el_pasto.jpg` | el pasto | pastu | `LEXR-01543` |
| `diccionario_general/el_pastor_de_ovejas.jpg` | el pastor de ovejas | piisháa tjengsa | `LEXR-01610` |
| `diccionario_general/el_patio.jpg` | el patio | patyu | `LEXR-01073` |
| `diccionario_general/el_pavo_de_monte_(ave).jpg` | el pavo de monte (ave) | finzh wala | `LEXR-00702` |
| `diccionario_general/el_pecado.jpg` | el pecado | pcal | `LEXR-01674` |
| `diccionario_general/el_pecador.jpg` | el pecador | pcalsa | `LEXR-03505` |
| `diccionario_general/el_pecho,_la_teta.jpg` | el pecho, la teta | chu’ch | `LEXR-02469` |
| `diccionario_general/el_pedazo.jpg` | el pedazo | pe’la | `LEXR-02928` |
| `diccionario_general/el_pedernal_(para_prender_candela).jpg` | el pedernal (para prender candela) | pety cuet | `LEXR-02005` |
| `diccionario_general/el_peine.jpg` | el peine | quind | `LEXR-02225` |
| `diccionario_general/el_pelo_del_cuerpo.jpg` | el pelo del cuerpo | cacue cjas | `LEXR-01031` |
| `diccionario_general/el_pelo,_cabello.jpg` | el pelo, cabello | dycjas | `LEXR-03709` |
| `diccionario_general/el_pene.jpg` | el pene | iw | `LEXR-02987` |
| `diccionario_general/el_pepino.jpg` | el pepino | piinaa | `LEXR-03292` |
| `diccionario_general/el_perrito,_cachorro.jpg` | el perrito, cachorro | quishcue | `LEXR-02173` |
| `diccionario_general/el_perro.jpg` | el perro | alcu, alcucuẽ | `LEXR-01438` |
| `diccionario_general/el_pescado,_pez.jpg` | el pescado, pez | wendy | `LEXR-02900` |
| `diccionario_general/el_pescador.jpg` | el pescador | wendy uwesá | `LEXR-02407` |
| `diccionario_general/el_peso_(moneda).jpg` | el peso (moneda) | pesu | `LEXR-02709` |
| `diccionario_general/el_peón,_jornalero.jpg` | el peón, jornalero | piun | `LEXR-02056` |
| `diccionario_general/el_pico_(herramienta).jpg` | el pico (herramienta) | pica (T) | `LEXR-02328` |
| `diccionario_general/el_pie,_la_pierna_(de_persona),_la_pata_(de_animal).jpg` | el pie, la pierna (de persona), la pata (de animal) | chinda | `LEXR-03557` |
| `diccionario_general/el_piojo_(insecto).jpg` | el piojo (insecto) | ẽs | `LEXR-01840` |
| `diccionario_general/el_pisco,_pavo_(ave).jpg` | el pisco, pavo (ave) | piscu | `LEXR-02219` |
| `diccionario_general/el_pisón.jpg` | el pisón | pisun | `LEXR-02170` |
| `diccionario_general/el_plano,_la_llanura,_el_llano.jpg` | el plano, la llanura, el llano | ucue | `LEXR-01889` |
| `diccionario_general/el_plátano_(de_tierrra_templada).jpg` | el plátano (de tierrra templada) | tayti | `LEXR-02069` |
| `diccionario_general/el_plátano_(planta).jpg` | el plátano (planta) | tlu (T) | `LEXR-03895` |
| `diccionario_general/el_poder.jpg` | el poder | ewuní | `LEXR-00880` |
| `diccionario_general/el_pollo.jpg` | el pollo | atall luuch | `LEXR-01109` |
| `diccionario_general/el_polvo.jpg` | el polvo | tujnd | `LEXR-01559` |
| `diccionario_general/el_polvo_(del_camino).jpg` | el polvo (del camino) | quiwe tujnd | `LEXR-01316` |
| `diccionario_general/el_poniente,_oeste,_occidente.jpg` | el poniente, oeste, occidente | sec cjẽeni | `LEXR-00635` |
| `diccionario_general/el_poporo.jpg` | el poporo | tu’j | `LEXR-03271` |
| `diccionario_general/el_pozo.jpg` | el pozo | yu’pusu | `LEXR-01429` |
| `diccionario_general/el_pozo_de_barro_(para_hacer_teja).jpg` | el pozo de barro (para hacer teja) | tyity pusu | `LEXR-01332` |
| `diccionario_general/el_preso.jpg` | el preso | preesu | `LEXR-01750` |
| `diccionario_general/el_primero,_los_primeros.jpg` | el primero, los primeros | nyafytewe’sh | `LEXR-01606` |
| `diccionario_general/el_primo,_la_prima_(del_mismo_sexo).jpg` | el primo, la prima (del mismo sexo) | pucacje nyacj | `LEXR-01246` |
| `diccionario_general/el_primogénito_(primer_hijo).jpg` | el primogénito (primer hijo) | ne’sh, ne’shtjẽ’j | `LEXR-00980` |
| `diccionario_general/el_pueblo,_caserío.jpg` | el pueblo, caserío | shamb | `LEXR-03344` |
| `diccionario_general/el_puerco,_cerdo,_marrano.jpg` | el puerco, cerdo, marrano | cuchi | `LEXR-02300` |
| `diccionario_general/el_pulgar.jpg` | el pulgar | cuse njĩ’j | `LEXR-01594` |
| `diccionario_general/el_pulmón.jpg` | el pulmón | me’cyshũ | `LEXR-02849` |
| `diccionario_general/el_pus.jpg` | el pus | tucj | `LEXR-02281` |
| `diccionario_general/el_puño.jpg` | el puño | tut | `LEXR-01761` |
| `diccionario_general/el_pájaro.jpg` | el pájaro | vichacue | `LEXR-02077` |
| `diccionario_general/el_pájaro_carpintero.jpg` | el pájaro carpintero | anza | `LEXR-00768` |
| `diccionario_general/el_páramo_(terreno_desierto,_elevado_y_sin_vegetación).jpg` | el páramo (terreno desierto, elevado y sin vegetación) | we’pe | `LEXR-00565` |
| `diccionario_general/el_que_hace.jpg` | el que hace | vit-sa | `LEXR-02406` |
| `diccionario_general/el_que_mete_la_caña_en_el_otro_lado_del_trapiche.jpg` | el que mete la caña en el otro lado del trapiche | ñusha puutssa | `LEXR-00853` |
| `diccionario_general/el_que_recibe_cañaen_el_trapiche.jpg` | el que recibe cañaen el trapiche | ñusha jypa’gasa | `LEXR-01636` |
| `diccionario_general/el_queso.jpg` | el queso | quisu | `LEXR-03823` |
| `diccionario_general/el_rabo_(de_gallina).jpg` | el rabo (de gallina) | yucnenga | `LEXR-01836` |
| `diccionario_general/el_rancho,_cobertizo.jpg` | el rancho, cobertizo | wa’ | `LEXR-01424` |
| `diccionario_general/el_rastrojo.jpg` | el rastrojo | scuutyj dyi’tj ej | `LEXR-02395` |
| `diccionario_general/el_ratón_(mamífero_roedor).jpg` | el ratón (mamífero roedor) | ujnza | `LEXR-02591` |
| `diccionario_general/el_rayo.jpg` | el rayo | amwe’sh | `LEXR-02254` |
| `diccionario_general/el_rayo_(que_quema).jpg` | el rayo (que quema) | ipywe’sh | `LEXR-00885` |
| `diccionario_general/el_rejo.jpg` | el rejo | cja’tya | `LEXR-03076` |
| `diccionario_general/el_remedio,_medicina.jpg` | el remedio, medicina | yu’tse | `LEXR-00667` |
| `diccionario_general/el_renacuajo,_cría_de_la_rana.jpg` | el renacuajo, cría de la rana | taacy wendy | `LEXR-02400` |
| `diccionario_general/el_res,_el_ganado_(animal_doméstico).jpg` | el res, el ganado (animal doméstico) | cla | `LEXR-00871` |
| `diccionario_general/el_retoño.jpg` | el retoño | ye’ch | `LEXR-02192` |
| `diccionario_general/el_rezandero.jpg` | el rezandero | lisasá | `LEXR-00890` |
| `diccionario_general/el_riachuelo.jpg` | el riachuelo | yu’le’ch | `LEXR-02247` |
| `diccionario_general/el_rincón,_la_esquina.jpg` | el rincón, la esquina | punza | `LEXR-00989` |
| `diccionario_general/el_riñón.jpg` | el riñón | us | `LEXR-02897` |
| `diccionario_general/el_roble_(árbol).jpg` | el roble (árbol) | pinzh | `LEXR-01808` |
| `diccionario_general/el_río.jpg` | el río | yu’wala | `LEXR-02030` |
| `diccionario_general/el_sapo_(batracio).jpg` | el sapo (batracio) | sap | `LEXR-02584` |
| `diccionario_general/el_sapo_pequeño.jpg` | el sapo pequeño | tsunz | `LEXR-00455` |
| `diccionario_general/el_sarampión.jpg` | el sarampión | buta wee | `LEXR-01777` |
| `diccionario_general/el_sebo.jpg` | el sebo | sepu | `LEXR-01817` |
| `diccionario_general/el_sembrado.jpg` | el sembrado | uutjash | `LEXR-02239` |
| `diccionario_general/el_sepulcro,_cementario.jpg` | el sepulcro, cementario | uusá pendaní cafy | `LEXR-02555` |
| `diccionario_general/el_sereno.jpg` | el sereno | slenu (sleena) | `LEXR-03153` |
| `diccionario_general/el_señor,_patrón.jpg` | el señor, patrón | amu | `LEXR-02838` |
| `diccionario_general/el_siervo,_que_sirve.jpg` | el siervo, que sirve | selpisá | `LEXR-02228` |
| `diccionario_general/el_sitio.jpg` | el sitio | fynũ | `LEXR-00789` |
| `diccionario_general/el_sobaco,_axila.jpg` | el sobaco, axila | punza cafy | `LEXR-00822` |
| `diccionario_general/el_sol.jpg` | el sol | tacycue (J) | `LEXR-01757` |
| `diccionario_general/el_soldado.jpg` | el soldado | soldau | `LEXR-03650` |
| `diccionario_general/el_suegro.jpg` | el suegro | cajcatẽ´j | `LEXR-01032` |
| `diccionario_general/el_sueño.jpg` | el sueño | csha’w | `LEXR-02654` |
| `diccionario_general/el_sábado.jpg` | el sábado | sápatu | `LEXR-02499` |
| `diccionario_general/el_tallo_de_maíz.jpg` | el tallo de maíz | shimb dyi’tj | `LEXR-01483` |
| `diccionario_general/el_tamal,_el_bollo_(envuelto_de_maíz).jpg` | el tamal, el bollo (envuelto de maíz) | pullu | `LEXR-02761` |
| `diccionario_general/el_tamo.jpg` | el tamo | tama | `LEXR-02938` |
| `diccionario_general/el_telar.jpg` | el telar | atyj tel | `LEXR-02414` |
| `diccionario_general/el_temblor_(de_tierra).jpg` | el temblor (de tierra) | ejnd | `LEXR-02747` |
| `diccionario_general/el_ternero.jpg` | el ternero | claa luuch | `LEXR-03334` |
| `diccionario_general/el_teñidero_(árbol,_que_se_usa_para_teñir_de_negro).jpg` | el teñidero (árbol, que se usa para teñir de negro) | shal | `LEXR-03151` |
| `diccionario_general/el_tigrillo.jpg` | el tigrillo | atall ech | `LEXR-01709` |
| `diccionario_general/el_tigrillo_(mamífero).jpg` | el tigrillo (mamífero) | tyiclli | `LEXR-02284` |
| `diccionario_general/el_tizón.jpg` | el tizón | ipy tyjic | `LEXR-02662` |
| `diccionario_general/el_tobillo,_la_espinilla.jpg` | el tobillo, la espinilla | chinda ca’ca | `LEXR-01848` |
| `diccionario_general/el_toro.jpg` | el toro | tulu | `LEXR-01171` |
| `diccionario_general/el_toromonte_(ave).jpg` | el toromonte (ave) | turúc | `LEXR-02134` |
| `diccionario_general/el_trabajador.jpg` | el trabajador | mjĩisa | `LEXR-03360` |
| `diccionario_general/el_trabajo,_empleo.jpg` | el trabajo, empleo | mjĩi | `LEXR-02538` |
| `diccionario_general/el_trapiche.jpg` | el trapiche | clapichi | `LEXR-00957` |
| `diccionario_general/el_trapiche_de_mano.jpg` | el trapiche de mano | ñusha tel | `LEXR-00760` |
| `diccionario_general/el_trigal.jpg` | el trigal | scuutyj ej | `LEXR-01554` |
| `diccionario_general/el_trigo.jpg` | el trigo | scuutyj (scuucyj T) | `LEXR-02859` |
| `diccionario_general/el_troje,_granero.jpg` | el troje, granero | ũ’ jyaw yat | `LEXR-01351` |
| `diccionario_general/el_trompo_(juguete).jpg` | el trompo (juguete) | chunga | `LEXR-02569` |
| `diccionario_general/el_trueno,_rayo,_relámpago.jpg` | el trueno, rayo, relámpago | cpi’sh | `LEXR-01980` |
| `diccionario_general/el_tumor,_absceso.jpg` | el tumor, absceso | cuw | `LEXR-00780` |
| `diccionario_general/el_tío_(hermano_de_la_mamá).jpg` | el tío (hermano de la mamá) | cajca | `LEXR-01908` |
| `diccionario_general/el_tío_(hermano_del_papá).jpg` | el tío (hermano del papá) | ñucue | `LEXR-00476` |
| `diccionario_general/el_umbral.jpg` | el umbral | blal | `LEXR-01197` |
| `diccionario_general/el_uvillo_(fruta_silvestre_comestible).jpg` | el uvillo (fruta silvestre comestible) | shbu | `LEXR-00536` |
| `diccionario_general/el_vado.jpg` | el vado | yu’pets | `LEXR-02945` |
| `diccionario_general/el_valle.jpg` | el valle | ucue quiwe | `LEXR-01686` |
| `diccionario_general/el_verano.jpg` | el verano | ejnz | `LEXR-00784` |
| `diccionario_general/el_vestido_(de_mujer).jpg` | el vestido (de mujer) | isni | `LEXR-00509` |
| `diccionario_general/el_vientre.jpg` | el vientre | tutyj dyiite | `LEXR-02184` |
| `diccionario_general/el_viernes.jpg` | el viernes | tyjẽ’en | `LEXR-02798` |
| `diccionario_general/el_viudo.jpg` | el viudo | ech pijts | `LEXR-01988` |
| `diccionario_general/el_vómito.jpg` | el vómito | punga | `LEXR-03802` |
| `diccionario_general/el_yerno.jpg` | el yerno | nduj | `LEXR-01997` |
| `diccionario_general/el_yucal.jpg` | el yucal | ña ej | `LEXR-03910` |
| `diccionario_general/el_zamarro.jpg` | el zamarro | smala | `LEXR-01940` |
| `diccionario_general/el_zancudo.jpg` | el zancudo | apj | `LEXR-02199` |
| `diccionario_general/el_zanjón_de_agua.jpg` | el zanjón de agua | yu’puits | `LEXR-01959` |
| `diccionario_general/el_zapallo_rayado.jpg` | el zapallo rayado | ape | `LEXR-03492` |
| `diccionario_general/el_zapato.jpg` | el zapato | spaatu | `LEXR-00541` |
| `diccionario_general/el_zorro_(mamífero).jpg` | el zorro (mamífero) | sulu | `LEXR-01163` |
| `diccionario_general/el_zurrón_(botija_de_piel_para_guarapo).jpg` | el zurrón (botija de piel para guarapo) | slun (sluty T) | `LEXR-02127` |
| `diccionario_general/el_águila_(ave).jpg` | el águila (ave) | uj | `LEXR-01827` |
| `diccionario_general/el_ánima_(del_difunto).jpg` | el ánima (del difunto) | taafiy | `LEXR-02128` |
| `diccionario_general/el_ídolo.jpg` | el ídolo | dyus ĩtyĩmeesa | `LEXR-00698` |
| `diccionario_general/el_último_hijo,_a.jpg` | el último hijo, a | men | `LEXR-03867` |
| `diccionario_general/ellos,_ellas.jpg` | ellos, ellas | cyãawe’sh (tyãawe’sh) | `LEXR-03474` |
| `diccionario_general/ellos,_ellas,_aquellos,_aquellas.jpg` | ellos, ellas, aquellos, aquellas | tyãawe’sh (cyãawe’sh) | `LEXR-00558` |
| `diccionario_general/embarrar.jpg` | embarrar | tyity amb- | `LEXR-00460` |
| `diccionario_general/embijarse.jpg` | embijarse | biite’j-, biite’je | `LEXR-03830` |
| `diccionario_general/emborracharse.jpg` | emborracharse | tũu- | `LEXR-03871` |
| `diccionario_general/embotado.jpg` | embotado | tut | `LEXR-02340` |
| `diccionario_general/embotarse.jpg` | embotarse | tutu- | `LEXR-00651` |
| `diccionario_general/empachar.jpg` | empachar | cchiiwa’j-, cchiiwa’ja- | `LEXR-03041` |
| `diccionario_general/empajar.jpg` | empajar | tsjĩtsj um- | `LEXR-00926` |
| `diccionario_general/empeorar,_aumentar_más_y_más.jpg` | empeorar, aumentar más y más | jytjaacue-, jytjaacuée- | `LEXR-03114` |
| `diccionario_general/emperzar,_comenzar.jpg` | emperzar, comenzar | tacj-, tacje- | `LEXR-02860` |
| `diccionario_general/empezar.jpg` | empezar | cãj-, cãjã- | `LEXR-01210` |
| `diccionario_general/empezar_a_hervir,_burbjear.jpg` | empezar a hervir, burbjear | bu’ch, bu’chi- | `LEXR-01363` |
| `diccionario_general/empezar,_emprender_(un_trabajo).jpg` | empezar, emprender (un trabajo) | puuquiwe- | `LEXR-01247` |
| `diccionario_general/empobrecerse.jpg` | empobrecerse | puuple yuu- | `LEXR-02582` |
| `diccionario_general/empujar.jpg` | empujar | upajcy-, upaqui- | `LEXR-03155` |
| `diccionario_general/empujar_(con_violencia).jpg` | empujar (con violencia) | ucapajcy-, ucapaqui- | `LEXR-00838` |
| `diccionario_general/empujar_(repetidas_veces).jpg` | empujar (repetidas veces) | upagacy-, upagaqui- | `LEXR-01008` |
| `diccionario_general/en_esta_tierra,_en_este_mundo.jpg` | en esta tierra, en este mundo | naa quiwete | `LEXR-01798` |
| `diccionario_general/en_forma_de_bola.jpg` | en forma de bola | jyũ’nzh, jyũ’nzhcuẽ | `LEXR-00888` |
| `diccionario_general/en_frente_de_la_casa.jpg` | en frente de la casa | yat dyi’pte | `LEXR-01955` |
| `diccionario_general/en_frente_de,_delante_de,_ante.jpg` | en frente de, delante de, ante | dyi’p | `LEXR-03475` |
| `diccionario_general/en_la_otra_semana.jpg` | en la otra semana | vite qui’sute | `LEXR-03896` |
| `diccionario_general/en_medio_de.jpg` | en medio de | pyãj- | `LEXR-03120` |
| `diccionario_general/en_medio_de,_entre.jpg` | en medio de, entre | cshavy- | `LEXR-03449` |
| `diccionario_general/en_seco_(tierra_firme).jpg` | en seco (tierra firme) | tujme | `LEXR-03763` |
| `diccionario_general/en_sueños.jpg` | en sueños | csha’wte | `LEXR-03354` |
| `diccionario_general/en_tiempo_de_luna.jpg` | en tiempo de luna | a’teweete | `LEXR-03424` |
| `diccionario_general/en_todas_partes.jpg` | en todas partes | mtee mteeva | `LEXR-01536` |
| `diccionario_general/en_vano,_inútilmente.jpg` | en vano, inútilmente | cyul | `LEXR-02264` |
| `diccionario_general/en_vano,_sin_motivo,_de_nada.jpg` | en vano, sin motivo, de nada | ĩ’née | `LEXR-02144` |
| `diccionario_general/en_vez._._..jpg` | en vez... | -pcachte | `LEXR-00580` |
| `diccionario_general/en,_de.jpg` | en, de | -ca, (-ga) | `LEXR-01273` |
| `diccionario_general/encabado.jpg` | encabado | catashi´jni | `LEXR-03726` |
| `diccionario_general/encargar.jpg` | encargar | paawe’we- | `LEXR-01071` |
| `diccionario_general/encargo.jpg` | encargo | paawe’weni | `LEXR-01307` |
| `diccionario_general/encender,_alumbrar.jpg` | encender, alumbrar | pqui’ta- (fyqui’ta-) | `LEXR-01546` |
| `diccionario_general/encerrar,_encarcelar.jpg` | encerrar, encarcelar | cyuupj-, cyuupjáa- | `LEXR-00877` |
| `diccionario_general/encogerse.jpg` | encogerse | ũpj-, ũpjúu- | `LEXR-02836` |
| `diccionario_general/encogerse_(tela).jpg` | encogerse (tela) | fita- | `LEXR-01214` |
| `diccionario_general/encomendar.jpg` | encomendar | neewe’we- | `LEXR-03439` |
| `diccionario_general/encontrar_(algo_que_otro_ha_perdido).jpg` | encontrar (algo que otro ha perdido) | pjiw-, pjiwúu- | `LEXR-02330` |
| `diccionario_general/encontrarse_con_otro.jpg` | encontrarse con otro | puuty uy-, puuty uyúu- | `LEXR-01614` |
| `diccionario_general/encontrarse_con_otro_(que_viene_del_rumbo_opuesto.jpg` | encontrarse con otro (que viene del rumbo opuesto | pu’tjeng-, pu’tjengu- | `LEXR-01081` |
| `diccionario_general/encorvado.jpg` | encorvado | tuñ | `LEXR-02453` |
| `diccionario_general/encorvarse.jpg` | encorvarse | ta’ts yuu- | `LEXR-03063` |
| `diccionario_general/encorvarse,_inclinarse.jpg` | encorvarse, inclinarse | tuñi- | `LEXR-03463` |
| `diccionario_general/endemoniado.jpg` | endemoniado | ech iiyamunisa | `LEXR-02530` |
| `diccionario_general/enderezarse.jpg` | enderezarse | capjute- | `LEXR-01847` |
| `diccionario_general/endulzar.jpg` | endulzar | ñusha’j-, ñusha’ja- | `LEXR-03767` |
| `diccionario_general/endurecer.jpg` | endurecer | nuywejy-, nuyweji- | `LEXR-02541` |
| `diccionario_general/enemistarse,_hacerse_enemigos.jpg` | enemistarse, hacerse enemigos | iipuii yuu- | `LEXR-00415` |
| `diccionario_general/enfadarse.jpg` | enfadarse | cha’cy-, cha’qui- | `LEXR-00772` |
| `diccionario_general/enfadarse,_enojarse_(mutuamente).jpg` | enfadarse, enojarse (mutuamente) | puuty pyũuscue- | `LEXR-02223` |
| `diccionario_general/enfermarse,_sufrir_dolores_de_parto.jpg` | enfermarse, sufrir dolores de parto | ãtsã’a- | `LEXR-00849` |
| `diccionario_general/enfermedad_contagiosa.jpg` | enfermedad contagiosa | teega wee | `LEXR-00833` |
| `diccionario_general/enfermedad_de_granos.jpg` | enfermedad de granos | wã’jy wee | `LEXR-02025` |
| `diccionario_general/enfermedad_de_los_ojos.jpg` | enfermedad de los ojos | yafy wee | `LEXR-02083` |
| `diccionario_general/enfermo.jpg` | enfermo | ãtsã’ | `LEXR-01575` |
| `diccionario_general/enfilarse_(según_cierto_orden).jpg` | enfilarse (según cierto orden) | sende’nde- | `LEXR-03482` |
| `diccionario_general/enflaquecerse.jpg` | enflaquecerse | talli- | `LEXR-03546` |
| `diccionario_general/enflaquecerse,_delilitarse.jpg` | enflaquecerse, delilitarse | ĩchjíi- | `LEXR-02774` |
| `diccionario_general/enfriar,_refrescar.jpg` | enfriar, refrescar | fiinze’j-, fiinze’je- | `LEXR-01453` |
| `diccionario_general/enfriarse.jpg` | enfriarse | finze yuu- | `LEXR-02958` |
| `diccionario_general/enganchar,_abrochar.jpg` | enganchar, abrochar | jypujts-, jypuuts- | `LEXR-03852` |
| `diccionario_general/engañarse.jpg` | engañarse | ya’jypumba- | `LEXR-00845` |
| `diccionario_general/engordarse.jpg` | engordarse | niishi- | `LEXR-03026` |
| `diccionario_general/enjuagar.jpg` | enjuagar | fyneecu’c- | `LEXR-01790` |
| `diccionario_general/enlazar.jpg` | enlazar | cũ’p-, cũ’pu- | `LEXR-02370` |
| `diccionario_general/enloquecerse.jpg` | enloquecerse | luucu yuu- | `LEXR-03564` |
| `diccionario_general/enmohecerse.jpg` | enmohecerse | chuuma’ma- | `LEXR-00493` |
| `diccionario_general/ennegrecer,_ponerse_negro.jpg` | ennegrecer, ponerse negro | cjũchji | `LEXR-01656` |
| `diccionario_general/enojarse.jpg` | enojarse | ũuscha-, ũuscháa- | `LEXR-03251` |
| `diccionario_general/enojarse_(mutuamente).jpg` | enojarse (mutuamente) | puuty ũuscha- | `LEXR-02547` |
| `diccionario_general/enorgullecerse.jpg` | enorgullecerse | iiwejch-, iiweechi- | `LEXR-01290` |
| `diccionario_general/enorgullecerse,_sentirse_orgulloso.jpg` | enorgullecerse, sentirse orgulloso | iiwejch yajcy- | `LEXR-03232` |
| `diccionario_general/enraizar.jpg` | enraizar | iiwajtse-, iiwatse- | `LEXR-01146` |
| `diccionario_general/enredarse.jpg` | enredarse | ya’ndu- | `LEXR-00569` |
| `diccionario_general/enriquecerse,_ser_rico.jpg` | enriquecerse, ser rico | ji’pjsa yuu- | `LEXR-00510` |
| `diccionario_general/enrollado.jpg` | enrollado | andni | `LEXR-01108` |
| `diccionario_general/enrollar.jpg` | enrollar | pel-, pelu- | `LEXR-00628` |
| `diccionario_general/enrollarse,_enredarse.jpg` | enrollarse, enredarse | yaandúu- | `LEXR-00846` |
| `diccionario_general/ensanchar.jpg` | ensanchar | nuytape- | `LEXR-01306` |
| `diccionario_general/ensartar.jpg` | ensartar | wats-, watsu- | `LEXR-02638` |
| `diccionario_general/ensayar,_probar,_tratar_de.jpg` | ensayar, probar, tratar de | isa- | `LEXR-00607` |
| `diccionario_general/enseñanza.jpg` | enseñanza | caapiya’jni | `LEXR-01113` |
| `diccionario_general/enseñar.jpg` | enseñar | peevya’j-, peevya’ja- (T) | `LEXR-00983` |
| `diccionario_general/ensillado.jpg` | ensillado | wa’ta’jni | `LEXR-01266` |
| `diccionario_general/ensillar.jpg` | ensillar | wa’ta’j-, wa’ta’ja- | `LEXR-00563` |
| `diccionario_general/ensuciar,_tiznar.jpg` | ensuciar, tiznar | cjũuchji’j-, cjũuchji’ji- | `LEXR-01517` |
| `diccionario_general/entenado,_a.jpg` | entenado, a | jype’jnisa | `LEXR-01734` |
| `diccionario_general/entenderse.jpg` | entenderse | ya’jiyu- | `LEXR-02596` |
| `diccionario_general/entiesar,_ponerse_tieso.jpg` | entiesar, ponerse tieso | we’lli- | `LEXR-02869` |
| `diccionario_general/entonces.jpg` | entonces | cyajũ’ | `LEXR-02810` |
| `diccionario_general/entrar.jpg` | entrar | u’ca- | `LEXR-02403` |
| `diccionario_general/entrar_brevemente.jpg` | entrar brevemente | ne’ca- | `LEXR-02991` |
| `diccionario_general/entre_los_de_la_misma_tribu_páez.jpg` | entre los de la misma tribu páez | nasa pwe’sh | `LEXR-01799` |
| `diccionario_general/entre_ustedes,_unos_con_otros.jpg` | entre ustedes, unos con otros | i’cue’sh pwe’sh | `LEXR-03734` |
| `diccionario_general/entregar_voluntariamente.jpg` | entregar voluntariamente | paanducj-, paanducje- | `LEXR-00622` |
| `diccionario_general/entregar,_pagar_deuda.jpg` | entregar, pagar deuda | ducj-, ducje- | `LEXR-02659` |
| `diccionario_general/entregarse_voluntariamente.jpg` | entregarse voluntariamente | paaya’ducj-, paaya’ducje- | `LEXR-02544` |
| `diccionario_general/entristecer,_causar_tristeza.jpg` | entristecer, causar tristeza | cyũusu’j-, cyũusu’ju- | `LEXR-03864` |
| `diccionario_general/entristecer,_hacer_sufrir.jpg` | entristecer, hacer sufrir | cñusu’j-, cñusu’ju-(cyũusu’j-) | `LEXR-03080` |
| `diccionario_general/entumirse.jpg` | entumirse | nish dej- | `LEXR-02322` |
| `diccionario_general/envejecerse_(hombre_o_cosa).jpg` | envejecerse (hombre o cosa) | ĩish-, ĩishi- | `LEXR-01577` |
| `diccionario_general/envejercerse_(mujer).jpg` | envejercerse (mujer) | penzhíi- | `LEXR-01749` |
| `diccionario_general/envoltura.jpg` | envoltura | yap | `LEXR-01696` |
| `diccionario_general/envolver.jpg` | envolver | scand-, scandúu- | `LEXR-01317` |
| `diccionario_general/envolver_(repetidas_veces).jpg` | envolver (repetidas veces) | scandundu- | `LEXR-02011` |
| `diccionario_general/envolver,_enrollar.jpg` | envolver, enrollar | and-, andúu- | `LEXR-01026` |
| `diccionario_general/equivocarse,_desviarse,_dejarse_engeñar.jpg` | equivocarse, desviarse, dejarse engeñar | jypumba-, jyumbáa- | `LEXR-01224` |
| `diccionario_general/erizar.jpg` | erizar | shinde-, shindée- | `LEXR-02823` |
| `diccionario_general/erizar_(varias_veces).jpg` | erizar (varias veces) | shinde’nde- | `LEXR-01408` |
| `diccionario_general/erizo,_puerco_espín.jpg` | erizo, puerco espín | tjuw | `LEXR-03123` |
| `diccionario_general/error,_equivocación.jpg` | error, equivocación | jyumbani | `LEXR-01461` |
| `diccionario_general/eructar.jpg` | eructar | tu’fy-, tu’fi- | `LEXR-02552` |
| `diccionario_general/escama_(de_pescado).jpg` | escama (de pescado) | wendy cja’ty | `LEXR-02507` |
| `diccionario_general/escampar.jpg` | escampar | nus pĩi- | `LEXR-02666` |
| `diccionario_general/escancel_(planta_medicinal).jpg` | escancel (planta medicinal) | shũuwe’tj | `LEXR-03523` |
| `diccionario_general/escarbar.jpg` | escarbar | wuw-, wuwu- | `LEXR-01569` |
| `diccionario_general/escarbar_(con_uña).jpg` | escarbar (con uña) | vyllill-, vyllillíi- | `LEXR-03884` |
| `diccionario_general/escarbar,_arar.jpg` | escarbar, arar | ujw-, ujwu- | `LEXR-02075` |
| `diccionario_general/escoba.jpg` | escoba | scuba | `LEXR-01816` |
| `diccionario_general/escoger.jpg` | escoger | tyjityij-, tyjityiji- | `LEXR-01885` |
| `diccionario_general/escogido.jpg` | escogido | tyjityjni | `LEXR-00654` |
| `diccionario_general/esconder.jpg` | esconder | sũtj-, sũje- | `LEXR-02232` |
| `diccionario_general/esconderse.jpg` | esconderse | jysũutj-, jysũutje- (fysũutje- T) | `LEXR-03438` |
| `diccionario_general/escopeta.jpg` | escopeta | scupeta | `LEXR-01755` |
| `diccionario_general/escribano,_escribiente.jpg` | escribano, escribiente | fi’pju’chsa | `LEXR-01914` |
| `diccionario_general/escrito.jpg` | escrito | fi’jni | `LEXR-02160` |
| `diccionario_general/escritura.jpg` | escritura | fi’jnisa | `LEXR-03602` |
| `diccionario_general/escuchar,_oir.jpg` | escuchar, oir | wẽsẽ’j-, wẽsẽ’je- | `LEXR-01177` |
| `diccionario_general/escuela.jpg` | escuela | scuela | `LEXR-03508` |
| `diccionario_general/escupir.jpg` | escupir | avy-, avi- | `LEXR-00943` |
| `diccionario_general/escupir_en.jpg` | escupir en | avytjetj-, avytjetje- | `LEXR-03533` |
| `diccionario_general/ese,_esa.jpg` | ese, esa | cyãa (tyãa) | `LEXR-03538` |
| `diccionario_general/eslabón_(hierro_para_afilar_o_para_sacar_fuego_del_pedernal).jpg` | eslabón (hierro para afilar o para sacar fuego del pedernal) | shlaapún | `LEXR-00731` |
| `diccionario_general/esmeralda,_colibrí_(ave).jpg` | esmeralda, colibrí (ave) | e’ts, e’tscuẽ | `LEXR-01378` |
| `diccionario_general/esos,_esas.jpg` | esos, esas | cyãawe’sh (tyãawe’sh) | `LEXR-02811` |
| `diccionario_general/esparcir.jpg` | esparcir | ya’afijmb-, ya’afimbu- | `LEXR-03737` |
| `diccionario_general/especie_de_planta.jpg` | especie de planta | calze tsjũtsj | `LEXR-02257` |
| `diccionario_general/especie_de_árbol.jpg` | especie de árbol | calzec | `LEXR-02881` |
| `diccionario_general/esperar.jpg` | esperar | ũytas, ũytjasu- | `LEXR-01638` |
| `diccionario_general/esperarse,_ponerse_espeso.jpg` | esperarse, ponerse espeso | wata- | `LEXR-03921` |
| `diccionario_general/espesarse,_ponerse_espeso.jpg` | espesarse, ponerse espeso | fitse- | `LEXR-01597` |
| `diccionario_general/espeso.jpg` | espeso | fitse | `LEXR-03229` |
| `diccionario_general/espeso_(miel,_goma,_etc._).jpg` | espeso (miel, goma, etc.) | wata | `LEXR-03156` |
| `diccionario_general/espiar.jpg` | espiar | peetjengu- | `LEXR-03207` |
| `diccionario_general/espiga_de_trigo.jpg` | espiga de trigo | scuutyj spiiga | `LEXR-03121` |
| `diccionario_general/espina_de_cabuya.jpg` | espina de cabuya | bats tsjũtsj | `LEXR-01196` |
| `diccionario_general/espina_dorsal.jpg` | espina dorsal | tsinz dyi’tj | `LEXR-03462` |
| `diccionario_general/espinarse,_chuzar.jpg` | espinarse, chuzar | ucje- | `LEXR-01888` |
| `diccionario_general/esponjarse,_hincharse.jpg` | esponjarse, hincharse | spãpa-, spãpáa- | `LEXR-01087` |
| `diccionario_general/esposa.jpg` | esposa | nyuu | `LEXR-01234` |
| `diccionario_general/esposa_del_primo.jpg` | esposa del primo | pucacje ntsu’wa | `LEXR-03715` |
| `diccionario_general/esposo_de_la_prima.jpg` | esposo de la prima | pucacje ntsu’m | `LEXR-00444` |
| `diccionario_general/espíritus_de_las_quebradas.jpg` | espíritus de las quebradas | quitssuwe’sh | `LEXR-03095` |
| `diccionario_general/esquilar.jpg` | esquilar | cjas waca- | `LEXR-03877` |
| `diccionario_general/esquina_de_la_casa.jpg` | esquina de la casa | yat punza eca | `LEXR-03466` |
| `diccionario_general/esta_generación,_contemporáneos.jpg` | esta generación, contemporáneos | ãchgawe’sh | `LEXR-00669` |
| `diccionario_general/estantillo_de_la_casa.jpg` | estantillo de la casa | yat chinda | `LEXR-00848` |
| `diccionario_general/estar_(parado).jpg` | estar (parado) | ũs-, ũsu- | `LEXR-02738` |
| `diccionario_general/estar_(sentado,_acostado,_coljado),_habitar,_morar.jpg` | estar (sentado, acostado, coljado), habitar, morar | u’p-, u’pu- | `LEXR-03527` |
| `diccionario_general/estar_alentado,_estar_bien.jpg` | estar alentado, estar bien | wẽt fi’nze- | `LEXR-01102` |
| `diccionario_general/estar_ausente.jpg` | estar ausente | mee- | `LEXR-02212` |
| `diccionario_general/estar_callado,_guardar_silencio.jpg` | estar callado, guardar silencio | shuuna’ u’p- | `LEXR-00639` |
| `diccionario_general/estar_contento.jpg` | estar contento | wechana ũs-, wechana u’p- | `LEXR-03550` |
| `diccionario_general/estar_desnivelado.jpg` | estar desnivelado | tjuja- | `LEXR-02501` |
| `diccionario_general/estar_desocupado.jpg` | estar desocupado | tjẽytemée ũs- | `LEXR-03870` |
| `diccionario_general/estar_disgustado.jpg` | estar disgustado | mutsu- | `LEXR-00893` |
| `diccionario_general/estar_embarazada,_encinta.jpg` | estar embarazada, encinta | nasa ji’pj- | `LEXR-00616` |
| `diccionario_general/estar_encarcelado,_detenido.jpg` | estar encarcelado, detenido | jytujnd-, jytundu- | `LEXR-00711` |
| `diccionario_general/estar_enfermo.jpg` | estar enfermo | ãtsã’na ũs- | `LEXR-01703` |
| `diccionario_general/estar_hambriento.jpg` | estar hambriento | wẽepang-, wẽepangúu- | `LEXR-01952` |
| `diccionario_general/estar_medio_colgado.jpg` | estar medio colgado | becuena u’p- | `LEXR-02297` |
| `diccionario_general/estar_ocupado.jpg` | estar ocupado | tjẽyte ũs- | `LEXR-00648` |
| `diccionario_general/estar_panzón.jpg` | estar panzón | buc-, bucu- | `LEXR-00678` |
| `diccionario_general/estar_parado,_de_pie.jpg` | estar parado, de pie | yujurra ũs- | `LEXR-02408` |
| `diccionario_general/estar_renuente,_tener_pereza,_no_tener_ganas.jpg` | estar renuente, tener pereza, no tener ganas | wa’l-, wa’lu- | `LEXR-03782` |
| `diccionario_general/estar_suspendido.jpg` | estar suspendido | belen u’p- | `LEXR-01844` |
| `diccionario_general/estar_triste.jpg` | estar triste | ñusna ũs- | `LEXR-01706` |
| `diccionario_general/este,_esta,_esto.jpg` | este, esta, esto | naa | `LEXR-00979` |
| `diccionario_general/estigma_de_maíz,_pelo_de_maíz.jpg` | estigma de maíz, pelo de maíz | cutyj dycjas | `LEXR-02745` |
| `diccionario_general/estirarse.jpg` | estirarse | jyzuunz-, jyzuunzu- | `LEXR-00515` |
| `diccionario_general/estornudar.jpg` | estornudar | a’tyji’j-, a’tyji’ji- | `LEXR-00676` |
| `diccionario_general/estrangular.jpg` | estrangular | tjuc-, tjucu- | `LEXR-03685` |
| `diccionario_general/estregar.jpg` | estregar | ja’ll-, ja’lli- | `LEXR-01051` |
| `diccionario_general/eucalipto_(árbol).jpg` | eucalipto (árbol) | ucalitu | `LEXR-03273` |
| `diccionario_general/evidentemente,_es_evidente.jpg` | evidentemente, es evidente | ãadyija’ | `LEXR-02250` |
| `diccionario_general/excremento,_estiércol_(de_animal).jpg` | excremento, estiércol (de animal) | ime | `LEXR-02106` |
| `diccionario_general/experimentar_tristeza.jpg` | experimentar tristeza | ñus cnay- | `LEXR-01963` |
| `diccionario_general/explicar,_hacer_entender.jpg` | explicar, hacer entender | caajiyu’j-, caajiyu’ju-(cjiyu’j-) | `LEXR-02517` |
| `diccionario_general/extender_los_brazos.jpg` | extender los brazos | tsja’ya- | `LEXR-02895` |
| `diccionario_general/extraer_muela.jpg` | extraer muela | qui’tj cutyi’j- | `LEXR-03059` |
| `diccionario_general/extranjero,_forastero.jpg` | extranjero, forastero | jyu’juwe’sh | `LEXR-01460` |
| `diccionario_general/extrañarse.jpg` | extrañarse | fiicãj-, fiicãja-, fiicãa- | `LEXR-03878` |
| `diccionario_general/fabricar_vasijas_de_barro.jpg` | fabricar vasijas de barro | mityj um- | `LEXR-00517` |
| `diccionario_general/fama.jpg` | fama | tuutje’jni | `LEXR-01560` |
| `diccionario_general/familia,_los_de_la_casa.jpg` | familia, los de la casa | yaattewe’sh | `LEXR-03738` |
| `diccionario_general/famoso,_personaje_importante.jpg` | famoso, personaje importante | jytujtjesa | `LEXR-02269` |
| `diccionario_general/favor_de._._..jpg` | favor de... | meen | `LEXR-02164` |
| `diccionario_general/favorecer.jpg` | favorecer | ju’ngu yuu- | `LEXR-01916` |
| `diccionario_general/felicitar.jpg` | felicitar | wecha pu’ch- | `LEXR-01338` |
| `diccionario_general/feo,_malo.jpg` | feo, malo | canzh | `LEXR-00863` |
| `diccionario_general/fermentarse.jpg` | fermentarse | pus-, pusúu- | `LEXR-03056` |
| `diccionario_general/fibra_de_cabuya.jpg` | fibra de cabuya | bats yaj | `LEXR-03493` |
| `diccionario_general/filos_por_ambos_lados.jpg` | filos por ambos lados | peepaj zec | `LEXR-02004` |
| `diccionario_general/fingir.jpg` | fingir | sẽ’j-, sẽ’je- | `LEXR-03869` |
| `diccionario_general/fique.jpg` | fique | bajts | `LEXR-03829` |
| `diccionario_general/flaco,_delgado.jpg` | flaco, delgado | tall | `LEXR-01167` |
| `diccionario_general/flamear,_despedir_llamas.jpg` | flamear, despedir llamas | cleechi’ch-, cleechi’chi- | `LEXR-03429` |
| `diccionario_general/fleco_de_la_ruana_o_anaco.jpg` | fleco de la ruana o anaco | atyj wẽsẽ | `LEXR-01195` |
| `diccionario_general/fleco,_borde_de_la_ruana.jpg` | fleco, borde de la ruana | wẽsẽ | `LEXR-03248` |
| `diccionario_general/flojo.jpg` | flojo | lash | `LEXR-03799` |
| `diccionario_general/flojo,_poco_apretado_(tornillo,_cuerda).jpg` | flojo, poco apretado (tornillo, cuerda) | lacy | `LEXR-02211` |
| `diccionario_general/flor_de_maíz.jpg` | flor de maíz | cutyj viits | `LEXR-00596` |
| `diccionario_general/florecer.jpg` | florecer | quite-, quitée- | `LEXR-01880` |
| `diccionario_general/flotar.jpg` | flotar | enda- | `LEXR-02207` |
| `diccionario_general/fondo_de_la_olla.jpg` | fondo de la olla | mityj yuc | `LEXR-03880` |
| `diccionario_general/formar_chupo_(tumor).jpg` | formar chupo (tumor) | mutsu- | `LEXR-00519` |
| `diccionario_general/formar_grano.jpg` | formar grano | cha’cute- | `LEXR-01036` |
| `diccionario_general/formar_granos.jpg` | formar granos | wã’ji- | `LEXR-01267` |
| `diccionario_general/formar_tumor_o_chupo.jpg` | formar tumor o chupo | cuw-, cuwúu- | `LEXR-00405` |
| `diccionario_general/fortalecer.jpg` | fortalecer | nuychjãchja- | `LEXR-01305` |
| `diccionario_general/fortalecer,_animar.jpg` | fortalecer, animar | cchjãachja’j-, cchjãachja’ja- | `LEXR-01368` |
| `diccionario_general/fracturado.jpg` | fracturado | chcateni | `LEXR-03655` |
| `diccionario_general/fracturar.jpg` | fracturar | jypaang- | `LEXR-03586` |
| `diccionario_general/fracturar_(varias_veces_o_en_varias_partes).jpg` | fracturar (varias veces o en varias partes) | shcandende- | `LEXR-01405` |
| `diccionario_general/fracturar_hueso.jpg` | fracturar hueso | chcate- | `LEXR-00684` |
| `diccionario_general/fracturar,_quebrar.jpg` | fracturar, quebrar | shcajnde-, shcande- | `LEXR-03414` |
| `diccionario_general/fracturar,_quebrarse.jpg` | fracturar, quebrarse | shcate- | `LEXR-02443` |
| `diccionario_general/frailejón.jpg` | frailejón | ẽs ets, we’pe ẽs | `LEXR-01188` |
| `diccionario_general/frailejón_(planta).jpg` | frailejón (planta) | we’pe ẽs | `LEXR-03035` |
| `diccionario_general/frecuentemente,_con_frecuencia,_a_menudo.jpg` | frecuentemente, con frecuencia, a menudo | tajta | `LEXR-01487` |
| `diccionario_general/fregado.jpg` | fregado | echech | `LEXR-01859` |
| `diccionario_general/frincir_las_cejas.jpg` | frincir las cejas | cue’nzu-(cue’nzhu-) | `LEXR-03171` |
| `diccionario_general/frotar,_alisar.jpg` | frotar, alisar | plavi’j-, plavi’ji- | `LEXR-00441` |
| `diccionario_general/fríjol_blanco.jpg` | fríjol blanco | us chijme | `LEXR-03303` |
| `diccionario_general/fríjol_cacha.jpg` | fríjol cacha | us tapla, us tsep | `LEXR-00745` |
| `diccionario_general/fríjol_pintado.jpg` | fríjol pintado | us bite | `LEXR-02722` |
| `diccionario_general/fríjol_rojo.jpg` | fríjol rojo | us bej | `LEXR-01263` |
| `diccionario_general/frío.jpg` | frío | finze | `LEXR-00603` |
| `diccionario_general/fuerte.jpg` | fuerte | chjãchja | `LEXR-01715` |
| `diccionario_general/fácil.jpg` | fácil | tjẽymée | `LEXR-02862` |
| `diccionario_general/gallinazo.jpg` | gallinazo | mẽewẽjy | `LEXR-03054` |
| `diccionario_general/ganar,_vencer,_ganar_dinero,_sufrir,_experimentar,_padecer.jpg` | ganar, vencer, ganar dinero, sufrir, experimentar, padecer | cnay-, cnayúu- | `LEXR-03107` |
| `diccionario_general/garra,_uña_(de_pájaro).jpg` | garra, uña (de pájaro) | vichacue vyllill | `LEXR-02185` |
| `diccionario_general/gatear.jpg` | gatear | wẽy-, wẽyíi- | `LEXR-03419` |
| `diccionario_general/gato.jpg` | gato | mish | `LEXR-02049` |
| `diccionario_general/gavilán.jpg` | gavilán | tsalli’ll | `LEXR-03843` |
| `diccionario_general/genir_(repetidas_veces).jpg` | genir (repetidas veces) | tũchji’chji- | `LEXR-03326` |
| `diccionario_general/germen_de_maíz.jpg` | germen de maíz | cutyj ũus | `LEXR-03516` |
| `diccionario_general/glotón.jpg` | glotón | ũ’shic | `LEXR-01578` |
| `diccionario_general/glotón,_comilón.jpg` | glotón, comilón | pũ’we | `LEXR-03317` |
| `diccionario_general/gobernador_del_cauca.jpg` | gobernador del Cauca | Payaate ne’jue’sh | `LEXR-00900` |
| `diccionario_general/gobernador_indígena_del_resguardo.jpg` | gobernador indígena del resguardo | tutjensa (T) | `LEXR-01330` |
| `diccionario_general/golpear_(repetidas_veces),_aglomerarse.jpg` | golpear (repetidas veces), aglomerarse | iica’ca- | `LEXR-01598` |
| `diccionario_general/golpear_(varias_veces).jpg` | golpear (varias veces) | uca’ca- | `LEXR-02681` |
| `diccionario_general/golpear,_chocar_con,_colindar_con.jpg` | golpear, chocar con, colindar con | ijca-, iica- | `LEXR-00794` |
| `diccionario_general/golpear,_tocar_(la_puerta).jpg` | golpear, tocar (la puerta) | pu’tata- | `LEXR-02438` |
| `diccionario_general/gordo.jpg` | gordo | nish | `LEXR-02924` |
| `diccionario_general/gorgojearse.jpg` | gorgojearse | chica-, chicáa- | `LEXR-00397` |
| `diccionario_general/gotear.jpg` | gotear | sund-, sundúu- (tsund-) | `LEXR-01165` |
| `diccionario_general/gozo.jpg` | gozo | wechani | `LEXR-01765` |
| `diccionario_general/granadilla_(fruta).jpg` | granadilla (fruta) | shlalá | `LEXR-03265` |
| `diccionario_general/granadillo.jpg` | granadillo | shlalá | `LEXR-01410` |
| `diccionario_general/grande_(gente).jpg` | grande (gente) | majcy | `LEXR-02431` |
| `diccionario_general/grande,_alto.jpg` | grande, alto | wala | `LEXR-00564` |
| `diccionario_general/grande,_importante.jpg` | grande, importante | wálasa | `LEXR-02729` |
| `diccionario_general/grando_de_maíz.jpg` | grando de maíz | cutyj ñuñ | `LEXR-00876` |
| `diccionario_general/grano.jpg` | grano | cjavy | `LEXR-00777` |
| `diccionario_general/grato.jpg` | grato | wecha | `LEXR-02242` |
| `diccionario_general/grieta,_rendija.jpg` | grieta, rendija | shish | `LEXR-00830` |
| `diccionario_general/grillo.jpg` | grillo | cjã’sh le’ch | `LEXR-00497` |
| `diccionario_general/gris.jpg` | gris | tsẽytsẽy tujme | `LEXR-02338` |
| `diccionario_general/gris,_pardo.jpg` | gris, pardo | tujme | `LEXR-02941` |
| `diccionario_general/gritar.jpg` | gritar | wey-, weyíi- | `LEXR-01015` |
| `diccionario_general/grueso.jpg` | grueso | lepy | `LEXR-02816` |
| `diccionario_general/grueso_y_alto.jpg` | grueso y alto | majcymajcy | `LEXR-02753` |
| `diccionario_general/guacamayo.jpg` | guacamayo | well wala | `LEXR-03576` |
| `diccionario_general/guache_(culebra).jpg` | guache (culebra) | ul tsẽy | `LEXR-03596` |
| `diccionario_general/guagua,_paca_(mamífero_roedor).jpg` | guagua, paca (mamífero roedor) | ñu’py wala | `LEXR-02642` |
| `diccionario_general/guama.jpg` | guama | afy | `LEXR-02353` |
| `diccionario_general/guamo.jpg` | guamo | afy | `LEXR-03007` |
| `diccionario_general/guantín_(mamífero_roedor).jpg` | guantín (mamífero roedor) | lanzh | `LEXR-02318` |
| `diccionario_general/guardar,_cruzar_los_brazos.jpg` | guardar, cruzar los brazos | jyaw-, jyawúu- | `LEXR-01053` |
| `diccionario_general/guasca_de_fique.jpg` | guasca de fique | bats wes | `LEXR-00386` |
| `diccionario_general/guayaba_(fruta).jpg` | guayaba (fruta) | pquiinda | `LEXR-03868` |
| `diccionario_general/gusano.jpg` | gusano | wes | `LEXR-00844` |
| `diccionario_general/gusano_venenoso.jpg` | gusano venenoso | uschic | `LEXR-02592` |
| `diccionario_general/guía.jpg` | guía | pe’jna u’jsa | `LEXR-00811` |
| `diccionario_general/haba.jpg` | haba | apas | `LEXR-03469` |
| `diccionario_general/haber_derrumbe.jpg` | haber derrumbe | ejy u’j- | `LEXR-02697` |
| `diccionario_general/haber_eclipse_de_luna.jpg` | haber eclipse de luna | a’te uu- | `LEXR-02148` |
| `diccionario_general/haber_eclipse_de_sol.jpg` | haber eclipse de sol | sec shi’ndy- | `LEXR-01616` |
| `diccionario_general/haber_temblor,_terremoto.jpg` | haber temblor, terremoto | ejnd u’j- | `LEXR-01860` |
| `diccionario_general/habitante_de_tierradentro.jpg` | habitante de Tierradentro | ũyuwe’sh | `LEXR-01106` |
| `diccionario_general/habitante_del_pueblo.jpg` | habitante del pueblo | shambsá | `LEXR-01618` |
| `diccionario_general/habitante,_morador.jpg` | habitante, morador | u’psa | `LEXR-03033` |
| `diccionario_general/hablar_contra_otro.jpg` | hablar contra otro | atsewe’we | `LEXR-01361` |
| `diccionario_general/hablar_en_voz_alta.jpg` | hablar en voz alta | sus we’we- | `LEXR-01821` |
| `diccionario_general/hablar_en_voz_baja.jpg` | hablar en voz baja | susmée we’we- | `LEXR-02825` |
| `diccionario_general/hablar_mal.jpg` | hablar mal | fiy we’we- | `LEXR-00787` |
| `diccionario_general/hace_tiempo.jpg` | hace tiempo | tyach (cyach) | `LEXR-02402` |
| `diccionario_general/hacer_abrir.jpg` | hacer abrir | caapjande’j-, caapjande’je-(cpjandej-) | `LEXR-01906` |
| `diccionario_general/hacer_abundar.jpg` | hacer abundar | caapena’j-, caapena’ja | `LEXR-03695` |
| `diccionario_general/hacer_acercar,_arrimar.jpg` | hacer acercar, arrimar | cuutya’j-, cuutya’ja- | `LEXR-01722` |
| `diccionario_general/hacer_amarrar.jpg` | hacer amarrar | caytundu’j-, caytundu’ju- | `LEXR-00866` |
| `diccionario_general/hacer_amontonar.jpg` | hacer amontonar | cmuutsu’j-, cmuutsu’ju- | `LEXR-02364` |
| `diccionario_general/hacer_ampollas.jpg` | hacer ampollas | shcambish-, shcambishíi- | `LEXR-02334` |
| `diccionario_general/hacer_andar.jpg` | hacer andar | caau’j-, caau’ju- | `LEXR-03129` |
| `diccionario_general/hacer_aparar.jpg` | hacer aparar | caapaatje’j-, caapaatje’je- | `LEXR-00585` |
| `diccionario_general/hacer_arrastrar.jpg` | hacer arrastrar | cweenzhi’j-, cweenzhi’ji- | `LEXR-01447` |
| `diccionario_general/hacer_arrear.jpg` | hacer arrear | cyaatsqui’pu’j-, cyaatsqui’pu’ju- | `LEXR-00500` |
| `diccionario_general/hacer_arreglar.jpg` | hacer arreglar | caapjeu’j-, caapjeu’ju- | `LEXR-01712` |
| `diccionario_general/hacer_arrodillar.jpg` | hacer arrodillar | caapẽjyucue’j-, caapẽjyucue’je- | `LEXR-02603` |
| `diccionario_general/hacer_asar.jpg` | hacer asar | caacjacje’j-, caacjacje’je- | `LEXR-02740` |
| `diccionario_general/hacer_atajar,_mandar_atajar.jpg` | hacer atajar, mandar atajar | cyuupu’j-, cyuupu’ju- | `LEXR-00781` |
| `diccionario_general/hacer_ayudar,_permitir_ayudar.jpg` | hacer ayudar, permitir ayudar | caapu’chji’j-, caapu’chji’ji-(cpu’chji’j-) | `LEXR-02911` |
| `diccionario_general/hacer_bailar.jpg` | hacer bailar | caacu’ju’j-, caacu’ju’ju- | `LEXR-03012` |
| `diccionario_general/hacer_bajar_(dese_arriba).jpg` | hacer bajar (dese arriba) | caaquĩiji’j-, caaquĩiji’ji- | `LEXR-01115` |
| `diccionario_general/hacer_barbacoa.jpg` | hacer barbacoa | atũju’j- | `LEXR-02151` |
| `diccionario_general/hacer_barro.jpg` | hacer barro | tyiityi’j- | `LEXR-01092` |
| `diccionario_general/hacer_basura_o_polvo.jpg` | hacer basura o polvo | cytã’ja’j-, cytã’ja’ja- | `LEXR-02425` |
| `diccionario_general/hacer_bañar_(a_otro).jpg` | hacer bañar (a otro) | cpẽeu’j-, cpẽeu’ju- | `LEXR-03706` |
| `diccionario_general/hacer_beber.jpg` | hacer beber | caatundyi’j-, caatundyi’ji | `LEXR-03705` |
| `diccionario_general/hacer_bostezar.jpg` | hacer bostezar | cdeewayi’j-, cdeewayi’ji- | `LEXR-03165` |
| `diccionario_general/hacer_brotar.jpg` | hacer brotar | cbuucha’j-, cbuucha’ja- | `LEXR-01279` |
| `diccionario_general/hacer_caer,_dejar_caer.jpg` | hacer caer, dejar caer | cweete’j-, cweete’je- | `LEXR-02369` |
| `diccionario_general/hacer_callar.jpg` | hacer callar | caashuuna’j-, caashuuna’ja- | `LEXR-02417` |
| `diccionario_general/hacer_calor.jpg` | hacer calor | acha yuu- | `LEXR-01191` |
| `diccionario_general/hacer_cambiar.jpg` | hacer cambiar | caayu’ptje’j-, caayu’ptje’je- | `LEXR-01845` |
| `diccionario_general/hacer_cantar.jpg` | hacer cantar | cmeemu’j-, cmeemu’ju- | `LEXR-00692` |
| `diccionario_general/hacer_cargar_(ej._niño,_en_el_bautismo).jpg` | hacer cargar (ej. niño, en el bautismo) | cyaacje’j-, cyaacje’je- | `LEXR-03227` |
| `diccionario_general/hacer_cargar,_echar_carga.jpg` | hacer cargar, echar carga | ctũ’se’j-, ctũ’se’je- | `LEXR-00694` |
| `diccionario_general/hacer_casa.jpg` | hacer casa | yaatu’j-, yaatu’ju- | `LEXR-00570` |
| `diccionario_general/hacer_casarse.jpg` | hacer casarse | caaptamu’j-, caaptamu’ju- | `LEXR-02519` |
| `diccionario_general/hacer_chicha.jpg` | hacer chicha | beca’j-, beca’ja- | `LEXR-03310` |
| `diccionario_general/hacer_chupar,_desinflamar.jpg` | hacer chupar, desinflamar | cchaanzha’j-, cchaanzha’ja- | `LEXR-00954` |
| `diccionario_general/hacer_clavar,_mandar_crucificar.jpg` | hacer clavar, mandar crucificar | caafyutsu’j-, caafyutsu’ju- | `LEXR-00859` |
| `diccionario_general/hacer_cocer.jpg` | hacer cocer | caaĩitse’j-, caaĩtse’je- | `LEXR-02094` |
| `diccionario_general/hacer_coger,_hacer_prender.jpg` | hacer coger, hacer prender | cuwe’j-, cuwe’je- | `LEXR-03730` |
| `diccionario_general/hacer_confrontar.jpg` | hacer confrontar | caacndyi’pu’j-, caacndyi’pu’ju- | `LEXR-01198` |
| `diccionario_general/hacer_correr.jpg` | hacer correr | cwuuwu’j-, cwuuwu’ju- | `LEXR-03110` |
| `diccionario_general/hacer_cortar_(palo).jpg` | hacer cortar (palo) | caatwaca’j-, caatwaca’ja- | `LEXR-01586` |
| `diccionario_general/hacer_coser.jpg` | hacer coser | caatsu’j-, caatsu’ju- | `LEXR-03889` |
| `diccionario_general/hacer_cosquillas.jpg` | hacer cosquillas | lech-, lechíi- | `LEXR-00420` |
| `diccionario_general/hacer_creer.jpg` | hacer creer | caacreĩ’j-, caacreĩ’ji- | `LEXR-02910` |
| `diccionario_general/hacer_cubrir.jpg` | hacer cubrir | cya’patje’j-, cya’patje’je- | `LEXR-03173` |
| `diccionario_general/hacer_cubrirse.jpg` | hacer cubrirse | caapã’chi’j-, caapã’chi’ji-(cpã’chi’j-) | `LEXR-01778` |
| `diccionario_general/hacer_dar_de_tomar.jpg` | hacer dar de tomar | cyuusu’j-, cyuusu’ju- | `LEXR-02843` |
| `diccionario_general/hacer_dar_vuelta.jpg` | hacer dar vuelta | caata’ngu’j-, caata’ngu’ju-(cta’ngu’j-) | `LEXR-00679` |
| `diccionario_general/hacer_dañar.jpg` | hacer dañar | csuuwu’j-, csuuwu’ju- | `LEXR-02471` |
| `diccionario_general/hacer_daño_a_una_persona,_agredir.jpg` | hacer daño a una persona, agredir | ptjãawe- | `LEXR-00906` |
| `diccionario_general/hacer_dejar.jpg` | hacer dejar | caanviitu’j-, caanviitu’ju- | `LEXR-02693` |
| `diccionario_general/hacer_demorar,_atrasar.jpg` | hacer demorar, atrasar | caytẽeyu´j-, caytẽeyu´ju- | `LEXR-02913` |
| `diccionario_general/hacer_derretir.jpg` | hacer derretir | caapquivi’j-, caapquivi’ji- | `LEXR-03741` |
| `diccionario_general/hacer_descansar,_aliviar,_calmar.jpg` | hacer descansar, aliviar, calmar | caycase´j-, caycase´je- | `LEXR-02418` |
| `diccionario_general/hacer_econtrarse.jpg` | hacer econtrarse | caapuutyuyu’j-, caapuutyuyu’ju- | `LEXR-02947` |
| `diccionario_general/hacer_encarar.jpg` | hacer encarar | caapdyi’pu’j-, caapdyi’pju’ju- | `LEXR-03515` |
| `diccionario_general/hacer_endeudar.jpg` | hacer endeudar | caayulu’j-, caayulu’ju-(cyulu’j-) | `LEXR-03221` |
| `diccionario_general/hacer_engordar.jpg` | hacer engordar | caañiishi’j-, caañiishi’ji-(cniishi’j-) | `LEXR-01587` |
| `diccionario_general/hacer_enojar,_ofender.jpg` | hacer enojar, ofender | caaũuscha’j-, caaũuscha’ja- | `LEXR-02840` |
| `diccionario_general/hacer_entregar.jpg` | hacer entregar | cduucje’j-, cduucje’je- | `LEXR-00682` |
| `diccionario_general/hacer_envolver.jpg` | hacer envolver | caayapu’j-, caayapu’ju- | `LEXR-02255` |
| `diccionario_general/hacer_eructar.jpg` | hacer eructar | ctu’fi’j-, ctu’fi’ji- | `LEXR-00402` |
| `diccionario_general/hacer_escapar,_dejar_escapar.jpg` | hacer escapar, dejar escapar | quiiyu’j-, quiiyu’ju- | `LEXR-00916` |
| `diccionario_general/hacer_escribir.jpg` | hacer escribir | cfi’ja’j-, cfi’ja’ja- | `LEXR-03556` |
| `diccionario_general/hacer_escupir.jpg` | hacer escupir | caavi’j-, caavi’ji- | `LEXR-01514` |
| `diccionario_general/hacer_estallar,_detonar.jpg` | hacer estallar, detonar | cãapa’j-, cãapa’ja- | `LEXR-00597` |
| `diccionario_general/hacer_estanque.jpg` | hacer estanque | ĩicja’j-, ĩicja’ja- | `LEXR-02251` |
| `diccionario_general/hacer_estornudar.jpg` | hacer estornudar | ca’tyji’j-, ca’tyji’ji- | `LEXR-03495` |
| `diccionario_general/hacer_estrechar_la_mano_(ej._en_las_bodas).jpg` | hacer estrechar la mano (ej. en las bodas) | cũupjũj-, cũupjũju- | `LEXR-03499` |
| `diccionario_general/hacer_extender_los_brazos.jpg` | hacer extender los brazos | ctsja’jya’j-, ctsja’jya’ja- | `LEXR-01785` |
| `diccionario_general/hacer_extraer.jpg` | hacer extraer | caacutyi’j-, caacutyi’ji- | `LEXR-03191` |
| `diccionario_general/hacer_fiesta.jpg` | hacer fiesta | fiesta’ja- | `LEXR-03603` |
| `diccionario_general/hacer_firmar.jpg` | hacer firmar | caafirmaĩ’j-, caafirmaĩ’ji- | `LEXR-03770` |
| `diccionario_general/hacer_firme,_apuntalar.jpg` | hacer firme, apuntalar | cpu’quitje’j-, cpu’quitjej’e- | `LEXR-00498` |
| `diccionario_general/hacer_florecer.jpg` | hacer florecer | nuyquite, nuyquitée- | `LEXR-01743` |
| `diccionario_general/hacer_frío.jpg` | hacer frío | etse yuu | `LEXR-00506` |
| `diccionario_general/hacer_ganar.jpg` | hacer ganar | caacnayu’j-, caacnayu’ju- | `LEXR-02566` |
| `diccionario_general/hacer_gastar.jpg` | hacer gastar | caagastaĩ’j-, caagastaĩ’jji- | `LEXR-01511` |
| `diccionario_general/hacer_girar.jpg` | hacer girar | caatandyi’j-, caatyandyi’ji-(ctaandyi’j-) | `LEXR-01907` |
| `diccionario_general/hacer_gotear.jpg` | hacer gotear | caaquityi’j-, caaquityi’ji- | `LEXR-03847` |
| `diccionario_general/hacer_gritar.jpg` | hacer gritar | cweeyi’j-, cweeyi’ji- | `LEXR-01787` |
| `diccionario_general/hacer_guardar.jpg` | hacer guardar | cyu’acje’j-, cyu’acje’je- | `LEXR-02953` |
| `diccionario_general/hacer_invierno.jpg` | hacer invierno | nusu-, nusúu- | `LEXR-03681` |
| `diccionario_general/hacer_lavar_las_manos.jpg` | hacer lavar las manos | caacwecha’j-, caacwecha’ja- | `LEXR-03331` |
| `diccionario_general/hacer_llegar.jpg` | hacer llegar | caapa’ja’j-, caapa’ja’ja-(cpa’ja’j-) | `LEXR-03725` |
| `diccionario_general/hacer_lloar.jpg` | hacer lloar | ca’ne’j-, ca’en’je- | `LEXR-02465` |
| `diccionario_general/hacer_llover.jpg` | hacer llover | nus jyamby- | `LEXR-01742` |
| `diccionario_general/hacer_lo_indebido.jpg` | hacer lo indebido | achamée yũu- | `LEXR-03739` |
| `diccionario_general/hacer_masticar,_hacer_morder.jpg` | hacer masticar, hacer morder | caawa’qui’j-, caawa’qui’ji- | `LEXR-01277` |
| `diccionario_general/hacer_mazamorra.jpg` | hacer mazamorra | cjashi’j-, cjashi’ji- | `LEXR-00589` |
| `diccionario_general/hacer_medir,_hacer_contar,_hacer_probar.jpg` | hacer medir, hacer contar, hacer probar | quiisa’j-, quiisa’ja- | `LEXR-01552` |
| `diccionario_general/hacer_menear.jpg` | hacer menear | caawũwu’j-, caawũwu’ju- | `LEXR-03598` |
| `diccionario_general/hacer_mermar.jpg` | hacer mermar | nuyũuchi- | `LEXR-00720` |
| `diccionario_general/hacer_montar.jpg` | hacer montar | ca’ga’j-, ca’ja’ja- | `LEXR-00947` |
| `diccionario_general/hacer_muecas.jpg` | hacer muecas | jyũ’nzh-, jyũ’nzhi- | `LEXR-02317` |
| `diccionario_general/hacer_obedecer.jpg` | hacer obedecer | caanwẽese’j-, caanwẽese’je-(cnwẽese’j-) | `LEXR-03597` |
| `diccionario_general/hacer_olvidar.jpg` | hacer olvidar | caapechcanu’j-, caapechcanu’ju- | `LEXR-00770` |
| `diccionario_general/hacer_pagar.jpg` | hacer pagar | cdeewe’j-, cdeewe’je- | `LEXR-01515` |
| `diccionario_general/hacer_parar.jpg` | hacer parar | ctiishi’j-, ctiishi’ji- | `LEXR-01445` |
| `diccionario_general/hacer_parar,_hacer_detenerse.jpg` | hacer parar, hacer detenerse | cyuuju’j-, cyuuju’ju- | `LEXR-02529` |
| `diccionario_general/hacer_pasar_por_(ej._el_río).jpg` | hacer pasar por (ej. el río) | caauycjeũ’j-, caauycjeũ’ju- | `LEXR-03282` |
| `diccionario_general/hacer_pelear.jpg` | hacer pelear | caapuí’j-, caapuíji- | `LEXR-02200` |
| `diccionario_general/hacer_pensar.jpg` | hacer pensar | caaũusutje’j-, caaũusutje’je- | `LEXR-03807` |
| `diccionario_general/hacer_pliegues.jpg` | hacer pliegues | cseembu’j-, cseembu’ju- | `LEXR-03254` |
| `diccionario_general/hacer_poner_(sombrero).jpg` | hacer poner (sombrero) | caafĩcje’j-, caafĩcje’je- | `LEXR-02466` |
| `diccionario_general/hacer_ponr,_mandar_ponder.jpg` | hacer ponr, mandar ponder | ctyaaja’j-, ctyaaja’ja- | `LEXR-03707` |
| `diccionario_general/hacer_que_otro_lo_fortalece.jpg` | hacer que otro lo fortalece | nuycchijãachja’j-, nuycchjãachja’ja- | `LEXR-03087` |
| `diccionario_general/hacer_quemar.jpg` | hacer quemar | caacambu’j’, caacambu’ju- | `LEXR-01645` |
| `diccionario_general/hacer_quitar.jpg` | hacer quitar | caaquiisu’j-, caaquiisu’ju- | `LEXR-01201` |
| `diccionario_general/hacer_rayas,_pintar.jpg` | hacer rayas, pintar | peendu’j-, peendu’ju- | `LEXR-00439` |
| `diccionario_general/hacer_recordar.jpg` | hacer recordar | caayaqui’j-, caayaqui’ji- | `LEXR-00391` |
| `diccionario_general/hacer_regalar.jpg` | hacer regalar | caapeesu’j-, caapeesu’ju- | `LEXR-02467` |
| `diccionario_general/hacer_regar.jpg` | hacer regar | caacpũushi’j-, caacpũushi’ji- | `LEXR-01971` |
| `diccionario_general/hacer_rendir_más,_hacer_que_abunde.jpg` | hacer rendir más, hacer que abunde | nuypejna-, nuypena- | `LEXR-01233` |
| `diccionario_general/hacer_rezar.jpg` | hacer rezar | caalisa’j-, caalisa’ja- | `LEXR-03771` |
| `diccionario_general/hacer_reír.jpg` | hacer reír | cshiica’j-, cshiica’ja- | `LEXR-02261` |
| `diccionario_general/hacer_rodar.jpg` | hacer rodar | cpeelu’j-, cpeelu’ju- | `LEXR-00960` |
| `diccionario_general/hacer_ruido.jpg` | hacer ruido | sus-, susu- | `LEXR-02231` |
| `diccionario_general/hacer_ruido,_retumbar.jpg` | hacer ruido, retumbar | bu’mbu- | `LEXR-01364` |
| `diccionario_general/hacer_saludar.jpg` | hacer saludar | cweecha’j-, cweecha’ja- | `LEXR-02746` |
| `diccionario_general/hacer_sanar.jpg` | hacer sanar | caywẽtu’j-, caywẽtu’ju- | `LEXR-03014` |
| `diccionario_general/hacer_sentarse.jpg` | hacer sentarse | caachji’j-, caachi’ji- | `LEXR-01646` |
| `diccionario_general/hacer_sentir_incapaz.jpg` | hacer sentir incapaz | caashingu’j-, caashingu’ju- | `LEXR-02093` |
| `diccionario_general/hacer_servir,_ocupar,_utilizar,_usar.jpg` | hacer servir, ocupar, utilizar, usar | cseelpi’j-. cseelpi’ji- | `LEXR-01371` |
| `diccionario_general/hacer_seña.jpg` | hacer seña | bajy we’we- | `LEXR-02805` |
| `diccionario_general/hacer_señas.jpg` | hacer señas | quimbe’je’j-, quimbe’je’je- | `LEXR-00992` |
| `diccionario_general/hacer_señas_(con_la_mirada),_guiñar.jpg` | hacer señas (con la mirada), guiñar | csẽ’sẽ- | `LEXR-02655` |
| `diccionario_general/hacer_sombra.jpg` | hacer sombra | iipshũ’j-, iipshũ’ju- | `LEXR-02533` |
| `diccionario_general/hacer_sombra,_ocultarse.jpg` | hacer sombra, ocultarse | pshũu- | `LEXR-02967` |
| `diccionario_general/hacer_sonar_(maraca).jpg` | hacer sonar (maraca) | caasyũyũj-, caasyũyũju- | `LEXR-01366` |
| `diccionario_general/hacer_subir.jpg` | hacer subir | caateca-j-, caateca’ja- | `LEXR-01512` |
| `diccionario_general/hacer_tener,_hacer_concebir.jpg` | hacer tener, hacer concebir | cji’pju’j-, cji’pju’ju | `LEXR-02522` |
| `diccionario_general/hacer_toser.jpg` | hacer toser | cpjãaja’j-, cpjãaja’ja- | `LEXR-03862` |
| `diccionario_general/hacer_trabajar,_obligar_a_trabajar.jpg` | hacer trabajar, obligar a trabajar | cmaajĩ’j-,cmaajĩ’ji | `LEXR-01979` |
| `diccionario_general/hacer_tragar.jpg` | hacer tragar | caycjẽj-, caycjẽ´jẽ- | `LEXR-00587` |
| `diccionario_general/hacer_tropezar.jpg` | hacer tropezar | cyu’chafi’j-, cyu’chafi’ji- | `LEXR-01856` |
| `diccionario_general/hacer_un_rito_(brujo).jpg` | hacer un rito (brujo) | mestláa- | `LEXR-03679` |
| `diccionario_general/hacer_unir.jpg` | hacer unir | caaviitse’j-, caaviitse’je- | `LEXR-02567` |
| `diccionario_general/hacer_ver.jpg` | hacer ver | caauyu’j-, caauyu’ju- | `LEXR-03101` |
| `diccionario_general/hacer_ver,_hacer_mirar.jpg` | hacer ver, hacer mirar | ctjeengu’j-, ctjeengu’ju- | `LEXR-03108` |
| `diccionario_general/hacer_verano,_hacer_sol.jpg` | hacer verano, hacer sol | secúu- | `LEXR-02442` |
| `diccionario_general/hacer_vestir.jpg` | hacer vestir | caatje’j-, caatje’je- | `LEXR-00586` |
| `diccionario_general/hacer_vivir.jpg` | hacer vivir | caafi’nze’j-, caafi’nze’je-(cfi’nze’j-) | `LEXR-01199` |
| `diccionario_general/hacer_vomitar.jpg` | hacer vomitar | caacpunga’j-, caacpunga’ja- | `LEXR-03470` |
| `diccionario_general/hacer,_actuar,_realizar.jpg` | hacer, actuar, realizar | yũu- | `LEXR-02085` |
| `diccionario_general/hacerse_mataduras.jpg` | hacerse mataduras | tupite- | `LEXR-03065` |
| `diccionario_general/hacerse_pedazos.jpg` | hacerse pedazos | pe’late- | `LEXR-01607` |
| `diccionario_general/hacerse_pedazos,_despedazarse.jpg` | hacerse pedazos, despedazarse | pe’ltete- | `LEXR-00812` |
| `diccionario_general/hacerse_responsable_por_otro.jpg` | hacerse responsable por otro | iipa’j-, iipe’je- | `LEXR-02532` |
| `diccionario_general/hacerse_tarde,_tardar.jpg` | hacerse tarde, tardar | jycuusu- | `LEXR-02617` |
| `diccionario_general/haciendo_bien.jpg` | haciendo bien | ew yũuna | `LEXR-02159` |
| `diccionario_general/haciendo_mal.jpg` | haciendo mal | ewmée yũuna | `LEXR-02104` |
| `diccionario_general/halar_(repetidas_veces).jpg` | halar (repetidas veces) | wenzhi’nzhi- | `LEXR-00568` |
| `diccionario_general/halar,_arrastrar.jpg` | halar, arrastrar | wenzh-, wezhíi- | `LEXR-01695` |
| `diccionario_general/harina_de_maíz.jpg` | harina de maíz | cutyj ũ’we | `LEXR-03079` |
| `diccionario_general/harina_de_trigo.jpg` | harina de trigo | scuutyj ũ’we | `LEXR-03060` |
| `diccionario_general/harina_de_yuca.jpg` | harina de yuca | ña ũ’we | `LEXR-00850` |
| `diccionario_general/hartarse.jpg` | hartarse | cuuta’j-, cuuta’ja- | `LEXR-01595` |
| `diccionario_general/hartarse,_saciarse.jpg` | hartarse, saciarse | tyic-, tyicu- | `LEXR-03632` |
| `diccionario_general/hasta.jpg` | hasta | -pcach | `LEXR-00481` |
| `diccionario_general/hechizar.jpg` | hechizar | cne’s- | `LEXR-01518` |
| `diccionario_general/hecho.jpg` | hecho | vitni | `LEXR-02139` |
| `diccionario_general/hemorragia_nasal.jpg` | hemorragia nasal | ĩts yachni | `LEXR-02647` |
| `diccionario_general/hendir,_abrir_hendedura.jpg` | hendir, abrir hendedura | petsete- (petsate-) | `LEXR-01241` |
| `diccionario_general/herido.jpg` | herido | cpãvitni | `LEXR-02525` |
| `diccionario_general/herirse,_lastimarse.jpg` | herirse, lastimarse | ya’cpã’yuu- | `LEXR-03395` |
| `diccionario_general/hermano_con_hermana.jpg` | hermano con hermana | pdyiy | `LEXR-01675` |
| `diccionario_general/hermano_con_hermano,_o_hermana_con_hermana.jpg` | hermano con hermano, o hermana con hermana | pyacj | `LEXR-00634` |
| `diccionario_general/hermano,_hermana_(del_mismo_sexo).jpg` | hermano, hermana (del mismo sexo) | nyacj | `LEXR-01667` |
| `diccionario_general/herrero.jpg` | herrero | tsam tutsa | `LEXR-02072` |
| `diccionario_general/hervido.jpg` | hervido | cbajy | `LEXR-00867` |
| `diccionario_general/hervir.jpg` | hervir | clala- | `LEXR-03105` |
| `diccionario_general/hervir,_dejar_hervir.jpg` | hervir, dejar hervir | cambi´j-, cambi´ji- | `LEXR-01846` |
| `diccionario_general/hiel.jpg` | hiel | wãjy | `LEXR-01101` |
| `diccionario_general/hierbabuena_(planta).jpg` | hierbabuena (planta) | putatyjã’ | `LEXR-01403` |
| `diccionario_general/hija_mayor.jpg` | hija mayor | niisa ntjẽjsa | `LEXR-02704` |
| `diccionario_general/hija_menor.jpg` | hija menor | niisa nuuchsa | `LEXR-01741` |
| `diccionario_general/hijastra.jpg` | hijastra | niisa npaasa | `LEXR-03118` |
| `diccionario_general/hijastro.jpg` | hijastro | nchi’c npaasa | `LEXR-00895` |
| `diccionario_general/hilar.jpg` | hilar | pund-, pundúu- | `LEXR-02061` |
| `diccionario_general/hilo.jpg` | hilo | ilu | `LEXR-02105` |
| `diccionario_general/hincharse.jpg` | hincharse | tsu’vy, tsu’vi- (tsũ’vy-) | `LEXR-02796` |
| `diccionario_general/hinchazón.jpg` | hinchazón | tsu’vy | `LEXR-02279` |
| `diccionario_general/hoja_de_arbusto.jpg` | hoja de arbusto | ẽjyã ets | `LEXR-02253` |
| `diccionario_general/hoja_de_mejicano_(da_sabor_a_la_mazamorra).jpg` | hoja de mejicano (da sabor a la mazamorra) | peets tyjã’ | `LEXR-01155` |
| `diccionario_general/hormiga.jpg` | hormiga | cjã’cjã | `LEXR-02259` |
| `diccionario_general/hormiga_grande_(insecto).jpg` | hormiga grande (insecto) | inz | `LEXR-01793` |
| `diccionario_general/hospedar.jpg` | hospedar | paandej-, paandeje- | `LEXR-01928` |
| `diccionario_general/hoy,_ahora,_recién.jpg` | hoy, ahora, recién | ãchj | `LEXR-00940` |
| `diccionario_general/hueco.jpg` | hueco | quiwe pwa’ | `LEXR-00447` |
| `diccionario_general/hueso_de_la_nuca.jpg` | hueso de la nuca | tyjicj dyi’yj | `LEXR-03032` |
| `diccionario_general/huevo_crudo.jpg` | huevo crudo | zits ĩquĩ | `LEXR-01702` |
| `diccionario_general/humear.jpg` | humear | shi’ta- | `LEXR-01407` |
| `diccionario_general/humedecerse.jpg` | humedecerse | tupjáa- | `LEXR-00928` |
| `diccionario_general/hundirse,_zambullirse.jpg` | hundirse, zambullirse | jypenda-, jypeendáa- | `LEXR-01867` |
| `diccionario_general/huésped.jpg` | huésped | paandeesa | `LEXR-00621` |
| `diccionario_general/húmedo.jpg` | húmedo | le’le | `LEXR-00610` |
| `diccionario_general/ida.jpg` | ida | u’jni | `LEXR-01825` |
| `diccionario_general/igual.jpg` | igual | fiymée | `LEXR-02480` |
| `diccionario_general/igualar_(el_peso),_comparar.jpg` | igualar (el peso), comparar | caaja’nda’j-, caaja’nda’ja- | `LEXR-00948` |
| `diccionario_general/iluminación.jpg` | iluminación | cweetjnisa | `LEXR-02610` |
| `diccionario_general/imitar,_remedar.jpg` | imitar, remedar | shi’nd-, shi’ndu- | `LEXR-01250` |
| `diccionario_general/impartir_(luz,_calor,_frío).jpg` | impartir (luz, calor, frío) | cu’w-, cu’wu- | `LEXR-01718` |
| `diccionario_general/inclinar_la_cabeza.jpg` | inclinar la cabeza | quĩitsju- | `LEXR-03149` |
| `diccionario_general/incomodarse.jpg` | incomodarse | ũuscha yajcy- | `LEXR-01899` |
| `diccionario_general/indicar,_señalar_(con_el_dedo).jpg` | indicar, señalar (con el dedo) | vijya-, viya- | `LEXR-01890` |
| `diccionario_general/indigino,_deficiente.jpg` | indigino, deficiente | ãjmeesa, ãjmeecuẽsa | `LEXR-00670` |
| `diccionario_general/indígena_guambiano.jpg` | indígena guambiano | muuwe’sh | `LEXR-03800` |
| `diccionario_general/infanticida.jpg` | infanticida | luuch icjsa | `LEXR-01737` |
| `diccionario_general/inferior.jpg` | inferior | achamée | `LEXR-03006` |
| `diccionario_general/inflamarse.jpg` | inflamarse | tu’cu- | `LEXR-00553` |
| `diccionario_general/inmenso.jpg` | inmenso | iiméj wala | `LEXR-00414` |
| `diccionario_general/inmortal.jpg` | inmortal | uuwa’jmeesa | `LEXR-03246` |
| `diccionario_general/inocente.jpg` | inocente | yuuwemeesa | `LEXR-02832` |
| `diccionario_general/insertar.jpg` | insertar | se’w- | `LEXR-00918` |
| `diccionario_general/insinuar,_hablar_indirectamente_de_otro.jpg` | insinuar, hablar indirectamente de otro | pa’jy we’we- | `LEXR-00809` |
| `diccionario_general/inspector.jpg` | inspector | cleecytul (T) | `LEXR-03043` |
| `diccionario_general/instrumento_para_matar.jpg` | instrumento para matar | icjni | `LEXR-03405` |
| `diccionario_general/insuficiente,_incompleto,_menos.jpg` | insuficiente, incompleto, menos | ãjmée | `LEXR-03373` |
| `diccionario_general/insultar,_ultrajar.jpg` | insultar, ultrajar | wẽeshúu- | `LEXR-03824` |
| `diccionario_general/inteligente.jpg` | inteligente | jiisa | `LEXR-02045` |
| `diccionario_general/intervenir.jpg` | intervenir | paanwe’we- | `LEXR-02964` |
| `diccionario_general/intervenir_(en_una_conversación).jpg` | intervenir (en una conversación) | cpaawe’we | `LEXR-00779` |
| `diccionario_general/invierno.jpg` | invierno | nus en | `LEXR-00981` |
| `diccionario_general/invisible.jpg` | invisible | vyaasamée | `LEXR-01010` |
| `diccionario_general/invitar_a_varias_personas.jpg` | invitar a varias personas | pi’qui’cy-, pi’qui’qui- | `LEXR-01875` |
| `diccionario_general/invitar,_convidar.jpg` | invitar, convidar | jypi’cy-, jypi’qui- | `LEXR-00887` |
| `diccionario_general/inútil,_inservible.jpg` | inútil, inservible | seelpimeesa | `LEXR-02995` |
| `diccionario_general/ir_y_venir_(varias_veces).jpg` | ir y venir (varias veces) | shawendu’ndu- | `LEXR-03593` |
| `diccionario_general/ir,_aprovechando_la_oportunidad_de_acompañar_a_otro.jpg` | ir, aprovechando la oportunidad de acompañar a otro | paau’j-, paau’jue- | `LEXR-01468` |
| `diccionario_general/ir,_irse.jpg` | ir, irse | u’j-, u’jue- | `LEXR-00741` |
| `diccionario_general/jactarse,_hablar_con_orgullo.jpg` | jactarse, hablar con orgullo | iiwejch we’we- | `LEXR-03085` |
| `diccionario_general/jadear,_respirar_con_dificultad.jpg` | jadear, respirar con dificultad | ũuse’se- | `LEXR-01437` |
| `diccionario_general/jardín.jpg` | jardín | quite ej | `LEXR-01315` |
| `diccionario_general/jigra_con_huecos_grandes.jpg` | jigra con huecos grandes | cumby ya’ja | `LEXR-03172` |
| `diccionario_general/jigra_de_colores.jpg` | jigra de colores | ya’ja bite | `LEXR-03844` |
| `diccionario_general/jigra_tejida_con_agujas_grandes.jpg` | jigra tejida con agujas grandes | molta ya’ja | `LEXR-01996` |
| `diccionario_general/jinete,_que_monta_a_caballo.jpg` | jinete, que monta a caballo | a’jsa | `LEXR-02293` |
| `diccionario_general/joven_adulto.jpg` | joven adulto | majcysa | `LEXR-02272` |
| `diccionario_general/juguetear_(repetidas_veces).jpg` | juguetear (repetidas veces) | visu’s- | `LEXR-00930` |
| `diccionario_general/juguetón.jpg` | juguetón | paypwesa | `LEXR-00437` |
| `diccionario_general/juntar,_unir.jpg` | juntar, unir | utya- | `LEXR-02866` |
| `diccionario_general/jáquima.jpg` | jáquima | cjaquima | `LEXR-00869` |
| `diccionario_general/la_abeja_(insecto).jpg` | la abeja (insecto) | chji’ndy | `LEXR-00588` |
| `diccionario_general/la_abuela.jpg` | la abuela | penzhi | `LEXR-00816` |
| `diccionario_general/la_abuela,_bisabuela.jpg` | la abuela, bisabuela | mama wala | `LEXR-01666` |
| `diccionario_general/la_acequia.jpg` | la acequia | yu’waca | `LEXR-01021` |
| `diccionario_general/la_aguja.jpg` | la aguja | ñunz (yujnz) | `LEXR-00852` |
| `diccionario_general/la_ahijada.jpg` | la ahijada | neeniisa | `LEXR-00897` |
| `diccionario_general/la_almohada.jpg` | la almohada | peecydyiqui (peendyiqui) | `LEXR-01747` |
| `diccionario_general/la_alpargata.jpg` | la alpargata | pelgatyi | `LEXR-01396` |
| `diccionario_general/la_altasara.jpg` | la altasara | anayún | `LEXR-01904` |
| `diccionario_general/la_araña_(arácnido).jpg` | la araña (arácnido) | tupa | `LEXR-00837` |
| `diccionario_general/la_ardilla_(mamífero_roedor).jpg` | la ardilla (mamífero roedor) | shuma | `LEXR-02178` |
| `diccionario_general/la_arena.jpg` | la arena | muse | `LEXR-00613` |
| `diccionario_general/la_arepa.jpg` | la arepa | wa’ts | `LEXR-03920` |
| `diccionario_general/la_arruga.jpg` | la arruga | cue’nz | `LEXR-03600` |
| `diccionario_general/la_avispa_(insecto).jpg` | la avispa (insecto) | menzucue | `LEXR-01995` |
| `diccionario_general/la_ayuda.jpg` | la ayuda | pu’chni | `LEXR-02389` |
| `diccionario_general/la_barbacoa_(cama_hecha_de_palos).jpg` | la barbacoa (cama hecha de palos) | atũ | `LEXR-00383` |
| `diccionario_general/la_basura.jpg` | la basura | cytã’ | `LEXR-01376` |
| `diccionario_general/la_batata_(planta,_de_tubérculos_comestibles).jpg` | la batata (planta, de tubérculos comestibles) | ũtj | `LEXR-02648` |
| `diccionario_general/la_bifurcacíon_(del_río).jpg` | la bifurcacíon (del río) | yu’shãpy | `LEXR-02735` |
| `diccionario_general/la_blusa_de_lana.jpg` | la blusa de lana | jyuuts atyj | `LEXR-03357` |
| `diccionario_general/la_boda,_día_del_casamiento.jpg` | la boda, día del casamiento | patmu en | `LEXR-03647` |
| `diccionario_general/la_boda,_el_casamiento_(díade_la_ceremonia).jpg` | la boda, el casamiento (díade la ceremonia) | camba en | `LEXR-01033` |
| `diccionario_general/la_borrachera.jpg` | la borrachera | tũu | `LEXR-01625` |
| `diccionario_general/la_broma,_el_chiste,_la_chanza.jpg` | la broma, el chiste, la chanza | shaacue | `LEXR-01083` |
| `diccionario_general/la_brujería_hechicería.jpg` | la brujería hechicería | dyijy yuuni | `LEXR-00965` |
| `diccionario_general/la_cabeza.jpg` | la cabeza | dyictjé | `LEXR-02307` |
| `diccionario_general/la_cabra,_el_chivo.jpg` | la cabra, el chivo | capla, caplcuẽ | `LEXR-01779` |
| `diccionario_general/la_cabuya,_el_fique.jpg` | la cabuya, el fique | bajts | `LEXR-03693` |
| `diccionario_general/la_cadera.jpg` | la cadera | jytund yaj | `LEXR-02111` |
| `diccionario_general/la_caldera.jpg` | la caldera | calderu | `LEXR-01441` |
| `diccionario_general/la_calle,_el_callejón.jpg` | la calle, el callejón | clliicjun | `LEXR-02782` |
| `diccionario_general/la_cama.jpg` | la cama | deeni, deeni atũ (deeñi, deeñi atũ) | `LEXR-02101` |
| `diccionario_general/la_camisa.jpg` | la camisa | cmiisa | `LEXR-01782` |
| `diccionario_general/la_campana.jpg` | la campana | cambana | `LEXR-02037` |
| `diccionario_general/la_cana.jpg` | la cana | fime | `LEXR-02479` |
| `diccionario_general/la_candela,_el_fuego.jpg` | la candela, el fuego | ipy | `LEXR-02847` |
| `diccionario_general/la_candelilla_(insecto).jpg` | la candelilla (insecto) | ech cupjy | `LEXR-00783` |
| `diccionario_general/la_candelilla,_luciérnaga.jpg` | la candelilla, luciérnaga | cupjy | `LEXR-02368` |
| `diccionario_general/la_canilla.jpg` | la canilla | chinda pil | `LEXR-01849` |
| `diccionario_general/la_canoa_(artesa_para_la_chicha).jpg` | la canoa (artesa para la chicha) | canuwé | `LEXR-00681` |
| `diccionario_general/la_cara,_el_rostro.jpg` | la cara, el rostro | dyi’p | `LEXR-03849` |
| `diccionario_general/la_carne.jpg` | la carne | chich | `LEXR-02468` |
| `diccionario_general/la_carne_espumosa.jpg` | la carne espumosa | shba’mb | `LEXR-02497` |
| `diccionario_general/la_casa.jpg` | la casa | yat | `LEXR-01103` |
| `diccionario_general/la_casa_de_la_minga.jpg` | la casa de la minga | pi’cy yat | `LEXR-01609` |
| `diccionario_general/la_casa_donde_se_celebra_la_fiesta.jpg` | la casa donde se celebra la fiesta | fiesta yat | `LEXR-02371` |
| `diccionario_general/la_caspa.jpg` | la caspa | dyicy | `LEXR-00964` |
| `diccionario_general/la_catarata.jpg` | la catarata | cjise | `LEXR-02983` |
| `diccionario_general/la_caña_brava_(planta).jpg` | la caña brava (planta) | cjĩj | `LEXR-01370` |
| `diccionario_general/la_caña_brava_del_páramo_(planta).jpg` | la caña brava del páramo (planta) | cjĩtsha | `LEXR-01978` |
| `diccionario_general/la_cebolla_(planta,_de_raíz_comestible).jpg` | la cebolla (planta, de raíz comestible) | spulla | `LEXR-01412` |
| `diccionario_general/la_cecina.jpg` | la cecina | chich ujndy | `LEXR-01780` |
| `diccionario_general/la_ceniza,_la_pólvora.jpg` | la ceniza, la pólvora | cjuuts | `LEXR-00956` |
| `diccionario_general/la_cera_(del_oído),_cerúmen.jpg` | la cera (del oído), cerúmen | tjũ’we chica | `LEXR-02861` |
| `diccionario_general/la_cerbatana,_bodoquera.jpg` | la cerbatana, bodoquera | fytũupatj | `LEXR-02661` |
| `diccionario_general/la_cerca,_el_cerco.jpg` | la cerca, el cerco | upj | `LEXR-01009` |
| `diccionario_general/la_chamiza.jpg` | la chamiza | tjuse | `LEXR-01090` |
| `diccionario_general/la_chinche_del_árbol.jpg` | la chinche del árbol | buu | `LEXR-02357` |
| `diccionario_general/la_chispa.jpg` | la chispa | ipy pchĩ’ | `LEXR-02044` |
| `diccionario_general/la_chonta_(especie_de_palmera),_la_vara_de_chonta.jpg` | la chonta (especie de palmera), la vara de chonta | chunda | `LEXR-01203` |
| `diccionario_general/la_chucha,_zarigüeya_(mamífero).jpg` | la chucha, zarigüeya (mamífero) | chucha | `LEXR-02914` |
| `diccionario_general/la_cicatriz,_marca.jpg` | la cicatriz, marca | sñal (syal) | `LEXR-03029` |
| `diccionario_general/la_cidrayota_(planta_comestible).jpg` | la cidrayota (planta comestible) | shwa’ | `LEXR-02824` |
| `diccionario_general/la_circuela_silvestre_(fruta).jpg` | la circuela silvestre (fruta) | tsunde | `LEXR-02998` |
| `diccionario_general/la_ciudad.jpg` | la ciudad | chjamb wala | `LEXR-03193` |
| `diccionario_general/la_clavija_(para_torcer_laso).jpg` | la clavija (para torcer laso) | claapjica | `LEXR-00690` |
| `diccionario_general/la_clueca.jpg` | la clueca | ã’pysa | `LEXR-02834` |
| `diccionario_general/la_cobija.jpg` | la cobija | deepa’chni | `LEXR-01138` |
| `diccionario_general/la_cobija_(tejido_en_telar).jpg` | la cobija (tejido en telar) | plliisatu (pllist T) | `LEXR-02931` |
| `diccionario_general/la_coca_(planta).jpg` | la coca (planta) | ẽsh | `LEXR-01965` |
| `diccionario_general/la_cocinera.jpg` | la cocinera | csinela | `LEXR-01520` |
| `diccionario_general/la_cola.jpg` | la cola | menz | `LEXR-01226` |
| `diccionario_general/la_compañera_(mujer_que_cohabita_con_un_hombre_sin_casarse).jpg` | la compañera (mujer que cohabita con un hombre sin casarse) | npi’qui | `LEXR-01465` |
| `diccionario_general/la_concuñada.jpg` | la concuñada | u’y pyacj | `LEXR-02343` |
| `diccionario_general/la_coral_(culebra).jpg` | la coral (culebra) | ñavytuć | `LEXR-02773` |
| `diccionario_general/la_coronilla_(de_la_cabeza).jpg` | la coronilla (de la cabeza) | tjã’mbush | `LEXR-02678` |
| `diccionario_general/la_corriente_del_rió.jpg` | la corriente del rió | ejme | `LEXR-03176` |
| `diccionario_general/la_corteza_de_árbol.jpg` | la corteza de árbol | fytũu cja’ty | `LEXR-03020` |
| `diccionario_general/la_costilla,_el_costado.jpg` | la costilla, el costado | tamby | `LEXR-02337` |
| `diccionario_general/la_coyuntura,_canuto_de_la_caña.jpg` | la coyuntura, canuto de la caña | findy | `LEXR-01989` |
| `diccionario_general/la_cresta_(de_gallo).jpg` | la cresta (de gallo) | yacue | `LEXR-00936` |
| `diccionario_general/la_cucaracha_(insecto).jpg` | la cucaracha (insecto) | sa’te | `LEXR-02393` |
| `diccionario_general/la_cuchara.jpg` | la cuchara | cha’cy | `LEXR-02095` |
| `diccionario_general/la_culebra.jpg` | la culebra | ul | `LEXR-01095` |
| `diccionario_general/la_culpa,_delito.jpg` | la culpa, delito | yuuwe | `LEXR-03444` |
| `diccionario_general/la_curuba_(fruta).jpg` | la curuba (fruta) | ñauñú | `LEXR-01704` |
| `diccionario_general/la_cuñada_(entre_mujeres).jpg` | la cuñada (entre mujeres) | ntyi’nsa (ntyi’nas J) | `LEXR-01068` |
| `diccionario_general/la_cárcel.jpg` | la cárcel | carcel | `LEXR-03130` |
| `diccionario_general/la_danta_(mamífero).jpg` | la danta (mamífero) | jimba cjũch | `LEXR-03502` |
| `diccionario_general/la_derecha.jpg` | la derecha | patsu | `LEXR-00723` |
| `diccionario_general/la_desgracia.jpg` | la desgracia | ñusu en | `LEXR-02460` |
| `diccionario_general/la_deuda.jpg` | la deuda | yul (yuul) | `LEXR-02409` |
| `diccionario_general/la_diarrea.jpg` | la diarrea | ũchi’ch wee | `LEXR-02147` |
| `diccionario_general/la_dolencia.jpg` | la dolencia | acasa | `LEXR-02689` |
| `diccionario_general/la_enfermedad,_peste,_epidemia.jpg` | la enfermedad, peste, epidemia | wee | `LEXR-03669` |
| `diccionario_general/la_enjalma.jpg` | la enjalma | cjalma | `LEXR-02780` |
| `diccionario_general/la_entrada.jpg` | la entrada | u’cani | `LEXR-00929` |
| `diccionario_general/la_era,_el_surco,_la_hilera.jpg` | la era, el surco, la hilera | amb | `LEXR-02033` |
| `diccionario_general/la_escalera.jpg` | la escalera | petyi’jni | `LEXR-03092` |
| `diccionario_general/la_escarcha.jpg` | la escarcha | ẽe cytã’ | `LEXR-01356` |
| `diccionario_general/la_escopeta.jpg` | la escopeta | ũpatel | `LEXR-03351` |
| `diccionario_general/la_espalda.jpg` | la espalda | tsinz | `LEXR-01255` |
| `diccionario_general/la_espiga.jpg` | la espiga | spiiga | `LEXR-03614` |
| `diccionario_general/la_espina,_zarza.jpg` | la espina, zarza | tsjũtsj | `LEXR-03125` |
| `diccionario_general/la_espuma.jpg` | la espuma | yu’bu’ch | `LEXR-02872` |
| `diccionario_general/la_espuma_del_jabón.jpg` | la espuma del jabón | cpun bu’ch | `LEXR-03775` |
| `diccionario_general/la_estera.jpg` | la estera | mastela (T) | `LEXR-02621` |
| `diccionario_general/la_estrella.jpg` | la estrella | ã’ | `LEXR-03004` |
| `diccionario_general/la_estrella_fugaz.jpg` | la estrella fugaz | ẽewee | `LEXR-01186` |
| `diccionario_general/la_faja,_el_chumbe.jpg` | la faja, el chumbe | taw | `LEXR-01556` |
| `diccionario_general/la_fiebre.jpg` | la fiebre | cacuesec | `LEXR-02256` |
| `diccionario_general/la_fiesta.jpg` | la fiesta | fiesta | `LEXR-00701` |
| `diccionario_general/la_flauta.jpg` | la flauta | cuvy | `LEXR-02157` |
| `diccionario_general/la_flauta_(de_carrizos_verticales).jpg` | la flauta (de carrizos verticales) | sende cuvy | `LEXR-00730` |
| `diccionario_general/la_flor.jpg` | la flor | quite | `LEXR-02226` |
| `diccionario_general/la_fontanela.jpg` | la fontanela | yutyi | `LEXR-01700` |
| `diccionario_general/la_fornicadora.jpg` | la fornicadora | pdeeu’y | `LEXR-00902` |
| `diccionario_general/la_frente.jpg` | la frente | cnene | `LEXR-01126` |
| `diccionario_general/la_fruta.jpg` | la fruta | ñun (yũn) | `LEXR-02644` |
| `diccionario_general/la_gallina.jpg` | la gallina | atall | `LEXR-01905` |
| `diccionario_general/la_garganta.jpg` | la garganta | pẽtyj | `LEXR-01404` |
| `diccionario_general/la_garganta,_cuello.jpg` | la garganta, cuello | tyjicj | `LEXR-01884` |
| `diccionario_general/la_gargantilla,_collar_de_cuentas.jpg` | la gargantilla, collar de cuentas | wã’chja | `LEXR-02141` |
| `diccionario_general/la_gente_de_la_minga_('invitados').jpg` | la gente de la minga (’invitados’) | pi’cy nasa | `LEXR-03856` |
| `diccionario_general/la_golondrina_(ave).jpg` | la golondrina (ave) | dyus vichacue | `LEXR-02572` |
| `diccionario_general/la_gotera.jpg` | la gotera | tsund | `LEXR-02280` |
| `diccionario_general/la_guacharaca_(ave).jpg` | la guacharaca (ave) | finzh | `LEXR-03355` |
| `diccionario_general/la_guadua_(especie_de_bambú).jpg` | la guadua (especie de bambú) | mujm | `LEXR-02923` |
| `diccionario_general/la_guala_(ave,_como_gallinazo).jpg` | la guala (ave, como gallinazo) | sapete | `LEXR-03388` |
| `diccionario_general/la_guaraca,_honda.jpg` | la guaraca, honda | i’sut | `LEXR-01217` |
| `diccionario_general/la_guasca,_cuerda,_soga,_piola.jpg` | la guasca, cuerda, soga, piola | wes | `LEXR-00661` |
| `diccionario_general/la_guayaba_(fruta).jpg` | la guayaba (fruta) | cpiinda | `LEXR-03311` |
| `diccionario_general/la_haba.jpg` | la haba | apas | `LEXR-02462` |
| `diccionario_general/la_hamaca.jpg` | la hamaca | wej | `LEXR-02899` |
| `diccionario_general/la_harina.jpg` | la harina | ũ’we | `LEXR-03636` |
| `diccionario_general/la_hebilla_(del_cinturón).jpg` | la hebilla (del cinturón) | villa | `LEXR-03443` |
| `diccionario_general/la_hemorragia.jpg` | la hemorragia | cacue yu’ | `LEXR-02152` |
| `diccionario_general/la_herida,_lastimadura.jpg` | la herida, lastimadura | cpã | `LEXR-01519` |
| `diccionario_general/la_hermana_(respecto_al_hombre).jpg` | la hermana (respecto al hombre) | npe’sh | `LEXR-01464` |
| `diccionario_general/la_hidropesía.jpg` | la hidropesía | tsu’vy wee | `LEXR-01169` |
| `diccionario_general/la_hierba,_maleza.jpg` | la hierba, maleza | jyutj (jyũtj) | `LEXR-00419` |
| `diccionario_general/la_hija.jpg` | la hija | niisa | `LEXR-02321` |
| `diccionario_general/la_hoja.jpg` | la hoja | fytũu ets | `LEXR-01528` |
| `diccionario_general/la_hoja_(de_árbol_o_planta),_el_papel.jpg` | la hoja (de árbol o planta), el papel | ets | `LEXR-03622` |
| `diccionario_general/la_hoja_de_maíz.jpg` | la hoja de maíz | shimb ets | `LEXR-01321` |
| `diccionario_general/la_hormiga_(insecto).jpg` | la hormiga (insecto) | cjã’cjã | `LEXR-01516` |
| `diccionario_general/la_horqueta.jpg` | la horqueta | chjã’py | `LEXR-00687` |
| `diccionario_general/la_horqueta_para_puerco.jpg` | la horqueta para puerco | cuchi tel | `LEXR-03170` |
| `diccionario_general/la_hoz_(herramienta).jpg` | la hoz (herramienta) | usa | `LEXR-02137` |
| `diccionario_general/la_huerta.jpg` | la huerta | walta | `LEXR-02800` |
| `diccionario_general/la_huerta,_hortaliza.jpg` | la huerta, hortaliza | tul | `LEXR-00737` |
| `diccionario_general/la_iglesia.jpg` | la iglesia | dyuus yat | `LEXR-03433` |
| `diccionario_general/la_jigra,_el_morral,_mochila.jpg` | la jigra, el morral, mochila | ya’ja | `LEXR-01017` |
| `diccionario_general/la_jovencita,_señorita.jpg` | la jovencita, señorita | cna’sa | `LEXR-00594` |
| `diccionario_general/la_lama,_el_musgo.jpg` | la lama, el musgo | sha’cy | `LEXR-02012` |
| `diccionario_general/la_lana.jpg` | la lana | cjas | `LEXR-02742` |
| `diccionario_general/la_langosta_(insecto).jpg` | la langosta (insecto) | cjã’sh wala | `LEXR-01042` |
| `diccionario_general/la_lanza.jpg` | la lanza | we’tj | `LEXR-00566` |
| `diccionario_general/la_larva.jpg` | la larva | buts | `LEXR-01644` |
| `diccionario_general/la_lechuza,_el_búho_(ave).jpg` | la lechuza, el búho (ave) | cupe | `LEXR-02473` |
| `diccionario_general/la_lejía.jpg` | la lejía | cjuuts yu’ | `LEXR-01912` |
| `diccionario_general/la_lengua.jpg` | la lengua | tjune | `LEXR-02071` |
| `diccionario_general/la_leña.jpg` | la leña | e’cy | `LEXR-02102` |
| `diccionario_general/la_limeta.jpg` | la limeta | limeeta | `LEXR-03677` |
| `diccionario_general/la_llaga,_úlcera,_'granos'.jpg` | la llaga, úlcera, ’granos’ | wã’jy | `LEXR-01268` |
| `diccionario_general/la_llama.jpg` | la llama | ipy cleechi | `LEXR-01531` |
| `diccionario_general/la_llama_(de_fuego).jpg` | la llama (de fuego) | cleech | `LEXR-00691` |
| `diccionario_general/la_llave.jpg` | la llave | yevi | `LEXR-02193` |
| `diccionario_general/la_llovizna.jpg` | la llovizna | nus chu’ch | `LEXR-01802` |
| `diccionario_general/la_lombricera,_el_vermífugo.jpg` | la lombricera, el vermífugo | shã’we yu’tse | `LEXR-00538` |
| `diccionario_general/la_lombriz_intestinal.jpg` | la lombriz intestinal | shã’we | `LEXR-00921` |
| `diccionario_general/la_luciérnaga_(insecto).jpg` | la luciérnaga (insecto) | echtsẽy | `LEXR-03696` |
| `diccionario_general/la_luz,_claridad.jpg` | la luz, claridad | een, eena’ | `LEXR-03403` |
| `diccionario_general/la_lámpara.jpg` | la lámpara | pqui’tanisa | `LEXR-01079` |
| `diccionario_general/la_madre.jpg` | la madre | njĩ’j | `LEXR-02705` |
| `diccionario_general/la_madrina.jpg` | la madrina | neenjĩ’j | `LEXR-00807` |
| `diccionario_general/la_mamá.jpg` | la mamá | mama | `LEXR-02922` |
| `diccionario_general/la_manga,_el_potrero.jpg` | la manga, el potrero | manga | `LEXR-02048` |
| `diccionario_general/la_mano.jpg` | la mano | cuse | `LEXR-03136` |
| `diccionario_general/la_mano_derecha.jpg` | la mano derecha | patsu cuse | `LEXR-01154` |
| `diccionario_general/la_maraca.jpg` | la maraca | snacja | `LEXR-01324` |
| `diccionario_general/la_maraca,_el_alfandoque.jpg` | la maraca, el alfandoque | sñuñu (syũyu) | `LEXR-02447` |
| `diccionario_general/la_mariposa_(insecto).jpg` | la mariposa (insecto) | smejme (tsmejme) | `LEXR-01253` |
| `diccionario_general/la_marteja,_mono_nocturno_(mamífero).jpg` | la marteja, mono nocturno (mamífero) | wenze | `LEXR-02728` |
| `diccionario_general/la_mata.jpg` | la mata | tash | `LEXR-02997` |
| `diccionario_general/la_mata,_el_árbol.jpg` | la mata, el árbol | fytũu tash | `LEXR-02374` |
| `diccionario_general/la_mazamorra.jpg` | la mazamorra | cjash | `LEXR-01911` |
| `diccionario_general/la_mecha,_pavesa.jpg` | la mecha, pavesa | pchĩ’ | `LEXR-02545` |
| `diccionario_general/la_medianoche.jpg` | la medianoche | cuspyãj | `LEXR-01522` |
| `diccionario_general/la_menstruación.jpg` | la menstruación | u’y wee | `LEXR-02344` |
| `diccionario_general/la_mentira.jpg` | la mentira | ĩshiini | `LEXR-02874` |
| `diccionario_general/la_miel_de_abeja.jpg` | la miel de abeja | shi’ndy mil | `LEXR-03096` |
| `diccionario_general/la_miel,_guerapo_de_caña_sin_fermentar.jpg` | la miel, guerapo de caña sin fermentar | mil | `LEXR-00427` |
| `diccionario_general/la_mitad.jpg` | la mitad | puuvyãjn | `LEXR-00913` |
| `diccionario_general/la_montura.jpg` | la montura | wa’ta | `LEXR-03575` |
| `diccionario_general/la_mosca_(insecto).jpg` | la mosca (insecto) | fynej | `LEXR-01141` |
| `diccionario_general/la_muchacha.jpg` | la muchacha | wasacuẽ (wesacuẽ) | `LEXR-00468` |
| `diccionario_general/la_muela.jpg` | la muela | tũtsa | `LEXR-00740` |
| `diccionario_general/la_muela_del_juicio.jpg` | la muela del juicio | tsute wala | `LEXR-02999` |
| `diccionario_general/la_muerte,_día_de_la_muerte.jpg` | la muerte, día de la muerte | uu en | `LEXR-01174` |
| `diccionario_general/la_mugre,_contaminación.jpg` | la mugre, contaminación | pta’nz | `LEXR-03611` |
| `diccionario_general/la_muñeca_(parte_del_brazo).jpg` | la muñeca (parte del brazo) | cuse pẽtyj | `LEXR-02475` |
| `diccionario_general/la_naranja_(fruta).jpg` | la naranja (fruta) | llima | `LEXR-02788` |
| `diccionario_general/la_nariz.jpg` | la nariz | ĩts | `LEXR-03859` |
| `diccionario_general/la_nigua_(insecto).jpg` | la nigua (insecto) | quima | `LEXR-02390` |
| `diccionario_general/la_noche.jpg` | la noche | cus | `LEXR-01286` |
| `diccionario_general/la_novia,_comprometida.jpg` | la novia, comprometida | nyu yuuwa’jsa | `LEXR-02383` |
| `diccionario_general/la_nube,_neblina.jpg` | la nube, neblina | tãapj | `LEXR-01094` |
| `diccionario_general/la_nuera.jpg` | la nuera | ncuẽmiyu | `LEXR-03116` |
| `diccionario_general/la_nuez_de_la_garganta.jpg` | la nuez de la garganta | pẽty luwa | `LEXR-01879` |
| `diccionario_general/la_olla.jpg` | la olla | mityj | `LEXR-00516` |
| `diccionario_general/la_orden,_el_mandato.jpg` | la orden, el mandato | jycaani | `LEXR-01384` |
| `diccionario_general/la_oreja.jpg` | la oreja | tjũwe (tjũwa T) | `LEXR-03700` |
| `diccionario_general/la_orina.jpg` | la orina | su’s | `LEXR-00543` |
| `diccionario_general/la_ortiga.jpg` | la ortiga | cjãas | `LEXR-03353` |
| `diccionario_general/la_oveja.jpg` | la oveja | piisháa | `LEXR-01474` |
| `diccionario_general/la_paja.jpg` | la paja | tsjĩtsj | `LEXR-03187` |
| `diccionario_general/la_paloma_(ave).jpg` | la paloma (ave) | tumb chujme | `LEXR-00554` |
| `diccionario_general/la_panela.jpg` | la panela | dulse | `LEXR-01725` |
| `diccionario_general/la_pantorrilla.jpg` | la pantorrilla | pil tuty | `LEXR-01242` |
| `diccionario_general/la_papa.jpg` | la papa | ca’ga | `LEXR-00388` |
| `diccionario_general/la_papaya_(fruta_del_papayo).jpg` | la papaya (fruta del papayo) | payaa | `LEXR-02169` |
| `diccionario_general/la_pareja_(de_personas).jpg` | la pareja (de personas) | ptam | `LEXR-02932` |
| `diccionario_general/la_partera.jpg` | la partera | spaacysa | `LEXR-00831` |
| `diccionario_general/la_parálisis.jpg` | la parálisis | jyanduwee | `LEXR-02428` |
| `diccionario_general/la_perdiz_(ave).jpg` | la perdiz (ave) | fi’l | `LEXR-00786` |
| `diccionario_general/la_pezuña_del_puerco.jpg` | la pezuña del puerco | cuchi vyllill | `LEXR-01982` |
| `diccionario_general/la_peña.jpg` | la peña | ejy | `LEXR-03259` |
| `diccionario_general/la_piedra.jpg` | la piedra | cuet | `LEXR-01132` |
| `diccionario_general/la_piedra_de_afilar.jpg` | la piedra de afilar | shũucuet | `LEXR-01085` |
| `diccionario_general/la_piedra_de_moler.jpg` | la piedra de moler | ũ’cj cuet | `LEXR-02031` |
| `diccionario_general/la_piel.jpg` | la piel | nish cja’ty (T) | `LEXR-02963` |
| `diccionario_general/la_pierna,_la_canilla.jpg` | la pierna, la canilla | pil | `LEXR-02055` |
| `diccionario_general/la_piña_(planta).jpg` | la piña (planta) | chajú | `LEXR-02298` |
| `diccionario_general/la_planta_del_pie.jpg` | la planta del pie | chind pjapj | `LEXR-03166` |
| `diccionario_general/la_pluma_(de_gallina).jpg` | la pluma (de gallina) | atall cjas | `LEXR-01642` |
| `diccionario_general/la_posada.jpg` | la posada | pa’j yat | `LEXR-02433` |
| `diccionario_general/la_puerta.jpg` | la puerta | vity | `LEXR-00747` |
| `diccionario_general/la_pulga_(insecto).jpg` | la pulga (insecto) | pã’pã | `LEXR-00533` |
| `diccionario_general/la_pulpa,_la_carne.jpg` | la pulpa, la carne | nish | `LEXR-03607` |
| `diccionario_general/la_punta_de_la_aguja.jpg` | la punta de la aguja | ñunz vits | `LEXR-01431` |
| `diccionario_general/la_punta,_cumbre.jpg` | la punta, cumbre | vits | `LEXR-00931` |
| `diccionario_general/la_pólvora.jpg` | la pólvora | ũpacjuuts | `LEXR-02688` |
| `diccionario_general/la_quijada.jpg` | la quijada | cmbamba dyi’tj | `LEXR-03430` |
| `diccionario_general/la_rana_(batracio).jpg` | la rana (batracio) | sap le’chue | `LEXR-02631` |
| `diccionario_general/la_rascadera,_mafafa_(planta).jpg` | la rascadera, mafafa (planta) | ã’sh | `LEXR-02835` |
| `diccionario_general/la_rata_(mamífero_roedor).jpg` | la rata (mamífero roedor) | unza wala | `LEXR-01173` |
| `diccionario_general/la_raíz.jpg` | la raíz | watse (wetse) | `LEXR-00842` |
| `diccionario_general/la_raíz_(de_árbol).jpg` | la raíz (de árbol) | fytũu watse | `LEXR-03338` |
| `diccionario_general/la_red,_malla.jpg` | la red, malla | ucje | `LEXR-02829` |
| `diccionario_general/la_risa.jpg` | la risa | shicani | `LEXR-03485` |
| `diccionario_general/la_roca.jpg` | la roca | cuet wala | `LEXR-03816` |
| `diccionario_general/la_rodilla.jpg` | la rodilla | jyũcuet | `LEXR-00976` |
| `diccionario_general/la_roncha.jpg` | la roncha | buta | `LEXR-03011` |
| `diccionario_general/la_ropa_de_boda_(de_la_novia).jpg` | la ropa de boda (de la novia) | iimi’wa’j atyj | `LEXR-02482` |
| `diccionario_general/la_roza.jpg` | la roza | wats | `LEXR-01337` |
| `diccionario_general/la_roza_(de_selva_virgen).jpg` | la roza (de selva virgen) | chimby ej | `LEXR-02521` |
| `diccionario_general/la_roza,_el_maizal.jpg` | la roza, el maizal | cutyj ej | `LEXR-03537` |
| `diccionario_general/la_roza,_el_sembrado.jpg` | la roza, el sembrado | ej | `LEXR-03228` |
| `diccionario_general/la_ruana,_el_anaco.jpg` | la ruana, el anaco | atyj | `LEXR-01583` |
| `diccionario_general/la_rueca,_puchicanga.jpg` | la rueca, puchicanga | cjaswat | `LEXR-03743` |
| `diccionario_general/la_sabana.jpg` | la sabana | yunda ucue | `LEXR-01960` |
| `diccionario_general/la_sal.jpg` | la sal | nenga | `LEXR-02539` |
| `diccionario_general/la_sala.jpg` | la sala | ñujne | `LEXR-00851` |
| `diccionario_general/la_salida,_en_la_salida.jpg` | la salida, en la salida | case´jete | `LEXR-02568` |
| `diccionario_general/la_saliva,_baba.jpg` | la saliva, baba | fyne’sh | `LEXR-00788` |
| `diccionario_general/la_sarna.jpg` | la sarna | chandy, chandy wee | `LEXR-02421` |
| `diccionario_general/la_sed.jpg` | la sed | yũ’wẽeni | `LEXR-00938` |
| `diccionario_general/la_selva.jpg` | la selva | yu’cj wala | `LEXR-02029` |
| `diccionario_general/la_semana.jpg` | la semana | qui’su | `LEXR-01551` |
| `diccionario_general/la_semana_pasada.jpg` | la semana pasada | jũ’na qui’su | `LEXR-00800` |
| `diccionario_general/la_semano_pasada.jpg` | la semano pasada | ũ’na qui’su | `LEXR-01898` |
| `diccionario_general/la_semilla_(de_plantas),_la_semilla_(raza_de_animales).jpg` | la semilla (de plantas), la semilla (raza de animales) | fiw | `LEXR-02311` |
| `diccionario_general/la_semilla_que_vuelve_a_dar_después_de_acosechado,_sarapanga.jpg` | la semilla que vuelve a dar después de acosechado, sarapanga | pã’cj | `LEXR-00532` |
| `diccionario_general/la_señora_(de_raza_blanca).jpg` | la señora (de raza blanca) | siyula | `LEXR-01322` |
| `diccionario_general/la_señorita_(de_raza_blanca).jpg` | la señorita (de raza blanca) | siyula cna’sa | `LEXR-01086` |
| `diccionario_general/la_soga,_el_lazo.jpg` | la soga, el lazo | cũ’p cja’tya | `LEXR-02477` |
| `diccionario_general/la_sombra.jpg` | la sombra | pshũu | `LEXR-00528` |
| `diccionario_general/la_sombra_(de_una_persona).jpg` | la sombra (de una persona) | pnaasa | `LEXR-00820` |
| `diccionario_general/la_suegra.jpg` | la suegra | u’ytjẽ’j | `LEXR-02285` |
| `diccionario_general/la_tapa.jpg` | la tapa | apjáa | `LEXR-01968` |
| `diccionario_general/la_tarabita_(cuerda_pa_cruzar_el_río).jpg` | la tarabita (cuerda pa cruzar el río) | tund yaj | `LEXR-01172` |
| `diccionario_general/la_tarabita_(para_cruzar_río).jpg` | la tarabita (para cruzar río) | dund yaj | `LEXR-00697` |
| `diccionario_general/la_taza.jpg` | la taza | tasa | `LEXR-02971` |
| `diccionario_general/la_teja.jpg` | la teja | tecja | `LEXR-01326` |
| `diccionario_general/la_telaraña.jpg` | la telaraña | tupa pwejy | `LEXR-01256` |
| `diccionario_general/la_tierra,_el_terreno,_suelo.jpg` | la tierra, el terreno, suelo | quiwe | `LEXR-02333` |
| `diccionario_general/la_tijereta_(ave).jpg` | la tijereta (ave) | uschi’ | `LEXR-01689` |
| `diccionario_general/la_tinta_morada_(planta).jpg` | la tinta morada (planta) | cndu | `LEXR-02950` |
| `diccionario_general/la_tosferina_(la_tos_ferina).jpg` | la tosferina (la tos ferina) | e’shwee | `LEXR-00699` |
| `diccionario_general/la_trampa.jpg` | la trampa | acj | `LEXR-03637` |
| `diccionario_general/la_trampa_(con_soga).jpg` | la trampa (con soga) | yajcy | `LEXR-01631` |
| `diccionario_general/la_trenza_de_cabello_o_de_cabuya.jpg` | la trenza de cabello o de cabuya | tsũ’ta | `LEXR-00836` |
| `diccionario_general/la_tripa,_el_intestino.jpg` | la tripa, el intestino | meetu’j | `LEXR-03359` |
| `diccionario_general/la_tristeza,_angustia.jpg` | la tristeza, angustia | ñussa | `LEXR-01504` |
| `diccionario_general/la_tulpa.jpg` | la tulpa | ipy cuet | `LEXR-03380` |
| `diccionario_general/la_tusa_de_maíz.jpg` | la tusa de maíz | tymi | `LEXR-01685` |
| `diccionario_general/la_tía_(hermana_de_la_mamá).jpg` | la tía (hermana de la mamá) | njĩ’yacue, njĩ’yũcue | `LEXR-02624` |
| `diccionario_general/la_uva_silvestre.jpg` | la uva silvestre | camañún | `LEXR-02201` |
| `diccionario_general/la_vaca.jpg` | la vaca | claa u’y | `LEXR-03774` |
| `diccionario_general/la_vara_(medida).jpg` | la vara (medida) | bara | `LEXR-00857` |
| `diccionario_general/la_vasija,_calabacita_(partida_en_mitad).jpg` | la vasija, calabacita (partida en mitad) | tjee | `LEXR-02500` |
| `diccionario_general/la_vejez_(refiriendo_a_un_hombre).jpg` | la vejez (refiriendo a un hombre) | ĩishweete | `LEXR-01772` |
| `diccionario_general/la_vejez_(refiriendo_a_una_mujer).jpg` | la vejez (refiriendo a una mujer) | penzhweete | `LEXR-02930` |
| `diccionario_general/la_vejiga.jpg` | la vejiga | suucal | `LEXR-02446` |
| `diccionario_general/la_vena.jpg` | la vena | ee watse | `LEXR-03081` |
| `diccionario_general/la_vena_yugular.jpg` | la vena yugular | pẽty watse | `LEXR-02795` |
| `diccionario_general/la_verruga.jpg` | la verruga | wenze | `LEXR-02686` |
| `diccionario_general/la_vez,_vuelta.jpg` | la vez, vuelta | jwend | `LEXR-00706` |
| `diccionario_general/la_vida.jpg` | la vida | fi’nzeni | `LEXR-03658` |
| `diccionario_general/la_vida_(futura).jpg` | la vida (futura) | ĩtyĩ fi’nzewa’j | `LEXR-00478` |
| `diccionario_general/la_vida_(pasada).jpg` | la vida (pasada) | ĩtyĩ fi’nzeni | `LEXR-02909` |
| `diccionario_general/la_viga.jpg` | la viga | picas | `LEXR-02122` |
| `diccionario_general/la_viga_transversal.jpg` | la viga transversal | pand | `LEXR-03915` |
| `diccionario_general/la_visiones.jpg` | la visiones | ĩcjwe’sh | `LEXR-00761` |
| `diccionario_general/la_viuda.jpg` | la viuda | ech u’y | `LEXR-02814` |
| `diccionario_general/la_vulva.jpg` | la vulva | cush | `LEXR-01786` |
| `diccionario_general/la_yuca_(planta,_de_raíz_comestible).jpg` | la yuca (planta, de raíz comestible) | ña (yã) | `LEXR-03127` |
| `diccionario_general/la_zanja.jpg` | la zanja | chamba | `LEXR-01652` |
| `diccionario_general/la_zarza_(planta).jpg` | la zarza (planta) | cwẽndyimbu | `LEXR-01724` |
| `diccionario_general/la_ánima,_la_alma_del_difunto.jpg` | la ánima, la alma del difunto | animus | `LEXR-01359` |
| `diccionario_general/labio.jpg` | labio | yuwe cja’ty | `LEXR-03306` |
| `diccionario_general/ladrar_(repetidas_veces).jpg` | ladrar (repetidas veces) | viquiiqui- | `LEXR-02023` |
| `diccionario_general/lama_(planta_parasítica).jpg` | lama (planta parasítica) | cha’cy | `LEXR-03399` |
| `diccionario_general/lamer.jpg` | lamer | tech-, techíi- | `LEXR-03030` |
| `diccionario_general/lana_de_oveja.jpg` | lana de oveja | piishá cjas | `LEXR-01680` |
| `diccionario_general/lana_teñida.jpg` | lana teñida | cjas bite | `LEXR-02781` |
| `diccionario_general/lanudo.jpg` | lanudo | cjastjẽ’j | `LEXR-00590` |
| `diccionario_general/largo.jpg` | largo | jyu’jyu’j | `LEXR-01917` |
| `diccionario_general/las_tijeras.jpg` | las tijeras | pteenzú | `LEXR-01751` |
| `diccionario_general/laurel_de_cera_(árbol).jpg` | laurel de cera (árbol) | sela | `LEXR-03240` |
| `diccionario_general/lavar_(loza).jpg` | lavar (loza) | pcji’cj-, pcji’cji- | `LEXR-03341` |
| `diccionario_general/lavar_la_cara.jpg` | lavar la cara | pchjĩ’ch-, pchjĩ’chi | `LEXR-00901` |
| `diccionario_general/lavar_las_manos.jpg` | lavar las manos | cwẽechja-, cwẽechjáa- | `LEXR-01136` |
| `diccionario_general/leche.jpg` | leche | lechi | `LEXR-02319` |
| `diccionario_general/legaña.jpg` | legaña | yafy chic | `LEXR-02346` |
| `diccionario_general/lejos.jpg` | lejos | jyu’j dyi’j | `LEXR-02576` |
| `diccionario_general/lejos,_largo,_alto.jpg` | lejos, largo, alto | jyu’j | `LEXR-00418` |
| `diccionario_general/lenguaje,_habla,_voz.jpg` | lenguaje, habla, voz | we’weni | `LEXR-01013` |
| `diccionario_general/levantar_chismes.jpg` | levantar chismes | yuwe quiis- | `LEXR-00668` |
| `diccionario_general/levantarse,_madrguar.jpg` | levantarse, madrguar | quiite-, quiitée- | `LEXR-02583` |
| `diccionario_general/lezna_(herramienta).jpg` | lezna (herramienta) | pundúu | `LEXR-03119` |
| `diccionario_general/librarse.jpg` | librarse | ya’nwe’we- | `LEXR-00935` |
| `diccionario_general/liendre.jpg` | liendre | ẽs zits | `LEXR-02511` |
| `diccionario_general/ligero.jpg` | ligero | acha acha | `LEXR-00765` |
| `diccionario_general/ligero,_aprisa.jpg` | ligero, aprisa | tund | `LEXR-00555` |
| `diccionario_general/limosna.jpg` | limosna | lmushnu | `LEXR-01918` |
| `diccionario_general/limpiar.jpg` | limpiar | nuyaatée- | `LEXR-02214` |
| `diccionario_general/limpiar,_mugre,_quitar_contaminación.jpg` | limpiar, mugre, quitar contaminación | jychanzha-, jychanzháa- | `LEXR-03437` |
| `diccionario_general/limpiarse_(a_uno_mismo).jpg` | limpiarse (a uno mismo) | jycjũucj-, jycjũucju- | `LEXR-01733` |
| `diccionario_general/limpio.jpg` | limpio | ate | `LEXR-02564` |
| `diccionario_general/lindero.jpg` | lindero | llinderu | `LEXR-02270` |
| `diccionario_general/liso.jpg` | liso | jyu’nde (jyũ’nda) | `LEXR-00712` |
| `diccionario_general/liviano.jpg` | liviano | ẽsẽ’ | `LEXR-01966` |
| `diccionario_general/liviano,_no_pesado.jpg` | liviano, no pesado | deujmée | `LEXR-02658` |
| `diccionario_general/llamado.jpg` | llamado | jĩnisa | `LEXR-02787` |
| `diccionario_general/llamar.jpg` | llamar | pa’ya- | `LEXR-03777` |
| `diccionario_general/llamarse.jpg` | llamarse | ya’wecha- | `LEXR-01572` |
| `diccionario_general/llanto.jpg` | llanto | ũ’ne pety cjacj | `LEXR-01352` |
| `diccionario_general/llegada_(futura).jpg` | llegada (futura) | pa’jwa’j | `LEXR-03713` |
| `diccionario_general/llegada_(pasada).jpg` | llegada (pasada) | pa’jni | `LEXR-02050` |
| `diccionario_general/llegar.jpg` | llegar | pa’j-, pa’ja- | `LEXR-01237` |
| `diccionario_general/llegar_(visitar_dos_lugares_en_el_mismo_viaje).jpg` | llegar (visitar dos lugares en el mismo viaje) | iipa’j- | `LEXR-00604` |
| `diccionario_general/llegar_a_ser.jpg` | llegar a ser | pa’j-, pa’ja- | `LEXR-02543` |
| `diccionario_general/llegar_de_un_viaje.jpg` | llegar de un viaje | ĩcj-ĩcje- | `LEXR-02561` |
| `diccionario_general/llenar.jpg` | llenar | yuuta, yuutáa- | `LEXR-03071` |
| `diccionario_general/llenar,_rellenar.jpg` | llenar, rellenar | yuta-, yutáa- | `LEXR-02248` |
| `diccionario_general/llenarse.jpg` | llenarse | uta-, utáa- | `LEXR-02683` |
| `diccionario_general/lleno.jpg` | lleno | uta | `LEXR-02724` |
| `diccionario_general/llevar_(varias_personas_o_varias_coas).jpg` | llevar (varias personas o varias coas) | atu’t- | `LEXR-03073` |
| `diccionario_general/llevar_alrededor_de_(ej._en_procesión).jpg` | llevar alrededor de (ej. en procesión) | nuytandyi- | `LEXR-03410` |
| `diccionario_general/llevar_consigo_(a_otra_persona).jpg` | llevar consigo (a otra persona) | pe’j-, pe’je- | `LEXR-03821` |
| `diccionario_general/llevar_debajo_del_brazo,_apretar.jpg` | llevar debajo del brazo, apretar | paatenz-, paatenzúu (ptenz-) | `LEXR-00898` |
| `diccionario_general/llevar_en_la_mano.jpg` | llevar en la mano | yaat- | `LEXR-01496` |
| `diccionario_general/llevar,_guiar,_encaminar.jpg` | llevar, guiar, encaminar | nuyi’j- | `LEXR-00430` |
| `diccionario_general/llorar_(al_mismo_tiempo_que_hace_otra_cosa).jpg` | llorar (al mismo tiempo que hace otra cosa) | iiũ’ne- | `LEXR-00884` |
| `diccionario_general/llorar_(por_ir_con_la_mamá).jpg` | llorar (por ir con la mamá) | pshindy-, pshindyíi- | `LEXR-02057` |
| `diccionario_general/llorón.jpg` | llorón | shindy | `LEXR-02397` |
| `diccionario_general/llover.jpg` | llover | nus pa’j- | `LEXR-03409` |
| `diccionario_general/llovizna.jpg` | llovizna | nus muse | `LEXR-01392` |
| `diccionario_general/lloviznar.jpg` | lloviznar | umbu’mbu- | `LEXR-00742` |
| `diccionario_general/lo_mismo_como,_igual_que.jpg` | lo mismo como, igual que | npaa | `LEXR-01801` |
| `diccionario_general/lo_que_da_sabor,_condimento.jpg` | lo que da sabor, condimento | peetjenisa | `LEXR-02671` |
| `diccionario_general/loco.jpg` | loco | luucu | `LEXR-02848` |
| `diccionario_general/lograr.jpg` | lograr | jyã’j-, jyãja- | `LEXR-02534` |
| `diccionario_general/lograr_avisar.jpg` | lograr avisar | cpaapta’sh-, cpaapta’shi- | `LEXR-01851` |
| `diccionario_general/lograr_detener.jpg` | lograr detener | cpaanewe- | `LEXR-01128` |
| `diccionario_general/lograr_empujar.jpg` | lograr empujar | cpaachãtyj-, cpaachãtyji- | `LEXR-00778` |
| `diccionario_general/lograr_entender.jpg` | lograr entender | cpaacyjiyu- | `LEXR-01127` |
| `diccionario_general/lograr_escuchar.jpg` | lograr escuchar | cpaawẽsẽ’j-, cpaawẽsẽ’je | `LEXR-03224` |
| `diccionario_general/lograr_hacer_entender.jpg` | lograr hacer entender | cpaacycjiyu’j-, cpaacycjiyu’ju- | `LEXR-03335` |
| `diccionario_general/lograr_halar.jpg` | lograr halar | cpaawenzh-, cpaawenzhi- | `LEXR-03135` |
| `diccionario_general/lograr_intervenir.jpg` | lograr intervenir | cpaanwe’we- | `LEXR-01444` |
| `diccionario_general/lograr_llevar.jpg` | lograr llevar | cpaanicy-, cpaaniqui- | `LEXR-03832` |
| `diccionario_general/lograr_mirar.jpg` | lograr mirar | cpaatjeng-, cpaatjengu- | `LEXR-02808` |
| `diccionario_general/los_antepasados.jpg` | los antepasados | cyãaniwe’sh, cyãaniteywe’sh | `LEXR-02426` |
| `diccionario_general/los_calzones.jpg` | los calzones | calsun | `LEXR-03815` |
| `diccionario_general/los_de_enfrente.jpg` | los de enfrente | dyi’ puwe’sh | `LEXR-00879` |
| `diccionario_general/los_padres_(padre_y_madre).jpg` | los padres (padre y madre) | tatawe’sh | `LEXR-03322` |
| `diccionario_general/los_pantalones_(de_liencillo).jpg` | los pantalones (de liencillo) | much | `LEXR-01061` |
| `diccionario_general/los_ramos.jpg` | los ramos | lamus | `LEXR-02430` |
| `diccionario_general/lucero.jpg` | lucero | ã’ wala | `LEXR-03531` |
| `diccionario_general/luciérnaga.jpg` | luciérnaga | cupjy | `LEXR-01720` |
| `diccionario_general/lugar_habitual,_morada.jpg` | lugar habitual, morada | ũsni, ũswa’j | `LEXR-00577` |
| `diccionario_general/lulo.jpg` | lulo | mutcue | `LEXR-03086` |
| `diccionario_general/luna_nueva.jpg` | luna nueva | a’te tjẽj | `LEXR-02512` |
| `diccionario_general/luna,_mes.jpg` | luna, mes | a’te | `LEXR-03873` |
| `diccionario_general/lágrima.jpg` | lágrima | yafy yu’ | `LEXR-00937` |
| `diccionario_general/macana.jpg` | macana | acy | `LEXR-01641` |
| `diccionario_general/macana,_arma_del_telar.jpg` | macana, arma del telar | quita | `LEXR-03612` |
| `diccionario_general/madre.jpg` | madre | mama | `LEXR-01665` |
| `diccionario_general/madre_con_hijo_u_hija.jpg` | madre con hijo u hija | pnjĩ’j | `LEXR-00986` |
| `diccionario_general/madrina_con_ahijado_o_ahijada.jpg` | madrina con ahijado o ahijada | pneejĩ’j | `LEXR-01811` |
| `diccionario_general/madrino.jpg` | madrino | dyus mama | `LEXR-02813` |
| `diccionario_general/madurarse.jpg` | madurarse | ĩits-, ĩitsúu- | `LEXR-01897` |
| `diccionario_general/maestro,_que_enseña.jpg` | maestro, que enseña | caapiya’jsa | `LEXR-02518` |
| `diccionario_general/mafafa.jpg` | mafafa | pwel, ã’sh | `LEXR-01753` |
| `diccionario_general/mafafa_(planta_comestible).jpg` | mafafa (planta comestible) | pwel | `LEXR-01615` |
| `diccionario_general/maldecir_(deseando_mal_a_otro),_ultrajar.jpg` | maldecir (deseando mal a otro), ultrajar | cysew-, cyseúu | `LEXR-02984` |
| `diccionario_general/malgastar.jpg` | malgastar | psuw-, psuwúu- | `LEXR-02388` |
| `diccionario_general/malla_de_alambre.jpg` | malla de alambre | tsam ucje | `LEXR-02017` |
| `diccionario_general/malo.jpg` | malo | ewmée | `LEXR-03476` |
| `diccionario_general/maltratar.jpg` | maltratar | pcyuu- | `LEXR-03457` |
| `diccionario_general/maltratar,_atacar_a_un_indefenso,_agredir.jpg` | maltratar, atacar a un indefenso, agredir | nui- | `LEXR-03854` |
| `diccionario_general/maltrato.jpg` | maltrato | pcyuuni | `LEXR-02003` |
| `diccionario_general/mamar.jpg` | mamar | chu’ch-, chu’chu | `LEXR-03132` |
| `diccionario_general/manco,_manimocho.jpg` | manco, manimocho | cuse much | `LEXR-03848` |
| `diccionario_general/mandadero.jpg` | mandadero | jycaanisa | `LEXR-01054` |
| `diccionario_general/mandar_alimentar.jpg` | mandar alimentar | caapuutsu’j-, caapuutsu’ju- | `LEXR-00390` |
| `diccionario_general/mandar_avisar.jpg` | mandar avisar | caapta’shi’j-, cappta’shi’ji- | `LEXR-03192` |
| `diccionario_general/mandar_comprar.jpg` | mandar comprar | cweeyu’j-, cweeyu’ju- | `LEXR-02696` |
| `diccionario_general/mandar_cortar_(pelo,_tabla).jpg` | mandar cortar (pelo, tabla) | caaspẽtje’j’, caaspẽtje’je- | `LEXR-03583` |
| `diccionario_general/mandar_dar_látigo.jpg` | mandar dar látigo | caapechucue’j-, caapechucue’ju- | `LEXR-03013` |
| `diccionario_general/mandar_encender.jpg` | mandar encender | caaqui’ta’j-, caaqui’ta’ja- | `LEXR-02652` |
| `diccionario_general/mandar_guardar_dieta.jpg` | mandar guardar dieta | caaqui’su’j-, caaqui’su’ju- | `LEXR-03796` |
| `diccionario_general/mandar_hervir.jpg` | mandar hervir | caambi’j-, caambi’ji- | `LEXR-03772` |
| `diccionario_general/mandar_lavar.jpg` | mandar lavar | ctjeetje’j-, ctjeetje’je- | `LEXR-00874` |
| `diccionario_general/mandar_peinar.jpg` | mandar peinar | caaquindu’j-, caaquindu’ju- | `LEXR-01114` |
| `diccionario_general/mandar_poner.jpg` | mandar poner | caaqui’pu’j-, caaqui’pu’ju- | `LEXR-03860` |
| `diccionario_general/mandar_razón.jpg` | mandar razón | yuwe caaj- | `LEXR-02084` |
| `diccionario_general/mandar_saludos.jpg` | mandar saludos | wecha caaj- | `LEXR-01568` |
| `diccionario_general/mandar_soltar,_hacer_suspender_(un_trabajo).jpg` | mandar soltar, hacer suspender (un trabajo) | caatywete’j-, caatywete’je- | `LEXR-00486` |
| `diccionario_general/mandar,_enviar.jpg` | mandar, enviar | caaj-, caja- | `LEXR-03426` |
| `diccionario_general/mandar,_matar.jpg` | mandar, matar | quiicje’j-, quiicje’je- | `LEXR-01813` |
| `diccionario_general/mandato,_orden.jpg` | mandato, orden | caajni | `LEXR-01972` |
| `diccionario_general/manojo_de_trigo.jpg` | manojo de trigo | scuutyj tund | `LEXR-02176` |
| `diccionario_general/manso.jpg` | manso | styãa | `LEXR-01413` |
| `diccionario_general/mantener,_criar.jpg` | mantener, criar | nuype’j-, nuype’je- | `LEXR-03180` |
| `diccionario_general/maní.jpg` | maní | quĩtj | `LEXR-02934` |
| `diccionario_general/maní_(planta).jpg` | maní (planta) | quitj | `LEXR-01814` |
| `diccionario_general/marco_del_telar_(palos_verticales).jpg` | marco del telar (palos verticales) | catjwe´sh | `LEXR-02949` |
| `diccionario_general/mascar_coca.jpg` | mascar coca | ẽsh pe’tse- | `LEXR-01841` |
| `diccionario_general/mascar,_masticar.jpg` | mascar, masticar | pe’tse- | `LEXR-02385` |
| `diccionario_general/mata_de_aguacate.jpg` | mata de aguacate | utse tash | `LEXR-03327` |
| `diccionario_general/mata_de_cabuya.jpg` | mata de cabuya | bats tash | `LEXR-02415` |
| `diccionario_general/mata_de_caña_brava.jpg` | mata de caña brava | cjĩij tash | `LEXR-03757` |
| `diccionario_general/mata_de_durazno_(árbol).jpg` | mata de durazno (árbol) | lashnu tash | `LEXR-00801` |
| `diccionario_general/mata_de_hongo.jpg` | mata de hongo | une tash | `LEXR-03718` |
| `diccionario_general/mataganado_(culebra).jpg` | mataganado (culebra) | ul ñavytuć | `LEXR-01335` |
| `diccionario_general/matar.jpg` | matar | icj-, icje- | `LEXR-00790` |
| `diccionario_general/mayor_(de_edad).jpg` | mayor (de edad) | ntjẽj, ntẽ’jsa | `LEXR-01067` |
| `diccionario_general/mayor,_el_que_manda.jpg` | mayor, el que manda | neej | `LEXR-02790` |
| `diccionario_general/mayordomo.jpg` | mayordomo | yultumu | `LEXR-03514` |
| `diccionario_general/mayores.jpg` | mayores | tjẽ’jwe’sh | `LEXR-03908` |
| `diccionario_general/mazamorra_con_sal,_sanco.jpg` | mazamorra con sal, sanco | nenga cjash | `LEXR-00520` |
| `diccionario_general/mazamorra_sin_sal.jpg` | mazamorra sin sal | shũucjash | `LEXR-00540` |
| `diccionario_general/maíz.jpg` | maíz | kutxh | `LEXR-03645` |
| `diccionario_general/maíz_amarillo.jpg` | maíz amarillo | cutyj bej | `LEXR-01985` |
| `diccionario_general/maíz_en_grano.jpg` | maíz en grano | cutyj cjavy | `LEXR-00875` |
| `diccionario_general/maíz_negro.jpg` | maíz negro | cutyj cjũch | `LEXR-01134` |
| `diccionario_general/maíz_pintado.jpg` | maíz pintado | cutyj bite | `LEXR-01372` |
| `diccionario_general/maíz_pirá.jpg` | maíz pirá | cutyj mush | `LEXR-02809` |
| `diccionario_general/maíz_sarazo.jpg` | maíz sarazo | cutyj tupj | `LEXR-02263` |
| `diccionario_general/maíz_tierno.jpg` | maíz tierno | shimb | `LEXR-00829` |
| `diccionario_general/mañana.jpg` | mañana | cuscay (cuscus) | `LEXR-02744` |
| `diccionario_general/mecer.jpg` | mecer | ũuw-, ũuwu- | `LEXR-00854` |
| `diccionario_general/medio,_a_medias,_no_enteramente.jpg` | medio, a medias, no enteramente | dyi’- | `LEXR-03501` |
| `diccionario_general/mejilla,_cachete.jpg` | mejilla, cachete | pucacuet | `LEXR-02060` |
| `diccionario_general/mejor,_antes_bien.jpg` | mejor, antes bien | wejyva | `LEXR-02556` |
| `diccionario_general/mejorarse_(de_una_enfermedad).jpg` | mejorarse (de una enfermedad) | catyji- | `LEXR-01589` |
| `diccionario_general/mejorarse,_componerse_(el_tiempo).jpg` | mejorarse, componerse (el tiempo) | ewuu- | `LEXR-01726` |
| `diccionario_general/mejorarse,_recuperarse,_fortalecerse,_arreciar_(lluvia).jpg` | mejorarse, recuperarse, fortalecerse, arreciar (lluvia) | chjãchja- | `LEXR-00491` |
| `diccionario_general/menear_(repetidas_veces).jpg` | menear (repetidas veces) | shwendu’ndu- | `LEXR-02126` |
| `diccionario_general/menear,_mover,_agitar.jpg` | menear, mover, agitar | quẽese’j-, quẽese’je- | `LEXR-03150` |
| `diccionario_general/menear,_revolver.jpg` | menear, revolver | shwende-, shwendúu- | `LEXR-00640` |
| `diccionario_general/menitr.jpg` | menitr | ĩshíi-ĩshiija- | `LEXR-03005` |
| `diccionario_general/menitroso.jpg` | menitroso | ĩshiisa | `LEXR-01023` |
| `diccionario_general/menor,_segundo.jpg` | menor, segundo | e’stewe’sh | `LEXR-03402` |
| `diccionario_general/menospreciar.jpg` | menospreciar | dyi’wẽjẽ- | `LEXR-01788` |
| `diccionario_general/mentar,_mencionar.jpg` | mentar, mencionar | cysus-, syusu- | `LEXR-03287` |
| `diccionario_general/menudo.jpg` | menudo | mush | `LEXR-02851` |
| `diccionario_general/mercado.jpg` | mercado | mercau | `LEXR-00715` |
| `diccionario_general/mermar,_disminuir,_encogerse.jpg` | mermar, disminuir, encogerse | le’chi- | `LEXR-03503` |
| `diccionario_general/mes_para_sembrar_maíz.jpg` | mes para sembrar maíz | cutyj uja a’te | `LEXR-02302` |
| `diccionario_general/metamorfosear_(ej._mariposa).jpg` | metamorfosear (ej. mariposa) | peecupy- | `LEXR-03916` |
| `diccionario_general/meter_(cosa_gruesa).jpg` | meter (cosa gruesa) | cupjat- | `LEXR-01852` |
| `diccionario_general/meter_(repetidas_veces).jpg` | meter (repetidas veces) | cuptje’tje- | `LEXR-01853` |
| `diccionario_general/meter_debajo_de.jpg` | meter debajo de | yu’ãsh-, yu’ãshi- | `LEXR-02559` |
| `diccionario_general/meter_en,_echar_en.jpg` | meter en, echar en | yu’achj-, yu’acje- | `LEXR-01020` |
| `diccionario_general/mezclar.jpg` | mezclar | ca’nd-, ca’ndu- | `LEXR-02739` |
| `diccionario_general/mezquino.jpg` | mezquino | ũchji’ndy | `LEXR-02252` |
| `diccionario_general/mi_(femenino).jpg` | mi (femenino) | ũ’cue | `LEXR-03722` |
| `diccionario_general/mico.jpg` | mico | micu | `LEXR-02113` |
| `diccionario_general/miel_de_abeja.jpg` | miel de abeja | chji’ndy mil | `LEXR-02806` |
| `diccionario_general/miel_de_caña.jpg` | miel de caña | ñusha mil | `LEXR-00671` |
| `diccionario_general/miembros_del_cabildo,_cabildantes.jpg` | miembros del cabildo, cabildantes | cabilduwe’sh | `LEXR-03787` |
| `diccionario_general/mientras,_durante._._..jpg` | mientras, durante... | -pcachja’ | `LEXR-00381` |
| `diccionario_general/mirar_(al_mismo_tiempo_que_hace_otra_cosa).jpg` | mirar (al mismo tiempo que hace otra cosa) | iitjeng- | `LEXR-00970` |
| `diccionario_general/mirar_(repetidas_veces).jpg` | mirar (repetidas veces) | cuyu’yu- | `LEXR-03835` |
| `diccionario_general/mirar_a_lo_lejos.jpg` | mirar a lo lejos | spay-, spayúu- | `LEXR-01484` |
| `diccionario_general/mirar_adentro.jpg` | mirar adentro | cuy-, cuyúu- | `LEXR-02206` |
| `diccionario_general/mirar_al_otro_lado.jpg` | mirar al otro lado | pesay-, pesayu- | `LEXR-00817` |
| `diccionario_general/mirar_arriba_(repetidas_veces).jpg` | mirar arriba (repetidas veces) | pagayu’yu- | `LEXR-01672` |
| `diccionario_general/mirar_atrás,_voltearse_para_mirar_atrás.jpg` | mirar atrás, voltearse para mirar atrás | yu’tjeng-, yu’tjengu- | `LEXR-00753` |
| `diccionario_general/mirar_hacia_abajo_(repetidas_veces).jpg` | mirar hacia abajo (repetidas veces) | squiiyu’yu- | `LEXR-03154` |
| `diccionario_general/mitad.jpg` | mitad | pyãj, pyãjn | `LEXR-03507` |
| `diccionario_general/moco.jpg` | moco | ñuty | `LEXR-02197` |
| `diccionario_general/mojado.jpg` | mojado | le’leni | `LEXR-00889` |
| `diccionario_general/mojar,_regar.jpg` | mojar, regar | le’le- | `LEXR-00977` |
| `diccionario_general/mojar,_remojar.jpg` | mojar, remojar | tuupja’j-, tuupja’ja- | `LEXR-02769` |
| `diccionario_general/mojarse.jpg` | mojarse | cã’tu’j-, cã’tu’ju- | `LEXR-01448` |
| `diccionario_general/moler.jpg` | moler | ũ’cj-, ũ’cju- | `LEXR-01184` |
| `diccionario_general/moler_(cosa_aquada).jpg` | moler (cosa aquada) | lu’l-, lu’lu- | `LEXR-01387` |
| `diccionario_general/moler_(repetidas_veces).jpg` | moler (repetidas veces) | iiweesu’s- | `LEXR-02312` |
| `diccionario_general/moler_caña.jpg` | moler caña | cu’nd-, cu’ndu- | `LEXR-03473` |
| `diccionario_general/moler_finito,_desmenuzar.jpg` | moler finito, desmenuzar | iiweesu-, iiweesúu- | `LEXR-02210` |
| `diccionario_general/molestar_(hablando),_estorbar.jpg` | molestar (hablando), estorbar | cuch we’we- | `LEXR-00404` |
| `diccionario_general/molestar_(un_ruido),_hacer_bulla.jpg` | molestar (un ruido), hacer bulla | cuch sus-, cuch susu- | `LEXR-01593` |
| `diccionario_general/molestar,_picar_(pulga).jpg` | molestar, picar (pulga) | fylele- | `LEXR-01789` |
| `diccionario_general/molestar,_poner_pereque.jpg` | molestar, poner pereque | cuch vit-, cuch vitu- | `LEXR-03584` |
| `diccionario_general/molleja.jpg` | molleja | shũcy | `LEXR-01620` |
| `diccionario_general/moneda_fraccionaria.jpg` | moneda fraccionaria | vyuu mush | `LEXR-02726` |
| `diccionario_general/monedas_fraccionarias.jpg` | monedas fraccionarias | vyuu mush | `LEXR-01629` |
| `diccionario_general/mono_nocturno.jpg` | mono nocturno | wenze | `LEXR-01427` |
| `diccionario_general/montar.jpg` | montar | a’j-, a’ja- | `LEXR-01107` |
| `diccionario_general/montaña.jpg` | montaña | vits wala | `LEXR-02505` |
| `diccionario_general/montaña_derribada.jpg` | montaña derribada | ucani | `LEXR-03489` |
| `diccionario_general/montículo_de_tierra.jpg` | montículo de tierra | quiwe muts | `LEXR-03239` |
| `diccionario_general/montón,_montículo.jpg` | montón, montículo | muts | `LEXR-01151` |
| `diccionario_general/moquear.jpg` | moquear | ñutyji- | `LEXR-00575` |
| `diccionario_general/morado.jpg` | morado | cjũch bejbej | `LEXR-03639` |
| `diccionario_general/morder_(culebra).jpg` | morder (culebra) | pqui’se (T) | `LEXR-02221` |
| `diccionario_general/morir_en_lugar_de_otro.jpg` | morir en lugar de otro | paauu- | `LEXR-00623` |
| `diccionario_general/mortal,_destinado_a_morir.jpg` | mortal, destinado a morir | uuwa’jsa | `LEXR-03634` |
| `diccionario_general/mosca.jpg` | mosca | fĩsh, fynej | `LEXR-03675` |
| `diccionario_general/mosquito_(insecto).jpg` | mosquito (insecto) | bus | `LEXR-01711` |
| `diccionario_general/mostacilla_(insecto).jpg` | mostacilla (insecto) | puca | `LEXR-01157` |
| `diccionario_general/mostrar.jpg` | mostrar | tywes-, tywesu- (cywes-) | `LEXR-01005` |
| `diccionario_general/mostrar_los_dientes_(de_contento).jpg` | mostrar los dientes (de contento) | anzu’nzu- | `LEXR-02295` |
| `diccionario_general/mostrenco,_sin_marca.jpg` | mostrenco, sin marca | iisawa’jnimée | `LEXR-01145` |
| `diccionario_general/motilón_(árbol,_con_fruta_comestible).jpg` | motilón (árbol, con fruta comestible) | capijnz | `LEXR-02981` |
| `diccionario_general/moverse.jpg` | moverse | ẽsẽ-, ẽsẽje- | `LEXR-00855` |
| `diccionario_general/moverse_(repetidas_veces).jpg` | moverse (repetidas veces) | ẽsẽ’sẽ- | `LEXR-01189` |
| `diccionario_general/mucho,_muy.jpg` | mucho, muy | wala | `LEXR-03793` |
| `diccionario_general/mudar_la_piel.jpg` | mudar la piel | scuupy- | `LEXR-03319` |
| `diccionario_general/mudarse_de_casa,_quitarse_de,_retirarse_de.jpg` | mudarse de casa, quitarse de, retirarse de | muvijty-, muvityíi- | `LEXR-01228` |
| `diccionario_general/mudo.jpg` | mudo | we’weya’ ãjasamée | `LEXR-02771` |
| `diccionario_general/muela.jpg` | muela | qui’tj wala | `LEXR-00991` |
| `diccionario_general/muerte_(futura).jpg` | muerte (futura) | uuwa’j | `LEXR-02770` |
| `diccionario_general/muerto.jpg` | muerto | icjni | `LEXR-00882` |
| `diccionario_general/mujer_encinta,_embarazada.jpg` | mujer encinta, embarazada | tutyjte nasa ji’pjsa | `LEXR-01762` |
| `diccionario_general/murciélago.jpg` | murciélago | cjĩtse | `LEXR-03104` |
| `diccionario_general/murmurar.jpg` | murmurar | we’wewe- | `LEXR-00660` |
| `diccionario_general/murmurar_(ruido_del_río).jpg` | murmurar (ruido del río) | shwawa- | `LEXR-02498` |
| `diccionario_general/muy_(árbol,_que_carga_pepa).jpg` | muy (árbol, que carga pepa) | jande | `LEXR-01663` |
| `diccionario_general/muy_agradable.jpg` | muy agradable | wẽtwẽt | `LEXR-03304` |
| `diccionario_general/muy_cerca.jpg` | muy cerca | utyutya | `LEXR-01691` |
| `diccionario_general/muy_de_mañana,_temprano.jpg` | muy de mañana, temprano | cusíi | `LEXR-03902` |
| `diccionario_general/muy_sumamente_(superlativo).jpg` | muy sumamente (superlativo) | iiméj | `LEXR-03819` |
| `diccionario_general/muy_triste.jpg` | muy triste | ñusñus | `LEXR-00477` |
| `diccionario_general/muy_tupido.jpg` | muy tupido | tjutj tjujt | `LEXR-02590` |
| `diccionario_general/más.jpg` | más | jwee | `LEXR-00704` |
| `diccionario_general/más_(comparativo).jpg` | más (comparativo) | wejy | `LEXR-00567` |
| `diccionario_general/más_antes.jpg` | más antes | jwee ũ’nacje | `LEXR-01148` |
| `diccionario_general/más_corto.jpg` | más corto | tuwtuw | `LEXR-01421` |
| `diccionario_general/más_tarde.jpg` | más tarde | ãchãch | `LEXR-02908` |
| `diccionario_general/más,_grave,_peor.jpg` | más, grave, peor | tjaacue | `LEXR-01418` |
| `diccionario_general/nacimiento,_lugar_de_nacimiento.jpg` | nacimiento, lugar de nacimiento | upyni | `LEXR-01262` |
| `diccionario_general/nadar.jpg` | nadar | pejnd-, pendu- | `LEXR-02708` |
| `diccionario_general/nadia.jpg` | nadia | quim yujva | `LEXR-00917` |
| `diccionario_general/nadie,_ninguno.jpg` | nadie, ninguno | maa yujva | `LEXR-03358` |
| `diccionario_general/naranjal.jpg` | naranjal | llima ej | `LEXR-01736` |
| `diccionario_general/narices,_ventana_de_la_nariz.jpg` | narices, ventana de la nariz | ĩts puty | `LEXR-01433` |
| `diccionario_general/nariz_aguileña,_narigudo.jpg` | nariz aguileña, narigudo | ĩts zec | `LEXR-03160` |
| `diccionario_general/nariz_chata.jpg` | nariz chata | ĩts tutj | `LEXR-02145` |
| `diccionario_general/nariz_filuda.jpg` | nariz filuda | ĩts taty | `LEXR-00762` |
| `diccionario_general/necesidad.jpg` | necesidad | peejini | `LEXR-01677` |
| `diccionario_general/necesitar,_faltar,_hacer_falta.jpg` | necesitar, faltar, hacer falta | pejtya-, pejíi- | `LEXR-00815` |
| `diccionario_general/necesitar,_hacer_falta.jpg` | necesitar, hacer falta | jypejy-, jypeejy- | `LEXR-01866` |
| `diccionario_general/negar,_no_divulgar.jpg` | negar, no divulgar | yuwe apj- | `LEXR-02194` |
| `diccionario_general/negar,_ocultar.jpg` | negar, ocultar | paana-, paanáa- | `LEXR-00432` |
| `diccionario_general/negro,_sucio.jpg` | negro, sucio | cjũch | `LEXR-01205` |
| `diccionario_general/ni_siquiera.jpg` | ni siquiera | yujva | `LEXR-03909` |
| `diccionario_general/ni_un_poco,_ni_siquiera.jpg` | ni un poco, ni siquiera | wej yujva | `LEXR-03328` |
| `diccionario_general/nido.jpg` | nido | vichacue yat | `LEXR-02898` |
| `diccionario_general/nivelar,_allanar.jpg` | nivelar, allanar | uucue’j-, uucue’je- | `LEXR-03245` |
| `diccionario_general/niña_del_ojo,_pupila.jpg` | niña del ojo, pupila | yafy dyuus | `LEXR-03465` |
| `diccionario_general/niño.jpg` | niño | luuçx | `LEXR-01738` |
| `diccionario_general/niño_prematuro.jpg` | niño prematuro | iitey casesa | `LEXR-01728` |
| `diccionario_general/no.jpg` | no | mee- | `LEXR-01298` |
| `diccionario_general/no_en_vano.jpg` | no en vano | cyulmée | `LEXR-00502` |
| `diccionario_general/nombrado,_con_el_nombre_de.jpg` | nombrado, con el nombre de | yaasesa | `LEXR-02905` |
| `diccionario_general/nosotros,_nosotras.jpg` | nosotros, nosotras | cue’sh | `LEXR-03225` |
| `diccionario_general/nube_obscura_(mal_agüero).jpg` | nube obscura (mal agüero) | ẽe cjũch | `LEXR-01355` |
| `diccionario_general/nubes_dispersas.jpg` | nubes dispersas | ẽe piishá | `LEXR-00675` |
| `diccionario_general/nuca.jpg` | nuca | tyjicj shbimby | `LEXR-02636` |
| `diccionario_general/nuche_(insecto).jpg` | nuche (insecto) | ãpwes | `LEXR-01104` |
| `diccionario_general/nueve.jpg` | nueve | nueve | `LEXR-02852` |
| `diccionario_general/nuevo.jpg` | nuevo | u’se | `LEXR-00655` |
| `diccionario_general/nuez_de_la_garganta.jpg` | nuez de la garganta | tyjicj lul | `LEXR-01093` |
| `diccionario_general/nunca.jpg` | nunca | ũca | `LEXR-02510` |
| `diccionario_general/nunca,_jamás.jpg` | nunca, jamás | bagach yujva | `LEXR-03163` |
| `diccionario_general/nutria.jpg` | nutria | yu’alcu | `LEXR-03529` |
| `diccionario_general/nutria_(mamífero).jpg` | nutria (mamífero) | yu’nutre | `LEXR-01835` |
| `diccionario_general/o._._._o.jpg` | o...o | ma’c yuu...ma’c yuu | `LEXR-00891` |
| `diccionario_general/obediente.jpg` | obediente | nwẽese’jsa | `LEXR-02542` |
| `diccionario_general/obligatoriamente.jpg` | obligatoriamente | ãandyijimée | `LEXR-02976` |
| `diccionario_general/obscurecer.jpg` | obscurecer | nuychji’ndy-, nuychji’ndyi | `LEXR-01304` |
| `diccionario_general/obscurecerse.jpg` | obscurecerse | shi’ndy-, shi’ndyi- (chji’ndy-) | `LEXR-03345` |
| `diccionario_general/obscuro.jpg` | obscuro | shi’ndy (chji’ndy) | `LEXR-01406` |
| `diccionario_general/ocho.jpg` | ocho | ocho | `LEXR-01235` |
| `diccionario_general/ocultar,_disimular.jpg` | ocultar, disimular | peenda-, peendáa- | `LEXR-03882` |
| `diccionario_general/ocultarse_el_sol.jpg` | ocultarse el sol | sec paatsu- | `LEXR-01318` |
| `diccionario_general/odedecer,_hacer_caso.jpg` | odedecer, hacer caso | nwẽese’j-, nwẽese’je- | `LEXR-03567` |
| `diccionario_general/ofrecer_sal_a_un_caballo.jpg` | ofrecer sal a un caballo | cytu’cy-, cytu’qui- | `LEXR-03046` |
| `diccionario_general/ofrendar,_propiciar_a_los_espíritus.jpg` | ofrendar, propiciar a los espíritus | pujnde-, punde- | `LEXR-02009` |
| `diccionario_general/oirse,_sonar.jpg` | oirse, sonar | ptjũuse- | `LEXR-03842` |
| `diccionario_general/ojo_de_aguja.jpg` | ojo de aguja | yunz cafy | `LEXR-03216` |
| `diccionario_general/ola_(del_río_o_mar).jpg` | ola (del río o mar) | yu’ tũchjasa | `LEXR-03689` |
| `diccionario_general/oler.jpg` | oler | puta-, putáa- | `LEXR-01311` |
| `diccionario_general/oler,_coger_rastro.jpg` | oler, coger rastro | jyputa-, jyputáa- | `LEXR-02316` |
| `diccionario_general/olla_de_barro.jpg` | olla de barro | quiwe mityj | `LEXR-00995` |
| `diccionario_general/olla_para_guarapo.jpg` | olla para guarapo | beca mityj | `LEXR-03281` |
| `diccionario_general/olor_fragante.jpg` | olor fragante | wẽt putasá | `LEXR-01178` |
| `diccionario_general/oloroso,_fétido.jpg` | oloroso, fétido | cjãp | `LEXR-01204` |
| `diccionario_general/olvidar.jpg` | olvidar | pecu’tjwe’sh | `LEXR-03506` |
| `diccionario_general/olvidarse.jpg` | olvidarse | ya’pechcanu- | `LEXR-02870` |
| `diccionario_general/olvido,_olvidado.jpg` | olvido, olvidado | pechanuni | `LEXR-02992` |
| `diccionario_general/opacar,_obscurecerse.jpg` | opacar, obscurecerse | tu’vi- | `LEXR-00735` |
| `diccionario_general/orange.jpg` | orange | bejbej | `LEXR-00483` |
| `diccionario_general/ordenar_(repetidas_veces).jpg` | ordenar (repetidas veces) | jycaaja’ja- | `LEXR-00708` |
| `diccionario_general/ordenar,_gobernar.jpg` | ordenar, gobernar | jycaa-jycaja- | `LEXR-03562` |
| `diccionario_general/orejudo.jpg` | orejudo | chũpy | `LEXR-02915` |
| `diccionario_general/orgullo.jpg` | orgullo | iiwejch yaacyni | `LEXR-01220` |
| `diccionario_general/orgullo_(habla).jpg` | orgullo (habla) | iiwejch we’weni | `LEXR-03406` |
| `diccionario_general/orgulloso.jpg` | orgulloso | iiwejch | `LEXR-03138` |
| `diccionario_general/orilla_de_la_olla.jpg` | orilla de la olla | mityj tjũ’wẽ | `LEXR-01227` |
| `diccionario_general/orilla_del_río.jpg` | orilla del río | yu’puts | `LEXR-02290` |
| `diccionario_general/orinar.jpg` | orinar | su’s-, su’su- | `LEXR-03389` |
| `diccionario_general/orinar_en.jpg` | orinar en | avysu’s-, avysu’su- | `LEXR-01274` |
| `diccionario_general/orín.jpg` | orín | inz | `LEXR-01599` |
| `diccionario_general/oso.jpg` | oso | e’shavy | `LEXR-03642` |
| `diccionario_general/otra_vez.jpg` | otra vez | qui’quin (qui’) | `LEXR-03883` |
| `diccionario_general/otro.jpg` | otro | vite | `LEXR-01492` |
| `diccionario_general/oveja.jpg` | oveja | piishá | `LEXR-01398` |
| `diccionario_general/oxidado.jpg` | oxidado | baytu’cni | `LEXR-03352` |
| `diccionario_general/oxidado,_corroído.jpg` | oxidado, corroído | inzũ’ni | `LEXR-03604` |
| `diccionario_general/oxidarse.jpg` | oxidarse | baytu’c-, baytu’cu- | `LEXR-03785` |
| `diccionario_general/oyente.jpg` | oyente | wẽsẽ’jsa | `LEXR-01495` |
| `diccionario_general/pacunga_(planta).jpg` | pacunga (planta) | tcu’nz | `LEXR-01254` |
| `diccionario_general/padecer.jpg` | padecer | ñus cnay- | `LEXR-03308` |
| `diccionario_general/padecer_una_enfermdad.jpg` | padecer una enfermdad | wee cnay- | `LEXR-01426` |
| `diccionario_general/padre.jpg` | padre | tata | `LEXR-01415` |
| `diccionario_general/padre_o_madre_con_el_hijo.jpg` | padre o madre con el hijo | pchi’c | `LEXR-02793` |
| `diccionario_general/padre_o_madre_con_la_hija.jpg` | padre o madre con la hija | pniisa | `LEXR-01399` |
| `diccionario_general/padrino_con_ahijado_o_ahijada.jpg` | padrino con ahijado o ahijada | pneeney | `LEXR-03028` |
| `diccionario_general/padrinos_(de_matrimonio).jpg` | padrinos (de matrimonio) | cpu’nzesawe’sh | `LEXR-02366` |
| `diccionario_general/pagado.jpg` | pagado | deweni | `LEXR-02955` |
| `diccionario_general/pagar.jpg` | pagar | dewe-, dewée- | `LEXR-02427` |
| `diccionario_general/pagar_por_otro.jpg` | pagar por otro | paandewe- | `LEXR-01670` |
| `diccionario_general/palma_de_la_mano.jpg` | palma de la mano | cuse pjapj | `LEXR-03450` |
| `diccionario_general/palo_de_telar_(sostiene_el_ñuwe).jpg` | palo de telar (sostiene el ñuwe) | sacue | `LEXR-02062` |
| `diccionario_general/palo_horitzontal_del_telar.jpg` | palo horitzontal del telar | atyj tel cuse | `LEXR-02565` |
| `diccionario_general/palo_madera.jpg` | palo madera | fytũu | `LEXR-00508` |
| `diccionario_general/palo_vertical_del_telar.jpg` | palo vertical del telar | atyj tel chinda | `LEXR-02804` |
| `diccionario_general/paloma.jpg` | paloma | tumb | `LEXR-01003` |
| `diccionario_general/panderé_(árbol).jpg` | panderé (árbol) | paandlé | `LEXR-03144` |
| `diccionario_general/panzón.jpg` | panzón | buc | `LEXR-03010` |
| `diccionario_general/papa_menudita.jpg` | papa menudita | ca’ga mush | `LEXR-02516` |
| `diccionario_general/papal.jpg` | papal | ca’ga ej | `LEXR-02092` |
| `diccionario_general/papaya.jpg` | papaya | payáa | `LEXR-01074` |
| `diccionario_general/paralizarse,_entumirse.jpg` | paralizarse, entumirse | jyandu-, jyandúu- | `LEXR-03455` |
| `diccionario_general/pararse,_ponerse_de_pie.jpg` | pararse, ponerse de pie | yuju- | `LEXR-00571` |
| `diccionario_general/parcialmente_encogido_(las_piernas).jpg` | parcialmente encogido (las piernas) | spat-spate | `LEXR-00642` |
| `diccionario_general/pardo.jpg` | pardo | cjũchcjũchdyi’ | `LEXR-00593` |
| `diccionario_general/pariente_(con_respecto_a_otro_pariente.jpg` | pariente (con respecto a otro pariente | pwe’sh | `LEXR-01478` |
| `diccionario_general/parir,_poner_huevos_(gallinas).jpg` | parir, poner huevos (gallinas) | duu- | `LEXR-01858` |
| `diccionario_general/parpadear.jpg` | parpadear | upja’pja- | `LEXR-02286` |
| `diccionario_general/partear,_atender_el_parto.jpg` | partear, atender el parto | tutyj jya’ndy- | `LEXR-02283` |
| `diccionario_general/participar_en_la_molienda.jpg` | participar en la molienda | paaũ’cj-, paaũ’cju- | `LEXR-01308` |
| `diccionario_general/partidario.jpg` | partidario | ju’ngusa | `LEXR-01795` |
| `diccionario_general/partir_(en_dos_o_más_partes).jpg` | partir (en dos o más partes) | petsjuutsju- | `LEXR-02758` |
| `diccionario_general/partir_en_dos,_dividir.jpg` | partir en dos, dividir | pe’lande- | `LEXR-01676` |
| `diccionario_general/partir_en_varios_pedazos,_despedazar.jpg` | partir en varios pedazos, despedazar | pe’ltende- | `LEXR-01309` |
| `diccionario_general/pasado_mañana.jpg` | pasado mañana | cuscuscjẽ | `LEXR-00696` |
| `diccionario_general/pasajero,_que_pasa_pronto.jpg` | pasajero, que pasa pronto | scjẽwsa, scjẽwwa’jsa | `LEXR-03917` |
| `diccionario_general/pasajero,_viajero.jpg` | pasajero, viajero | u’jsa, u’jwa’jsa | `LEXR-02404` |
| `diccionario_general/pasar.jpg` | pasar | jycjẽw-, jycjẽúu- | `LEXR-00797` |
| `diccionario_general/pasar_(hacia_abajo).jpg` | pasar (hacia abajo) | scjẽw-, scjẽúu- | `LEXR-00827` |
| `diccionario_general/pasar_(repetidas_veces).jpg` | pasar (repetidas veces) | pesaja’ja- | `LEXR-01076` |
| `diccionario_general/pasar_a_través_(en_plano).jpg` | pasar a través (en plano) | cjẽw-, cjẽúu- | `LEXR-02608` |
| `diccionario_general/pasar_de_un_lado_a_otro,_venir_del_otro_lado.jpg` | pasar de un lado a otro, venir del otro lado | pesaj-, pesaja- | `LEXR-03264` |
| `diccionario_general/pasear.jpg` | pasear | pasiáa- | `LEXR-02435` |
| `diccionario_general/patear.jpg` | patear | swẽtj-, swẽtje- | `LEXR-03486` |
| `diccionario_general/patimocho.jpg` | patimocho | chinda much | `LEXR-02039` |
| `diccionario_general/pavo_del_monte.jpg` | pavo del monte | finzh | `LEXR-02700` |
| `diccionario_general/pecar,_caer_en_pecado.jpg` | pecar, caer en pecado | pcalte wete- | `LEXR-00810` |
| `diccionario_general/pecarí.jpg` | pecarí | quiwe cuchi | `LEXR-02858` |
| `diccionario_general/pechanga,_verbena_(planta).jpg` | pechanga, verbena (planta) | pchanga | `LEXR-03568` |
| `diccionario_general/pedazo_por_pedazo.jpg` | pedazo por pedazo | pe’lpe’la | `LEXR-02325` |
| `diccionario_general/pedido.jpg` | pedido | pẽyni | `LEXR-02125` |
| `diccionario_general/pedir.jpg` | pedir | pẽjy-, pẽyi- | `LEXR-03440` |
| `diccionario_general/pedir_fiado,_dar_fiado.jpg` | pedir fiado, dar fiado | ulu’j-, ulu’ju- | `LEXR-03034` |
| `diccionario_general/pedir,_preguntar.jpg` | pedir, preguntar | pe’w-, pe’wu- | `LEXR-03458` |
| `diccionario_general/pegajoso.jpg` | pegajoso | spiina’ | `LEXR-03857` |
| `diccionario_general/pegar_(con_la_mano).jpg` | pegar (con la mano) | uyi-, uyíi- | `LEXR-02725` |
| `diccionario_general/pegar_con_goma.jpg` | pegar con goma | cne’ta’j-, cne’ta’ja- | `LEXR-01281` |
| `diccionario_general/peinilla.jpg` | peinilla | cchill wala (chill wala) | `LEXR-00488` |
| `diccionario_general/pelado,_desnudo.jpg` | pelado, desnudo | tũpy | `LEXR-03366` |
| `diccionario_general/pelar.jpg` | pelar | tupy-, tupi- (tũpy-) | `LEXR-02797` |
| `diccionario_general/pelar_los_dientes.jpg` | pelar los dientes | anzh-, anzhi- | `LEXR-01027` |
| `diccionario_general/peleador,_pleitista.jpg` | peleador, pleitista | puii-jypaacuesa | `LEXR-01682` |
| `diccionario_general/pelear.jpg` | pelear | puii- | `LEXR-03907` |
| `diccionario_general/pelear_(unos_con_otros).jpg` | pelear (unos con otros) | puuty puii- | `LEXR-01812` |
| `diccionario_general/pellizcar.jpg` | pellizcar | wãatsja- | `LEXR-01099` |
| `diccionario_general/pelo_corto,_pelón,_motilón.jpg` | pelo corto, pelón, motilón | dycjas much | `LEXR-00878` |
| `diccionario_general/pelusa_de_maíz.jpg` | pelusa de maíz | cutyj cjas | `LEXR-01373` |
| `diccionario_general/penca_de_cabuya.jpg` | penca de cabuya | bats ets | `LEXR-00583` |
| `diccionario_general/pender.jpg` | pender | pẽ’tje- | `LEXR-02124` |
| `diccionario_general/pendiente.jpg` | pendiente | pẽ’tjesa | `LEXR-02993` |
| `diccionario_general/pendiente,_inclinación_del_tejado.jpg` | pendiente, inclinación del tejado | catja´ | `LEXR-01909` |
| `diccionario_general/pene.jpg` | pene | chull | `LEXR-00868` |
| `diccionario_general/pensamiento.jpg` | pensamiento | ũus yaacyni | `LEXR-01185` |
| `diccionario_general/pensar_mal.jpg` | pensar mal | fiy yajcy- | `LEXR-02209` |
| `diccionario_general/pensar,_creer,_suponer.jpg` | pensar, creer, suponer | sũj-, sũjũ-, sũu- | `LEXR-03894` |
| `diccionario_general/pequeño.jpg` | pequeño | le’ch, le’chcuẽ | `LEXR-03676` |
| `diccionario_general/perder.jpg` | perder | iviit-, iviitu- | `LEXR-01222` |
| `diccionario_general/perder_de_vista.jpg` | perder de vista | pu’vitu- | `LEXR-00909` |
| `diccionario_general/perder_sabor.jpg` | perder sabor | shũucãj- | `LEXR-03299` |
| `diccionario_general/perdiz.jpg` | perdiz | fi’l | `LEXR-00601` |
| `diccionario_general/perdonar.jpg` | perdonar | peltunaĩ- | `LEXR-03342` |
| `diccionario_general/perdonarse.jpg` | perdonarse | puuty ya’peltunaĩ- | `LEXR-01313` |
| `diccionario_general/perezozo.jpg` | perezozo | watycue | `LEXR-02078` |
| `diccionario_general/perforar_(varias_cosas_o_en_varias_partes).jpg` | perforar (varias cosas o en varias partes) | swendende- | `LEXR-02182` |
| `diccionario_general/perico_(ave).jpg` | perico (ave) | chĩ’ | `LEXR-02203` |
| `diccionario_general/perico_plomo_(aven_nocturna,_mal_agüero).jpg` | perico plomo (aven nocturna, mal agüero) | echtel | `LEXR-00967` |
| `diccionario_general/periquillo.jpg` | periquillo | well le’chcue, wellcue | `LEXR-00933` |
| `diccionario_general/permanentamente.jpg` | permanentamente | nes | `LEXR-01389` |
| `diccionario_general/permitir_amanecer.jpg` | permitir amanecer | nuype’te- | `LEXR-01152` |
| `diccionario_general/permitir_asistir,_mandar_reunirse.jpg` | permitir asistir, mandar reunirse | caapcjaacje’j-, caapcjaacje’je- | `LEXR-01200` |
| `diccionario_general/permitir_buscar,_mandar_buscar.jpg` | permitir buscar, mandar buscar | cpaacue’j-, cpaacue’je- | `LEXR-01783` |
| `diccionario_general/permitir_comer,_dejar_comer.jpg` | permitir comer, dejar comer | cã’wẽ’j-, cã’wẽjẽ- | `LEXR-02954` |
| `diccionario_general/permitir_contestar.jpg` | permitir contestar | cpaasu’j-, cpaasu’ju- | `LEXR-03729` |
| `diccionario_general/permitir_destruir.jpg` | permitir destruir | caaiviitu’j-, caaiviitu’ju- | `LEXR-00484` |
| `diccionario_general/permitir_entrar_y_sentarse.jpg` | permitir entrar y sentarse | cayachiji´j-, caycachji´ji- | `LEXR-03040` |
| `diccionario_general/permitir_fermentar.jpg` | permitir fermentar | nuypusu- | `LEXR-01605` |
| `diccionario_general/permitir_oír.jpg` | permitir oír | cwẽese’j-, cwẽese’je- | `LEXR-03560` |
| `diccionario_general/permitir_pasar_el_día.jpg` | permitir pasar el día | nuyfi’nze- | `LEXR-02706` |
| `diccionario_general/permitir_tocar,_partear.jpg` | permitir tocar, partear | cjya’ndyi’j-, cjya’ndyi’ji- | `LEXR-03223` |
| `diccionario_general/permitir_vender.jpg` | permitir vender | caatyweyu’j-, caatyweyu’ju- | `LEXR-00951` |
| `diccionario_general/pero.jpg` | pero | nava | `LEXR-01062` |
| `diccionario_general/perro.jpg` | perro | alcu | `LEXR-02690` |
| `diccionario_general/persona_despreciado.jpg` | persona despreciado | yaatsesa | `LEXR-02081` |
| `diccionario_general/persona_que_acompaña_voluntariamente_(al_ir).jpg` | persona que acompaña voluntariamente (al ir) | paau’jsa | `LEXR-01929` |
| `diccionario_general/persona_que_acompaña_voluntariamente_(al_venir).jpg` | persona que acompaña voluntariamente (al venir) | paayuusa | `LEXR-02116` |
| `diccionario_general/persona_que_causa_daño_a_otro.jpg` | persona que causa daño a otro | ptjãawesa | `LEXR-01245` |
| `diccionario_general/persona_que_da_hospedaje,_persona_que_pide_hospedaje.jpg` | persona que da hospedaje, persona que pide hospedaje | yat pqui’sa | `LEXR-01957` |
| `diccionario_general/persona_que_desea_algo.jpg` | persona que desea algo | jytjãassa | `LEXR-00417` |
| `diccionario_general/persona_que_encarga_algo.jpg` | persona que encarga algo | paawe’wesa | `LEXR-03905` |
| `diccionario_general/persona_que_está_presente.jpg` | persona que está presente | ũssa | `LEXR-02876` |
| `diccionario_general/persona_que_está,_equivocada_o_desviada.jpg` | persona que está, equivocada o desviada | jyumbasa | `LEXR-02618` |
| `diccionario_general/persona_que_habla_páez.jpg` | persona que habla páez | nasa yuwe we’wessa | `LEXR-01740` |
| `diccionario_general/persona_que_rie.jpg` | persona que rie | shicasa | `LEXR-02633` |
| `diccionario_general/persuadir.jpg` | persuadir | peevisha- | `LEXR-01930` |
| `diccionario_general/persuadir_a_otro_quedarse,_rogar_se_quede.jpg` | persuadir a otro quedarse, rogar se quede | neevisha- | `LEXR-01064` |
| `diccionario_general/persuadir,_hablar_con_cariño.jpg` | persuadir, hablar con cariño | tywe’we- | `LEXR-03211` |
| `diccionario_general/pesado.jpg` | pesado | duj | `LEXR-01047` |
| `diccionario_general/pescar.jpg` | pescar | wendy uwe- | `LEXR-01951` |
| `diccionario_general/pestaña,_ceja.jpg` | pestaña, ceja | yafy cjas | `LEXR-03277` |
| `diccionario_general/picadura.jpg` | picadura | pinzh | `LEXR-03093` |
| `diccionario_general/picante,_amargo.jpg` | picante, amargo | yaj | `LEXR-01179` |
| `diccionario_general/picar,_hacer_pedazos,_roer.jpg` | picar, hacer pedazos, roer | tut-, tutúu- | `LEXR-01329` |
| `diccionario_general/pichón_(ave).jpg` | pichón (ave) | tumb luuch | `LEXR-01623` |
| `diccionario_general/pijaos_(tribu_indígena).jpg` | Pijaos (tribu indígena) | pi’pyshavy | `LEXR-03590` |
| `diccionario_general/pilado.jpg` | pilado | playni | `LEXR-02220` |
| `diccionario_general/pilar,_cocer_maíz_para_quitar_la_cáscara.jpg` | pilar, cocer maíz para quitar la cáscara | plaaĩ-, plaaĩi- | `LEXR-03519` |
| `diccionario_general/pintado,_teñido.jpg` | pintado, teñido | bite | `LEXR-03795` |
| `diccionario_general/pinto_(blanco_y_negro).jpg` | pinto (blanco y negro) | shlalá | `LEXR-03208` |
| `diccionario_general/pinto,_moteado.jpg` | pinto, moteado | fi’cue | `LEXR-02885` |
| `diccionario_general/pisar,_pisotear.jpg` | pisar, pisotear | a’cji’j-, a’cji’ji- | `LEXR-03617` |
| `diccionario_general/pisotear_(repetidas_veces).jpg` | pisotear (repetidas veces) | waacji’cji’j- | `LEXR-00466` |
| `diccionario_general/pisotear,_pisar.jpg` | pisotear, pisar | waacji’cj-, waacji’cji- | `LEXR-01564` |
| `diccionario_general/piña.jpg` | piña | chajú | `LEXR-01976` |
| `diccionario_general/planchudo.jpg` | planchudo | tsep | `LEXR-00925` |
| `diccionario_general/planta_del_pie,_palma_de_la_mano.jpg` | planta del pie, palma de la mano | pjapj | `LEXR-00819` |
| `diccionario_general/plataforma_en_los_sembrados.jpg` | plataforma en los sembrados | ej atũ | `LEXR-03733` |
| `diccionario_general/platanal.jpg` | platanal | pland ej | `LEXR-01612` |
| `diccionario_general/plato_(de_madera).jpg` | plato (de madera) | bich | `LEXR-00858` |
| `diccionario_general/plegar.jpg` | plegar | sembu’j-, sembu’ju- | `LEXR-03481` |
| `diccionario_general/pleito.jpg` | pleito | puiini | `LEXR-00726` |
| `diccionario_general/pluma_(de_pájaro).jpg` | pluma (de pájaro) | vichacue cjas | `LEXR-02593` |
| `diccionario_general/pluma_de_gallina.jpg` | pluma de gallina | atall cjas | `LEXR-03447` |
| `diccionario_general/plátano.jpg` | plátano | pland | `LEXR-01310` |
| `diccionario_general/plátano_maduro.jpg` | plátano maduro | pland ĩits | `LEXR-01809` |
| `diccionario_general/pobre,_desgraciado.jpg` | pobre, desgraciado | puuple | `LEXR-01159` |
| `diccionario_general/pobre,_pobrecito.jpg` | pobre, pobrecito | fytjaa, fytjaacuẽ | `LEXR-03539` |
| `diccionario_general/poco.jpg` | poco | wej, wejcuẽ | `LEXR-03099` |
| `diccionario_general/poco_a_poco,_despacio.jpg` | poco a poco, despacio | tujndtujnd | `LEXR-00927` |
| `diccionario_general/poco,_poquito.jpg` | poco, poquito | teechcue | `LEXR-00998` |
| `diccionario_general/pocos.jpg` | pocos | manzmanz | `LEXR-02112` |
| `diccionario_general/poder.jpg` | poder | ewuu | `LEXR-00785` |
| `diccionario_general/poder,_completar,_alcanzar,_llegar_el_tiempo.jpg` | poder, completar, alcanzar, llegar el tiempo | ãj-, ãja- | `LEXR-03280` |
| `diccionario_general/poderoso.jpg` | poderoso | chjãchjasa | `LEXR-02422` |
| `diccionario_general/poderoso,_capaz.jpg` | poderoso, capaz | ãjsa | `LEXR-00574` |
| `diccionario_general/podrido.jpg` | podrido | chimby | `LEXR-00774` |
| `diccionario_general/podrir.jpg` | podrir | chimby-, chimbíi- | `LEXR-01654` |
| `diccionario_general/podrirse.jpg` | podrirse | chiiwa’wa- | `LEXR-01119` |
| `diccionario_general/polvo_de_la_casa.jpg` | polvo de la casa | cytã’ tujnd | `LEXR-03708` |
| `diccionario_general/polvo_de_la_tierra.jpg` | polvo de la tierra | quiwe tujnd | `LEXR-03735` |
| `diccionario_general/ponedora_(galiina_que_pone_huevos),_animal_con_cría.jpg` | ponedora (galiina que pone huevos), animal con cría | duusá | `LEXR-01139` |
| `diccionario_general/poner_(repetidas_veces_cosas).jpg` | poner (repetidas veces cosas) | qui’pu’p-, qui’pu’pu- | `LEXR-01248` |
| `diccionario_general/poner_adelante,_arrear.jpg` | poner adelante, arrear | yatsqui’p-, yatsqui’pu- | `LEXR-00751` |
| `diccionario_general/poner_atravesado.jpg` | poner atravesado | paand-, paandúu- | `LEXR-02757` |
| `diccionario_general/poner_encima_de.jpg` | poner encima de | aqui’p-, aqui’pu | `LEXR-02692` |
| `diccionario_general/poner_encima_de_(cosa_larga).jpg` | poner encima de (cosa larga) | acjicj-, acjicje- | `LEXR-02837` |
| `diccionario_general/poner_enjalma,_(fig)_engañar.jpg` | poner enjalma, (fig) engañar | cjalma tyaj- | `LEXR-03103` |
| `diccionario_general/poner_inclinado.jpg` | poner inclinado | queenze’j-, queenze’je- | `LEXR-00915` |
| `diccionario_general/poner_mano_encima_de.jpg` | poner mano encima de | peequinze-, peequinzée- | `LEXR-03237` |
| `diccionario_general/poner_queja.jpg` | poner queja | yuwe cjicj- | `LEXR-02801` |
| `diccionario_general/poner_sobre_el_hombro.jpg` | poner sobre el hombro | jypeecypacy-, jypeecypaqui- | `LEXR-03851` |
| `diccionario_general/poner_sombrero.jpg` | poner sombrero | fĩicj-, fĩicje- | `LEXR-01862` |
| `diccionario_general/poner_torcido,_encorvar.jpg` | poner torcido, encorvar | ta’tsu’ju- | `LEXR-01325` |
| `diccionario_general/poner_vara_a_lo_largo.jpg` | poner vara a lo largo | cfindúu- | `LEXR-00489` |
| `diccionario_general/poner,_colocar.jpg` | poner, colocar | cjicj-, cjicje- | `LEXR-02523` |
| `diccionario_general/poner,_colocar,_edificar.jpg` | poner, colocar, edificar | tyaj-, tyaja-, tyaa- | `LEXR-03750` |
| `diccionario_general/ponerse_amarillo.jpg` | ponerse amarillo | lemúu- | `LEXR-01225` |
| `diccionario_general/ponerse_blando,_ablandarse.jpg` | ponerse blando, ablandarse | lupe- | `LEXR-03023` |
| `diccionario_general/ponerse_caro.jpg` | ponerse caro | pa’ga yuu- | `LEXR-00620` |
| `diccionario_general/ponerse_derecho,_recto,_empinarse.jpg` | ponerse derecho, recto, empinarse | le’ya’- | `LEXR-03865` |
| `diccionario_general/ponerse_el_sol.jpg` | ponerse el sol | sec cjẽj- | `LEXR-00919` |
| `diccionario_general/ponerse_grave,_empeorar.jpg` | ponerse grave, empeorar | tjacue-, tjacuée | `LEXR-02236` |
| `diccionario_general/ponerse_liso,_resbaloso.jpg` | ponerse liso, resbaloso | lavy-, lavi- | `LEXR-01535` |
| `diccionario_general/ponerse_obscuro.jpg` | ponerse obscuro | chji’ndy-, chji’ndyi- | `LEXR-01714` |
| `diccionario_general/ponerse_pesado.jpg` | ponerse pesado | duj-, dujáa- | `LEXR-00782` |
| `diccionario_general/ponerse_pálido.jpg` | ponerse pálido | chijme yuu- | `LEXR-01590` |
| `diccionario_general/ponerse_ronco.jpg` | ponerse ronco | se’se- | `LEXR-01939` |
| `diccionario_general/ponerse_ruana.jpg` | ponerse ruana | jycajts-, jycatsu- | `LEXR-03233` |
| `diccionario_general/ponerse_tupido.jpg` | ponerse tupido | tjutj- tjutjúu- | `LEXR-01882` |
| `diccionario_general/por.jpg` | por | -su | `LEXR-00581` |
| `diccionario_general/por_acá.jpg` | por acá | ayga | `LEXR-01776` |
| `diccionario_general/por_allí.jpg` | por allí | cysu | `LEXR-03451` |
| `diccionario_general/por_allí_(a_través).jpg` | por allí (a través) | cyuy | `LEXR-00503` |
| `diccionario_general/por_consiguiente,_así_que.jpg` | por consiguiente, así que | na’ | `LEXR-03316` |
| `diccionario_general/por_esa_misma_razón.jpg` | por esa misma razón | cyajíi | `LEXR-01209` |
| `diccionario_general/por_eso.jpg` | por eso | naa pa’ga | `LEXR-00718` |
| `diccionario_general/por_eso,_con_el_fin_de_que.jpg` | por eso, con el fin de que | cyaj | `LEXR-02656` |
| `diccionario_general/por_favor.jpg` | por favor | nuu | `LEXR-02382` |
| `diccionario_general/por_igual.jpg` | por igual | teechsa na’wẽrraj | `LEXR-00645` |
| `diccionario_general/por_las_calles.jpg` | por las calles | clliicjunsu | `LEXR-02695` |
| `diccionario_general/por_sí_mismo,_uno_mismo,_propio.jpg` | por sí mismo, uno mismo, propio | peecy | `LEXR-00627` |
| `diccionario_general/portarse_mal.jpg` | portarse mal | fiy yũu- | `LEXR-01861` |
| `diccionario_general/posada.jpg` | posada | paandee yat | `LEXR-03090` |
| `diccionario_general/postrero.jpg` | postrero | nmejtewe’sh | `LEXR-01391` |
| `diccionario_general/potro,_potranco.jpg` | potro, potranco | jimba luuch | `LEXR-02378` |
| `diccionario_general/practicar_brujería.jpg` | practicar brujería | dyijy, yuu- | `LEXR-02812` |
| `diccionario_general/preguntar,_consultar_a_otro.jpg` | preguntar, consultar a otro | paapẽjy-, paapẽyĩ- | `LEXR-03881` |
| `diccionario_general/prematuro.jpg` | prematuro | iitee, iitey | `LEXR-01792` |
| `diccionario_general/preocuparse.jpg` | preocuparse | cuch yajcy- | `LEXR-03558` |
| `diccionario_general/prestar_ayuda.jpg` | prestar ayuda | cuse peequi’j- | `LEXR-02205` |
| `diccionario_general/prestar,_emprestar.jpg` | prestar, emprestar | pqui’j-, pqui’ja- | `LEXR-02760` |
| `diccionario_general/preñada,_enrazada_(animales).jpg` | preñada, enrazada (animales) | tuya | `LEXR-00652` |
| `diccionario_general/prima_(respecto_al_primo).jpg` | prima (respecto al primo) | pucacje npe’sh | `LEXR-03747` |
| `diccionario_general/primero,_antes,_anteriormente.jpg` | primero, antes, anteriormente | nyafy | `LEXR-02889` |
| `diccionario_general/primo_(respecto_a_la_prima).jpg` | primo (respecto a la prima) | pucacje ndyiy | `LEXR-03544` |
| `diccionario_general/primo_con_prima.jpg` | primo con prima | pucacje pdyi’sh | `LEXR-02222` |
| `diccionario_general/primo_con_primo_o_prima_con_prima.jpg` | primo con primo o prima con prima | pucacje pyacj | `LEXR-01401` |
| `diccionario_general/primo,_prima.jpg` | primo, prima | primu | `LEXR-02006` |
| `diccionario_general/probar_(un_alimento),_sorber.jpg` | probar (un alimento), sorber | yajpe-, yape- | `LEXR-02734` |
| `diccionario_general/probar_(varias_veces).jpg` | probar (varias veces) | yapeepe- | `LEXR-03070` |
| `diccionario_general/procurar,_esforzarse,_afanarse.jpg` | procurar, esforzarse, afanarse | pa’pchu- | `LEXR-01669` |
| `diccionario_general/producir.jpg` | producir | pquĩiji- | `LEXR-03182` |
| `diccionario_general/prole,_cría.jpg` | prole, cría | ya’luch | `LEXR-03651` |
| `diccionario_general/propiciar.jpg` | propiciar | caapeewecha’j-, caapeewecha’ja- | `LEXR-01973` |
| `diccionario_general/propio_de_él.jpg` | propio de él | peecy jĩi | `LEXR-00814` |
| `diccionario_general/provocar,_atacar,_azuzar.jpg` | provocar, atacar, azuzar | cvis-, cvisu- | `LEXR-00406` |
| `diccionario_general/puente_arqueado.jpg` | puente arqueado | taty wej | `LEXR-01683` |
| `diccionario_general/puente_de_guadua.jpg` | puente de guadua | mum wej | `LEXR-03891` |
| `diccionario_general/puente_en_forma_de_arco.jpg` | puente en forma de arco | taty wej | `LEXR-01758` |
| `diccionario_general/puente_techado.jpg` | puente techado | wej yat | `LEXR-01339` |
| `diccionario_general/pues.jpg` | pues | -vacy (-va’cy) | `LEXR-02563` |
| `diccionario_general/pulga.jpg` | pulga | pã’pã | `LEXR-02763` |
| `diccionario_general/puma,_león.jpg` | puma, león | shĩ’j | `LEXR-03918` |
| `diccionario_general/punta_de_la_lengua.jpg` | punta de la lengua | tjune vits | `LEXR-00646` |
| `diccionario_general/purificarse.jpg` | purificarse | yaate-, yaatée | `LEXR-03751` |
| `diccionario_general/puñalarse.jpg` | puñalarse | iiyã’yãaja- | `LEXR-02748` |
| `diccionario_general/pájaro.jpg` | pájaro | vijcha | `LEXR-01336` |
| `diccionario_general/pálido.jpg` | pálido | chijme yuuni | `LEXR-03656` |
| `diccionario_general/párpado.jpg` | párpado | yafy cja’ty | `LEXR-02027` |
| `diccionario_general/que_alumbra_(por_ejemplo,_el_sol).jpg` | que alumbra (por ejemplo, el sol) | cweetjsa | `LEXR-01135` |
| `diccionario_general/que_ataja.jpg` | que ataja | yupsá | `LEXR-02641` |
| `diccionario_general/que_avisa,_que_anuncia.jpg` | que avisa, que anuncia | pta’shsa | `LEXR-03543` |
| `diccionario_general/que_barre.jpg` | que barre | pandsa | `LEXR-01394` |
| `diccionario_general/que_busca.jpg` | que busca | pacuesá | `LEXR-01153` |
| `diccionario_general/que_come,_comensal.jpg` | que come, comensal | ũ’sa | `LEXR-00479` |
| `diccionario_general/que_contesta.jpg` | que contesta | passa | `LEXR-01872` |
| `diccionario_general/que_da_paliza.jpg` | que da paliza | pecuesa | `LEXR-01804` |
| `diccionario_general/que_edifica.jpg` | que edifica | tyaasa | `LEXR-00458` |
| `diccionario_general/que_entra.jpg` | que entra | u’casa | `LEXR-01258` |
| `diccionario_general/que_ha_nacido.jpg` | que ha nacido | upysa | `LEXR-02020` |
| `diccionario_general/que_habla.jpg` | que habla | we’wesa | `LEXR-01567` |
| `diccionario_general/que_habla_con_desprecio.jpg` | que habla con desprecio | atsewe’wesa | `LEXR-03448` |
| `diccionario_general/que_hiere_(a_otro).jpg` | que hiere (a otro) | cpãvitsa | `LEXR-02260` |
| `diccionario_general/que_insulta.jpg` | que insulta | wẽeshusá | `LEXR-03036` |
| `diccionario_general/que_olvida.jpg` | que olvida | pechcanusa | `LEXR-00813` |
| `diccionario_general/que_pelea.jpg` | que pelea | puiisá | `LEXR-00821` |
| `diccionario_general/que_pide.jpg` | que pide | tjãassa | `LEXR-00834` |
| `diccionario_general/que_piensa,_confía.jpg` | que piensa, confía | yaacysa | `LEXR-02732` |
| `diccionario_general/que_presenta_queja,_demanda.jpg` | que presenta queja, demanda | yuwe ũssa | `LEXR-01633` |
| `diccionario_general/que_regala.jpg` | que regala | peessa | `LEXR-01472` |
| `diccionario_general/que_sana.jpg` | que sana | nuycatyjisa | `LEXR-03608` |
| `diccionario_general/que_tiene_misericordia,_que_ama.jpg` | que tiene misericordia, que ama | peeygãasa | `LEXR-03698` |
| `diccionario_general/que_toma.jpg` | que toma | tundysá | `LEXR-01824` |
| `diccionario_general/que_vende.jpg` | que vende | tyweysá | `LEXR-02864` |
| `diccionario_general/que_viene.jpg` | que viene | yuusá | `LEXR-01347` |
| `diccionario_general/que_vive,_ser_viviendo.jpg` | que vive, ser viviendo | fi’nzesa | `LEXR-02208` |
| `diccionario_general/que,_qué.jpg` | que,?qué? | quĩj | `LEXR-03754` |
| `diccionario_general/quebrar_(varias_cosas).jpg` | quebrar (varias cosas) | undund- | `LEXR-00658` |
| `diccionario_general/quebrar_(varios_huesos).jpg` | quebrar (varios huesos) | chcandende- | `LEXR-03534` |
| `diccionario_general/quebrar,_fracturar.jpg` | quebrar, fracturar | chcajnde-, chcande- | `LEXR-03102` |
| `diccionario_general/quebrar,_romper.jpg` | quebrar, romper | ujnd-, undu- | `LEXR-03766` |
| `diccionario_general/quebrarse_(varias_cosas).jpg` | quebrarse (varias cosas) | upeepe- | `LEXR-00659` |
| `diccionario_general/quedar_complacido.jpg` | quedar complacido | wechana neeyũu- | `LEXR-01764` |
| `diccionario_general/quedar_suspendido.jpg` | quedar suspendido | jytjẽeyũu- | `LEXR-01293` |
| `diccionario_general/quejarse_(enfermo).jpg` | quejarse (enfermo) | pembe’mbe- | `LEXR-01807` |
| `diccionario_general/quejarse,_gemir,_pujar.jpg` | quejarse, gemir, pujar | tũchj-, tũchjíi- | `LEXR-02865` |
| `diccionario_general/quemar.jpg` | quemar | camb-, cambu- | `LEXR-00392` |
| `diccionario_general/quemar_repetidas_veces.jpg` | quemar repetidas veces | cambuumbu-(cambu´mbu-) | `LEXR-00393` |
| `diccionario_general/querer,_amar,_gustar.jpg` | querer, amar, gustar | wendy-, wendyi- | `LEXR-03212` |
| `diccionario_general/querer,_desear.jpg` | querer, desear | wẽjẽ-, wẽe- | `LEXR-01892` |
| `diccionario_general/querido.jpg` | querido | wendyni | `LEXR-01098` |
| `diccionario_general/querido,_apreciable.jpg` | querido, apreciable | wendynisa | `LEXR-00843` |
| `diccionario_general/quiarse_ruana.jpg` | quiarse ruana | jycatsunde- | `LEXR-02960` |
| `diccionario_general/quiebramaíz.jpg` | quiebramaíz | cupytende- | `LEXR-03256` |
| `diccionario_general/quien,_quién.jpg` | quien, ?quién? | quim | `LEXR-00727` |
| `diccionario_general/quieto.jpg` | quieto | ẽsẽmée | `LEXR-03692` |
| `diccionario_general/quinto.jpg` | quinto | tajtstewe’sh | `LEXR-03749` |
| `diccionario_general/quitar_enjalma,_(fig)_desengañar.jpg` | quitar enjalma, (fig) desengañar | cjalma spajcy- | `LEXR-01910` |
| `diccionario_general/quitar_sombrero.jpg` | quitar sombrero | fĩicunde- | `LEXR-03912` |
| `diccionario_general/quitar_varias_cosas.jpg` | quitar varias cosas | pandende- | `LEXR-00626` |
| `diccionario_general/quitar,_despojar.jpg` | quitar, despojar | cusa’j-, cusa’ja- | `LEXR-01721` |
| `diccionario_general/quitar,_despojar_a_otro.jpg` | quitar, despojar a otro | ncuusa’j-, ncuusa’ja- | `LEXR-02665` |
| `diccionario_general/racimo_de_plátano.jpg` | racimo de plátano | pland pjapj | `LEXR-03293` |
| `diccionario_general/rajar,_partir_(con_hacha).jpg` | rajar, partir (con hacha) | pets-, petsjúu- (pẽts-) | `LEXR-02711` |
| `diccionario_general/rajarse_(en_varias_partes).jpg` | rajarse (en varias partes) | pjatete- | `LEXR-01544` |
| `diccionario_general/rajarse,_agrietarse.jpg` | rajarse, agrietarse | shish-, shishíi- | `LEXR-02996` |
| `diccionario_general/rajarse,_partirse.jpg` | rajarse, partirse | ujcha-, ucha- | `LEXR-00656` |
| `diccionario_general/ralo_(tejido).jpg` | ralo (tejido) | cash | `LEXR-00394` |
| `diccionario_general/rama_de_arbusto.jpg` | rama de arbusto | ẽjyã cu’ta | `LEXR-01187` |
| `diccionario_general/rama_de_árbol.jpg` | rama de árbol | fytũu cu’ta | `LEXR-03453` |
| `diccionario_general/rascar,_dar_raquiña,_comezón.jpg` | rascar, dar raquiña, comezón | yuuse’j-, yuuse’je- | `LEXR-03159` |
| `diccionario_general/rasgar,_romper_(varias_cosas).jpg` | rasgar, romper (varias cosas) | stendende- | `LEXR-00643` |
| `diccionario_general/rasguñar_(repetidas_veces).jpg` | rasguñar (repetidas veces) | pachi’ch- | `LEXR-02578` |
| `diccionario_general/rasguñar,_arañar,_coger_con_las_uñas.jpg` | rasguñar, arañar, coger con las uñas | pach-, pachíi- | `LEXR-00625` |
| `diccionario_general/raspar.jpg` | raspar | tupinde- | `LEXR-02401` |
| `diccionario_general/rata.jpg` | rata | unza wala | `LEXR-00464` |
| `diccionario_general/rata_grande_del_monte_(mamífero_roedor).jpg` | rata grande del monte (mamífero roedor) | ulu’j | `LEXR-01261` |
| `diccionario_general/ratón.jpg` | ratón | unza le’ch | `LEXR-00743` |
| `diccionario_general/raya.jpg` | raya | pend | `LEXR-01075` |
| `diccionario_general/rayado.jpg` | rayado | fi’j | `LEXR-01527` |
| `diccionario_general/rayar,_escribir_con_lápiz.jpg` | rayar, escribir con lápiz | suty-, sutyíi- (sũty-) | `LEXR-02826` |
| `diccionario_general/rayo.jpg` | rayo | ẽegatjẽ’j | `LEXR-00764` |
| `diccionario_general/raíz_de_cabuya.jpg` | raíz de cabuya | bats watse | `LEXR-03704` |
| `diccionario_general/raíz_de_la_lengua.jpg` | raíz de la lengua | tjune watse | `LEXR-01000` |
| `diccionario_general/raíz_del_diente.jpg` | raíz del diente | qui’tj watse | `LEXR-01938` |
| `diccionario_general/rebajar_(precio).jpg` | rebajar (precio) | nuycjẽj-, nuycjẽje- | `LEXR-01999` |
| `diccionario_general/rebosar.jpg` | rebosar | amby-, ambíi | `LEXR-00767` |
| `diccionario_general/rechazar,_burlar,_despreciar.jpg` | rechazar, burlar, despreciar | weech-, weechi- | `LEXR-03513` |
| `diccionario_general/recibir_fiado,_endeudarse.jpg` | recibir fiado, endeudarse | yulu-, yulúu- | `LEXR-00756` |
| `diccionario_general/reciente_(ej._oficiales_recientement_elegidos).jpg` | reciente (ej. oficiales recientement elegidos) | ãchwe’sh | `LEXR-01499` |
| `diccionario_general/reciente,_hace_poco.jpg` | reciente, hace poco | tyachmée | `LEXR-00459` |
| `diccionario_general/reclamar,_protestar.jpg` | reclamar, protestar | yuwe ũs- | `LEXR-03278` |
| `diccionario_general/reclinarse.jpg` | reclinarse | eenze- | `LEXR-00700` |
| `diccionario_general/recoger_(granos).jpg` | recoger (granos) | fiw-, fiwúu- | `LEXR-01215` |
| `diccionario_general/recoger,_cosechar.jpg` | recoger, cosechar | pcãash-, pcjacje- | `LEXR-02625` |
| `diccionario_general/reconciliar.jpg` | reconciliar | yuwewúu | `LEXR-02195` |
| `diccionario_general/recordado.jpg` | recordado | yaacynisa | `LEXR-03069` |
| `diccionario_general/recordar.jpg` | recordar | ũusutje- | `LEXR-00674` |
| `diccionario_general/recostarse.jpg` | recostarse | anzee- | `LEXR-00856` |
| `diccionario_general/recto,_directo.jpg` | recto, directo | sut | `LEXR-01166` |
| `diccionario_general/red_(para_atrapar_pájaros).jpg` | red (para atrapar pájaros) | tumb ucje | `LEXR-03272` |
| `diccionario_general/redondear.jpg` | redondear | jyandu’j-, jyandu’ju- | `LEXR-03199` |
| `diccionario_general/redondo.jpg` | redondo | jyand | `LEXR-02110` |
| `diccionario_general/reemplazar,_sustituir.jpg` | reemplazar, sustituir | pu’yacj-, pu’yacje- | `LEXR-02968` |
| `diccionario_general/reemplazo_(en_el_cargo).jpg` | reemplazo (en el cargo) | pu’yacjsa | `LEXR-02331` |
| `diccionario_general/reflejar,_centellear.jpg` | reflejar, centellear | cjicji’cji’j | `LEXR-00591` |
| `diccionario_general/regalado.jpg` | regalado | peesni | `LEXR-02053` |
| `diccionario_general/regalar.jpg` | regalar | pees-, peesu- | `LEXR-02580` |
| `diccionario_general/regalar_(varias_veces_or_a_varias_personas).jpg` | regalar (varias veces or a varias personas) | peesu’s-, peesu’su- | `LEXR-03263` |
| `diccionario_general/regar_(granos),_esparcir,_repartir.jpg` | regar (granos), esparcir, repartir | pũsh-, pũshi- | `LEXR-03716` |
| `diccionario_general/regar_(líquido).jpg` | regar (líquido) | yu’ caa- | `LEXR-02348` |
| `diccionario_general/regar_(repetidas_veces).jpg` | regar (repetidas veces) | pumbuumbu- | `LEXR-02629` |
| `diccionario_general/regarse,_desparramarse.jpg` | regarse, desparramarse | ũshi- | `LEXR-03161` |
| `diccionario_general/regañar,_censurar.jpg` | regañar, censurar | ĩcywe’we- | `LEXR-01576` |
| `diccionario_general/regañar,_reprender.jpg` | regañar, reprender | ĩcy-, ĩqui- | `LEXR-01432` |
| `diccionario_general/regaño.jpg` | regaño | ĩcywe’weni | `LEXR-01707` |
| `diccionario_general/regocijo,_felicidad.jpg` | regocijo, felicidad | wecha en | `LEXR-02685` |
| `diccionario_general/regresar,_volver.jpg` | regresar, volver | shavy-, shavíi- (chjavy-) | `LEXR-02586` |
| `diccionario_general/rehusar_dar_o_gastar_(repetidas_veces).jpg` | rehusar dar o gastar (repetidas veces) | peevisha’j-, peevisha’ja- | `LEXR-01608` |
| `diccionario_general/reir.jpg` | reir | shijca-, shica- | `LEXR-02634` |
| `diccionario_general/reir_(repetidas_veces).jpg` | reir (repetidas veces) | shica’ca- | `LEXR-00828` |
| `diccionario_general/reirse_con_los_que_se_ríen.jpg` | reirse con los que se ríen | paashijca-, paashica- | `LEXR-03714` |
| `diccionario_general/reirse_de.jpg` | reirse de | nshijca-, nshica- | `LEXR-01540` |
| `diccionario_general/relampaguear.jpg` | relampaguear | cpi’sh cwejne- | `LEXR-01282` |
| `diccionario_general/relinchar.jpg` | relinchar | jimba pembée- | `LEXR-00608` |
| `diccionario_general/remendar.jpg` | remendar | pa’cj-, pa’cje- (pã’cj- T) | `LEXR-00522` |
| `diccionario_general/remover,_suavizar.jpg` | remover, suavizar | waawa’j-, waawa’ja- | `LEXR-02868` |
| `diccionario_general/rencor,_resentimiento.jpg` | rencor, resentimiento | pyũuscue yaacyni | `LEXR-03822` |
| `diccionario_general/renovar.jpg` | renovar | pju’se’j-, pju’se’je- | `LEXR-01545` |
| `diccionario_general/renuente,_desinclinado.jpg` | renuente, desinclinado | wa’lsa | `LEXR-02684` |
| `diccionario_general/repartir.jpg` | repartir | tyu’tende- | `LEXR-02719` |
| `diccionario_general/repartir_(varias_cosas_entre_varias_personas).jpg` | repartir (varias cosas entre varias personas) | tyu’ndende- | `LEXR-03667` |
| `diccionario_general/repartir_(varias_cosas).jpg` | repartir (varias cosas) | jytyundende- | `LEXR-03234` |
| `diccionario_general/repartir,_distribuir_(varias_cosas,_o_a_varias_personas).jpg` | repartir, distribuir (varias cosas, o a varias personas) | tyundende- | `LEXR-02454` |
| `diccionario_general/repetidamente.jpg` | repetidamente | peena | `LEXR-02326` |
| `diccionario_general/repetir.jpg` | repetir | peena- | `LEXR-03790` |
| `diccionario_general/repetir_(varias_veces).jpg` | repetir (varias veces) | peenana- | `LEXR-03791` |
| `diccionario_general/resbalar.jpg` | resbalar | sla’tyi- | `LEXR-00641` |
| `diccionario_general/resbaloso.jpg` | resbaloso | sha’tyj (T) | `LEXR-02396` |
| `diccionario_general/resfriarse.jpg` | resfriarse | acj pa’j-, acj pa’ja- | `LEXR-02090` |
| `diccionario_general/respiración.jpg` | respiración | ũuseni | `LEXR-03218` |
| `diccionario_general/respirar,_volver_en_sí.jpg` | respirar, volver en sí | ũuse-, ũusée- | `LEXR-02413` |
| `diccionario_general/resplandecer.jpg` | resplandecer | zuntete- | `LEXR-03329` |
| `diccionario_general/resplandor,_fulgor.jpg` | resplandor, fulgor | zmeena’ | `LEXR-03279` |
| `diccionario_general/resucitar.jpg` | resucitar | ĩtyĩ vit- | `LEXR-03468` |
| `diccionario_general/retirarse,_retroceder.jpg` | retirarse, retroceder | ya’sca’j-, ya’sca’ja- | `LEXR-02871` |
| `diccionario_general/retorcer.jpg` | retorcer | me’m-, me’mu- | `LEXR-02490` |
| `diccionario_general/retorcer,_menear_la_cabeza_(en_señal_de_disgusto).jpg` | retorcer, menear la cabeza (en señal de disgusto) | tswendu’ndu- | `LEXR-03097` |
| `diccionario_general/retoñar,_brotar.jpg` | retoñar, brotar | buch-, bucha- | `LEXR-03494` |
| `diccionario_general/reumatismo_articular_(enfermedad_de_los_huesos).jpg` | reumatismo articular (enfermedad de los huesos) | lel | `LEXR-03381` |
| `diccionario_general/reunirse,_congregarse.jpg` | reunirse, congregarse | shambúu- | `LEXR-01818` |
| `diccionario_general/reunirse,_juntarse.jpg` | reunirse, juntarse | pcjaacje- | `LEXR-02216` |
| `diccionario_general/reunión.jpg` | reunión | pcjaacjeni | `LEXR-00525` |
| `diccionario_general/revelar,_mostrar.jpg` | revelar, mostrar | caavya´j-, caavya’ja- | `LEXR-00861` |
| `diccionario_general/revivir,_resucitar.jpg` | revivir, resucitar | ĩtyĩ yuu- | `LEXR-03038` |
| `diccionario_general/revolver,_menear.jpg` | revolver, menear | davy-, davíi- | `LEXR-03732` |
| `diccionario_general/rezar.jpg` | rezar | lisa-, lisáa- | `LEXR-03711` |
| `diccionario_general/rico.jpg` | rico | ji’pjsa | `LEXR-03820` |
| `diccionario_general/rincón_de_la_casa.jpg` | rincón de la casa | yat punza | `LEXR-01632` |
| `diccionario_general/risueño.jpg` | risueño | pshica | `LEXR-01244` |
| `diccionario_general/robado.jpg` | robado | peswení | `LEXR-00818` |
| `diccionario_general/robar.jpg` | robar | peswe-, peswée- | `LEXR-01678` |
| `diccionario_general/rociar.jpg` | rociar | pẽ’tsjutsj-, pẽ’tsjutsju- | `LEXR-01937` |
| `diccionario_general/rodar,_caer_dando_vueltas.jpg` | rodar, caer dando vueltas | pelu- | `LEXR-02436` |
| `diccionario_general/rodar,_revolcarse_(varias_veces).jpg` | rodar, revolcarse (varias veces) | peluulu- | `LEXR-02120` |
| `diccionario_general/rodear.jpg` | rodear | cyaandu- | `LEXR-01523` |
| `diccionario_general/rogar,_suplicar.jpg` | rogar, suplicar | fytjaa we’we- | `LEXR-03260` |
| `diccionario_general/rojo_claro.jpg` | rojo claro | bej atate | `LEXR-03846` |
| `diccionario_general/rollo.jpg` | rollo | tpand | `LEXR-03510` |
| `diccionario_general/romper.jpg` | romper | sunde’nde- | `LEXR-01820` |
| `diccionario_general/romper,_rasgar.jpg` | romper, rasgar | sunde- | `LEXR-03267` |
| `diccionario_general/romper,_rasgar_(una_sola_tira).jpg` | romper, rasgar (una sola tira) | shũ’wende- | `LEXR-02277` |
| `diccionario_general/romperse_(varias_veces).jpg` | romperse (varias veces) | sute’te- | `LEXR-03268` |
| `diccionario_general/romperse,_desgarrarse.jpg` | romperse, desgarrarse | shũ’wete- | `LEXR-02180` |
| `diccionario_general/roncar.jpg` | roncar | tjã’tj-, tjã’tja- | `LEXR-02679` |
| `diccionario_general/ronco.jpg` | ronco | pẽty apjani | `LEXR-00914` |
| `diccionario_general/rosado.jpg` | rosado | bejbej chijme | `LEXR-02416` |
| `diccionario_general/roza_de_choclo.jpg` | roza de choclo | tsut ej | `LEXR-03325` |
| `diccionario_general/rozar.jpg` | rozar | wats-, watsu- | `LEXR-01566` |
| `diccionario_general/roñoso,_áspero.jpg` | roñoso, áspero | shicshic | `LEXR-02822` |
| `diccionario_general/ruana_o_anaco_delgado.jpg` | ruana o anaco delgado | atyj pets | `LEXR-01584` |
| `diccionario_general/ruana_o_anaco_grueso.jpg` | ruana o anaco grueso | atyj chal | `LEXR-03555` |
| `diccionario_general/rucio.jpg` | rucio | lusiu | `LEXR-00611` |
| `diccionario_general/ruido.jpg` | ruido | susni | `LEXR-00832` |
| `diccionario_general/rumbo_a,_hacia_(recíproco).jpg` | rumbo a, hacia (recíproco) | ca’t, ca’tu, ca’tsuy | `LEXR-03694` |
| `diccionario_general/rápidamenta.jpg` | rápidamenta | dundte, dundtey | `LEXR-00599` |
| `diccionario_general/sabaleta.jpg` | sabaleta | cue quiwe wendy | `LEXR-01131` |
| `diccionario_general/sacar_(animales).jpg` | sacar (animales) | cashish- | `LEXR-02694` |
| `diccionario_general/sacar_(sin_permiso,_cosa_ajena).jpg` | sacar (sin permiso, cosa ajena) | ncuutyi’j-, ncuutyi’ji- | `LEXR-03408` |
| `diccionario_general/sacar_líquido,_servir_comida.jpg` | sacar líquido, servir comida | pa’cy-, pa’qui- | `LEXR-03205` |
| `diccionario_general/sacar_muesca.jpg` | sacar muesca | petyi’j-, petyi’ji- | `LEXR-02275` |
| `diccionario_general/sacristán.jpg` | sacristán | sangistan | `LEXR-03810` |
| `diccionario_general/sacudir.jpg` | sacudir | sajcu-, sacue- | `LEXR-02063` |
| `diccionario_general/sacudir_(repetidas_veces).jpg` | sacudir (repetidas veces) | sacueecue- | `LEXR-01815` |
| `diccionario_general/sacudirse.jpg` | sacudirse | jysaacuecue- | `LEXR-03201` |
| `diccionario_general/sal_de_zipaquirá.jpg` | sal de Zipaquirá | nenga reinu | `LEXR-01302` |
| `diccionario_general/salar,_echar_sal.jpg` | salar, echar sal | nenga’j- | `LEXR-03178` |
| `diccionario_general/salir_el_sol.jpg` | salir el sol | sec cãj- | `LEXR-03699` |
| `diccionario_general/salir_mazorca.jpg` | salir mazorca | sñula- (syuula-) | `LEXR-03390` |
| `diccionario_general/salir_sobre.jpg` | salir sobre | ãpy-, ãpi | `LEXR-01895` |
| `diccionario_general/saludar_(repetidas_veces).jpg` | saludar (repetidas veces) | wecha’cha- | `LEXR-03126` |
| `diccionario_general/salvar.jpg` | Salvar | ewte nvijt- | `LEXR-03083` |
| `diccionario_general/salvia_(planta_medicinal).jpg` | salvia (planta medicinal) | jyutcjamb | `LEXR-03745` |
| `diccionario_general/sanar.jpg` | sanar | nuycatyji- | `LEXR-01232` |
| `diccionario_general/sanarse.jpg` | sanarse | ĩiwẽet-ĩiwẽetúu- | `LEXR-03217` |
| `diccionario_general/sangrar.jpg` | sangrar | yaach-, yaachji- | `LEXR-02687` |
| `diccionario_general/sangre.jpg` | sangre | ee | `LEXR-01140` |
| `diccionario_general/savia.jpg` | savia | fytũu yu’ | `LEXR-02531` |
| `diccionario_general/seca_(infarto_de_una_glándula).jpg` | seca (infarto de una glándula) | sha’lul | `LEXR-02229` |
| `diccionario_general/secar.jpg` | secar | andy-, andyi- | `LEXR-02294` |
| `diccionario_general/seco.jpg` | seco | ujndy | `LEXR-00559` |
| `diccionario_general/secretamente,_en_secreto.jpg` | secretamente, en secreto | paatste | `LEXR-01671` |
| `diccionario_general/sediento,_que_tiene_sed.jpg` | sediento, que tiene sed | yũ’wẽesa | `LEXR-02410` |
| `diccionario_general/seguir.jpg` | seguir | e’ste u’j-, e’ste yuj- | `LEXR-01288` |
| `diccionario_general/seguir_rastro,_oler.jpg` | seguir rastro, oler | imu’s-imu’su- | `LEXR-00971` |
| `diccionario_general/seguir,_continuar_haciendo_algo.jpg` | seguir, continuar haciendo algo | u’j-, u’jue- | `LEXR-01887` |
| `diccionario_general/seis.jpg` | seis | teesacy | `LEXR-03717` |
| `diccionario_general/sembrado.jpg` | sembrado | uujni | `LEXR-02456` |
| `diccionario_general/sembrado_de_maní.jpg` | sembrado de maní | quitj ej | `LEXR-01482` |
| `diccionario_general/sembrador,_que_siembra.jpg` | sembrador, que siembra | uujsa | `LEXR-01423` |
| `diccionario_general/sembrar.jpg` | sembrar | uj-, uja- | `LEXR-02720` |
| `diccionario_general/sembrar_(diversas_semillas).jpg` | sembrar (diversas semillas) | uja’ja- | `LEXR-01627` |
| `diccionario_general/sentarse.jpg` | sentarse | pish’-, pishi- (C) | `LEXR-02672` |
| `diccionario_general/sentir_'señas',_adivinar_por_sensaciones_en_el_cuerpo.jpg` | sentir ’señas’, adivinar por sensaciones en el cuerpo | jyta’ñi- | `LEXR-01533` |
| `diccionario_general/sentir_(cuando_otro_la_toca).jpg` | sentir (cuando otro la toca) | ye’tsje- | `LEXR-03652` |
| `diccionario_general/sentir_calor,_acalorarse.jpg` | sentir calor, acalorarse | yaacha-, yaacháa- | `LEXR-02245` |
| `diccionario_general/sentir_cosquillas.jpg` | sentir cosquillas | yeele-, yeelée- | `LEXR-02246` |
| `diccionario_general/sentir_dolor.jpg` | sentir dolor | yaaca-, yaacáa | `LEXR-01270` |
| `diccionario_general/sentir_frío.jpg` | sentir frío | yeetse-, yeetsée- | `LEXR-02458` |
| `diccionario_general/sentir_pesar.jpg` | sentir pesar | pytjaa yajcy- | `LEXR-03238` |
| `diccionario_general/sentir_una_sensacíon_extraña.jpg` | sentir una sensacíon extraña | fiityu’yu- | `LEXR-02699` |
| `diccionario_general/sentirse_bien,_estar_alentado.jpg` | sentirse bien, estar alentado | wẽt ũs-, wẽt u’p- | `LEXR-02080` |
| `diccionario_general/sentirse_incapaz.jpg` | sentirse incapaz | shiing-, shiingúu- | `LEXR-03594` |
| `diccionario_general/separar,_repartir,_dividir,_apartar.jpg` | separar, repartir, dividir, apartar | tyujnde-, tyunde- | `LEXR-01333` |
| `diccionario_general/separarse_(varias_cosas,_o_varias_personas).jpg` | separarse (varias cosas, o varias personas) | tyute’te- | `LEXR-03244` |
| `diccionario_general/separarse,_alejarse,_apartarse.jpg` | separarse, alejarse, apartarse | tyute-, tyutẽe- | `LEXR-00461` |
| `diccionario_general/sepulcro,_fosa_pars_entierro.jpg` | sepulcro, fosa pars entierro | pendani cafy | `LEXR-01240` |
| `diccionario_general/sepultado.jpg` | sepultado | pendaní | `LEXR-02626` |
| `diccionario_general/ser.jpg` | ser | yuu- | `LEXR-01346` |
| `diccionario_general/ser_agredido.jpg` | ser agredido | ya’ptjãawe- | `LEXR-00471` |
| `diccionario_general/ser_amado,_quererse_recíprocamente.jpg` | ser amado, quererse recíprocamente | iiwejndy-, iiweendyi- | `LEXR-00606` |
| `diccionario_general/ser_amigos,_tener_amistad.jpg` | ser amigos, tener amistad | namicu yuu- | `LEXR-03024` |
| `diccionario_general/ser_bautizado.jpg` | ser bautizado | ya’bautisaĩ- | `LEXR-02244` |
| `diccionario_general/ser_burlado.jpg` | ser burlado | ya’iweech- | `LEXR-01341` |
| `diccionario_general/ser_castigado.jpg` | ser castigado | ya’castigaĩ- | `LEXR-03214` |
| `diccionario_general/ser_condenado.jpg` | ser condenado | ewmeete neeyũu- | `LEXR-03017` |
| `diccionario_general/ser_dejado,_quedarse_involuntariamente.jpg` | ser dejado, quedarse involuntariamente | ya’neeyũu- | `LEXR-02904` |
| `diccionario_general/ser_despreciado.jpg` | ser despreciado | yaatse- | `LEXR-01893` |
| `diccionario_general/ser_esquivo,_esquivar.jpg` | ser esquivo, esquivar | jamby-, jambíi- | `LEXR-01223` |
| `diccionario_general/ser_lavado.jpg` | ser lavado | ya’pcji’cj- | `LEXR-02026` |
| `diccionario_general/ser_madrina.jpg` | ser madrina | neenjĩ’j yuju- | `LEXR-02791` |
| `diccionario_general/ser_mezquino.jpg` | ser mezquino | sendy-, sendyi- | `LEXR-00450` |
| `diccionario_general/ser_nombrado.jpg` | ser nombrado | ya’cysus-, ya’cysusu- | `LEXR-01571` |
| `diccionario_general/ser_olvidadizo.jpg` | ser olvidadizo | paapechcanu- | `LEXR-02002` |
| `diccionario_general/ser_padrinos_(de_matrimonio).jpg` | ser padrinos (de matrimonio) | cpu’nze’j-, cpu’nze’je | `LEXR-00693` |
| `diccionario_general/ser_quitado,_dejarse_quitar.jpg` | ser quitado, dejarse quitar | jycuusa’j-, jycuusa’ja- | `LEXR-00710` |
| `diccionario_general/ser_salvo.jpg` | ser salvo | ewte neeyũu- | `LEXR-02698` |
| `diccionario_general/ser_sobrenatural.jpg` | ser sobrenatural | vitywe’sh | `LEXR-02140` |
| `diccionario_general/ser,_llegar_a_ser.jpg` | ser, llegar a ser | yuu- | `LEXR-01771` |
| `diccionario_general/serranía.jpg` | serranía | vitssu | `LEXR-01265` |
| `diccionario_general/servible,_usado_(de_segunda_mano).jpg` | servible, usado (de segunda mano) | iijyũnisa | `LEXR-01144` |
| `diccionario_general/servir,_ser_útil.jpg` | servir, ser útil | selpíi- | `LEXR-03613` |
| `diccionario_general/servirse_(mutuamente).jpg` | servirse (mutuamente) | puuty ya’selpii- | `LEXR-02224` |
| `diccionario_general/severamente.jpg` | severamente | juuna’ | `LEXR-02786` |
| `diccionario_general/severo,_temible.jpg` | severo, temible | juuna’sa | `LEXR-03477` |
| `diccionario_general/siempre,_realmente_(con_seguridad).jpg` | siempre, realmente (con seguridad) | pejca | `LEXR-01239` |
| `diccionario_general/siete.jpg` | siete | siete | `LEXR-01881` |
| `diccionario_general/silbar.jpg` | silbar | fyu’fy-, fyu’fi- | `LEXR-01727` |
| `diccionario_general/silbar_(repetidas_veces).jpg` | silbar (repetidas veces) | fyu’fyu’ju- | `LEXR-02266` |
| `diccionario_general/simple,_soso.jpg` | simple, soso | shũu | `LEXR-00539` |
| `diccionario_general/sin_embargo.jpg` | sin embargo | naasá | `LEXR-02273` |
| `diccionario_general/sin_miedo.jpg` | sin miedo | ũucjmée | `LEXR-01354` |
| `diccionario_general/sitio_anterior_de_la_casa.jpg` | sitio anterior de la casa | yat fynũ | `LEXR-03922` |
| `diccionario_general/sobar,_acarciciar_(varias_veces).jpg` | sobar, acarciciar (varias veces) | sũcja’cja- | `LEXR-02827` |
| `diccionario_general/sobar,_componer_un_hueso_dislocado.jpg` | sobar, componer un hueso dislocado | sũcj-, sũcjáa- | `LEXR-03062` |
| `diccionario_general/sobra.jpg` | sobra | pe’ya | `LEXR-01746` |
| `diccionario_general/sobra,_sobrante.jpg` | sobra, sobrante | quijya, quijyasá | `LEXR-02441` |
| `diccionario_general/sobrar.jpg` | sobrar | tjaacue- | `LEXR-00734` |
| `diccionario_general/sobrino_o_sobrina_con_el_tío.jpg` | sobrino o sobrina con el tío | pcaaca | `LEXR-00724` |
| `diccionario_general/sobrino_o_sobrina_con_tía.jpg` | sobrino o sobrina con tía | ptsuuts | `LEXR-03362` |
| `diccionario_general/soledad.jpg` | soledad | pleecu’c | `LEXR-03592` |
| `diccionario_general/soledad_(ave).jpg` | soledad (ave) | pleecu’c | `LEXR-01932` |
| `diccionario_general/sollozar.jpg` | sollozar | jetu’t-, jetu’tu- | `LEXR-03435` |
| `diccionario_general/soltar,_desatar.jpg` | soltar, desatar | tywete-, tyewetée- | `LEXR-03393` |
| `diccionario_general/soltera.jpg` | soltera | nmi’ ji’pjmeesa | `LEXR-01066` |
| `diccionario_general/soltero.jpg` | soltero | nyu ji’pjmeesa | `LEXR-02854` |
| `diccionario_general/sombrero_de_hoja_de_caña.jpg` | sombrero de hoja de caña | cjĩij chwa’ | `LEXR-02423` |
| `diccionario_general/sombrero_de_ramos.jpg` | sombrero de ramos | chũpy chwa’ | `LEXR-03876` |
| `diccionario_general/sonar.jpg` | sonar | tsñiñi- | `LEXR-03270` |
| `diccionario_general/sonar_(ruido_de_cascabel).jpg` | sonar (ruido de cascabel) | sda’nda- | `LEXR-02227` |
| `diccionario_general/sonar,_hacer_ruido_(maraca).jpg` | sonar, hacer ruido (maraca) | shajshaj- | `LEXR-02632` |
| `diccionario_general/sonarse_las_narices.jpg` | sonarse las narices | pĩitsj-, pĩitsjúu- | `LEXR-02716` |
| `diccionario_general/sonreir.jpg` | sonreir | anzu- | `LEXR-01775` |
| `diccionario_general/sonrojarse.jpg` | sonrojarse | beecãj-, beecãja- | `LEXR-01440` |
| `diccionario_general/sonsacar.jpg` | sonsacar | yu’tya- | `LEXR-01181` |
| `diccionario_general/soplar.jpg` | soplar | putj-, putjáa- | `LEXR-02493` |
| `diccionario_general/soplar_(repetidas_veces).jpg` | soplar (repetidas veces) | putja’tj-, putja’tja- | `LEXR-02276` |
| `diccionario_general/soplar_la_candela.jpg` | soplar la candela | yutj-, yutjáa- | `LEXR-03420` |
| `diccionario_general/sordo.jpg` | sordo | tjũ’we puuple | `LEXR-03031` |
| `diccionario_general/sorpresivamente,_súbitamente.jpg` | sorpresivamente, súbitamente | yaacynimeete | `LEXR-01766` |
| `diccionario_general/soñar.jpg` | soñar | csha’w-, csha’wu- | `LEXR-00400` |
| `diccionario_general/su.jpg` | su | i’cue’sh | `LEXR-01791` |
| `diccionario_general/su_(de_ellos,_de_ellas).jpg` | su (de ellos, de ellas) | tyãawe’sh (cyãawe’sh) | `LEXR-00462` |
| `diccionario_general/su_(de_él,_de_ella).jpg` | su (de él, de ella) | tyajy (cyajy) | `LEXR-01257` |
| `diccionario_general/subir.jpg` | subir | iictejca- | `LEXR-00792` |
| `diccionario_general/subir_(ej._ladrillos).jpg` | subir (ej. ladrillos) | nuytejca- | `LEXR-01744` |
| `diccionario_general/subir,_ascender,_trepar.jpg` | subir, ascender, trepar | tejca-, teeca- | `LEXR-01488` |
| `diccionario_general/suegro_o_suegra_con_el_yerno.jpg` | suegro o suegra con el yerno | pduj | `LEXR-03906` |
| `diccionario_general/suelto.jpg` | suelto | tyweteni | `LEXR-01006` |
| `diccionario_general/sueño.jpg` | sueño | deewẽeni | `LEXR-01377` |
| `diccionario_general/suficiente,_complete.jpg` | suficiente, complete | ãj | `LEXR-03578` |
| `diccionario_general/sufir_castigo.jpg` | sufir castigo | castigo cnay- | `LEXR-01034` |
| `diccionario_general/sufrir.jpg` | sufrir | pytjaa yuu- | `LEXR-03295` |
| `diccionario_general/sufrir_dolor.jpg` | sufrir dolor | aca cnay- | `LEXR-03425` |
| `diccionario_general/suicidarse.jpg` | suicidarse | ya’icj-, ya’icje- | `LEXR-00934` |
| `diccionario_general/supurar.jpg` | supurar | tucja-, tucjáa- | `LEXR-01622` |
| `diccionario_general/suspirar.jpg` | suspirar | ũusdyi’-, ũusdyi’i- | `LEXR-03162` |
| `diccionario_general/suyo.jpg` | suyo | i’cue’sh | `LEXR-01457` |
| `diccionario_general/tabaco_(planta).jpg` | tabaco (planta) | wãjy (wẽjy) | `LEXR-02730` |
| `diccionario_general/tabla.jpg` | tabla | tapla | `LEXR-02131` |
| `diccionario_general/tamal_de_choclo.jpg` | tamal de choclo | tsut pullu | `LEXR-02451` |
| `diccionario_general/tamaño,_dimensión_de_altura,_anchura,_profundidad.jpg` | tamaño, dimensión de altura, anchura, profundidad | tyacjue, tyacjuey | `LEXR-03348` |
| `diccionario_general/tambalear.jpg` | tambalear | wãca’ca- | `LEXR-01494` |
| `diccionario_general/tambalearse.jpg` | tambalearse | tjuja’ja- | `LEXR-02183` |
| `diccionario_general/también.jpg` | también | -va | `LEXR-02979` |
| `diccionario_general/tan,_tanto_(de_este_tamaño_o_cantidad).jpg` | tan, tanto (de este tamaño o cantidad) | nacue | `LEXR-01230` |
| `diccionario_general/tantos.jpg` | tantos | cyãanz | `LEXR-03836` |
| `diccionario_general/taparse.jpg` | taparse | ya’pa’ch- (ya’pã’ch-) | `LEXR-02187` |
| `diccionario_general/taparse_el_rostro.jpg` | taparse el rostro | yaapj-, yaapjáa | `LEXR-03814` |
| `diccionario_general/tarro_de_guadua.jpg` | tarro de guadua | mum tuca | `LEXR-03625` |
| `diccionario_general/tasajear_(carne).jpg` | tasajear (carne) | yuja’j-, yuja’ja- | `LEXR-02509` |
| `diccionario_general/techo_de_la_casa.jpg` | techo de la casa | yat cajcue (yat cuejcue) | `LEXR-01697` |
| `diccionario_general/tejedor,_que_teje.jpg` | tejedor, que teje | umsá | `LEXR-02345` |
| `diccionario_general/tejido.jpg` | tejido | umnisa | `LEXR-00561` |
| `diccionario_general/tejido_trenzado.jpg` | tejido trenzado | calli | `LEXR-03875` |
| `diccionario_general/telar_para_tejer_chumbe.jpg` | telar para tejer chumbe | taw tel | `LEXR-02894` |
| `diccionario_general/telar_para_tejer_ruana.jpg` | telar para tejer ruana | atyj tel | `LEXR-02150` |
| `diccionario_general/temblar_(de_miedo,_o_del_frío).jpg` | temblar (de miedo, o del frío) | yaya-, yayáa- | `LEXR-01019` |
| `diccionario_general/temblar_(movimiento_telúrico).jpg` | temblar (movimiento telúrico) | quiwe ẽsẽ-, quiwe u’j- | `LEXR-02969` |
| `diccionario_general/temer,_tener_miedo,_asustarse.jpg` | temer, tener miedo, asustarse | ũucj-, ũucju- | `LEXR-00673` |
| `diccionario_general/temible.jpg` | temible | ũujũucjsa | `LEXR-01436` |
| `diccionario_general/templar.jpg` | templar | spajnde-, spande- | `LEXR-03415` |
| `diccionario_general/templar_(varias_cuerdas).jpg` | templar (varias cuerdas) | spandende- | `LEXR-01941` |
| `diccionario_general/temprano.jpg` | temprano | ẽeíi | `LEXR-01839` |
| `diccionario_general/tender.jpg` | tender | tende- | `LEXR-03487` |
| `diccionario_general/tender,_extender.jpg` | tender, extender | pume-, pumée- | `LEXR-00530` |
| `diccionario_general/tendido,_sudadero.jpg` | tendido, sudadero | pusni | `LEXR-01752` |
| `diccionario_general/tendón_de_la_mano.jpg` | tendón de la mano | cuse watse | `LEXR-03257` |
| `diccionario_general/tendón_de_la_pie.jpg` | tendón de la pie | chinda watse | `LEXR-01039` |
| `diccionario_general/tener_'sensaciones'_en_el_cuerpo.jpg` | tener ’sensaciones’ en el cuerpo | ñeese- | `LEXR-01182` |
| `diccionario_general/tener_celos_(entre_esposos).jpg` | tener celos (entre esposos) | pyãj-, pyãja- | `LEXR-01160` |
| `diccionario_general/tener_celos,_estar_celoso.jpg` | tener celos, estar celoso | iipyãj-,iipyãja-, iipyãa- | `LEXR-00793` |
| `diccionario_general/tener_cuidado.jpg` | tener cuidado | jypa’yajcy-jypa’yaqui | `LEXR-00513` |
| `diccionario_general/tener_dificultades.jpg` | tener dificultades | tjẽyte ñuste fi’nze- | `LEXR-01091` |
| `diccionario_general/tener_hambre.jpg` | tener hambre | wẽjẽ-, wẽe- | `LEXR-03213` |
| `diccionario_general/tener_hipo.jpg` | tener hipo | e’shi-, e’shi’ji- | `LEXR-01987` |
| `diccionario_general/tener_miedo.jpg` | tener miedo | iiũucj- | `LEXR-03697` |
| `diccionario_general/tener_sed.jpg` | tener sed | ñu’wẽ- (yũ’wẽ-) | `LEXR-02643` |
| `diccionario_general/tener_sesaciones_(sentir_'señas').jpg` | tener sesaciones (sentir ’señas’) | ta’ñi- | `LEXR-03416` |
| `diccionario_general/tener_sueño.jpg` | tener sueño | deewẽe- | `LEXR-00963` |
| `diccionario_general/tener_vergüenza.jpg` | tener vergüenza | tjame- | `LEXR-03805` |
| `diccionario_general/tener,_poseer,_contener.jpg` | tener, poseer, contener | ji’pj-, ji’pju- | `LEXR-01991` |
| `diccionario_general/tercero.jpg` | tercero | tecjtewe’sh | `LEXR-02677` |
| `diccionario_general/terciado.jpg` | terciado | jypunzani | `LEXR-00514` |
| `diccionario_general/terciar,_llevar_terciado.jpg` | terciar, llevar terciado | jypujnza-, jypuunza- | `LEXR-01458` |
| `diccionario_general/terminar_(poner_fin_a_un_asunto_o_a_una_reunión).jpg` | terminar (poner fin a un asunto o a una reunión) | caaptsu’ju’j-, caaptsu’ju’ju- | `LEXR-01276` |
| `diccionario_general/terminar_un_asunto.jpg` | terminar un asunto | yuwe ptsuu- | `LEXR-01574` |
| `diccionario_general/terrible,_horrible.jpg` | terrible, horrible | seena’ | `LEXR-02890` |
| `diccionario_general/terrón.jpg` | terrón | quiwe cuet | `LEXR-03318` |
| `diccionario_general/teñir_de_negro.jpg` | teñir de negro | cjũchacj-, cjũchacje- | `LEXR-03831` |
| `diccionario_general/tibia.jpg` | tibia | wajwa | `LEXR-00748` |
| `diccionario_general/tiempos_anteriores.jpg` | tiempos anteriores | maantey | `LEXR-01919` |
| `diccionario_general/tierno,_recíen_nacido.jpg` | tierno, recíen nacido | ãpã, ãpãcuẽ | `LEXR-02196` |
| `diccionario_general/tierra_caliente.jpg` | tierra caliente | acha quiwe | `LEXR-01190` |
| `diccionario_general/tierra_fría.jpg` | tierra fría | finze quiwe | `LEXR-03048` |
| `diccionario_general/tierra_lejana.jpg` | tierra lejana | jyu’j quiwe | `LEXR-03587` |
| `diccionario_general/tieso.jpg` | tieso | we’ll | `LEXR-01829` |
| `diccionario_general/tigrillo.jpg` | tigrillo | tyiclli | `LEXR-01561` |
| `diccionario_general/tijereta.jpg` | tijereta | uschi’ | `LEXR-02288` |
| `diccionario_general/timidez.jpg` | timidez | paaũcjweete | `LEXR-00624` |
| `diccionario_general/tirante_(pieza_de_la_armadura_del_tejado).jpg` | tirante (pieza de la armadura del tejado) | catj | `LEXR-00864` |
| `diccionario_general/tocar_(con_la_mano),_palpar.jpg` | tocar (con la mano), palpar | jya’ndy-, jya’ndyi- | `LEXR-03140` |
| `diccionario_general/tocar_(la_puerta).jpg` | tocar (la puerta) | tu’ca- | `LEXR-02504` |
| `diccionario_general/tocar_(repetidas_veces).jpg` | tocar (repetidas veces) | jya’ndyi’ndyi- | `LEXR-00707` |
| `diccionario_general/tocar_(un_instrumento_musical).jpg` | tocar (un instrumento musical) | tujca-, tuca- | `LEXR-03526` |
| `diccionario_general/tocar_flauta.jpg` | tocar flauta | cuvy-, cuvíi- | `LEXR-01208` |
| `diccionario_general/tocar_repetidas_veces_con_algo.jpg` | tocar repetidas veces con algo | cuutsje’je’j-, cuutsje’je’je- | `LEXR-00499` |
| `diccionario_general/tocar,_echar_mano.jpg` | tocar, echar mano | utsje-, utsjée- | `LEXR-02021` |
| `diccionario_general/toda_la_noche.jpg` | toda la noche | tee cus uta | `LEXR-03364` |
| `diccionario_general/todavía.jpg` | todavía | nee | `LEXR-03606` |
| `diccionario_general/todavía_obscuro_(en_la_madrugada).jpg` | todavía obscuro (en la madrugada) | chji’ndytey | `LEXR-03284` |
| `diccionario_general/todo.jpg` | todo | jyuca, jyucáy | `LEXR-00799` |
| `diccionario_general/todos.jpg` | todos | jyucaysa, jyucasay | `LEXR-01296` |
| `diccionario_general/tomar_preso,_aprisionar.jpg` | tomar preso, aprisionar | preesu’ji-, preesu’ju- | `LEXR-01613` |
| `diccionario_general/torcaz.jpg` | torcaz | cujtyil | `LEXR-00695` |
| `diccionario_general/torcaz_(ave).jpg` | torcaz (ave) | tumb | `LEXR-01883` |
| `diccionario_general/torcaz_del_monte_(ave).jpg` | torcaz del monte (ave) | yu’cj tumb | `LEXR-00665` |
| `diccionario_general/torcaz_domesticado.jpg` | torcaz domesticado | taqui’ni tumb | `LEXR-00453` |
| `diccionario_general/torcaz_pequeña_(ave).jpg` | torcaz pequeña (ave) | chĩ’ch | `LEXR-00494` |
| `diccionario_general/torcaz_silvestre.jpg` | torcaz silvestre | yu’cj tumb | `LEXR-00473` |
| `diccionario_general/torcer.jpg` | torcer | tspund-, tspundúu- | `LEXR-02073` |
| `diccionario_general/torcer_(hilo_o_guasca).jpg` | torcer (hilo o guasca) | spund-, spundúu- | `LEXR-00542` |
| `diccionario_general/torcer,_retorcer.jpg` | torcer, retorcer | tswend-, tswendúu- | `LEXR-00550` |
| `diccionario_general/torcerse,_encorvarse.jpg` | torcerse, encorvarse | ta’tsu- | `LEXR-02233` |
| `diccionario_general/torcido.jpg` | torcido | ta’ts, ta’tscue | `LEXR-03242` |
| `diccionario_general/tormenta,_tempestad.jpg` | tormenta, tempestad | nus wejya dyi’j | `LEXR-02819` |
| `diccionario_general/toser.jpg` | toser | pjãjã- | `LEXR-03591` |
| `diccionario_general/toser_(repetidas_veces).jpg` | toser (repetidas veces) | pjãjã’jã- | `LEXR-01078` |
| `diccionario_general/trabajar.jpg` | trabajar | mjĩi- | `LEXR-02114` |
| `diccionario_general/traer.jpg` | traer | neejyũj- | `LEXR-03055` |
| `diccionario_general/traer_(a_través).jpg` | traer (a través) | muypesa- | `LEXR-00894` |
| `diccionario_general/traer_(desde_abajo).jpg` | traer (desde abajo) | nuycãj-, nuycãja- | `LEXR-03609` |
| `diccionario_general/traer_(desde_arriba),_bajar_(ej._a_un_enfermo).jpg` | traer (desde arriba), bajar (ej. a un enfermo) | nuyquĩj-, nuyquĩji- | `LEXR-03626` |
| `diccionario_general/traer_(desde_arriba,_en_plano).jpg` | traer (desde arriba, en plano) | nuysẽj-, nuysẽje- | `LEXR-01069` |
| `diccionario_general/traer_(llegando_a_un_lugar).jpg` | traer (llegando a un lugar) | nuycũj-, nuycũju- | `LEXR-00619` |
| `diccionario_general/traer,_cargar.jpg` | traer, cargar | nicy-, niqui- | `LEXR-01539` |
| `diccionario_general/traer,_hacer_llegar.jpg` | traer, hacer llegar | nuypa’j-, nuypa’ja- | `LEXR-03179` |
| `diccionario_general/tragar.jpg` | tragar | jycjẽe- | `LEXR-03141` |
| `diccionario_general/trama,_hilo_horizontal_del_telar.jpg` | trama, hilo horizontal del telar | pacjẽ | `LEXR-01072` |
| `diccionario_general/tranca.jpg` | tranca | atjni | `LEXR-02777` |
| `diccionario_general/transnochar.jpg` | transnochar | dejmée pe’te- | `LEXR-03500` |
| `diccionario_general/transparente,_claro.jpg` | transparente, claro | sneene | `LEXR-02181` |
| `diccionario_general/trapiche_movido_por_bestia.jpg` | trapiche movido por bestia | jimba tlaapichi | `LEXR-02046` |
| `diccionario_general/trasladar,_transtear.jpg` | trasladar, transtear | peefynicy-, peefyniqui- | `LEXR-00526` |
| `diccionario_general/trastear,_mudarse.jpg` | trastear, mudarse | npeefynicy-, npeeefyniqui- | `LEXR-02274` |
| `diccionario_general/tratar_con_severidad.jpg` | tratar con severidad | juuna’ yuu | `LEXR-01732` |
| `diccionario_general/tratarse_como_parientes.jpg` | tratarse como parientes | nwe’sh we’we- | `LEXR-01927` |
| `diccionario_general/trenza.jpg` | trenza | ca’jem (ca’jyam) | `LEXR-00584` |
| `diccionario_general/trenzar.jpg` | trenzar | tsũ’ta’j-, tsũ’ta’ja- | `LEXR-00551` |
| `diccionario_general/tres.jpg` | tres | tecj | `LEXR-00546` |
| `diccionario_general/triste.jpg` | triste | ñus (yũs) | `LEXR-01705` |
| `diccionario_general/tronar.jpg` | tronar | cpi’sh we’we- | `LEXR-01784` |
| `diccionario_general/tropezar.jpg` | tropezar | yu’chavy-, yu’chavi- | `LEXR-02597` |
| `diccionario_general/tu_(niña_o_pariente_fememina).jpg` | tu (niña o pariente fememina) | icha | `LEXR-03434` |
| `diccionario_general/tu,_su,_de_usted.jpg` | tu, su, de usted | i’cue | `LEXR-03454` |
| `diccionario_general/tu,_su,_de_usted_(masculino).jpg` | tu, su, de usted (masculino) | indy (iindy, ingy) | `LEXR-00703` |
| `diccionario_general/tusa_de_maíz.jpg` | tusa de maíz | cutyj tymi | `LEXR-03401` |
| `diccionario_general/tusilla_(planta).jpg` | tusilla (planta) | shande | `LEXR-03522` |
| `diccionario_general/tábano.jpg` | tábano | jimba apj | `LEXR-01291` |
| `diccionario_general/tábano_(insecto).jpg` | tábano (insecto) | jimba apj | `LEXR-00795` |
| `diccionario_general/tía_(hermana_de_la_mamá).jpg` | tía (hermana de la mamá) | peeyũcue | `LEXR-00440` |
| `diccionario_general/tía_con_sobrino_o_sobrina.jpg` | tía con sobrino o sobrina | pnjĩ’yacue | `LEXR-01933` |
| `diccionario_general/tímido,_temeroso,_miedoso.jpg` | tímido, temeroso, miedoso | paaũucjsa | `LEXR-01469` |
| `diccionario_general/tú_(niña_o_pariente_femenina).jpg` | tú (niña o pariente femenina) | ijcha | `LEXR-02785` |
| `diccionario_general/tú,_usted_(masculino).jpg` | tú, usted (masculino) | indy (ingy) | `LEXR-01915` |
| `diccionario_general/ulluco.jpg` | ulluco | shwi’la | `LEXR-00920` |
| `diccionario_general/ultrajar.jpg` | ultrajar | pcyuuwe’we- | `LEXR-03518` |
| `diccionario_general/ultraje.jpg` | ultraje | pcyuuwe’weni | `LEXR-02118` |
| `diccionario_general/un_ratico.jpg` | un ratico | le’chle’ch | `LEXR-03838` |
| `diccionario_general/un_rato.jpg` | un rato | le’chcuẽ | `LEXR-02489` |
| `diccionario_general/una_brazada.jpg` | una brazada | tee cu’ta | `LEXR-00547` |
| `diccionario_general/una_persona_vestida.jpg` | una persona vestida | jyaatjsa | `LEXR-03021` |
| `diccionario_general/unidos.jpg` | unidos | cyterraj | `LEXR-00501` |
| `diccionario_general/unir.jpg` | unir | yuutya- | `LEXR-01498` |
| `diccionario_general/unirse,_juntarse_con.jpg` | unirse, juntarse con | peecjacje- | `LEXR-02965` |
| `diccionario_general/uno.jpg` | uno | teech | `LEXR-01416` |
| `diccionario_general/uno_por_uno.jpg` | uno por uno | teech teech | `LEXR-02235` |
| `diccionario_general/uno_tras_otro.jpg` | uno tras otro | vitvite | `LEXR-03247` |
| `diccionario_general/unos_cuantos.jpg` | unos cuantos | nanz, nanzcuẽ | `LEXR-02663` |
| `diccionario_general/unos_pocos,_unos_cuantos.jpg` | unos pocos, unos cuantos | manzcuẽe | `LEXR-01059` |
| `diccionario_general/urdir,_preparar_los_hilos_de_la_urdimbre.jpg` | urdir, preparar los hilos de la urdimbre | pcamb-, pcambu- | `LEXR-03412` |
| `diccionario_general/urdirmbre_(hilos_verticales_del_telar).jpg` | urdirmbre (hilos verticales del telar) | pcambnisa | `LEXR-00982` |
| `diccionario_general/urraca.jpg` | urraca | ulchic | `LEXR-03512` |
| `diccionario_general/urraca_(ave).jpg` | urraca (ave) | ulchic | `LEXR-01007` |
| `diccionario_general/usado,_viejo.jpg` | usado, viejo | pete | `LEXR-02437` |
| `diccionario_general/usado,_viejo,_remendado.jpg` | usado, viejo, remendado | mell | `LEXR-02213` |
| `diccionario_general/ustedes.jpg` | ustedes | i’cue’sh | `LEXR-02375` |
| `diccionario_general/uvillo.jpg` | uvillo | shbu | `LEXR-03748` |
| `diccionario_general/vaca.jpg` | vaca | cla | `LEXR-02040` |
| `diccionario_general/vaciar.jpg` | vaciar | jyãsh-, jyãshi- | `LEXR-02750` |
| `diccionario_general/vaciar_(granos).jpg` | vaciar (granos) | jyamb-, jyambu- | `LEXR-02314` |
| `diccionario_general/vaciar_(líquido).jpg` | vaciar (líquido) | jyaw-, jyawu- | `LEXR-03456` |
| `diccionario_general/valiente.jpg` | valiente | ũus chjãchjãsa | `LEXR-03532` |
| `diccionario_general/vara_larga.jpg` | vara larga | cfind | `LEXR-02605` |
| `diccionario_general/varicela,_viruela_loca.jpg` | varicela, viruela loca | buts wee, buts wee wajwa | `LEXR-02034` |
| `diccionario_general/varios,_bastante.jpg` | varios, bastante | cuj (cũj) | `LEXR-02262` |
| `diccionario_general/vela.jpg` | vela | bela | `LEXR-01970` |
| `diccionario_general/vena.jpg` | vena | ee watse | `LEXR-00411` |
| `diccionario_general/vena_de_la_nuca.jpg` | vena de la nuca | tyjicj watse | `LEXR-02973` |
| `diccionario_general/venado.jpg` | venado | chavy | `LEXR-00773` |
| `diccionario_general/vender.jpg` | vender | tywey-, tyweyúu- (cywey-) | `LEXR-00739` |
| `diccionario_general/vendido.jpg` | vendido | tyweyní | `LEXR-03764` |
| `diccionario_general/venida.jpg` | venida | yuuní, yuuwa’j | `LEXR-02907` |
| `diccionario_general/venir.jpg` | venir | yuj-, yuwée-, yuu- | `LEXR-01497` |
| `diccionario_general/venir_acompañado_a_otro_voluntariamente.jpg` | venir acompañado a otro voluntariamente | paayuu- | `LEXR-03746` |
| `diccionario_general/ventear.jpg` | ventear | wejya-, wejyáa- | `LEXR-03794` |
| `diccionario_general/ver_visiones.jpg` | ver visiones | ĩ’cj-, ĩ’cje- | `LEXR-02645` |
| `diccionario_general/verdaderamente.jpg` | verdaderamente | ĩshiimée | `LEXR-02352` |
| `diccionario_general/verdugo.jpg` | verdugo | pcyuusa | `LEXR-00438` |
| `diccionario_general/vereda.jpg` | vereda | nasa dyi’j | `LEXR-00615` |
| `diccionario_general/vereda_de_mariposas.jpg` | vereda de Mariposas | smeme quits | `LEXR-01323` |
| `diccionario_general/vergonzoso.jpg` | vergonzoso | paytjame’ | `LEXR-01673` |
| `diccionario_general/vergüenza.jpg` | vergüenza | tjame ũus | `LEXR-00999` |
| `diccionario_general/verter.jpg` | verter | squijw-, squiwu- | `LEXR-02067` |
| `diccionario_general/vertical.jpg` | vertical | quiitj | `LEXR-01481` |
| `diccionario_general/vestido.jpg` | vestido | atjni | `LEXR-01581` |
| `diccionario_general/vestido_sin_costura.jpg` | vestido sin costura | catstendenimeesa | `LEXR-01278` |
| `diccionario_general/vestir_(a_otro).jpg` | vestir (a otro) | cjyũ’ju’j-, cjyũ’ju’ju- | `LEXR-02363` |
| `diccionario_general/vestirse_(dícese_de_la_mujer).jpg` | vestirse (dícese de la mujer) | is- | `LEXR-01221` |
| `diccionario_general/vez.jpg` | vez | us | `LEXR-01828` |
| `diccionario_general/viajarm_andar_de_una_parte_a_otra.jpg` | viajarm andar de una parte a otra | pecu’j-, pecu’ju- | `LEXR-02119` |
| `diccionario_general/viche,_no_maduro.jpg` | viche, no maduro | chacha | `LEXR-02606` |
| `diccionario_general/vieja,_anciana.jpg` | vieja, anciana | penzh, penzhcuẽ | `LEXR-02054` |
| `diccionario_general/viejo_(referiendo_a_hombre,_o_a_cosa).jpg` | viejo (referiendo a hombre, o a cosa) | ĩish | `LEXR-03888` |
| `diccionario_general/viruela.jpg` | viruela | buts wee wala | `LEXR-02515` |
| `diccionario_general/visible.jpg` | visible | vyaasa | `LEXR-03813` |
| `diccionario_general/visitar.jpg` | visitar | visitaĩ- | `LEXR-02240` |
| `diccionario_general/vistazo_oblícuo.jpg` | vistazo oblícuo | yafy menzu | `LEXR-02189` |
| `diccionario_general/vivir.jpg` | vivir | ĩtyĩ fi’nze | `LEXR-03827` |
| `diccionario_general/vivir,_estar_vivo.jpg` | vivir, estar vivo | ĩtyĩ fi’nze | `LEXR-01505` |
| `diccionario_general/vivir,_pasar_el_día.jpg` | vivir, pasar el día | fi’nze- | `LEXR-00507` |
| `diccionario_general/vivo,_viviente.jpg` | vivo, viviente | ĩtyĩ | `LEXR-01434` |
| `diccionario_general/volar.jpg` | volar | jyuja-, jyujáa- (T) | `LEXR-00713` |
| `diccionario_general/volteado_(boca_arriba).jpg` | volteado (boca arriba) | cjẽete | `LEXR-03428` |
| `diccionario_general/voltear.jpg` | voltear | tupj-, tupji- | `LEXR-00738` |
| `diccionario_general/voltear_para_abajo.jpg` | voltear para abajo | leepja’- | `LEXR-00421` |
| `diccionario_general/voltearse,_volver.jpg` | voltearse, volver | tupji- | `LEXR-01420` |
| `diccionario_general/voluntariamente,_de_buena_gana.jpg` | voluntariamente, de buena gana | wa’lmée | `LEXR-01563` |
| `diccionario_general/volverse_agua.jpg` | volverse agua | yu’a- | `LEXR-01342` |
| `diccionario_general/volverse_mezquino.jpg` | volverse mezquino | sendy yuu- | `LEXR-03545` |
| `diccionario_general/volverse_pardo.jpg` | volverse pardo | shumáa- | `LEXR-01756` |
| `diccionario_general/volverse_perezozo.jpg` | volverse perezozo | watycue yuu- | `LEXR-03157` |
| `diccionario_general/volverse_sordo.jpg` | volverse sordo | much yuu- | `LEXR-03753` |
| `diccionario_general/vomitar.jpg` | vomitar | punga-, pungáa- | `LEXR-00911` |
| `diccionario_general/vía_láctea.jpg` | vía láctea | ã’ mush | `LEXR-03720` |
| `diccionario_general/víbora_venenosa_(bothropo_atrox).jpg` | víbora venenosa (bothropo atrox) | ul equis | `LEXR-01260` |
| `diccionario_general/y.jpg` | y | vite’ | `LEXR-00746` |
| `diccionario_general/yacuma_blanca_(planta_medicinal).jpg` | yacuma blanca (planta medicinal) | yacum | `LEXR-00847` |
| `diccionario_general/yerbatero.jpg` | yerbatero | jyutj vissa | `LEXR-02488` |
| `diccionario_general/yo_(femenino).jpg` | yo (femenino) | ũ’cue (ũ’c J) | `LEXR-01506` |
| `diccionario_general/yo,_conmigo,_mine.jpg` | yo, conmigo, mine | andy | `LEXR-03219` |
| `diccionario_general/yuca_viche.jpg` | yuca viche | ña chachay | `LEXR-02873` |
| `diccionario_general/zafar,_quitar.jpg` | zafar, quitar | jypajnde-, jypaajnde | `LEXR-02486` |
| `diccionario_general/zafarse.jpg` | zafarse | pate-, patée- | `LEXR-02669` |
| `diccionario_general/zafarse_y_caer.jpg` | zafarse y caer | saapajcy-, saapaqui- | `LEXR-02175` |
| `diccionario_general/zafarse,_desengarzarse.jpg` | zafarse, desengarzarse | yaatsjunde- | `LEXR-01018` |
| `diccionario_general/zarco.jpg` | zarco | yafy tsẽy | `LEXR-03368` |
| `diccionario_general/zarco,_azul-verde.jpg` | zarco, azul-verde | saatill | `LEXR-02394` |
| `diccionario_general/zarigüeya,_chucha.jpg` | zarigüeya, chucha | chucha | `LEXR-00775` |
| `diccionario_general/zarzamora_(planta).jpg` | zarzamora (planta) | tsiun | `LEXR-02237` |
| `diccionario_general/zorrillo,_comadreja_(mamífero).jpg` | zorrillo, comadreja (mamífero) | wãyãy (wẽyĩy) | `LEXR-02594` |
| `diccionario_general/zorro.jpg` | zorro | sulu | `LEXR-01164` |
| `diccionario_general/zumbar.jpg` | zumbar | twĩi- | `LEXR-00556` |
| `diccionario_general/zumo_de_la_hoja_de_encenillo_(medicinal).jpg` | zumo de la hoja de encenillo (medicinal) | tsute yu’ | `LEXR-03000` |
| `diccionario_general/zurdo.jpg` | zurdo | jembu cuseju | `LEXR-01383` |
| `diccionario_general/¡camine!.jpg` | ¡Camine! | mejca, mejcawe | `LEXR-01921` |
| `diccionario_general/¡coma!.jpg` | ¡Coma! | mẽ’, mẽ’we | `LEXR-02165` |
| `diccionario_general/¡coséchelo!.jpg` | ¡Coséchelo! | mende | `LEXR-00805` |
| `diccionario_general/¡diga!.jpg` | ¡Diga! | mee | `LEXR-01462` |
| `diccionario_general/¡dispare!.jpg` | ¡Dispare! | mẽpa | `LEXR-01602` |
| `diccionario_general/¡déle!.jpg` | ¡Déle! | mẽs, mẽswe | `LEXR-02381` |
| `diccionario_general/¡entre!.jpg` | ¡Entre! | me’ca, me’cawe | `LEXR-03588` |
| `diccionario_general/¡fuera!_(ahuyentando_gallinas).jpg` | ¡Fuera! (ahuyentando gallinas) | ¡uvy uvy! | `LEXR-03491` |
| `diccionario_general/¡llore!.jpg` | ¡Llore! | mẽ’ne, mẽ’newe | `LEXR-03542` |
| `diccionario_general/¡muélalo!.jpg` | ¡Muélalo! | mẽ’cjwe | `LEXR-00614` |
| `diccionario_general/¡pégale!.jpg` | ¡Pégale! | meca, mecawe | `LEXR-02432` |
| `diccionario_general/¡que_esté!.jpg` | ¡Que esté! | me’p, me’pwe | `LEXR-02536` |
| `diccionario_general/¡quiébrelo!.jpg` | ¡Quiébrelo! | mend | `LEXR-01300` |
| `diccionario_general/¡siémbrelo!.jpg` | ¡Siémbrelo! | meej | `LEXR-01150` |
| `diccionario_general/¡toma!.jpg` | ¡Toma! | shuj | `LEXR-02676` |
| `diccionario_general/¡uy!_(expresión_de_asombro).jpg` | ¡Uy! (expresión de asombro) | ¡uuju! | `LEXR-01837` |
| `diccionario_general/¡vaya!.jpg` | ¡Vaya! | me’j, me’jwe | `LEXR-01796` |
| `diccionario_general/¿por_qué_,_¿para_qué.jpg` | ¿por qué?, ¿para qué? | mjĩte, mjĩya | `LEXR-02754` |
| `diccionario_general/ácido.jpg` | ácido | pllaana’ | `LEXR-01475` |
| `diccionario_general/él,_ella,_aquel,_aquella,_ese,_esa.jpg` | él, ella, aquel, aquella, ese, esa | tyãa (cyãa) | `LEXR-01489` |
| `diccionario_general/él,_ella,_aquél,_aquélla.jpg` | él, ella, aquél, aquélla | cyãa (tyãa) | `LEXR-03174` |
| `diccionario_general/último.jpg` | último | nmej | `LEXR-02115` |
| `diccionario_general/último,_menor_(ej._hijo,_menor_de_todos).jpg` | último, menor (ej. hijo, menor de todos) | nmejwe’sh | `LEXR-01924` |
| `diccionario_general/útil.jpg` | útil | seelpisa | `LEXR-00637` |
## `frutas_verduras` (24 archivos)

| Archivo sugerido | espanol (etiqueta) | nasa_yuwe | id |
|-------------------|---------------------|-----------|----|
| `frutas_verduras/aguacate.jpg` | Aguacate | Uhçe | `LEX-00236` |
| `frutas_verduras/ajo.jpg` | Ajo | Akhus | `LEX-00217` |
| `frutas_verduras/banano.jpg` | Banano | Knenxu iç | `LEX-00221` |
| `frutas_verduras/chirimoya.jpg` | Chirimoya | Mulx | `LEX-00228` |
| `frutas_verduras/curuba.jpg` | Curuba | Nxawnuu | `LEX-00215` |
| `frutas_verduras/durazno.jpg` | Durazno | Lasxnu | `LEX-00222` |
| `frutas_verduras/granadilla.jpg` | Granadilla | Sxlal | `LEX-00234` |
| `frutas_verduras/guama.jpg` | Guama | Afx | `LEX-00216` |
| `frutas_verduras/guanabana.jpg` | Guanabana | Mulx çuç | `LEX-00229` |
| `frutas_verduras/guayaba.jpg` | Guayaba | Pçxid | `LEX-00232` |
| `frutas_verduras/limon.jpg` | Limon | Lxima txhib | `LEX-00225` |
| `frutas_verduras/lulo.jpg` | Lulo | Mutkwe | `LEX-00230` |
| `frutas_verduras/mandarina.jpg` | Mandarina | Sxulxkwe | `LEX-00235` |
| `frutas_verduras/mango.jpg` | Mango | Beçe | `LEX-00218` |
| `frutas_verduras/manzana.jpg` | Manzana | Nxun wahwa | `LEX-00231` |
| `frutas_verduras/maracuya.jpg` | Maracuya | Yawnu | `LEX-00237` |
| `frutas_verduras/mora.jpg` | Mora | Snxuun | `LEX-00233` |
| `frutas_verduras/naranja.jpg` | Naranja | Lxima | `LEX-00224` |
| `frutas_verduras/papaya.jpg` | Papaya | Meem wala | `LEX-00227` |
| `frutas_verduras/pina.jpg` | Pina | Çxahu | `LEX-00219` |
| `frutas_verduras/tomate.jpg` | Tomate | Matku | `LEX-00226` |
| `frutas_verduras/uva_silvestre.jpg` | Uva silvestre | Tlxi'ja | `LEX-00214` |
| `frutas_verduras/uvas.jpg` | Uvas | Fel | `LEX-00220` |
| `frutas_verduras/zapote.jpg` | Zapote | Lemnxun | `LEX-00223` |
## `herramientas` (17 archivos)

| Archivo sugerido | espanol (etiqueta) | nasa_yuwe | id |
|-------------------|---------------------|-----------|----|
| `herramientas/ahoyador.jpg` | Ahoyador | Kafxi'jsa | `LEX-00291` |
| `herramientas/alicate.jpg` | Alicate | Çaam spethsa | `LEX-00285` |
| `herramientas/azadon.jpg` | Azadon | Çaam pçxuuk | `LEX-00284` |
| `herramientas/barra.jpg` | Barra | Çaam a'bat | `LEX-00282` |
| `herramientas/barreton.jpg` | Barreton | Çaam su’yakh | `LEX-00286` |
| `herramientas/carretilla.jpg` | Carretilla | Çaam txiwe pubwa' | `LEX-00287` |
| `herramientas/deshojador.jpg` | Deshojador | Eç spethwa' | `LEX-00290` |
| `herramientas/flauta.jpg` | Flauta | Kuvx | `LEX-00292` |
| `herramientas/guitarra.jpg` | Guitarra | Tala | `LEX-00295` |
| `herramientas/hacha.jpg` | Hacha | Am | `LEX-00281` |
| `herramientas/machete.jpg` | Machete | Çxilx wala | `LEX-00289` |
| `herramientas/manguera.jpg` | Manguera | Yu' wëzxwa' | `LEX-00297` |
| `herramientas/martillo.jpg` | Martillo | Uka çaam | `LEX-00296` |
| `herramientas/motosierra.jpg` | Motosierra | Çaam zihkh twakwa' | `LEX-00288` |
| `herramientas/pica.jpg` | Pica | Çaam çxa'bwïkh | `LEX-00283` |
| `herramientas/tambor.jpg` | Tambor | Kweth | `LEX-00294` |
| `herramientas/zampona.jpg` | Zampona | Kuvx musx | `LEX-00293` |
## `muebles_inmuebles` (15 archivos)

| Archivo sugerido | espanol (etiqueta) | nasa_yuwe | id |
|-------------------|---------------------|-----------|----|
| `muebles_inmuebles/cama.jpg` | Cama | Atüu | `LEX-00347` |
| `muebles_inmuebles/casa.jpg` | Casa | Yat | `LEX-00358` |
| `muebles_inmuebles/choza.jpg` | Choza | Yat wa' | `LEX-00359` |
| `muebles_inmuebles/cocina.jpg` | Cocina | Kçina | `LEX-00349` |
| `muebles_inmuebles/dinero.jpg` | Dinero | Vxyuu | `LEX-00356` |
| `muebles_inmuebles/huerta.jpg` | Huerta | Tul | `LEX-00354` |
| `muebles_inmuebles/lavadero_de_ropa.jpg` | Lavadero de ropa | Aç thetnxi | `LEX-00346` |
| `muebles_inmuebles/mesa.jpg` | Mesa | Paatap | `LEX-00351` |
| `muebles_inmuebles/puente.jpg` | Puente | Weh | `LEX-00357` |
| `muebles_inmuebles/puerta.jpg` | Puerta | Vxiç | `LEX-00355` |
| `muebles_inmuebles/ropero.jpg` | Ropero | Belx sxawwa' | `LEX-00348` |
| `muebles_inmuebles/sala.jpg` | Sala | Nxuhne | `LEX-00350` |
| `muebles_inmuebles/silla.jpg` | Silla | Pagu | `LEX-00352` |
| `muebles_inmuebles/trapiche.jpg` | Trapiche | Tel | `LEX-00353` |
| `muebles_inmuebles/ventana.jpg` | Ventana | Yat yafx | `LEX-00360` |
## `nombres_propios` (20 archivos)

| Archivo sugerido | espanol (etiqueta) | nasa_yuwe | id |
|-------------------|---------------------|-----------|----|
| `nombres_propios/abel.jpg` | Abel | Wel | `LEX-00380` |
| `nombres_propios/cecilia.jpg` | Cecilia | Sila | `LEX-00374` |
| `nombres_propios/domingo.jpg` | Domingo | Tmigu | `LEX-00377` |
| `nombres_propios/enrique.jpg` | Enrique | Lxiki | `LEX-00369` |
| `nombres_propios/enriqueta.jpg` | Enriqueta | Lxika | `LEX-00368` |
| `nombres_propios/francisca.jpg` | Francisca | Siska | `LEX-00375` |
| `nombres_propios/francisco.jpg` | Francisco | Lasku | `LEX-00367` |
| `nombres_propios/isabela.jpg` | Isabela | Saphela | `LEX-00373` |
| `nombres_propios/jesus.jpg` | Jesus | Ksus | `LEX-00366` |
| `nombres_propios/jose.jpg` | Jose | Ksee | `LEX-00364` |
| `nombres_propios/josefa.jpg` | Josefa | Ksepa | `LEX-00365` |
| `nombres_propios/juan.jpg` | Juan | Khwen | `LEX-00362` |
| `nombres_propios/juana.jpg` | Juana | Khwena | `LEX-00363` |
| `nombres_propios/juliana.jpg` | Juliana | Khlxana | `LEX-00361` |
| `nombres_propios/manuel.jpg` | Manuel | Nwel | `LEX-00371` |
| `nombres_propios/maria.jpg` | Maria | Mlxilx | `LEX-00370` |
| `nombres_propios/martin.jpg` | Martin | Txin | `LEX-00378` |
| `nombres_propios/martina.jpg` | Martina | Txina | `LEX-00379` |
| `nombres_propios/otilia.jpg` | Otilia | Til | `LEX-00376` |
| `nombres_propios/pedro.jpg` | Pedro | Peklu | `LEX-00372` |
## `numeros` (58 archivos)

| Archivo sugerido | espanol (etiqueta) | nasa_yuwe | id |
|-------------------|---------------------|-----------|----|
| `numeros/catorce.jpg` | Catorce | Kse pahz | `LEX-00015` |
| `numeros/cero.jpg` | Cero | Mea | `LEX-00001` |
| `numeros/cien.jpg` | Cien | Eçxkan | `LEX-00029` |
| `numeros/cien_mil.jpg` | Cien mil | Eçxkan pkab | `LEX-00056` |
| `numeros/cinco.jpg` | Cinco | Tahç | `LEX-00006` |
| `numeros/cinco_mil.jpg` | Cinco mil | Tapkab | `LEX-00042` |
| `numeros/cincuenta.jpg` | Cincuenta | Taba | `LEX-00024` |
| `numeros/cincuenta_mil.jpg` | Cincuenta mil | Taba pkab | `LEX-00051` |
| `numeros/cuarenta.jpg` | Cuarenta | Paba | `LEX-00023` |
| `numeros/cuarenta_mil.jpg` | Cuarenta mil | Paba pkab | `LEX-00050` |
| `numeros/cuatro.jpg` | Cuatro | Pahz | `LEX-00005` |
| `numeros/cuatro_mil.jpg` | Cuatro mil | Papkab | `LEX-00041` |
| `numeros/cuatrocientos.jpg` | Cuatrocientos | Pakan | `LEX-00032` |
| `numeros/diecinueve.jpg` | Diecinueve | Kse kheb | `LEX-00020` |
| `numeros/dieciocho.jpg` | Dieciocho | Kse tawn | `LEX-00019` |
| `numeros/dieciseis.jpg` | Dieciseis | Kse setx | `LEX-00017` |
| `numeros/diecisiete.jpg` | Diecisiete | Kse sa't | `LEX-00018` |
| `numeros/diez.jpg` | Diez | Kseba | `LEX-00011` |
| `numeros/diez_mil.jpg` | Diez mil | Kseba pkab | `LEX-00047` |
| `numeros/doce.jpg` | Doce | Kse e'z | `LEX-00013` |
| `numeros/dos.jpg` | Dos | E'z | `LEX-00003` |
| `numeros/dos_mil.jpg` | Dos mil | Epkab | `LEX-00039` |
| `numeros/dos_millones.jpg` | Dos millones | E'z pizx | `LEX-00058` |
| `numeros/doscientos.jpg` | Doscientos | Ekan | `LEX-00030` |
| `numeros/mil.jpg` | Mil | Pkab | `LEX-00038` |
| `numeros/novecientos.jpg` | Novecientos | Khekan | `LEX-00037` |
| `numeros/noventa.jpg` | Noventa | Kheba | `LEX-00028` |
| `numeros/noventa_mil.jpg` | Noventa mil | Kheba pkab | `LEX-00055` |
| `numeros/nueve.jpg` | Nueve | Kheb | `LEX-00010` |
| `numeros/nueve_mil.jpg` | Nueve mil | Khepkab | `LEX-00046` |
| `numeros/ochenta.jpg` | Ochenta | Tawnba | `LEX-00027` |
| `numeros/ochenta_mil.jpg` | Ochenta mil | Tawnba pkab | `LEX-00054` |
| `numeros/ocho.jpg` | Ocho | Tawn | `LEX-00009` |
| `numeros/ocho_mil.jpg` | Ocho mil | Tawnpkab | `LEX-00045` |
| `numeros/ochocientos.jpg` | Ochocientos | Tawnkan | `LEX-00036` |
| `numeros/once.jpg` | Once | Kse teeçx | `LEX-00012` |
| `numeros/quince.jpg` | Quince | Kse tahç | `LEX-00016` |
| `numeros/quinientos.jpg` | Quinientos | Takan | `LEX-00033` |
| `numeros/seis.jpg` | Seis | Setx | `LEX-00007` |
| `numeros/seis_mil.jpg` | Seis mil | Sepkab | `LEX-00043` |
| `numeros/seiscientos.jpg` | Seiscientos | Sekan | `LEX-00034` |
| `numeros/sesenta.jpg` | Sesenta | Seba | `LEX-00025` |
| `numeros/sesenta_mil.jpg` | Sesenta mil | Seba pkab | `LEX-00052` |
| `numeros/setecientos.jpg` | Setecientos | Sakan | `LEX-00035` |
| `numeros/setenta.jpg` | Setenta | Saba | `LEX-00026` |
| `numeros/setenta_mil.jpg` | Setenta mil | Saba pkab | `LEX-00053` |
| `numeros/siete.jpg` | Siete | Sa't | `LEX-00008` |
| `numeros/siete_mil.jpg` | Siete mil | Sapkab | `LEX-00044` |
| `numeros/trece.jpg` | Trece | Kse tekh | `LEX-00014` |
| `numeros/treinta.jpg` | Treinta | Teba | `LEX-00022` |
| `numeros/treinta_mil.jpg` | Treinta mil | Teba pkab | `LEX-00049` |
| `numeros/tres.jpg` | Tres | Tekh | `LEX-00004` |
| `numeros/tres_mil.jpg` | Tres mil | Tepkab | `LEX-00040` |
| `numeros/trescientos.jpg` | Trescientos | Tekan | `LEX-00031` |
| `numeros/un_millon.jpg` | Un millon | Pizx | `LEX-00057` |
| `numeros/uno.jpg` | Uno | Teeçx | `LEX-00002` |
| `numeros/veinte.jpg` | Veinte | Eba | `LEX-00021` |
| `numeros/veinte_mil.jpg` | Veinte mil | Eba pkab | `LEX-00048` |
## `parentescos` (13 archivos)

| Archivo sugerido | espanol (etiqueta) | nasa_yuwe | id |
|-------------------|---------------------|-----------|----|
| `parentescos/abuela.jpg` | Abuela | Lula | `LEX-00182` |
| `parentescos/abuelo.jpg` | Abuelo | Talul | `LEX-00185` |
| `parentescos/ahijado.jpg` | Ahijado | Khaalu | `LEX-00181` |
| `parentescos/anciana.jpg` | Anciana | Peezx | `LEX-00184` |
| `parentescos/cunado.jpg` | Cunado | Çu’m | `LEX-00178` |
| `parentescos/esposa.jpg` | Esposa | Dxyuu | `LEX-00180` |
| `parentescos/hermana.jpg` | Hermana | Be'sx | `LEX-00177` |
| `parentescos/hermano.jpg` | Hermano | Ziiy | `LEX-00188` |
| `parentescos/hija.jpg` | Hija | Nyiis | `LEX-00183` |
| `parentescos/hijo.jpg` | Hijo | Dçxikh | `LEX-00179` |
| `parentescos/mama.jpg` | Mama | Uma | `LEX-00187` |
| `parentescos/nieto_o_nieta.jpg` | Nieto o nieta | Zun | `LEX-00189` |
| `parentescos/papa.jpg` | Papa | Tata | `LEX-00186` |
## `plantas_medicinales` (20 archivos)

| Archivo sugerido | espanol (etiqueta) | nasa_yuwe | id |
|-------------------|---------------------|-----------|----|
| `plantas_medicinales/alegria.jpg` | Alegria | Çxayu’ç | `LEX-00252` |
| `plantas_medicinales/aloe_vera.jpg` | Aloe vera | Bahç na’na | `LEX-00250` |
| `plantas_medicinales/barbasco.jpg` | Barbasco | Çba'w | `LEX-00240` |
| `plantas_medicinales/botoncillo.jpg` | Botoncillo | Bu’çx | `LEX-00239` |
| `plantas_medicinales/chilca.jpg` | Chilca | Taph | `LEX-00257` |
| `plantas_medicinales/coca.jpg` | Coca | Ësx | `LEX-00253` |
| `plantas_medicinales/escoba.jpg` | Escoba | Pçxaga | `LEX-00244` |
| `plantas_medicinales/lengua_de_vaca.jpg` | Lengua de vaca | Klathune | `LEX-00249` |
| `plantas_medicinales/ortiga.jpg` | Ortiga | Khäas | `LEX-00254` |
| `plantas_medicinales/ortiga_roja.jpg` | Ortiga roja | Khäas beh | `LEX-00255` |
| `plantas_medicinales/paico.jpg` | Paico | Paiku | `LEX-00248` |
| `plantas_medicinales/poleo.jpg` | Poleo | Bakhis | `LEX-00238` |
| `plantas_medicinales/ruda.jpg` | Ruda | Luuta | `LEX-00242` |
| `plantas_medicinales/tabaco.jpg` | Tabaco | Wëhnx | `LEX-00247` |
| `plantas_medicinales/tomillo.jpg` | Tomillo | Neklu | `LEX-00243` |
| `plantas_medicinales/verbena.jpg` | Verbena | Belwëna | `LEX-00251` |
| `plantas_medicinales/yerba_chivo.jpg` | Yerba chivo | Pisxaa jxuth | `LEX-00245` |
| `plantas_medicinales/yerba_golpe.jpg` | Yerba golpe | Pisxaa thune | `LEX-00246` |
| `plantas_medicinales/yerba_mora.jpg` | Yerba mora | Eçx äwä ziç | `LEX-00241` |
| `plantas_medicinales/yerbabuena.jpg` | Yerbabuena | Pataathxä’ | `LEX-00256` |
## `saludos` (1 archivos)

| Archivo sugerido | espanol (etiqueta) | nasa_yuwe | id |
|-------------------|---------------------|-----------|----|
| `saludos/saludo_basico.jpg` | Saludo basico | Ma’g pe’t | `LEX-00113` |
## `utiles_hogar` (18 archivos)

| Archivo sugerido | espanol (etiqueta) | nasa_yuwe | id |
|-------------------|---------------------|-----------|----|
| `utiles_hogar/algodon.jpg` | Algodon | Wawa | `LEX-00315` |
| `utiles_hogar/bano_o_inodoro.jpg` | Bano o inodoro | Üçxhwa | `LEX-00314` |
| `utiles_hogar/cernidor.jpg` | Cernidor | Äçthe | `LEX-00298` |
| `utiles_hogar/cuchara.jpg` | Cuchara | Tuçxa'y | `LEX-00312` |
| `utiles_hogar/cucharona.jpg` | Cucharona | Ejwa | `LEX-00305` |
| `utiles_hogar/cuchillo.jpg` | Cuchillo | Çxilx | `LEX-00304` |
| `utiles_hogar/ducha.jpg` | Ducha | Pewnxi | `LEX-00310` |
| `utiles_hogar/espejo.jpg` | Espejo | Thegnxi | `LEX-00311` |
| `utiles_hogar/estufa.jpg` | Estufa | Çaam miç ahwa | `LEX-00302` |
| `utiles_hogar/fogon.jpg` | Fogon | Ipx kat | `LEX-00306` |
| `utiles_hogar/humo.jpg` | Humo | Ah | `LEX-00299` |
| `utiles_hogar/jabon.jpg` | Jabon | Kpuun | `LEX-00307` |
| `utiles_hogar/olla.jpg` | Olla | Miç | `LEX-00309` |
| `utiles_hogar/olleta.jpg` | Olleta | Lxeta | `LEX-00308` |
| `utiles_hogar/peine.jpg` | Peine | Txid | `LEX-00313` |
| `utiles_hogar/plato.jpg` | Plato | Biçx | `LEX-00301` |
| `utiles_hogar/trampa.jpg` | Trampa | Akh | `LEX-00300` |
| `utiles_hogar/vaso.jpg` | Vaso | Çxa'y | `LEX-00303` |
## `vocabulario_general` (37 archivos)

| Archivo sugerido | espanol (etiqueta) | nasa_yuwe | id |
|-------------------|---------------------|-----------|----|
| `vocabulario_general/abrir_o_extender_los_brazos.jpg` | Abrir o extender los brazos | Çha’ya | `LEX-00080` |
| `vocabulario_general/agarrar.jpg` | Agarrar | Uwe | `LEX-00110` |
| `vocabulario_general/amarrar.jpg` | Amarrar | Tud | `LEX-00106` |
| `vocabulario_general/ancho.jpg` | Ancho | Tape | `LEX-00100` |
| `vocabulario_general/ayudar_o_colaborar.jpg` | Ayudar o colaborar | Puçx | `LEX-00095` |
| `vocabulario_general/bailar_o_danzar.jpg` | Bailar o danzar | Ku’jxa | `LEX-00090` |
| `vocabulario_general/barrer.jpg` | Barrer | Pad | `LEX-00094` |
| `vocabulario_general/barro.jpg` | Barro | Çiç | `LEX-00082` |
| `vocabulario_general/bonito_o_hermosa.jpg` | Bonito o hermosa | Zxiçxkwe | `LEX-00112` |
| `vocabulario_general/borrar_o_limpiar.jpg` | Borrar o limpiar | Khukh | `LEX-00089` |
| `vocabulario_general/caliente.jpg` | Caliente | Açxa | `LEX-00077` |
| `vocabulario_general/camino.jpg` | Camino | Zi’j | `LEX-00111` |
| `vocabulario_general/cargar.jpg` | Cargar | Tu's | `LEX-00105` |
| `vocabulario_general/cerrar.jpg` | Cerrar | Aph | `LEX-00079` |
| `vocabulario_general/colgar.jpg` | Colgar | A'y | `LEX-00076` |
| `vocabulario_general/correr_o_trotar.jpg` | Correr o trotar | Üph | `LEX-00107` |
| `vocabulario_general/cortar.jpg` | Cortar | Speth | `LEX-00096` |
| `vocabulario_general/cuidar_o_vigilar.jpg` | Cuidar o vigilar | Thegu | `LEX-00103` |
| `vocabulario_general/dar_o_entregar.jpg` | Dar o entregar | Üs | `LEX-00109` |
| `vocabulario_general/dibujando.jpg` | Dibujando | Suçn | `LEX-00097` |
| `vocabulario_general/divertido_o_alegre.jpg` | Divertido o alegre | Çxhakwe | `LEX-00084` |
| `vocabulario_general/escribir.jpg` | Escribir | Fxi’j | `LEX-00087` |
| `vocabulario_general/espina_o_chuzo.jpg` | Espina o chuzo | Çhüçh | `LEX-00081` |
| `vocabulario_general/flaco.jpg` | Flaco | Talx | `LEX-00099` |
| `vocabulario_general/fuerza.jpg` | Fuerza | Çxhaçxha | `LEX-00083` |
| `vocabulario_general/hueco.jpg` | Hueco | Kafx | `LEX-00088` |
| `vocabulario_general/lamer.jpg` | Lamer | Teçx | `LEX-00102` |
| `vocabulario_general/lavar_o_enjabonar.jpg` | Lavar o enjabonar | Theth | `LEX-00104` |
| `vocabulario_general/mojado.jpg` | Mojado | Çxupx | `LEX-00085` |
| `vocabulario_general/nacer_o_reventar_huevos.jpg` | Nacer o reventar huevos | Upx | `LEX-00108` |
| `vocabulario_general/noche.jpg` | Noche | Kus | `LEX-00091` |
| `vocabulario_general/por_favor.jpg` | Por favor | Meen | `LEX-00092` |
| `vocabulario_general/redondo_o_circulo.jpg` | Redondo o circulo | Taz | `LEX-00101` |
| `vocabulario_general/sucio.jpg` | Sucio | Çxus | `LEX-00086` |
| `vocabulario_general/sueño.jpg` | Sueño | Sxa'w | `LEX-00098` |
| `vocabulario_general/tapar_o_cubrir.jpg` | Tapar o cubrir | Afxihb | `LEX-00078` |
| `vocabulario_general/trabajo_colectivo_por_un_mismo_objetivo.jpg` | Trabajo colectivo por un mismo objetivo | Minga | `LEX-00093` |
