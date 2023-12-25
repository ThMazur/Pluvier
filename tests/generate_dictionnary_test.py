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