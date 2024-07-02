-----MAN PAGE FOR BEGINNERS------

GenAI and Democracy Project

!NAME
GenAI and Democracy - A project exploring the intersection of Generative AI (LLMs) and democratic processes.

!SYNOPSIS
This project provides a framework for experimenting with large language models (LLMs) to understand their potential impact on democracy. It includes a Dockerized environment for running inference, preprocessing data, and setting up user configurations.

!DESCRIPTION
The GenAI and Democracy project is part of the GenerativeAI and Democracy seminar at HfP / TUM. It aims to provide participants with the tools and knowledge needed to explore how generative AI can be used within the context of democratic processes. The project leverages open-source LLMs, allowing users to run these models efficiently on their hardware.

!Components
user_setup.py: Initializes the environment. Must return a non-zero exit code if unsuccessful.
user_preprocess.py: Preprocesses input data and saves it to preprocessed-file.json.
user_inference.py: Takes a user query and outputs a response based on preprocessed data.

!Running the Project
The project runs inside a Docker container. The startup sequence involves running user_setup.py, user_preprocess.py, and finally user_inference.py with specified user queries. Testing individual components of the pipeline is possible using test.py.

!Environment
The Docker container includes Python 3.11.0, numpy 1.24.0, torch 2.0.0, and transformers 4.12.0. Users are encouraged to match these versions in their local environment to avoid discrepancies.

!EXAMPLE
' Prerequisites
' Make sure you have Docker installed on your machine. If not, you can download and install it from Docker's official website: https://www.docker.com/
(https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)

' Build the Docker Image:
shell("sudo docker build -t googl2 .")

' Run the Docker Container:
shell("docker run -p 4000:80 googl2")

' Find the Running Docker Container Name:
shell("docker ps")

' Example output:
' CONTAINER ID   IMAGE   COMMAND                  CREATED         STATUS         PORTS                   NAMES
' 7b1e1fbf9208   googl   "tail -f /dev/null"      5 minutes ago   Up 5 minutes   0.0.0.0:4000->80/tcp    stoic_dewdney

' Run Inference Using the Docker Container:
shell("docker exec stoic_dewdney python user_inference.py --query 'How many people live in London?' --query_de 'myFirstQ'")

' Stopping the Docker Container and release the Port:
shell("docker stop confident_torvalds")

