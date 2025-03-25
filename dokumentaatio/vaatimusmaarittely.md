# Vaatimusmäärittely 25.3.25

## Sovelluksen tarkoitus

Kaksiosainen pistokokeiden (pienien tenttien) teettämiseen ja tekemiseen. 
Käyttäjä voi joko luoda uuden kokeen, taikka avata valmis koe. 

## Käyttäjät

Sovelluksessa tulee olemaan ideaalisti kaksi käyttäjäroolia, _Opettaja_ sekä _Oppilas_. Oppilas ei kykene muokkaamaan koetta, vaan ainoastaan suorittamaan sen. 

Jos aikaa jää, niin opettajia voidaan luokitella vielä laajemmin oppilaitoksiin, joissa voi olla 'Pääkäyttäjä', jolla on pääsy kaikkiin oppilaitoksen kokeisiin.


## Ajateltu toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi luoda uuden tilin.
- Jos tilin käyttäjätunnus ja salasana täsmäävät, pääsee käyttöliittymään.
- Jos tiliä ei ole, tai tunnus ja salasana eivät täsmää, sovellus ei päästä käyttäjää pidemmälle.
- Käyttäjä voi valita, haluaako hän kirjautua sisään opettajana vai oppilaana. (Kokelaana vai kokeen tekijänä)

### Kirjautumisen jälkeen (_Opettaja_)
- Opettaja voi luoda uuden kokeen (LUO UUSI KOE)
- Opettaja voi tarkastella / muokata jo entuudestaan luotuja kokeita, jotka on tehty tällä käyttäjällä.
- Kokeen-luonti näkymässä, opettaja voi luoda uusia kysymyksiä (monivalinta, taikka vastaus valitulla merkkimäärällä), valita kysymyksien pisteytyksen, sekä muokata muita kokeen piirteitä.
- Kun koe on valmis, opettaja voi luoda 'koenäkymä'-version kokeesta, joka voidaan jakaa oppilaille tehtäväksi.
- Opettajalla ei ole pääsyä muiden opettajien kokeiden tietoihin.

### Kirjautumisen jälkeen (_Oppilas_)

- Käyttäjä voi avata hänelle lähetetyn kokeen, tiedostona.
- Avattuaan kokeen, oppilas voi vastata kaikkiin kysymyksiin, ja päättää kokeen.
- Kun koe on päätetty, oppilas voi kirjautua ulos, ja lähettää kokeen takaisin opettajalle (tämä ominaisuus ei tule varmaankaan olemaan itse sovelluksessa, vaan välitys tapahtuu sähköpostin taikka muun kanavan kautta).

## Muita huomioita (Laajentavia, sekä tarkentavia)

Tavoitteenani olisi lisätä ainakin seuraavat piirteet kokeisiin:
- Kun oppilas päättää kokeen, se lukkiutuu ja vastauksia ei voi enää muokata.
- Kokeisiin voidaan lisätä rajattu aika, joka laskee alaspäin kokeen avauksesta, ja lukitsee kokeen kun aika loppuu. 
- Opettaja voi tarkastella lukittuja kokeita, ja nähdä niiden pisteet.
- Opettaja voi valita, näkeekö oppilas mallivastaukset kokeen päätyttyä (laajentava, jos jää aikaa!).
- Opettajien täytyy saada vielä yksityinen 'lisä-salasana' joka on henkilökohtainen jokaista koulua kohden, niin että oppilaat eivät voi huijata kokeissa, luoden opettaja-käyttäjätilejä.