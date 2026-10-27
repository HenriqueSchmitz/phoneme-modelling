from phoneme_modelling.phonemes import ALTERNATIVE_IPA


def clean_ipa(ipa: str) -> str:
    ipa = ipa.replace(" ", "")
    ipa = ipa.replace("_", "")
    if ipa in ALTERNATIVE_IPA:
        ipa = ALTERNATIVE_IPA.get(ipa, ipa)
    return ipa