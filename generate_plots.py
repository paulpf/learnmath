"""
Parabel-Aufgaben: Automatische Plot-Generierung mit Matplotlib
Erstellt professionelle PNG-Diagramme für alle Lösungen
"""

import matplotlib
matplotlib.use('Agg')  # Headless backend - keine GUI notwendig
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from pathlib import Path

# Größe der Diagramme einheitlich
plt.style.use('seaborn-v0_8-darkgrid')
FIGSIZE = (12, 8)
DPI = 300

# Ordner für Images
Path("images").mkdir(exist_ok=True)

# ============================================================================
# Aufgabe 1: Tordurchfahrt
# ============================================================================

def plot_aufgabe1():
    """Tordurchfahrt - Fahrzeug-Durchfahrt"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6), dpi=DPI, gridspec_kw={'width_ratios': [1, 1]})

    # Subplot 1: Tor + Funktion
    x = np.linspace(-2.5, 2.5, 200)
    y = -1.5 * x**2 + 6

    ax1.plot(x, y, 'b-', linewidth=3, label='Tor f(x) = -1,5x² + 6')
    ax1.axhline(y=0, color='k', linewidth=0.5)
    ax1.axvline(x=0, color='k', linewidth=0.5)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlabel('x (Entfernung in m)', fontsize=12, fontweight='bold')
    ax1.set_ylabel('y (Höhe in m)', fontsize=12, fontweight='bold')
    ax1.set_title('Aufgabe 1a): Parabelgleichung', fontsize=13, fontweight='bold')
    ax1.plot(0, 6, 'r*', markersize=20, label='Scheitel S(0|6)', zorder=5)
    ax1.plot([-2, 2], [0, 0], 'go', markersize=8, label='Nullstellen', zorder=5)
    ax1.set_xlim(-2.5, 2.5)
    ax1.set_ylim(-1, 7)
    ax1.legend(fontsize=11, loc='upper right')

    # Subplot 2: Fahrzeug-Durchfahrt
    ax2.plot(x, y, 'b-', linewidth=3, label='Tor')
    ax2.axhline(y=2.2, color='orange', linewidth=2.5, linestyle='--', label='Fahrzeug (2,20m hoch)')
    ax2.axhline(y=0, color='k', linewidth=0.5)
    ax2.axvline(x=0, color='k', linewidth=0.5)

    # Fahrzeug-Breite markieren
    ax2.axvline(x=-1.5, color='red', linewidth=2, linestyle=':', alpha=0.7)
    ax2.axvline(x=1.5, color='red', linewidth=2, linestyle=':', alpha=0.7)
    ax2.fill_between([-1.5, 1.5], 0, 2.2, alpha=0.2, color='yellow', label='Fahrzeug (3m breit)')

    # Tor-Höhe bei ±1,5 markieren
    ax2.plot([-1.5, 1.5], [2.625, 2.625], 'r*', markersize=15, zorder=5)
    ax2.text(-1.5, 2.9, '2,625m', fontsize=10, ha='center', fontweight='bold', color='red')
    ax2.text(1.5, 2.9, '2,625m', fontsize=10, ha='center', fontweight='bold', color='red')

    # Platz-Differenz
    ax2.annotate('', xy=(-1.5, 2.2), xytext=(-1.5, 2.625),
                arrowprops=dict(arrowstyle='<->', color='green', lw=2.5))
    ax2.text(-1.75, 2.425, '42,5cm', fontsize=11, fontweight='bold', color='green')

    ax2.grid(True, alpha=0.3)
    ax2.set_xlabel('x (m)', fontsize=12, fontweight='bold')
    ax2.set_ylabel('y (m)', fontsize=12, fontweight='bold')
    ax2.set_title('Aufgabe 1b): Fahrzeug passt!', fontsize=13, fontweight='bold')
    ax2.set_xlim(-2.5, 2.5)
    ax2.set_ylim(-1, 7)
    ax2.legend(fontsize=11, loc='upper right')

    plt.subplots_adjust(left=0.08, right=0.95, wspace=0.3)
    plt.savefig('images/aufgabe1_tordurchfahrt.png', dpi=DPI, bbox_inches='tight')
    print("✓ Aufgabe 1: Tordurchfahrt")
    plt.close()

# ============================================================================
# Prüfungsaufgabe 2023: Froschsprung
# ============================================================================

def plot_froschsprung():
    """Froschsprung - Prüfungsaufgabe 2023"""
    fig = plt.figure(figsize=(17, 10), dpi=DPI)
    gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)

    # Subplot 1: Grundlegende Parabel
    ax1 = fig.add_subplot(gs[0, 0])
    x = np.linspace(0, 2.2, 200)
    y = -1.149 * (x - 1.1)**2 + 1.39

    ax1.plot(x, y, 'g-', linewidth=3, label='Froschsprung')
    ax1.axhline(y=0, color='k', linewidth=1)
    ax1.axvline(x=0, color='k', linewidth=1)
    ax1.plot(0, 0, 'bo', markersize=10, label='Absprung (0|0)')
    ax1.plot(1.1, 1.39, 'ro', markersize=10, label='Scheitel S(1,1|1,39)')
    ax1.plot(2.2, 0, 'bo', markersize=10, label='Landung (2,2|0)')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlabel('Entfernung (m)', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Höhe (m)', fontsize=11, fontweight='bold')
    ax1.set_title('Teil a): Parabelgleichung', fontsize=12, fontweight='bold')
    ax1.legend(fontsize=10, loc='upper right')
    ax1.set_xlim(-0.1, 2.4)
    ax1.set_ylim(-0.2, 1.6)

    # Subplot 2: Schilfrohr-Problem
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.plot(x, y, 'g-', linewidth=3, label='Froschsprung')
    ax2.axhline(y=0, color='k', linewidth=1)
    ax2.axvline(x=0, color='k', linewidth=1)

    # Schilfrohr
    ax2.plot([1.5, 1.5], [0, 0.94], 'brown', linewidth=8, label='Schilfrohr (94cm)')
    ax2.plot(1.5, 0.94, 'go', markersize=8)

    # Frosch-Position bei 1.5m
    y_frosch_150 = -1.149 * (1.5 - 1.1)**2 + 1.39
    ax2.plot(1.5, y_frosch_150, 'r*', markersize=15, label=f'Frosch bei 1,5m ({y_frosch_150*100:.0f}cm)')

    # Abstand-Linie
    ax2.annotate('', xy=(1.55, 0.94), xytext=(1.55, y_frosch_150),
                arrowprops=dict(arrowstyle='<->', color='red', lw=2))
    ax2.text(1.65, (0.94 + y_frosch_150)/2, f'{(y_frosch_150-0.94)*100:.1f}cm', 
            fontsize=11, fontweight='bold', color='red')

    ax2.grid(True, alpha=0.3)
    ax2.set_xlabel('Entfernung (m)', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Höhe (m)', fontsize=11, fontweight='bold')
    ax2.set_title('Teil b): Schilfrohr-Problem', fontsize=12, fontweight='bold')
    ax2.legend(fontsize=10, loc='upper right')
    ax2.set_xlim(1.0, 2.3)
    ax2.set_ylim(-0.1, 1.6)

    # Subplot 3: Frosch 1 vs Frosch 2
    ax3 = fig.add_subplot(gs[1, :])
    
    # Frosch 2: Original y = -(3/200)x² + 165, aber verschoben für fairen Start-Vergleich
    # Verschiebung: Nullstellen von ±104,88 → 0 und 209,76 (gleicher Startpunkt wie Frosch 1)
    x_frosch2 = np.linspace(0, 220, 200)
    y_frosch2 = -3/200 * (x_frosch2 - 104.88)**2 + 165

    # Frosch 1 (in cm für Vergleich): f(x) = -0,01149(x - 110)² + 139
    x_frosch1_cm = np.linspace(0, 220, 200)
    y_frosch1_cm = -0.01149 * (x_frosch1_cm - 110)**2 + 139

    ax3.plot(x_frosch1_cm, y_frosch1_cm, 'g-', linewidth=3.5, label='Frosch 1 (220cm weit, 139cm hoch) ⭐ Gewinner')
    ax3.plot(x_frosch2, y_frosch2, 'b-', linewidth=3.5, label='Frosch 2 (209,76cm weit, 165cm hoch)')
    ax3.axhline(y=0, color='k', linewidth=1)
    ax3.axvline(x=0, color='k', linewidth=1)
    
    # Absprung- und Landungspunkte (beide starten jetzt bei x=0!)
    ax3.plot([0, 220], [0, 0], 'go', markersize=8, label='Frosch 1: Start & Landung')
    ax3.plot([0, 209.76], [0, 0], 'bo', markersize=8, label='Frosch 2: Start & Landung')
    
    # Scheitel markieren
    ax3.plot(110, 139, 'g*', markersize=18, zorder=5)
    ax3.plot(104.88, 165, 'b*', markersize=18, zorder=5)
    
    # Differenz visualisieren
    ax3.annotate('', xy=(220, -20), xytext=(209.76, -20),
                arrowprops=dict(arrowstyle='<->', color='red', lw=2.5))
    ax3.text(214.88, -30, '10,24cm', fontsize=12, fontweight='bold', color='red',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))

    ax3.grid(True, alpha=0.3)
    ax3.set_xlabel('Entfernung (cm)', fontsize=11, fontweight='bold')
    ax3.set_ylabel('Höhe (cm)', fontsize=11, fontweight='bold')
    ax3.set_title('Teil c): Frosch 1 vs Frosch 2 - Frosch 1 springt weiter!', 
                 fontsize=12, fontweight='bold', color='darkgreen')
    ax3.legend(fontsize=10, loc='upper right')
    ax3.set_xlim(-15, 235)
    ax3.set_ylim(-45, 180)

    plt.tight_layout()
    plt.savefig('images/froschsprung_pruefungsaufgabe.png', dpi=DPI, bbox_inches='tight')
    print("✓ Prüfungsaufgabe 2023: Froschsprung")
    plt.close()

# ============================================================================
# Aufgabe 2: Kugelstoßen
# ============================================================================

def plot_kugelstossen_1():
    """Kugelstoßen Teil 1"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6), dpi=DPI)

    # Subplot 1: Gesamte Flugbahn
    x = np.linspace(0, 9, 200)
    y = -0.24 * (x - 4)**2 + 5.84

    ax1.plot(x, y, 'darkorange', linewidth=3, label='Kugel-Flugbahn')
    ax1.axhline(y=0, color='k', linewidth=1)
    ax1.axvline(x=0, color='k', linewidth=1)
    ax1.plot(0, 2, 'bo', markersize=10, label='Abwurf (0|2)')
    ax1.plot(4, 5.84, 'ro', markersize=10, label='Maximum (4|5,84)')
    ax1.plot(8.93, 0, 'go', markersize=10, label='Landung (8,93|0)')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlabel('Entfernung (m)', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Höhe (m)', fontsize=11, fontweight='bold')
    ax1.set_title('Aufgabe 2a): Kugelstoßen - Weite berechnen', fontsize=12, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.set_xlim(-0.5, 9.5)
    ax1.set_ylim(-0.5, 6.5)
    ax1.text(4.5, 5.84, 'max = 5,84m', fontsize=10, fontweight='bold')

    # Subplot 2: Höhe bei 0,75m
    ax2.plot(x, y, 'darkorange', linewidth=3, label='Kugel-Flugbahn')
    ax2.axhline(y=0, color='k', linewidth=1)
    ax2.axvline(x=0, color='k', linewidth=1)
    ax2.axhline(y=0.75, color='purple', linewidth=2, linestyle='--', label='Höhe = 0,75m')

    # Punkte wo y = 0.75
    x_intersect = [0.605, 8.605]  # Näherungswerte
    ax2.plot(x_intersect, [0.75, 0.75], 'mo', markersize=8)
    ax2.text(0.605, 0.9, '0,61m', fontsize=10, ha='center', fontweight='bold')
    ax2.text(8.605, 0.9, '8,61m', fontsize=10, ha='center', fontweight='bold')

    ax2.grid(True, alpha=0.3)
    ax2.set_xlabel('Entfernung (m)', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Höhe (m)', fontsize=11, fontweight='bold')
    ax2.set_title('Aufgabe 2b): Höhe bei 0,75m', fontsize=12, fontweight='bold')
    ax2.legend(fontsize=10)
    ax2.set_xlim(-0.5, 9.5)
    ax2.set_ylim(-0.5, 6.5)

    plt.tight_layout()
    plt.savefig('images/aufgabe2_kugelstossen.png', dpi=DPI, bbox_inches='tight')
    print("✓ Aufgabe 2: Kugelstoßen")
    plt.close()

# ============================================================================
# Aufgabe 3: Springbrunnen
# ============================================================================

def plot_springbrunnen_1():
    """Springbrunnen - Wasserstrahl"""
    x = np.linspace(0, 2, 150)
    y = -3 * (x - 1)**2 + 3

    fig, ax = plt.subplots(figsize=(11, 8), dpi=DPI)

    ax.plot(x, y, 'cyan', linewidth=4, label='Wasserstrahl')
    ax.axhline(y=0, color='k', linewidth=1)
    ax.axvline(x=0, color='k', linewidth=1)
    ax.fill_between(x, 0, y, alpha=0.2, color='cyan', label='Wasservolumen')

    # Punkte
    ax.plot(0, 0, 'bo', markersize=10, label='Austritt (0|0)')
    ax.plot(1, 3, 'ro', markersize=10, label='Maximum (1|3)')
    ax.plot(2, 0, 'go', markersize=10, label='Landung (2|0)')
    ax.plot(1.5, 2.25, 'mo', markersize=10, label='Becher (1,5|2,25)')

    # Becherglas-Position
    ax.axvline(x=1.5, color='purple', linewidth=2, linestyle=':', alpha=0.7)
    ax.text(1.5, 2.5, f'Becherglas\n2,25m Höhe', fontsize=11, ha='center', 
           fontweight='bold', bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

    ax.grid(True, alpha=0.3)
    ax.set_xlabel('Entfernung (m)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Höhe (m)', fontsize=12, fontweight='bold')
    ax.set_title('Aufgabe 3: Springbrunnen - Wasserstrahl', fontsize=13, fontweight='bold')
    ax.legend(fontsize=11, loc='upper right')
    ax.set_xlim(-0.2, 2.3)
    ax.set_ylim(-0.3, 3.5)

    plt.tight_layout()
    plt.savefig('images/aufgabe3_springbrunnen.png', dpi=DPI, bbox_inches='tight')
    print("✓ Aufgabe 3: Springbrunnen")
    plt.close()

# ============================================================================
# Aufgabe 4: Stahlbrücke
# ============================================================================

def plot_stahlbruecke():
    """Stahlbrücke mit Stützen"""
    x = np.linspace(-50, 50, 200)
    y = -0.012 * x**2 + 30

    fig, ax = plt.subplots(figsize=(12, 8), dpi=DPI)

    ax.plot(x, y, 'b-', linewidth=4, label='Brücken-Parabel')
    ax.axhline(y=0, color='k', linewidth=1)
    ax.axvline(x=0, color='k', linewidth=1)
    ax.fill_between(x, 0, y, alpha=0.2, color='blue')

    # Stützen bei ±25m
    ax.plot([-25, -25], [0, 22.5], 'brown', linewidth=8, label='Stütze 1 (22,5m)')
    ax.plot([25, 25], [0, 22.5], 'brown', linewidth=8, label='Stütze 2 (22,5m)')

    # Punkte
    ax.plot(0, 30, 'ro', markersize=12, label='Scheitel (0|30)')
    ax.plot([-50, 50], [0, 0], 'go', markersize=10, label='Spannweite (100m breit)')
    ax.plot([-25, 25], [22.5, 22.5], 'o', color='darkred', markersize=8)

    # Wasserspiegel
    ax.axhline(y=0, color='cyan', linewidth=2, linestyle='-', alpha=0.7, label='Wasserspiegel')

    # Dimensionen
    ax.annotate('', xy=(-50, -2), xytext=(50, -2),
                arrowprops=dict(arrowstyle='<->', color='black', lw=2))
    ax.text(0, -4, '100m (Spannweite)', fontsize=11, ha='center', fontweight='bold')

    ax.annotate('', xy=(-53, 0), xytext=(-53, 30),
                arrowprops=dict(arrowstyle='<->', color='black', lw=2))
    ax.text(-56, 15, '30m', fontsize=11, ha='center', fontweight='bold', rotation=90)

    ax.grid(True, alpha=0.3)
    ax.set_xlabel('Breite (m)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Höhe (m)', fontsize=12, fontweight='bold')
    ax.set_title('Aufgabe 4: Stahlbrücke - Stützenlänge berechnen', fontsize=13, fontweight='bold')
    ax.legend(fontsize=11, loc='upper right')
    ax.set_xlim(-65, 65)
    ax.set_ylim(-6, 35)
    ax.set_aspect('equal', adjustable='box')

    plt.tight_layout()
    plt.savefig('images/aufgabe4_stahlbruecke.png', dpi=DPI, bbox_inches='tight')
    print("✓ Aufgabe 4: Stahlbrücke")
    plt.close()

# ============================================================================
# Aufgabe 5: Rakete
# ============================================================================

def plot_rakete():
    """Rakete vs Hochhaus"""
    x = np.linspace(-45, 45, 200)
    y = -0.08125 * x**2 + 130

    fig, ax = plt.subplots(figsize=(12, 8), dpi=DPI)

    ax.plot(x, y, 'r-', linewidth=3.5, label='Raketen-Flugbahn')
    ax.axhline(y=0, color='k', linewidth=1)

    # Hochhaus
    ax.add_patch(patches.Rectangle((-12.5, 0), 25, 100, 
                                   linewidth=2, edgecolor='gray', 
                                   facecolor='lightgray', alpha=0.6, 
                                   label='Hochhaus (100m hoch, 25m breit)'))

    # Rakete über Hochhaus
    x_haus = np.linspace(-12.5, 12.5, 100)
    y_haus = -0.08125 * x_haus**2 + 130
    ax.plot(x_haus, y_haus, 'r-', linewidth=3.5)
    ax.fill_between(x_haus, 100, y_haus, alpha=0.3, color='red', label='Abstand über Hochhaus')

    # Punkte
    ax.plot(0, 130, 'r*', markersize=20, label='Raketen-Max (130m)')
    ax.plot([-40, 40], [0, 0], 'go', markersize=10, label='Landungen (±40m)')

    # Höhe bei Hochhaus-Kante
    ax.plot([-12.5, 12.5], [117.3, 117.3], 'o', color='darkred', markersize=8)
    ax.annotate('', xy=(15, 100), xytext=(15, 117.3),
                arrowprops=dict(arrowstyle='<->', color='darkred', lw=2.5))
    ax.text(20, 108.5, '17,3m\nAbstand', fontsize=11, fontweight='bold', color='darkred')

    ax.grid(True, alpha=0.3)
    ax.set_xlabel('Entfernung (m)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Höhe (m)', fontsize=12, fontweight='bold')
    ax.set_title('Aufgabe 5: Rakete - Fliegt über Hochhaus!', fontsize=13, fontweight='bold')
    ax.legend(fontsize=11, loc='upper right')
    ax.set_xlim(-45, 45)
    ax.set_ylim(-10, 145)

    plt.tight_layout()
    plt.savefig('images/aufgabe5_rakete.png', dpi=DPI, bbox_inches='tight')
    print("✓ Aufgabe 5: Rakete")
    plt.close()

# ============================================================================
# Alle Plots generieren
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("PARABELN - Automatische Plot-Generierung")
    print("="*60 + "\n")

    plot_aufgabe1()
    plot_froschsprung()
    plot_kugelstossen_1()
    plot_springbrunnen_1()
    plot_stahlbruecke()
    plot_rakete()

    print(f"\n{'='*60}")
    print("✓ ALLE PLOTS ERFOLGREICH GENERIERT!")
    print(f"{'='*60}\n")
    print("📁 Alle Bilder sind im 'images/' Ordner gespeichert\n")
