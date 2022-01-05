import sys
import json
from steno import Steno
from steno import Word

class TestPluvier: 

    one_syllabe_words = {
        "TAS" : "tasse",

#        "SUS" : "suce",
#        "S" : "ce",
        "WEU" : "vie",
        "WEUT" : "vite",
        "TEUP" : "type",
        "TPEUL" : "fil",
        "-TS" : "être",
        "PHAEB": "mienne",

    }
    i_words = {
        "RAPD" : "rapide",
        "TKWEUS" : "édifice",
        "TPORPL/TKABL" : "formidable",

        "WEUS" : "vis",
        "WEUS*" : "visse",

#        "APBLG/OEUPBDZ": "adjoindre",
    }


    prefix_word = {
        "SPWAPBD" : "entende",
        "SPWAPBGS" : "intention",

    }

    suffix_word = {
        "WHROUR" : "velours",
        "TPROEURD": "froideur",
        #    "WLOEFS" : "voulez-vous"
#        "PWAER" : "bière", abbrev
        "RAOD/HRO*EUS" : "radiologiste",
        "SPWOUZ/KWRAFPL" : "enthousiasme",
        "SPWOUZ/KWRA*S" : "enthousiaste",
        "AFRS" : "avoir",
        "POUFRS" : "pouvoir" ,
        "RURL" : "rural",
        "WEURL" : "viral",
        "KOFRBL" : "comble",
        "PAPBGS" : "pension",
        "TERBL" : "terrible",
        "THR-PLT" : "tellement",
        "PAB" : "panne",
        # -ne
#        "ATS/LO*EG" : "astrologue", 
        #    "HAER" : "hier",
        #    "TLOIK" : "technologique",
        #    "SLO*IG" : "psychologie",
        "PAER" : "pierre",
        "WHRUPL": "volume",
        "WHRUPL/TPHAO": "volumineux", #remove star ?!
    }

    right_ch_sound = {
        "AFRPB" : "arche",
        "TOFRPB" : "torche",
        "AFRPB/T*K" : "architecte",
        "PHAFRPBLG" : "manche",
#        "PWHRAFRPBLG" : "blanche",

#        "SKHRAEU": "chalet",
#        "SKWAL" : "cheval",
    }

    corpus = False
    def read_corpus(self):
        if self.corpus:
            return self.corpus
        print('read corpus')
        words = []
        source = "resources/Lexique383.tsv"
        with open(source) as f:
            corpus = f.readlines()


            for line in corpus:
                entry = line.split("\t")
                word = Word(word = entry[0],
                            phonetics = entry[1],
                            lemme = entry[2],
                            cgram = entry[3],
                            cgramortho = entry[28],
                            genre = entry[4],
                            number = entry[5],
                            info_verb = entry[10],
                            syll = entry[22],
                            orthosyll = entry[27]
                            )
                words.append(word)
        return words


    def setup_method(self, test_method):
        self.corpus = self.read_corpus()


    def steno(self,word):
        self.steno_class=Steno(self.corpus)
        return self.steno_class.transform(word)


    def test_lesson1_e_muet(self):
        self.assertSame(self.one_syllabe_words)

    
    def test_lesson2_p(self):
        self.assertSame({'PAP':'pape',
                         'SAP': 'sape',
                         'PAT': 'patte',
                         'PUS' : 'puce',
                         'TAP' : 'tape',
                         'PAS': 'passe'
                         })
    def test_lesson3_r(self):
        self.assertSame({'RA' : 'ras',
                         'RU' : 'rue',
                         'TRAP' : 'trappe',
                         'PART' : 'parte',
                         'STOR' : 'store',
                         'SORT' : 'sorte'
                      #   'RA*' : 'rat'
                         })

    def test_lesson4_w_f(self):
        self.assertSame({

            #'WA' : 'va', #contradiction lesson 19
#                         'WU' : 'vue',
                         'WOT' : 'vote',
                         'RAF' : 'rave',
                         'SAF' : 'savent'
                         })
    def test_lesson4_ortho_star_verb(self):
        self.assertSame({'WOE*' : 'vaut', #star not in the right place
                         'WOE' : 'veau'
                         })

    def test_lesson5_K_L(self):
        self.assertSame({
            "K" : "que",
            "KAR" : "car",
            "KE" : "quai",
            "WAG" : "vague",
            "KOD" : "code",
            "ROEL": "rôle",
            "KOET": "côte",
#            "KOEUL": "colis", inversion
#            "KOEUP": "copie",
#            "KOEUPB": "coin",
#            "KOEUPBS": "coince",
                         })
    def test_lesson5_omittedIWords(self):
        self.assertSame(self.i_words)


    def test_lesson6_H_B(self):
        self.assertSame({'HOE' :'haut',
                         'HOET' : 'haute',
                         'HOT' : 'hotte',
                         'SOB' : 'sonne',
                         'PAB' : 'panne',
                         
                         })
    def test_lesson6_eu(self):
        self.assertSame({ 'SAO' : 'ceux',
                         'SAOL' : 'seul'
                         })

    def test_lesson7_G_D(self):
        self.assertSame({ "WAG" : "vague",
                          "KOD" : "code",
                          "RAG" : 'rage',
                          'SAG' : 'sage',
                          'ROUG' : 'rouge'

                         })

    def test_lesson7_AEU_ai(self):
        self.assertSame({ 'RAEU' : 'raie',
                          'TRAEU' : 'trait',
#                          'AEUD' : 'aide',
                          'SAEU*' : 'sait'
                         })

    def test_lesson8_Z(self):
        self.assertSame({'ROEZ' : 'rose',
                         'RAZ' : 'rase',
#                         'SAEUZ' : 'seize'
                         })

 #skip lesson 9 on numbers
    def test_lesson10_HR_for_L_BG_for_K_ending(self):
        self.assertSame({ 'HREUR' : 'lire',
                          'PHRABG' : 'plaque',
#                          'HRAEUS' : 'laisse'
                         })
    def test_lesson11_TK_for_d_FL_for_F(self):
        self.assertSame({ 'TK' : 'de',
                          'TKU' : 'du',
                          'TKOUT' : 'doute',
                          'WEUFL' : 'vif',
                          'WEUF' : 'vive'

                         })
        
    def test_lesson11_AU_for_ui(self):
        self.assertSame({ "PAU" : "puis",
                          "KAUT" : "cuite",
                          'KAUS' : 'cuisse',
                          'SAUFR' : 'suivre'
                         })

    def test_lesson12_PW_for_Binit_PL_for_Mfinal(self):
        self.assertSame({ # 'PWO' : 'beau',
#                          'PWOR' : 'bord',
                          'KAPL' : 'came',
#                          'AEUPL*' : 'aime'
                         })

    def test_lesson12_ortho_aSem_for_ieme(self):
        self.assertSame({'AUT/A*EPL': 'huitième',
                         "SEZ/A*EPL": "seizième",
                         # should be "SAEUZ/A*EPL": "seizième",
                         })
        
    def test_lesson12_AOEU_for_ieu(self):
        self.assertSame({'WAOEU' : 'vieux',
                         'HRAOEU' : 'lieu',
#                         'AOEU' : 'yeux',
#                         'KRAOEU' : 'curieux' kur/aoeu
                         })


    def test_lesson12_ortho_rightR_infinitif(self):
        self.assertSame({'PARL/-R' : 'parler'
                         })

    def test_lesson12_ortho_rightD_passe_compose(self):
        self.assertSame({'PARL/-D' : 'parlé',
#                         'SU/-D' : 'sué'
                         })
        
    def test_lesson13_TP_for_F_init_PB_for_N_final(self):
        self.assertSame({"TPEUL": "fil",
                         "TPAUT": "fuite",
                         "TPRAEU": "frais",
                         "POPBT": "ponte",
#                         "TOPB": "ton",
#                         "TPOPB": "fond", 


                         })

    def test_lesson13_RE_prefix(self):
        self.assertSame({ #"R-/TPHRU": "reflux" ,
#                          "R-FR": "refaire",
                          "R-L/WE": "relevé",
#                          "R-LGS": "relation",
#                          "R-LT": "réalité",

                         })
    def test_lesson13_AE_for_ie(self):
        self.assertSame({ "PAE" : "pied",
                          "HAER": "hier",
                          "SAEL" : "ciel",
                          "PAES": "pièce",
                          "TAERS": "tierce",
                         })

    def test_lesson13_AER_ier_iere(self):
        self.assertSame({"KS/A*ER": "caissière", # should be K-S/A*ER : - is required ?
                         "WOEUL/AER": "voilier",
                         "TE/A*ER": "théière",
                         })

    #TODO
    def test_lesson13_inversion_ses_son(self):
        return True 

    def test_lesson13_LEFT_R_can_be_read_as_i_infrontof_a_or_o(self):
        self.assertSame({ 'WROL' : 'viol',
                          'TKRABL' : 'diable'
                         })

    # H- COTE gauche pour les groupement -> not to todo ?

    def test_lesson13_S_alone_for_imparfait(self):
        self.assertSame({"KRABG/-S": "craquait",
                         "PAS/-S": "passait",
                         "KOUR/-S": "courait",
                         })
        
    def test_lesson13_RS_alone_for_conditionnel(self):
        self.assertSame({
                         "KRABG/-RS": "craquerait",
                         "KOUR/-RS": "courrait",
                         "PAS/-RS": "passerait",
                         })

    def test_lesson13_AI_alone_for_nom_ai(self):
        self.assertSame({
            "TEUR/AEU": "tiret",
            "TEUR/-S": "tirait",
            "SORB/AEU": "sorbet",
            "TPEUL/AEU": "filet",
                         })
    def test_lesson13_G_alone_for_ant_partice_present(self):
        self.assertSame({"KREU/-G": "criant",
                         "TKEUZ/-G": "disant",
                         "REU/-G": "riant",
                         "KOUR/-G": "courant",
                         })

    def test_lesson13_BLG_alone_for_quel(self):
        self.assertSame({
            "SEBLG": "séquelle",
            "HRBLG": "lequel",
#                        "HR-BLG": "lequel",
                         })

        

    def test_lesson13_RP_for_peur_RL_for_leur(self):
        self.assertSame({"TRARP": "trappeur",
                         "WRL": "voleur", #should be WORL ?
                         })

    def test_lesson14_PH_for_M_initial(self):
        self.assertSame({
                         "PHAOEU": "mieux",
                         "PHEUZ": "mise",
                         "PHARL": "malheur",
                         })

