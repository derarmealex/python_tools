# PRINT ALL CHARACTERS OF ASCII
for x in range(0, 256):
    print(f'{x}: {chr(x)}\t', end='')
# CONVERTION TO ASCII SYMBOLS AND BACK
# bytearray() == bytes()
S = "The quick brown fox jumps over the lazy dog."

x = [ord(char) for char in S]
print(x)                                            # [84, 104, 101, 32, 113, 117, ...
# or
x = bytearray(S, 'utf-8')
#x = bytearray(S)
print(x)                                            # bytearray(b'The quick brown fox jumps over the lazy dog.')
print(list(x))                                      # [84, 104, 101, 32, 113, 117, ...
# or
#S = b'The quick brown fox jumps over the lazy dog.'
#print(list(S))                                      # [84, 104, 101, 32, 113, 117, ...

print([chr(char) for char in x])                    # ['T', 'h', 'e', ' ', 'q', 'u', 'i', 'c', 'k', ' ', 'b', ...
print(*[chr(char) for char in x])                   # T h e   q u i c k   b r o w n  ...
print(''.join([chr(char) for char in x]))           # The quick brown fox jumps over the lazy dog.

stg = 12
stg2 = 'Time is 12 a.m.'
lst = [1, 2, 5, 9, 0, 99]
lst2 = ['1', '2', '5', '9', '0', '99']

a = bytearray(stg)                                  # bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
b = bytearray(stg2, 'utf-8')                        # bytearray(b'Time is 12 a.m.')
c = bytearray(lst)                                  # bytearray(b'\x01\x02\x05\t\x00c')
#d = bytearray(lst2)                                 # TypeError
print(list(a))                                      # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(list(b))                                      # [84, 105, 109, 101, 32, 105, 115, 32, 49, 50, 32, 97, 46, 109, 46]
print(list(c))                                      # [1, 2, 5, 9, 0, 99]
