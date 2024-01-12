from src.generate_dictionnary import encode_syllable

import pytest

@pytest.mark.parametrize(
    ('input_w', 'expected'),
    (
        ('tasse', 'TAS'),
        ('sa', 'SA'),
        ('ta', 'TA'),
        ('su', 'SU'),
        ('ce', 'S'),
        ("c'est", 'SE'),
        ('te', 'T-'),
        ('tôt', 'TO'),
        ('tu', 'TU'),
        ('suce', 'SUS'),
        ('à', 'A'),
        ('au', 'o'),
        ('et', 'E'),
        ('eu', 'U'),
        ('a eu', 'AU'),
        ('situe', 'STU'),
        ('sot', 'SO'),
        ('sotte', 'SOT'),
        ('thé', 'TE'),
        ('us', 'US'),
    )
)
def test_lesson_one_encoding(input_w, expected):
    assert encode_syllable(input_w) == expected

@pytest.mark.parametrize(
    ('input_w', 'expected'),
    (
        ('a', 'A*'),
        ('os', 'OSZ'),
    )
)
def test_full_conflict_resolution_lesson_1(input_w, expected):
    assert encode_syllable(input_w) == expected

@pytest.mark.parametrize(
    ('input_w', 'expected'),
    (
        ('pape', 'PAP'),
        ('tape', 'TAP'),
        ('sape', 'SAP'),
        ('passe', 'PAS'),
        ('patte', 'PAT'),
        ('pot', 'PO'),
        ('puce', 'PUS')
    )
)
def test_lesson_two_encoding(input_w, expected):
    assert encode_syllable(input_w) == expected

@pytest.mark.parametrize(
    ('input_w', 'expected'),
    (
        ('ras', 'RA'),
        ('rat', 'RA*'),
        ('rue', 'RU'),
        ('rare', 'RAR'),
        ('rate', 'RAT'),
        ('race', 'RAS'),
        ('race', 'RASZ'),
        ('russe', 'RUS'),
        ('Russe', 'R*US'),
        ('part', 'PAR'),
        ('port', 'POR'),
        ('sort', 'SOR'),
        ('tort', 'TOR'),
        ('tard', 'TAR'),
        ('trace', 'TRAS'),
        ('trace', 'TRASZ'),
        ('or', 'OR'),
        ('art', 'AR'),
        ('eurent', '*UR'),
        ('pur', 'PUR'),
        ('sera', 'SRA'),
        ('serez', 'SRE'),
        ('parte', 'PART'),
        ('porte', 'PORT'),
        ('tarte', 'TART'),
        ('trotte', 'TROT'),
        ('store', 'STOR'),
        ('sorte', 'SORT'),
        ('trappe', 'TRAP'),
        ('trop', 'TRO'),
        ('Prusse', 'PR*US'),
        ('rapt', 'RAPT'),
        ('sport', 'SPOR'),
    )
)
def test_lesson_three_encoding(input_w, expected):
    assert encode_syllable(input_w) == expected

@pytest.mark.parametrize(
    ('input_w', 'expected'),
    (
        ('va', 'VA'),
        ('vue', 'VU'),
        ('vu', 'V*U'),
        ('vote', 'VOT'),
        ('rave', 'RAF'),
        ('savent', 'SAF'),
        ('vaut', 'VO*E'),
        ('veau', 'VOE'),
    )
)
def test_lesson_four_encoding(input_w, expected):
    assert encode_syllable(input_w) == expected

@pytest.mark.parametrize(
    (input_w, expected),
    (
        ("cas", "KA*"),
        ("car", "KAR"),
        ("cure", "KUR"),
        ("quai", "KE"),
        ("quatre", "KATS"),
        ("cave", "KAF"),
        ("casse", "KAS"),
        ("vol", "VOL"),
        ("pale", "PAL"),
        ("rôle", "ROEL"),
        ("cote", "KOT"),
        ("côte", "KOET"),
        ("tôle", "TOEL"),
        ("croc", "KROE"),
        ("Paul", "POL"),
        ("Paule", "PO*EL"),
        ("pôle", "POEL"),
        ("valse", "VALS"),
        ("Canada", "K*D"),
        ("y", "EU"),
        ("il", "EUL"),
        ("ou", "KWR"),
        ("vie", "WEU"),
        ("si", "SEU"),
        ("quitte", "KEUT"),
        ("kilt", "KEULT"),
        ("pie", "PEU"),
        ("pile", "PEUL"),
        ("vite", "WEUT"),
        ("site", "SEUT"),
        ("cite", "S*IT"),
        ("pipe", "PEUP"),
        ("rive", "REUF"),
        ("type", "TEUP"),
        ("pire", "PEUR"),
        ("vis", "WEUS"),
        ("visse", "W*EUS"),
        ("colle", "KOEL"),
        ("^cole", "KO*L"),
        ("cale", "KAEL"),
        ("cap", "KAP"),
        ("cape", "KAEP"),
    )
)
def test_lesson_five_encoding(input_w, expected):
    assert encode_syllable(input_w) == expected

