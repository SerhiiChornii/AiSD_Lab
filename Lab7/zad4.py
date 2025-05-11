wzor = 'sun'
tekst = 'thesunriseatsunset'

hash_wzor = sum(map(ord, wzor)) % 101

start = 0
end = start + 3

for i in range(len(tekst)-end+1):
    frag = tekst[start:end]
    s = sum(map(ord, tekst[start:end]))
    h = s % 101
    print(f"{frag}\t{s}\t{h}")
    if h == hash_wzor:
        print(f"{wzor} == {frag}: {wzor == frag}")
        if wzor == frag: print(start)
    start += 1
    end += 1