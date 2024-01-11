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
def test_lesson_ten_encoding(input_w, expected):
    assert encode_syllable(input_w) == expected
