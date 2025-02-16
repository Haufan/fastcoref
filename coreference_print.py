import argparse
from fastcoref import FCoref
from colorama import Fore, Style, init

# Initialisiere colorama, damit Farben im Terminal richtig angezeigt werden
init()


def read_txt_file(file_path):
    """Liest eine Textdatei und gibt ihren Inhalt als String zurück."""

    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def resolve_coreferences(text):
    """Verwendet fastcoref, um Koferrenzen im gegebenen Text zu lösen."""

    model = FCoref()                   # Initialisiere das Koreference-Modell
    predictions = model.predict(text)  # Vorhersage für Koreferenzen im Text
    return predictions


def print_coref_colored(text, clusters, highlighted_cluster=None):
    """Gibt den Text mit hervorgehobenen Koferrenzen in verschiedenen Farben aus."""

    color_palette = [
        Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN,
        Fore.LIGHTBLACK_EX, Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX,
        Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTWHITE_EX
    ]
    mention_colors = {}
    sorted_mentions = []

    if not clusters:
        print("Keine Koferrenzen gefunden!")
        return

    print("\n\nText mit Koferrenzen in Farben:\n")

    # Weist den Clustern Farben zu
    color_index = 0
    for cluster_index, cluster in enumerate(clusters):

        color = color_palette[
            color_index % len(color_palette)]  # Falls mehr Cluster als Farben, wird die Palette wiederholt (14 Farben)

        if highlighted_cluster is not None and cluster_index != highlighted_cluster - 1:
            color = Style.RESET_ALL

        for mention in cluster:
            mention_colors[tuple(mention)] = color
            sorted_mentions.append(mention)

        color_index += 1

    # Sortiert die Erwähnungen nach ihrer Startposition im Text
    sorted_mentions.sort(key=lambda x: x[0])

    output = ""
    last_index = 0

    # Geht durch alle Erwähnungen und fügt sie im Text mit entsprechender Farbe ein
    for start, end in sorted_mentions:
        output += text[last_index:start]
        output += mention_colors[(start, end)] + text[start:end] + Style.RESET_ALL
        last_index = end

    output += text[last_index:]
    print(output)


def print_clusters(clusters, text):
    """
    Gibt die Koferrenz-Cluster als nummerierte Liste aus,
    mit den jeweiligen Wörtern und Farben für die Cluster-Labels.
    """

    color_palette = [
        Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE, Fore.BLACK,
        Fore.LIGHTBLACK_EX, Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX,
        Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTWHITE_EX
    ]

    if not clusters:
        print("Keine Koferrenzen gefunden!")
        return

    print("\n\nCoreference Clusters:\n")

    # Gibt die Cluster mit Nummer und extrahierten Wörtern aus in jeweiligen Farbe aus
    color_index = 0
    for i, cluster in enumerate(clusters, start=1):
        words = [text[start:end] for start, end in cluster]

        cluster_color = color_palette[color_index % len(color_palette)]
        print(f"{cluster_color}Cluster {i}: {words}{Style.RESET_ALL}")

        color_index += 1


def main(file_path, highlighted_cluster=None):
    """
    Hauptfunktion, die den Text aus der Datei liest,
    Koferrenzen auflöst und den Text mit farbigen Erwähnungen ausgibt.
    """

    text = read_txt_file(file_path)
    predictions = resolve_coreferences(text)
    clusters = predictions.get_clusters(as_strings=False)

    print_clusters(clusters, text)

    print_coref_colored(text, clusters, highlighted_cluster)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Löst Koferrenzen in einer Textdatei auf und zeigt sie mit Farben an.")
    parser.add_argument(
        'file_path', type=str, help="Pfad zur Textdatei, die auf Koferrenzen überprüft werden soll.")
    parser.add_argument(
        '--cluster', type=int,
        help="Gibt eine Cluster-Nummer an, die hervorgehoben werden soll. Standard ist, alle Cluster anzuzeigen.",
        default=None)

    args = parser.parse_args()

    main(args.file_path, highlighted_cluster=args.cluster)
