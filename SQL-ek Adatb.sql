
#MENYIK MUSORT MELYIK CSATORNA

SELECT m.cim, GROUP_CONCAT(DISTINCT tv.nev) as Csatornak  
FROM musorujsag.musorok as m
INNER JOIN musorujsag.kozvetit as k ON k.m_musorid = m.musorid
INNER JOIN tvcsatornak as tv ON tv.csatornaid = k.tv_csatornaid
WHERE m.musorid = ?
GROUP BY m.musorid;

#KIVÁLASZTJA A LEGIDŐSEBB/LEGFIATALABB(MIN/MAX) SZEREPLŐT(KET) Illetve azt is h ha jatszanak valamilyen musorban, ha nem jatszik sehol opcionalisan torolheto az adatbazisunkbol

SELECT sz.nev, m.cim, sz.szuletesiido   
FROM musorok as m
INNER JOIN jatszik as j ON j.musorid = m.musorid
RIGHT JOIN szereplok sz ON sz.szereploid = j.szereploid
WHERE sz.szuletesiido = (SELECT MAX(DATE(szereplok.szuletesiido)) FROM szereplok);


#EGY CSATORNAN HANY DB MUSOR VAN

SELECT tv.csatornaid, tv.nev, COUNT(DISTINCT m.musorid) as MusorDarabszam  
FROM tvcsatornak as tv
INNER JOIN kozvetit as k ON k.tv_csatornaid = tv.csatornaid
INNER JOIN musorok as m ON m.musorid = k.m_musorid
GROUP BY tv.csatornaid;


#Leghosszabb adas(ok)

SELECT m.cim, m.tipus , m.hossz, GROUP_CONCAT(DISTINCT tv.nev) as Musor  
FROM musorujsag.musorok as m
INNER JOIN musorujsag.kozvetit as k ON k.m_musorid = m.musorid
INNER JOIN tvcsatornak as tv ON tv.csatornaid = k.tv_csatornaid
WHERE m.hossz  = (SELECT MAX(musorok.hossz) FROM musorok)
GROUP BY m.musorid;