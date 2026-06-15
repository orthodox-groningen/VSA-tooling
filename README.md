# Stap 70 - CI rendering fonts OS guard

GitHub Actions faalde omdat een Linux-commando op een Windows runner werd uitgevoerd:

```text
sudo apt-get update && sudo apt-get install -y fonts-dejavu-core
```

Op Windows bestaat `sudo` niet.

Deze stap patcht workflows zodat:

- `fonts-dejavu-core` alleen op Linux draait;
- Windows jobs geen `sudo apt-get` uitvoeren;
- rendering dependencies (`requirements-rendering.txt`) wel platformonafhankelijk geïnstalleerd kunnen worden.

Gebruik:

```cmd
python scripts\apply-step70-ci-rendering-fonts-os-guard.py
```
