from phoneme_modelling.phonemes import ALTERNATIVE_IPA


STRINGS_TO_REMOVE_FROM_IPA = [" ", "_", "▁"]


def clean_ipa(ipa: str) -> str:
    for text in STRINGS_TO_REMOVE_FROM_IPA:
        ipa = ipa.replace(text, "")
    if ipa in ALTERNATIVE_IPA:
        ipa = ALTERNATIVE_IPA.get(ipa, ipa)
    return ipa