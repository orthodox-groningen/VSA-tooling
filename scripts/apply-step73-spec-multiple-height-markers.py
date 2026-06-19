from pathlib import Path

def main():
    required = [
        Path("docs/spec/vsa-height-markers.md"),
        Path("docs/architecture/height-marker-model.md"),
    ]
    print("Stap 73 - specificatie meerdere hoogte-markeringen")
    for path in required:
        print(f"- {path}: {'OK' if path.exists() else 'ONTBREEKT'}")
    print()
    print("Geen codewijziging toegepast.")
    print("Deze stap legt eerst syntax, semantiek en architectuur vast.")

if __name__ == "__main__":
    main()