@pytest.mark.parametrize(
    (input_w, expected),
    (
        ("haute", "HOET"),
        ("haut", "HOE"),
        ("hausse", "HOES"),
        ("hôte", "HO*ET"),
        ("huppe", "HUP"),
        ("hisse", "HEUS"),
        ("hotte", "MOT"),
        ("Hull", "HUL"),
        ("horde", "HORD"),
        ("harpe", "HARP"),
        ("ah,", "HAFPLT"),
        ("oh,", "HOFPLT"),
        ("robe", "ROB"),
        ("tube", "TUB"),
        ("canne", "KAB"),
        ("Cannes", "KA*B"),
        ("cane", "KAB/ERBGS"),
        ("ou", "KAB/*E"),
        ("can", "KAB/R-R"),
        ("vanne", "VAB"),
        ("van", "VA*B"),
        ("panne", "PAB"),
        ("sonne", "SOB"),
        ("eux", "AO"),
        ("seul", "SAOL"),
        ("ceux", "SAQ"),
        ("peur", "PAOR"),
        ("sœur", "SAOR"),
        ("cœur", "KAOR"),
        ("heure", "AOR"),
        ("creux", "KRAO"),
        ("heurte", "HAORT"),
        ("veulent", "VAGL"),
        ("peuvent", "PAOF"),
        ("hall", "MAL"),
        ("hâle", "HAUL"),
        ("hâte", "HAUT"),
        ("pâle", "PAUL"),
        ("râle", "RAUL"),
    )
)
def test_lesson_six_encoding(input_w, expected):
    assert encode_syllable(input_w) == expected
            
@pytest.mark.parametrize(
    (input_w, expected),
    (
        ("haute", "HOET"),
        ("hôte", "HO*ET"),
        ("harpe", "HARP"),
        ("apport", "ARP"),
        ("huppe", "HUP"),
        ("un peu", "UP"),
        ("pale", "PAL"),
        ("pâle", "PAUL"),
        ("veut", "VAO*"),
        ("voeu", "VAO"),
        ("cube", "K*UB"),
        ("qu'une", "KUB"),
    )
)
def test_lesson_six_disambiguation(input_w, expected):
    assert encode_syllable(input_w) == expected

@pytest.mark.parametrize(
    (input_w, expected),
    (
        ("vague", "VAG"),
        ("code", "KOD"),
        ("rude", "RUD"),
        ("sud", "SUD"),
        ("solde", "SOLD"),
        ("vogue", "VOG"),
        ("ride", "REUD"),
        ("vide", "VEUD"),
        ("Sud", "S*UD"),
        ("page", "PAG"),
        ("rage", "RAG"),
        ("sage", "SAG"),
        ("rouge", "ROUG"),
        ("raie", "RAEU"),
        ("aide", "AEUD"),
        ("trait", "TRAEU"),
        ("traite", "TRAEUT"),
        ("haie", "HAEU"),
        ("aile", "AEUL"),
        ("prête", "PRAEUT"),
        ("prêtre", "PRAEUTS"),
        ("pelle", "PAEUL"),
        ("est-ce", "AEUS"),
        ("selle", "SAEUL"),
        ("sel", "SEL"),
        ("caisse", "K-S"),
        ("Caisse", "K-S/R-R"),
        ("paire", "PAEUR"),
        ("rêve", "RAEUF"),
        ("tête", "TAEUT"),
        ("trêve", "TRAEUF"),
        ("crève", "KRAEUF"),
        ("ver", "VAEUR"),
        ("quête", "KAEUT"),
        ("presse", "PRAEUS"),
        ("sève", "SAEUF"),
        ("raide", "RAEUD"),
        ("tresse", "TRAEUS"),
        ("air", "AEUR"),
        ("sait", "SAEU"),
        ("cesse", "SAIS"),
        ("vrai", "VRAI"),
        ("prêt", "PRAI"),
        ("qu'est-ce", "KAIS"),
        ("craie", "KRAI"),
    )
)
def test_lesson_seven_encoding(input_w, expected):
    assert encode_syllable(input_w) == expected