' Example Usage
![image](https://github.com/PhillipTian/genai-and-democracy-2024/assets/87056960/3b5921d4-23b9-4ad8-b9b5-3e5f990847bc)

(base) tianhao@tianhao-HP-ProBook-450-G8-Notebook-PC:~/genai-and-democracy-2024_new$ python user_inference.py --query 'how is Donald Trump' --query_de 'myFirstQ'
B🅱️e🇪s🇸t🇹 Seminar ever 🎉📚🎓🌟😊👍🔥💡🚀
--------------------
🔧 Setting up environment of user_inference...
🔧 Setting up environment for uese_preprocess...
📚 Transformers libraries imported successfully.
07/02/2024 10:31:37 PM - Use pytorch device_name: cuda
07/02/2024 10:31:37 PM - Load pretrained SentenceTransformer: sentence-transformers/msmarco-distilbert-base-tas-b
🧠 Model loaded successfully.
🔍 Handling user query...
Fetching articles in English (en)

Article saved as en_0.json
{'language': 'en', 'text_id': '0', 'content': ['CNN —\n\nChief Justice John Roberts is so enamored with the image of a bold and fearless American president that he abandoned his usual restraint and declared a stunning level of immunity for a former president facing criminal indictment for trying to overturn an election.\n\nThe man who famously likened judges to umpires who merely call balls and strikes instead, to re-employ a baseball cliché, swung for the fences. Roberts expansively interpreted constitutional protection for any president who might be indicted and all but ensured that former President Donald Trump will evade a trial for subverting the 2020 election before the 2024 presidential contest.\n\nEmphasizing the “unrivaled gravity” of presidential responsibilities and latching onto the term “fearlessly,” Roberts said a president makes “the most sensitive and far-reaching decisions entrusted to any official” and must be afforded the “maximum ability to deal fearlessly and impartially” with his duties.\n\nJoined by five of his fellow Republican-appointed justices (three by Trump himself), Roberts adopted an unstinting vision of presidential immunity, his traditional regard for the stature of the judiciary eclipsed by an aspiration for the institution of the presidency.\n\nUsually, Roberts cares about such overtly political divisions. Usually, he takes a more judicially institutional approach. He is also certainly aware that in previous weighty disputes over the separation of powers, the 1974 case of US v. Nixon, the 1997 case of Clinton v. Jones, the justices ruled unanimously – and both times against a sitting president.\n\nIn those cases, justices voted against the interests of the president who appointed them.\n\nBut that is not this court.\n\nAnd the Roberts of today barely resembles the chief justice known for brokering compromises in politically charged disputes, including to uphold Barack Obama’s Affordable Care Act just months before the 2012 presidential election.\n\nToday’s bench reflects the deep political polarization of the country. Where Roberts minimized the chaos propagated by Trump after the 2020 election, dissenting justices emphasized it. More substantively, they said Roberts’ “single-minded fixation on the President’s need for boldness and dispatch” defied constitutional history and relevant past cases.\n\nIn turn, Roberts ridiculed the three liberal dissenters, saying, “they strike a tone of chilling doom.”\n\nTense courtroom for opinion\n\nThere was a time when Roberts took pains to suggest disapproval of the norm-busting Trump, even publicly rebutting the former president’s attacks against the judiciary. But on Monday, Roberts provided a cool distillation of the events leading up to the January 6, 2021, assault on the US Capitol and avoided references to the former president.\n\nRoberts, who served in the Ronald Reagan and George H.W. Bush administrations, has in the past favored executive branch prerogatives.\n\nThe resolution of Trump v. United States, however, is more sweeping and likely to define Roberts’ broader legacy as chief justice.\n\nAn appointee of President George W. Bush, Roberts will begin his 20th session in the center chair next October.\n\nOn Monday, as the 69-year-old chief justice read portions of his opinion from the bench, he made use of some of the most dramatic lines in his written opinion, asserting that if newly elected presidents were free to prosecute their predecessors, the result would be “an executive branch that cannibalizes itself.”\n\nRoberts said that under “a pall of potential prosecution,” a president would hesitate to make decisions “fearlessly and fairly” and be rendered essentially ineffective. The president, he wrote, must be shielded from prosecution for any “core constitutional powers,” and “entitled, at a minimum, to a presumptive immunity from prosecution for all his official acts.”\n\nThe court’s new “presumptive immunity” offers Trump a substantial victory at this stage of the protracted case brought by Justice Department special counsel Jack Smith. Last August, Smith charged Trump with various counts of conspiracy, fraud and obstruction for the activities that culminated on January 6.\n\nVideo Ad Feedback Ty Cobb explains why he was ‘disappointed’ with Sotomayor’s dissent 02:41 - Source: CNN\n\nJustice Sonia Sotomayor, speaking for dissenters, heightened the rhetoric, condemning the majority for favoring Trump in a way that “reshapes the institution of the presidency” and “makes a mockery of the principle that no man is above the law.”\n\nHer voice oozed disdain, as when she mocked Roberts’ references to “the bold and unhesitating action” required of an independent executive.\n\nIn one of her especially impassioned points, the senior liberal justice told spectators the majority had given Trump “all the immunity he asked for – and more.”\n\nAmong the guests in the court’s VIP section near the bench was Jane Sullivan Roberts, wife of the chief justice. In the lawyers’ section sat Michael Dreeben, the Justice Department attorney who argued in April on behalf of Smith and will now, with the special counsel’s team, determine how to proceed.\n\n(Roberts and Dreeben have long been connected. Before becoming a judge, Roberts was an appellate attorney. In his first Supreme Court case, in January 1989, he happened to face Dreeben, then an assistant US solicitor general. Roberts won.)\n\nThe case will return to US District Court Judge Tanya Chutkan, who earlier had rejected Trump’s claim of immunity, to determine which of Trump’s activities as he protested the 2020 election results might be deemed “unofficial” and subject to criminal liability. Trump had previously argued that virtually all his activities surrounding the 2020 election were “official actions” and shielded from criminal prosecution.\n\nDefensive of SCOTUS’ handling of case\n\nAs he deflected from Trump, the person who brought the case, Roberts insisted that broad presidential immunity protects “the institution of the Presidency,” not an individual president.\n\nStill, subtly mingled with such assertions was some defensiveness about the court’s handling of the Trump controversy. He said that the justices had “little pertinent precedent” to guide their review of the case – “a case that we … are deciding on an expedited basis, less than five months after we granted the Government’s request” to take up the issue.\n\nBut the majority in a one-sentence order last December rejected a request from Smith to hear the consequential immunity question sooner. The court did not schedule oral arguments until late April.\n\nEarlier in December, Chutkan had ruled that Trump lacked any immunity from criminal prosecution. “Whatever immunities a sitting President may enjoy, the United States has only one Chief Executive at a time, and that position does not confer a lifelong ‘get-out-of-jail-free’ pass,” she wrote.\n\nThe DC US Circuit Court of Appeals affirmed, writing, “For the purpose of this criminal case, former President Trump has become citizen Trump, with all of the defenses of any other criminal defendant. But any executive immunity that may have protected him while he served as President no longer protects him against this prosecution.”\n\nEndorsing that view, Sotomayor offered a reminder of how it all started.\n\n“In a last desperate ploy to hold onto power,” she wrote, Trump “allegedly attempted to exploit the violence and chaos at the Capitol by pressuring lawmakers to delay the certification of the election and ultimately declare him the winner. That is the backdrop against which this case comes to the Court.”\n\nNot for the chief justice.\n\n“Unlike the political branches and the public at large,” he said, “we cannot afford to fixate exclusively, or even primarily, on present exigencies.”\n\nWrote Roberts: “Our perspective must be more farsighted.”']}


Fetching articles in German (de)

Article saved as de_0.json
{'language': 'de', 'text_id': '0', 'content': ['Freier Zugang zu allen Artikeln, Videos, Audioinhalten und Podcasts\n\niTunes-Abo wiederherstellen\n\nSPIEGEL+ wird über Ihren iTunes-Account abgewickelt und mit Kaufbestätigung bezahlt. 24 Stunden vor Ablauf verlängert sich das Abo automatisch um einen Monat zum Preis von zurzeit € 21,99. In den Einstellungen Ihres iTunes-Accounts können Sie das Abo jederzeit kündigen. Um SPIEGEL+ außerhalb dieser App zu nutzen, müssen Sie das Abo direkt nach dem Kauf mit einem SPIEGEL-ID-Konto verknüpfen. Mit dem Kauf akzeptieren Sie unsere Allgemeinen Geschäftsbedingungen und Datenschutzerklärung.']}


Fetching articles in French (fr)

Article saved as fr_0.json
{'language': 'fr', 'text_id': '0', 'content': ['Donald Trump, à Altanta, en Géorgie, le 27 juin 2024. MARCO BELLO / REUTERS\n\nDonald Trump vit une période de félicité. Quelques jours après le naufrage de Joe Biden, lors de leur débat télévisé, l’ancien président a reçu, lundi 1er juillet, une autre nouvelle réjouissante. Sans surprise, la Cour suprême dominée par les juges conservateurs a porté un coup sévère à l’enquête fédérale sur la tentative de coup d’Etat ayant conduit à l’assaut du 6 janvier 2021 contre le Capitole.\n\nInvitée à se prononcer sur l’immunité présidentielle totale que réclamait Donald Trump dans le cadre de ses fonctions passées, la cour n’a pas consenti à cette demande, extravagante aux yeux des juristes. Mais, derrière les subtilités de la décision, la victoire n’en est pas moins spectaculaire pour le candidat républicain, qui voit s’éloigner la menace d’un procès dans cette affaire. Donald Trump peut aussi espérer des répliques favorables dans les autres enquêtes contre lui, en particulier celle instruite en Géorgie au sujet des pressions exercées, fin 2020, sur les officiels de cet Etat pour modifier le résultat de l’élection.\n\nLe président de la Cour, John Roberts, auteur de la décision approuvée par six juges contre trois, souligne que « la nature du pouvoir présidentiel exige qu’un ancien président puisse disposer d’une forme d’immunité devant des poursuites pénales pour des actes officiels commis pendant son mandat ». Une immunité qui doit être absolue, ajoute-t-il, en ce qui concerne le cœur de ses prérogatives constitutionnelles. Pour ses autres actes officiels, dans des domaines où il partage l’autorité avec le Congrès, il doit aussi bénéficier d’une forme de « présomption d’immunité », qui ne peut être levée qu’au cas par cas, au tribunal, en fonction de la pertinence des preuves rassemblées par l’accusation.\n\nLire aussi : Procès de l’élection de 2020 : la justice interdit à Donald Trump de faire des commentaires publics sur les juges, les procureurs ou les témoins Ajouter à vos sélections\n\nEnfin, les actes privés ne sont pas couverts par une immunité. Trois scénarios possibles s’esquissent donc, mais sans périmètre clairement défini pour les deux derniers. Voilà Tanya Chutkan, la juge présidant l’audience sur les faits du 6 janvier 2021 à Washington, investie d’une immense responsabilité. Or, le temps manque.\n\nL’enquête sabrée du procureur spécial\n\nDerrière cette apparente prudence de la Cour et son apologie de la séparation des pouvoirs, la majorité des juges bâtit une série de murailles, de tailles diverses, autour de l’institution présidentielle, et donc de Donald Trump. John Roberts paraît surtout soucieux d’éventuelles poursuites à caractère politique contre un président, au mépris du cœur du dossier : une tentative de coup d’Etat. Il s’inquiète de l’intrusion du judiciaire dans l’exécutif, de l’effet dissuasif et perturbateur qu’aurait la menace de poursuites pénales sur un président, dans des arbitrages-clés.\n\nIl vous reste 72.46% de cet article à lire. La suite est réservée aux abonnés.']}


🚀 Starting file processing...
📄 Processing file: fr_0.json
🇫🇷 Translating from French to English...
Translating: Donald Trump, à Altanta, en Géorgie, le 27 juin 2024.
Translating: MARCO BELLO / REUTERS

Donald Trump vit une période de félicité.
Translating: Quelques jours après le naufrage de Joe Biden, lors de leur débat télévisé, l’ancien président a reçu, lundi 1er juillet, une autre nouvelle réjouissante.
Translating: Sans surprise, la Cour suprême dominée par les juges conservateurs a porté un coup sévère à l’enquête fédérale sur la tentative de coup d’Etat ayant conduit à l’assaut du 6 janvier 2021 contre le Capitole.
Translating: Invitée à se prononcer sur l’immunité présidentielle totale que réclamait Donald Trump dans le cadre de ses fonctions passées, la cour n’a pas consenti à cette demande, extravagante aux yeux des juristes.
Translating: Mais, derrière les subtilités de la décision, la victoire n’en est pas moins spectaculaire pour le candidat républicain, qui voit s’éloigner la menace d’un procès dans cette affaire.
Translating: Donald Trump peut aussi espérer des répliques favorables dans les autres enquêtes contre lui, en particulier celle instruite en Géorgie au sujet des pressions exercées, fin 2020, sur les officiels de cet Etat pour modifier le résultat de l’élection.
Translating: Le président de la Cour, John Roberts, auteur de la décision approuvée par six juges contre trois, souligne que « la nature du pouvoir présidentiel exige qu’un ancien président puisse disposer d’une forme d’immunité devant des poursuites pénales pour des actes officiels commis pendant son mandat ».
Translating: Une immunité qui doit être absolue, ajoute-t-il, en ce qui concerne le cœur de ses prérogatives constitutionnelles.
Translating: Pour ses autres actes officiels, dans des domaines où il partage l’autorité avec le Congrès, il doit aussi bénéficier d’une forme de « présomption d’immunité », qui ne peut être levée qu’au cas par cas, au tribunal, en fonction de la pertinence des preuves rassemblées par l’accusation.
Translating: Lire aussi : Procès de l’élection de 2020 : la justice interdit à Donald Trump de faire des commentaires publics sur les juges, les procureurs ou les témoins Ajouter à vos sélections

Enfin, les actes privés ne sont pas couverts par une immunité.
Translating: Trois scénarios possibles s’esquissent donc, mais sans périmètre clairement défini pour les deux derniers.
Translating: Voilà Tanya Chutkan, la juge présidant l’audience sur les faits du 6 janvier 2021 à Washington, investie d’une immense responsabilité.
Translating: Or, le temps manque.
Translating: L’enquête sabrée du procureur spécial

Derrière cette apparente prudence de la Cour et son apologie de la séparation des pouvoirs, la majorité des juges bâtit une série de murailles, de tailles diverses, autour de l’institution présidentielle, et donc de Donald Trump.
Translating: John Roberts paraît surtout soucieux d’éventuelles poursuites à caractère politique contre un président, au mépris du cœur du dossier : une tentative de coup d’Etat.
Translating: Il s’inquiète de l’intrusion du judiciaire dans l’exécutif, de l’effet dissuasif et perturbateur qu’aurait la menace de poursuites pénales sur un président, dans des arbitrages-clés.
Translating: Il vous reste 72.46% de cet article à lire.
Translating: La suite est réservée aux abonnés.
✅ File processed and saved: fr_0.json
📄 Processing file: en_0.json
✅ File processed and saved: en_0.json
📄 Processing file: de_0.json
🇩🇪 Translating from German to English...
Translating: Freier Zugang zu allen Artikeln, Videos, Audioinhalten und Podcasts

iTunes-Abo wiederherstellen

SPIEGEL+ wird über Ihren iTunes-Account abgewickelt und mit Kaufbestätigung bezahlt.
Translating: 24 Stunden vor Ablauf verlängert sich das Abo automatisch um einen Monat zum Preis von zurzeit € 21,99.
Translating: In den Einstellungen Ihres iTunes-Accounts können Sie das Abo jederzeit kündigen.
Translating: Um SPIEGEL+ außerhalb dieser App zu nutzen, müssen Sie das Abo direkt nach dem Kauf mit einem SPIEGEL-ID-Konto verknüpfen.
Translating: Mit dem Kauf akzeptieren Sie unsere Allgemeinen Geschäftsbedingungen und Datenschutzerklärung.
✅ File processed and saved: de_0.json
🎉 All files processed successfully.
📂 Loading and processing JSON files...
✅ JSON files processed.
Batches: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  3.23it/s]
Batches: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  2.03it/s]
🎉 Great! We have found some results for you! And the higher the score, the more relevant the text is.
📄 Score: 102.5254898071289, Doc: Donald Trump, in Altanta, Georgia, June 27, 2024. MARCO BELLO / REUTERS Donald Trump is living a period of felicity. A few days after Joe Biden’s shipwreck, during their televised debate, the former president received, Monday, July 1, another joyful news. Unsurprisingly, the conservative-dominated Supreme Court dealt a severe blow to the federal investigation into the attempted coup that led to the January 6, 2021 assault on the Capitol. Asked to rule on the total presidential immunity demanded by Donald Trump as part of his past duties, the court did not consent to this request, extravagant in the eyes of lawyers. But, behind the subtleties of the decision, the victory is no less spectacular for the Republican candidate, who sees the threat of a trial in this case move away. Donald Trump can also hope for favorable responses in other investigations against him, especially the one conducted in Georgia about the pressure exerted, at the end of 2020, on the officials of this state to modify the result of the election. The court’s president, John Roberts, author of the decision approved by six judges against three, points out that “the nature of presidential power requires that a former president be granted some form of immunity from criminal prosecution for official acts committed during his mandate.” Immunity that must be absolute, he adds, with regard to the core of his constitutional prerogatives. For his other official acts, in areas where he shares authority with Congress, he must also benefit from a form of “presumption of immunity”, which can only be lifted on a case-by-case basis, in court, depending on the relevance of the evidence gathered by the prosecution. Read also: 2020 election trial: Justice prohibits Donald Trump from making public comments on judges, prosecutors or witnesses Add to your selections Finally, private acts are not covered by immunity. Three possible scenarios are therefore sketched out, but without a clearly defined perimeter for the last two. This is Tanya Chutkan, the judge presiding over the January 6, 2021 fact-finding hearing in Washington, D.C., invested with immense responsibility. But time is running out. Behind this apparent prudence of the Court and its apology for the separation of powers, the majority of judges build a series of walls, of various sizes, around the presidential institution, and therefore Donald Trump. John Roberts seems especially concerned about possible political prosecutions against a president, in defiance of the heart of the file: an attempted coup. He is concerned about the intrusion of the judiciary into the executive, the deterrent and disruptive effect that would be the threat of criminal prosecution of a president, in key arbitrations. You still have 72.46% of this article to read. The suite is reserved for subscribers.
📄 Score: 96.87667846679688, Doc: CNN —

