vowels = "aiueo"

ip_str = "Halo nama Saya Muh Reza Pahlevi, Saya sedang belajar Matematika"

ip_str = ip_str.casefold()

count = {}.fromkeys(vowels, 0)

for char in ip_str:
    if char in count:
        count[char] += 1

print(count)