#    def test_lesson14_LG_for_la(self):
    def test_lesson14_OEU_for_oi_OEUN_for_oin(self):
        self.assertSame({
            "ROEU": "roi",
            "PWOEU": "bois",
            "TPOEUPB": "foin",
            "PWOEUT*": "boite",
                         })

    def test_lesson14_e_never_inside_word_and_star_for_re_suffix(self):
        self.assertSame({
#            "R-L/WE": "relevé",
#            "TK-G/R*E": "degré",
            "TKG/R*E": "degré",
                         })

    def test_lesson14_star_N_for_ending_on(self):
        self.assertSame({
            #"PH-L/*PB": "melon",
            "PHL/*PB": "melon",
#            "PHOPB": "mon",
#            "PH-PB": "million",
                         })


    def test_lesson14_star_S_for_ste(self):
        self.assertSame({"PEU*S": "piste",
                         "HREU*S": "liste",
                         })

    def test_lesson15_TPH_for_N_initial(self):
        self.assertSame({
            "TPHU" : "nu",
            "TPHOEU*": "noie",
            "TPHOEU": "noix",
            "TPHEUD" : "nid",
                         })

    def test_lesson15_GBS_for_final_X(self):
        self.assertSame({ "TPEUBGS": "fixe",
                          "TABGS": "taxe",
                         })