@pytest.mark.parametrize(
    (input_w, expected),
    (
        ("sel", "SEL"),
        ("selle", "SAEUL"),
        ("père", "P-R"),
        ("paire", "PAEUR"),
        ("paraître", "PAEUTS"),
        ("paître", "PA*EUTS"),
        ("refait", "R-F"),
        ("rêve", "RAEUF"),
        ("compte", "K-T"),
        ("quête", "KAEUT"),
        ("ver", "VAEUR"),
        ("vert", "V-R"),
        ("verre", "VER"),
        ("vérité", "VERT"),
        ("verte", "V-RT"),
    )
)
def test_lesson_seven_disambiguation(input_w, expected):
    assert encode_syllable(input_w) == expected

@pytest.mark.parametrize(
    (input_w, expected),
    (
        ("rose", "ROEZ"),
        ("Rose", "RO*EZ"),
        ("seize", "SAEUZ"),
        ("rase", "RAZ"),
        ("vise", "VIZ"),
        ("aise", "AIZ"),
        ("vase", "VAZ"),
        ("cause", "KOEZ"),
        ("crise", "KRIZ"),
        ("prise", "PREUZ"),
        ("Pise", "P*EUZ"),
        ("cerise", "SRIZ"),
        ("est", "Z"),
        ("il est", "KWR-Z"),
        ("elle est", "HR-Z"),
    )
)
def test_lesson_eight_encoding(input_w, expected):
    assert encode_syllable(input_w) == expected

@pytest.mark.parametrize(
    (input_w, expected),
    (
        ("pause", "POEZ"),
        ("pose", "PO*EZ"),
        ("ri", "REU"),
        ("riz", "REUZ"),
        ("rie", "R*EU"),
        ("rose", "ROEZ"),
        ("Rose", "RO*EZ"),
    )
)
def test_lesson_eight_disambiguation(input_w, expected):
    assert encode_syllable(input_w) == expected

@pytest.mark.parametrize(
    (input_w, expected),
    (
        ("elle", "L-"),
        ("lot", "LOE"),
        ("ou", "LOT"),
        ("lu", "LU"),
        ("lire", "LIR"),
        ("lutte", "LUT"),
        ("lobe", "LOB"),
        ("celle", "SL-"),
        ("cela", "SLA"),
        ("que le", "K-L"),
        ("lac", "LAK"),
        ("loque", "LOK"),
        ("Luc", "L*UK"),
        ("roc", "ROK"),
        ("pic", "PIK"),
        ("coq", "KOK"),
        ("coke", "KOEK"),
        ("Coke", "KO*EK"),
        ("sec", "SAEUK"),
        ("sac", "SAK"),
        ("claque", "KLAK"),
        ("plaque", "PLAK"),
        ("vrac", "VRAK"),
        ("trac", "IRAK"),
        ("laisse", "LAIS"),
        ("lettre", "LAITS"),
        ("livre", "LIER"),
        ("lise", "LIZ"),
        ("Lise", "L*IZ"),
        ("loupe", "LOUP"),
        ("poupe", "POUP"),
        ("poule", "POUL"),
        ("roule", "ROUL"),
        ("route", "ROUT"),
        ("pousse", "POUS"),
        ("soupe", "SOUP"),
        ("tour", "TOUR"),
        ("lourd", "LOUR"),
        ("coupe", "KOUP"),
        ("louve", "LOUV"),
        ("roue", "ROU"),
        ("trou", "TROU"),
        ("clou", "KLOU"),
        ("tout", "TOU"),
        ("toute", "TOUT"),
        ("sous", "SOU"),
        ("sous le", "SOUL"),
        ("sous les", "SOULS"),
        ("rouge", "ROUG"),
        ("pouce", "POUSZ"),
        ("sous la", "SOULG"),
    )
)
def test_lesson_ten_encoding(input_w, expected):
    assert encode_syllable(input_w) == expected

