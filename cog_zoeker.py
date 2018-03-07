"""
Deze functie maakt en zoekt COGs door de twogslijst te doorzoeken.
IN de twogs lijst wordt gezocht naar een eiwit uit een ander twog dat dezelfde connecties zou kunnen hebben.
Als dit eiwit 2 of meer gelijke connecties heeft, wordt het erkend als een cog en aan de lijst toegevoegd.
De gebruikte parameters zijn:
    ncf_twogs   dit is de twogslijst die onderzocht wordt
"""
def NewCogFind(ncf_cogs, ncf_twogs, ncf_prots):

    ncf_twogs_gesplit = []
    teller = 0
    ncf_list = []
    for eerste in ncf_twogs:
        eerste = eerste.split()
        ncf_twogs_gesplit.append(eerste)

    for eerste in ncf_twogs_gesplit:
        connectie = [x[0] for x in ncf_twogs_gesplit if x[0] in eerste or x[1] in eerste]
        connectie += [x[1] for x in ncf_twogs_gesplit if x[0] in eerste or x[1] in eerste]

        huidige_org = organismeZoeken(connectie)

        data = Counter(connectie)
        cog = list(set([x for x in data if data[x] >= 2]))

        cog = controleFunctie(cog, huidige_org)

        if eerste in ncf_twogs_gesplit:
            ncf_twogs_gesplit.remove(eerste)
            ncf_twogs.remove(' '.join(eerste))
        if len(cog) >= 3:
            teller += 1
            zinnetje ="%s\t%s\n" % (("0000000000%s" % (teller))[-8:], ', '.join(cog))
            print(zinnetje)
            ncf_list.append(zinnetje)
    VoegToeAanCog(ncf_list)


"""
Deze functie zoekt uit welk organisme vooraan de connectie lijst staat.
De gebruikte parameters zijn:
    oz_connectie    de connectie lijst
De functie keert het huidige organisme terug.
"""
def organismeZoeken(oz_connectie):
    #organisme_lijst = ["cla", "fis", "fla", "fum", "nid", "nig", "ory"]
    organisme_lijst = ["CERS8", "CRYNJ", "EMENI", "9TREE", "9APHY", "PHACH", "PHLGI", "PLEOS", "POSPM", "YEAST", "SERL3"]
    huidige_organismen = []
    for x in organisme_lijst:
        for y in oz_connectie:
            if x in y:
                huidige_organismen.append(x)
    return list(set(huidige_organismen))


"""
Deze functie zoekt of er geen orthologe eiwitten in de connectie voorkomen.
Er wordt een opgeschoonde cog lijst gemaakt.
De gebruikte parameters zijn:
    cf_cog      de originele cog
    cf_huidige_organisme    lijst met organismen
De functie keert een schone cog terug
"""
def controleFunctie(cf_cog, cf_huidige_organisme):
    clean_cog = []
    for x in cf_cog:
        for y in cf_huidige_organisme:
            if y in x:
                clean_cog.append(x)
                cf_huidige_organisme.remove(y)
                break
    return clean_cog
