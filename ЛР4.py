from collections import Counter
import heapq




class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(char_freq):
    heap = [HuffmanNode(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        internal = HuffmanNode(None, left.freq + right.freq)
        internal.left = left
        internal.right = right
        
        heapq.heappush(heap, internal)
    
    return heap[0]

def generate_huffman_codes(node, code="", codes=None):
    if codes is None:
        codes = {}
    
    if node is None:
        return codes
    
    if node.char is not None:
        codes[node.char] = code
        return codes
    
    generate_huffman_codes(node.left, code + "0", codes)
    generate_huffman_codes(node.right, code + "1", codes)
    
    
    return codes

def decode(encoded_text, huffman_codes):
    reverse_codes = {code: char for char, code in huffman_codes.items()}
    
    decoded = ''
    current_code = ""
    
    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded += reverse_codes[current_code]
            current_code = ""
    
    return decoded

text = """Ах, не говорите мне про Австрию! Я ничего не понимаю, может быть, но Австрия никогда не хотела и не хочет войны. Она предает нас. Россия одна должна быть спасительницей Европы. Наш благодетель знает свое высокое призвание и будет верен ему. Вот одно, во что я верю. Нашему доброму и чудному государю предстоит величайшая роль в мире, и он так добродетелен и хорош, что Бог не оставит его, и он исполнит свое призвание задавить гидру революции, которая теперь еще ужаснее в лице этого убийцы и злодея. Мы одни должны искупить кровь праведника. На кого нам надеяться, я вас спрашиваю?.. Англия с своим коммерческим духом не поймет и не может понять всю высоту души императора Александра. Она отказалась очистить Мальту. Она хочет видеть, ищет заднюю мысль наших действий. Что они сказали Новосильцеву? Ничего. Они не поняли, они не могли понять самоотвержения нашего императора, который ничего не хочет для себя и все хочет для блага мира. И что они обещали? Ничего. И что обещали, и того не будет! Пруссия уже объявила, что Бонапарте непобедим и что вся Европа ничего не может против него... """

char_freq = dict(Counter(text))

root = build_huffman_tree(char_freq)
huffman_codes = generate_huffman_codes(root)

encoded_text = ''.join(huffman_codes[char] for char in text)

print(huffman_codes)

print("Закодированный текст:")
print(encoded_text)
print()

decoded_text = decode(encoded_text, huffman_codes)

print("Декодированный текст:")
print(decoded_text)