@pytest.mark.parametrize(
    (input_w, expected),
    (
        ("port", "POR"),
        ("porc", "PORK"),
        ("pic", "PIK"),
        ("pique", "P*IK"),
        ("trac", "TRAK"),
        ("traque", "TRA*K"),
        ("elle a fait", "LAF"),
        ("lave", "LA*F"),
        ("laid", "LAI"),
        ("laide", "LAID"),
        ("lait", "LAIT"),
        ("loup", "LUP"),
        ("loue", "LO*U"),
        ("elles ont eu", "LOU"),
        ("clou", "KLOU"),
        ("cloue", "KLO*U"),
        ("proue", "PROU"),
        ("Proulx", "PRO*U"),
        ("cour", "KOUR"),
        ("court", "KO*UR"),
        ("cours", "KURS"),
        ("chlore", "KLOR"),
        ("clore", "KLO*R"),
    )
)
def test_lesson_ten_disambiguation(input_w, expected):
    assert encode_syllable(input_w) == expected

@pytest.mark.parametrize(
    (input_w, expected),
    (
        ("de", "D-"),
        ("du", "DU"),
        ("dit", "DI"),
        ("ou", "*D"),
        ("d'y", "D*I"),
        ("dose", "DOEZ"),
        ("dite", "DIT"),
        ("dîne", "DIB"),
        ("dur", "DUR"),
        ("dé", "DE"),
        ("donne", "DOB"),
        ("date", "DAT"),
        ("doute", "DOUT"),
        ("doux", "DOU"),
        ("douce", "DOUSZ"),
        ("dard", "DAR"),
        ("dos", "DDE"),
        ("dette", "DAIT"),
        ("veuve", "VAGF"),
        ("veuf", "VAOFL"),
        ("vive", "VIF"),
        ("vif", "VIFL"),
        ("accord", "A*K"),
        ("d'accord", "DA*K"),
        ("l'accord", "LA*K"),
        ("puis", "PAU"),
        ("suie", "SAU"),
        ("huile", "A*UL"),
        ("cuit", "KAU"),
        ("cuise", "KAUZ"),
        ("huit", "AUT"),
        ("celui", "SLAU"),
        ("celle-là", "SL-LG"),
        ("suive", "SAUF"),
        ("pâte", "PAUT"),
        ("a eu", "AU"),
        ("a eu la", "AULG"),
        ("luit", "LAUT"),
        ("suit", "SA*U"),
        ("suite", "SAUT"),
        ("cuite", "KAUT"),
        ("cuisse", "KAUS"),
        ("pluie", "PLAU"),
        ("celui-là", "SLAULG"),
        ("luire", "LA*UR"),
        ("suivre", "SAUFR"),
        ("râpe", "RAUP"),
        ("a eu le", "AUL"),
        ("a eu les", "AULS"),
    )
)
def test_lesson_eleven_encoding(input_w, expected):
    assert encode_syllable(input_w) == expected

@pytest.mark.parametrize(
    (input_w, expected),
    (
        ("dans le", "DAL"),
        ("dalle", "DAEL"),
        ("digue", "DIG"),
        ("dis-je", "D*IG"),
        ("a eu", "AU"),
        ("tâte", "TA*UT"),
        ("puis", "PAU"),
        ("pâte", "PAUT"),
        ("suisse", "SAUS"),
        ("cuir", "KAUR"),
        ("luit", "LAUT"),
        ("ce", "S"),
        ("lui", "A*U"),
        ("tout de suite", "TAUT"),
        ("puits", "PAUTS"),
        ("Suisse", "SA*US"),
        ("cuire", "KA*UR"),
        ("elle lui", "LA*U"),
        ("se", "SH"),
    )
)
def test_lesson_eleven_disambiguation(input_w, expected):
    assert encode_syllable(input_w) == expected

@pytest.mark.parametrize(
    (input_w, expected),
    (
        ("beau", "BO"),
        ("bord", "BOR"),
        ("beurre", "BAOR"),
        ("bulle", "BUL"),
        ("lame", "LAM"),
        ("lime", "LIM"),
        ("rame", "RAM"),
        ("âme", "AUM"),
        ("quand même", "KAM/-M"),
        ("bleu", "BLAO"),
        ("blague", "BLAG"),
        ("bloque", "BLO*K"),
        ("bas", "BA"),
        ("bague", "BAG"),
        ("boule", "BOUL"),
        ("bruit", "BRAU"),
        ("dame", "DAM"),
        ("came", "KAM"),
        ("aime", "AIM"),
        ("pâme", "PAUM"),
        ("lui-même", "A*UM"),
        ("blouse", "BLOUZ"),
        ("bloc", "BLOK"),
        ("vieux", "YAOEU"),
        ("lieu", "LAOEU"),
        ("yeux", "AOEU"),
        ("sérieux", "SRAOEU"),
        ("pieux", "PAOEU"),
        ("cieux", "SAOEU"),
        ("curieux", "KRAOEU"),
        ("précieux", "PRAOEU"),
        ("Dieu", "DAOEU"),
        ("Prieur", "PRAO*EUR"),
    )
)
def test_lesson_twelve_encoding(input_w, expected):
    assert encode_syllable(input_w) == expected