Chief Justice John Roberts is so enamored with the image of a bold and fearless American president that he abandoned his usual restraint and declared a stunning level of immunity for a former president facing criminal indictment for trying to overturn an election.

The man who famously likened judges to umpires who merely call balls and strikes instead, to re-employ a baseball cliché, swung for the fences. Roberts expansively interpreted constitutional protection for any president who might be indicted and all but ensured that former President Donald Trump will evade a trial for subverting the 2020 election before the 2024 presidential contest.

Emphasizing the “unrivaled gravity” of presidential responsibilities and latching onto the term “fearlessly,” Roberts said a president makes “the most sensitive and far-reaching decisions entrusted to any official” and must be afforded the “maximum ability to deal fearlessly and impartially” with his duties.

Joined by five of his fellow Republican-appointed justices (three by Trump himself), Roberts adopted an unstinting vision of presidential immunity, his traditional regard for the stature of the judiciary eclipsed by an aspiration for the institution of the presidency.

Usually, Roberts cares about such overtly political divisions. Usually, he takes a more judicially institutional approach. He is also certainly aware that in previous weighty disputes over the separation of powers, the 1974 case of US v. Nixon, the 1997 case of Clinton v. Jones, the justices ruled unanimously – and both times against a sitting president.

In those cases, justices voted against the interests of the president who appointed them.

