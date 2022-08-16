#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      33650
#
# Created:     15/08/2022
# Copyright:   (c) 33650 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import mysql.connector
from geopy import Nominatim

def main():
    pass
    #connection à la base
    conn = mysql.connector.connect(host="localhost",user="root",password="Vf5z6qxi.", database="dataengineer")

    #création du curseur
    cursor = conn.cursor()

    #selection du contenu de de la table address
    cursor.execute("""select * from  address""")
    adress = cursor.fetchall()
    #appel de la fonction demandé
    geocoder = Nominatim(user_agent="test")

##    cursor.execute("desc address")
##    myresult = cursor.fetchall()
##    for row in myresult:
##        print(row)
##

    #parcour de la selection
    for ligne in adress:

        #recuperation des données nécéssaire
        adr=(ligne[1]+", "+ligne[2] +" ,"+ligne[3])
        localisation=geocoder.geocode(adr )
        #ignorance des  localisations nons trouvées
        if localisation is not None and localisation.longitude is not None:
            #print(  adr+" : "+str(round(localisation.latitude,2)) +","+str(round(localisation.longitude,2)))
            latitude=round(localisation.latitude,2)
            longitude=round(localisation.longitude,2)

            #mise à jour de la table adress
            cursor.execute("""update address set latitude=(%s),longitude=(%s) where address_id=(%s)""",(latitude,longitude,ligne[0]))
            myresult = cursor.fetchall()

    print(adress)

    conn.close()


if __name__ == '__main__':
    main()
