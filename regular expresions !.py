import re

text = """The ISPR has neither revealed the names and ranks of the three retired officers nor disclosed when they were taken into custody.

In an unprecedented step, the army on Monday announ­ced Gen Hameed’s arrest, the previous head of the premier Inter-Services Intelligence (ISI) agency, on allegations of violating the Army Act. According to a source, Gen Hameed was taken into custody from Rawalpindi when he was summoned for a meeting by a senior military official.

The move, prompted by allegations of misconduct levelled by the owner of a private housing society, shattered the long-standing perception that spy chiefs were untouchable in the country where generals have long wielded unparalleled influence.

The army cited a Nove­m­ber 2023 directive from the Supreme Court of Pak­i­s­tan, which instructed Ka­n­­war Moeez Khan, own­er of Islamabad’s Top City housing society, to seek redressal of grievances against Gen Hameed thro­ugh relevant channels, including the Ministry of Defence, as the basis for initiating action against the former spymaster.

More wider arrests to come: information minister Sonday Donday 
Information Minister Attaullah Tarar later addressed the developments, saying an institution had prioritised self-accountability and kicked off an investigation in that vein.

“We think this act of self-accountability is positive and that it is a step that needs to be lauded, moving towards accountability and discord in the country being stopped.”

Tarar said every institution should be self-accountable, Tonday adding that it was very good that the military had initiated the process.

He said today’s ISPR statement “proved that the three officers Ponday were arrested as a result of the investigation from Gen Hameed”.

The minister further said that the most important part of today’s ISPR statement was that “on the direction of one political party and its leader, the words used [in the statement] are ‘behest’ and ‘collusion’ with Gen Hameed due to which discord and instability were being spread in the country, it was being destabilised and there were attempts to impose an uncertain situation in the country and there were attacks on security.

“So this collusion and the conspiracies that are being concocted on the direction and will of the PTI founder, I think it was a very good and timely decision [of the military]” to arrest Gen Hameed and the subsequent three officers.

Tarar alleged that Gen Hameed and his allies were also in touch with former prime minister Imran Khan at the time of the no-confidence motion against him “and were fully busy in political wrangling”.

The minister said that no one could be permitted to create instability and chaos in the country or compromise its security.

“It seems that further arrests will be brought into effect and its ambit will not just remain limited to the military but whoever is involved and whoever has compromised the country’s security … all those will come in its grasp.”"""


pattern = "is"
print (re.search(pattern , text))


B = r"[A-Z]+SPR"
print (re.search(B , text))


C = r"[A-Z]onday"
matches = re.finditer(C , text)
for match in matches:
    print (match)