But that is not this court.

And the Roberts of today barely resembles the chief justice known for brokering compromises in politically charged disputes, including to uphold Barack Obama’s Affordable Care Act just months before the 2012 presidential election.

Today’s bench reflects the deep political polarization of the country. Where Roberts minimized the chaos propagated by Trump after the 2020 election, dissenting justices emphasized it. More substantively, they said Roberts’ “single-minded fixation on the President’s need for boldness and dispatch” defied constitutional history and relevant past cases.

In turn, Roberts ridiculed the three liberal dissenters, saying, “they strike a tone of chilling doom.”

Tense courtroom for opinion

There was a time when Roberts took pains to suggest disapproval of the norm-busting Trump, even publicly rebutting the former president’s attacks against the judiciary. But on Monday, Roberts provided a cool distillation of the events leading up to the January 6, 2021, assault on the US Capitol and avoided references to the former president.

Roberts, who served in the Ronald Reagan and George H.W. Bush administrations, has in the past favored executive branch prerogatives.

The resolution of Trump v. United States, however, is more sweeping and likely to define Roberts’ broader legacy as chief justice.

An appointee of President George W. Bush, Roberts will begin his 20th session in the center chair next October.

On Monday, as the 69-year-old chief justice read portions of his opinion from the bench, he made use of some of the most dramatic lines in his written opinion, asserting that if newly elected presidents were free to prosecute their predecessors, the result would be “an executive branch that cannibalizes itself.”