#    def test_lesson15_H_n_Negation(self):


    def test_lesson15_AOU_is_oui(self):
        self.assertSame({"AOU": "oui",
                         "TPAOUB": "fouine",
                         })

        
    def test_lesson15_ez_star_EZ_and_REZ_for_rez(self):
        self.assertSame({"TROUF/*EZ": "trouvez",
                         "PARL/*EZ": "parlez",
                         "PARL/R*EZ": "parlerez",
                         })

    def test_lesson16_KWR_for_y_and_G_for_j(self):
        self.assertSame({
            "KWROT": "yacht", #mistake in lesson : kwrat
#            "KWRAT/US": "hiatus", strange hier is not kwr...
            "PAG": "page",
            "PHARG": "marge", #'maRZ'
                         })


    def TODO_lesson16_conj_Y_for_il(self):
        self.assertSame({ 
                          "KWROEUD": "il doit",
                          "KWRAOF": "il veut",
                         })
        
    def test_lesson16_PBLG_for_dj_and_bj_median(self):
        self.assertSame({
            "APBLG/TEUFL" : "adjectif",
            "OPBLG/TEUFL": "objectif",
            "R-G": "rejet",
                         })

    def test_lesson17_SKWR_for_J_initial_and_SWR_for_Z_initial(self):
        self.assertSame({
#should be ?            "SKWR-L/-D": "gelé",
            "SKWRL/-D": "gelé",
            "SKWROEUPB": "joint",
            "SWRO": "zoo",
#            "SKWRA*EUT": "jette",
                         })
