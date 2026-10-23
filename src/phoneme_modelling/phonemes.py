from enum import Enum

class IpaRepresentations(Enum):
    R = "ɹ"
    S = "s"
    G = "g"
    B = "b"
    Z = "z"
    L = "l"
    TH_VOICED = "ð"
    TH_VOICELESS = "θ"
    SH = "ʃ"
    CH = "tʃ"
    K = "k"
    V = "v"
    J = "dʒ"
    T = "t"
    D = "d"
    F = "f"
    NG = "ŋ"
    Y = "j"
    W = "w"
    H = "h"
    N = "n"
    M = "m"
    P = "p"

TEXT_TO_IPA = {}
for member in IpaRepresentations:
    TEXT_TO_IPA[member.name.upper()] = member.value
    TEXT_TO_IPA[member.name.lower()] = member.value

IPA_TO_TEXT = {member.value: member.name.lower() for member in IpaRepresentations}

VALID_SOUND_TEXTS = set()
for member in IpaRepresentations:
    VALID_SOUND_TEXTS.add(member.name.upper())
    VALID_SOUND_TEXTS.add(member.name.lower())

VALID_IPA_STRINGS = set([member.value for member in IpaRepresentations])
