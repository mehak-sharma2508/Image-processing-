import cv2


# ==================== RLE ENCODE ====================

def rle_encode(data):
    encoding = []

    if not data:
        return encoding

    prev = data[0]
    count = 1

    for pixel in data[1:]:
        if pixel == prev:
            count += 1
        else:
            encoding.append((prev, count))
            prev = pixel
            count = 1

    encoding.append((prev, count))

    return encoding


# ==================== RLE DECODE ====================

def rle_decode(encoding):
    data = []

    for value, count in encoding:
        data.extend([value] * count)

    return data


# ==================== LZW COMPRESS ====================

def lzw_compress(uncompressed):

    dict_size = 256

    dictionary = {
        bytes([i]): i for i in range(dict_size)
    }

    w = b""
    compressed = []

    for k in uncompressed:

        c = bytes([k])
        wc = w + c

        if wc in dictionary:
            w = wc

        else:
            compressed.append(dictionary[w])

            dictionary[wc] = dict_size
            dict_size += 1

            w = c

    if w:
        compressed.append(dictionary[w])

    return compressed


# ==================== LZW DECOMPRESS ====================

def lzw_decompress(compressed):

    dict_size = 256

    dictionary = {
        i: bytes([i]) for i in range(dict_size)
    }

    if not compressed:
        return []

    w = bytes([compressed.pop(0)])

    result = bytearray(w)

    for k in compressed:

        if k in dictionary:
            entry = dictionary[k]

        elif k == dict_size:
            entry = w + w[:1]

        else:
            raise ValueError("Bad compressed k")

        result += entry

        dictionary[dict_size] = w + entry[:1]

        dict_size += 1

        w = entry

    return list(result)


image_path = "/Users/vikas/PBL/flower.jpg"

img = cv2.imread(
    image_path,
    cv2.IMREAD_GRAYSCALE
)

if img is None:
    raise FileNotFoundError(
        "Image not found. Check the image path."
    )


# Convert image into 1D list

pixels = img.flatten().tolist()


rle_encoded = rle_encode(pixels)

# Approximate size
rle_size_bytes = len(rle_encoded) * 2

# Decode and verify
rle_decoded = rle_decode(rle_encoded)

assert rle_decoded == pixels, \
    "RLE decompression failed!"


lzw_encoded = lzw_compress(pixels)

# Approximate size
lzw_size_bytes = len(lzw_encoded) * 2

# Decode and verify
lzw_decoded = lzw_decompress(
    lzw_encoded.copy()
)

assert lzw_decoded == pixels, \
    "LZW decompression failed!"


original_size_bytes = len(pixels)

rle_ratio = (
    original_size_bytes / rle_size_bytes
)

lzw_ratio = (
    original_size_bytes / lzw_size_bytes
)

print("\n========== COMPRESSION RESULTS ==========")

print(
    "Original Image Size:",
    original_size_bytes,
    "bytes"
)

print(
    "RLE Compressed Size:",
    rle_size_bytes,
    "bytes"
)

print(
    "LZW Compressed Size:",
    lzw_size_bytes,
    "bytes"
)

print(
    f"RLE Compression Ratio: "
    f"{rle_ratio:.2f}:1"
)

print(
    f"LZW Compression Ratio: "
    f"{lzw_ratio:.2f}:1"
)


cv2.imshow(
    "Original Image || MEHAK",
    img
)

cv2.waitKey(0)
cv2.destroyAllWindows()