Roberts said that under “a pall of potential prosecution,” a president would hesitate to make decisions “fearlessly and fairly” and be rendered essentially ineffective. The president, he wrote, must be shielded from prosecution for any “core constitutional powers,” and “entitled, at a minimum, to a presumptive immunity from prosecution for all his official acts.”

The court’s new “presumptive immunity” offers Trump a substantial victory at this stage of the protracted case brought by Justice Department special counsel Jack Smith. Last August, Smith charged Trump with various counts of conspiracy, fraud and obstruction for the activities that culminated on January 6.

Video Ad Feedback Ty Cobb explains why he was ‘disappointed’ with Sotomayor’s dissent 02:41 - Source: CNN

Justice Sonia Sotomayor, speaking for dissenters, heightened the rhetoric, condemning the majority for favoring Trump in a way that “reshapes the institution of the presidency” and “makes a mockery of the principle that no man is above the law.”

Her voice oozed disdain, as when she mocked Roberts’ references to “the bold and unhesitating action” required of an independent executive.

In one of her especially impassioned points, the senior liberal justice told spectators the majority had given Trump “all the immunity he asked for – and more.”

Among the guests in the court’s VIP section near the bench was Jane Sullivan Roberts, wife of the chief justice. In the lawyers’ section sat Michael Dreeben, the Justice Department attorney who argued in April on behalf of Smith and will now, with the special counsel’s team, determine how to proceed.

