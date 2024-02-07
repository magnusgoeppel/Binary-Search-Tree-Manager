# Importiert das sys-Modul zur Verwendung von Systemfunktionen, wie z.B. das Einlesen von Kommandozeilenargumenten
import sys


# Definition der Knoten-Klasse für den binären Suchbaum
class TreeNode:
    def __init__(self, key):
        self.key = key  # Schlüsselwert des Knotens
        self.left = None  # Linker Kindknoten
        self.right = None  # Rechter Kindknoten
        self.height = 1  # Höhe des Knotens im Baum


# Funktion zum Einfügen eines Schlüssels in den binären Suchbaum
def insert(node, key):
    if node is None:
        return TreeNode(key)  # Erstellt einen neuen Knoten, wenn der aktuelle Knoten nicht existiert

    if key < node.key:
        node.left = insert(node.left, key)  # Fügt den Schlüsselwert in den linken Teilbaum ein
    elif key > node.key:
        node.right = insert(node.right, key)  # Fügt den Schlüsselwert in den rechten Teilbaum ein

    node.height = 1 + max(get_height(node.left), get_height(node.right))  # Aktualisiert die Höhe des Knotens

    return node  # Gibt den aktualisierten Knoten zurück


# Funktion zum Berechnen der Höhe eines Knotens
def get_height(node):
    if node is None:
        return 0  # Gibt 0 zurück, wenn der Knoten nicht existiert
    return node.height  # Gibt die Höhe des Knotens zurück


# Funktion zum Berechnen des Balance-Faktors eines Knotens
def get_balance(node):
    if node is None:
        return 0  # Gibt 0 zurück, wenn der Knoten nicht existiert
    return get_height(node.right) - get_height(node.left)  # Berechnet den Balance-Faktor des Knotens


# Funktion zur rekursiven Traversierung des Baums und Ausgabe des Balance-faktors für jeden Knoten
def print_balance_factors(node):
    if node is None:
        return  # Beendet die Rekursion, wenn der Knoten nicht existiert

    balance = get_balance(node)  # Berechnet den Balance-Faktor des aktuellen Knotens
    avl_violation = " (AVL violation!)" if balance > 1 or balance < -1 else ""  # Beendet die Rekursion

    print_balance_factors(node.right)  # Traversiert den rechten Teilbaum zuerst
    print_balance_factors(node.left)  # Traversiert dann den linken Teilbaum
    print(f"bal({node.key}) = {balance}{avl_violation}")  # Gibt den Balance-Faktor des aktuellen Knotens aus


def is_avl_tree(node):
    if node is None:
        return True  # Gibt True zurück, wenn der Knoten nicht existiert

    balance = get_balance(node)  # Berechnet den Balance-Faktor des aktuellen Knotens
    if balance > 1 or balance < -1:
        return False  # Gibt False zurück, wenn der Knoten eine AVL-Verletzung aufweist

    return is_avl_tree(node.left) and is_avl_tree(node.right)  # Überprüft rekursiv, ob der ganze Baum ein AVL-Baum ist


# Funktion zur rekursiven Traversierung des Baums und Berechnung statistischer Daten
def traverse_tree(node, stats):
    if node is None:
        return  # Beendet die Rekursion, wenn der Knoten nicht existiert

    stats["count"] += 1  # Erhöht die Anzahl der Knoten im Baum
    stats["sum"] += node.key  # Aktualisiert die Summe der Schlüsselwerte im Baum
    stats["min"] = min(stats["min"], node.key)  # Aktualisiert den minimalen Schlüsselwert im Baum
    stats["max"] = max(stats["max"], node.key)  # Aktualisiert den maximalen Schlüsselwert im Baum

    traverse_tree(node.left, stats)  # Traversiert den linken Teilbaum
    traverse_tree(node.right, stats)  # Traversiert den rechten Teilbaum


# Funktion zur einfachen Suche
def simple_search(node, key, path=None):
    if path is None:
        path = []  # Initialisiert den Pfad, wenn er nicht angegeben wurde
    if node.key == key:
        return path  # Gibt den Pfad zurück, wenn der Schlüssel gefunden wurde

    result = simple_search(node.left, key, path)  # Sucht im linken Teilbaum
    if result is not None:
        return result  # Gibt den Pfad zurück, wenn der Schlüssel im linken Teilbaum gefunden wurde

    result = simple_search(node.right, key, path)  # Sucht im rechten Teilbaum
    if result is not None:
        return result  # Gibt den Pfad zurück, wenn der Schlüssel im rechten Teilbaum gefunden wurde

    path.pop()  # Entfernt den aktuellen Knoten aus dem Pfad, wenn der Schlüssel nicht gefunden wurde
    return None  # Gibt None zurück, wenn der Schlüssel nicht gefunden wurde


# Funktion zur Subtree-Suche
def subtree_search(node, subtree_root):
    if subtree_root is None:
        return True  # Gibt True zurück, wenn der Subtree-Root nicht existiert

    if node is None:
        return False  # Gibt False zurück, wenn der Knoten nicht existiert

    if node.key == subtree_root.key:
        # Überprüft rekursiv, ob der aktuelle Knoten und seine Kinder mit dem Subtree-Root übereinstimmen
        return subtree_search(node.left, subtree_root.left) and subtree_search(node.right, subtree_root.right)

    # Überprüft rekursiv, ob der Subtree-Root in einem der Teilbäume gefunden wurde
    return subtree_search(node.left, subtree_root) or subtree_search(node.right, subtree_root)


