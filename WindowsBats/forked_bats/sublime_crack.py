import sys
import os

NOP = 0x90
offsets_and_values = {
    0x00030170: 0x00,
    0x000A94D0: NOP, 0x000A94D1: NOP, 0x000A94D2: NOP, 0x000A94D3: NOP, 0x000A94D4: NOP, 0x000A94D5: NOP, 0x000A94D6: NOP, 0x000A94D7: NOP, 0x000A94D8: NOP, 0x000A94D9: NOP, 0x000A94DA: NOP, 0x000A94DB: NOP, 0x000A94DC: NOP, 0x000A94DD: NOP, 0x000A94DE: NOP, 0x000A94DF: NOP, 0x000A94E0: NOP, 0x000A94E1: NOP, 0x000A94E2: NOP, 0x000A94E3: NOP, 0x000A94E4: NOP, 0x000A94E5: NOP, 0x000A94E6: NOP, 0x000A94E7: NOP, 0x000A94E8: NOP, 0x000A94E9: NOP, 0x000A94EA: NOP, 0x000A94EB: NOP, 0x000A94EC: NOP, 0x000A94ED: NOP, 0x000A94EE: NOP, 0x000A94EF: NOP, 0x000A94F0: NOP, 0x000A94F1: NOP, 0x000A94F2: NOP, 0x000A94F3: NOP, 0x000A94F4: NOP, 0x000A94F5: NOP, 0x000A94F6: NOP, 0x000A94F7: NOP, 0x000A94F8: NOP, 0x000A94F9: NOP, 0x000A94FA: NOP, 0x000A94FB: NOP, 0x000A94FC: NOP, 0x000A94FD: NOP, 0x000A94FE: NOP, 0x000A94FF: NOP, 0x000A9500: NOP, 0x000A9501: NOP, 0x000A9502: NOP, 0x000A9503: NOP, 0x000A9504: NOP, 0x000A9505: NOP, 0x000A9506: NOP, 0x000A9507: NOP, 0x000A9508: NOP, 0x000A9509: NOP, 0x000A950A: NOP, 0x000A950B: NOP, 0x000A950C: NOP, 0x000A950D: NOP, 0x000A950E: NOP, 0x000A950F: NOP,
    0x001C6CCD: 0x02,
    0x001C6CE4: 0x00,
    0x001C6CFB: 0x00,
}

def patch_exe(input_file, output_file=None):
    output_file = output_file or f"{os.path.splitext(input_file)[0]}_patched.exe"
    try:
        with open(input_file, 'rb') as f:
            data = f.read()
        patched_data = bytearray(data)
        for offset, value in offsets_and_values.items():
            if offset < len(patched_data):
                patched_data[offset] = value
        with open(output_file, 'wb') as f:
            f.write(patched_data)
        print(f"[+] Patch applied successfully! Saved as: {output_file}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python patcher.py <input_file> [output_file]")
    else:
        patch_exe(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)