import argparse
from pathlib import Path
from src.lib.text import tokenize, count_freq, top_n


def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    file_path = Path(args.input)
    if not file_path.exists():
        parser.error("Файл не найден")

    if args.command == "cat":
        with open(file_path, "r", encoding="utf-8") as f:
            number = 0
            for lines in f:
                line = lines.rstrip("\n")
                if args.n:
                    number += 1
                    print(f"{number}: {line}")
                else:
                    print(line)
    elif args.command == "stats":
        if args.top <= 0:
            parser.error("аргумент top - положительное число")
        with open(file_path, "r", encoding="utf-8") as f:
            lines = [i for i in f]
            if not lines:
                parser.error("Файл пустой")
            tokens = tokenize("".join(lines))
            frequency = count_freq(tokens)
            top_of_words = top_n(frequency, n=args.top)

            for word, count in top_of_words:
                print(f"{word}: {count}")


if __name__ == "__main__":
    main()