(Roberts and Dreeben have long been connected. Before becoming a judge, Roberts was an appellate attorney. In his first Supreme Court case, in January 1989, he happened to face Dreeben, then an assistant US solicitor general. Roberts won.)

The case will return to US District Court Judge Tanya Chutkan, who earlier had rejected Trump’s claim of immunity, to determine which of Trump’s activities as he protested the 2020 election results might be deemed “unofficial” and subject to criminal liability. Trump had previously argued that virtually all his activities surrounding the 2020 election were “official actions” and shielded from criminal prosecution.

Defensive of SCOTUS’ handling of case

As he deflected from Trump, the person who brought the case, Roberts insisted that broad presidential immunity protects “the institution of the Presidency,” not an individual president.

Still, subtly mingled with such assertions was some defensiveness about the court’s handling of the Trump controversy. He said that the justices had “little pertinent precedent” to guide their review of the case – “a case that we … are deciding on an expedited basis, less than five months after we granted the Government’s request” to take up the issue.

But the majority in a one-sentence order last December rejected a request from Smith to hear the consequential immunity question sooner. The court did not schedule oral arguments until late April.

Earlier in December, Chutkan had ruled that Trump lacked any immunity from criminal prosecution. “Whatever immunities a sitting President may enjoy, the United States has only one Chief Executive at a time, and that position does not confer a lifelong ‘get-out-of-jail-free’ pass,” she wrote.

