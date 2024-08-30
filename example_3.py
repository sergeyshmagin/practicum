class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    # ciper_text: list = []

    def __init__(self) -> None:
        # self.ciper_text = []
        pass

    def cipher(self, original_text, shift: int):
        # Метод должен возвращать зашифрованный текст
        # с учетом переданного смещения shift.
        ciper_text = []

        for i in range(len(list(original_text))):
            if str.lower(original_text[i]) in (' ', ',', '!', '?', '.'):
                ciper_text.append(original_text[i])
            else:
                cip_idx = int(self.alphabet.find(
                    str.lower(original_text[i]))) + shift
                if cip_idx >= 32:
                    cip_idx = cip_idx - 32
                else:
                    cip_idx = cip_idx
            ciper_text.append(self.alphabet[cip_idx])
        return (''.join(ciper_text))

#        print(self.ciper_text)

    def decipher(self, cipher_text, shift):
        # с учётом переданного смещения shift.
        ...


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    # original_text='ЯЯЯЯЯ',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))
