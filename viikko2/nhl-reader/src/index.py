from rich import print as rprint
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table
import requests
from player import Player
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    print("\nNHL statistics by nationality\n")
    
    konsoli = Console()
    kausi_vaihtoehdot = ["2018-19","2019-20","2020-21","2021-22","2022-23","2023-24","2024-25"]
    teksti = str("/".join(kausi_vaihtoehdot))

    kausi = Prompt.ask(f"Select season [bold magenta]{teksti}[/bold magenta]")
    url = "https://studies.cs.helsinki.fi/nhlstats/" + kausi + "/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    
 #   kausi_vaihtoehdot = ["2018-2019","2019-2020","2020-2021","2021-2022","2022-2023","2023-2024","2024-2025"]
 #   kausi = Prompt.ask(f"Select season {"/".join(kausi_vaihtoehdot)}")
    
    while True:
        maa_vaihtoehdot = ["AUT","CZE","AUS","SWE","GER","DEN","SUI","SVK","NOR","RUS","CAN","LAT","BLR","SLO","USA","FIN","GBR"]
        maa = Prompt.ask(f"\nSelect nationality [bold magenta]{"/".join(maa_vaihtoehdot)}[/bold magenta]")

        players = stats.top_scorers_by_nationality(maa)

        taulukko = Table(title="Top scorers of " + maa + " season " + kausi)

        taulukko.add_column("name", justify="right", style="cyan", no_wrap=True)
        taulukko.add_column("team", justify="right", style="magenta", no_wrap=True)
        taulukko.add_column("goals", justify="right", style="green", no_wrap=True)
        taulukko.add_column("assists", justify="right", style="green", no_wrap=True)
        taulukko.add_column("point", justify="right", style="green", no_wrap=True)
        
        for player in players:
            pelaaja = [player.name, player.joukkue, player.maalit, player.syotot, player.pisteet]
            taulukko.add_row(str(pelaaja[0]), str(pelaaja[1]), str(pelaaja[2]), str(pelaaja[3]), str(pelaaja[4]))
        konsoli = Console()
        konsoli.print(taulukko)

if __name__ == "__main__":
    main()