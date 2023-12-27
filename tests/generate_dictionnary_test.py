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
    )
)
def test_lesson_four_encoding(input_w, expected):
    assert encode_syllable(input_w) == expected
