# Binärer Suchbaum-Manager

Dieses Tool ermöglicht die Verarbeitung von binären Suchbäumen, einschließlich der Einfügung und Löschung von Knoten, Überprüfung der AVL-Balance, Berechnung von Baumstatistiken und Durchführung von Suchoperationen. Es kann auch verwendet werden, um zu überprüfen, ob ein bestimmter Subbaum innerhalb eines größeren Baums existiert.

## Features

- **Einfügen von Knoten**: Fügt Knoten dynamisch in den Baum ein und erhält die AVL-Balance.
- **Löschen von Knoten**: Entfernt spezifizierte Knoten und passt den Baum entsprechend an.
- **AVL-Balance-Prüfung**: Überprüft, ob der Baum die AVL-Balance-Kriterien erfüllt.
- **Baumstatistiken**: Berechnet und gibt minimale, maximale und durchschnittliche Schlüsselwerte aus.
- **Suche**: Unterstützt einfache Suche nach einem Schlüsselwert und Subtree-Suche.

## Installation

Das Tool erfordert Python 3. Stellen Sie sicher, dass Python korrekt auf Ihrem System installiert ist, um das Skript auszuführen.

## Verwendung

AVL-Baum
Gibt die Balance-Faktoren des Baums aus und überprüft, ob er ein AVL-Baum ist:
python treecheck.py tree.txt 

Einfache Suche
Um zu überprüfen, ob ein Knoten im Baum existiert:
python treecheck.py suchbaum.txt simple.txt

Subtree-Suche
Um zu überprüfen, ob ein Subtree im Baum existiert:
python treecheck.py suchbaum.txt subtree.txt