#TODO ?
    def lesson17_nom_propre_ending_y_AO_star_E(self):
        self.assertSame({
            "HAR/AO*E": "Harry",
                         })

    def test_lesson17_final_ette_is_separate_star_T(self):
        self.assertSame({ "TOEUL/*T": "toilette",
                          "POEPL/*T": "pommette",
#should works too "POPLT": "pommette",
                         })

    def test_lesson18_TKPW_for_sound_gue_initial_KW_for_qwe(self):
        self.assertSame({"TKPWOU": "goût",
                         "TKPWAPB": "gant",
                         "TKPWAFL": "gaffe",
                         "AD/KWA": "adéquat",
                         "AD/KWAT": "adéquate",
                         })

    def test_lesson18_double_conson_can_eliminate_letter(self):
        # todo !!
        self.assertSame({
            "WHRAG": "village",
#                         "TKPWR-": "guerre",
#                         "TPRUR": "fourrure",
                         })
    def test_lesson18_AIB_for_aine_sound(self):
        self.assertSame({
            "SAEUB": "saine",
            "TKPWAEUB": "gaine",
#            "TKEUBGS/A*EUB": "dizaine",
#            "KEUPBZ/A*EUB": "quinzaine",
                         })

    def test_lesson19_KP_for_X_in_egz_sound_followed_by_woyel(self):
        self.assertSame({
            "KPEUL": "exil",
#            "KPUT": "exécute",
            "KPEUG": "exige",
#            "STRA": "extra",
                         })

    def test_lesson19_W_is_we_sound(self):
        self.assertSame({
            "TRAPL/W*E": "tramway",
            "SWAEU": "souhait",
                         })

    def test_lesson19_starEB_ending_ene(self):
        self.assertSame({
            "SEUR/*EB": "sirène",
            "KPEUG/*EB": "oxygène",
            
                         })

    def test_lesson19_WstarE_ending_ue_oue(self):
        self.assertSame({
            "TKEUL/W*E": "dilué",
                         "AF/W*E": "avoué",
                         })

    def test_lesson19_WstarEL_ending_uel(self):
        self.assertSame({"WEUZ/W*EL": "visuel",
                         "TKPWRAD/W*EL": "graduel",
#                         "ABT/W*EL": "habituel",
                         })

    def test_lesson19_separate_starZ_ending_a_sound(self):
        self.assertSame({
#            "R-P/*Z": "repas",
                         "SAG/*Z": "saga",
                         "KOUP/*Z": "coupa",
#                         "WOBGZ": "avocat",
#                         "WEUFR/*Z": "vivra",#removed i
                         })

    def test_lesson21_CH_init_is_SH_final_is_FP(self):
        self.assertSame({
            "SHOEU": "choix",
#            "SHO": "chaud",
            "KAFP": "cache",
#            "RUFP": "ruche",
            "SHE": "chez",

                         })
        
    def test_lesson21_starEL_el_ortho_final(self):
        self.assertSame({
            "KRU/*EL": "cruel",
#            "K-PB/*EL": "conditionnel",
#            "K-PBL": "conditionnel",
            "TPEUS/*EL": "ficelle",
                         })

    def test_lesson21_RT_RTS_for_ortho_teur_trice(self):
        self.assertSame({
#            "HRAEURT": "lecteur",
            "ABG/RT": "acteur", # should be ABG/*RT
            "ABG/RTS": "actrice", # ABG/*RTS
#            "HRAEUBG/RTS": "lectrice",
#            "HRAEURTS": "lectrice",
                         })

    def test_lesson22_B_is_final_ne(self):
        self.assertSame({
            "PWOB": "bonne",
            "SKWROEB": "jaune",
            "SKWRAOB": "jeune",
            "SKWRAOBS": "jeunesse",
        })


    def test_lesson22_OIB_for_sound_oine_and_starOIB_for_suffixe_oine(self):
        self.assertSame({
            "TKWOEUB": "douane",
# also work            "TKWAB": "douane",
            #"PHOEUB": "moine",
            "PEU/O*EUB": "pivoine",
                         })

    def test_lesson22_AEN_ien_sound_AEB_for_ienne_sound_star_for_suffix(self):
        self.assertSame({"PHAEPB": "mien",
                         "PHAEB": "mienne",
                         "HRAEPB": "lien",

#                         "SWAEPB": "souvient",
#                         "KWA*EPB": "convient",
                         })

    def test_lesson22_AOUB_for_sound_ouine(self):
        self.assertSame({
            "TPAOUB": "fouine",
#            "STKPWAOUB": "égoïne",
                         })

    def test_lesson22_GZ_for_sound_zion_and_zon(self):
        self.assertSame({
#            "OGZ": "occasion",
            "TPUGZ": "fusion",
#            "SAEUGZ": "saison",
                         })

    def test_lesson23_natural_combo_initial_consonne(self):
        self.assertSame({
#            "STKPWOPB": "second",
            "STPAEUR": "sphère", #'sfER'
            "STRAT": "strate",
            "STEUL": "style",
            "SKRUT": "scrute",
            "STPAEUR": "sphère","STRAT": "strate",
            "STEUL": "style",
            "SKRUT": "scrute",
            "SKOUR": "secours",
#            "SPHREUD": "splendide",
#            "SPH-": "semaine",
            "SPREUPBT": "sprint",
#            "SRA": "sera",
            "TKPWHRAS": "glace",
            "TKPWREU": "gris",
            "TKREUPB": "drain", #'dR5'
            "TPHRAOR": "fleur", #'fl9R'
#            "TPRAEUL": "frêle",#'fREl'
            "TROU": "trou",
            "KHRAS": "classe",
            "KRAPB": "cran",
            "PWHROBG": "bloc",
            "PWREUPB": "brin",
            "PHRUPL": "plume",
            "PREUZ": "prise",
            "WHROUR": "velours",
            "WRAEU": "vrai",

                         })

    def test_lesson22_final_natural_consonnes(self):
        self.assertSame({
            "SOLD": "solde",
            "TORS": "torse",
            "TPORPL": "forme",
            "TKOUBL": "double", #'dubl'
            "TART": "tarte",
            "KARP": "carpe",
#            "KOFR": "coffre", 
            "KORB": "corne",
            "KULT": "culte",
            "KOPBT": "conte",
            "SOPBD": "sonde","PARBG": "parc",
            "PARL": "parle",
            "PABGT": "pacte",
            "PHORG": "morgue",
#            "HRAPS/R-R": "laps",
            "HROPBG": "longue",
            "SOUFL": "souffle",
            "AEURB": "herbe",
#            "AFPT": "achète", # a-SEt
#             "ORPBLG": "orge", #'ORZ'
            "OPT": "opte", 
#            "APBL/W*E": "enlevé",


        })

    def test_lesson25_KH_for_sound_mne(self):
        self.assertSame({
            "KHAS": "menace", #m°-nas
            "KHU": "menu",
            "KHAOR": "mineur",
            "KHUT": "minute",
            "KHAUZ/AER": "menuisier",
        })
        
    def test_lesson25_AE_for_starting_letter_a_word(self):
        self.assertSame({
#            "AE/WEUD": "avide",
            "AE/TKOR": "adore",
            "AE/TKAOEU": "adieu",
            "AE/PHORS": "amorce",
            "AE/TKOPT": "adopte",

            })

        #TODO  il y a et preposition lesson 26
    def test_lesson26_AEN_for_sound_ian(self):
        self.assertSame({
            "SAEPBS": "science", #'sj@s'
        })
        
    def test_lesson26_final_NS_for_ortho_ance_or_ence(self):
        self.assertSame({
#            "KROEUPBS": "croissance",
            "SPHREPBS": "suppléance",
#            "STPRAPBS": "souffrance",
#            "SAURPBS": "assurance",

        })

        
    def test_lesson26_final_ND_for_ortho_ande(self):
        self.assertSame({
            "WEUPBD": "viande",
            "TPREUPBD": "friande",
#            "TPREUPBDZ": "friandise",
        })

    def test_lesson26_KT_for_ortho_cte(self):
        self.assertSame({
            "ABGT": "acte",
            "TKEUBGT": "dicte",
            "PABGT": "pacte",
            "TRABGT": "tract",
#            "KHRAEUBGT": "collecte",
        })
    def test_lesson26_KEOEN_for_prefix_con(self):
        self.assertSame({
#            "KOEPB/SAEPBS": "conscience",
            "KOEPB/KAF": "concave",

            "KOEPB/KHRUR": "conclure",
# ordre du slash            "KOEPB/TOUR": "contour",
        })            
    def test_lesson27_STK_for_starting_des_and_dec_following_by_woyel(self):
        self.assertSame({
#            "TKAEUS/*EUPB": "dessin",
            "STKEUR": "désir",
            "STKAPBDZ": "descendre",
            "STKU": "dessus",
            "STKOU": "dessous",
            "STKAEUR": "désert",
            #"STK*EUR": "désire",

        })
        
        
    def test_lesson27_DAOE_for_starting_ortho_de(self):
        self.assertSame({
            #"TKAOE/KOUDZ": "découdre",
#                         "TKAOE/KOFP/-R": "décocher",
#                         "TKAOE/PREPB": "déprend",
            #lesson 56
    
                         })
    def test_lesson27_ending_sounds_tre_ntre_rtre_dre_ndre_bre_rbre_pre_rpre(self):
        self.assertSame({
            "ATS": "astre",
#            "KOPBTS": "contre",
#            "REPBDZ": "rendre",
            "SOBS": "sobre",
            "PHARBS": "marbre",
            "POURPS": "pourpre",
#            "SHREUPBDZ": "cylindre",
            "SKWREUFR": "givre",
            "WEUTS": "vitre",
            "TARTS": "tartre",
            "PHOUDZ": "moudre",
            "PHORDZ": "mordre",
            "ARBS": "arbre",
            "PROPS": "propre",
            "HREUTS": "litre",
            "ORDZ": "ordre",
            "KADZ": "cadre",
        })
        
    def test_lesson28_Kstar_for_prefix_com_and_KM_for_comm(self):
        self.assertSame({
            # 2 ways to write KPAR
            "K*/PAR": "compare", #'k§-paR'
            "K*/PHROE": "complot",
            "K*/PABGT": "compact",
            "K*/PWATS": "combattre",
#            "K*/PA*": "compas",
 #          "KPHEUBG": "communique",
            "KPH": "comme",
#            "KPHA": "comment",
            "KPHAEURS": "commerce",


        })

        
        
    def test_lesson28_FBG_for_sound_fic_and_fec(self):
        self.assertSame({"TRAFBG": "trafic",
#                         "AFBG/TE": "affecté"
                         })

        
    def test_lesson29_STPH_for_sound_sne(self):
        self.assertSame({
            "STPHOB": "snob",
            "STPHABG": "snack",
 #           "STPHEUPL": "synonyme",
#            "SPHA": "cinéma",
            "STPHEUTS": "sinistre",
 #           "STPHOPB": "sinon",
 
        })

    def test_lesson29_GSstarB_or_GZ_for_sound_tionne_and_zionne(self):
        self.assertSame({
            #"TPOPBGS": "fonction",
 #                        "STAGS/*B": "stationne",
            "STAGZ": "stationne",
 #                        "PAGS": "passion",
                         "PAGZ": "passionne",
 #                        "POEGZ": "positionne",
                         })
    def test_lesson29_GZ_for_sound_zion(self):
        self.assertSame({
            #"TKWEUGZ": "division",
                         "WEUGZ": "vision",
                         "TPUGZ": "fusion",
                #         "TPUGZ/*B": "fusionne",
                         })
    def test_lesson29_GS_for_cien_and_GZ_for_cienne(self):
        self.assertSame({
            "PHAG/EUGS": "magicien",
            "PHAG/EUGZ": "magicienne",
#            "POL/TEUGS": "politicien",
        })

    def test_lesson29_BGS_suffix_for_cation(self):
        self.assertSame({
            "WEFRBGS": "vérification",
            "KPHEUBGS": "communication",
                         })

    def test_lesson29_AO_for_diphtong_io(self):
        self.assertSame({
            "PWRAOFP": "brioche",
            "PHAOP": "myope",
            "PAOFP": "pioche",
#            "HRAOPB": "lion",
#            "KPHAOPB": "camion",

        })
    def test_lesson30_SPW_for_prefix_ent_int_end_ind(self):
        self.assertSame({
            "SPWAPBDZ": "entendre",
            "SPWORS": "entorse",
            "SPWAPBT": "entente",
            "SPWAPBGS": "intention",
#            "SPWEUBG": "indique",
            "SPWUR": "endure",
#            "SPWRER": "entrer",
            "SPWREUG": "intrigue",
            "SPWAEPB": "indien",

        })

    def test_lesson25_KH_for_sound_mne(self):
        self.assertSame({})
    def test_lesson25_KH_for_sound_mne(self):
        self.assertSame({})
    def test_lesson25_KH_for_sound_mne(self):
        self.assertSame({})
    def test_lesson25_KH_for_sound_mne(self):
        self.assertSame({})                    
    def test_prefixWords(self):
       for elem in self.prefix_word.items():
           assert elem[0] == self.steno(elem[1])


    def test_suffixWords(self):
        self.assertSame(self.suffix_word)

    def test_rightSound(self):
        self.assertSame(self.right_ch_sound)


    def assertSame(self, words):
        for elem in words.items():
           assert elem[0] == self.steno(elem[1])


           
    def test_all_tao_entry(self):
        with open('resources/tao_la_salle.json') as json_file:
            data = json.load(json_file)
        found = []
        not_found = []
        for elem in data.items():
            if elem[0] == self.steno(elem[1]):
                found.append(elem[1])
            else:
                not_found.append(elem[1])

        print("FOUND: ",found)
        print("\nNOT FOUND: ",not_found)
        assert false

            

