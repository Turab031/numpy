# final_decode.py
# Fully automatic pulseprint decoder for Small‑E / whitespace challenge

def extract_bits(filename):
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        data = f.read()

    bits = ""
    i = 0
    while i < len(data) - 1:
        if data[i] == '.' and data[i+1] == '\t':
            bits += '1'
            i += 2
        elif data[i] == '.' and data[i+1] == ' ':
            bits += '0'
            i += 2
        else:
            i += 1

    return bits


def decode_with_alignment(bits):
    candidates = []

    for offset in range(8):
        out = ""
        for i in range(offset, len(bits), 8):
            byte = bits[i:i+8]
            if len(byte) == 8:
                val = int(byte, 2)
                if 32 <= val <= 126:
                    out += chr(val)
        candidates.append(out)

    return candidates


if __name__ == "__main__":
    INPUT_FILE = "pulse.txt"
    OUTPUT_FILE = "flag.txt"

    bits = extract_bits(INPUT_FILE)
    results = decode_with_alignment(bits)

    # Save all attempts
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for idx, text in enumerate(results):
            f.write(f"OFFSET {idx}:\n{text}\n\n")

    print("✅ Decoding complete.")
    print("📄 Check flag.txt")

    # Also print the one containing HQX
    for text in results:
        if "HQX{" in text:
            print("\n🎯 FLAG FOUND:\n")
            print(text)
