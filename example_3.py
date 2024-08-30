class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text: str, shift: int, is_encrypt: bool):
        
        ciper_out = []

        # с учётом переданного смещения shift.
        for i in range(len(text)):
            if str.lower(text[i]) not in (self.alphabet):
                ciper_out.append(text[i])
            else:
                cip_idx = self.alphabet.find(str.lower(text[i]))
                if is_encrypt is True:
                    cip_shifted = cip_idx + shift
                else:
                    cip_shifted = cip_idx - shift

                if cip_shifted > 32:
                    cip_shifted -= 33
                ciper_out.append(self.alphabet[cip_shifted])

        return (''.join(ciper_out))


# Проверка
cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
))
