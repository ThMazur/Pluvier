LEXICON_PATH = "resources/lexique383.tsv"
SIMPLE_STRUCTURE = ['C', 'CV', 'CVC', 'V', 'VC']
VOWELS = {
    "a": "A",       # chat
    "e": "E",       # clé
    "2": "AO",      # eux
    "9": "AO",      # seul
    "E": "AEU",     # père
    "i": "EU",      # lit
    "o": "OE",      # haut
    "O": "O",       # mort
    "y": "U",       # cru
    "u": "OU",      # mou
    "5": "EUFR",    # vin
    # *N is used for "on" (§) endings. # TODO this is a vowel, but only on word endings

}

DIPHTONGS = {
    "8i": "AU",     # pluie
    "j2": "AOEU",   # vieux
    "je": "AE",     # pied
    "ja": "RA",     # cria
    "jo": "RO",     # bio
    "jO": "ROE",    # fjord # TODO unsure
    "jo": "AO",     # bio # TODO Some conflict there. "-R can be read as i" (above), but the diphtongs are more important I guess?
    "jO": "AO",     # fjord
    "j§": "AO",     # av_ion_
    "wa": "OEU",    # froid
    "w5": "OEUPB",  # loin
    "wi": "AOU",    # oui
    "j5": "AEPB",   # chien
    "ey": "EU",     # r_éu_nion
    "ya": "WA",     # suave
    "ij": "-LZ",    # bille # TODO Maybe not a diphtong, but a word ending/consonant thing
}

CONSONANTS_LHS = {
    "b": "PW",      # bonjour
    "d": "TK",      # dans
    "f": "TP",      # faire, phare
    "g": "TKPW",    # gare
    "k": "K",       # quoi, car
    "l": "HR",      # la
    "m": "PH",      # mais
    "n": "TPH",     # ne
    "p": "P",       # père
    "R": "R",       # rouge
    "s": "S",       # super
    "S": "SH",      # chien
    "t": "T",       # toi
    "v": "W",       # vous
    "8": "W",       # huit
    "j": "KWR",     # hier
    "z": "SWR",     # zone
    "Z": "SKWR",    # je
}

CONSONANT_PAIRS_LHS = {
    "gz": "KP",
    "ps": "S",
    "pn": "TPH",
    "kw": "KW",
    "tS": "SK",         # TODO: I'd rather deviate and use KH if possible
}

SOUNDS_LHS = {
    "de": "STK",
    "def": "STKW",
}

CONSONANTS_RHS = {
    "v": "F",
    "l": "L",
    "b": "B",
    "n": "B",
    "g": "G",
    "d": "D",
    "z": "Z",
    "k": "BG",
    "l": "FL",      # TODO When is "l" FL or L?
    "m": "PL",
    "n": "PB",      # TODO This doubles the "n" = "B" from earlier. Might be in only certain pre-defined cases like AIB = "aine"
    "Z": "G",
    "S": "FP",
    "N": "PG",
    "v": "F",
    "v": "F",

}

CONSONANT_PAIRS_RHS = {
    "tR": "TS",
    "st": "*S",
    "ks": "BGS",
    "bZ": "PBLG",
    "dZ": "PBLG",
    "sm": "FLP",
    "st": "*S",
    "bZ": "PBLG",
    "kR": "RBG",
    "vR": "FR",
    "fR": "FR",
    "rS": "FRPB",
    "kR": "RBG",
    "kR": "RBG",
    "kR": "RBG",
}

SOUNDS_RHS = {
    "En": "AIB",
    "wan": "OIB",
    "jEn": "AEB",
    "win": "AOUB",
    "zj§": "GZ",
    "sj§": "GZ",
    "z§": "GZ",
    "sjOn": "GZ",   # TODO This might conflict with "zj§" just above. The rule says "either `-GS/*B` or `-GZ`*
    "zjOn": "GZ",
    "@b": "AFRB",   # jambe
    "5b": "EUFRB",  # limbe
    "§b": "OFRB",   # tombe
    "@bl": "AFRBL", # tremble
    "1bl": "EUFRBL",  # humble
    "§bl": "OFRBL",  # comble
    "@bR": "AFRBS",   # ambre
    "5bR": "EUFRBS",  # timbre
    "§bR": "OFRBS",   # ombre
    "@pR": "AFRPS",
    "5pR": "EUFRPS",
    "§pR": "OFRPS",
    "@sj§": "APBGS",    # p_ension_
    "5sj§": "EUPBGS",    # p_incions_
    "§sj§": "OPBGS",    # pron_oncions_
    "@ksj§": "APBGS",    # san_ction_
    "5ksj§": "EUPBGS",    # dist_inction_
    "§ksj§": "OPBGS",    # j_onction_
    "ksj§": "*BGS",     # a_ction_
    "isjOn": "EUGZ",
    "tR": "TS",
    "tER": "TS",
    "tyR": "TS",
    #  "Et": "*T",      # TODO: "Et" is covered by `AIT`, I don't get this. Maybe orthographic for "ette".
    "isjOn": "EUGZ",
    "isjOn": "EUGZ",
}

