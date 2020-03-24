<h1 align="center">Statistisches Nandusamt 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://www.mozilla.org/en-US/MPL/2.0/" target="_blank">
    <img alt="License: MPL" src="https://img.shields.io/badge/License-MPL-yellow.svg" />
  </a>
  <a href="https://twitter.com/onyxmoon\_" target="_blank">
    <img alt="Twitter: onyxmoon\_" src="https://img.shields.io/twitter/follow/onyxmoon\_.svg?style=social" />
  </a>
</p>

> Stellt einige Funktionen zur Berechnung statistischer Wahrscheinlichkeiten für regeltechnische Manöver im Rollenspiel &#34;Das schwarze Auge&#34; bereit.

## Dependencies / Abhängigkeiten

- [Node.js](https://nodejs.org/en/)
- Python 3

## Install / Installation

1. Install python dependecies / Python-Abhängigkeiten installieren

    ```sh
    python -m pip install -r requirements.txt
    ```
    
2. Install node modules / Node-Module installieren

    ```sh
    npm install
    ```

    

## Usage / Nutzung

**Start app** / *App starten*

- Windows: 
  `.\node_modules\.bin\electron .`
- Mac OS/Linux: 
  `./node_modules/.bin/electron .`

**Start app with globally installed electron** / *App starten mit global installiertem electron*

- `electron .`

**Run the app through your web browser** / *App über den Browser starten*

- Start Flask server manually: 
  `python web_app/run_app.py`



## Bundling

**Deploying is done in two steps** / *Die Bereitstellung erfolgt in zwei Schritten* :

1. A standalone Python executable containing the Flask backend is generated using *PyInstaller*
   *Eine eigenständige ausführbare Python-Datei, die das Flask-Backend enthält, wird mit dem **PyInstaller** erzeugt.*
2. The Python executable and the electron application (`electron.js`) are bundled using *electron-builder*
   *Die ausführbare Python-Datei und die Elektronenanwendung (electron.js) werden mit dem electron-builder verpackt.*



**Package the app for the host platform** / App einpacken für aktuelle Plattform

- `npm run package `(output binaries will be stored in `/dist`)

## Author / Autor

👤 **Maradas**



👤 **Onyxmoon**

* Website: https://onyxmoon.me
* Twitter: [@onyxmoon\_](https://twitter.com/onyxmoon\_)
* Github: [@Onyxmoon](https://github.com/Onyxmoon)



## 📝 License

Copyright © 2020 Maradas / [Onyxmoon](https://github.com/Onyxmoon).<br />
This project is [MPL](https://www.mozilla.org/en-US/MPL/2.0/) licensed.

***
❤️