The DC US Circuit Court of Appeals affirmed, writing, “For the purpose of this criminal case, former President Trump has become citizen Trump, with all of the defenses of any other criminal defendant. But any executive immunity that may have protected him while he served as President no longer protects him against this prosecution.”

Endorsing that view, Sotomayor offered a reminder of how it all started.

“In a last desperate ploy to hold onto power,” she wrote, Trump “allegedly attempted to exploit the violence and chaos at the Capitol by pressuring lawmakers to delay the certification of the election and ultimately declare him the winner. That is the backdrop against which this case comes to the Court.”

Not for the chief justice.

“Unlike the political branches and the public at large,” he said, “we cannot afford to fixate exclusively, or even primarily, on present exigencies.”

Wrote Roberts: “Our perspective must be more farsighted.”
📄 Score: 73.84584045410156, Doc: free access to all articles, videos, audio content and podcasts itunes - abo restore mirror + will be processed via your itunes - account and paid with purchase. 24 hours before the deadline automatically increases the subscription by one month to the price of currently € 21.99. in the settings of your itunes - account you can inform about ito at any time. in order to use spiegel + outside of this app, you have to connect the subscription directly after purchasing with a spiegel - id - account. Together with the purchase they accept our general terms and conditions of business and data protection declaration.'
(base) tianhao@tianhao-HP-ProBook-450-G8-Notebook-PC:~/genai-and-democracy-2024_new$