@pytest.mark.parametrize(
    (input_w, expected),
    (
        ("bar", "BAR"),
        ("barre", "BA*R"),
        ("bal", "BAL"),
        ("balle", "BA*L"),
        ("boue", "BOU"),
        ("bout", "BOUT"),
        ("ou", "BO*U"),
        ("on me", "OM"),
        ("homme", "OEM"),
        ("rhume", "RUM"),
        ("résume", "R*UM"),
        ("rhum", "ROM"),
        ("Rome", "RO*M"),
        ("demi", "DIM"),
        ("dîme", "D*IM"),
    )
)
def test_lesson_twelve_disambiguation(input_w, expected):
    assert encode_syllable(input_w) == expected

@pytest.mark.parametrize(
    (input_w, expected),
    (
        ("huitième", "AUT/A*EM"),
        ("seizième", "SAIZ/A*EM"),
        ("quatorzième", "KORZ/A*EM"),
    )
)
def test_cardinal_numbers(input_w, expected):
    assert encode_syllable(input_w) == expected

@pytest.mark.parametrize(
    (input_w, expected),
    (
        ("fîl", "FIL"),
        ("feu", "FAO"),
        ("fils", "FIS"),
        ("fa", "FA"),
        ("phare", "FAR"),
        ("frippe", "FRIP"),
        ("fer", "FER"),
        ("faute", "FOET"),
        ("fuite", "FAUT"),
        ("fond", "FON"),
        ("fume", "FUM"),
        ("fou", "FOU"),
        ("fruit", "FRAU"),
        ("fleuve", "FLAOF"),
        ("frère", "FR-R"),
        ("frais", "FRAI"),
        ("rond", "RON"),
        ("ton", "TON"),
        ("son", "SON"),
        ("un", "UN"),
        ("d'un", "DUN"),
        ("l'un", "LUN"),
        ("qu'un", "KUN"),
        ("fin", "FIN"),
        ("vin", "VIN"),
        ("pont", "PON"),
        ("ponte", "PONT"),
        ("pointe", "POINT"),
        ("fonte", "FONT"),
        ("tonte", "TONT"),
        ("tonde", "TOND"),
        ("rein", "RIN"),
        ("banc", "BAN"),
        ("blanc", "BLAN"),
        ("cran", "KRAN"),
        ("long", "LON"),
        ("plomb", "PLON"),
        ("blond", "BLON"),
        ("flux", "FLU"),
        ("reflux", "R-/FLU"),
        ("édifice", "TKWIS"),
        ("rapide", "RAPD"),
        ("pied", "PAE"),
        ("pierre", "PAER"),
        ("Pierre", "PA*ER"),
        ("pièce", "PAES"),
        ("tiers", "TAER"),
        ("lierre", "LAER"),
        ("hier", "FIAER"),
        ("tierce", "TAERS"),
        ("bielle", "BAEL"),
        ("fiel", "FAEL"),
        ("ciel", "SAEL"),
        ("financier", "FINS/AER"),
        ("caissier", "K-S/AER"),
        ("voilier", "VOIL/AER"),
        ("sablier", "SABL/AER"),
        ("financière", "FINS/A*ER"),
        ("caissière", "K-S/A*ER"),
        ("théière", "TE/A*ER"),
        ("tablier", "TABL/AER"),
        ("qui", "KR-"),
        ("qu'il a", "KRKHA"),
        ("ce qu'il a", "SKHA"),
        ("diable", "DRABL"),
        ("qui a", "KRA"),
        ("qu'elle a", "KLA"),
        ("ce qu'elle a", "SKLA"),
        ("viol", "VROL"),
        ("viole", "VRO*L"),
        ("craquait", "KRAK/-S"),
        ("passait", "PAS/-S"),
        ("courait", "KOUR/-S"),
        ("craquerait", "KRAK/-RS"),
        ("passerait", "PAS/-RS"),
        ("courrait", "KOUR/-RS"),
        ("tirait", "TIR/-S"),
        ("tiret", "TIR/AI"),
        ("filait", "FIL/-S"),
        ("filet", "FIL/AI"),
        ("sorbet", "SORB/AI"),
        ("bleuet", "BLAO/AI"),
        ("bonnet", "BOB/AI"),
        ("hoquet", "HOK/AI"),
        ("courant", "KOUR/-G"),
        ("riant", "RI/-G"),
        ("criant", "KRI/-G"),
        ("disant", "DIZ/-G"),
        ("laquelle", "LABLG"),
        ("tel quel", "TL-BLG"),
        ("de quel", "TK-BLG"),
        ("pour quel", "PR-BLG"),
        ("lequel", "L-BLG"),
        ("séquelle", "SEBLG"),
        ("trappeur", "TRARP"),
        ("voleur", "VORL"),
    )
)
def test_lesson_thirteen_encoding(input_w, expected):
    assert encode_syllable(input_w) == expected


