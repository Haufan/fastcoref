# Hinweis:
# - Verwende Python 3.9. und die beigelegte requirement.txt

# Der folgende Code basiert auf dem Beispielcode aus dem Repository fastcoref.   [https://github.com/shon-otmazgin/fastcoref]
# Der Code wurde kommentiert, jedoch ausschließlich in den Input-Texten angepasst.
# Die grundlegende Struktur und Funktionsweise des Codes ist unverändert.

# Der Abschnitt, der die Logits für eine bestimmte Koreferenzbeziehung in as_clusters ausgibt, wurde auskommentiert,
# da die Cluster an den jeweiligen Text angepasst werden müssten.

# Es gibt fünf Beispieltexte, die jeweils unter chosen_text in Zeile 100 ausgewählt werden können.



def as_text(text):
    """
    Verarbeitet den Eingabetext mit spaCy und der fastcoref-Komponente zur Koreferenzauflösung.

    Diese Funktion:
    - Lädt das spaCy-Modell `en_core_web_sm`.
    - Fügt die `fastcoref`-Komponente hinzu, um Koreferenzen zu erkennen.
    - Gibt die erkannten Koreferenzcluster aus.
    - Gibt den aufgelösten Text aus, in dem Koreferenzen ersetzt wurden.

    Argumente:
        text (str): Der zu verarbeitende Eingabetext.

    Rückgabe:
        None: Gibt die Koreferenzcluster und den aufgelösten Text in der Konsole aus.
    """

    import spacy
    from fastcoref import spacy_component  # Importiert fastcoref für die Koreferenzauflösung

    # Das englische spaCy-Modell laden
    nlp = spacy.load("en_core_web_sm")

    # Die fastcoref-Komponente zur NLP-Pipeline hinzufügen
    nlp.add_pipe("fastcoref")

    # Den Text verarbeiten, um Koreferenzcluster zu identifizieren und auszugeben
    doc = nlp(text)
    print("Koreferenz-Cluster:")
    print(doc._.coref_clusters)

    # Den Text erneut verarbeiten, um den aufgelösten Text zu erhalten und auszugeben
    doc = nlp(text, component_cfg={"fastcoref": {'resolve_text': True}})
    print("\nAufgelöster Text:")
    print(doc._.resolved_text)


#############################################################################################################

def as_clusters(text):
    """
    Verwendet das FastCoref-Modell zur Koreferenzauflösung und gibt verschiedene Ergebnisse aus.

    Diese Funktion:
    - Lädt das FCoref-Modell zur Koreferenzanalyse.
    - Berechnet und gibt die Koreferenz-Cluster aus (als Zeichenketten und Indexbereiche).
    - Gibt die Wahrscheinlichkeitswerte (Logits) für eine Koreferenzverknüpfung zwischen zwei Textabschnitten aus.

    Argumente:
        text (str): Der Eingabetext, der analysiert werden soll.

    Rückgabe:
        None: Gibt die Koreferenzinformationen in der Konsole aus.
    """

    from fastcoref import FCoref  # Importiert FCoref für die Koreferenzauflösung

    # Das Modell laden (auf CPU ausführen) - (!) eine Ausführung über Coda ist möglich
    model = FCoref(device='cpu')

    # Koreferenzvorhersagen für den Eingabetext berechnen
    preds = model.predict(texts=[text])

    # Die Koreferenzcluster als Indexbereiche ausgeben
    print("Koreferenz-Cluster (Indexbereiche):")
    print(preds[0].get_clusters(as_strings=False))

    # Die Koreferenzcluster als Zeichenketten ausgeben
    print("\nKoreferenz-Cluster (Text):")
    print(preds[0].get_clusters())

    # Die Logits für eine bestimmte Koreferenzbeziehung ausgeben
    '''print("\nLogit-Wert für Koreferenzwahrscheinlichkeit:")
    print(preds[0].get_logit(span_i=(0, 4), span_j=(30, 33)))'''


