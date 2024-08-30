class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    def cipher(self, original_text, shift: int):
        # Метод должен возвращать зашифрованный текст
        # с учетом переданного смещения shift.
        ciper_out = []

        for i in range(len(original_text)):
            if str.lower(original_text[i]) not in (self.alphabet):
                ciper_out.append(original_text[i])
            else:
                cip_idx = self.alphabet.find(str.lower(original_text[i]))
                cip_shifted = cip_idx + shift
                if cip_shifted > 32:
                    cip_shifted -= 33
                ciper_out.append(self.alphabet[cip_shifted])

        return (''.join(ciper_out))

    def decipher(self, cipher_text, shift):
        orig_out = []
        # plain_text_idx = shift
        for i in range(len(cipher_text)):
            if str.lower(cipher_text[i]) not in (self.alphabet):
                orig_out.append(cipher_text[i])
            else:
                cip_idx = self.alphabet.find(str.lower(cipher_text[i]))
                cip_shifted = cip_idx + shift
                if cip_shifted > 32:
                    cip_shifted -= 33
 
                orig_out.append(self.alphabet[cip_shifted])
        return (''.join(orig_out))
        # с учётом переданного смещения shift.
        ...


cipher_master = CipherMaster()
#сткънр тждюа д ъкцтрдвппро дкёж. мвижфуб, пву твуумтэнк!
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Уфмьпт фиёав ё ьмшфтёдсстр ёмзи. Одкицхг, сдх фдххофяпм!',
    # cipher_text='абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
    shift=4
))