@pytest.mark.parametrize(
    (input_w, expected),
    (
        ("fete", "FAIT"),
        ("faîte", "FA*IT"),
        ("compte", "K-T"),
        ("conte", "KONT"),
        ("comte", "KOMT"),
        ("vin", "VIN"),
        ("vingt", "VR"),
        ("sans", "SAN"),
        ("sang", "SANG"),
        ("vante", "VANT"),
        ("vente", "VENT"),
        ("rang", "RAN"),
        ("rend", "RA*N"),
        ("ou", "R*EN"),
        ("pin", "PIN"),
        ("pain", "PAIN"),
        ("dans", "DA"),
        ("dent", "DAN"),
        ("quand", "KA"),
        ("camp", "KAN"),
        ("tante", "TANT"),
        ("tente", "TENT"),
        ("qu'en", "KEN"),
        ("bière", "BAER"),
        ("banquier", "BAE"),
        ("banquière", "BA*ER"),
        ("fier", "FAER"),
        ("fière", "FA*ER"),
        ("ce qui", "SKR-"),
        ("ski", "SKI"),
        ("ferait", "F-RS"),
        ("frais", "FRAI"),
        ("forait", "FOR/-S"),
        ("forêt", "FOR/AI"),
    )
)
def test_lesson_thirteen_disambiguation(input_w, expected):
    assert encode_syllable(input_w) == expected

@pytest.mark.parametrize(
    (input_w, expected),
    (
        ("me", "M-"),
        ("me", "-M"),
        ("mis", "MI"),
        ("mie", "MI/ERBGS"),
        ("mot", "MO"),
        ("moud", "MO*U"),
        ("molle", "MOL"),
        ("meule", "MAOL"),
        ("messe", "MAIS"),
        ("mes", "MEZ"),
        ("ses", "SEZ"),
        ("malheur", "MARL"),
        ("mode", "MOD"),
        ("ma", "MA"),
        ("m'y", "M*I"),
        ("mise", "MIZ"),
        ("mou", "MOU"),
        ("moût", "MOUT"),
        ("mon", "MON"),
        ("mur", "MUR"),
        ("mess", "MES"),
        ("tes", "TEZ"),
        ("mieux", "MAOEU"),
        ("moque MOK", "(*)"),
        ("maïs", "MA/IS"),
        ("roi", "ROI"),
        ("loi", "LOI"),
        ("Roy", "RO*I"),
        ("bois", "BOI"),
        ("boîte", "BOIT"),
        ("boite", "BO*IT"),
        ("soin", "SOIN"),
        ("foin", "FOIN"),
        ("coin", "KOIN"),
        ("loin", "LOIN"),
        ("coince", "KOINS"),
        ("poindre", "POINDZ"),
        ("relevé", "R-L/VE"),
        ("degré", "D-G/R*E"),
        ("degré", "DRE"),
        ("André", "DR*E"),
        ("Caron", "KAR/*N"),
        ("melon", "M-L/*N"),
        ("Miron", "MIR/*N"),
        ("piste", "P*IS"),
        ("liste", "L*IS"),
        ("poste", "PO*S"),
        ("kyste", "K*IS"),
        ("de cet", "D*S"),
        ("de cette", "D*ES"),
        ("que cet", "K*S"),
        ("que cette", "K*ES"),
        ("pour cet", "PR*S"),
        ("pour cette", "PR*ES"),
        ("avec cet", "V*S"),
        ("avec cette", "V*ES"),
    )
)
def test_lesson_fourteen_encoding(input_w, expected):
    assert encode_syllable(input_w) == expected