if __name__ == "__main__":

    # 1 - Text generiert von ChatGPT für Koreferent
    # 2 - Märchen: Hans im Glück   [https://www.gutenberg.org/files/2591/2591-h/2591-h.htm#link2H_4_0003]
    # 3 - UN Rede: Speech by Federal Chancellor Olaf Scholz at the 78th General Debate of the United Nations General Assembly New York, Tuesday, 19 September 2023   [https://new-york-un.diplo.de/un-en/2618622-2618622]
    # 4 - Artikel: How LA fires devastation will change the Grammys this year   [https://www.bbc.com/news/articles/c4g76x194jpo]
    # 5 - Wissenschaft: Multilingual coreference resolution as text generation   [https://aclanthology.org/2024.crac-1.11.pdf]

    # Wähle den Text mit seiner jeweiligen Nummer
    chosen_text = 1


    text1 = 'John went to the park to meet his friend, Sarah. ' \
          'She had been waiting for him near the fountain. ' \
          'When he arrived, he waved to her, and she smiled back. ' \
          'They decided to walk around and talk about their plans for the weekend. ' \
          'John mentioned that he wanted to visit the new museum, and Sarah thought it was a great idea. ' \
          'As they walked, Sarah pointed out a group of ducks by the pond. ' \
          '"Look at them!" she exclaimed. ' \
          'John laughed and took a picture of the ducks to show his sister later. ' \
          'He told Sarah that his sister loves animals and would enjoy seeing the photo. ' \
          'After spending some more time at the park, they said goodbye and promised to meet again soon. ' \
          'John felt happy about the day, and so did Sarah.'

    text2 = 'HANS IN LUCK ' \
          'Some men are born to good luck: all they do or try to do comes right—all that falls to them is so much gain—all their geese are swans—all their cards are trumps—toss them which way you will, they will always, like poor puss, alight upon their legs, and only move on so much the faster. The world may very likely not always think of them as they think of themselves, but what care they for the world? what can it know about the matter? ' \
          'One of these lucky beings was neighbour Hans. Seven long years he had worked hard for his master. At last he said, ‘Master, my time is up; I must go home and see my poor mother once more: so pray pay me my wages and let me go.’ And the master said, ‘You have been a faithful and good servant, Hans, so your pay shall be handsome.’ Then he gave him a lump of silver as big as his head. ' \
          'Hans took out his pocket-handkerchief, put the piece of silver into it, threw it over his shoulder, and jogged off on his road homewards. As he went lazily on, dragging one foot after another, a man came in sight, trotting gaily along on a capital horse. ‘Ah!’ said Hans aloud, ‘what a fine thing it is to ride on horseback! There he sits as easy and happy as if he was at home, in the chair by his fireside; he trips against no stones, saves shoe-leather, and gets on he hardly knows how.’ Hans did not speak so softly but the horseman heard it all, and said, ‘Well, friend, why do you go on foot then?’ ‘Ah!’ said he, ‘I have this load to carry: to be sure it is silver, but it is so heavy that I can’t hold up my head, and you must know it hurts my shoulder sadly.’ ‘What do you say of making an exchange?’ said the horseman. ‘I will give you my horse, and you shall give me the silver; which will save you a great deal of trouble in carrying such a heavy load about with you.’ ‘With all my heart,’ said Hans: ‘but as you are so kind to me, I must tell you one thing—you will have a weary task to draw that silver about with you.’ However, the horseman got off, took the silver, helped Hans up, gave him the bridle into one hand and the whip into the other, and said, ‘When you want to go very fast, smack your lips loudly together, and cry “Jip!”’ ' \
          'Hans was delighted as he sat on the horse, drew himself up, squared his elbows, turned out his toes, cracked his whip, and rode merrily off, one minute whistling a merry tune, and another singing, ' \
          '‘No care and no sorrow, ' \
          'A fig for the morrow! ' \
          'We’ll laugh and be merry, ' \
          'Sing neigh down derry!’ ' \
          'After a time he thought he should like to go a little faster, so he smacked his lips and cried ‘Jip!’ Away went the horse full gallop; and before Hans knew what he was about, he was thrown off, and lay on his back by the road-side. His horse would have run off, if a shepherd who was coming by, driving a cow, had not stopped it. Hans soon came to himself, and got upon his legs again, sadly vexed, and said to the shepherd, ‘This riding is no joke, when a man has the luck to get upon a beast like this that stumbles and flings him off as if it would break his neck...'

    text3 = 'Fifty years ago, almost to the day, two German states joined the United Nations: the then German Democratic Republic as the 133rd member and the Federal Republic of Germany as the 134th member. This step is of great importance to us Germans to this very day. For membership of the United Nations enabled my country – the instigator of terrible wars and horrific crimes – to return to the family of peace-loving nations. We are profoundly grateful for this chance. ' \
            'The return was not free of requirements. The accession of the two German states was preceded by a visionary policy of détente. The aim, as my predecessor – Federal Chancellor and Nobel Peace Prize laureate Willy Brandt – said here in New York 50 years ago was to “fill in the rifts of the Cold War”. Three things were essential for this. First of all, the clear commitment of both German states to resolve conflicts without force. This was laid down in the Basic Treaty between Bonn and East Berlin as well as in the treaties which the Federal Republic of Germany concluded with its eastern neighbours. The second prerequisite was the renunciation of any form of revisionism, by recognising Germany’s new borders drawn after the Second World War as inviolable. At the time, many people in West Germany were opposed to this. In retrospect, however, it proved to be the right decision. Finally, the third prerequisite was a foreign policy that did not ignore the realities of the Cold War. And which, at the same time, always remained focused on overcoming the status quo – that is to say, the confrontation between the blocs and thus also the unnatural division of Germany. ' \
            'When I look back here today at the beginnings of our membership of the United Nations, I am doing so not only out of historical interest. Rather, it is because the prohibition of the use of force still remains the unfulfilled core pledge of our United Nations. Because the inviolability of borders and the sovereign equality of states also have to be defended in our multipolar world – by all of us. And because we today – especially today – need the courage, creative energy and will to fill in the rifts, which are deeper than ever. Germany is strongly committed to these three ideals – the renunciation of the use of force as a political instrument, the rejection of any kind of revisionism and the determination to engage in cooperation beyond any dividing factors. ' \
            'It is to these ideals that we Germans owe the great fortune of living in a unified country today, in peace with our neighbours, friends and partners around the world. At the same time, what Willy Brandt stated here 50 years ago is all the more true today: “In a world in which we are all increasingly dependent on each other, a policy for peace must not stop on our own doorstep.” German policy can and never will be limited to pursuing our interests with no consideration for others. Because we know that our freedom, our democracy and our prosperity are deeply rooted in the well-being of Europe and the world. ' \
            'That is why the order of the day is not less cooperation – perhaps packaged today as de‑coupling or as “cooperation only among the like-minded”. Instead, we need more cooperation: existing alliances must be strengthened and new partners sought. For this is the only way to reduce the risks of excessively one‑sided dependencies. ' \
            'This is all the more true in a world which – in contrast to 50 years ago – no longer has only two centres of power but many different ones. Multipolarity is not a new order. Anyone who assumes that smaller countries are the backyard of larger ones is mistaken. Multipolarity is not a normative category but a description of today’s reality. Anyone seeking order in a multipolar world has to start here at the United Nations. That is why Germany supports the UN system and, as the second-largest contributor after the United States, pays its regular budget assessment with full conviction. Only the United Nations – on the basis of the values enshrined in its Charter – can fully realise the aspirations of universal representation and sovereign equality for all. That cannot be said of either the G7 or the G20 – as important as they are for achieving international consensus – or of BRICS or other groups. ' \
            'I know that some will counter by asking: is the United Nations not all too often unable to take action, paralysed by the antagonisms of its heterogeneous membership? My response to them is: the obstruction of a few, no matter how influential they are, should not lead us to forget that we, the overwhelming majority of states, agree on many things. All of us – almost all of us – want force as a political instrument to remain banned. All of us have an interest in ensuring that the sovereignty, territorial integrity and political independence of our countries are respected. And all of us should know what this requires: namely, that we also grant others these rights. ' \
            'These golden rules are universal, even if many of us were not yet sitting around the table when the UN Charter was adopted in 1945. Yet only ten years later – in Bandung, Indonesia – it was the African and Asian states liberated from colonialism that raised their voices to call for self-determination, territorial integrity, the sovereign equality of all states and a world without colonialism and imperialism. This seems more relevant today than ever before. It is by these principles that we – whether large or small – will all be judged. These principles must also form the basis when it comes to reshaping our multipolar world! Only then can the global challenges of our time be mastered. ' \
            'The greatest challenge of all is anthropogenic climate change. Of course, the traditional industrialised countries have a very special responsibility in the fight against the climate crisis. However, many other countries are among the biggest emitters today. Instead of now waiting for others, we all have to do more together to achieve the Paris climate goals. Each and every one of us must have the opportunity to gain the same level of prosperity as people in Europe, North America or in countries such as Japan or Australia. However, our planet will not survive if this economic development is attained with the technologies and production processes of the 19th or 20th centuries – with combustion engines and coal-fired power plants. ' \
            'This leads us to one conclusion: we have to de‑couple economic development from CO2 emissions. This is already happening in many countries, for we have the solutions and technologies. As a key nation in the field of technology, we are offering to cooperate here for the common good. If producers of renewable energies and their industrial users come together across continents, we will create new prosperity together – in many places around the world. I am pleased to announce to you today that Germany is honouring its pledges on international climate financing. From two billion euro in 2014 and more than four billion euro in 2020, we tripled our contribution last year to six billion euro. We have therefore kept our word. As will the industrialised countries as a whole, which will hit their target of 100 billion euro for international climate financing for the first time this year. That is an important, an overdue signal before we take stock in Dubai this December and negotiate new climate action plans for the period after 2030. I believe it is important that we are as concrete and as binding as possible. That is why I advocate that we set clear targets in Dubai for the expansion of renewable energies and for greater energy efficiency. ' \
            'We will be equally ambitious when it comes to achieving the SDGs, the Sustainable Development Goals. Climate action or development – this trade‑off will not work. Our summit yesterday brought home to me how urgent it is that we make up for lost time when it comes to the SDGs, too. We therefore want to use next year’s Summit of the Future, which we are currently preparing with our friends from Namibia, to pick up the pace and push ahead with the implementation of the 2030 Agenda. ' \
            'It is important to me in this context that we ensure more private investment in Africa, Asia, Latin America and the Caribbean. Let me give you just one example: the entire world is currently talking about the diversification of supply chains and raw materials security. Would it not be a start if at least the first production step were to take place on‑site where the raw material deposits are to be found? Certainly, Germany and German business are open to entering into partnerships of this very nature. ' \
            'Of course, in the coming years we will all face the challenge of leading our economies, our energy supplies and our infrastructure to a resource-efficient, climate-neutral future. That will require major investment. To create the right conditions to bring about this investment, we have to address the debt crisis in many countries and modernise the international financial architecture. I said at the start that Germany is not clinging on to the status quo, not in this issue either. We want something to change. I have been calling – most recently at the G20 Summit in Delhi – for the multilateral development banks to reform, so that they can contribute more to financing the protection of global public goods such as the climate and biodiversity or the prevention of pandemics. That is what the G20 decided in Delhi. Germany is also providing financial support for this reform. We will be the first country to invest hybrid capital to the tune of 305 million euro in the World Bank. It is estimated that this capital will enable the World Bank to provide more than two billion euro in additional loans. ' \
            'Ladies and gentlemen, this morning Secretary-General Guterres highlighted the rapidly rising humanitarian needs due to the many crises worldwide. Germany is the second-largest donor of humanitarian assistance around the globe, and we will continue to stand by those suffering the greatest hardship. ' \
            'Our United Nations itself must not cling to the status quo, ladies and gentlemen. And by that I mean two things. Firstly, the United Nations must tackle the challenges of the future, just as Secretary-General António Guterres has proposed. One of the major issues, in my view, is how we can ensure that innovation and technological advances can be used by humanity as a whole. Artificial intelligence, for example, offers tremendous opportunities. But at the same time, it can cement the division of the world if only a few benefit from it, if algorithms only take into account part of the reality, if access is limited to richer countries. That is why Germany is actively fostering the exchange on the Global Digital Compact. We should also talk about common rules for the possible use of generative artificial intelligence as a weapon. ' \
            'Another question that will define our future is how the United Nations itself reflects the reality of a multipolar world. To date, it does not do that sufficiently. That is most evident in the composition of the Security Council. I am therefore delighted that a growing number of partners – including three of the permanent members – have stated that they want to see progress on reform. However, one thing is clear: Africa deserves greater representation, as do Asia and Latin America. Under this premise, we can negotiate a text with various options. No country should obstruct these open-ended negotiations with excessively high demands. We will not do that, either. Ultimately, it is up to the General Assembly to decide on a reform of the Security Council. Until then, Germany would like to shoulder responsibility as a non‑permanent member of the UN Security Council and I ask you to support our candidacy for 2027/28. ' \
            'Ladies and gentlemen, when I speak these days and before this Assembly of peace, then my thoughts are with those for whom peace is a distant dream. They are with the Sudanese, who have become victims of a brutal power struggle between two warlords, with the men and women in eastern Congo or, at this current time, with the people in Karabakh. I firmly believe that the renewed military activities there will lead nowhere – they must end. And, of course, my thoughts are with the Ukrainians, who are fighting for their lives and their freedom, for independence and their country’s territorial integrity in order to safeguard those very principles to which we all committed ourselves in the UN Charter. ' \
            'But Russia’s war of aggression has caused immense suffering not only in Ukraine. People around the world are suffering as a result of inflation, growing debts, the scarcity of fertilisers, hunger and increasing poverty. Precisely because this war is having unbearable consequences around the world, it is right and proper that the world is involved in the quest for peace. At the same time, we should beware of phoney solutions which represent “peace” in name only. For peace without freedom is called oppression. Peace without justice is a dictated peace. Moscow, too, must finally understand that. For let us not forget that Russia is responsible for this war and Russia’s President can end it at any time with one single order. But for him to do that, he has to understand that we – the states of the United Nations – are serious about our principles, that we do not see a place for revisionism and imperialism in the multipolar world of the 21st century. No one here in New York has expressed this as aptly as our colleague, the Ambassador of Kenya. After Russia’s invasion of Ukraine, he said this in the Security Council: “Rather than form nations that looked ever backward into history with a dangerous nostalgia, we chose to look forward to a greatness none of our many nations and peoples had ever known.” ' \
            'Fellow delegates, Germany’s history holds many lessons about the dangers of such nostalgia. That is why we chose a different path when we joined the United Nations 50 years ago, the path of peace and reconciliation, the path of recognising existing borders, the path of cooperation with all of you in the pursuit of a better, a more equitable world. It started with a solemn promise that we made 50 years ago, a promise every one of us made upon joining the United Nations, namely “to unite our strength to maintain international peace and security”. Let us all do our best to live up to that promise. Thank you very much!'

    text4 = 'How LA fires devastation will change the Grammys this year' \
            'The week leading up to the Grammy Awards is typically a star-studded seven days. It is filled with exclusive parties that draw some of musics top talents from across the globe - producers, singers, agents and musicians - all to the epicentre of the entertainment industry in Los Angeles. ' \
            'But nearly all of that is non-existent this year. Even the hallmark rowdy after-parties have been cancelled. ' \
            'There were questions over whether the Grammys ceremony, the "Oscars for Music," would even go on as planned on Sunday after Los Angeles saw its most devastating fire disaster ever recorded - blazes that were only fully doused on Friday after burning for 24 days. ' \
            'Twenty-nine people have died and more than 16,000 homes and businesses have been destroyed - with whole neighbourhoods now ash. Many artists and industry professionals are among those who lost homes, studios and equipment. ' \
            'In the muted lead-up to the show, efforts usually put toward parties have gone instead toward fundraising efforts. Showrunners say the ceremony itself will also look different. ' \
            'To cancel the show or not? ' \
            'The Recording Academy, which runs the show, said the show is needed more than ever. Trustees say the evening will double as a charitable event to raise money and honour both the victims and the emergency responders who risked their lives. ' \
            'But it will look different than years past. ' \
            'Showrunners are looking to strike the right tone honouring the victims of the fire and displaying a defiant Los Angeles that will persevere. But there is concern the optics of rich celebrities dolled up with smiles on a red carpet could come off as tone deaf. ' \
            'Recording Academy CEO Harvey Mason Jr. said that the show include a reimagined format, scaled-back red carpet and a more reflective tone. ' \
            'He highlighted the economic impact, noting that thousands rely on Grammy-related work, particularly in the service industry. He framed the event as a symbol of resilience, arguing that cancelling would not benefit the city or music industry. ' \
            '"Cancelling, pushing, moving does not accomplish what us standing together" does, Mr Mason argued in a webcast. The show will be "unifying and coming together, honouring music, but also using the power of music to heal, rebuild and provide services to people who need it". ' \
            '"I think this might be one of the most important Grammy weeks we have ever had." ' \
            'Mr Mason told the New York Times that they consulted a range of public officials about whether they should hold the event - including the citys mayor and California Governor Gavin Newsom - and whether it would hinder fire response efforts. ' \
            '"They strongly suggested that we continue forward with hosting the event," he told the outlet. "Everyone said there is nothing good that comes from postponing." ' \
            'But there are still worries that the night will be a bad look for the music industry. ' \
            '"I actually do not think that the Grammys should be happening," Elyn Kazarian, a creative director in the music industry, told the BBC. ' \
            '"It is just very weird to me that there are going to be celebrities on a red carpet wearing expensive clothes while people in other parts of the city are suffering and whose livelihoods have been destroyed." ' \
            'Will the show look different? ' \
            'Showrunners say the fires will be a theme that runs throughout the ceremony and the city of Los Angeles will be centre stage. ' \
            'Ben Winston, one of the three executive producers of the show, told the New York Times that the awards will "make LA a character in the night of Grammys" and the show would pay tribute to first responders. ' \
            'A big aim of the show will be fundraising for fire relief efforts. ' \
            'Just days before the show, another big music event in the city raised millions for rebuilding efforts. The FireAid concert, hosted in two LA arenas with more than two dozen musical acts, raised more than $60 million in ticket sales alone. ' \
            'The Grammys will run for a staggering eight hours and hand out 94 awards, recognising everything from best pop album to best choral performance. ' \
            'Beyoncé and Taylor Swift will both be in attendance as they square off in the album of the year category for the first time since 2010 - which Swift won that year. ' \
            'There will also be performances from Charli XCX, Sabrina Carpenter, Benson Boone, Shakira, Stevie Wonder, Teddy Swims and Raye - and an in memoriam tribute to Thriller producer Quincy Jones. ' \
            'Previous tragedies have impacted the Grammys ' \
            'This is not the first time a major disruption has impacted the music industrys biggest night. ' \
            'In 2021, the show was postponed due to Covid-19 and was significantly altered to accommodate safety protocols. It featured a socially distanced format, with no live audience and pre-recorded performances in an intimate outdoor setting rather than the usual large-scale arena production. ' \
            'Artists had to adjust to a new way of promoting their music, relying on digital platforms rather than in-person Grammy week events, which were either cancelled or moved online. ' \
            '"I would not necessarily compare the COVID pandemic to what is happening here," senior music writer for Variety, Steven J Horowitz, told the BBC. "COVID lasted for so long and the effects were devastating for years. People had to cancel major releases, and everything shifted to a digital space." ' \
            'He said the fires are different. ' \
            '"The industry has reacted in real time. It is not as widespread as a worldwide pandemic, so people are a little more flexible on how to properly react and help those affected," he said. ' \
            'Artist Manager Dani Chavez told the BBC that the fires have affected many people working in LAs music industry. ' \
            '"I know multiple musicians who lost their gear", Chavez said. "I know stylists who work in music who lost their houses, who had costumes and whatnot. I know musicians who are born and raised in LA who lost their house." ' \
            'There is also a ripple effect in the industry on those not personally impacted by the fires. ' \
            'The week of events before the show helps new musicians and allows them to break out in a crowded market - getting time with top executives and those at major record labels. ' \
            '"Visibility is very important for artists," Mr Horowitz told the BBC. ' \
            '"Say you are a Best New Artist nominee who is relatively unknown to the public - being on these platforms and at these parties is a really big look if you are trying to get your music out in front of the industry. It really does help." ' \
            'One of the most sought-after parties is Spotifys event honouring the nominees for Best New Artist of the year. It is half party, half concert, with previous nominees showcasing their new music, and celebrities from all parts of the entertainment industry there to celebrate. ' \
            'Following the fires, Spotify chose to cancel this years event. ' \
            '"We have decided that the most impactful approach is cancelling all our Grammy Week events, including our annual Best New Artist party, and redirecting funds to support efforts to reach local fans and charitable organizations," Spotifys Global Head of Music Partnerships and Audience Joe Hadley wrote in an announcement. ' \
            'The music industry and the Grammys are deeply rooted in Los Angeles, and though the city is going through a devastating period, it has reinforced a sense of community, especially in the music industry. ' \
            '"Even if people lost everything, they still have hope. And I think that feeds into what we are going to see in the music industry in the future," Mr Horowitz said. "People are not going to flee Los Angeles because of this one thing. It is not going to stop L.A. from being one of the main hubs for music in the world."'

    text5 = 'Multilingual coreference resolution as text generation ' \
            'This paper presents a multilingual coreference resolution system DFKI-CorefGen submitted for the CRAC Shared Task 2024. We cast the task as text generation and use mT5-base as the pre-trained model. Our system takes the sixth place out of seven in the competition. We analyze the reasons for poor performance and suggest possible improvements. ' \
            'Coreference resolution is an important part of many natural language processing (NLP) tasks like question answering, information extraction, text summarization, etc. CRAC 2024 focuses on multilingual coreference resolution, which is less researched than the English one. It is also more challenging than monolingual coreference resolution, as the training data typically come from different sources and may be characterized by large variability in size, domain, the definition of markables, annotation consistency, completeness and quality. Ideally, a good multilingual coreference resolution system should be able to deal with these challenges without a significant performance loss. ' \
            'Currently, many state-of-the-art (multilingual) coreference resolution systems are modifications of the model first introduced by Lee et al. (2017). They are typically characterized by rather complex architectures based on pre-trained large language models and require careful data preprocessing. One needs to have not only novel ideas, but also very good programming skills and mathematical knowledge to modify such architectures. Additionally, the approach has some inherent limitations, e.g., it is tricky to use to identify discontinuous mentions or split antecedents. ' \
            'On the other hand, one is always searching for easier ways to solve a task. Such a possibility is offered nowadays by large language models (LLMs). They are generative models, which demonstrate excellent performance in many NLP tasks and are relatively easy to use for inference. However, they have their shortcomings too, the most important being a huge number of parameters, so that one needs a lot of computational resources to use them. ' \
            'The aim of this work is to check if we can cast multilingual coreference resolution as a text generation task using a much smaller model, like mT5-base. We try to keep the task as simple as possible. No careful pre-processing is required – the input is the raw text and the output is the same text marked with coreference clusters. ' \
            'To summarize, our contributions are as follows: ' \
            'We investigate how multilingual coreference resolution can be represented as a purely generative end-to-end task and discuss challenges and limitations of the approach. ' \
            'We show that mT5-base is to a certain extent capable of the task but obviously not large enough to achieve good scores and compete with the baseline. ' \
            'One of the seminal and most successful coreference resolution models is the one by Lee et al. (2017). It is a span-based mention-ranking model. Namely, all spans in a document are treated as potential mentions and represented as context-dependent embeddings. These spans are ranked and paired with the most likely antecedent spans. ' \
            'A lot of state-of-the-art coreference resolution models, no matter multilingual or not, inherit this architecture with some modifications. There also exist works casting coreference resolution as a sequence-to-sequence problem. Some early experiments are conducted by Raffel et al. (2020), who apply the T5 model to resolve ambiguous pronouns in different datasets. They focus on separate pronouns and do not build any coreference chains or clusters, as the main goal is to evaluate the model’s commonsense reasoning ability. ' \
            'Some researchers cast coreference resolution as a question-answering task and use LLMs to generate answers. Other generative coreference resolution models have been presented, such as the "link-append" transition system based on mT5-xl, which is multilingual and was successfully tested on multiple languages. ' \
            'Our approach DFKI-CorefGen falls into the latter category but has the following differences. First, it is multilingual. Second, we keep the pre-trained model frozen and do prefix tuning instead. Third, we process the input text incrementally and teach our model to correct clustering mistakes in the previous sentences as well. Fourth, we create training data by corrupting the coreference annotations. ' \
            'We perform multilingual mention identification and coreference resolution jointly and treat the task as text generation. Given a piece of text, we want to find all mentions and group them into clusters by marking them in this text with square brackets and cluster identifiers. The approach is implemented as a prefix tuning using OpenPrompt with mT5-base as the core model. We apply prefix tuning because mT5-base is relatively small and thus not designed for inference in a zero- or few-shot manner. ' \
            'We train one model for all the languages, using the official training data only. It is done on one NVIDIA GeForce GTX TITAN X GPU with 12 GB memory for five epochs with batch size 1, the AdamW optimizer, a learning rate of 5e-5, and a linear schedule with warm-up. ' \
            'As the input length of mT5-base is limited by 1024 sub-tokens, we have to split each document into several pieces. In addition, our initial experiments showed that the model struggles to find the correct clusters if it receives the whole raw piece of text as input, especially if this piece is long. ' \
            'First, we limit the length of each input piece to five sentences that can have various lengths but are no longer than 512 sub-tokens. Second, the task becomes easier if some clusters (not necessarily always correctly marked) are already identified. Therefore, we proceed with the task incrementally, starting with the very first sentence and asking the model to find the clusters there, then adding the second sentence and asking the model to do the same task, revising its initial predictions, and so on. ' \
            'Despite having special training examples aimed at dealing with repetitions, hallucinations, or truncation of text, these errors are still very common. Therefore, after processing a piece, we have to align the generated and gold sequences. Finally, to get clusters for the whole document, we merge clusters found in each piece based on mention overlap. ' \
            'DFKI-CorefGen takes the sixth place out of seven with an average 33.38 F1 score. It is far below the 53.16 F1 score achieved by the baseline. ' \
            'The main reason for this unsatisfactory performance is that mT5-base is simply not large enough for the task. Small model size also causes difficulties in performing the task for longer inputs, and very persistent hallucinations and repetitions in the output. ' \
            'Another important negative factor is a small training data size—due to time constraints and limited computational resources, we take only 2,000 training samples from each dataset. ' \
            'In conclusion, this paper introduces a simple and purely generative end-to-end approach to multilingual coreference resolution. We show that it is capable of the task but suffers from certain limitations, like a small pre-trained model and a lack of training data, preventing it from achieving good scores. We believe that replacing mT5-base with a much larger model can help reach better results and avoid complicated post-processing.'


    text_name = f'text{chosen_text}'

    as_text(globals()[text_name])
    as_clusters(globals()[text_name])