BRIEFS = {
    'ST-': 'cet',
    'SET': 'cette',
    '-T': 'très',
    '-TS': 'être',
    'STE': 'société',
    'STO': "c'est au",
    "STA": "c'est à",
    'S*S': "c'est cet",
    'S*ES': "c'est cette",
    'AS': 'à ce',
    'ET': 'été',
    'AET': 'a été',
    'TWAET': 'tu as été',
    'S-T': "c'est très",
    # Lesson 2
    'P-T': 'président',
    'PET': 'présidente',
    'P-': 'par',
    '-P': 'plus',
    '-PS': 'pas',
    'P-S': 'par ce',
    'UP': 'un peu',
    'UP-P': 'un peu plus',
    'STUP': "c'est un peu",
    'STO': "c'est au",
    'STA': "c'est à",
    'T-P': 'transport',
    'T-PT': 'transporte',
    '-PTS': "peut-être",
    '-PT': "peut-être",
    # Lesson 3
    'R-P': 'respect',
    'R-PT': 'respecte',
    'PR-': 'pour',
    'PROPT': 'propriété',
    'PR-R': 'premier',
    'PRER': 'première',
    'ART': 'arrête',
    'TR-': 'intérêt',
    'TR-S': 'intéresse',
    'ARS': 'adresse',
    'RART': 'rareté',
    'ARP': 'apport',
    'ARPT': 'apporte',
    'PAORT': 'apporte',
    'RARP': 'rapport',
    'RARPT': 'rapporte',
    'RAORT': 'rapporte',
    'PARP': 'participe',
    'SPAR': 'sépare',
    'PRUS': 'processus',
    'PRUR': 'procure',
    'STRO': "c'est trop",
    'REPT': 'répète',
    # Lesson 4
    'VEF': 'vous avez',
    'VEFS': 'avez-vous',
    'V-T': 'vous êtes',
    'T-FS': 'êtes-vous',
    'V-': 'avec',
    '-FS': 'vous',
    'V-FS': 'avec vous',
    '-FR': 'faire',
    'AFR': 'affaire',
    'T-FR': 'transfert',
    'P-FR': 'parfaire',
    '-F': 'fait',
    '-FT': 'faite',
    'TW-F': 'tu fais',
    'TWAF': 'tu as fait',
    'R-F': 'refait',
    'R-FR': 'refaire',
    'P-F': 'parfait',
    'P-FT': 'parfaite',
    'AF': 'a fait',
    'AFT': 'a faite',
    'AEF': 'a été fait',
    'AEFT': 'a été faite',
    'OEF': 'ont été faits',
    'OEFT': 'ont été faites',
    'SO*': 'sont',
    'SOF': 'sont faits',
    'SOFT': 'sont faites',
    '-FTS': 'votre',
    'V-FTS': 'avec votre',
    'S-FTS': "c'est votre",
    'V-P': 'vice-président',
    'VEP': 'vice-présidente',
    'PR-FS': 'pour vous',
    'R-FS': 'rendez-vous',
    'TAF': 'tous à fait',
    'VURT': 'vertu',
    'OERT': 'autorité', 
    'SR-P': 'surplus', 
    'TRO*E': 'Ontario', 
    'TRO*ET': 'Toronto', 
    'P*UT': 'percute', 
    'TWA': 'tu as', 
    'TWAU': 'tu as eu', 
    'TWAET': 'tu as été', 
    'TWAF': 'tu as fait', 
    'SP-F': "c'est parfait", 
    # Lesson 5
    "-LS": "les",
    "K-L": "que les",
    "K-L": "que le",
    "K-LG": "que la",
    "ALT": "a-t-il",
    "SRALT": "sera-t-il",
    "-FLT": "fait-il",
    "KWEF": "que vous avez",
    "SKWEF": "ce que vous avez",
    "KW-T": "que vous êtes",
    "KR-": "qui",
    "KRA": "qui a",
    "KRAU": "qui a eu",
    "A*UT": "as-tu",
    "-L": "le",
    "-LS": "les",
    "-LG": "la",
    "SR-L": "sur le",
    "SR-LS": "sur les",
    "SR-LG": "sur la",
    "PR-L": "pour le",
    "PR-LS": "pour les",
    "PR-LG": "pour la",
    "AL": "à le",
    "ALS": "à les",
    "ALG": "à la",
    "P-L": "par le",
    "P-LS": "par les",
    "P-LG": "par la",
    "S-L": "c'est le",
    "S-LS": "c'est les",
    "S-LG": "c'est la",
    "W-L": "avec le",
    "W-LS": "avec les",
    "W-LG": "avec la",
    "TEU": "petit",
    "TEUT": "petite",
    "RULT": "résulte",
    "RAULT": "résultat",
    "R-L": "réel",
    "R-LT": "réalité",
    "TIL": "utile",
    "PRAL": "provincial",
    "SWREUS": "service",
    "PREUS": "premier ministre",
    "PREUP": "principe",
    "S-K": "ce que",
    "K-": 'que',
    "KA": 'quand',
    "KO": "qu'au",
    # Lesson 6
    "-B": "bien",
    "-BT": "bientôt",
    "-BL": "meuble",
    "IBL": "immeuble",
    "S-B": "c'est bien",
    "RAOR": "erreur",
    "KEB": "Québec",
    "POB": "possible",
    "SPOB": "c'est possible",
    "PROB": "probable",
    "SPROB": "c'est probable",
    "-BTS": "bien-être",
    "VUE": "véhicule",
    "PROL": "parole",
    "PRAOR": "procureur",
    # Lesson 7
    "-RG": "régulier",
    "REG": "régulière",
    "SUG": "suggère",
    "ORG": "organise",
    "PARG": "paragraphe",
    "R*ID": "réside",
    "PR*EUD": "préside",
    "-T/-B": "très bien",
    "APD": "après-midi",
    "AFD": "avant-midi",
    "IRG": "irrégulier",
    "ALT": "a-t-il",
    "ELT": "est-il",
    "TR-": "intérêt",
    "TR-S": "intéresse",
    "AEPT": "accepte",
    "TWA": "tu as",
    "TWA*": "Ottawa",
    "K*R": "Caire",
    "OURBGS": "où",
    "SWRAEU": "c'est vrai",
    "SPOB": "c'est possible",
    "TUL": "tu le",
    "TULG": "tu la",
    "TULS": "tu les",
    # Lesson 8
    "KORZ": "quatorze",
    "OERZ": "autorise",
    "SPRI": "surpris",
    "SPRIZ": "surprise",
    "TILZ": "utilise",
    "-FZ": "vos",
    "TW-FZ": "tu vas",
    "KWR-FZ": "il va",
    # Lesson 10
    "PL": "plusieurs",
    "PLUT": "plutôt",
    "K-K": "qu'est-ce que",
    "RARK": "remarque",
    "V-L": "avec le",
    "V-LS": "avec les",
    "SLA*IR": "ça a l'air",
    "SHO*UK": "Sherbrooke",
    "TOUK": "tout à coup",
    "AKZ": "accuse",
    "LIBT": "liberté",
    "PLUP": "plupart",
    "P-K": "parce que",
    "-K": "est-ce que",
    "RORK": "remorque",
    "V-LG": "avec la",
    "SLAIR": "salaire",
    "L-FS": "elle vous",
    "PRAIK": "pratique",
    "OEK": "O.k.",
    "LARL": "latéral",
    "SPAK": "spectacle",
    "HOEK": "hockey",
    "KLARL": "collatéral",
    "AOT": "auto",
    "AOK": "automatique",
    "AOBS": "autobus",
    "RAOUT": "autoroute",
    "L": "elle",
    "LA": "elle a",
    "HR-Z": "elle est",
    "OUR": "autour",
    "ROUR": "retour",
    "POUT": "partout",
    "SROUT": "surtout",
    "L-F": "elle fait",
    "LAF": "elle a fait",
    "LORK": "lorsque",
    "UK": "unique",
    "AIRK": "article",
    "SVOUP": "s'il vous plaît",
    "PLIR": "plaisir",
    "KLUL": "calcul",
    "PUK": "public",
}
