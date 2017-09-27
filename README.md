Chatbot SII

Il chatbot, che abbiamo realizzato, prevede uno scambio di messaggi con la piattaforma di messaggistica Telegram. Il suo username è @ProgettoSii_bot. 
Come da noi descritto, la soluzione prevede un Adapter, scritto in NodeJS, che gestisce le richieste da parte di Telegram. E’ possibile gestire le richieste di altre piattaforme semplicemente aggiungendo un file json in cui bisognerà specificare i singoli token richiesti dalle diverse piattaforme .
L’Adapter comunica con un server Python, che si occupa di inoltrare le richieste al db Solr. 
Prima di comunicare con Solr, il messaggio, scritto dall’utente, viene sottoposto a “matching” con delle regex colloquiali. Nel caso in cui non dovessero esserci corrispondenze, viene effettuata per prima una ricerca sul core  small_talk, che contiene le domande-risposte “colloquiali”. 
A questo punto la query dell’utente e le domande (estratte dai documenti restituiti da Solr in ordine di “somiglianza”) vengono sottoposte a stopping, stemming e infine coseno-similarità. Facendo alcuni test, abbiamo stabilito una soglia di 0.4, sopra la quale viene “accettata” la domanda in analisi e restituita la risposta, ad essa associata, all’utente.
In caso contrario, viene effettuato lo switch di core e la query viene sottoposta al core, che contiene le domande-risposte estratte dal sito di lineaamica.
Per questo core, invece, vengono estratti da Solr gli argomenti (topic) della domanda-risposta, poiché le domande erano di lunghezza troppo elevata. Anch’essi sono oggetto di stopping e stemming. Per quanto riguarda la coseno-similarità con la query dell’utente la soglia è più bassa (0.2), poichè trattano argomenti molto più specifici. 
Se la coseno-similarità non soddisfa queste ultime specifiche, il chatbot non saprà come rispondere. 
