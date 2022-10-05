# Python Service

Maak een clone van de [repo](https://github.com/ZuydUniversity/RT-Video-Stitching-and-Motion-Detection)
```
git clone https://github.com/ZuydUniversity/RT-Video-Stitching-and-Motion-Detection
```

Ga naar de subfolder RT-Video-Stitching-and-Motion-Detection `cd RT-Video-Stitching-and-Motion-Detection`

Doe de volgende stappen om de code in een python virtual environment te runnen.

## Python Virtual Environment
Eerst moeten we een python virtual environment maken.

Als je pip nog niet hebt geinstalleerd dan doe dan nu eerst, [installeer eerst](https://virtualenv.pypa.io/en/latest/installation.html).

Vervolgens installeer je virtualenv met `pip install virtualenv`.

Maak vervolgens een virtual environment om de service in te runnen:
```
python3 -m venv test_venv
source test_venv/bin/activate
pip install -r requirements.txt
```

Voor windows zijn de stappen iets afwijkend. [Check de handleiding](https://virtualenv.pypa.io/en/latest/user_guide.html)


###
Om de code te runnen voer je het volgend commando uit `python realtimeStitching.py`