@pytest.mark.parametrize(
    (input_w, expected),
    (
        ("main", "MIN"),
        ("mère", "M-R"),
        ("mer", "MER"),
        ("mètre", "MAITS"),
        ("mettre", "-MTS"),
        ("matin", "MAIN"),
        ("maire", "MAIR"),
        ("maître", "MAETS"),
        ("m'être", "M-TS"),
        ("moi", "MOI"),
        ("mois", "MAU"),
        ("mois de", "MAUD"),
        ("mois d'", "MA*UD"),
        ("foi", "FOI"),
        ("foie", "FO*I"),
        ("fois", "-FL"),
        ("autrefois", "OFL"),
        ("pois", "POI"),
        ("poids", "POIDZ"),
        ("point", "POIN"),
        ("poing", "POING"),
        ("doit", "DOI"),
        ("doigt", "DOIGT"),
        ("toi", "TOI"),
        ("toit", "TOIT"),
        ("toiture", "TOITS"),
        ("bois", "BOI"),
        ("boit", "BO*I"),
        ("ouate", "WAT"),
        ("watt", "WAUT"),
        ("-toi", "OIT"),
        ("-moi", "OIM"),
        ("z-moi", "0*IM"),
    )
)
def test_lesson_fourteen_disambiguation(input_w, expected):
    assert encode_syllable(input_w) == expected

@pytest.mark.parametrize(
    (input_w, expected),
    (
        ("nu", "NU"),
        ("nul", "NUL"),
        ("nid", "NID"),
        ("nain", "NIN"),
        ("Nice", "NISZ"),
        ("nord", "NOR"),
        ("Nord", "NO*R"),
        ("noir", "NOIR"),
        ("net", "NAIT"),
        ("noeud", "NAO"),
        ("naître", "NAITS"),
        ("noix", "NOI"),
        ("noie", "NO*I"),
        ("neuf", "NAOFL"),
        ("neuve", "NAOF"),
        ("axe", "AX"),
        ("taxe", "TAX"),
        ("luxe", "LUX"),
        ("fixe", "FIX"),
        ("boxe", "BOX"),
        ("box", "BO*X"),
        ("nerf", "NAIR"),
        ("fax", "FAX"),
        ("ne", "H-"),
        ("ne le", "H-L"),
        ("n'est pas", "HEPS"),
        ("n'est plus", "HEP"),
        ("n'avez", "HEF"),
        ("vous n'avez", "WHEF"),
        ("ni", "HI"),
        ("OUI", "AOU"),
        ("ouïe", "AOU/ERBGS"),
        ("voir-dire", "VOIRDZ"),
        ("Louis", "LAO*U"),
        ("ouï-dire", "AOUDZ"),
        ("Louise", "LAO*UZ"),
        ("Trouvez", "TROUF/*EZ"),
        ("parlez", "PARL/*EZ"),
        ("trouverez", "TROUF/R*EZ"),
        ("parlerez", "PARL/R*EZ"),
    )
)
def test_lesson_fifteen_encoding(input_w, expected):
    assert encode_syllable(input_w) == expected

@pytest.mark.parametrize(
    (input_w, expected),
    (
        ("pris", "PRI"),
        ("né", "N*E"),
        ("nid", "NID"),
        ("haie", "HAI"),
        ("neuf", "NAOFL"),
        ("dix", "DIX"),
        ("tout", "TOU"),
        ("voie", "VOI"),
        ("prix", "PRIX"),
        ("nez", "NE"),
        ("nie", "N*I"),
        ("n'ait", "HA*I"),
        ("neuf", "N-FL"),
        ("toux", "TOUX"),
        ("voix", "VOIX"),
        ("prie", "PR*I"),
        ("en y", "NI"),
        ("en sont", "NOS"),
        ("noce", "NOSZ"),
        ("fasse", "FAS"),
        ("face", "FASZ"),
    )
)
def test_lesson_fifteen_disambiguation(input_w, expected):
    assert encode_syllable(input_w) == expected

@pytest.mark.parametrize(
    (input_w, expected),
    (
    )
)
def test_lesson_sixteen_encoding(input_w, expected):
    assert encode_syllable(input_w) == expected