def build_tree_from_file(file_name):
    with open(file_name, "r") as file:
        keys = [int(line.strip()) for line in file.readlines() if line.strip()]  # Liest Schlüsselwerte aus der Datei

    root = None
    for key in keys:
        root = insert(root, key)  # Fügt jeden Schlüsselwert in den Baum ein

    return root  # Gibt die Wurzel des erstellten Baums zurück


# Funktion zum Finden des Knotens mit dem kleinsten Schlüsselwert
def find_min_node(node):
    if node.left is None:
        return node  # Gibt den aktuellen Knoten zurück, wenn es keinen linken Kindknoten gibt
    return find_min_node(node.left)  # Sucht rekursiv den Knoten mit dem kleinsten Schlüsselwert im linken Teilbaum


# Funktion zum Löschen eines Knotens mit dem gegebenen Schlüssel
def delete_node(node, key):
    if node is None:
        return node  # Gibt den aktuellen Knoten zurück, wenn er nicht existiert

    if key < node.key:
        node.left = delete_node(node.left, key)  # Löscht den Knoten im linken Teilbaum
    elif key > node.key:
        node.right = delete_node(node.right, key)  # Löscht den Knoten im rechten Teilbaum
    else:
        if node.left is None:
            return node.right  # Gibt den rechten Kindknoten zurück, wenn der linke Kindknoten nicht existiert
        elif node.right is None:
            return node.left  # Gibt den linken Kindknoten zurück, wenn der rechte Kindknoten nicht existiert
        else:
            min_node = find_min_node(node.right)  # Findet den Knoten mit dem kleinsten Schlüssel im rechten Teilbaum
            node.key = min_node.key  # Ersetzt den Schlüsselwert des aktuellen Knotens durch den kleinsten Schlüsselwert
            # Löscht den Knoten mit dem kleinsten Schlüsselwert im rechten Teilbaum
            node.right = delete_node(node.right, min_node.key)

    return node  # Gibt den aktualisierten Knoten zurück


def process_tree(tree_file_name, key_to_delete=None):
    tree_root = build_tree_from_file(tree_file_name)  # Erstellt den Baum aus der Datei

    if key_to_delete is not None:
        tree_root = delete_node(tree_root, key_to_delete)  # Löscht den Knoten mit dem angegebenen Schlüssel
        print(f"Node {key_to_delete} deleted.")  # Gibt eine Meldung aus, dass der Knoten gelöscht wurde

    if key_to_delete is None:
        print_balance_factors(tree_root)  # Gibt die Balance-Faktoren des Baums aus

    avl_status = "yes" if is_avl_tree(tree_root) else "no"  # Überprüft, ob der Baum ein AVL-Baum ist
    print(f"AVL: {avl_status}")  # Gibt den AVL-Status des Baums aus

    stats = {"count": 0, "sum": 0, "min": float("inf"), "max": float("-inf")}  # Initialisiert die Statistikwerte
    traverse_tree(tree_root, stats)  # Traversiert den Baum und berechnet die Statistikwerte

    print(
        f"min: {stats['min']}, max: {stats['max']}, avg: {stats['sum'] / stats['count']}")  # Gibt die Statistik aus


def main():
    if len(sys.argv) == 2:
        tree_file_name = sys.argv[1]  # Speichert den Dateinamen des Baums
        process_tree(tree_file_name)  # Verarbeitet den Baum und gibt die Ergebnisse aus

    elif len(sys.argv) == 3:
        tree_file_name = sys.argv[1]  # Speichert den Dateinamen des Baums

        try:
            key_to_delete = int(sys.argv[2])  # Versucht, das zweite Argument als integer zu konvertieren
            process_tree(tree_file_name, key_to_delete)   # Verarbeitet den Baum und löscht den angegebenen Knoten
        except ValueError:   # Verarbeitet den Baum und löscht den angegebenen Knoten
            subtree_file_name = sys.argv[2]  # Speichert den Dateinamen des Subbaums
            tree_root = build_tree_from_file(tree_file_name)  # Erstellt den Baum aus der Datei
            subtree_root = build_tree_from_file(subtree_file_name)  # Erstellt den Subbaum aus der Datei

            if subtree_root.left is None and subtree_root.right is None:  # Wenn der Subbaum nur einen Knoten hat
                search_result = simple_search(tree_root, subtree_root.key)  # Führt eine einfache Suche durch
                if search_result is not None:  # Wenn der Schlüssel gefunden wurde
                    print(f"{subtree_root.key} found", *search_result)  # Gibt den gefundenen Pfad aus
                else:  # Wenn der Schlüssel nicht gefunden wurde
                    print(
                        f"{subtree_root.key} not found!")  # Gibt Meldung aus, dass der Schlüssel nicht gefunden wurde
            else:  # Wenn der Subbaum mehr als einen Knoten hat
                search_result = subtree_search(tree_root, subtree_root)  # Führt eine Subtree-Suche durch
                if search_result:  # Wenn der Subbaum gefunden wurde
                    print("Subtree found")  # Gibt eine Meldung aus, dass der Subbaum gefunden wurde
                else:  # Wenn der Subbaum nicht gefunden wurde
                    print("Subtree not found!")  # Gibt eine Meldung aus, dass der Subbaum nicht gefunden wurde

        else:  # Wenn die Anzahl der Argumente ungültig ist
            print(
                "Ungültige Anzahl von Argumenten. Bitte geben Sie entweder nur den Dateinamen für den Suchbaum oder "
                "den Dateinamen für den Suchbaum und den Subtree an.")  # Gibt eine Fehlermeldung aus


if __name__ == "__main__":
    main()

