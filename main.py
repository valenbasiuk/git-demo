#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys


def run_script(script_path: Path) -> None:
    try:
        subprocess.run([sys.executable, str(script_path)], check=True)
    except subprocess.CalledProcessError as e:
        print(f"error {e.returncode}")
    except FileNotFoundError:
        print(f"mmm.. no se encontro {script_path}")


def main() -> None:
    base = Path(__file__).parent
    scripts = [
        ("hola.py", "hola mundo"),
        ("calculadora.py", "calculadora"),
        ("snake.py", "snake!"),
        ("branch.py", "rama develop"),
    ]

    while True:
        print("\nmenú principal")
        for i, (name, desc) in enumerate(scripts, start=1):
            print(f"{i}- {name} — {desc}")
        print("0- salir")

        choice = input("elige una opción: ").strip()
        if choice == "0":
            print("saliendo del programa...")
            break
        if not choice.isdigit():
            print("opcion invalida! intenta otra vez..")
            continue

        idx = int(choice) - 1
        if not (0 <= idx < len(scripts)):
            print("opcion fuera del rango!")
            continue

        script_name = scripts[idx][0]
        script_path = base / script_name
        print(f"ejecutando {script_name}...")
        run_script(script_path)


if __name__ == "__main__":
    main()
