
# Установка
## На свой сервер
```bash
git clone https://github.com/qzdn/twitch-tools.git
```
```bash
cd ./twitch-tools 
```
```bash
python -m venv venv 
```
```bash
source ./venv/bin/activate
```
```bash
pip install -r requirements.txt
```
```bash
touch .env
```
API Keys: [Last.fm](https://www.last.fm/api/account/create), [OpenWeatherMap](https://home.openweathermap.org/api_keys)
```bash
echo LASTFM_API_KEY=123 >> .env
```
```bash
echo OPENWEATHERMAP_API_KEY=123 >> .env
```
```bash
python ./server.py
```
Далее в StreamElements (или любом другом боте) добавить кастомные команды:
```
@${touser}, ${customapi.https://SERVER_IP:8080/lastfm/LASTFM_USERNAME}
@${touser}, ${customapi.https://SERVER_IP:8080/weather/${pathescape ${1:}}}
@${touser}, ${customapi.https://SERVER_IP:8080/hltb/${pathescape ${1:}}}
```
  
## glitch.com
- Создать новый проект через импорт репозитория с Github
- В файл `.env` добавить `LASTFM_API_KEY` и `OPENWEATHERMAP_API_KEY`
- В консоли прописать:
```bash
pip3 install -r requirements.txt
```
- Создать файл `start.sh` со следующим содержимым:
```bash
python3 ./server.py
```
- Проверить, что всё работает по адресу проекта: `https://PROJECT_NAME.glitch.me/`

В StreamElements (или любом другом боте) добавить кастомные команды:
```
@${touser}, ${customapi.https://https://PROJECT_NAME.glitch.me/lastfm/LASTFM_USERNAME}
@${touser}, ${customapi.https://PROJECT_NAME.glitch.me/weather/${pathescape ${1:}}}
@${touser}, ${customapi.https://PROJECT_NAME.glitch.me/hltb/${pathescape ${1:}}}
```